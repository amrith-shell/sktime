# -*- coding: utf-8 -*-
"""Probability Threshold Early Classifier."""

__author__ = ["MatthewMiddlehurst"]
__all__ = ["ProbabilityThresholdEarlyClassifier"]

import copy

import numpy as np
from joblib import Parallel, delayed
from sklearn.utils import check_random_state

from sktime.base._base import _clone_estimator
from sktime.classification.base import BaseClassifier
from sktime.classification.feature_based import Catch22Classifier


class ProbabilityThresholdEarlyClassifier(BaseClassifier):
    """Probability Threshold Early Classifier."""

    _tags = {
        "capability:multivariate": True,
        "capability:multithreading": True,
    }

    def __init__(
        self,
        probability_threshold=0.85,
        consecutive_predictions=1,
        estimator=None,
        classification_points=None,
        n_jobs=1,
        random_state=None,
    ):
        self.probability_threshold = probability_threshold
        self.consecutive_predictions = consecutive_predictions
        self.estimator = estimator
        self.classification_points = classification_points

        self.n_jobs = n_jobs
        self.random_state = random_state

        self._estimators = []
        self._classification_points = []

        super(ProbabilityThresholdEarlyClassifier, self).__init__()

    def _fit(self, X, y):
        _, _, series_length = X.shape

        self._classification_points = (
            copy.deepcopy(self.classification_points)
            if self.classification_points is not None
            else [round(series_length / i) for i in range(1, 21)]
        )
        # remove duplicates
        self._classification_points = list(set(self._classification_points))
        # remove classification points that are less than 3
        self._classification_points = [i for i in self._classification_points if i >= 3]
        # create dictionary of classification point indicies
        self._classification_point_dictionary = {}
        for index, classification_point in enumerate(self.classes_):
            self._classification_point_dictionary[classification_point] = index

        fit = Parallel(n_jobs=self._threads_to_use)(
            delayed(self._fit_estimator)(
                X,
                y,
                i,
            )
            for i in range(len(self._classification_points))
        )

        self._estimators = zip(*fit)

        return self

    def _predict(self, X):
        rng = check_random_state(self.random_state)
        return np.array(
            [
                self.classes_[int(rng.choice(np.flatnonzero(prob == prob.max())))]
                for prob in self._predict_proba(X)
            ]
        )

    def _predict_proba(self, X):
        _, _, series_length = X.shape
        idx = self._classification_point_dictionary.get(series_length, default=-1)
        if idx == -1:
            raise ValueError(
                f"Input series length does not match the classification points produced"
                f" in fit. Current classification points: {self._classification_points}"
            )

        m = getattr(self._estimators[idx], "predict_proba", None)
        if callable(m):
            return self._estimators[idx].predict_proba(X)
        else:
            dists = np.zeros((X.shape[0], self.n_classes_))
            preds = self._estimators[idx].predict(X)
            for i in range(0, X.shape[0]):
                dists[i, self._class_dictionary[preds[i]]] = 1
            return dists

    def decide_prediction_safety(self, X, X_probabilities, state_info):
        """Decide on the safety of an early classification"""
        n_instances, _, series_length = X.shape
        idx = self._classification_point_dictionary.get(series_length, default=-1)

        # If this is the smallest dataset, there should be no state_info, else we
        # should have state info for each, and they should all be the same length
        if state_info is None and idx == 0:
            state_info = [(0, 0, 0) for _ in range(n_instances)]
        elif (
            isinstance(state_info, list)
            and idx > 0
            and not all(si[0] == idx for si in state_info)
        ):
            raise ValueError("All input instances must be of the same length.")
        else:
            raise ValueError(
                "state_info should be None for first time input, and a list of "
                "state_info outputs from the previous decision making for later inputs."
            )

        # if we have the full series, always return true
        if idx == len(self._classification_points) - 1:
            return [True for _ in n_instances]

        # find predicted class for each instance
        rng = check_random_state(self.random_state)
        preds = [
            int(rng.choice(np.flatnonzero(prob == prob.max())))
            for prob in X_probabilities
        ]

        # make a decision based on probability threshold, record consecutive class
        # decisions
        decisions = [
            X_probabilities[i][preds[i]] >= self.probability_threshold
            for i in range(n_instances)
        ]
        new_state_info = [
            (
                # next classification point index
                idx + 1,
                # consecutive predictions, add one if positive decision and same class
                state_info[i][1] + 1 if decisions[i] and preds[i] == state_info[i][2]
                # 0 if the decision is negative, 1 if its positive but different class
                else 1 if decisions[i] else 0,
                # predicted class index
                preds[i],
            )
            for i in range(n_instances)
        ]

        # return the safety decisions and new state information for the instances
        if self.consecutive_predictions < 2:
            return decisions, new_state_info
        else:
            return [
                True
                if decisions[i] and new_state_info[i][1] >= self.consecutive_predictions
                else False
                for i in range(n_instances)
            ], new_state_info

    def _fit_estimator(self, X, y, i):
        rs = 255 if self.random_state == 0 else self.random_state
        rs = None if self.random_state is None else rs * 37 * (i + 1)
        rng = check_random_state(rs)

        estimator = _clone_estimator(
            Catch22Classifier() if self.estimator is None else self.estimator,
            rng,
        )

        estimator.fit(X[:, :, : self._classification_points[i]], y)

        return estimator