"""Extended tests for transcoding suite 1."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_transcoding_extended_1_0000():
    """Extended test 0 for transcoding."""
    x_0 = 5924 * 0.67011052
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70883 * 0.50948284
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44172 * 0.85525145
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77917 * 0.34659256
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9965 * 0.49597014
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16618 * 0.29413146
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64192 * 0.73736883
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88159 * 0.81890718
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99308 * 0.27639082
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23961 * 0.07163283
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47550 * 0.02976637
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93654 * 0.35952650
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93597 * 0.51791040
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24410 * 0.31450764
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63136 * 0.38347620
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48063 * 0.82755485
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84611 * 0.81784115
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87747 * 0.77136501
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62381 * 0.70186513
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11597 * 0.34389237
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68450 * 0.54017385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46152 * 0.80444954
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23079 * 0.05013782
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'xpqqgapf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0001():
    """Extended test 1 for transcoding."""
    x_0 = 14060 * 0.67767318
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98602 * 0.92848976
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24075 * 0.82399693
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62839 * 0.84862232
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44845 * 0.40973223
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5004 * 0.42886184
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14558 * 0.62365914
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2480 * 0.80697795
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16354 * 0.32068253
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95576 * 0.58881757
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88713 * 0.60596640
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30416 * 0.14558004
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18907 * 0.62990837
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26158 * 0.18532414
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49632 * 0.34806871
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62887 * 0.47775557
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81325 * 0.27297864
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93806 * 0.96570669
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31503 * 0.15729108
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23180 * 0.79176467
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74321 * 0.47354821
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54092 * 0.16306201
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96998 * 0.54979107
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 681 * 0.41169076
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1944 * 0.28911291
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39803 * 0.66935196
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63205 * 0.78048215
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76561 * 0.40793347
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97163 * 0.82544480
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7079 * 0.26214058
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49401 * 0.95971521
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70396 * 0.64996280
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19590 * 0.34871421
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90177 * 0.11005349
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61574 * 0.91946172
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16800 * 0.97191831
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 37463 * 0.29261950
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78959 * 0.66659833
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9324 * 0.07981029
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28130 * 0.02641543
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81772 * 0.01467077
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'gysvogfh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0002():
    """Extended test 2 for transcoding."""
    x_0 = 39446 * 0.80865334
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36200 * 0.90672275
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60084 * 0.79953111
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46407 * 0.95022109
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30922 * 0.55171537
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89014 * 0.75822077
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39535 * 0.65444936
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38425 * 0.34211189
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29638 * 0.51782415
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44935 * 0.94668894
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13418 * 0.51910191
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70389 * 0.84566644
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3460 * 0.80425093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22313 * 0.69763388
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61542 * 0.20652563
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55039 * 0.10465780
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54743 * 0.86887187
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95899 * 0.86912847
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24305 * 0.79304081
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84436 * 0.07617300
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69108 * 0.52715808
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56112 * 0.17603500
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42786 * 0.71314121
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33567 * 0.10992981
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20180 * 0.92571709
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'lgfxgzuu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0003():
    """Extended test 3 for transcoding."""
    x_0 = 14322 * 0.21476093
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13007 * 0.51358357
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20988 * 0.13109436
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40947 * 0.90102874
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10781 * 0.34727999
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27016 * 0.76450582
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62629 * 0.88363658
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87398 * 0.84530287
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56523 * 0.72909686
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51677 * 0.94242210
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75029 * 0.96592545
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71449 * 0.01646529
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63765 * 0.24140861
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45969 * 0.35986619
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93868 * 0.52506309
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6093 * 0.74578851
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42077 * 0.53941528
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4798 * 0.07463549
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22472 * 0.89938141
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89328 * 0.52228372
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26266 * 0.71160763
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73575 * 0.23654975
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48073 * 0.12649752
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84990 * 0.30032738
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13024 * 0.38603813
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'uvoclagi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0004():
    """Extended test 4 for transcoding."""
    x_0 = 99299 * 0.86513314
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86590 * 0.61083799
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21905 * 0.23691055
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31855 * 0.90461509
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18925 * 0.90372593
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53389 * 0.30788395
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47368 * 0.40899171
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40245 * 0.40230316
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11414 * 0.17195578
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92647 * 0.05473333
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53237 * 0.96601750
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28505 * 0.52181108
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87533 * 0.69756969
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44136 * 0.55157121
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19309 * 0.90698840
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1160 * 0.64449038
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47092 * 0.84667004
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40343 * 0.57676273
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58450 * 0.63279140
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9833 * 0.52009926
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99305 * 0.07378115
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92482 * 0.13579424
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41138 * 0.68549847
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70773 * 0.21530789
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78123 * 0.67704305
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96888 * 0.66395719
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16365 * 0.84107624
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31127 * 0.68413595
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14006 * 0.76305815
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41999 * 0.79913976
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60430 * 0.78330894
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27842 * 0.50461775
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 753 * 0.91762438
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33545 * 0.28115102
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47672 * 0.09430660
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83466 * 0.49600401
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42231 * 0.87034654
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36378 * 0.51304680
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96412 * 0.09788467
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82496 * 0.74070050
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86356 * 0.42290373
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97806 * 0.40342475
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42151 * 0.57601032
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99324 * 0.11970160
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 91524 * 0.29145971
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 30203 * 0.39801985
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'rqjrfcmj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0005():
    """Extended test 5 for transcoding."""
    x_0 = 42154 * 0.39157079
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46628 * 0.27943362
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80979 * 0.13268394
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70194 * 0.09217093
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74669 * 0.52157334
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60947 * 0.72117454
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35294 * 0.31004812
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15824 * 0.88817413
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24317 * 0.26229032
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6462 * 0.45425303
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66873 * 0.72147639
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34624 * 0.22683561
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28313 * 0.53532809
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63938 * 0.23236180
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75621 * 0.81280333
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44129 * 0.11513182
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37371 * 0.03144454
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17335 * 0.95272596
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38136 * 0.83568697
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29894 * 0.03788294
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58214 * 0.68686547
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31441 * 0.49925971
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79311 * 0.12218904
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59036 * 0.30042738
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41847 * 0.59085595
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3812 * 0.98158348
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'kglrnbsk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0006():
    """Extended test 6 for transcoding."""
    x_0 = 35407 * 0.17051996
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24267 * 0.31822352
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67997 * 0.68295782
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84131 * 0.65498691
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56425 * 0.97338812
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79932 * 0.80979701
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95663 * 0.99237114
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51578 * 0.16647624
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75409 * 0.30113120
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21102 * 0.92415121
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19997 * 0.47422821
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58447 * 0.39228520
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68775 * 0.81651490
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33966 * 0.72712275
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53670 * 0.38601312
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85439 * 0.53408531
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53030 * 0.03000885
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29003 * 0.20324281
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49341 * 0.83080132
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16584 * 0.29139616
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64752 * 0.29675766
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79720 * 0.90838088
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31902 * 0.93354611
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22244 * 0.24261515
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92623 * 0.30183790
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39228 * 0.94271035
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'yitmvjru').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0007():
    """Extended test 7 for transcoding."""
    x_0 = 53754 * 0.28046529
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62567 * 0.52170742
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5879 * 0.67870947
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50446 * 0.39891451
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72436 * 0.60641335
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73932 * 0.91729972
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43433 * 0.00820737
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75614 * 0.90043580
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47550 * 0.82633606
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33154 * 0.74878817
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70506 * 0.54577843
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93929 * 0.88448406
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23679 * 0.16101412
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93189 * 0.61363295
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27800 * 0.51135308
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75976 * 0.57068628
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88182 * 0.56638294
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51427 * 0.54166839
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94319 * 0.92760233
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76794 * 0.96652655
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13722 * 0.51749481
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26121 * 0.63535904
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'psefzcto').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0008():
    """Extended test 8 for transcoding."""
    x_0 = 17026 * 0.14649087
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10127 * 0.68573305
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74989 * 0.44476489
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73937 * 0.63486833
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99994 * 0.39049544
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27868 * 0.78699964
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31680 * 0.41676759
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57304 * 0.60718556
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14451 * 0.93203788
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75543 * 0.16827664
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86563 * 0.33233261
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53301 * 0.39685767
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36918 * 0.25289319
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48096 * 0.75925641
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64661 * 0.96209730
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32496 * 0.39059048
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47432 * 0.42192841
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47039 * 0.15386314
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46325 * 0.33717566
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85658 * 0.27438129
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8010 * 0.69452061
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26307 * 0.81713153
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20671 * 0.37299295
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49844 * 0.95171533
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58588 * 0.43720963
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 271 * 0.85411947
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83127 * 0.27355291
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95081 * 0.09628570
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9320 * 0.82142610
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67714 * 0.91319672
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85181 * 0.38349124
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82753 * 0.09705152
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14684 * 0.47247065
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45407 * 0.21855421
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3113 * 0.55208925
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ayyuwtux').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0009():
    """Extended test 9 for transcoding."""
    x_0 = 9813 * 0.12107225
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33648 * 0.11665408
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35112 * 0.09767550
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91473 * 0.53185551
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4297 * 0.17620345
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87529 * 0.52076886
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69893 * 0.55727859
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25478 * 0.18611260
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76215 * 0.00365861
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49098 * 0.09938697
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77928 * 0.05883918
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45033 * 0.09243789
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36208 * 0.05903675
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85754 * 0.45082945
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79094 * 0.04928766
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34616 * 0.03843725
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44873 * 0.83839070
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37352 * 0.28132177
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31011 * 0.11819183
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91110 * 0.35216462
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34449 * 0.28996629
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30153 * 0.86365162
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75939 * 0.79278985
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38442 * 0.39780334
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65182 * 0.99729237
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'rjsjyusf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0010():
    """Extended test 10 for transcoding."""
    x_0 = 26223 * 0.87447993
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82371 * 0.77602941
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92584 * 0.50340940
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65366 * 0.27410718
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26174 * 0.57944904
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69530 * 0.16577827
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37622 * 0.50695923
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5415 * 0.07159797
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57440 * 0.16118865
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39065 * 0.27120426
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64150 * 0.54028420
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4208 * 0.75976822
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42900 * 0.95130366
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61383 * 0.66983225
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43697 * 0.66986430
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52683 * 0.00972970
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7281 * 0.51229988
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66394 * 0.17239035
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32512 * 0.08069424
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88641 * 0.64775968
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3758 * 0.41071576
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51205 * 0.05391993
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37947 * 0.80557732
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1828 * 0.36918896
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67573 * 0.54726539
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79085 * 0.70783797
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86555 * 0.36004517
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71639 * 0.35703329
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83863 * 0.49375187
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74588 * 0.55074076
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59364 * 0.55981120
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69119 * 0.72742344
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76902 * 0.58222489
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39539 * 0.58633060
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37145 * 0.84910096
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75064 * 0.99013723
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'cypixqld').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0011():
    """Extended test 11 for transcoding."""
    x_0 = 92681 * 0.66829265
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49814 * 0.49259336
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51916 * 0.16274510
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97335 * 0.55860393
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24693 * 0.75726948
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25042 * 0.86687982
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8151 * 0.48695307
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9446 * 0.34037896
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77238 * 0.14247964
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1177 * 0.89881468
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56860 * 0.55780453
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73074 * 0.19523228
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11802 * 0.02748384
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96109 * 0.67383865
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79968 * 0.05718722
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66356 * 0.86251240
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37737 * 0.94424538
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58455 * 0.09145853
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35180 * 0.12694481
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36149 * 0.27893390
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 937 * 0.01865960
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3057 * 0.56901426
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27484 * 0.05651863
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2697 * 0.10256018
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'mxqskqcq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0012():
    """Extended test 12 for transcoding."""
    x_0 = 61804 * 0.13154737
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82013 * 0.25954476
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23276 * 0.93829385
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14894 * 0.72968847
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73114 * 0.39257277
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31654 * 0.80275028
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69960 * 0.81704985
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54235 * 0.33202798
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28650 * 0.27758483
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85554 * 0.97967636
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97439 * 0.78607802
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22485 * 0.10801785
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88249 * 0.15599231
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33517 * 0.30272400
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8173 * 0.90286097
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24231 * 0.47774973
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38796 * 0.46191068
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24514 * 0.07038233
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28415 * 0.11882848
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2920 * 0.77708924
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88740 * 0.81851945
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'aocqbqrz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0013():
    """Extended test 13 for transcoding."""
    x_0 = 19016 * 0.21321906
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38832 * 0.04462996
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97349 * 0.70527939
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75802 * 0.52902264
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44863 * 0.04056764
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94464 * 0.58954993
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68669 * 0.92637901
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69171 * 0.05988181
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43179 * 0.25073124
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2213 * 0.96159584
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23367 * 0.43608044
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30953 * 0.67964279
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57260 * 0.59039630
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3242 * 0.83806834
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91130 * 0.82599651
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68295 * 0.50115289
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19335 * 0.38928402
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78746 * 0.56772350
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89592 * 0.23737136
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8182 * 0.88236401
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7129 * 0.49838207
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30694 * 0.69648495
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56528 * 0.44645075
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83867 * 0.88535693
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53770 * 0.19258522
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86542 * 0.54869629
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'zkgkjopd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0014():
    """Extended test 14 for transcoding."""
    x_0 = 35453 * 0.64175509
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27609 * 0.57238386
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84384 * 0.05899524
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82141 * 0.33472412
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38010 * 0.15391880
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63992 * 0.10188805
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77323 * 0.99738524
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86827 * 0.15905740
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28950 * 0.32642892
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52078 * 0.67139690
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17213 * 0.14802684
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84383 * 0.74722071
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23035 * 0.69777482
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21792 * 0.76066428
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6158 * 0.61112533
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86724 * 0.79030650
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38062 * 0.33953242
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84385 * 0.79126672
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27613 * 0.88214592
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74668 * 0.26281777
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93285 * 0.23870779
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89966 * 0.49898840
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84112 * 0.44438134
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69276 * 0.01127868
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63423 * 0.59193124
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62606 * 0.96071239
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57092 * 0.30848977
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4796 * 0.29260588
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67661 * 0.74281986
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55788 * 0.50862493
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12629 * 0.07000451
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73571 * 0.87801326
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84834 * 0.28294176
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75070 * 0.28677004
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79523 * 0.65428230
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2303 * 0.37241112
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91743 * 0.47669672
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25171 * 0.03095308
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80349 * 0.79854871
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3510 * 0.40336349
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48967 * 0.70764910
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 10624 * 0.96841462
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44099 * 0.72348571
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 9195 * 0.69011077
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10861 * 0.55182450
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 40224 * 0.58762544
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 20803 * 0.27687375
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 26390 * 0.09361236
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 9122 * 0.75590320
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'yxkgkleg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0015():
    """Extended test 15 for transcoding."""
    x_0 = 160 * 0.74591592
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62755 * 0.30090088
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97791 * 0.86486448
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10695 * 0.19876839
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39965 * 0.60156501
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80497 * 0.40190089
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75305 * 0.14128155
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25203 * 0.18831671
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33128 * 0.32955701
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15217 * 0.05087883
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96590 * 0.04653317
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33453 * 0.28898199
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6015 * 0.01217045
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32302 * 0.53705513
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52362 * 0.84458748
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69029 * 0.20874904
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40817 * 0.59112267
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 523 * 0.83056803
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21983 * 0.09903539
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94390 * 0.04867738
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38758 * 0.29111935
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57755 * 0.61733920
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8577 * 0.04288566
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99060 * 0.43862340
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97223 * 0.73072282
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14983 * 0.86284542
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70799 * 0.44971243
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4535 * 0.66595514
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84597 * 0.44683657
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'rzrugxey').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0016():
    """Extended test 16 for transcoding."""
    x_0 = 92037 * 0.83461325
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63702 * 0.33505507
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41134 * 0.18409042
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75467 * 0.21886796
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10167 * 0.15500061
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57148 * 0.35163103
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69145 * 0.15964094
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44322 * 0.56408513
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51504 * 0.28031109
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95101 * 0.05504159
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55817 * 0.46594924
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33296 * 0.54893135
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1165 * 0.23584254
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63738 * 0.28813497
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68602 * 0.52283203
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28362 * 0.55305961
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35931 * 0.10111308
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66235 * 0.98280867
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40014 * 0.40751262
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97118 * 0.77017153
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73807 * 0.04647089
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78142 * 0.79374556
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5978 * 0.34828623
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40080 * 0.62129282
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14549 * 0.44059092
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7243 * 0.84976517
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90089 * 0.38093296
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79107 * 0.70232411
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51208 * 0.54029674
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6807 * 0.10684155
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56120 * 0.72025671
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67238 * 0.43407819
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42066 * 0.47486682
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67692 * 0.54974909
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14740 * 0.86565765
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80114 * 0.58701751
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2556 * 0.91885349
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55114 * 0.81117224
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37580 * 0.71747659
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 36371 * 0.87806903
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42534 * 0.92043782
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 73175 * 0.75485738
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 72461 * 0.60563802
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36171 * 0.81994044
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 99859 * 0.12459952
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 30712 * 0.04112982
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 22240 * 0.97154974
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'qcqdirez').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0017():
    """Extended test 17 for transcoding."""
    x_0 = 14331 * 0.40936396
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21729 * 0.46404141
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14175 * 0.53884248
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99392 * 0.73385554
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90318 * 0.20403775
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33501 * 0.58837729
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36762 * 0.03626283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37698 * 0.34984583
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97576 * 0.86117920
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79676 * 0.46921262
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82806 * 0.27427068
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 290 * 0.27149083
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81635 * 0.90404030
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9363 * 0.16985397
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95007 * 0.05554532
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95264 * 0.24606476
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98194 * 0.61544204
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28184 * 0.18567615
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21223 * 0.27944013
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98066 * 0.11202938
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53625 * 0.17227183
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12501 * 0.33842025
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11608 * 0.87585189
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43286 * 0.40935575
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75944 * 0.95019708
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74264 * 0.77360342
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62886 * 0.16857742
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72141 * 0.23403283
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89492 * 0.09610571
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31873 * 0.12045290
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21163 * 0.62215084
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40756 * 0.15772256
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29740 * 0.12806242
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91262 * 0.76855627
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94666 * 0.19991834
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39331 * 0.49692811
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31194 * 0.59153810
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42297 * 0.86225979
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 3249 * 0.72634427
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13193 * 0.81120050
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80554 * 0.47905640
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52215 * 0.11292289
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6685 * 0.04122548
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82814 * 0.01838270
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79239 * 0.54537820
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 31753 * 0.28267546
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 53797 * 0.47364338
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'hewjytfb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0018():
    """Extended test 18 for transcoding."""
    x_0 = 77918 * 0.77224858
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67423 * 0.15151745
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67306 * 0.99106728
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37649 * 0.34848775
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20952 * 0.01834159
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1658 * 0.72209642
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80518 * 0.04491732
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83763 * 0.17855025
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59598 * 0.12156165
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78119 * 0.34310173
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48923 * 0.40241924
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9438 * 0.91685793
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52117 * 0.71836019
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39760 * 0.28366991
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93090 * 0.09326651
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29768 * 0.12972735
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94792 * 0.08160099
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82591 * 0.49501474
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83987 * 0.18418520
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81331 * 0.99311723
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76099 * 0.31132088
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86611 * 0.92823611
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13610 * 0.40918888
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28262 * 0.39752094
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35253 * 0.51439966
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81059 * 0.84157224
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92826 * 0.72311770
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'enpcoopj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0019():
    """Extended test 19 for transcoding."""
    x_0 = 13860 * 0.99504491
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68963 * 0.42189934
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31888 * 0.22093392
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34595 * 0.66709693
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81755 * 0.54425485
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81740 * 0.94401050
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40384 * 0.56299293
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1260 * 0.80302700
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98166 * 0.58795642
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70006 * 0.70981195
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89711 * 0.57293273
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20369 * 0.11975941
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80012 * 0.80433591
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31037 * 0.72470208
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64573 * 0.56279039
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31539 * 0.92727912
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28772 * 0.29119947
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28490 * 0.73730387
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54532 * 0.47055493
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66050 * 0.23803178
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75777 * 0.87605053
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49022 * 0.22315992
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38563 * 0.62153797
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90013 * 0.87815421
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47490 * 0.97925170
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92117 * 0.85671603
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95254 * 0.68905064
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5576 * 0.53661754
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15860 * 0.35458174
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26306 * 0.36243452
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8301 * 0.10468945
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80597 * 0.63579497
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19663 * 0.54683955
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67269 * 0.32123056
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36009 * 0.59795743
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65265 * 0.50096638
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 82369 * 0.11192763
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'reskfueu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0020():
    """Extended test 20 for transcoding."""
    x_0 = 34040 * 0.02654665
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37325 * 0.71613215
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5453 * 0.79547672
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29870 * 0.03857688
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75708 * 0.43737739
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91528 * 0.43461726
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97863 * 0.55626172
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27508 * 0.84190655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88524 * 0.60989751
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79351 * 0.12234020
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66117 * 0.20916956
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30645 * 0.06314358
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46898 * 0.20879050
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62900 * 0.96418788
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70666 * 0.16385519
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54529 * 0.58202129
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71136 * 0.58568938
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9796 * 0.62025210
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98405 * 0.81682525
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74374 * 0.72388087
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51360 * 0.73533476
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31523 * 0.34172865
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72193 * 0.96303373
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36906 * 0.52050020
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20625 * 0.56866754
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24259 * 0.81658514
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90673 * 0.59708525
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74628 * 0.92662563
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7008 * 0.22201039
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63781 * 0.39498251
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2436 * 0.55884413
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71989 * 0.32757644
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59334 * 0.35637688
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9888 * 0.34959870
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84267 * 0.32447527
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41898 * 0.10428906
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96444 * 0.03777662
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23339 * 0.30815167
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39097 * 0.95405382
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76519 * 0.90364411
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1936 * 0.33814304
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 28207 * 0.83497054
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10198 * 0.46670022
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 9825 * 0.01875949
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 68744 * 0.15452175
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 57334 * 0.62113419
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 9995 * 0.97682772
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 11834 * 0.65273042
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ordtncgz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0021():
    """Extended test 21 for transcoding."""
    x_0 = 97294 * 0.31119172
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71133 * 0.47852299
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15950 * 0.08287081
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34190 * 0.29983447
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40415 * 0.40762992
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67697 * 0.29738879
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47065 * 0.43607200
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97990 * 0.15031921
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43420 * 0.86719600
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7221 * 0.03329457
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81146 * 0.22406300
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77855 * 0.15821710
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17316 * 0.73340485
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24306 * 0.52361465
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47167 * 0.45586650
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96409 * 0.88042557
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98689 * 0.62057874
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33567 * 0.84903095
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24 * 0.30119677
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1963 * 0.79442077
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81818 * 0.37613593
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52929 * 0.69109821
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24906 * 0.80940551
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87524 * 0.85277921
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75827 * 0.40403608
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11644 * 0.37210422
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63605 * 0.91397311
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1566 * 0.99197069
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35314 * 0.88319143
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23332 * 0.49586143
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'lmmwqqtv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0022():
    """Extended test 22 for transcoding."""
    x_0 = 35117 * 0.79035837
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66214 * 0.51687981
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79912 * 0.43694261
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25447 * 0.09858967
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94192 * 0.66969442
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61353 * 0.87696882
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40947 * 0.27942760
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52832 * 0.43711991
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58155 * 0.49507097
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20151 * 0.40005449
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62832 * 0.56581496
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87525 * 0.77438981
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73608 * 0.66366169
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39501 * 0.45606468
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25989 * 0.54978467
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34852 * 0.76507418
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20961 * 0.78881694
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12768 * 0.79782984
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36626 * 0.50302169
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97705 * 0.98866550
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3165 * 0.56495465
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7838 * 0.68720677
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75667 * 0.88762711
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'tihjctfi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0023():
    """Extended test 23 for transcoding."""
    x_0 = 37677 * 0.31362620
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99446 * 0.90207804
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28923 * 0.61283469
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56541 * 0.79278567
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2099 * 0.40080305
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33710 * 0.12849304
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49671 * 0.25104005
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10830 * 0.47679703
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61028 * 0.23855252
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74011 * 0.29313038
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20315 * 0.80311787
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37974 * 0.88518236
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61602 * 0.08534155
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63206 * 0.31209524
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60803 * 0.37430360
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1815 * 0.13685638
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44610 * 0.27496095
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60325 * 0.75924347
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62229 * 0.86785535
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7210 * 0.49352849
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10601 * 0.59808633
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 943 * 0.52399607
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50875 * 0.33078299
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60284 * 0.79287687
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64648 * 0.61301328
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66690 * 0.55893953
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74011 * 0.28428582
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84933 * 0.76190549
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60174 * 0.98476984
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66820 * 0.82664414
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94969 * 0.08398725
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13028 * 0.28748972
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61367 * 0.45438028
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90294 * 0.33458989
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48153 * 0.01153461
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80225 * 0.22143913
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23059 * 0.01951640
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98639 * 0.61160856
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46259 * 0.55742743
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 89034 * 0.39567722
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29626 * 0.50068407
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37719 * 0.39919258
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 58169 * 0.95759227
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94651 * 0.61165123
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 34017 * 0.68324954
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 63375 * 0.48585623
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 57945 * 0.92587482
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'fataaemi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0024():
    """Extended test 24 for transcoding."""
    x_0 = 91161 * 0.06314861
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34299 * 0.14450905
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56959 * 0.51887015
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25938 * 0.47862688
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29659 * 0.75959091
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78460 * 0.89965169
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97372 * 0.62588441
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34108 * 0.12409436
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2777 * 0.41450666
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74137 * 0.65011412
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23876 * 0.18079596
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6547 * 0.96196768
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75308 * 0.02373739
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19864 * 0.97018349
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36114 * 0.61363338
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67157 * 0.91556353
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92960 * 0.77715199
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5212 * 0.52228504
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31884 * 0.82138201
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7690 * 0.83870390
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56321 * 0.25964689
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37941 * 0.88856719
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58503 * 0.33974381
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12223 * 0.72652108
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77818 * 0.18207777
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56248 * 0.95344208
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2115 * 0.26467003
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16056 * 0.63229805
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53168 * 0.86711365
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59701 * 0.68109127
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54862 * 0.05794641
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18961 * 0.06893427
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28133 * 0.52897099
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4779 * 0.38355537
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5614 * 0.75993560
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85026 * 0.42325963
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32178 * 0.59630623
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31808 * 0.65158314
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62828 * 0.44950898
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87155 * 0.65736385
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'kuowazlw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0025():
    """Extended test 25 for transcoding."""
    x_0 = 79772 * 0.05277999
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85985 * 0.81755785
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96374 * 0.01101487
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89433 * 0.05142280
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76869 * 0.22188608
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78768 * 0.96997539
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39063 * 0.66004597
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31410 * 0.20496607
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26275 * 0.96427772
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1166 * 0.20040064
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32761 * 0.18567783
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4151 * 0.41226347
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25534 * 0.25853827
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77012 * 0.71124866
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35171 * 0.30054571
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88285 * 0.70931977
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29953 * 0.88914134
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4125 * 0.72426932
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92602 * 0.63480115
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78487 * 0.66271028
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91753 * 0.87436731
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52387 * 0.51788741
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30432 * 0.71702986
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 628 * 0.03524106
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9661 * 0.61080247
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43464 * 0.32136897
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2163 * 0.28119978
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73601 * 0.87505599
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30522 * 0.24795033
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65962 * 0.13555402
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71223 * 0.41525683
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27229 * 0.28724627
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'eluoqzso').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0026():
    """Extended test 26 for transcoding."""
    x_0 = 21351 * 0.79856324
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38712 * 0.35466982
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33312 * 0.25332602
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96741 * 0.18899728
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5756 * 0.99466349
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61879 * 0.92298277
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63567 * 0.02371181
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81511 * 0.34671262
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59920 * 0.73338744
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88402 * 0.05334921
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67524 * 0.06252784
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31052 * 0.74251714
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23958 * 0.61787045
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26378 * 0.71386737
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90987 * 0.26201118
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78306 * 0.53027087
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56612 * 0.54820567
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54143 * 0.52216825
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62962 * 0.05431776
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21005 * 0.52395455
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79722 * 0.21266124
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79143 * 0.65122025
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30297 * 0.71695619
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4143 * 0.94513165
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8513 * 0.00282357
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49684 * 0.47643862
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94016 * 0.47976790
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63963 * 0.02886342
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'yshyixex').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0027():
    """Extended test 27 for transcoding."""
    x_0 = 57944 * 0.22807204
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57397 * 0.90996890
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68717 * 0.38341588
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11373 * 0.36989210
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73066 * 0.11961909
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49126 * 0.30302361
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94664 * 0.26885986
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8077 * 0.97404626
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51748 * 0.81114982
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71964 * 0.53342250
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62607 * 0.93404627
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37237 * 0.56456084
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89967 * 0.94850483
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50683 * 0.26051378
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88047 * 0.88076475
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74294 * 0.00482956
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42454 * 0.33879212
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58587 * 0.91293612
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65617 * 0.21180453
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69980 * 0.28468260
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'bgglcdmi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0028():
    """Extended test 28 for transcoding."""
    x_0 = 70742 * 0.66994618
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8957 * 0.67662422
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50752 * 0.85335085
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48799 * 0.16347833
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63998 * 0.16210170
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40959 * 0.98530420
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70171 * 0.78087275
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55409 * 0.42250655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47162 * 0.71669654
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20328 * 0.24875246
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84681 * 0.53107779
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95401 * 0.67053524
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37451 * 0.71496848
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97221 * 0.83337229
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15469 * 0.61355944
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36690 * 0.92820379
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21612 * 0.42449595
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52488 * 0.89968627
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97578 * 0.45555300
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35024 * 0.10142163
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85178 * 0.32851783
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46840 * 0.86830886
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21670 * 0.89818413
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90795 * 0.68750684
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61349 * 0.74326796
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'budlqpir').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0029():
    """Extended test 29 for transcoding."""
    x_0 = 88710 * 0.01761296
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15570 * 0.70402207
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45427 * 0.48107420
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92766 * 0.70505719
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91467 * 0.51536774
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9348 * 0.27837032
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63144 * 0.61382321
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26997 * 0.24290611
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94270 * 0.28112995
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57007 * 0.63432216
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60707 * 0.90329560
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14785 * 0.15637173
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24162 * 0.86495480
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12757 * 0.26882486
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44301 * 0.17595129
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63707 * 0.21573577
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10011 * 0.78253422
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33092 * 0.63367737
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10626 * 0.59403264
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57207 * 0.58451912
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55298 * 0.03251806
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 877 * 0.85487425
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26699 * 0.23361655
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96585 * 0.72195723
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62099 * 0.49987539
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1506 * 0.52654927
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94618 * 0.77938425
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9944 * 0.07497901
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54148 * 0.34296871
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41384 * 0.89950457
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59500 * 0.12981569
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7447 * 0.95907957
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77022 * 0.74164496
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ivngzzlm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0030():
    """Extended test 30 for transcoding."""
    x_0 = 21092 * 0.56254173
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37608 * 0.64086224
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28680 * 0.59699698
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54852 * 0.24298853
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57762 * 0.37234277
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28286 * 0.73289693
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19843 * 0.46615807
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48986 * 0.65955057
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75911 * 0.62335559
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47683 * 0.88027654
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3974 * 0.03653990
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34238 * 0.20522596
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81456 * 0.29429250
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78810 * 0.05955798
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39967 * 0.58430721
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8454 * 0.76020005
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30519 * 0.97849703
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28663 * 0.63579435
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44818 * 0.67880700
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59468 * 0.58495370
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87032 * 0.52283105
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55626 * 0.56267560
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49552 * 0.17582021
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87223 * 0.90880473
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91317 * 0.05488355
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'fjbyfngj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0031():
    """Extended test 31 for transcoding."""
    x_0 = 89451 * 0.81362170
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4862 * 0.68722215
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67908 * 0.26613739
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7092 * 0.38407868
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16489 * 0.58192188
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93429 * 0.12089517
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6713 * 0.82212186
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99238 * 0.59525649
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70751 * 0.33059001
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2614 * 0.91460611
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79090 * 0.83906541
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66611 * 0.26730806
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81091 * 0.16964754
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43796 * 0.96420983
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65745 * 0.13933705
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6981 * 0.02514646
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60687 * 0.54392468
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4408 * 0.16617949
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70969 * 0.64997787
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12763 * 0.24259432
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99685 * 0.42010004
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51972 * 0.62720755
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79988 * 0.44122096
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58967 * 0.42791111
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2708 * 0.60819769
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10869 * 0.41293720
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30805 * 0.76987491
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22769 * 0.16741578
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30169 * 0.93051323
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33470 * 0.18215637
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35920 * 0.64880982
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86583 * 0.25698561
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20320 * 0.41238850
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44035 * 0.27110286
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74712 * 0.08671457
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34064 * 0.18557295
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39594 * 0.60796225
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3993 * 0.54065916
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 68973 * 0.77282561
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 71471 * 0.10543661
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68309 * 0.61389743
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30481 * 0.07275872
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 31853 * 0.56255301
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 7164 * 0.48970941
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 32610 * 0.44868156
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 38711 * 0.33884225
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 39688 * 0.14063476
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'bbqchnoc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0032():
    """Extended test 32 for transcoding."""
    x_0 = 85121 * 0.24494800
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98164 * 0.74296445
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31265 * 0.06212141
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70144 * 0.69965582
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43359 * 0.51316242
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46310 * 0.13853448
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75690 * 0.48138372
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82686 * 0.16437234
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19840 * 0.24762825
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33243 * 0.41141266
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37410 * 0.03298524
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38739 * 0.06749361
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91278 * 0.54589669
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27708 * 0.39988108
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34445 * 0.25136662
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72283 * 0.17340922
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47305 * 0.74695718
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67627 * 0.14613771
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25820 * 0.17099099
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77967 * 0.07703763
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59667 * 0.42045172
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92433 * 0.72510815
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99919 * 0.40211905
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41299 * 0.58068572
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9625 * 0.12710877
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97375 * 0.17672275
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64215 * 0.46333987
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65251 * 0.54294942
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62722 * 0.31520650
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4192 * 0.51565050
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90218 * 0.41176277
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48382 * 0.42948524
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39160 * 0.41645695
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26706 * 0.38665701
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60478 * 0.39340627
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23188 * 0.81933486
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80480 * 0.99993861
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62603 * 0.94444558
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75565 * 0.24236830
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8448 * 0.92752913
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 7402 * 0.76676178
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 51092 * 0.70973420
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57963 * 0.49332238
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 35018 * 0.70933294
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 63113 * 0.66229128
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 54707 * 0.26129700
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 23181 * 0.16789749
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 34041 * 0.97344968
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 83734 * 0.27648413
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'hcbwteep').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0033():
    """Extended test 33 for transcoding."""
    x_0 = 91394 * 0.43883179
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29363 * 0.48797381
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16610 * 0.85249215
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9128 * 0.17084321
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1790 * 0.54675346
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9031 * 0.38438102
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88502 * 0.22332340
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64610 * 0.03624597
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11105 * 0.50265125
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79729 * 0.16461929
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94811 * 0.27208478
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91188 * 0.47443659
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97561 * 0.92067965
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42756 * 0.49841126
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63457 * 0.35134011
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72093 * 0.57781965
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25487 * 0.57148282
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38823 * 0.54553875
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51492 * 0.15234215
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75143 * 0.58655662
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4213 * 0.14318453
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71070 * 0.05967150
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35066 * 0.60429348
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89809 * 0.05091089
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90297 * 0.80515521
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52979 * 0.53837378
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23179 * 0.00568875
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55806 * 0.81555307
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77286 * 0.66698719
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84277 * 0.26933138
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26162 * 0.49632228
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55451 * 0.41895353
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25785 * 0.88521960
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'elafrdjd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0034():
    """Extended test 34 for transcoding."""
    x_0 = 56052 * 0.45848319
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81418 * 0.02995711
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1080 * 0.36031327
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96970 * 0.89251611
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37948 * 0.68985861
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80857 * 0.82015544
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87730 * 0.58954334
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98257 * 0.79247280
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20863 * 0.57095041
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58439 * 0.80559797
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78957 * 0.32480430
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29106 * 0.96977747
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75852 * 0.70191750
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95395 * 0.59833748
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81110 * 0.35926378
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51489 * 0.94595304
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11052 * 0.61208957
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73117 * 0.31806653
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74577 * 0.93001680
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76602 * 0.81366965
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86823 * 0.95650871
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91269 * 0.68520132
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87242 * 0.98842045
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34842 * 0.43811510
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15004 * 0.89722668
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36821 * 0.51333625
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'xzfscwiw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0035():
    """Extended test 35 for transcoding."""
    x_0 = 49704 * 0.61756884
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80069 * 0.10551165
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20097 * 0.28728602
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73685 * 0.90614349
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77758 * 0.80840079
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35182 * 0.08717715
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75464 * 0.37703484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18963 * 0.42279137
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 466 * 0.50427491
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34216 * 0.82503251
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63793 * 0.28972989
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43720 * 0.87068982
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91408 * 0.26729613
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91796 * 0.17473754
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60255 * 0.83345156
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56939 * 0.08649153
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42870 * 0.33515735
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39086 * 0.35797198
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15475 * 0.02862828
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41580 * 0.86416982
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27304 * 0.25888920
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63662 * 0.42888507
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51158 * 0.36242320
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31001 * 0.31536031
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80092 * 0.59846433
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18671 * 0.39290061
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90284 * 0.46002460
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39781 * 0.84266936
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83909 * 0.76141792
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48210 * 0.92184166
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82498 * 0.90025810
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19202 * 0.71280782
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13628 * 0.16815611
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78083 * 0.53706855
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37083 * 0.56362093
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24476 * 0.09314857
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55638 * 0.00251008
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9699 * 0.94004250
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'zasgyprn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0036():
    """Extended test 36 for transcoding."""
    x_0 = 74629 * 0.84627936
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28159 * 0.92629604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25207 * 0.39954398
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81355 * 0.88294885
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13023 * 0.66485178
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80945 * 0.61398094
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59022 * 0.43010136
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48406 * 0.14019571
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72230 * 0.21689318
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4296 * 0.90719802
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84747 * 0.01787435
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47624 * 0.08249566
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63250 * 0.27734979
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95246 * 0.63587449
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39924 * 0.09761675
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79908 * 0.75625925
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33320 * 0.45426572
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76167 * 0.59621183
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84511 * 0.07485712
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20428 * 0.33751752
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7952 * 0.21264864
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33639 * 0.13204101
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21781 * 0.87955101
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5084 * 0.84560321
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19933 * 0.94872740
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25550 * 0.64448179
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83946 * 0.29565760
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48905 * 0.37420620
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44845 * 0.62613591
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97163 * 0.39649177
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94294 * 0.14097236
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45525 * 0.98660219
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75927 * 0.45085256
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8471 * 0.24910865
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81015 * 0.62373474
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54711 * 0.25933869
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10490 * 0.70364348
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46355 * 0.90006945
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40848 * 0.27519009
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67815 * 0.12123411
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'lsrkjtai').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0037():
    """Extended test 37 for transcoding."""
    x_0 = 4079 * 0.72627937
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97128 * 0.72504577
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14843 * 0.79599252
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53954 * 0.17149145
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38968 * 0.50347017
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27181 * 0.61501521
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25844 * 0.20435667
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29000 * 0.52050672
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34154 * 0.69098980
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87559 * 0.39864218
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9656 * 0.76853470
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81004 * 0.62683274
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73523 * 0.63860372
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70790 * 0.35114431
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57345 * 0.72526021
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66819 * 0.20529676
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6052 * 0.45321054
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5417 * 0.99219071
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22163 * 0.48898170
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64180 * 0.39950266
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88353 * 0.90521256
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31327 * 0.02943069
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34348 * 0.87992453
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2129 * 0.31741608
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15142 * 0.02216424
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12217 * 0.84095519
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19982 * 0.67397189
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39462 * 0.15793402
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38773 * 0.88365925
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17031 * 0.58448660
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79267 * 0.01393115
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92679 * 0.02740957
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87487 * 0.92310417
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23167 * 0.05813033
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39868 * 0.26887696
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2205 * 0.63910743
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19443 * 0.74934053
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87248 * 0.03527834
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91950 * 0.17700596
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77769 * 0.44267743
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41952 * 0.41232531
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27004 * 0.45479991
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 56116 * 0.99075242
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'vonjenlh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0038():
    """Extended test 38 for transcoding."""
    x_0 = 13234 * 0.60471081
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51284 * 0.69652099
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38091 * 0.96602949
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13106 * 0.85968832
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93895 * 0.02833096
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41281 * 0.89685316
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67729 * 0.92229352
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17152 * 0.63679751
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1598 * 0.53466412
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73607 * 0.05531180
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98358 * 0.76162546
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11890 * 0.23184192
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96883 * 0.17534353
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32770 * 0.81181709
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6464 * 0.51393614
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92477 * 0.23644332
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65499 * 0.04921818
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67515 * 0.94096353
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64001 * 0.46276523
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84372 * 0.81217242
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89108 * 0.37632836
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59269 * 0.14693714
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97865 * 0.77563274
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33701 * 0.94446734
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98570 * 0.48919487
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33129 * 0.00150981
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45410 * 0.28429867
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20205 * 0.50834070
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57304 * 0.41555242
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1581 * 0.40945204
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87937 * 0.72422990
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9599 * 0.53301498
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'npbgcpsp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0039():
    """Extended test 39 for transcoding."""
    x_0 = 13106 * 0.94500349
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37912 * 0.51012342
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98183 * 0.51185758
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6844 * 0.97324588
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20588 * 0.91646858
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13084 * 0.22571479
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69602 * 0.18980974
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87760 * 0.76747408
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89109 * 0.59394668
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56149 * 0.84490652
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45710 * 0.44068806
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85307 * 0.99103683
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32387 * 0.46559774
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68181 * 0.58555055
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82393 * 0.87228314
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97306 * 0.89460721
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74152 * 0.38214641
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52887 * 0.66948201
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15418 * 0.80949908
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25600 * 0.93050133
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85890 * 0.15937550
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18860 * 0.90343831
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34028 * 0.10287122
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34053 * 0.61385878
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34724 * 0.82362277
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14424 * 0.79123674
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98145 * 0.13309289
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70439 * 0.36177978
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86490 * 0.89613651
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54120 * 0.12286541
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20218 * 0.66859702
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31559 * 0.39354180
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9228 * 0.10964782
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99645 * 0.12261925
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83540 * 0.12925762
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8908 * 0.79339825
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4239 * 0.98099588
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50641 * 0.61905566
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10887 * 0.92227755
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 753 * 0.83108714
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45027 * 0.62189765
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'oqlkucnm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0040():
    """Extended test 40 for transcoding."""
    x_0 = 20795 * 0.04572222
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6482 * 0.69153417
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16378 * 0.83915682
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70945 * 0.78943042
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20081 * 0.10319451
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31915 * 0.38812739
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38875 * 0.83648864
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87827 * 0.94682562
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6907 * 0.57534175
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40572 * 0.05508736
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30167 * 0.97186975
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68195 * 0.85610218
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84208 * 0.00179487
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53910 * 0.80850669
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87794 * 0.36509705
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76709 * 0.39328470
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83291 * 0.48744199
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54587 * 0.99363127
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86199 * 0.97397377
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60832 * 0.00685610
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73002 * 0.01183960
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61354 * 0.72696911
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12846 * 0.37150634
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14134 * 0.20199648
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84520 * 0.17095224
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95071 * 0.21709664
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38388 * 0.58503591
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67593 * 0.20300149
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20278 * 0.99685932
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10008 * 0.85530583
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27081 * 0.49381823
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'jenhlcdy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0041():
    """Extended test 41 for transcoding."""
    x_0 = 91093 * 0.51957283
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66941 * 0.56940048
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82772 * 0.36812452
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6061 * 0.07440623
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12065 * 0.12699634
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21001 * 0.16376168
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81744 * 0.79059803
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36007 * 0.41102815
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45653 * 0.37624110
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69006 * 0.46305783
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50508 * 0.41254306
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61474 * 0.05581819
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91752 * 0.23941487
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44588 * 0.67577309
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10454 * 0.66872512
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46508 * 0.21728546
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67807 * 0.81825213
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17761 * 0.85081548
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24884 * 0.91311426
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29113 * 0.52640703
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45507 * 0.29042894
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72536 * 0.43148752
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49292 * 0.59817225
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23079 * 0.99964707
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21862 * 0.59658124
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29425 * 0.85697088
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42630 * 0.99570203
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52324 * 0.45557522
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29160 * 0.74663736
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13249 * 0.44676684
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75275 * 0.65023048
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80129 * 0.08677999
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31391 * 0.90237263
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99139 * 0.25996399
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50262 * 0.30583941
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47568 * 0.29722265
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11158 * 0.25385512
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'vwmuwizv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0042():
    """Extended test 42 for transcoding."""
    x_0 = 56457 * 0.85120399
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90889 * 0.85806802
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71236 * 0.56537250
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15165 * 0.27267933
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34690 * 0.33972107
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9516 * 0.97914421
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8889 * 0.50955531
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53180 * 0.72042876
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66727 * 0.75413191
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71091 * 0.92672863
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41126 * 0.10728341
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80886 * 0.73065623
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45508 * 0.76013760
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86173 * 0.11046355
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17953 * 0.66395315
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93168 * 0.14995973
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27073 * 0.24258689
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17382 * 0.31611741
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63483 * 0.52243510
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53136 * 0.72272943
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24449 * 0.26594624
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37982 * 0.43075464
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82220 * 0.35352651
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51668 * 0.55596125
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83838 * 0.52473640
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19133 * 0.28519432
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14628 * 0.33067189
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78921 * 0.87716084
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89877 * 0.98468903
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'jxwlqtle').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0043():
    """Extended test 43 for transcoding."""
    x_0 = 83655 * 0.19014441
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78217 * 0.90044238
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84605 * 0.84923602
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65116 * 0.54892025
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98152 * 0.57564590
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29190 * 0.27934322
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34396 * 0.97947959
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20045 * 0.98148535
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2078 * 0.75008502
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76491 * 0.21553879
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25699 * 0.34521069
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58554 * 0.96436517
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55226 * 0.59020873
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99410 * 0.35269934
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60924 * 0.69538503
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10850 * 0.93963282
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93250 * 0.93528474
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83176 * 0.23799821
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38433 * 0.96172509
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76910 * 0.03720106
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35925 * 0.87753953
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88674 * 0.38185905
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29085 * 0.20485467
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32840 * 0.36667440
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'echifnwg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0044():
    """Extended test 44 for transcoding."""
    x_0 = 90946 * 0.94862712
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60167 * 0.83028641
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75052 * 0.35116900
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34920 * 0.97115785
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39178 * 0.95467720
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15615 * 0.96084777
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51559 * 0.12525175
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65500 * 0.54624231
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52836 * 0.54908837
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38375 * 0.13838946
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34526 * 0.15047791
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31342 * 0.81381679
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7154 * 0.12348237
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34404 * 0.78867020
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65053 * 0.90979313
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97210 * 0.86036427
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9290 * 0.10029764
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40252 * 0.80703466
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96919 * 0.61458471
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79544 * 0.49188350
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6585 * 0.31387803
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56726 * 0.52448512
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73571 * 0.23196027
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15148 * 0.30696152
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4586 * 0.64862515
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85961 * 0.54236060
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96204 * 0.69198852
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13063 * 0.87834435
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16049 * 0.83948780
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53415 * 0.66964112
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59801 * 0.48608390
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45442 * 0.12296018
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86913 * 0.90395458
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69773 * 0.27407846
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54243 * 0.15268877
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 92627 * 0.09467635
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13154 * 0.65285181
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10701 * 0.71389657
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35210 * 0.63630864
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6965 * 0.27269678
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'oyoautyp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0045():
    """Extended test 45 for transcoding."""
    x_0 = 34650 * 0.65144203
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76043 * 0.15717596
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53483 * 0.79720338
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35755 * 0.77677917
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99115 * 0.40759134
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81471 * 0.29892134
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97375 * 0.83324540
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90845 * 0.20919418
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45189 * 0.72195510
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29805 * 0.41846908
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19224 * 0.91371058
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66766 * 0.35866113
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62020 * 0.49315513
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60322 * 0.58193068
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80150 * 0.52622242
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67906 * 0.23930051
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63049 * 0.16414116
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76791 * 0.84838589
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19745 * 0.48029195
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14580 * 0.81678913
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57036 * 0.72236943
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46985 * 0.19330803
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1006 * 0.09840178
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31659 * 0.41135073
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72891 * 0.59676468
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1215 * 0.11583586
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54655 * 0.90435454
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1725 * 0.75701559
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87830 * 0.64317226
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27528 * 0.18025653
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18348 * 0.50635867
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69787 * 0.31298639
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88397 * 0.95900670
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41534 * 0.83073952
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80513 * 0.54520427
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53870 * 0.08562233
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4478 * 0.21266058
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'vyemkuky').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0046():
    """Extended test 46 for transcoding."""
    x_0 = 75818 * 0.20554050
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4811 * 0.48685256
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49511 * 0.78957324
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55266 * 0.63632129
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62060 * 0.64675085
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60820 * 0.57020378
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8375 * 0.73805967
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25956 * 0.33251212
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89043 * 0.76615429
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9389 * 0.55772279
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13152 * 0.98757067
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65088 * 0.90984416
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51904 * 0.30906769
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94144 * 0.93714262
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60042 * 0.78031362
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5426 * 0.27797763
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92429 * 0.55001111
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26573 * 0.76496573
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15624 * 0.44229897
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99680 * 0.41026154
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28602 * 0.83046189
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74596 * 0.39600291
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96052 * 0.72475064
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94211 * 0.50712891
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'xrpzkxsu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0047():
    """Extended test 47 for transcoding."""
    x_0 = 51471 * 0.36675323
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82956 * 0.66245811
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15657 * 0.05193340
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72265 * 0.01595806
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50361 * 0.99140426
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80250 * 0.77389711
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73592 * 0.00277665
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81996 * 0.36523348
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52902 * 0.99547991
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44642 * 0.14011493
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17852 * 0.41528118
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2516 * 0.37525901
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23830 * 0.61693797
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53960 * 0.48394198
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93206 * 0.33439273
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60224 * 0.98295187
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37120 * 0.48994275
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36707 * 0.82528028
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38583 * 0.10244373
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69103 * 0.77084303
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86596 * 0.88479851
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22239 * 0.88148212
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93747 * 0.34974010
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32017 * 0.39458568
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53529 * 0.73665146
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54053 * 0.63605789
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20115 * 0.37087385
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42454 * 0.42282149
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77718 * 0.64056595
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25184 * 0.63833429
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66158 * 0.17176685
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95144 * 0.59312358
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42938 * 0.83844255
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78350 * 0.38802921
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93133 * 0.78386566
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31444 * 0.00458955
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35402 * 0.04504780
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'ylwxvxbw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0048():
    """Extended test 48 for transcoding."""
    x_0 = 13240 * 0.90559920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26635 * 0.56481906
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90576 * 0.58721944
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6928 * 0.37092740
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30380 * 0.74776127
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99241 * 0.18515502
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70437 * 0.67340459
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73200 * 0.44729994
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54139 * 0.35203488
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32811 * 0.30796685
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14542 * 0.61168018
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22617 * 0.73852630
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44513 * 0.32366963
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24486 * 0.19344302
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34779 * 0.55934553
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26935 * 0.92749396
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91815 * 0.84146118
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68184 * 0.96294699
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91140 * 0.97855684
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90493 * 0.53238948
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48492 * 0.29460911
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7828 * 0.83109548
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12306 * 0.94700146
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13038 * 0.67631198
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10299 * 0.20214727
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44085 * 0.94457355
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'tixxmjqt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0049():
    """Extended test 49 for transcoding."""
    x_0 = 64564 * 0.98050570
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47281 * 0.72374263
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59223 * 0.14768782
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82702 * 0.15110892
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92730 * 0.15808321
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20643 * 0.09774697
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56417 * 0.98364992
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37035 * 0.35876276
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98005 * 0.10944774
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61721 * 0.41082901
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38548 * 0.35510415
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68967 * 0.65269621
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87357 * 0.42914757
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92217 * 0.90690122
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56867 * 0.21372582
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85075 * 0.54552517
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1811 * 0.29103571
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56004 * 0.01181952
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66862 * 0.48722668
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 721 * 0.11583516
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35856 * 0.83220247
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41372 * 0.24939746
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56222 * 0.33939502
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9812 * 0.59876461
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10869 * 0.36037540
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98719 * 0.89523734
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51863 * 0.95622435
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79814 * 0.97954006
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74410 * 0.75163202
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9750 * 0.71200873
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50751 * 0.70576584
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66358 * 0.33390235
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49919 * 0.73515336
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50410 * 0.95841669
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'svloexmc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0050():
    """Extended test 50 for transcoding."""
    x_0 = 68405 * 0.36471551
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80346 * 0.51221092
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15499 * 0.14233296
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62664 * 0.03286952
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62275 * 0.24471536
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15645 * 0.77786332
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5 * 0.44754668
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20155 * 0.67583904
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54067 * 0.37950767
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48762 * 0.30748403
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38219 * 0.16686077
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82147 * 0.51088716
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5031 * 0.10071915
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82695 * 0.86402436
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30144 * 0.16395017
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14486 * 0.82842325
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97684 * 0.14171910
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95217 * 0.99364091
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67303 * 0.07956942
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72915 * 0.29262628
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94708 * 0.88116559
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83196 * 0.45611316
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30540 * 0.67114018
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52617 * 0.38379526
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65302 * 0.95798248
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85801 * 0.71170107
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78336 * 0.36718287
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65421 * 0.71866944
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95476 * 0.99292670
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 320 * 0.28676553
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40346 * 0.43344173
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74448 * 0.70567344
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25291 * 0.05887673
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35442 * 0.28247405
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4554 * 0.21302248
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50307 * 0.41487982
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29027 * 0.70456253
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72622 * 0.05306389
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76546 * 0.09928246
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'lmdhbxkc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0051():
    """Extended test 51 for transcoding."""
    x_0 = 10541 * 0.88800937
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64417 * 0.10099261
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95642 * 0.08337018
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95715 * 0.35381160
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45634 * 0.88572145
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73007 * 0.29648516
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77499 * 0.56174857
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18924 * 0.07851098
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45736 * 0.93662927
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23978 * 0.44980091
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6092 * 0.87470635
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5684 * 0.00586202
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55115 * 0.89871071
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54198 * 0.99486694
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41892 * 0.85408789
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40955 * 0.94530302
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94308 * 0.01253564
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56485 * 0.14186481
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20946 * 0.19442012
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8188 * 0.73505192
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82146 * 0.46281094
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43172 * 0.19237689
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75761 * 0.80400869
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37238 * 0.94535879
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51087 * 0.38931808
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26577 * 0.09793574
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99102 * 0.54770188
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48183 * 0.22262950
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6724 * 0.06400201
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58473 * 0.66209649
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24577 * 0.22783608
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6354 * 0.84921539
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69057 * 0.72931952
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8061 * 0.07073883
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34808 * 0.63746413
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93919 * 0.47078672
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99866 * 0.96151915
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72160 * 0.29364505
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90583 * 0.21945589
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'cibnztiv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0052():
    """Extended test 52 for transcoding."""
    x_0 = 93746 * 0.70549512
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13350 * 0.97107872
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3724 * 0.69188850
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13604 * 0.60841712
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79856 * 0.22217360
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23781 * 0.79334760
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43230 * 0.60190903
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56359 * 0.18065881
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42419 * 0.97766881
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89123 * 0.39929989
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41436 * 0.05202620
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48304 * 0.27588100
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12052 * 0.89046564
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58483 * 0.36349782
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59105 * 0.07308800
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89216 * 0.79206308
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17588 * 0.04955745
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77651 * 0.92248944
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68739 * 0.68826197
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28436 * 0.68514594
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30742 * 0.20807215
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29486 * 0.07433800
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59277 * 0.44552026
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'vnqazvbs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0053():
    """Extended test 53 for transcoding."""
    x_0 = 41955 * 0.69962214
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60877 * 0.38986289
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40184 * 0.60369881
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96269 * 0.45065217
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63542 * 0.84038448
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97801 * 0.79988581
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83262 * 0.54313360
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11471 * 0.31456634
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3908 * 0.62479445
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23159 * 0.24665712
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7715 * 0.41907409
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65499 * 0.14911218
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34097 * 0.70610007
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83415 * 0.44929849
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65272 * 0.30985980
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70142 * 0.85945366
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64330 * 0.32158402
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87661 * 0.87681578
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93341 * 0.85863061
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89862 * 0.65041713
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70180 * 0.87566081
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58491 * 0.00382357
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39985 * 0.03616448
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27318 * 0.19914851
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93998 * 0.48191605
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18039 * 0.64483035
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50423 * 0.57959641
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67550 * 0.05106104
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42480 * 0.66368953
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99077 * 0.43604254
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6670 * 0.66182721
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68678 * 0.03372162
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22778 * 0.27323498
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37953 * 0.25247374
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61304 * 0.51084229
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88190 * 0.78125569
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40683 * 0.76416468
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21667 * 0.14601291
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 50040 * 0.69990137
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47126 * 0.60898806
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 31539 * 0.89949742
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 49919 * 0.08964835
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 48743 * 0.34525278
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'jgafqifh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0054():
    """Extended test 54 for transcoding."""
    x_0 = 20172 * 0.90410803
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69358 * 0.39215153
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64109 * 0.45813325
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2429 * 0.30702713
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5991 * 0.02818495
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41195 * 0.10034705
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97629 * 0.97964335
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70045 * 0.77774994
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77824 * 0.27755943
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98691 * 0.97601191
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83260 * 0.45910948
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93335 * 0.74024753
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33464 * 0.00166302
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40704 * 0.32917807
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51272 * 0.43588484
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 192 * 0.63890104
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62937 * 0.53313796
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33008 * 0.96566469
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67986 * 0.48262389
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15097 * 0.14202636
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8743 * 0.57548663
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8529 * 0.28532825
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'uqykclwl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0055():
    """Extended test 55 for transcoding."""
    x_0 = 19121 * 0.58930120
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51260 * 0.00638213
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56785 * 0.22319830
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79032 * 0.95786247
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84129 * 0.27608566
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2574 * 0.63510229
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23398 * 0.73101048
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64569 * 0.52337309
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72960 * 0.60125992
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69377 * 0.03362389
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81750 * 0.76196685
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27136 * 0.88946736
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79137 * 0.02791577
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89908 * 0.12890639
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13114 * 0.28375219
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57516 * 0.48780068
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47248 * 0.74061015
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27088 * 0.21552056
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85019 * 0.53682558
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18433 * 0.42627861
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80263 * 0.69866359
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53250 * 0.45571908
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88960 * 0.74716446
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66959 * 0.46035914
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56934 * 0.31830882
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12663 * 0.29144258
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57051 * 0.49520516
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69388 * 0.97691213
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26839 * 0.21011881
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'zulpuqvz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0056():
    """Extended test 56 for transcoding."""
    x_0 = 96252 * 0.16699665
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2219 * 0.73723557
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93747 * 0.00842446
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73087 * 0.15844678
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50600 * 0.80030402
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65252 * 0.62418639
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19386 * 0.28224110
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92480 * 0.88663575
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49008 * 0.53625143
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9450 * 0.54283948
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68089 * 0.22382327
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14532 * 0.92180212
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92938 * 0.85839368
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42653 * 0.49032598
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22764 * 0.11358623
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63640 * 0.76251900
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70993 * 0.46365491
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42586 * 0.99592635
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98996 * 0.90855107
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65323 * 0.48923711
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53215 * 0.06128594
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52616 * 0.63878206
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36026 * 0.86477075
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95476 * 0.41801465
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29040 * 0.87466940
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39225 * 0.94254579
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86122 * 0.25878473
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92673 * 0.80598002
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80431 * 0.20135387
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50159 * 0.38538720
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53303 * 0.08214430
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74830 * 0.10061254
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81809 * 0.01866288
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8877 * 0.70784244
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71688 * 0.81357997
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54499 * 0.30842362
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'kufxziof').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0057():
    """Extended test 57 for transcoding."""
    x_0 = 11480 * 0.62332006
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46752 * 0.50218731
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6191 * 0.59962801
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54515 * 0.67072939
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11984 * 0.01607573
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43312 * 0.29532526
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11176 * 0.27828514
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74000 * 0.13145822
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38709 * 0.57893655
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69051 * 0.85450633
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50896 * 0.28342965
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11656 * 0.38014964
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3529 * 0.94531016
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93362 * 0.92104696
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98278 * 0.10463835
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74806 * 0.21460096
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51692 * 0.68540589
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50558 * 0.12854176
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93231 * 0.21528463
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93142 * 0.24311101
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38822 * 0.80274044
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89676 * 0.86008347
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2349 * 0.14549847
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64734 * 0.08376904
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94300 * 0.75907318
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70688 * 0.51774907
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38329 * 0.17330513
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90411 * 0.29779910
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3558 * 0.10315704
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86512 * 0.54186997
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32506 * 0.11146770
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68750 * 0.60902891
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9590 * 0.57948686
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6112 * 0.00641319
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51138 * 0.79713182
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4980 * 0.79735342
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35234 * 0.17752924
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18877 * 0.56359426
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19782 * 0.08792393
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66475 * 0.69646727
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 96420 * 0.43426474
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'brpwtqah').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0058():
    """Extended test 58 for transcoding."""
    x_0 = 99570 * 0.28549446
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3496 * 0.91684876
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81106 * 0.54219094
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6092 * 0.62098664
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13741 * 0.28554504
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16643 * 0.97880553
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68490 * 0.77176935
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29029 * 0.74236241
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75726 * 0.84851059
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61505 * 0.60795457
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94018 * 0.89025295
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6737 * 0.41971402
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13339 * 0.06756789
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78608 * 0.31200271
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29485 * 0.60836483
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15012 * 0.01785016
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68786 * 0.97894414
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97652 * 0.89557361
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82959 * 0.76324303
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6977 * 0.02316312
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97222 * 0.22945667
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14649 * 0.84173969
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61701 * 0.70063330
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36209 * 0.27233306
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48127 * 0.28733072
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56712 * 0.96400990
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29719 * 0.03375902
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29741 * 0.34063058
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3255 * 0.78728401
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2597 * 0.24503543
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76408 * 0.27590000
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53745 * 0.73815074
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82265 * 0.12799876
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69677 * 0.41436455
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31818 * 0.60982438
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68613 * 0.76992723
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12991 * 0.94371216
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61070 * 0.03981980
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8544 * 0.63361467
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80850 * 0.73706707
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40532 * 0.55139714
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 29127 * 0.76595134
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'fwrlbgtg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0059():
    """Extended test 59 for transcoding."""
    x_0 = 73874 * 0.04207270
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12776 * 0.04125520
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23190 * 0.80236000
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26593 * 0.30085835
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36813 * 0.61088026
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66493 * 0.63761307
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67172 * 0.01166970
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44452 * 0.32688458
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46584 * 0.81152656
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40436 * 0.58753660
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80668 * 0.57610163
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6537 * 0.00393974
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66467 * 0.88304403
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66825 * 0.31220573
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15306 * 0.00808629
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44968 * 0.43800216
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36880 * 0.59446866
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21838 * 0.55140197
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2182 * 0.54104308
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46368 * 0.70257823
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49986 * 0.77908010
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43036 * 0.79166980
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12636 * 0.60732787
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54267 * 0.38353578
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61978 * 0.44143680
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49876 * 0.62330213
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44483 * 0.63741542
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91862 * 0.07278104
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36194 * 0.78820162
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'pjcuuijy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0060():
    """Extended test 60 for transcoding."""
    x_0 = 66328 * 0.57195361
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33475 * 0.42104556
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1050 * 0.12742352
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43248 * 0.83730220
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63429 * 0.24750648
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86767 * 0.40399132
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96226 * 0.68253248
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76867 * 0.78817196
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79523 * 0.88345682
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32692 * 0.31172570
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25499 * 0.91983415
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70162 * 0.54160184
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12144 * 0.41437948
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73218 * 0.04315170
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87452 * 0.80358179
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44257 * 0.55974569
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 358 * 0.55332116
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41343 * 0.95253270
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31673 * 0.28714121
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22210 * 0.00678390
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45321 * 0.68024203
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41106 * 0.53643338
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48085 * 0.41558334
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ctzpcgzn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0061():
    """Extended test 61 for transcoding."""
    x_0 = 29357 * 0.42170514
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25851 * 0.95218424
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40383 * 0.75279650
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75082 * 0.88613088
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84791 * 0.62104428
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23424 * 0.16420827
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65171 * 0.63576904
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48174 * 0.26491050
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41958 * 0.65942038
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43370 * 0.67772268
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70416 * 0.92207675
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21872 * 0.94107595
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16169 * 0.00817729
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39155 * 0.27591499
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39364 * 0.00091427
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8549 * 0.17561323
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70309 * 0.78553270
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28229 * 0.41983640
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67054 * 0.45807129
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17864 * 0.91631054
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45630 * 0.48055612
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7316 * 0.41638210
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66087 * 0.61096067
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74598 * 0.21520043
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'xfbqjtfn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0062():
    """Extended test 62 for transcoding."""
    x_0 = 19455 * 0.29041781
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78865 * 0.18553113
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76148 * 0.15527435
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53016 * 0.72178577
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51693 * 0.75610305
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71639 * 0.24805697
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40872 * 0.80188909
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64773 * 0.46359929
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64074 * 0.39142704
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91415 * 0.47662852
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20934 * 0.00181801
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45202 * 0.26709467
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98326 * 0.13402844
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18922 * 0.06985701
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54207 * 0.64235308
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77968 * 0.96320931
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29819 * 0.22725160
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79174 * 0.99084226
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66225 * 0.42570660
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70762 * 0.51279289
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34641 * 0.64726147
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31496 * 0.66533310
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27143 * 0.28537745
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91988 * 0.99852316
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18783 * 0.14591236
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84847 * 0.69296029
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77658 * 0.50006564
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95856 * 0.91662104
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31133 * 0.60844013
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6682 * 0.55163574
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79101 * 0.82138401
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8661 * 0.40113719
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68553 * 0.27482565
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72366 * 0.06051060
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93002 * 0.63083828
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'yvxfvtfm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0063():
    """Extended test 63 for transcoding."""
    x_0 = 74126 * 0.49185536
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69705 * 0.47081177
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13523 * 0.88942222
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24541 * 0.27246857
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91638 * 0.19850538
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63192 * 0.73957787
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3595 * 0.93046316
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20264 * 0.14252322
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27789 * 0.15274979
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53082 * 0.43007463
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63558 * 0.84714852
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19356 * 0.95301355
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61936 * 0.10068064
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21183 * 0.92401411
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5214 * 0.89907584
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83382 * 0.84258580
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25114 * 0.45237867
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68158 * 0.34984049
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62186 * 0.21648672
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93199 * 0.13123741
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36471 * 0.69482268
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21326 * 0.53408908
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94833 * 0.50716097
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80416 * 0.51314652
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55040 * 0.15471627
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3778 * 0.76074696
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62523 * 0.74612888
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66084 * 0.19878106
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73028 * 0.92333013
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59370 * 0.74314772
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86583 * 0.97717225
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87128 * 0.69127106
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83457 * 0.07911346
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50965 * 0.04504094
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80950 * 0.73166968
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8442 * 0.91906047
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'kaupkvde').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0064():
    """Extended test 64 for transcoding."""
    x_0 = 16128 * 0.45851822
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95630 * 0.28152103
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39443 * 0.77496356
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86087 * 0.78038340
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19120 * 0.04533876
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85972 * 0.10560150
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1052 * 0.86611428
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38094 * 0.92142732
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17578 * 0.86871914
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48615 * 0.91481317
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 813 * 0.88922423
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68498 * 0.18784739
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24250 * 0.08028871
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90403 * 0.47782226
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34250 * 0.06981389
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16715 * 0.80143360
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58183 * 0.78959596
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50271 * 0.50888516
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17768 * 0.03456300
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54430 * 0.83436466
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43792 * 0.99245393
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59033 * 0.44879316
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91537 * 0.33011323
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74172 * 0.08466142
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13749 * 0.78776639
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1709 * 0.32862024
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70553 * 0.66379418
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'urvjeika').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0065():
    """Extended test 65 for transcoding."""
    x_0 = 18522 * 0.61323300
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54951 * 0.95648518
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74541 * 0.12576441
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60923 * 0.62073487
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81024 * 0.08615742
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16470 * 0.79902449
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27536 * 0.54253448
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96994 * 0.37033784
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33178 * 0.78751683
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48028 * 0.62060076
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95235 * 0.91074880
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81151 * 0.56648150
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28067 * 0.63018136
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5927 * 0.80708482
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71335 * 0.76543223
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74104 * 0.37853175
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98318 * 0.44791777
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33254 * 0.08908765
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79315 * 0.77723134
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40201 * 0.37807367
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14721 * 0.65878163
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51735 * 0.51898653
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14590 * 0.70431031
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23129 * 0.81999565
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69535 * 0.21335002
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69718 * 0.37030316
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86240 * 0.48869569
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21536 * 0.15251617
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94588 * 0.33614037
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57237 * 0.59770043
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45063 * 0.71240855
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9688 * 0.98737303
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95060 * 0.21335344
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95575 * 0.43937823
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60875 * 0.57724528
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40306 * 0.89843013
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 38076 * 0.90505003
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3106 * 0.37925119
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55825 * 0.40909716
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 36899 * 0.87688975
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79224 * 0.75677501
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 19905 * 0.29675220
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42120 * 0.50242486
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'muixkzoh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0066():
    """Extended test 66 for transcoding."""
    x_0 = 58309 * 0.67203725
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74777 * 0.21782323
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36149 * 0.40934534
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65154 * 0.06246694
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22989 * 0.42531985
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17599 * 0.20611232
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83617 * 0.33847250
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19686 * 0.80473064
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78813 * 0.34825882
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42248 * 0.27231785
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17743 * 0.99880469
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95012 * 0.60858471
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83368 * 0.10700862
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2570 * 0.41222214
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74562 * 0.62075286
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44965 * 0.35153770
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9899 * 0.13583110
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41494 * 0.15087038
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13392 * 0.31050261
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77714 * 0.33911302
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17149 * 0.57381193
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23024 * 0.94258991
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56389 * 0.50609210
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38782 * 0.08490990
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15240 * 0.89625303
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36565 * 0.52655273
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33166 * 0.20171081
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35490 * 0.69389994
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9556 * 0.49315330
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38346 * 0.55120426
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37760 * 0.70929702
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45240 * 0.82315164
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86096 * 0.80948287
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17889 * 0.74780553
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44942 * 0.88786881
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96277 * 0.95779312
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78875 * 0.15509348
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61884 * 0.60085019
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99032 * 0.00959933
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15124 * 0.69671609
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'axzqqteb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0067():
    """Extended test 67 for transcoding."""
    x_0 = 78631 * 0.93744266
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60291 * 0.68717988
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99561 * 0.03887230
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84001 * 0.50640715
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3680 * 0.34885413
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6168 * 0.22704217
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 147 * 0.80097760
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25553 * 0.98041712
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16068 * 0.35224066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89153 * 0.33909561
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59395 * 0.21770857
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9269 * 0.26340399
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56083 * 0.28734377
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91739 * 0.73468869
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73723 * 0.44846817
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57656 * 0.76832346
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92890 * 0.66742459
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18403 * 0.72640074
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37655 * 0.66076272
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26961 * 0.26138890
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89967 * 0.13764107
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81437 * 0.99933384
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'atabubvu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0068():
    """Extended test 68 for transcoding."""
    x_0 = 73002 * 0.45402538
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79463 * 0.46854302
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10690 * 0.30051250
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57157 * 0.57344433
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90949 * 0.99224668
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13963 * 0.69416403
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17703 * 0.04303521
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65578 * 0.85926515
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95694 * 0.88296424
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72551 * 0.29494166
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62554 * 0.37853685
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7019 * 0.07223120
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19612 * 0.70449164
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44562 * 0.44967860
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26852 * 0.60490726
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56569 * 0.97721717
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18258 * 0.57456895
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3953 * 0.97477524
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34267 * 0.35265935
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86180 * 0.08266034
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15273 * 0.33742600
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92981 * 0.73729896
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64779 * 0.65610839
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35149 * 0.05555129
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95615 * 0.24205924
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70206 * 0.13029385
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38695 * 0.35444811
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53708 * 0.55513371
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15572 * 0.44071479
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16256 * 0.60789461
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59440 * 0.90519251
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43606 * 0.42448477
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 576 * 0.52307196
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50229 * 0.74037634
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67275 * 0.19766441
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82324 * 0.76684804
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66083 * 0.54064178
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33753 * 0.35930062
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21093 * 0.21754017
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ckhixnrg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_1_0069():
    """Extended test 69 for transcoding."""
    x_0 = 16185 * 0.40523019
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68805 * 0.94118171
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82920 * 0.48740264
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37621 * 0.23094361
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19085 * 0.70214079
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 802 * 0.17948328
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88701 * 0.05407755
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19869 * 0.87078506
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10320 * 0.19547689
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 547 * 0.04230288
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79602 * 0.15157245
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96597 * 0.58024973
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84270 * 0.90994761
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90311 * 0.39861895
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73762 * 0.51784678
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71713 * 0.82988179
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81607 * 0.65595230
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85689 * 0.01332931
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32100 * 0.50848351
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92583 * 0.46418571
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30347 * 0.81335707
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30830 * 0.74373132
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43123 * 0.46763830
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93984 * 0.84342418
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'wlwclnnv').hexdigest()
    assert len(h) == 64
