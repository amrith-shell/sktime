# -*- coding: utf-8 -*-
import numpy as np
from numpy import testing

from sktime.datasets import load_gunpoint, load_basic_motions
from sktime.transformations.panel.random_intervals import RandomIntervals


def test_random_intervals_on_gunpoint():
    # load gunpoint data
    X_train, y_train = load_gunpoint(split="train", return_X_y=True)
    indices = np.random.RandomState(0).permutation(10)

    # fit random intervals
    ri = RandomIntervals(n_intervals=3)
    ri.fit(X_train.iloc[indices], y_train[indices])

    # assert transformed data is the same
    data = ri.transform(X_train.iloc[indices])
    testing.assert_array_almost_equal(data, random_intervals_gunpoint_data)


def test_random_intervals_on_basic_motions():
    # load basic motions data
    X_train, y_train = load_basic_motions(split="train", return_X_y=True)
    indices = np.random.RandomState(0).permutation(20)

    # fit random intervals
    ri = RandomIntervals(n_intervals=3)
    ri.fit(X_train.iloc[indices], y_train[indices])

    # assert transformed data is the same
    data = ri.transform(X_train.iloc[indices])
    testing.assert_array_almost_equal(data, random_intervals_basic_motions_data)


random_intervals_gunpoint_data = np.array(
    [
        [
            -0.5340330004692078,
            -0.6583515405654907,
            50.0,
            0.026666666666666734,
            -0.36,
            21.0,
            53.0,
            0.9891347486540218,
            0.04908738521234052,
            0.14031287549910743,
            0.0004932560523963748,
            0.7720925140620327,
            28.0,
            0.2214765100671141,
            34.0,
            1.2532075490830958,
            1.0333333333333334,
            3.003340098266461,
            0.85,
            0.775,
            0.0625,
            0.0,
        ],
        [
            -0.008949995040893555,
            -1.004485011100769,
            77.0,
            -0.18666666666666662,
            0.5466666666666667,
            21.0,
            71.0,
            0.9856024313477253,
            0.04908738521234052,
            0.13407420576778473,
            0.0003505433403922421,
            0.8515090675700048,
            33.0,
            0.2080536912751678,
            26.0,
            1.415882200884052,
            0.6,
            3.527077008825863,
            0.675,
            0.15,
            0.0625,
            47.0,
        ],
        [
            -0.45477402210235596,
            -0.5941169857978821,
            43.0,
            -0.05999999999999994,
            0.3000000000000001,
            18.0,
            48.0,
            0.9897830203618154,
            0.04908738521234052,
            0.16069747492186845,
            -0.00020938216969741563,
            0.7032491208737225,
            24.0,
            0.21476510067114093,
            19.0,
            1.3231592758318387,
            0.5769230769230769,
            3.2211369624886736,
            0.85,
            0.2,
            0.04000000000000001,
            0.0,
        ],
        [
            0.9494199752807617,
            1.075909972190857,
            71.0,
            -0.01333333333333327,
            0.48666666666666675,
            23.0,
            64.0,
            0.9830263343008879,
            0.04908738521234052,
            0.11145162796784516,
            8.572850232464896e-05,
            1.058963848184742,
            31.0,
            0.30201342281879195,
            35.0,
            1.2298893149751353,
            1.3333333333333333,
            5.044065129305102,
            0.775,
            0.15,
            0.0625,
            43.0,
        ],
        [
            -0.5402599573135376,
            -0.6772300004959106,
            46.0,
            0.026666666666666734,
            -0.30666666666666664,
            19.0,
            50.0,
            0.9901767250643734,
            0.04908738521234052,
            0.14268463418853075,
            -6.245959731104885e-05,
            0.7535346860231785,
            26.0,
            0.2483221476510067,
            26.0,
            1.3333730700119033,
            0.7037037037037037,
            3.736262227381728,
            0.825,
            0.775,
            0.04000000000000001,
            0.0,
        ],
        [
            0.6714509725570679,
            0.7845205068588257,
            89.0,
            -0.019999999999999938,
            0.6333333333333334,
            19.0,
            83.0,
            0.982208455624619,
            0.04908738521234052,
            0.13976072683243265,
            0.00026650590367927637,
            0.8168335974002957,
            26.0,
            0.174496644295302,
            29.0,
            1.3158531729493108,
            0.9285714285714286,
            3.3890366309883193,
            0.7,
            0.15,
            0.04000000000000001,
            0.0,
        ],
        [
            0.33238399028778076,
            0.46317198872566223,
            113.0,
            0.18666666666666673,
            -0.7966666666666666,
            19.0,
            106.0,
            0.9748317705206727,
            0.04908738521234052,
            0.14450721853733675,
            0.0005655017923872651,
            0.6543521253348017,
            28.0,
            0.16778523489932887,
            14.0,
            1.4799761177886066,
            0.4,
            3.03779506371995,
            0.8,
            0.5,
            0.0625,
            0.0,
        ],
        [
            -0.5347490310668945,
            -0.6635295152664185,
            49.0,
            -0.019999999999999938,
            0.3366666666666668,
            21.0,
            53.0,
            0.9894573682044566,
            0.04908738521234052,
            0.13483798131609315,
            0.00019436396634169123,
            0.7919401876906283,
            28.0,
            0.24161073825503357,
            33.0,
            1.2963293092153911,
            0.9655172413793104,
            3.9201995337307496,
            0.85,
            0.75,
            0.04000000000000001,
            0.0,
        ],
        [
            -0.5196340084075928,
            -0.6510469913482666,
            47.0,
            0.10000000000000007,
            -0.3266666666666666,
            19.0,
            48.0,
            0.9899716947443201,
            0.04908738521234052,
            0.14680900551692314,
            -2.738106572734594e-05,
            0.7484418959395499,
            26.0,
            0.2214765100671141,
            29.0,
            1.3158470923962604,
            0.6428571428571429,
            2.704906570998835,
            0.85,
            0.15,
            0.08000000000000002,
            0.0,
        ],
        [
            -0.551160991191864,
            -0.6888254880905151,
            49.0,
            -0.053333333333333274,
            0.35333333333333344,
            20.0,
            50.0,
            0.9901896245955241,
            0.04908738521234052,
            0.14099862347379769,
            0.00031279548603681994,
            0.7782319338279381,
            26.0,
            0.2751677852348993,
            30.0,
            1.2532075490830958,
            0.75,
            3.332550873259107,
            0.85,
            0.75,
            0.06666666666666668,
            0.0,
        ],
    ]
)
random_intervals_basic_motions_data = np.array(
    [
        [
            -0.12603044509887695,
            -2.0302743911743164,
            12.0,
            -0.7,
            -0.5499999999999999,
            2.0,
            5.0,
            8.078970274057987,
            0.7547185476397354,
            8.030953449670445,
            44.540463361397016,
            0.15605461522355613,
            1.0,
            0.8914858096828047,
            6.0,
            1.964399110758362,
            1.0,
            0.04679712446031222,
            0.5957446808510638,
            0.7659574468085106,
            0.0026621626156306975,
            7.0,
        ],
        [
            0.7396649718284607,
            0.1444549858570099,
            79.0,
            -0.52,
            -0.3183333333333333,
            2.0,
            6.0,
            0.3634282573860222,
            0.5706408530934585,
            0.7659862168893204,
            -0.920318941141439,
            0.04343773242417128,
            3.0,
            0.5626043405676127,
            7.0,
            1.8629919641528145,
            0.25,
            0.08361295075415102,
            0.8723404255319149,
            0.1702127659574468,
            0.014383736468327253,
            10.0,
        ],
        [
            -0.9049410820007324,
            1.005660057067871,
            8.0,
            -0.755,
            -0.48666666666666664,
            2.0,
            4.0,
            10.932744612478352,
            0.7363107781851077,
            8.357599529522645,
            70.6931550583625,
            0.14977870731176432,
            1.0,
            0.9065108514190318,
            7.0,
            2.00007033238774,
            0.6666666666666666,
            0.041094784485698664,
            0.6170212765957447,
            0.7872340425531915,
            0.006043618427144096,
            8.0,
        ],
        [
            0.19263949990272522,
            0.04344375059008598,
            19.0,
            -0.355,
            -0.36666666666666664,
            2.0,
            4.0,
            0.024642107184348973,
            0.6872233929727672,
            0.2734659555995279,
            0.003161112594296024,
            0.07785794903159358,
            2.0,
            0.6410684474123539,
            7.0,
            1.9920409265055654,
            0.6666666666666666,
            0.7241463486513618,
            0.6170212765957447,
            0.7872340425531915,
            0.008341540196796376,
            8.0,
        ],
        [
            -0.9242509603500366,
            1.2295366525650024,
            17.0,
            -0.765,
            -0.5666666666666667,
            2.0,
            4.0,
            9.663608404545622,
            0.7424467013366504,
            8.595807801855527,
            153.66135166502792,
            0.19204051006487527,
            1.0,
            0.9031719532554258,
            6.0,
            1.9693438493555184,
            0.6666666666666666,
            0.04087988134099288,
            0.6170212765957447,
            0.7659574468085106,
            0.007828085149364915,
            8.0,
        ],
        [
            0.9939271211624146,
            -0.922040581703186,
            9.0,
            -0.77,
            -0.5116666666666666,
            2.0,
            5.0,
            11.382869719351612,
            0.6994952392758523,
            8.023135806110874,
            -29.9843944315622,
            0.20699373944733643,
            1.0,
            0.8864774624373957,
            6.0,
            1.9491564270996997,
            0.6666666666666666,
            0.04377806812272683,
            0.6170212765957447,
            0.7872340425531915,
            0.013509759854549129,
            8.0,
        ],
        [
            0.046059995889663696,
            -0.28826379776000977,
            8.0,
            -0.5316666666666666,
            -0.565,
            2.0,
            5.0,
            0.3238840833136196,
            0.6135923151542565,
            0.7797117441918526,
            0.04641664669963232,
            0.12225668722081758,
            2.0,
            0.6460767946577629,
            6.0,
            1.892292517622323,
            1.0,
            0.18859149478931703,
            0.3617021276595745,
            0.1276595744680851,
            0.013846451688930414,
            9.0,
        ],
        [
            0.012160062789916992,
            -2.1224682331085205,
            11.0,
            -0.7716666666666666,
            -0.49666666666666665,
            2.0,
            4.0,
            18.620768814635415,
            0.6810874698212247,
            9.132455435489714,
            97.36548285838056,
            0.16756995070982156,
            2.0,
            0.8597662771285476,
            6.0,
            1.9705254043909413,
            0.6666666666666666,
            0.05092465090142344,
            0.6382978723404256,
            0.7659574468085106,
            0.005286061799786201,
            8.0,
        ],
        [
            -0.09692030400037766,
            -0.009259849786758423,
            26.0,
            -0.5133333333333333,
            -0.6858333333333333,
            3.0,
            5.0,
            0.041056491939962456,
            0.5706408530934585,
            0.22088812492458434,
            0.00398598554690871,
            0.06944705742142714,
            2.0,
            0.5893155258764607,
            7.0,
            1.8693323843465879,
            0.75,
            0.6017013946518414,
            0.6170212765957447,
            0.7872340425531915,
            0.011035538939687402,
            10.0,
        ],
        [
            0.008406490087509155,
            0.19938664138317108,
            25.0,
            -0.44666666666666666,
            -0.4716666666666666,
            3.0,
            6.0,
            0.22546058767625193,
            0.5338253141842031,
            0.5231453836148842,
            -0.002215470058895813,
            0.10981335242084253,
            2.0,
            0.7545909849749582,
            8.0,
            1.9232645007341582,
            1.0,
            0.3703066576118429,
            0.6595744680851063,
            0.1276595744680851,
            0.0009174852486890062,
            11.0,
        ],
        [
            0.12431000918149948,
            -0.013205096125602722,
            27.0,
            -0.4233333333333333,
            -0.6283333333333333,
            2.0,
            4.0,
            0.02289398177807329,
            0.6749515466696822,
            0.2410044321583942,
            0.001041234040354553,
            0.035762790697329606,
            2.0,
            0.5509181969949917,
            6.0,
            1.9592576936772688,
            0.6666666666666666,
            0.6666597783946031,
            0.6382978723404256,
            0.7872340425531915,
            0.01122025538075638,
            9.0,
        ],
        [
            0.5035299062728882,
            -1.5499299764633179,
            9.0,
            -0.7566666666666666,
            -0.49999999999999994,
            2.0,
            5.0,
            15.897939718108509,
            0.6810874698212247,
            8.474541884671803,
            86.63694135041521,
            0.20429749523219767,
            2.0,
            0.8981636060100167,
            6.0,
            1.9640342424949715,
            0.6666666666666666,
            0.045509744316097264,
            0.5957446808510638,
            0.7659574468085106,
            0.008358374788515442,
            8.0,
        ],
        [
            -0.5781440138816833,
            -0.24315521121025085,
            16.0,
            -0.5616666666666666,
            -0.5425,
            2.0,
            5.0,
            0.19950934085293104,
            0.6013204688511713,
            0.5999862389473237,
            -0.22729932425403832,
            0.05197693475159555,
            2.0,
            0.7245409015025042,
            6.0,
            1.978421854984168,
            0.3333333333333333,
            0.14095702843411778,
            0.8297872340425532,
            0.1276595744680851,
            0.006371892965665852,
            10.0,
        ],
        [
            0.11512099951505661,
            -0.04020300135016441,
            9.0,
            -0.5008333333333332,
            -0.43166666666666664,
            2.0,
            5.0,
            0.09303334283664481,
            0.6258641614573416,
            0.4734833608912293,
            0.01856395183142546,
            0.09946307958242893,
            2.0,
            0.7161936560934892,
            7.0,
            1.9556657265785635,
            1.0,
            0.5542142375560684,
            0.5957446808510638,
            0.7872340425531915,
            0.0015235305505753222,
            9.0,
        ],
        [
            0.8463379144668579,
            -1.3739063739776611,
            9.0,
            -0.79,
            -0.5316666666666666,
            2.0,
            4.0,
            13.734430536255998,
            0.760854470791278,
            8.757506343251935,
            -41.19763367749615,
            0.13857012217820144,
            1.0,
            0.8948247078464107,
            6.0,
            1.9943038788906615,
            0.6666666666666666,
            0.04893213662658496,
            0.6170212765957447,
            0.7872340425531915,
            0.004680016497899885,
            7.0,
        ],
        [
            0.3560640811920166,
            -1.3956140279769897,
            10.0,
            -0.74,
            -0.5125,
            2.0,
            5.0,
            8.532538115865874,
            0.6994952392758523,
            7.3608275274022255,
            -19.73833840623707,
            0.18602289172468586,
            1.0,
            0.8497495826377296,
            6.0,
            1.9358304058211278,
            0.6666666666666666,
            0.047316129017023874,
            0.5957446808510638,
            0.7872340425531915,
            0.006270885415351464,
            8.0,
        ],
        [
            0.09050050377845764,
            -0.033291954547166824,
            17.0,
            -0.5299999999999999,
            -0.3533333333333333,
            2.0,
            5.0,
            0.04565721060627117,
            0.6258641614573416,
            0.31757284727923407,
            -0.002979493015171669,
            0.06969385047426252,
            2.0,
            0.7362270450751253,
            7.0,
            2.012541851676139,
            0.6666666666666666,
            0.6795929164507785,
            0.6382978723404256,
            0.1276595744680851,
            0.0052355580246290076,
            8.0,
        ],
        [
            -0.20884649455547333,
            0.13690856099128723,
            9.0,
            -0.5108333333333333,
            -0.42166666666666663,
            2.0,
            5.0,
            0.15634889612674788,
            0.6320000846088841,
            0.6249898088302414,
            -0.12107029403787448,
            0.10359208088384624,
            2.0,
            0.7011686143572621,
            7.0,
            1.9561050523084529,
            0.6666666666666666,
            0.18322646159929554,
            0.6595744680851063,
            0.1276595744680851,
            0.0022558352903546204,
            9.0,
        ],
        [
            0.42760252952575684,
            -1.8662387132644653,
            8.0,
            -0.7416666666666667,
            -0.5266666666666666,
            2.0,
            4.0,
            12.810612264646405,
            0.7485826244881929,
            9.58698290213626,
            -9.650884858956239,
            0.1707873009867936,
            1.0,
            0.8547579298831386,
            7.0,
            1.9947038119311238,
            0.6666666666666666,
            0.05532697113711143,
            0.6382978723404256,
            0.7872340425531915,
            0.005277644503926668,
            7.0,
        ],
        [
            0.3592264652252197,
            -1.3742399215698242,
            9.0,
            -0.7533333333333333,
            -0.5633333333333334,
            2.0,
            4.0,
            6.471193909211073,
            0.7547185476397354,
            7.2850360070374425,
            -6.396498247426594,
            0.16049203945709742,
            1.0,
            0.8914858096828047,
            6.0,
            1.9844297409817642,
            0.6666666666666666,
            0.04101122017649204,
            0.6382978723404256,
            0.7872340425531915,
            0.007482976019124097,
            7.0,
        ],
    ]
)


# def print_array(array):
#     print('[')
#     for sub_array in array:
#         print('[')
#         for value in sub_array:
#             print(value.astype(str), end='')
#             print(', ')
#         print('],')
#     print(']')
#
# if __name__ == "__main__":
#     X_train, y_train = load_gunpoint(split="train", return_X_y=True)
#     indices = np.random.RandomState(0).permutation(10)
#
#     c22_u = Catch22()
#
#     c22_u.fit(X_train.iloc[indices], y_train[indices])
#     data = c22_u.transform(X_train.iloc[indices])
#     print_array(data.to_numpy())
#
#     c22_s = Catch22()
#
#     data = []
#     for i in range(22):
#         data.append(c22_s._transform_single_feature(X_train.iloc[indices], i))
#     print_array(data)
#
#     X_train, y_train = load_basic_motions(split="train", return_X_y=True)
#     indices = np.random.RandomState(0).permutation(20)
#
#     c22_m = Catch22()
#
#     c22_m.fit(X_train.iloc[indices], y_train[indices])
#     data = c22_m.transform(X_train.iloc[indices])
#     print_array(data.to_numpy())