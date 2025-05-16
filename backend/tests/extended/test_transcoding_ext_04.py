"""Extended tests for transcoding suite 4."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_transcoding_extended_4_0000():
    """Extended test 0 for transcoding."""
    x_0 = 64964 * 0.84199574
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97494 * 0.00371809
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63862 * 0.64270920
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99297 * 0.98225872
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29164 * 0.28921265
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36855 * 0.91647339
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67692 * 0.21912973
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90962 * 0.25231744
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59815 * 0.29465998
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80574 * 0.50071764
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94881 * 0.69398123
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74945 * 0.34234306
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37892 * 0.86909839
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72322 * 0.50285293
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48826 * 0.68065832
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 588 * 0.58111805
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67642 * 0.00439622
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62149 * 0.36236622
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40040 * 0.28933126
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99470 * 0.53437566
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'nyhukhll').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0001():
    """Extended test 1 for transcoding."""
    x_0 = 81690 * 0.01305855
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52219 * 0.08567075
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50437 * 0.73688269
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87125 * 0.64952737
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99546 * 0.64740030
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21028 * 0.58865578
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14219 * 0.45055653
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34176 * 0.69565207
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47130 * 0.05428436
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23890 * 0.45857377
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62981 * 0.96018309
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16236 * 0.89601232
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77096 * 0.53481526
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70770 * 0.76281730
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57224 * 0.21472059
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72710 * 0.26922799
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54104 * 0.07733779
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25719 * 0.20314999
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6682 * 0.41168018
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22949 * 0.82240686
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10224 * 0.49507908
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22043 * 0.53967132
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35314 * 0.15512729
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54694 * 0.02505583
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5858 * 0.18094520
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95638 * 0.24942130
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98676 * 0.61853502
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22587 * 0.52768985
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13165 * 0.22697792
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25262 * 0.00682761
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83083 * 0.48490203
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90989 * 0.14312297
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88974 * 0.13051123
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59005 * 0.56258485
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42842 * 0.35627994
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85841 * 0.02434500
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65133 * 0.64962119
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73186 * 0.15928901
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60122 * 0.74878405
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63404 * 0.73863054
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83647 * 0.48558130
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58670 * 0.95400958
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77126 * 0.83325712
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'jnohvwxw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0002():
    """Extended test 2 for transcoding."""
    x_0 = 70351 * 0.42404548
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12033 * 0.71915789
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47971 * 0.67194619
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12912 * 0.32545210
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55272 * 0.43512396
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86470 * 0.09222472
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4468 * 0.47284763
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82998 * 0.41218905
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 312 * 0.99532736
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13148 * 0.71873278
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84225 * 0.83201173
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86471 * 0.36519209
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74651 * 0.43426300
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12247 * 0.79913332
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95064 * 0.20745691
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57138 * 0.04548279
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29720 * 0.18821413
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90284 * 0.05319148
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85442 * 0.47898291
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27436 * 0.00117838
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60530 * 0.31685846
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98021 * 0.22999069
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78839 * 0.93118612
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'oayhrwks').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0003():
    """Extended test 3 for transcoding."""
    x_0 = 5323 * 0.25258328
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66628 * 0.41519989
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46971 * 0.07835251
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77878 * 0.75947133
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36645 * 0.55563940
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52947 * 0.45821327
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71277 * 0.56789427
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79097 * 0.44587611
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82673 * 0.75307325
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81402 * 0.09795689
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83687 * 0.85229388
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13871 * 0.47415107
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99904 * 0.85690715
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88314 * 0.78220035
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67298 * 0.36591483
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72625 * 0.01753851
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80247 * 0.07780564
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17785 * 0.09576398
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96554 * 0.56456446
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35015 * 0.25908746
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97575 * 0.53419210
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2304 * 0.02057074
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47362 * 0.58511917
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53607 * 0.79647575
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ogumpryw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0004():
    """Extended test 4 for transcoding."""
    x_0 = 92458 * 0.00913135
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17175 * 0.42557102
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78104 * 0.76536610
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23865 * 0.64573051
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96599 * 0.21105721
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57834 * 0.48635908
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36186 * 0.49362284
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62969 * 0.18840206
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9640 * 0.35669754
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54840 * 0.21619298
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73386 * 0.11425535
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91869 * 0.89091653
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32748 * 0.54212115
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68666 * 0.75203937
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3037 * 0.04947051
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2274 * 0.73522192
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67444 * 0.44004843
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92299 * 0.93199701
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31218 * 0.75213197
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30337 * 0.05054250
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72153 * 0.72401211
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41560 * 0.09139591
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69495 * 0.19509767
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22011 * 0.13152605
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69604 * 0.52693335
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79029 * 0.42977049
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20633 * 0.83763159
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18075 * 0.16794754
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97375 * 0.57605688
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'syqlcnaw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0005():
    """Extended test 5 for transcoding."""
    x_0 = 40274 * 0.93599200
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94626 * 0.24334373
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71231 * 0.51823890
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30479 * 0.65670917
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40954 * 0.58242450
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57775 * 0.95291328
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29157 * 0.76065967
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7253 * 0.07472305
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 108 * 0.57298754
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31145 * 0.61368641
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11634 * 0.51309174
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65910 * 0.70083344
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50092 * 0.76515658
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50468 * 0.35023618
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55917 * 0.80650258
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24853 * 0.95087693
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48064 * 0.61615712
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37071 * 0.13155202
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39904 * 0.30810320
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33955 * 0.16641903
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95257 * 0.20861449
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30732 * 0.50328461
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8592 * 0.72032650
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70322 * 0.70331220
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79536 * 0.27996632
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98758 * 0.11147207
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96985 * 0.62184546
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63479 * 0.91769691
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77376 * 0.34786848
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62192 * 0.83536020
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99650 * 0.71649065
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88506 * 0.61338356
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12017 * 0.64011175
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ocxpsnfa').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0006():
    """Extended test 6 for transcoding."""
    x_0 = 85615 * 0.76815445
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11228 * 0.57714252
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30278 * 0.64484161
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66622 * 0.50924172
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60653 * 0.57625847
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88962 * 0.10735406
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10366 * 0.35209069
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21762 * 0.13838732
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20871 * 0.06653031
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98116 * 0.15844666
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3258 * 0.18534575
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41969 * 0.94984351
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85882 * 0.09614669
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5641 * 0.36824676
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85287 * 0.50377137
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45158 * 0.03034527
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29604 * 0.02569460
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51464 * 0.97413548
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27250 * 0.54959732
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33682 * 0.50125147
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50611 * 0.57990280
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87204 * 0.66806722
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86797 * 0.84279444
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56515 * 0.69884534
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55567 * 0.92474579
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15564 * 0.16864393
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60115 * 0.01365379
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31616 * 0.93916516
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26819 * 0.94208049
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1457 * 0.58587967
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18879 * 0.23901542
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27282 * 0.77463956
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5628 * 0.90081651
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84940 * 0.88730488
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65543 * 0.90035717
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22295 * 0.18498479
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ubmzdfyc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0007():
    """Extended test 7 for transcoding."""
    x_0 = 64226 * 0.39659435
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31328 * 0.94510594
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95208 * 0.71937317
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27200 * 0.70702503
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29226 * 0.67768958
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74211 * 0.24049011
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6987 * 0.73437330
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75823 * 0.39142955
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94420 * 0.56461849
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23015 * 0.89735633
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53833 * 0.09363566
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17596 * 0.29784504
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56648 * 0.94538988
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71842 * 0.44864773
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92475 * 0.39199351
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97167 * 0.84385221
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30263 * 0.46243279
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5273 * 0.62899444
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93896 * 0.58204637
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42623 * 0.41093656
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47453 * 0.59073655
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46177 * 0.23497297
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15056 * 0.46053875
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41087 * 0.20592328
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'htbozhzj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0008():
    """Extended test 8 for transcoding."""
    x_0 = 60519 * 0.34988200
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84720 * 0.22946269
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30521 * 0.17474458
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18034 * 0.82726351
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61315 * 0.70621797
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45401 * 0.02532246
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60143 * 0.24485710
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99391 * 0.39478602
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74453 * 0.42080407
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 740 * 0.06686881
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79674 * 0.25807591
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3941 * 0.36907015
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96500 * 0.87628286
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29955 * 0.80480185
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21788 * 0.25408568
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97033 * 0.80799263
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35866 * 0.45466629
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12406 * 0.24225985
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58808 * 0.43671810
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32581 * 0.51321178
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89665 * 0.38761503
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31563 * 0.85292501
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96699 * 0.10816526
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79689 * 0.68925863
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23898 * 0.17718338
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46435 * 0.98030821
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9781 * 0.23789511
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92806 * 0.13685761
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71043 * 0.97098734
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85310 * 0.27233449
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36086 * 0.05494939
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76287 * 0.46156556
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71757 * 0.91014882
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49899 * 0.11096800
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'eoaykdfw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0009():
    """Extended test 9 for transcoding."""
    x_0 = 24390 * 0.30141943
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88654 * 0.39193288
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45188 * 0.19275707
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82015 * 0.85240172
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95423 * 0.53239316
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47616 * 0.95411004
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17809 * 0.00597389
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34462 * 0.01306643
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56560 * 0.96345762
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93452 * 0.01432026
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4834 * 0.08831787
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30703 * 0.87321428
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35543 * 0.56572469
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58420 * 0.86075399
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81694 * 0.29032549
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19098 * 0.57244228
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45311 * 0.91532848
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65497 * 0.61949954
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63660 * 0.58113877
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5459 * 0.74984238
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12524 * 0.95273553
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76245 * 0.33785319
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14896 * 0.93045594
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60410 * 0.13249368
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40769 * 0.11911141
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51670 * 0.02324860
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99713 * 0.03604991
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27517 * 0.23415874
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18812 * 0.34969829
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95391 * 0.26312502
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68614 * 0.87958396
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25169 * 0.75197737
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5651 * 0.38174284
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2910 * 0.58244493
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4563 * 0.34944850
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81061 * 0.74260673
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73651 * 0.77029755
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59370 * 0.11712478
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'bnonvuhk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0010():
    """Extended test 10 for transcoding."""
    x_0 = 52243 * 0.11396350
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83320 * 0.20339603
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4461 * 0.05366319
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35903 * 0.52079518
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25191 * 0.22569285
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33257 * 0.31145269
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19269 * 0.08805548
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77541 * 0.77724660
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95333 * 0.45114655
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78907 * 0.81345996
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51324 * 0.80817045
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96707 * 0.97171633
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8797 * 0.88605109
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32221 * 0.13101724
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20366 * 0.88699222
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3103 * 0.48864692
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4477 * 0.95059856
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51104 * 0.53048409
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35834 * 0.30057582
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49555 * 0.17116394
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67353 * 0.63228065
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85042 * 0.21778001
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94165 * 0.36521643
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'jdnpgwlv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0011():
    """Extended test 11 for transcoding."""
    x_0 = 32977 * 0.64949055
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4110 * 0.22893126
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70473 * 0.90877926
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51345 * 0.86586787
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18078 * 0.70056522
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86143 * 0.05271358
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55095 * 0.20333518
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55793 * 0.26609492
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77993 * 0.62599676
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76020 * 0.04465537
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24374 * 0.89241968
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38113 * 0.08954062
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37602 * 0.58584638
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28647 * 0.77819085
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8693 * 0.55377475
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83727 * 0.92557887
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46639 * 0.52159248
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77641 * 0.64698596
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77872 * 0.79126392
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1247 * 0.67363623
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69415 * 0.31878771
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11404 * 0.54507569
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90030 * 0.46942648
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19959 * 0.92525584
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58734 * 0.40614541
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89024 * 0.12363631
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21809 * 0.90163846
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98052 * 0.29828134
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34947 * 0.15603222
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67599 * 0.45326709
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22854 * 0.88023192
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35587 * 0.19646694
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74148 * 0.02157974
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33635 * 0.57463470
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35961 * 0.48299183
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11470 * 0.95183716
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57655 * 0.88939445
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82088 * 0.18608203
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12834 * 0.05142599
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66577 * 0.71917328
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35014 * 0.08258940
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 24219 * 0.07970835
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28623 * 0.24700589
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 25619 * 0.75536448
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 3555 * 0.54761453
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'ohakxbdx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0012():
    """Extended test 12 for transcoding."""
    x_0 = 18458 * 0.71271972
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69996 * 0.66987486
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2767 * 0.57806879
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99529 * 0.12502622
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34552 * 0.62593683
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48004 * 0.33538953
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18304 * 0.88935527
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26070 * 0.19769271
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15125 * 0.52527968
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10709 * 0.77735444
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65574 * 0.91322402
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16069 * 0.19051551
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94797 * 0.47085099
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1345 * 0.48567251
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33404 * 0.91087443
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62683 * 0.37028342
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65043 * 0.63899226
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33360 * 0.44379862
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60314 * 0.65997540
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13999 * 0.77140662
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70556 * 0.25599913
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71864 * 0.55502544
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44240 * 0.91680459
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62023 * 0.94853216
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52368 * 0.90048199
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5610 * 0.95401438
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75716 * 0.59541780
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43930 * 0.81501480
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42882 * 0.18865709
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31850 * 0.23970678
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37144 * 0.04591985
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98342 * 0.29154846
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59658 * 0.41706096
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ivgduonw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0013():
    """Extended test 13 for transcoding."""
    x_0 = 13807 * 0.91447684
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88170 * 0.29081635
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6912 * 0.64452189
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53627 * 0.72381164
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66986 * 0.75850162
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41896 * 0.98483949
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73939 * 0.47002026
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45877 * 0.90695290
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57013 * 0.48081688
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46548 * 0.08861657
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96820 * 0.60724451
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67985 * 0.07611098
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25342 * 0.90198988
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82126 * 0.89367684
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73141 * 0.08886829
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10253 * 0.68869759
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63985 * 0.14704681
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37931 * 0.54769205
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14152 * 0.82572863
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75395 * 0.75944942
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 270 * 0.46561772
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69630 * 0.29460230
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76620 * 0.24274192
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63062 * 0.63412788
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49341 * 0.06659477
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11880 * 0.02226996
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66601 * 0.32892506
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'qptscndz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0014():
    """Extended test 14 for transcoding."""
    x_0 = 50474 * 0.13924245
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44939 * 0.61264590
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21931 * 0.95552167
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28151 * 0.90087085
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87115 * 0.50868076
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41745 * 0.80527101
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32211 * 0.73173498
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62126 * 0.39347310
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46955 * 0.35028803
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14618 * 0.91396854
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58735 * 0.83771781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46038 * 0.62584590
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87483 * 0.59742012
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69101 * 0.85321148
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24191 * 0.37296082
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50174 * 0.33796731
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1464 * 0.18538933
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28066 * 0.12337852
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67765 * 0.36242007
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7202 * 0.03100297
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39734 * 0.34946579
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82406 * 0.46425106
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95417 * 0.43120407
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58853 * 0.37429636
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58554 * 0.01061228
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49906 * 0.95131406
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4014 * 0.71994363
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54613 * 0.92749910
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29217 * 0.41325323
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43159 * 0.35382463
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73959 * 0.89748660
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76723 * 0.35281471
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1259 * 0.41166902
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82979 * 0.80671287
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68205 * 0.12118978
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'vhypgnfi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0015():
    """Extended test 15 for transcoding."""
    x_0 = 48629 * 0.17526029
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38455 * 0.84718915
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88543 * 0.86435986
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 951 * 0.23462431
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37612 * 0.76441967
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7082 * 0.52928440
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37428 * 0.95385994
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10070 * 0.87934830
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79800 * 0.88878551
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42240 * 0.91576435
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24161 * 0.40674274
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12311 * 0.38257177
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68684 * 0.78526046
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80266 * 0.46542794
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84566 * 0.87122366
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99209 * 0.80450550
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45168 * 0.14844364
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74197 * 0.38279896
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3563 * 0.32737727
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89952 * 0.76889984
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92301 * 0.66376628
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'oyibejaq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0016():
    """Extended test 16 for transcoding."""
    x_0 = 8772 * 0.44071325
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3342 * 0.02565206
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52685 * 0.33568791
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2753 * 0.49813073
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92319 * 0.48118459
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9274 * 0.68809840
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56916 * 0.32490212
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99909 * 0.91988205
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62314 * 0.27492179
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31820 * 0.38817768
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68062 * 0.95588458
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38196 * 0.42024912
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34252 * 0.89859991
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86966 * 0.02936698
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94755 * 0.86183233
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90278 * 0.66002885
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10582 * 0.98205888
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62962 * 0.92492138
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74799 * 0.49670658
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45295 * 0.42493895
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57140 * 0.82268668
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 582 * 0.70974244
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81053 * 0.33977767
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20479 * 0.22542889
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5742 * 0.47332695
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63872 * 0.70538049
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22707 * 0.89794524
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82459 * 0.44962773
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67301 * 0.85456488
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62703 * 0.45874000
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15216 * 0.27146733
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68058 * 0.12083265
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6645 * 0.77387611
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5173 * 0.32827169
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68496 * 0.76280415
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43534 * 0.29166443
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80842 * 0.92149887
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59831 * 0.29517646
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90668 * 0.14021762
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10973 * 0.28886317
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'wddkwyoi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0017():
    """Extended test 17 for transcoding."""
    x_0 = 29965 * 0.65440093
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11926 * 0.94225140
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38388 * 0.68777837
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92831 * 0.29700340
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78668 * 0.31499923
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5467 * 0.13497726
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96441 * 0.69801030
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84973 * 0.48712726
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30098 * 0.76891594
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79551 * 0.78974544
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91123 * 0.84303819
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88400 * 0.73010367
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61615 * 0.23084167
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30716 * 0.31997272
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30031 * 0.09723043
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45880 * 0.49757586
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75575 * 0.52768517
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53908 * 0.50784528
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54881 * 0.16150450
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45790 * 0.34236927
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66780 * 0.02036570
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76573 * 0.79755588
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22488 * 0.81741572
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22126 * 0.91722421
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66332 * 0.85777919
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24775 * 0.39600177
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8795 * 0.08122926
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71117 * 0.49057218
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56079 * 0.86908106
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26204 * 0.77307543
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84678 * 0.50308932
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35010 * 0.77768597
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2400 * 0.37661643
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38111 * 0.27600995
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21853 * 0.49795990
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60170 * 0.89862887
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97584 * 0.02547115
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12235 * 0.45245087
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76498 * 0.34110226
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54112 * 0.92604211
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 50888 * 0.77554042
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38583 * 0.10523352
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10263 * 0.93066800
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94999 * 0.67581490
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 29 * 0.90960885
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 76478 * 0.80958571
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 6076 * 0.74516757
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 3922 * 0.43360561
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'jtljohct').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0018():
    """Extended test 18 for transcoding."""
    x_0 = 46191 * 0.72192047
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80859 * 0.51808443
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55252 * 0.44836610
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63448 * 0.77841309
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28233 * 0.97971566
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64760 * 0.50943341
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84694 * 0.95837607
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34708 * 0.08767661
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13567 * 0.55087509
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11009 * 0.50340440
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92674 * 0.09466980
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99741 * 0.59860854
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84626 * 0.17445140
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26947 * 0.32575204
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38476 * 0.53894714
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37690 * 0.37284357
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60090 * 0.29499681
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47627 * 0.49054580
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99510 * 0.20343326
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92640 * 0.42552954
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48876 * 0.58826193
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30635 * 0.53511911
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98352 * 0.12992156
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14458 * 0.50887310
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99735 * 0.91301745
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62379 * 0.68389909
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60784 * 0.51371266
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69128 * 0.35083478
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74820 * 0.47547582
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45339 * 0.35996938
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33829 * 0.39907797
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46810 * 0.68621181
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53073 * 0.58313929
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10694 * 0.52471190
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18345 * 0.17134098
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69026 * 0.73258411
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69669 * 0.91696350
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45840 * 0.49152993
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10742 * 0.07663781
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96935 * 0.54809458
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65245 * 0.13203754
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 7027 * 0.63208333
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'mawfzhug').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0019():
    """Extended test 19 for transcoding."""
    x_0 = 94681 * 0.68787269
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4708 * 0.99384460
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41730 * 0.48844109
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71277 * 0.76589733
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78103 * 0.54349994
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64705 * 0.62470164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38440 * 0.09388198
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87496 * 0.14739083
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43817 * 0.79593311
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84146 * 0.76239752
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57879 * 0.63574393
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49882 * 0.71244181
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8682 * 0.76865898
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20586 * 0.83850423
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1513 * 0.89127663
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23835 * 0.01747182
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33261 * 0.01230609
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88307 * 0.35591615
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27552 * 0.69271686
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95196 * 0.20796254
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82334 * 0.65372806
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14954 * 0.74710738
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20429 * 0.63724131
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7943 * 0.98866751
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44393 * 0.95119009
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73282 * 0.25249628
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32952 * 0.66479716
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'qpildgci').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0020():
    """Extended test 20 for transcoding."""
    x_0 = 56353 * 0.73042089
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17856 * 0.44506761
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71536 * 0.13292787
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71708 * 0.61018225
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71957 * 0.83469925
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22046 * 0.66956722
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78074 * 0.63274532
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78823 * 0.79687594
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34067 * 0.66603810
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80430 * 0.57464290
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41927 * 0.50793103
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46574 * 0.43068715
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4063 * 0.86752024
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78383 * 0.66891341
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66448 * 0.02696739
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86397 * 0.08889181
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73038 * 0.86008471
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93067 * 0.84214732
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40789 * 0.97250314
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13103 * 0.30168229
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21861 * 0.16616116
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17947 * 0.83245824
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64236 * 0.38902660
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17058 * 0.45433159
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44552 * 0.38080761
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14736 * 0.41044324
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11863 * 0.96026428
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48011 * 0.39765438
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24814 * 0.77297777
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84260 * 0.81347179
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2035 * 0.03832405
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77392 * 0.19969123
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97908 * 0.20895226
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87849 * 0.73165661
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23597 * 0.79791429
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66488 * 0.54819574
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74513 * 0.12116199
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61283 * 0.31696031
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'arwcavqk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0021():
    """Extended test 21 for transcoding."""
    x_0 = 17973 * 0.08021904
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33889 * 0.21429051
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88257 * 0.98985593
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71945 * 0.35667988
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62101 * 0.19130326
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58026 * 0.64594418
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18915 * 0.31424320
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42811 * 0.52635442
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25591 * 0.41551943
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4282 * 0.36664674
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 558 * 0.29359255
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83606 * 0.10322670
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27808 * 0.17771998
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40425 * 0.41882451
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69280 * 0.16111050
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14727 * 0.14193271
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78520 * 0.83069614
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72544 * 0.51435026
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25724 * 0.05475942
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41104 * 0.62549747
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89959 * 0.44378364
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91211 * 0.88473289
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11542 * 0.75513408
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55535 * 0.60677189
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16749 * 0.06242080
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90330 * 0.93933796
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74161 * 0.84807833
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23545 * 0.31098409
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57590 * 0.99664952
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78695 * 0.93012911
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29016 * 0.24810517
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'scezmwnx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0022():
    """Extended test 22 for transcoding."""
    x_0 = 78352 * 0.16298183
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42054 * 0.22347454
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12130 * 0.97264048
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4248 * 0.71873892
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31677 * 0.15364341
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9018 * 0.47680381
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20671 * 0.29501711
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17824 * 0.06024973
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16277 * 0.55665752
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95281 * 0.34217460
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43395 * 0.03016403
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99691 * 0.96558707
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62959 * 0.85228395
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29536 * 0.45182460
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10244 * 0.74519156
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99231 * 0.13387778
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43119 * 0.60564670
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11618 * 0.35835833
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99062 * 0.41593562
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46283 * 0.65922521
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49670 * 0.92135352
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43616 * 0.46702966
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39962 * 0.17930008
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35666 * 0.56881529
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9457 * 0.54601950
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78255 * 0.45277739
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66223 * 0.92175880
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96000 * 0.66692675
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91144 * 0.70989167
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15647 * 0.45172504
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49507 * 0.60514961
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66721 * 0.41178275
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56350 * 0.46120544
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88669 * 0.28919929
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88715 * 0.48019103
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10328 * 0.70328220
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30533 * 0.15864324
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67969 * 0.91327341
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20066 * 0.46024887
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70760 * 0.37625709
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74292 * 0.19798666
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53934 * 0.01771108
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35273 * 0.15082769
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39992 * 0.41390725
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 55662 * 0.06467908
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 34809 * 0.40781168
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 80783 * 0.67484784
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ncksvosn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0023():
    """Extended test 23 for transcoding."""
    x_0 = 90375 * 0.88903773
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10556 * 0.33763432
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42353 * 0.36568026
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8256 * 0.85201579
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16732 * 0.96755919
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10211 * 0.08465358
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80202 * 0.56736001
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40337 * 0.37226573
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69278 * 0.39691605
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34044 * 0.28542880
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97588 * 0.52741780
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80792 * 0.21699558
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82862 * 0.89560188
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22234 * 0.85216995
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90983 * 0.47631964
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33123 * 0.40033417
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53822 * 0.44414046
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65531 * 0.77656281
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12755 * 0.93965218
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92474 * 0.48806551
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68788 * 0.84433924
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1885 * 0.86042514
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68822 * 0.44403115
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33357 * 0.98973834
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87377 * 0.87183992
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11465 * 0.68372981
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69375 * 0.18733614
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26842 * 0.98788496
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37295 * 0.17929504
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90114 * 0.37910059
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89872 * 0.06196228
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42173 * 0.98895003
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95834 * 0.79243371
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38775 * 0.44849268
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90389 * 0.29996196
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1137 * 0.35534153
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85459 * 0.10132095
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91616 * 0.12578601
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4690 * 0.28721134
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67396 * 0.41427077
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95761 * 0.14719936
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59888 * 0.75103085
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'vgcichet').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0024():
    """Extended test 24 for transcoding."""
    x_0 = 26541 * 0.74034450
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 158 * 0.02720023
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93668 * 0.89358692
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19999 * 0.58789782
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59285 * 0.81114259
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61820 * 0.16380784
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78744 * 0.48239830
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99236 * 0.16832334
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17159 * 0.47353963
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76780 * 0.22477914
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38120 * 0.12280082
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25884 * 0.39058274
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12787 * 0.77830959
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63747 * 0.51665377
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5418 * 0.77212357
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11081 * 0.62445688
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90698 * 0.30960228
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50001 * 0.26218627
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43568 * 0.35322900
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50427 * 0.44593637
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44804 * 0.51527088
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31183 * 0.78473021
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77865 * 0.25569004
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36489 * 0.49258605
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82497 * 0.03212975
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95694 * 0.88626587
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26950 * 0.30980478
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44366 * 0.97460467
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11518 * 0.81626255
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81938 * 0.09866240
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61369 * 0.67755952
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42001 * 0.92015396
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89125 * 0.16172106
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56650 * 0.30527836
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59842 * 0.35972835
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18961 * 0.67809643
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68800 * 0.91066275
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13550 * 0.02010205
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40737 * 0.99412025
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43495 * 0.38326965
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84629 * 0.60257973
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60266 * 0.55370182
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46241 * 0.67812888
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58773 * 0.32398174
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 33868 * 0.21349155
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 23272 * 0.84757043
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 98253 * 0.83455778
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 37199 * 0.19534721
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 78485 * 0.10460827
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 56959 * 0.63836504
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'nqihozds').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0025():
    """Extended test 25 for transcoding."""
    x_0 = 84489 * 0.42256763
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89002 * 0.57690840
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33660 * 0.54107716
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66015 * 0.34640869
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63293 * 0.47076276
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78410 * 0.55251580
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20052 * 0.46378969
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52169 * 0.36187785
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61070 * 0.99406536
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54543 * 0.18121757
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12755 * 0.40403071
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71953 * 0.65404558
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55877 * 0.86883067
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72104 * 0.07463947
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48290 * 0.35399492
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57677 * 0.78962513
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72997 * 0.10278580
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34776 * 0.92900685
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81930 * 0.42886519
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86370 * 0.13517242
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60064 * 0.84054119
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17209 * 0.97130682
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24676 * 0.29196535
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49967 * 0.11107912
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85318 * 0.79478862
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ejoqmbwa').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0026():
    """Extended test 26 for transcoding."""
    x_0 = 98499 * 0.30400716
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66046 * 0.90439623
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46894 * 0.58010452
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98459 * 0.83763877
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10613 * 0.89458607
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84395 * 0.84449190
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14691 * 0.61466695
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83454 * 0.12491917
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9432 * 0.96026885
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75002 * 0.30451791
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14200 * 0.84653268
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60976 * 0.57622522
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11489 * 0.55400003
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20484 * 0.91531469
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64137 * 0.29007733
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54424 * 0.05402683
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8459 * 0.57862482
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1953 * 0.70605525
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65118 * 0.21933551
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73549 * 0.75070094
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90534 * 0.22586909
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 714 * 0.61984565
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52032 * 0.05268150
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99595 * 0.78075044
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74214 * 0.52678551
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87123 * 0.15518670
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42720 * 0.32246620
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91083 * 0.52298366
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69278 * 0.99879436
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73230 * 0.71160918
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94330 * 0.85328302
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81541 * 0.01217673
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6407 * 0.38207427
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12899 * 0.46906082
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53654 * 0.29422517
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76700 * 0.81990390
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97253 * 0.11067134
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48280 * 0.47652051
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35255 * 0.49821126
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8806 * 0.78618744
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82042 * 0.93337845
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59274 * 0.62652671
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 5006 * 0.66979567
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 87986 * 0.80872486
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 14517 * 0.15179061
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 45715 * 0.50977428
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 65039 * 0.50261361
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 36400 * 0.69293933
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'htrkzklp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0027():
    """Extended test 27 for transcoding."""
    x_0 = 25950 * 0.82023065
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32642 * 0.51845622
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 370 * 0.75973831
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45743 * 0.21392956
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4721 * 0.23441800
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76494 * 0.46474489
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73320 * 0.94950557
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51624 * 0.21727478
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65693 * 0.99745214
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56835 * 0.73383529
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73908 * 0.06865095
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8650 * 0.90290375
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28967 * 0.70256251
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90384 * 0.20361628
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1820 * 0.05544998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97124 * 0.73554995
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33838 * 0.95624534
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42364 * 0.52704786
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19257 * 0.71955380
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58775 * 0.29047809
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58898 * 0.05001160
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74875 * 0.55655425
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35526 * 0.89834853
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90459 * 0.34297196
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73460 * 0.13957533
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45579 * 0.35837320
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70022 * 0.70654301
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88118 * 0.77436970
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37479 * 0.76523302
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72250 * 0.47609744
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84792 * 0.14506365
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65514 * 0.62678694
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62274 * 0.73589033
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12236 * 0.31128973
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96297 * 0.92419661
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77817 * 0.42979993
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29759 * 0.30976526
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40997 * 0.38794263
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58168 * 0.01153033
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65207 * 0.47126110
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 73732 * 0.43086400
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 29829 * 0.66343894
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66748 * 0.12836217
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 28125 * 0.42473652
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 34551 * 0.52869407
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 9537 * 0.83019754
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 86883 * 0.00819019
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'bueapooy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0028():
    """Extended test 28 for transcoding."""
    x_0 = 44291 * 0.64748025
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4186 * 0.53051843
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63243 * 0.80124538
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65925 * 0.64491763
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35586 * 0.33615943
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41421 * 0.79176954
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25564 * 0.14151391
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93727 * 0.82664351
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35247 * 0.10087933
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13013 * 0.86960637
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11143 * 0.99046929
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52592 * 0.82064108
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70298 * 0.13885413
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68649 * 0.76441022
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52237 * 0.27944579
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26792 * 0.23979171
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70823 * 0.15317725
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70295 * 0.66419855
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28037 * 0.89310314
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43147 * 0.35869113
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47102 * 0.69321289
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41823 * 0.33114944
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93710 * 0.58158625
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53068 * 0.13717503
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67700 * 0.82967211
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93112 * 0.60018301
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44523 * 0.90292650
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14708 * 0.24870182
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32667 * 0.67920540
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97576 * 0.85116934
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87933 * 0.07134859
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61086 * 0.79741048
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37569 * 0.42631676
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5718 * 0.10489125
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16970 * 0.13336235
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28040 * 0.24921043
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'rylwnxvb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0029():
    """Extended test 29 for transcoding."""
    x_0 = 98002 * 0.49949209
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19349 * 0.29959481
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91610 * 0.81564087
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21583 * 0.48203060
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86751 * 0.15789165
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34276 * 0.78159613
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56979 * 0.46923879
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68154 * 0.27827237
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81160 * 0.59685985
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38161 * 0.34375799
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90836 * 0.21771853
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80139 * 0.41587673
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49391 * 0.49186066
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90111 * 0.59506635
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11236 * 0.70105783
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39909 * 0.51104418
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53871 * 0.51414553
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95769 * 0.77313130
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54296 * 0.92429454
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5219 * 0.98413171
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41785 * 0.27594568
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97250 * 0.16376345
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24569 * 0.97340551
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79591 * 0.97386392
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61512 * 0.57590374
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21140 * 0.40364964
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10349 * 0.22898315
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76240 * 0.90846230
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66457 * 0.92859457
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64931 * 0.78571491
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93121 * 0.84678627
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77324 * 0.04614077
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79849 * 0.18020916
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92563 * 0.15214133
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73733 * 0.92211981
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15798 * 0.59680739
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52846 * 0.84661177
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'mvucnzvd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0030():
    """Extended test 30 for transcoding."""
    x_0 = 1880 * 0.08326950
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92590 * 0.17565582
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2598 * 0.58677522
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23156 * 0.52175821
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60610 * 0.71323620
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45347 * 0.06696514
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67572 * 0.07666136
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21009 * 0.02404814
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41358 * 0.49914103
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29415 * 0.63708186
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4384 * 0.66674408
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86771 * 0.69996238
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45917 * 0.02340508
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81933 * 0.55067815
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3010 * 0.09897957
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27040 * 0.69352834
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19208 * 0.71866266
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25748 * 0.17423829
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2219 * 0.69724388
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85824 * 0.71703689
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84451 * 0.18447240
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23444 * 0.91304093
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88766 * 0.17190017
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74808 * 0.48714758
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93596 * 0.68197500
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38635 * 0.61105762
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32620 * 0.23145743
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87581 * 0.15325932
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9768 * 0.19545060
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'xthgwvty').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0031():
    """Extended test 31 for transcoding."""
    x_0 = 87346 * 0.86773828
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53560 * 0.30488293
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89400 * 0.53792217
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59405 * 0.42838547
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52883 * 0.90307129
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73627 * 0.92354986
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77030 * 0.23057789
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57621 * 0.79188408
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62414 * 0.70609903
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42486 * 0.40151301
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61304 * 0.10371485
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76708 * 0.36816851
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26727 * 0.59350658
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95307 * 0.50792090
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2654 * 0.49696122
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51626 * 0.67755739
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47689 * 0.90034020
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15311 * 0.92128833
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47946 * 0.53785713
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86124 * 0.11372016
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31567 * 0.40232293
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5104 * 0.99397378
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78330 * 0.36116234
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53300 * 0.05846566
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32120 * 0.02577897
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76933 * 0.55468560
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92081 * 0.89603939
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95160 * 0.53534596
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77606 * 0.86183366
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82063 * 0.72527969
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62320 * 0.76472827
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30655 * 0.50500528
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'pqtztehw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0032():
    """Extended test 32 for transcoding."""
    x_0 = 70395 * 0.17767513
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27370 * 0.91854126
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15655 * 0.01524768
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71591 * 0.89774260
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66147 * 0.48037934
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29635 * 0.21472698
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74042 * 0.83343092
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74290 * 0.33413653
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48413 * 0.80395506
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59874 * 0.89682815
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14897 * 0.53923567
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83914 * 0.86017149
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28577 * 0.05361612
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85979 * 0.39953716
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74680 * 0.88351327
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9069 * 0.10496698
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46202 * 0.12704511
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28816 * 0.56047180
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16386 * 0.35094898
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54144 * 0.35426506
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39353 * 0.25095232
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95206 * 0.43611614
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68935 * 0.00625331
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68263 * 0.17402926
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80219 * 0.43178216
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16507 * 0.76680003
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76705 * 0.36122215
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34995 * 0.24823082
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20042 * 0.46788180
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50548 * 0.56207616
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3536 * 0.48963572
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33330 * 0.99394626
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62203 * 0.31317959
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74556 * 0.98425984
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80542 * 0.86161559
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'cjhstugl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0033():
    """Extended test 33 for transcoding."""
    x_0 = 16387 * 0.00726945
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51493 * 0.28400718
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62121 * 0.36652988
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75894 * 0.14023597
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79160 * 0.59678801
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68599 * 0.23729144
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94309 * 0.12818758
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88406 * 0.41419986
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67928 * 0.89605252
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45005 * 0.08771602
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77 * 0.69250038
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79367 * 0.53540722
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79258 * 0.10819772
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44987 * 0.48438410
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45013 * 0.93161378
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49324 * 0.09035219
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18993 * 0.59284455
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48608 * 0.68413038
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98130 * 0.55292216
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6048 * 0.17889976
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22151 * 0.44051844
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11447 * 0.55098388
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'ttkwdrev').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0034():
    """Extended test 34 for transcoding."""
    x_0 = 82986 * 0.13970571
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33016 * 0.85960997
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12048 * 0.79409341
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83960 * 0.06313585
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56614 * 0.82920354
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17628 * 0.59694269
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77517 * 0.03757302
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80270 * 0.07891534
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16906 * 0.76622029
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95827 * 0.66185277
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13465 * 0.06169744
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75152 * 0.76261688
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22234 * 0.22274095
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3318 * 0.61191701
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96564 * 0.50577832
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 582 * 0.06170870
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29862 * 0.48274312
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96889 * 0.65570755
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94782 * 0.36548628
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56076 * 0.72547424
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99945 * 0.44425910
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33611 * 0.96895083
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67204 * 0.42625033
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24540 * 0.15299657
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80127 * 0.39124824
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23244 * 0.87120466
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96005 * 0.57013695
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73318 * 0.75713379
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14098 * 0.29670312
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14064 * 0.46253319
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85195 * 0.17740652
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79814 * 0.26843386
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45167 * 0.78429377
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7570 * 0.31399129
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46840 * 0.36073799
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71938 * 0.64289048
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'uomiijto').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0035():
    """Extended test 35 for transcoding."""
    x_0 = 27199 * 0.77985206
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92797 * 0.31899191
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99203 * 0.73455591
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15462 * 0.56380812
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79183 * 0.56819299
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67897 * 0.41690669
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74036 * 0.18659283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60862 * 0.96216779
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53323 * 0.80886468
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13928 * 0.62067349
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28114 * 0.16298810
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36601 * 0.22204988
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47540 * 0.42134274
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84960 * 0.93076474
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6638 * 0.44091587
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71876 * 0.02634069
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9940 * 0.30274697
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75505 * 0.43802825
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89273 * 0.95000849
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23308 * 0.32578087
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73793 * 0.77210060
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87405 * 0.51385480
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67543 * 0.74743262
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41820 * 0.41008222
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18205 * 0.99765662
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63337 * 0.90731979
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77964 * 0.39689481
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3316 * 0.91615772
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33902 * 0.44203789
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21078 * 0.97716291
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67579 * 0.79632338
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40742 * 0.32326352
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54578 * 0.94061066
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70357 * 0.61520214
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73314 * 0.39324074
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40182 * 0.66860484
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47965 * 0.64574179
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'ibpeiopc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0036():
    """Extended test 36 for transcoding."""
    x_0 = 35081 * 0.63644906
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39701 * 0.88797086
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52437 * 0.53620100
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41346 * 0.40839485
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15437 * 0.88519981
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75071 * 0.71862658
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93360 * 0.55231755
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30394 * 0.50274766
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56405 * 0.88167785
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47549 * 0.11070917
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67455 * 0.12080585
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84398 * 0.71682073
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88093 * 0.76434093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19627 * 0.07802375
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57788 * 0.96882406
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93823 * 0.50788642
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29349 * 0.06244497
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41421 * 0.06626659
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82414 * 0.07721507
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9529 * 0.50667948
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65677 * 0.01774139
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77659 * 0.19375312
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72629 * 0.57073845
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70628 * 0.28496612
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46720 * 0.91260662
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38996 * 0.56046553
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48434 * 0.84180695
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87972 * 0.56004314
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71809 * 0.18708092
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46335 * 0.90864861
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47721 * 0.01377865
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88111 * 0.77307821
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75185 * 0.05985948
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81481 * 0.02473293
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64926 * 0.13214908
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23753 * 0.52994109
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64295 * 0.59211827
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7372 * 0.07890819
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70126 * 0.97315505
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ourwtdnr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0037():
    """Extended test 37 for transcoding."""
    x_0 = 31644 * 0.05586113
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75268 * 0.73360573
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72744 * 0.71720987
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21306 * 0.67395374
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48737 * 0.64688865
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59329 * 0.63760270
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66800 * 0.31398216
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20179 * 0.10062361
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3177 * 0.06845413
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72472 * 0.60132845
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67963 * 0.41428529
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40711 * 0.16142485
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60347 * 0.16799108
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94473 * 0.09908807
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99592 * 0.57839043
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71494 * 0.49468763
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59839 * 0.45401241
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98182 * 0.54670952
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15771 * 0.41185415
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16401 * 0.12248496
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96855 * 0.52591626
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32955 * 0.81014618
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28292 * 0.14073367
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58375 * 0.38622551
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76851 * 0.36678173
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44061 * 0.85789028
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11355 * 0.15387039
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5271 * 0.26389140
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69263 * 0.23184508
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6519 * 0.42429732
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11497 * 0.76238246
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98817 * 0.62840412
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99519 * 0.27065013
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7683 * 0.40466853
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2228 * 0.84205080
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97486 * 0.06179448
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45452 * 0.15785345
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20464 * 0.33680679
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11840 * 0.79707901
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59730 * 0.24515681
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 59487 * 0.49514172
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93942 * 0.30471798
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88133 * 0.75223688
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47376 * 0.06581789
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89509 * 0.43712742
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 94032 * 0.89407092
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 18332 * 0.76087960
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 48156 * 0.70064751
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'uphsqgzb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0038():
    """Extended test 38 for transcoding."""
    x_0 = 89739 * 0.14964716
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1024 * 0.27527371
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50226 * 0.40929365
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73687 * 0.31479624
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49216 * 0.93799552
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68817 * 0.54967822
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76677 * 0.61146971
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25098 * 0.36068548
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72706 * 0.55962235
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36103 * 0.50076399
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53375 * 0.71163483
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24579 * 0.80863363
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30943 * 0.83811738
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16173 * 0.59461781
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95814 * 0.62094709
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69337 * 0.18516561
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90016 * 0.03637601
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12081 * 0.42289770
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27920 * 0.64337417
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69209 * 0.97725185
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57471 * 0.65487748
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19775 * 0.46731803
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41181 * 0.28843680
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19298 * 0.64000708
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99467 * 0.07441251
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89907 * 0.68988494
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3380 * 0.85424601
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68622 * 0.83578159
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9664 * 0.83687384
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37298 * 0.63369905
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57127 * 0.14880190
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52710 * 0.57180873
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31560 * 0.37626679
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78737 * 0.78000940
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65518 * 0.80078102
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'smecmwsp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0039():
    """Extended test 39 for transcoding."""
    x_0 = 1623 * 0.44634218
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90396 * 0.13871046
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42345 * 0.49668807
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58905 * 0.90633289
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64855 * 0.09596713
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76204 * 0.83538413
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37500 * 0.80775089
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93418 * 0.17123684
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24141 * 0.01160743
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54260 * 0.08287751
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49541 * 0.53275765
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36487 * 0.01603382
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70323 * 0.35619987
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41896 * 0.89783670
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36575 * 0.44029227
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81934 * 0.38426229
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17671 * 0.45331086
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71811 * 0.97431512
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80013 * 0.56927384
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56530 * 0.28114400
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51414 * 0.26515169
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98568 * 0.23521812
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99579 * 0.47097695
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37041 * 0.93257037
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1118 * 0.29061448
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86418 * 0.14305159
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4182 * 0.49024361
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97629 * 0.18328841
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73625 * 0.90228991
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29844 * 0.60606818
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12654 * 0.74762710
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58757 * 0.66499204
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 525 * 0.06314862
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30318 * 0.12841492
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79735 * 0.39836385
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85775 * 0.21959594
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58551 * 0.28684855
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59777 * 0.80606911
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27854 * 0.54054915
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 658 * 0.49593146
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53085 * 0.96028491
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4894 * 0.61952515
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 64801 * 0.77606723
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'tdrbbtho').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0040():
    """Extended test 40 for transcoding."""
    x_0 = 7897 * 0.23114995
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79473 * 0.27147866
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26707 * 0.22427086
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9399 * 0.07516579
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59300 * 0.39478353
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47658 * 0.82699550
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12643 * 0.31036133
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84615 * 0.26458699
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77752 * 0.86658808
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85986 * 0.43459560
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19866 * 0.48606597
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3144 * 0.55683210
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53326 * 0.95233999
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32311 * 0.39534715
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33913 * 0.70795667
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68449 * 0.76635708
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44704 * 0.51985863
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26599 * 0.23174280
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31547 * 0.22519223
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54972 * 0.84296710
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15693 * 0.98794634
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45116 * 0.10396597
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67295 * 0.00704339
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82919 * 0.45639388
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38116 * 0.71970621
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79423 * 0.23686949
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66671 * 0.82349531
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 680 * 0.92632835
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1524 * 0.92808814
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85895 * 0.49819308
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74604 * 0.58138146
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62400 * 0.82767881
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97658 * 0.92093617
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17318 * 0.47324302
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30065 * 0.68645112
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70424 * 0.16342381
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13560 * 0.19003958
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31118 * 0.84745905
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94657 * 0.73185272
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65639 * 0.86235752
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82037 * 0.20490229
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72140 * 0.42343119
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 19667 * 0.54090212
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 19476 * 0.17831772
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79730 * 0.19731082
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 94763 * 0.88847114
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 22871 * 0.43723696
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 13315 * 0.44329412
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 28052 * 0.46758713
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'aiqfvdsc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0041():
    """Extended test 41 for transcoding."""
    x_0 = 36823 * 0.64397943
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45684 * 0.20060473
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64584 * 0.40227641
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27703 * 0.43251730
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93983 * 0.23094801
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46670 * 0.58719975
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83837 * 0.34623516
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65725 * 0.52337091
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54427 * 0.29206386
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1557 * 0.28144679
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40794 * 0.89747535
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5457 * 0.66938461
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9393 * 0.81636401
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4699 * 0.54082767
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27281 * 0.45587550
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55465 * 0.85135443
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59179 * 0.26602670
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96106 * 0.78811720
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10101 * 0.47948017
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93662 * 0.39029773
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60960 * 0.39555418
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'kfvkotgb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0042():
    """Extended test 42 for transcoding."""
    x_0 = 73286 * 0.16278191
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93115 * 0.56638193
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12940 * 0.56845412
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63428 * 0.12675048
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6051 * 0.03294038
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90635 * 0.15242667
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9199 * 0.22758950
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97001 * 0.93956986
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54963 * 0.75245722
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4151 * 0.09838330
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 479 * 0.76426782
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83080 * 0.65500431
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1485 * 0.80304335
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3739 * 0.85942203
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11045 * 0.88108596
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2308 * 0.78803568
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70848 * 0.63925810
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82081 * 0.74117621
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65868 * 0.46250277
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81168 * 0.20972848
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24735 * 0.21657311
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88758 * 0.16362192
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9937 * 0.89585431
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76212 * 0.55173388
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22578 * 0.20030456
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 723 * 0.54019571
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75345 * 0.16732815
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5540 * 0.99421308
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43049 * 0.15977855
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84636 * 0.97059153
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21315 * 0.60305088
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11886 * 0.89699835
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58528 * 0.56913283
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62664 * 0.14818259
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86352 * 0.57975780
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31476 * 0.03115284
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48716 * 0.05577064
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2409 * 0.93176159
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77892 * 0.80918500
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9514 * 0.81273903
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42464 * 0.69521336
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4420 * 0.56668759
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28712 * 0.30963642
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 63450 * 0.02551871
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61018 * 0.29311391
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 94511 * 0.23907416
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 67498 * 0.24480237
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 21599 * 0.11853207
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 75139 * 0.92611236
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'oskmzjbg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0043():
    """Extended test 43 for transcoding."""
    x_0 = 84213 * 0.43035270
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5291 * 0.86385041
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64220 * 0.40591440
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24037 * 0.94877707
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7286 * 0.51289215
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52848 * 0.67722946
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5309 * 0.81903447
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42359 * 0.32445054
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17494 * 0.17784635
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94611 * 0.62266251
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45252 * 0.11598379
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65627 * 0.38341814
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85630 * 0.04567204
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74177 * 0.17201520
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77998 * 0.95013826
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58170 * 0.32737339
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54803 * 0.25299874
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40012 * 0.99953542
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11467 * 0.76900116
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44947 * 0.07061863
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67874 * 0.03111519
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68042 * 0.88900992
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77500 * 0.11801375
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93645 * 0.91110531
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44572 * 0.23479703
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57199 * 0.43243036
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88481 * 0.36243302
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1834 * 0.66153841
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83707 * 0.33688201
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31963 * 0.60630475
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67067 * 0.20761078
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46210 * 0.89273384
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12964 * 0.41932209
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73003 * 0.32101528
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18755 * 0.87478750
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96100 * 0.03835525
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95004 * 0.72088975
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74960 * 0.46286434
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9202 * 0.11800163
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85511 * 0.96278322
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37766 * 0.64778326
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54645 * 0.08560785
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'epjumlvn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0044():
    """Extended test 44 for transcoding."""
    x_0 = 77080 * 0.18432944
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93676 * 0.24383474
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73192 * 0.09079607
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53023 * 0.05117770
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61683 * 0.38292074
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2398 * 0.37917552
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25829 * 0.88286130
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91251 * 0.48583162
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34778 * 0.28659100
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56294 * 0.47376659
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98662 * 0.88340037
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1062 * 0.75971146
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25704 * 0.30238265
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80389 * 0.72010672
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44760 * 0.78104917
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58085 * 0.85506408
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55579 * 0.84002344
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80104 * 0.81132541
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5120 * 0.85304756
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10268 * 0.36185299
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73895 * 0.99232616
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 397 * 0.05416832
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38509 * 0.28397236
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64374 * 0.95809730
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79801 * 0.28516807
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19415 * 0.30425688
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49876 * 0.93988717
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18234 * 0.38021665
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97948 * 0.07848480
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74296 * 0.09600394
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88960 * 0.89637044
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8391 * 0.15714425
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74270 * 0.76887217
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46624 * 0.10095141
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52625 * 0.14391343
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78155 * 0.67456755
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64028 * 0.71981965
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71022 * 0.20943304
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37814 * 0.97280222
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82838 * 0.42438077
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54759 * 0.08431622
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 64701 * 0.08506394
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22174 * 0.06748195
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 1034 * 0.06592208
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 53572 * 0.07143708
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 67164 * 0.83076497
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 8088 * 0.28514093
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 87710 * 0.94412787
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 51043 * 0.36464145
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'zmepjfcw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0045():
    """Extended test 45 for transcoding."""
    x_0 = 71833 * 0.82966511
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87699 * 0.07484312
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93978 * 0.22510780
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91531 * 0.19010446
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67637 * 0.49128400
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74690 * 0.73584667
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77271 * 0.99997874
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87421 * 0.21932879
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62966 * 0.69823120
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3998 * 0.60510496
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79916 * 0.27414489
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90617 * 0.62759243
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50863 * 0.72635701
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93621 * 0.58090036
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81490 * 0.36293209
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19409 * 0.07320490
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67742 * 0.97978973
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33184 * 0.12665527
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32278 * 0.91767618
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90743 * 0.83239650
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96390 * 0.11087644
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10992 * 0.09360708
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34186 * 0.86288843
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89623 * 0.77091899
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77825 * 0.03504722
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62631 * 0.25978946
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70074 * 0.90284583
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62112 * 0.07014531
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62955 * 0.75266033
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48623 * 0.78471389
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57736 * 0.57649702
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62756 * 0.68287136
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33329 * 0.80290003
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15698 * 0.66257884
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57500 * 0.36376481
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42679 * 0.65324632
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1604 * 0.69548186
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29264 * 0.25114971
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 33201 * 0.25648768
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80855 * 0.32957616
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86606 * 0.22873792
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92964 * 0.21587428
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18259 * 0.80228357
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 49593 * 0.85091878
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 22025 * 0.21134443
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 53457 * 0.29456377
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 68619 * 0.76734589
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 33945 * 0.25244367
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'zypixaba').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0046():
    """Extended test 46 for transcoding."""
    x_0 = 47712 * 0.53106975
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71010 * 0.36063975
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4216 * 0.81406080
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86825 * 0.20714056
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67117 * 0.43758763
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14092 * 0.45135422
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57659 * 0.19299587
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23414 * 0.89717042
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43580 * 0.00105085
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66845 * 0.29058678
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77312 * 0.93314240
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97720 * 0.22007068
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28108 * 0.71130272
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79924 * 0.22987786
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20506 * 0.35410144
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30219 * 0.37414193
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96834 * 0.98323808
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17285 * 0.37539450
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66366 * 0.19091810
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27877 * 0.20910203
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5559 * 0.43635725
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80593 * 0.23123556
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32951 * 0.06902585
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55567 * 0.38227809
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17099 * 0.68233664
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91467 * 0.17339268
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'yvchmahe').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0047():
    """Extended test 47 for transcoding."""
    x_0 = 66871 * 0.49434014
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16855 * 0.50885869
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14949 * 0.37792941
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8131 * 0.61445426
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40469 * 0.32096857
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95340 * 0.48076221
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67723 * 0.99891743
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38217 * 0.06939445
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7814 * 0.22815661
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56524 * 0.23484902
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43718 * 0.86415040
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93128 * 0.18338505
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55155 * 0.21071220
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6432 * 0.43868715
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81582 * 0.54422065
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38845 * 0.41106797
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3902 * 0.28701619
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59229 * 0.47494393
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29275 * 0.30017370
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 595 * 0.61033025
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36596 * 0.91749107
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32118 * 0.23276955
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79076 * 0.76212445
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73178 * 0.02743630
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90392 * 0.78191864
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11910 * 0.51118005
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86163 * 0.63209928
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7377 * 0.83117194
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89108 * 0.70780644
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79045 * 0.25272405
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37918 * 0.61174156
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39267 * 0.23731907
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19596 * 0.42041639
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71153 * 0.99210086
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84973 * 0.03853534
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44594 * 0.85033528
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32839 * 0.40654915
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38376 * 0.72273004
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 95722 * 0.46810304
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'jtflnlot').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0048():
    """Extended test 48 for transcoding."""
    x_0 = 1915 * 0.20118388
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19426 * 0.23524576
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62958 * 0.76831565
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40341 * 0.80829219
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3153 * 0.49095024
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72499 * 0.30694188
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47922 * 0.13749608
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69218 * 0.79704100
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51989 * 0.78005567
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 671 * 0.99529780
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70136 * 0.50633918
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29201 * 0.17053473
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17428 * 0.14602631
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16410 * 0.44897531
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21627 * 0.40498558
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88934 * 0.00109713
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66168 * 0.68699049
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37043 * 0.76032642
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13508 * 0.40982740
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12511 * 0.35553744
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55343 * 0.25040722
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20159 * 0.75175981
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8086 * 0.83311064
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14133 * 0.54976614
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46709 * 0.57701762
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98894 * 0.65698971
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29860 * 0.15497149
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'usfwfiuo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0049():
    """Extended test 49 for transcoding."""
    x_0 = 85339 * 0.31969201
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47944 * 0.26919676
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7716 * 0.77145608
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63838 * 0.01573873
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42293 * 0.93131287
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24803 * 0.10421641
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73645 * 0.05577928
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19378 * 0.52175762
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58369 * 0.00097133
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98268 * 0.15714393
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55162 * 0.61452938
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8989 * 0.13787337
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94112 * 0.22420814
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87688 * 0.24801106
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22202 * 0.68940121
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10385 * 0.46841061
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72391 * 0.79448616
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77145 * 0.92949422
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58511 * 0.73821748
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58327 * 0.22078808
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28770 * 0.63875577
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26093 * 0.21472655
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58316 * 0.22917274
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73237 * 0.17946486
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22827 * 0.70247931
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8451 * 0.13518153
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82468 * 0.61933399
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21437 * 0.73773532
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42820 * 0.44070402
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95717 * 0.09513353
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92499 * 0.35115121
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 34740 * 0.76689499
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52106 * 0.10367113
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42064 * 0.91060471
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93041 * 0.61678931
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 73724 * 0.14414128
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88122 * 0.47472375
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83940 * 0.14483800
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74258 * 0.61476473
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18848 * 0.15098988
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43200 * 0.92795395
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79027 * 0.57190520
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 50459 * 0.50607222
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88129 * 0.03162387
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 87679 * 0.37499704
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 54615 * 0.39813879
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 48490 * 0.34818667
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 53520 * 0.48771846
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'qfaxbswm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0050():
    """Extended test 50 for transcoding."""
    x_0 = 92001 * 0.23943429
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50677 * 0.25027445
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26281 * 0.03624354
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31097 * 0.66755494
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54467 * 0.65231707
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43879 * 0.48597154
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61807 * 0.32820428
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78614 * 0.87109268
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28353 * 0.36836374
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39482 * 0.67741419
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36563 * 0.88108786
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87076 * 0.55587395
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16198 * 0.64909170
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58486 * 0.69515000
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26729 * 0.29881732
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78678 * 0.29017689
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65050 * 0.73257368
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67841 * 0.80803117
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68565 * 0.76002023
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29857 * 0.23899851
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51669 * 0.67734189
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49347 * 0.07064128
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70870 * 0.28483252
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62827 * 0.44005927
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62244 * 0.39117891
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73128 * 0.95861490
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56543 * 0.13737064
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6106 * 0.90904694
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30635 * 0.28358752
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85004 * 0.32820936
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45133 * 0.48175772
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ytlgixpq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0051():
    """Extended test 51 for transcoding."""
    x_0 = 15368 * 0.30661284
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16222 * 0.12433788
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41210 * 0.69781207
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62241 * 0.97474571
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50828 * 0.34221671
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4188 * 0.65508776
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82863 * 0.65718644
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12749 * 0.62325367
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13841 * 0.40592213
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57150 * 0.17879067
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8640 * 0.48206620
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82655 * 0.01918867
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40928 * 0.72790691
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88950 * 0.40560843
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2946 * 0.48737270
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62435 * 0.86272290
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90172 * 0.54437897
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66601 * 0.94441868
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60354 * 0.46125558
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99936 * 0.32872852
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60780 * 0.49908145
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43555 * 0.23660040
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59415 * 0.33256749
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16353 * 0.16475848
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62538 * 0.39721648
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10349 * 0.85299274
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68218 * 0.44364259
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24637 * 0.05955332
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63987 * 0.15607240
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82864 * 0.91528697
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20264 * 0.75471209
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21767 * 0.21707880
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95133 * 0.23705120
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11357 * 0.52643458
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56764 * 0.26922175
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75508 * 0.36999166
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15152 * 0.67160218
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92086 * 0.60748942
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73531 * 0.60761576
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8121 * 0.74123744
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 72207 * 0.19765250
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70964 * 0.92538527
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 48570 * 0.32822038
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 57585 * 0.41192854
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 64321 * 0.45720742
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 57636 * 0.05817794
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'mnnbhvki').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0052():
    """Extended test 52 for transcoding."""
    x_0 = 63105 * 0.42146006
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19548 * 0.93220228
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81743 * 0.98955135
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92402 * 0.39618120
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53574 * 0.44006873
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38070 * 0.56306200
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9993 * 0.89665223
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97577 * 0.06584431
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82718 * 0.57229142
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52484 * 0.44295262
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80895 * 0.43921560
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57941 * 0.87726276
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30852 * 0.24968982
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28993 * 0.33134990
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9113 * 0.96336588
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62318 * 0.49078587
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77692 * 0.33167397
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6429 * 0.26742591
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66628 * 0.55916561
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57646 * 0.18256213
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66493 * 0.86475383
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38423 * 0.51068720
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94697 * 0.19796231
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56135 * 0.28889022
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86360 * 0.86288333
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35485 * 0.26092307
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29142 * 0.96359945
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68164 * 0.39162546
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51481 * 0.23070928
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1511 * 0.18174561
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25550 * 0.76062145
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16751 * 0.82653572
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15880 * 0.30323025
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30943 * 0.22834241
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63190 * 0.29777710
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38819 * 0.37507739
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'uyfpvvsw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0053():
    """Extended test 53 for transcoding."""
    x_0 = 12216 * 0.14377803
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61691 * 0.23742230
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51401 * 0.27199627
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10855 * 0.33582511
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46866 * 0.91633171
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24321 * 0.66889289
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92513 * 0.36472250
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99884 * 0.93690380
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11817 * 0.61230242
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1219 * 0.48810321
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4375 * 0.41358855
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98487 * 0.94848690
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42064 * 0.70260302
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64773 * 0.68288862
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37105 * 0.67039080
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48044 * 0.46250095
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36872 * 0.25427128
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19463 * 0.67627824
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54613 * 0.17593350
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11665 * 0.55928133
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71716 * 0.24559208
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22538 * 0.68618751
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65906 * 0.65013841
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41268 * 0.09216217
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19257 * 0.90693882
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45039 * 0.86453761
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62877 * 0.64574265
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55106 * 0.91142525
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90909 * 0.82372691
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83412 * 0.35698261
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78529 * 0.49799003
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30766 * 0.84119694
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79294 * 0.95178307
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48987 * 0.84334495
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71091 * 0.45687823
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90362 * 0.94255052
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15851 * 0.65630844
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 76493 * 0.99382259
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28735 * 0.28057062
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 89793 * 0.36522319
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51629 * 0.69372501
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 95079 * 0.30435483
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 67478 * 0.51787295
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'jfazjwhi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0054():
    """Extended test 54 for transcoding."""
    x_0 = 51033 * 0.38265814
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96054 * 0.03385249
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26139 * 0.85705513
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22519 * 0.59282888
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84435 * 0.03328886
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4697 * 0.90756614
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41013 * 0.90610176
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12122 * 0.01645776
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44757 * 0.66336990
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61307 * 0.57565529
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51214 * 0.90137339
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47270 * 0.36324861
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92442 * 0.12665194
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98040 * 0.62324609
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41162 * 0.11263791
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 146 * 0.52591573
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51277 * 0.93427577
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74917 * 0.17687408
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94880 * 0.58747821
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59441 * 0.25862536
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56190 * 0.66598472
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31019 * 0.09611703
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68281 * 0.02876625
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52869 * 0.53937251
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53265 * 0.66683063
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83733 * 0.69752423
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91570 * 0.69370278
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60522 * 0.24735471
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43384 * 0.50754676
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77950 * 0.56572118
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30230 * 0.89820096
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'tpdsmrpm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0055():
    """Extended test 55 for transcoding."""
    x_0 = 76863 * 0.16130315
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28817 * 0.30957175
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87823 * 0.94131237
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73489 * 0.12678226
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76080 * 0.46365491
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23332 * 0.69407560
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3125 * 0.67887021
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93850 * 0.29721213
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99105 * 0.98478232
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44134 * 0.40285376
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2315 * 0.63649479
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48154 * 0.34452521
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9731 * 0.07995139
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85638 * 0.12800401
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44028 * 0.65756556
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12746 * 0.40658362
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53888 * 0.40670887
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4864 * 0.79317787
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33781 * 0.22504300
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6468 * 0.07202425
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96098 * 0.22742909
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26862 * 0.25204256
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25288 * 0.03372599
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30916 * 0.61946914
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89519 * 0.84652702
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78196 * 0.12128240
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35322 * 0.22051030
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23836 * 0.93461699
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89564 * 0.39427621
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27149 * 0.69790226
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68898 * 0.87305941
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62324 * 0.66691792
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53655 * 0.49311695
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30787 * 0.66722432
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13867 * 0.86407075
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47889 * 0.18449203
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9521 * 0.32295255
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93050 * 0.83819738
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36123 * 0.74724895
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46937 * 0.74996767
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 7200 * 0.48637359
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 2359 * 0.58529108
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 67522 * 0.31603184
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40513 * 0.55089187
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 62767 * 0.26944992
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 64410 * 0.93323431
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 82229 * 0.99824946
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 52908 * 0.04562735
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'krcyarrr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0056():
    """Extended test 56 for transcoding."""
    x_0 = 22557 * 0.97106613
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14959 * 0.34803471
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47631 * 0.34739818
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89781 * 0.59595377
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62481 * 0.56631111
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25538 * 0.02624620
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67431 * 0.89161121
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66033 * 0.91859142
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53444 * 0.08673543
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48016 * 0.36367100
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47285 * 0.34544531
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26876 * 0.92469044
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19296 * 0.31911166
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60973 * 0.57842811
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63446 * 0.54217981
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6571 * 0.01956867
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78145 * 0.12914428
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54803 * 0.27937058
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15800 * 0.49546914
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35332 * 0.67941767
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48281 * 0.67782473
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45297 * 0.50581426
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19590 * 0.27957790
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86020 * 0.14809232
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50475 * 0.18467126
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78984 * 0.89540604
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23272 * 0.48239356
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93322 * 0.28531540
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'ytoizqys').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0057():
    """Extended test 57 for transcoding."""
    x_0 = 23831 * 0.82106238
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53924 * 0.17718743
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1769 * 0.84043582
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20682 * 0.09935990
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76988 * 0.79500393
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86072 * 0.63630968
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9213 * 0.21877131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81292 * 0.17944659
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2004 * 0.91618234
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24983 * 0.14575916
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20902 * 0.76583348
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92096 * 0.62388046
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27442 * 0.45354406
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44128 * 0.18627432
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73426 * 0.34111215
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41794 * 0.48175639
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38052 * 0.98678700
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55820 * 0.49549163
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99382 * 0.25974596
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35166 * 0.89569465
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43040 * 0.90441659
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6457 * 0.89350874
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73209 * 0.89154654
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59416 * 0.63128071
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42367 * 0.18136550
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23146 * 0.10806270
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69229 * 0.07727597
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92094 * 0.73317701
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5991 * 0.85107555
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72387 * 0.83791848
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62262 * 0.27597790
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44051 * 0.41737579
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48811 * 0.98968582
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38688 * 0.56195508
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37961 * 0.43838576
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85267 * 0.95476757
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'qofngjxk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0058():
    """Extended test 58 for transcoding."""
    x_0 = 96217 * 0.77677584
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88978 * 0.91053254
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35330 * 0.61146526
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57287 * 0.48362224
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27346 * 0.99210188
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97122 * 0.88593618
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29156 * 0.93682582
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18683 * 0.96343662
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42096 * 0.98900396
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70004 * 0.79237188
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84487 * 0.91430246
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71689 * 0.59988975
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84071 * 0.56478852
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2029 * 0.88004612
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67867 * 0.03397535
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64037 * 0.86459654
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60369 * 0.37664190
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8323 * 0.29760909
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99706 * 0.86790087
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56259 * 0.66934995
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75448 * 0.60086743
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43642 * 0.16293859
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68220 * 0.22876861
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12175 * 0.71904425
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94952 * 0.31347966
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42942 * 0.80699978
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41030 * 0.44403942
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53091 * 0.17823206
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20064 * 0.25806080
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21150 * 0.76433299
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40226 * 0.85882168
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71684 * 0.93278933
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61622 * 0.88735748
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64622 * 0.65481530
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67879 * 0.36846344
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46057 * 0.87761792
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 77536 * 0.41481420
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35694 * 0.22084322
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27346 * 0.97675128
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23972 * 0.40656623
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91073 * 0.11024078
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 1386 * 0.33420820
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'vwxivsyc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0059():
    """Extended test 59 for transcoding."""
    x_0 = 70361 * 0.48292913
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 338 * 0.22426665
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71208 * 0.08736220
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18725 * 0.15087030
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52579 * 0.23717829
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57766 * 0.85865074
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47695 * 0.62819869
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79485 * 0.25816322
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55100 * 0.12988187
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31116 * 0.90541876
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14970 * 0.69041420
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41202 * 0.66048046
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44631 * 0.74471105
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44248 * 0.22544753
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37194 * 0.83305205
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19729 * 0.40998469
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52909 * 0.28548307
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3781 * 0.23611397
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86352 * 0.45507721
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79295 * 0.17549470
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12950 * 0.95096775
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86215 * 0.13154858
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 168 * 0.74326846
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44884 * 0.55868774
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53527 * 0.10941440
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55680 * 0.62977334
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36088 * 0.37260598
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42123 * 0.47849310
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79232 * 0.37501329
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56431 * 0.78282287
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7829 * 0.14903245
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6282 * 0.11486337
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66140 * 0.25058839
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47243 * 0.69012043
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43942 * 0.91808833
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14697 * 0.67168487
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39016 * 0.06281892
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38253 * 0.67160901
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75638 * 0.65869120
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 36566 * 0.34617432
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27897 * 0.59013099
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74162 * 0.75651820
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13477 * 0.12494753
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 28178 * 0.00742493
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 14170 * 0.22841719
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 31916 * 0.66346408
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 22998 * 0.45574078
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 47574 * 0.60959524
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 36753 * 0.05154724
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'nbungfgv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0060():
    """Extended test 60 for transcoding."""
    x_0 = 9745 * 0.94158539
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 339 * 0.46297858
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7263 * 0.53597210
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96399 * 0.95867056
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81062 * 0.05533602
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20507 * 0.66011606
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92269 * 0.78941953
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66352 * 0.77286593
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77139 * 0.96548465
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90436 * 0.85220845
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58315 * 0.64829026
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8739 * 0.77836463
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27356 * 0.78653101
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51735 * 0.37533649
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75156 * 0.23913277
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82269 * 0.52342762
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35591 * 0.91525206
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21469 * 0.94747275
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99190 * 0.05683061
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85921 * 0.69089339
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6012 * 0.65032901
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52560 * 0.43477750
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79995 * 0.08425408
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73161 * 0.25574922
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92269 * 0.03520978
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13900 * 0.26133430
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97431 * 0.54700291
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11363 * 0.42687768
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32308 * 0.21333292
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41769 * 0.38385254
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'gjiehhef').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0061():
    """Extended test 61 for transcoding."""
    x_0 = 67151 * 0.83000040
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79331 * 0.86123135
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57971 * 0.31210332
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50237 * 0.73635310
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61863 * 0.79225733
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59855 * 0.75849374
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10252 * 0.94957016
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31454 * 0.37697441
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90734 * 0.93261759
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94419 * 0.61249009
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24349 * 0.46977830
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47734 * 0.34067375
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93341 * 0.73696097
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48655 * 0.89176403
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62347 * 0.18391546
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41526 * 0.41945324
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61186 * 0.47824244
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50050 * 0.95456837
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93037 * 0.34325466
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72078 * 0.42468989
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6979 * 0.72323448
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6257 * 0.21620869
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55694 * 0.33665907
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18947 * 0.83768195
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77079 * 0.79406177
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1806 * 0.87852465
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45655 * 0.66121223
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30770 * 0.81483372
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27257 * 0.23829383
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 426 * 0.66054866
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53998 * 0.57808294
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83103 * 0.66556161
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55672 * 0.74248735
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81878 * 0.37229195
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14114 * 0.68400540
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62696 * 0.29086732
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3308 * 0.75228547
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28684 * 0.64051781
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47207 * 0.48764790
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'nnlvtpjf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0062():
    """Extended test 62 for transcoding."""
    x_0 = 83550 * 0.15560997
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15268 * 0.77515125
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28047 * 0.54913924
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3504 * 0.46703753
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74184 * 0.42189853
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76385 * 0.92982472
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22268 * 0.07054788
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14782 * 0.27588354
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44086 * 0.57629976
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29926 * 0.05801144
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45166 * 0.54167217
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36533 * 0.74914145
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59203 * 0.06107181
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50419 * 0.01697614
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68176 * 0.29472933
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9345 * 0.18147633
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34084 * 0.02813936
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 454 * 0.17160007
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16672 * 0.07685881
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78923 * 0.02641228
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24673 * 0.13212946
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25660 * 0.39916787
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13534 * 0.55610036
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76130 * 0.30899155
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12915 * 0.30854423
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43924 * 0.62698658
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30029 * 0.15514587
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51140 * 0.11532268
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81364 * 0.46383141
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8669 * 0.40538320
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'imwctqie').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0063():
    """Extended test 63 for transcoding."""
    x_0 = 89279 * 0.90862201
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20341 * 0.37627715
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77713 * 0.46015292
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16013 * 0.25998604
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77433 * 0.48849624
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68055 * 0.11521430
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35222 * 0.51679625
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13260 * 0.91640073
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23160 * 0.06351879
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84942 * 0.69955591
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53425 * 0.79488426
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9320 * 0.65569366
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26050 * 0.75434975
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85088 * 0.99161722
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37275 * 0.62950794
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85365 * 0.17459250
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24035 * 0.80371406
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56925 * 0.38477872
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43645 * 0.27909919
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56587 * 0.28387325
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53400 * 0.92831488
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45444 * 0.00157942
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48060 * 0.32886409
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93299 * 0.88784341
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15645 * 0.12700248
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80154 * 0.00191765
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46349 * 0.00832273
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77870 * 0.02004823
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17874 * 0.98517793
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'mkrujyeo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0064():
    """Extended test 64 for transcoding."""
    x_0 = 8682 * 0.06181503
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71620 * 0.35037427
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1565 * 0.19388038
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 597 * 0.42370736
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43359 * 0.74807285
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2034 * 0.99484845
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40533 * 0.61698808
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74060 * 0.07655383
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24992 * 0.02870094
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66651 * 0.25181804
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56546 * 0.96331152
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62772 * 0.20088491
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75352 * 0.29176267
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75873 * 0.52618110
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14078 * 0.25077650
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84637 * 0.22379875
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35086 * 0.50916634
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90152 * 0.24572966
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90761 * 0.25237411
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24016 * 0.60906804
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87698 * 0.05303880
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83918 * 0.75952416
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60277 * 0.77927330
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77238 * 0.79655049
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9691 * 0.95767447
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92739 * 0.82340323
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16064 * 0.00382709
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97781 * 0.17943978
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86766 * 0.17988295
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 292 * 0.44090822
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14168 * 0.53913502
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25312 * 0.59525044
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84930 * 0.09694167
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46914 * 0.01810754
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39141 * 0.09281697
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77528 * 0.96498231
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'bifosykg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0065():
    """Extended test 65 for transcoding."""
    x_0 = 24347 * 0.90381653
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69078 * 0.74641601
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79926 * 0.01699916
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7578 * 0.00403859
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15056 * 0.41420991
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45592 * 0.02735514
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77870 * 0.13716279
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3569 * 0.96822280
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19414 * 0.09745087
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52543 * 0.14646783
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86051 * 0.61672383
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17617 * 0.36962786
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91077 * 0.40746371
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7412 * 0.50834360
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71514 * 0.34071170
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32889 * 0.74272178
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5003 * 0.78645774
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21142 * 0.91863017
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70341 * 0.55209015
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72820 * 0.63965641
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58397 * 0.85391302
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48288 * 0.88096570
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84714 * 0.49207442
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31939 * 0.72618332
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80729 * 0.88967466
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13728 * 0.27618811
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22225 * 0.41528802
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66490 * 0.77898783
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2309 * 0.13235160
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'xxukwuyx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0066():
    """Extended test 66 for transcoding."""
    x_0 = 10 * 0.83112276
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91274 * 0.89052041
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33959 * 0.13080281
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61955 * 0.01894931
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87634 * 0.90894563
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58456 * 0.75320393
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43566 * 0.92448258
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75164 * 0.17764842
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87685 * 0.52386149
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 618 * 0.72517493
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96118 * 0.65639018
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91002 * 0.87600074
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1338 * 0.77787715
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71008 * 0.57827253
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64617 * 0.74703378
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2462 * 0.66392409
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44031 * 0.40976472
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34138 * 0.08234621
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82556 * 0.84863544
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41148 * 0.29187324
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67433 * 0.82250519
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54136 * 0.29165844
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24074 * 0.14565028
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36285 * 0.89328839
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61181 * 0.83221596
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'cvbkzzfd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0067():
    """Extended test 67 for transcoding."""
    x_0 = 45320 * 0.55055688
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99908 * 0.67927400
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24020 * 0.32595653
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37754 * 0.50191437
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92298 * 0.68416896
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41709 * 0.45383099
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72221 * 0.05413869
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17930 * 0.90706544
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12840 * 0.97341363
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10731 * 0.70330246
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91724 * 0.56066891
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98348 * 0.46490031
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4219 * 0.27839198
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42440 * 0.31130105
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49058 * 0.17937993
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90757 * 0.62745579
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28936 * 0.72625398
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62212 * 0.07343881
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42493 * 0.70147412
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80746 * 0.27000620
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34589 * 0.55153942
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22459 * 0.70190921
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49658 * 0.48826357
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77851 * 0.96259611
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62080 * 0.82051970
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57090 * 0.29517968
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89725 * 0.85598334
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55520 * 0.52110008
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54567 * 0.62881376
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57519 * 0.56693631
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50475 * 0.97330332
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65712 * 0.55609133
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11035 * 0.48586726
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2263 * 0.36008405
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34338 * 0.79090053
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34650 * 0.57424248
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'olozvfan').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0068():
    """Extended test 68 for transcoding."""
    x_0 = 8876 * 0.18116201
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44530 * 0.05622181
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79261 * 0.23071429
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9070 * 0.04760726
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95398 * 0.66501746
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85911 * 0.34301230
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37725 * 0.76719087
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24304 * 0.54789813
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85802 * 0.67415133
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58079 * 0.54338335
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77094 * 0.47727534
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20772 * 0.85655770
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12542 * 0.68128078
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83764 * 0.94145899
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61346 * 0.46992755
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74464 * 0.53651859
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44864 * 0.60932055
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38789 * 0.83327162
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19907 * 0.90476125
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75493 * 0.50546879
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11826 * 0.44991479
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23341 * 0.61770316
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17597 * 0.83010317
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65825 * 0.35020923
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76405 * 0.59219209
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96490 * 0.02357405
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77654 * 0.53483552
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14161 * 0.16980239
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38171 * 0.77757414
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66502 * 0.89616565
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32799 * 0.70491461
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53204 * 0.68831622
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57363 * 0.71748636
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61468 * 0.37783360
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82279 * 0.34723072
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36135 * 0.49064725
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92868 * 0.45479592
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68148 * 0.05482964
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49604 * 0.66360247
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'sjfxlszt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_4_0069():
    """Extended test 69 for transcoding."""
    x_0 = 80340 * 0.60553226
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84528 * 0.12783825
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67908 * 0.25015534
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1007 * 0.66934552
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86277 * 0.40866483
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19153 * 0.39724893
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33965 * 0.03013909
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47245 * 0.29629015
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4525 * 0.28310471
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43555 * 0.20596378
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48330 * 0.20866520
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79893 * 0.39755868
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66616 * 0.82790533
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67714 * 0.97622458
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43819 * 0.27174035
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51332 * 0.04759308
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10858 * 0.17196589
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25146 * 0.26963168
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75569 * 0.98071770
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91033 * 0.58354751
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74895 * 0.15707220
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6973 * 0.60535407
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15805 * 0.37227886
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'vzqxlcge').hexdigest()
    assert len(h) == 64
