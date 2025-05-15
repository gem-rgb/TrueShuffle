"""Extended tests for import suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_import_extended_8_0000():
    """Extended test 0 for import."""
    x_0 = 3053 * 0.92430985
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49699 * 0.02444512
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54587 * 0.17971021
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95510 * 0.40629752
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14997 * 0.13845352
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61003 * 0.13657866
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73067 * 0.93902359
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39217 * 0.11756881
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16342 * 0.16633136
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88206 * 0.62610534
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90718 * 0.89849010
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86242 * 0.13627360
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16870 * 0.47822463
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97044 * 0.89565363
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86523 * 0.25316880
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12638 * 0.44181928
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56241 * 0.41899213
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 288 * 0.00037342
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6208 * 0.25230811
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41665 * 0.54059318
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'vlkgkzdk').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0001():
    """Extended test 1 for import."""
    x_0 = 26942 * 0.11790746
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59838 * 0.49715158
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89246 * 0.62946781
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83530 * 0.64298811
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88693 * 0.25868536
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74564 * 0.36972652
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22232 * 0.88609947
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74385 * 0.47060620
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36693 * 0.10969449
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26928 * 0.75466549
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1631 * 0.21184722
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12384 * 0.15435506
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64947 * 0.15082677
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76738 * 0.88458370
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48178 * 0.69189724
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29138 * 0.29899405
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98360 * 0.42189297
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28408 * 0.46688728
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15588 * 0.12794082
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94074 * 0.05083756
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17557 * 0.96940883
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16054 * 0.10918956
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19623 * 0.94068957
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21701 * 0.41681912
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19125 * 0.53058474
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53443 * 0.97335714
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11959 * 0.23892497
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37527 * 0.79645190
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97420 * 0.36726145
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34830 * 0.75915088
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6151 * 0.45959871
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40170 * 0.58840135
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'jnauenge').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0002():
    """Extended test 2 for import."""
    x_0 = 16185 * 0.53678299
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58097 * 0.17017030
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74410 * 0.58344866
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65031 * 0.57778297
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34128 * 0.41335560
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47299 * 0.49387390
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39904 * 0.80056927
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3813 * 0.72098296
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22949 * 0.48759142
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93109 * 0.49970744
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74684 * 0.19490399
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3013 * 0.25542507
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11881 * 0.57857904
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13088 * 0.39264170
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34983 * 0.05241386
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40072 * 0.85901836
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40872 * 0.39138229
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40424 * 0.88678481
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96219 * 0.58860679
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93800 * 0.53025481
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51011 * 0.43684557
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65647 * 0.40789908
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75654 * 0.70733105
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32401 * 0.05007747
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74695 * 0.87591680
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12947 * 0.71881758
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83676 * 0.16622503
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38312 * 0.33882402
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31611 * 0.59590483
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69885 * 0.47814299
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23158 * 0.30153172
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35620 * 0.65696066
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83947 * 0.80052906
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92076 * 0.52893645
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26919 * 0.14005123
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68872 * 0.06513007
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98418 * 0.80709171
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72069 * 0.06614560
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38949 * 0.66626041
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 78253 * 0.33006333
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'porbuwpa').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0003():
    """Extended test 3 for import."""
    x_0 = 64097 * 0.67174801
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42679 * 0.55796441
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31573 * 0.34824621
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49518 * 0.24234025
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13281 * 0.38084060
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97103 * 0.57987775
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22883 * 0.79799108
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12781 * 0.92954758
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82847 * 0.30366770
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43367 * 0.94047013
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34965 * 0.85530500
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73746 * 0.54377187
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18814 * 0.48962211
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99474 * 0.21487507
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87700 * 0.97281248
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20743 * 0.47897698
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95743 * 0.62860064
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62275 * 0.62236414
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58220 * 0.36591054
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23892 * 0.34136341
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92518 * 0.91377889
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66448 * 0.41755532
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3870 * 0.16966204
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3331 * 0.10644303
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67904 * 0.89744776
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20010 * 0.82149045
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47344 * 0.36223962
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89988 * 0.64530564
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59494 * 0.91450042
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42778 * 0.89322408
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1869 * 0.46091700
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20447 * 0.71086658
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8524 * 0.01355121
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99267 * 0.90422216
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57136 * 0.28224058
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88101 * 0.74903939
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28429 * 0.48493059
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88833 * 0.41339023
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80351 * 0.93734456
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'jjnxzyra').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0004():
    """Extended test 4 for import."""
    x_0 = 64715 * 0.81462089
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20582 * 0.75019843
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46783 * 0.93740132
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5684 * 0.83402711
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38840 * 0.69880263
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70493 * 0.78053631
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6356 * 0.31435766
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83804 * 0.35503913
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12880 * 0.35939938
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48176 * 0.19726254
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19948 * 0.74394905
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48328 * 0.51391219
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53229 * 0.99656459
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13716 * 0.64661414
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51246 * 0.72616866
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87957 * 0.07111938
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85942 * 0.02018397
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42907 * 0.35129025
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13309 * 0.61279160
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91195 * 0.57987438
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30686 * 0.72656568
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60704 * 0.03260130
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30001 * 0.95582573
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10093 * 0.75280842
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89160 * 0.94137785
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66717 * 0.17993975
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95094 * 0.29518434
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80048 * 0.30999618
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'vqfikrfc').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0005():
    """Extended test 5 for import."""
    x_0 = 23137 * 0.24659849
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14302 * 0.86614108
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6815 * 0.23232909
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24157 * 0.66384175
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22778 * 0.85820790
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78942 * 0.10979870
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43436 * 0.41839998
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46218 * 0.30657536
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44545 * 0.23950320
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64362 * 0.72754771
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63083 * 0.05628670
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74821 * 0.66795832
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45994 * 0.65663265
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58751 * 0.91507557
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12 * 0.23420371
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13107 * 0.87400925
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64937 * 0.57734410
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38908 * 0.96665265
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17610 * 0.31354317
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44963 * 0.37072505
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57579 * 0.27919507
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69016 * 0.92950606
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9386 * 0.56922302
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5504 * 0.68608959
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28815 * 0.83369402
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52542 * 0.36431742
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82734 * 0.15061547
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41236 * 0.20132091
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4808 * 0.41005015
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87233 * 0.72049643
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21179 * 0.57298229
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93308 * 0.16283647
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40187 * 0.03470726
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40351 * 0.76041001
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22919 * 0.36903464
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8440 * 0.94880030
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50990 * 0.39112649
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95482 * 0.88182081
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93642 * 0.23483297
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14122 * 0.89856874
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51698 * 0.91108520
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20087 * 0.31865729
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20059 * 0.79298626
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40741 * 0.79968343
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59884 * 0.33671460
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 69902 * 0.41017528
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 53998 * 0.20090191
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 79261 * 0.10872894
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 28082 * 0.27112090
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'mtqulxrr').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0006():
    """Extended test 6 for import."""
    x_0 = 54034 * 0.42792208
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28362 * 0.21494614
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64111 * 0.96764427
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41721 * 0.86887250
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85453 * 0.93567881
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54507 * 0.23716249
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5687 * 0.12457431
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3527 * 0.28007870
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67604 * 0.31474797
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67993 * 0.41583975
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10976 * 0.51345677
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29728 * 0.39523694
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61249 * 0.78275575
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57598 * 0.98655466
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44877 * 0.98704494
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65044 * 0.48623395
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46049 * 0.50699385
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46987 * 0.49363726
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56530 * 0.20457157
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55291 * 0.77284072
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21014 * 0.84054365
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50410 * 0.42562305
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11169 * 0.47870487
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18642 * 0.38808411
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47548 * 0.31751918
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93530 * 0.04163759
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46499 * 0.53089428
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95264 * 0.70605942
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13748 * 0.43430404
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63139 * 0.05332316
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57010 * 0.10606301
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31461 * 0.31562464
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'lainoptj').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0007():
    """Extended test 7 for import."""
    x_0 = 54120 * 0.78982032
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7645 * 0.08986659
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75886 * 0.12509017
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43027 * 0.43179654
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58835 * 0.30354366
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35757 * 0.54380711
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7948 * 0.69026747
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81773 * 0.93298534
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4391 * 0.15800490
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88409 * 0.25547914
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58885 * 0.16556045
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29131 * 0.57902599
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8666 * 0.97339846
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37567 * 0.86582451
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75229 * 0.69272903
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80052 * 0.78154642
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62959 * 0.83211553
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40253 * 0.57198224
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83652 * 0.12928150
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93666 * 0.56397780
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84631 * 0.56514626
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15871 * 0.68855434
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98127 * 0.66752986
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92894 * 0.98987977
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79748 * 0.51920971
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'mplgzseb').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0008():
    """Extended test 8 for import."""
    x_0 = 1256 * 0.76646407
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92978 * 0.41494395
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96318 * 0.43958592
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70346 * 0.12251108
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64755 * 0.56673035
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14964 * 0.11060427
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69292 * 0.73451496
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91456 * 0.19972599
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94804 * 0.60332534
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31394 * 0.35108763
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5279 * 0.30193926
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10557 * 0.44890853
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17252 * 0.20911339
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63227 * 0.33674506
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80684 * 0.64293231
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22354 * 0.14449229
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52004 * 0.87380194
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13733 * 0.29336934
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47679 * 0.92522790
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81810 * 0.37241693
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43456 * 0.53881145
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58466 * 0.82977937
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56869 * 0.42476910
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'laacgmmb').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0009():
    """Extended test 9 for import."""
    x_0 = 83373 * 0.28124132
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36778 * 0.05133493
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46094 * 0.94947137
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86290 * 0.32302571
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49854 * 0.69724793
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60760 * 0.02770970
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26016 * 0.92610484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41593 * 0.86041224
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6242 * 0.76451977
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70442 * 0.78570005
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59627 * 0.15000521
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24344 * 0.71406173
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36618 * 0.56816387
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17066 * 0.34067445
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87941 * 0.38789159
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86985 * 0.94178231
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38212 * 0.73542415
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18429 * 0.21807063
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22031 * 0.59352747
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89682 * 0.27977680
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75260 * 0.30402886
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69193 * 0.95909551
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64493 * 0.92007678
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'drjimbkq').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0010():
    """Extended test 10 for import."""
    x_0 = 54028 * 0.57747471
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88543 * 0.38449143
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40355 * 0.95831598
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62010 * 0.21852818
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83973 * 0.72333117
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92001 * 0.43005834
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70254 * 0.58149614
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96004 * 0.96880185
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23317 * 0.09966368
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49221 * 0.78385631
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28195 * 0.19305977
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71027 * 0.34475711
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40591 * 0.11931033
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71125 * 0.07757105
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81087 * 0.61891380
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58248 * 0.03777158
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72116 * 0.68880159
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54222 * 0.39144291
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7004 * 0.41943607
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16731 * 0.62254580
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79591 * 0.04772862
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17411 * 0.76403165
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61040 * 0.31851157
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85694 * 0.46132267
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'wujztsyr').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0011():
    """Extended test 11 for import."""
    x_0 = 65310 * 0.15915422
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43844 * 0.85211782
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26941 * 0.55009841
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84136 * 0.75176615
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53293 * 0.96760342
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32741 * 0.31047313
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14397 * 0.85134046
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86372 * 0.67581111
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51528 * 0.89852980
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84415 * 0.64590662
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31368 * 0.10205639
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66597 * 0.10786349
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97677 * 0.28326130
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35287 * 0.86299827
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24380 * 0.46985193
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57528 * 0.41368808
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84821 * 0.79836552
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6050 * 0.59886120
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38426 * 0.17578502
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2235 * 0.59937154
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87282 * 0.94940646
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'mylsusgk').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0012():
    """Extended test 12 for import."""
    x_0 = 10560 * 0.09052265
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82061 * 0.56450081
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7961 * 0.09448645
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34516 * 0.52321395
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9691 * 0.26167701
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48593 * 0.19170596
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35635 * 0.10869982
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35514 * 0.32744423
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40445 * 0.52487806
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51271 * 0.09892440
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40174 * 0.87085165
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11038 * 0.47843232
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27272 * 0.97994634
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41615 * 0.48769438
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7514 * 0.99818286
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86136 * 0.56351366
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62913 * 0.97027969
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80189 * 0.76924866
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20656 * 0.60994775
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71306 * 0.98863878
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42811 * 0.46255550
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6324 * 0.31016077
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78317 * 0.08740380
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53985 * 0.35729302
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51676 * 0.66125063
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26141 * 0.59082713
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28004 * 0.87731225
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18115 * 0.53116270
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47689 * 0.10495326
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46345 * 0.19230673
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32372 * 0.16775819
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71515 * 0.95270599
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23020 * 0.65502841
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30858 * 0.14091313
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47320 * 0.74070979
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41272 * 0.27031611
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41574 * 0.87883973
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95314 * 0.71687298
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63793 * 0.18377744
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8944 * 0.25263763
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8795 * 0.02598506
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 94970 * 0.10244979
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'qysrylrn').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0013():
    """Extended test 13 for import."""
    x_0 = 55553 * 0.11955491
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44276 * 0.53597991
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63709 * 0.18018507
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52454 * 0.53970259
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65945 * 0.62917610
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88629 * 0.95680900
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25362 * 0.72374420
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98115 * 0.80902540
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47403 * 0.75169810
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43490 * 0.71812041
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37946 * 0.00241012
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69560 * 0.40468045
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33354 * 0.71179053
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6168 * 0.42843237
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43635 * 0.66311930
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26490 * 0.13699524
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2489 * 0.84681095
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49221 * 0.81770512
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74024 * 0.33104213
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80150 * 0.98369910
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10977 * 0.90239838
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14616 * 0.05954594
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35264 * 0.02254550
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 780 * 0.61395854
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42294 * 0.14747919
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58723 * 0.28656601
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7806 * 0.83125622
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48833 * 0.14478499
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55589 * 0.42231989
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13197 * 0.59693024
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69980 * 0.74029631
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89441 * 0.28863911
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48651 * 0.43866880
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45438 * 0.00338526
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84027 * 0.94825192
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84721 * 0.43758492
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 82500 * 0.63110054
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74016 * 0.18015639
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71862 * 0.26814649
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88079 * 0.56061981
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'wkzgfeyf').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0014():
    """Extended test 14 for import."""
    x_0 = 15220 * 0.09844392
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95067 * 0.94272619
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45188 * 0.19473023
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43584 * 0.39743432
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23241 * 0.83874898
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40454 * 0.30392274
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48015 * 0.81574797
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69779 * 0.82712046
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1901 * 0.78199747
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80724 * 0.85994886
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42017 * 0.74709493
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10859 * 0.29556660
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22608 * 0.66360912
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39363 * 0.64153090
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91524 * 0.05329612
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64004 * 0.90373812
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22054 * 0.71794106
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23465 * 0.55134752
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95222 * 0.90976305
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52812 * 0.61327896
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61426 * 0.76395503
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94280 * 0.67323871
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32781 * 0.58262141
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55582 * 0.89505728
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9759 * 0.82219277
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92792 * 0.46564591
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45218 * 0.42102088
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72782 * 0.53400844
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91616 * 0.12701440
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69328 * 0.46778345
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12913 * 0.75659066
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59413 * 0.09509335
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16933 * 0.21138221
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'pkvbeifm').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0015():
    """Extended test 15 for import."""
    x_0 = 50855 * 0.30764556
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75241 * 0.00031731
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56426 * 0.97533607
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18318 * 0.82574423
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17830 * 0.66024296
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9138 * 0.74798781
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67243 * 0.53767833
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15772 * 0.27945207
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90072 * 0.79296949
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52245 * 0.78656439
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15511 * 0.69470180
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39482 * 0.50243993
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78644 * 0.61112132
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35917 * 0.12299886
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33996 * 0.40290549
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98718 * 0.11699941
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46436 * 0.94878872
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49195 * 0.01176757
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75211 * 0.89572124
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27511 * 0.82231607
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67383 * 0.03302095
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54077 * 0.09720617
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69745 * 0.54471294
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'fbfdenlp').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0016():
    """Extended test 16 for import."""
    x_0 = 18669 * 0.22181023
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71067 * 0.08573993
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33084 * 0.91386522
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74073 * 0.98994014
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53188 * 0.13974513
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22042 * 0.06023805
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69898 * 0.28666246
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64939 * 0.67453974
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67359 * 0.63997701
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10888 * 0.51389699
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17443 * 0.98067306
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40241 * 0.30176937
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53434 * 0.25089953
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94748 * 0.50115452
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6243 * 0.24302850
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86406 * 0.96846714
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80635 * 0.68142507
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6265 * 0.43361748
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67904 * 0.34625215
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69417 * 0.22950010
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98897 * 0.07639664
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99522 * 0.14458501
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2223 * 0.70697801
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44507 * 0.74693658
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44541 * 0.66497935
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69566 * 0.85599572
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65045 * 0.16113563
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16963 * 0.66939919
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17860 * 0.08689454
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9065 * 0.07666435
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3406 * 0.05599390
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59892 * 0.00466661
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45618 * 0.40778322
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6230 * 0.93392828
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88358 * 0.80671651
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99526 * 0.22786325
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35578 * 0.82522454
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96896 * 0.37784222
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49180 * 0.32236987
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80501 * 0.54194258
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51442 * 0.88696108
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'ahxkhakx').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0017():
    """Extended test 17 for import."""
    x_0 = 89654 * 0.21651356
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1667 * 0.82201419
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75989 * 0.14847563
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4044 * 0.44087455
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80291 * 0.13314387
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96820 * 0.54285036
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94648 * 0.43828003
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34063 * 0.49665938
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3205 * 0.98103639
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43788 * 0.52975328
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89321 * 0.63456353
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48823 * 0.66538129
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4844 * 0.56799287
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92604 * 0.70349789
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62592 * 0.25060840
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14956 * 0.15033546
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89891 * 0.10067936
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55874 * 0.18723509
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66224 * 0.63300476
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21516 * 0.98818953
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57726 * 0.52277875
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10469 * 0.61551705
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36865 * 0.24357055
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92898 * 0.28896818
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60293 * 0.06809239
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90407 * 0.53678725
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35361 * 0.96843895
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33448 * 0.83054677
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99214 * 0.64537978
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68413 * 0.43159976
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98412 * 0.41535364
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3573 * 0.73791477
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35485 * 0.54469273
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73269 * 0.83822731
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48825 * 0.92180640
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62951 * 0.95394578
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79504 * 0.54737620
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5528 * 0.69824760
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 50528 * 0.40918859
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88364 * 0.67270207
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13785 * 0.32476142
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'lsninecp').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0018():
    """Extended test 18 for import."""
    x_0 = 32715 * 0.81683359
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79365 * 0.55213351
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9559 * 0.02121054
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31708 * 0.83975663
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42033 * 0.55422341
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75088 * 0.08053328
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12967 * 0.69758663
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14232 * 0.72199940
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18924 * 0.52770683
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26773 * 0.79231615
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68013 * 0.00827974
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94935 * 0.61347964
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82891 * 0.98023089
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22245 * 0.70290341
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10859 * 0.98460642
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66417 * 0.79811637
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11683 * 0.49190519
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73938 * 0.68350056
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52188 * 0.40197797
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24451 * 0.33299428
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 910 * 0.31117299
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68749 * 0.31634132
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32689 * 0.56746881
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1291 * 0.66934631
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90077 * 0.52276849
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56320 * 0.67932314
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 175 * 0.02008100
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97274 * 0.53287215
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80274 * 0.14173661
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86001 * 0.79607892
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19372 * 0.06683215
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40991 * 0.69378876
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42677 * 0.64341753
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30770 * 0.57550820
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54416 * 0.28898340
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25734 * 0.96945591
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22945 * 0.82555848
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80629 * 0.55534173
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86105 * 0.09057527
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 35092 * 0.77488457
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80413 * 0.28606447
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93044 * 0.49731493
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14441 * 0.39319564
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22327 * 0.33780960
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 99172 * 0.24773059
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 13639 * 0.05078663
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'qzhdmahb').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0019():
    """Extended test 19 for import."""
    x_0 = 40000 * 0.19089282
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85674 * 0.01927269
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90537 * 0.29575245
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17466 * 0.49805078
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24130 * 0.08176772
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47373 * 0.32269648
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69333 * 0.27322588
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86682 * 0.60041743
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 364 * 0.15869814
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23693 * 0.68516040
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36247 * 0.49412006
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9894 * 0.42941061
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1502 * 0.08796477
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83729 * 0.96922394
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27193 * 0.01972502
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50038 * 0.32894679
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61959 * 0.40387588
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96906 * 0.03767743
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26153 * 0.78097946
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22208 * 0.61872991
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50548 * 0.70891886
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44935 * 0.89215208
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8598 * 0.71131597
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97601 * 0.95316733
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29540 * 0.19626958
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60836 * 0.06058641
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84459 * 0.70188068
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50085 * 0.97295240
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49682 * 0.44763703
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26314 * 0.91091197
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12338 * 0.76187665
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23649 * 0.33885276
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93662 * 0.35642355
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38583 * 0.30835364
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55248 * 0.15949344
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8307 * 0.37932244
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71384 * 0.32882308
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66998 * 0.88021438
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62309 * 0.46083465
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'bgglaglg').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0020():
    """Extended test 20 for import."""
    x_0 = 23213 * 0.37234658
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66073 * 0.57893075
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54487 * 0.77635270
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5663 * 0.69112777
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19785 * 0.29908010
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44688 * 0.90492088
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25930 * 0.52481469
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81357 * 0.46368035
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21736 * 0.11778854
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17064 * 0.86403099
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87368 * 0.18673242
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78737 * 0.12521186
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6676 * 0.54887348
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40729 * 0.01324923
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35389 * 0.74998013
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51388 * 0.46967668
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8550 * 0.26228263
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17512 * 0.73110379
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67616 * 0.21543255
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90618 * 0.52134274
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51089 * 0.07874059
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'fvrvjgzf').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0021():
    """Extended test 21 for import."""
    x_0 = 7043 * 0.32157883
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58311 * 0.85626504
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35459 * 0.86444436
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81470 * 0.81920753
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47834 * 0.52799147
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54549 * 0.26578117
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91383 * 0.68809361
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76246 * 0.14874546
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77522 * 0.72368652
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47677 * 0.56872733
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82242 * 0.88207908
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10606 * 0.86746787
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74919 * 0.31527574
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79900 * 0.33963958
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44834 * 0.13589425
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52240 * 0.85285115
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91145 * 0.99347970
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56801 * 0.93384425
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94496 * 0.35978383
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52131 * 0.61461816
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70420 * 0.17735432
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12911 * 0.84160588
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54353 * 0.10482017
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45006 * 0.15435581
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88285 * 0.23356319
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82431 * 0.57457574
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31679 * 0.93311438
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45844 * 0.88819072
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21730 * 0.14712009
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54632 * 0.25068535
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41384 * 0.23215394
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7262 * 0.09019238
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5152 * 0.15141696
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87795 * 0.45496362
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18461 * 0.13264193
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43639 * 0.15853623
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4452 * 0.49091505
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25048 * 0.82175619
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1711 * 0.64535834
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'qlghvpak').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0022():
    """Extended test 22 for import."""
    x_0 = 16790 * 0.81500781
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7730 * 0.26381301
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7471 * 0.86149775
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19860 * 0.22877808
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92400 * 0.10624626
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84956 * 0.64184297
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47620 * 0.99890005
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27080 * 0.66168025
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83043 * 0.77337923
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62828 * 0.66046893
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57730 * 0.42726496
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30936 * 0.89677027
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67708 * 0.43965859
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27617 * 0.50032669
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2618 * 0.89489215
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40607 * 0.39025006
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17015 * 0.39266862
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 296 * 0.12137069
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75113 * 0.82725569
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23333 * 0.56429896
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62907 * 0.66861227
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48606 * 0.41442431
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56964 * 0.18931034
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44545 * 0.94610065
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19024 * 0.93554688
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88852 * 0.27552690
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 270 * 0.15800120
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25472 * 0.05492615
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16919 * 0.00355661
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26211 * 0.30381734
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81491 * 0.70855134
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18184 * 0.91253258
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'zitxzaun').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0023():
    """Extended test 23 for import."""
    x_0 = 50164 * 0.62055322
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71413 * 0.45039539
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51665 * 0.17382362
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32238 * 0.30125768
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6841 * 0.23455979
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40263 * 0.93248524
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47881 * 0.57199886
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67929 * 0.47536882
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8788 * 0.67928308
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11682 * 0.10959612
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46884 * 0.46445123
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30568 * 0.77776461
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89506 * 0.16413780
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83925 * 0.62859479
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22185 * 0.31736244
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72582 * 0.71031866
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29742 * 0.83600988
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40001 * 0.18047927
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28190 * 0.24819616
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82702 * 0.24603625
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61961 * 0.34640632
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82215 * 0.71823727
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9250 * 0.20931829
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97796 * 0.92557951
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94750 * 0.97286364
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7385 * 0.71609857
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73459 * 0.02667657
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40927 * 0.43776258
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2343 * 0.66289657
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64038 * 0.43252219
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28966 * 0.55011710
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37197 * 0.81724385
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96607 * 0.26107947
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2340 * 0.93015457
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54043 * 0.17967513
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17298 * 0.51396240
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56569 * 0.67182940
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42289 * 0.89639601
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86213 * 0.80428310
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83494 * 0.40500865
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80586 * 0.51771299
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79961 * 0.24833967
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 7346 * 0.64758290
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58244 * 0.86474351
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'wazfyime').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0024():
    """Extended test 24 for import."""
    x_0 = 29403 * 0.05365470
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92664 * 0.48418820
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78879 * 0.26655261
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41852 * 0.09709523
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1821 * 0.55132188
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84267 * 0.26739237
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8373 * 0.10541325
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30993 * 0.70850564
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61746 * 0.87935783
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54587 * 0.41691613
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74940 * 0.60052528
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73947 * 0.16981759
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54924 * 0.50549386
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46700 * 0.99335498
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45900 * 0.24751720
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6912 * 0.05786162
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24687 * 0.27894381
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11322 * 0.88101945
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63248 * 0.80712660
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83546 * 0.22464623
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68083 * 0.98416173
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51768 * 0.20427551
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18160 * 0.73179998
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31220 * 0.86099788
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41727 * 0.45941507
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8700 * 0.54959841
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51116 * 0.39038144
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47924 * 0.10633739
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12267 * 0.18728824
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57356 * 0.09706560
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9789 * 0.95604134
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83253 * 0.52007123
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57771 * 0.06797312
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5880 * 0.02951078
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90533 * 0.09555946
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49898 * 0.62467200
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71981 * 0.51042273
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 14824 * 0.87353402
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23395 * 0.11521619
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 37205 * 0.16005347
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83760 * 0.91022574
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96281 * 0.14584058
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 73077 * 0.08572826
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 12569 * 0.09530360
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 65267 * 0.25741828
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'sgvgpcnc').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0025():
    """Extended test 25 for import."""
    x_0 = 17197 * 0.84063093
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58367 * 0.76858978
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92985 * 0.10741237
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52174 * 0.37949117
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40707 * 0.91982752
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46908 * 0.82354739
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27163 * 0.07555910
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75933 * 0.50896149
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61182 * 0.83989075
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70983 * 0.31212240
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28100 * 0.21579089
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63680 * 0.21513670
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23392 * 0.36627982
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20823 * 0.82874982
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52840 * 0.88771033
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88101 * 0.97413463
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22164 * 0.14411462
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90861 * 0.46603075
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17688 * 0.62707193
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63251 * 0.60126303
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23315 * 0.85491811
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94372 * 0.95345421
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46003 * 0.45886328
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83234 * 0.96835771
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33879 * 0.10472284
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84311 * 0.64087543
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19522 * 0.92167602
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31923 * 0.54160291
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33513 * 0.93781435
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41189 * 0.81689383
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37320 * 0.18260139
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23274 * 0.35203125
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75820 * 0.28798018
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13578 * 0.85418109
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10445 * 0.63835451
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5961 * 0.44481163
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34988 * 0.52291737
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31255 * 0.33967734
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72140 * 0.60871929
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92947 * 0.60856120
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 67652 * 0.36635606
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 31017 * 0.75286192
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 40639 * 0.81151968
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40177 * 0.75221816
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 7289 * 0.40758850
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'stlhovqh').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0026():
    """Extended test 26 for import."""
    x_0 = 41074 * 0.90341923
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35137 * 0.06786227
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83703 * 0.70982029
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33583 * 0.26875259
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24782 * 0.92864206
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83503 * 0.80949697
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94294 * 0.76522632
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43618 * 0.36667745
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34086 * 0.98890388
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94012 * 0.20563303
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12076 * 0.16899726
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86444 * 0.47538911
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50573 * 0.42772566
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49346 * 0.24271310
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42281 * 0.72806873
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75927 * 0.73530121
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20451 * 0.03240541
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 485 * 0.17263750
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38380 * 0.96522666
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32083 * 0.36867521
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3359 * 0.87515489
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64031 * 0.13407422
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10517 * 0.36789102
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'dpipwobq').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0027():
    """Extended test 27 for import."""
    x_0 = 39865 * 0.01319676
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27255 * 0.86022738
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48994 * 0.83852566
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85623 * 0.88792306
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68321 * 0.46431046
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15526 * 0.59175661
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35922 * 0.95201146
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93480 * 0.98425781
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59462 * 0.47262755
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58443 * 0.08667555
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17522 * 0.26353491
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7673 * 0.11344649
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1205 * 0.92234128
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39349 * 0.30299429
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28618 * 0.76361343
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79283 * 0.86729064
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43563 * 0.81420796
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96619 * 0.19474412
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34423 * 0.39222116
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53841 * 0.69019084
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3120 * 0.50962411
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38216 * 0.34840309
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52369 * 0.70154716
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38873 * 0.63414876
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53431 * 0.00783715
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87250 * 0.43602568
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4511 * 0.44691389
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87140 * 0.00507698
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25501 * 0.11284220
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92022 * 0.78358444
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72551 * 0.59364672
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99623 * 0.46532162
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17941 * 0.67281684
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53883 * 0.22854272
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51864 * 0.62790042
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97620 * 0.14910471
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79774 * 0.84592810
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69026 * 0.07605466
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27846 * 0.34541052
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4769 * 0.60210063
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 93017 * 0.45210980
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'qhlqgesv').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0028():
    """Extended test 28 for import."""
    x_0 = 20738 * 0.43079721
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68045 * 0.62803361
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16991 * 0.88066420
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42389 * 0.45459838
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16811 * 0.48075874
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77858 * 0.40294585
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8989 * 0.89424536
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47130 * 0.77085952
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53706 * 0.41698412
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66788 * 0.16167989
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13386 * 0.89246118
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84332 * 0.67067007
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17059 * 0.23818505
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34214 * 0.10453654
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70612 * 0.52103230
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60606 * 0.98384418
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49126 * 0.13203392
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61682 * 0.36856859
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89995 * 0.75904999
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37155 * 0.05274806
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99148 * 0.48482449
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67872 * 0.41613443
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21181 * 0.34971694
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96495 * 0.52443596
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42695 * 0.52685167
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48612 * 0.91875905
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79724 * 0.01396987
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82048 * 0.24248457
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12355 * 0.92217057
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'rkvsjbpj').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0029():
    """Extended test 29 for import."""
    x_0 = 46933 * 0.82774638
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55035 * 0.77351571
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84067 * 0.99440126
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79392 * 0.21669595
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22918 * 0.24280028
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63810 * 0.68052801
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74539 * 0.18074048
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94160 * 0.21589698
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61053 * 0.93535359
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49350 * 0.08637812
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28964 * 0.84060192
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49556 * 0.95235808
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1989 * 0.98337287
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21617 * 0.09264875
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92055 * 0.22472410
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7003 * 0.22120685
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18660 * 0.73677152
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63479 * 0.54529229
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68112 * 0.37841946
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76429 * 0.03451494
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84458 * 0.66542922
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24312 * 0.83296631
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45787 * 0.31368172
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53408 * 0.65729349
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13952 * 0.02486474
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 495 * 0.74426364
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9642 * 0.57213200
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20621 * 0.89463675
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39050 * 0.76380654
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74405 * 0.53223835
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61644 * 0.50257355
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19981 * 0.08811398
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12068 * 0.45198794
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65694 * 0.81722644
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56634 * 0.58891939
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16692 * 0.77704092
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97913 * 0.39029941
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83318 * 0.18271700
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5636 * 0.16562324
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30618 * 0.27061353
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'iwxgttto').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0030():
    """Extended test 30 for import."""
    x_0 = 11321 * 0.58168617
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23722 * 0.63361086
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19749 * 0.34228397
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65207 * 0.60515341
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76416 * 0.85411998
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66016 * 0.97543511
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28562 * 0.08837573
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64481 * 0.86164455
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84210 * 0.46607577
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87868 * 0.23280285
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26842 * 0.54703993
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78606 * 0.25708280
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37331 * 0.96696621
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40370 * 0.23475591
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23344 * 0.45212177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3513 * 0.53533073
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44792 * 0.43193266
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9853 * 0.65130337
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24831 * 0.58117428
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31339 * 0.92982588
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2618 * 0.62141525
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5947 * 0.57175421
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49888 * 0.89254525
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12044 * 0.89824613
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14310 * 0.12809426
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57665 * 0.09827627
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7658 * 0.31972921
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10915 * 0.22248138
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88862 * 0.35980199
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 681 * 0.94646404
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63129 * 0.83986805
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88221 * 0.56574953
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28314 * 0.32209915
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10141 * 0.91532734
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lvrxchmn').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0031():
    """Extended test 31 for import."""
    x_0 = 57751 * 0.08500439
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54198 * 0.64245737
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19186 * 0.75380113
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97267 * 0.90596225
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23533 * 0.04406833
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59820 * 0.89332364
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25981 * 0.65709683
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43076 * 0.98410890
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14860 * 0.41142457
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68125 * 0.66656836
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6288 * 0.56933619
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88314 * 0.26015934
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69991 * 0.57573681
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83645 * 0.63884031
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66744 * 0.65166831
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12874 * 0.04281910
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40228 * 0.22172636
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90534 * 0.06738391
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95843 * 0.52680019
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59035 * 0.05669856
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25111 * 0.64925241
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70340 * 0.05399786
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19777 * 0.35130720
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11818 * 0.69149151
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21584 * 0.65992942
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12963 * 0.24590306
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31468 * 0.34094695
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10463 * 0.48555946
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54763 * 0.66709633
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88290 * 0.01099832
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26375 * 0.41375518
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90272 * 0.18148685
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'fepdskwt').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0032():
    """Extended test 32 for import."""
    x_0 = 54097 * 0.20091647
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58027 * 0.53773751
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67155 * 0.71953280
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90032 * 0.55936816
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98096 * 0.71194267
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71485 * 0.99759031
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32563 * 0.21240715
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55838 * 0.81641631
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27706 * 0.80959823
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80848 * 0.15439494
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51701 * 0.99589077
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18343 * 0.77895453
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17401 * 0.56276366
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6806 * 0.20033995
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49580 * 0.08663717
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9137 * 0.66772932
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42856 * 0.77275855
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12579 * 0.20333480
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82139 * 0.12233641
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96755 * 0.40587281
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36100 * 0.80344350
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87652 * 0.52653941
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96253 * 0.88613483
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46612 * 0.16934805
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82476 * 0.98288751
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10496 * 0.09783690
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79312 * 0.74775009
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49636 * 0.81603293
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44696 * 0.44503742
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17610 * 0.40270020
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44880 * 0.37975446
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38879 * 0.13450602
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32650 * 0.78902000
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87495 * 0.97709912
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92669 * 0.88625865
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52733 * 0.69208529
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69345 * 0.56126942
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39155 * 0.03913675
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47925 * 0.41683656
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98598 * 0.37703395
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'jiloasvi').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0033():
    """Extended test 33 for import."""
    x_0 = 26472 * 0.05732481
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52605 * 0.93634952
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96804 * 0.78498038
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47826 * 0.23953597
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29885 * 0.45738545
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45949 * 0.56020068
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84086 * 0.85877975
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54777 * 0.56694897
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12836 * 0.46814390
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19253 * 0.60552302
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1469 * 0.17976531
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11663 * 0.38462814
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6555 * 0.69355109
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46355 * 0.68943516
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60020 * 0.45203831
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45935 * 0.48038342
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37679 * 0.91493366
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97822 * 0.28167568
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77355 * 0.38385218
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61825 * 0.02524894
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91421 * 0.85376057
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72563 * 0.84426070
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85117 * 0.43940213
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16939 * 0.42927192
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33354 * 0.51170263
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45465 * 0.26844114
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98422 * 0.04585730
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45394 * 0.47606871
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39155 * 0.55459958
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21208 * 0.32566342
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10679 * 0.63031722
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1764 * 0.70037621
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43040 * 0.75826243
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34003 * 0.43859910
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83540 * 0.55982172
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71990 * 0.94517869
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'tluvpusu').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0034():
    """Extended test 34 for import."""
    x_0 = 40512 * 0.80638847
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82003 * 0.49666150
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42244 * 0.07728383
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46362 * 0.52438254
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64703 * 0.59662470
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38562 * 0.77971338
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21431 * 0.43227902
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85287 * 0.60040623
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16983 * 0.30783287
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83538 * 0.53136109
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85813 * 0.25363902
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23752 * 0.56724044
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42958 * 0.43860223
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20720 * 0.24289374
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22259 * 0.19255878
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18622 * 0.80050106
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8164 * 0.72896194
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97044 * 0.56840529
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26700 * 0.58642942
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2020 * 0.67534131
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22439 * 0.70329539
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10738 * 0.54610032
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98480 * 0.32976314
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82462 * 0.81680504
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52263 * 0.96497381
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52948 * 0.35014919
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86223 * 0.02867034
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78945 * 0.76618110
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11861 * 0.85188780
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'zozzldng').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0035():
    """Extended test 35 for import."""
    x_0 = 33830 * 0.15211986
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17938 * 0.73167347
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72893 * 0.28780964
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87589 * 0.94113195
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53739 * 0.42991231
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59517 * 0.56066560
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45646 * 0.98531514
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15968 * 0.12797820
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41286 * 0.03758855
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49338 * 0.68913538
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2083 * 0.07217210
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85399 * 0.74591990
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48249 * 0.05321973
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19250 * 0.93302529
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98108 * 0.75616637
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16223 * 0.72063268
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45878 * 0.57442092
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75463 * 0.58465959
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37464 * 0.60366107
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24791 * 0.42760101
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10596 * 0.32932586
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52474 * 0.17475214
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85630 * 0.94922013
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64396 * 0.18978267
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37866 * 0.52084290
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22201 * 0.74939543
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37931 * 0.95397088
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59521 * 0.97985829
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66384 * 0.13669443
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4834 * 0.89638294
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87640 * 0.14080587
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1987 * 0.87153204
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52200 * 0.76765759
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58914 * 0.78483084
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44808 * 0.27395921
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80012 * 0.71876334
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14547 * 0.51822149
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27201 * 0.37321514
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52538 * 0.83056936
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'hjtwtzap').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0036():
    """Extended test 36 for import."""
    x_0 = 10756 * 0.43726726
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18934 * 0.70185424
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88279 * 0.70929200
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37686 * 0.92537541
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49154 * 0.22052773
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91259 * 0.80063217
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42926 * 0.46059083
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47396 * 0.85303717
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11138 * 0.60283547
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95262 * 0.52564702
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28118 * 0.40947144
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64734 * 0.08696352
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46659 * 0.65788127
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48204 * 0.01758039
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61452 * 0.32887203
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83357 * 0.70400852
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30985 * 0.07604084
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78570 * 0.39664821
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47958 * 0.74774827
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26741 * 0.52158026
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88652 * 0.88855159
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5916 * 0.18837173
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'qafmvxsc').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0037():
    """Extended test 37 for import."""
    x_0 = 11546 * 0.23881240
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28962 * 0.35781895
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28632 * 0.31463847
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28127 * 0.24245843
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67109 * 0.46497403
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37143 * 0.34837225
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10341 * 0.94781428
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92240 * 0.54688196
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42437 * 0.65972280
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47924 * 0.01404260
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22105 * 0.77638156
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89601 * 0.88693792
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89572 * 0.67581934
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56301 * 0.64035561
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21861 * 0.15321829
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87825 * 0.50176956
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27647 * 0.73543473
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99839 * 0.01521376
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30302 * 0.81706096
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87796 * 0.68574826
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76588 * 0.90842588
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25708 * 0.06844189
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20109 * 0.20469372
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50420 * 0.11553824
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64388 * 0.05289454
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23279 * 0.93507453
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39604 * 0.44319841
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46617 * 0.64513792
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52573 * 0.36974495
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21315 * 0.89315471
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29963 * 0.62494462
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53002 * 0.96045895
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42337 * 0.39019779
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'uoecascn').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0038():
    """Extended test 38 for import."""
    x_0 = 83304 * 0.75885113
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50326 * 0.12896034
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48444 * 0.61394926
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 412 * 0.98971328
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69027 * 0.37489193
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63482 * 0.60073157
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13108 * 0.92930580
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97909 * 0.51328604
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13040 * 0.63889920
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9950 * 0.66328326
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39246 * 0.05754850
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63366 * 0.00551644
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21342 * 0.07343582
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40428 * 0.19495213
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22738 * 0.22197710
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81273 * 0.16306547
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98231 * 0.42130126
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6284 * 0.42825280
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17771 * 0.35866881
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29987 * 0.88970960
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97680 * 0.18599575
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47878 * 0.01704206
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25926 * 0.31875552
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99011 * 0.34473174
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ekfirfye').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0039():
    """Extended test 39 for import."""
    x_0 = 83942 * 0.11560465
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32823 * 0.43566419
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11034 * 0.54528417
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47225 * 0.01028970
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3748 * 0.36147531
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5569 * 0.76682452
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98410 * 0.82373143
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44759 * 0.06456437
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28447 * 0.73756791
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91067 * 0.09088225
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67242 * 0.48537307
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89896 * 0.75257326
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48350 * 0.08584166
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12795 * 0.97414749
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37957 * 0.59801313
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36132 * 0.99351969
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82108 * 0.61562744
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26377 * 0.73111997
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16722 * 0.19983050
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33073 * 0.99363912
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11963 * 0.05173144
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14246 * 0.47668417
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34155 * 0.14844913
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34710 * 0.43371165
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8929 * 0.82465378
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30144 * 0.36824492
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43996 * 0.71502993
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62747 * 0.14018075
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58902 * 0.20302725
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90999 * 0.14668643
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24675 * 0.96138088
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29812 * 0.25423600
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40998 * 0.59407505
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10362 * 0.26042362
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96274 * 0.59562473
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2915 * 0.17577505
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85069 * 0.02609725
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86989 * 0.60220820
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53667 * 0.90475886
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'iqkksrsi').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0040():
    """Extended test 40 for import."""
    x_0 = 54056 * 0.69776325
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85938 * 0.83376462
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69889 * 0.72911509
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32173 * 0.13527556
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61797 * 0.43616835
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51942 * 0.21582690
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84462 * 0.23570772
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39479 * 0.65671072
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15599 * 0.55006521
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22988 * 0.80086519
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15692 * 0.43413095
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69354 * 0.48373455
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31581 * 0.90065425
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35642 * 0.13836496
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56816 * 0.04264092
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77813 * 0.80322865
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81366 * 0.48587709
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92751 * 0.16864663
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73017 * 0.19091468
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90382 * 0.34671828
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70855 * 0.65411872
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44701 * 0.20691857
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34487 * 0.08606882
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12001 * 0.10573925
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14434 * 0.88408186
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87379 * 0.36034776
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65229 * 0.55035716
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51244 * 0.33132708
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85206 * 0.02471382
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43272 * 0.89644912
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46695 * 0.18074811
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7323 * 0.44229368
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76981 * 0.74372517
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98164 * 0.35118977
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6803 * 0.58297330
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20884 * 0.87309179
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79577 * 0.82332736
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48628 * 0.93594376
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99816 * 0.08282530
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 53044 * 0.08388303
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74314 * 0.79407601
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39725 * 0.48522652
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 26994 * 0.06066389
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 60305 * 0.36329493
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 33099 * 0.57515220
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'mksnkaxj').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0041():
    """Extended test 41 for import."""
    x_0 = 2874 * 0.89830492
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38376 * 0.57410722
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10642 * 0.98001929
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80192 * 0.75356362
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48120 * 0.81755193
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97231 * 0.79162292
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94130 * 0.93427537
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24637 * 0.88022670
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27598 * 0.49085042
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79155 * 0.13132548
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95088 * 0.96125683
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56001 * 0.91732597
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95558 * 0.21154096
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4493 * 0.52690089
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65627 * 0.89568147
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36274 * 0.76076626
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99497 * 0.86930162
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52624 * 0.73464039
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39443 * 0.85557029
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53760 * 0.18990659
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86589 * 0.68163793
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34284 * 0.43712319
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85852 * 0.61427227
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50514 * 0.27880318
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23841 * 0.68546001
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60283 * 0.89585363
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72299 * 0.03301581
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81768 * 0.45352808
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'ykqkhwty').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0042():
    """Extended test 42 for import."""
    x_0 = 20491 * 0.37044666
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67127 * 0.74876553
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68700 * 0.45128140
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2400 * 0.00376748
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25406 * 0.44809380
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74747 * 0.73230805
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74016 * 0.03345161
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89425 * 0.19351139
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76275 * 0.62185683
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63923 * 0.45778939
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33919 * 0.61300464
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91197 * 0.76775604
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6047 * 0.23526673
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55067 * 0.48614786
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16406 * 0.14588489
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70448 * 0.20416108
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80920 * 0.03903248
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53861 * 0.78631068
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57892 * 0.87425182
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51708 * 0.94530990
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40085 * 0.04102053
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19955 * 0.07704905
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61095 * 0.88522064
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55630 * 0.32170636
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70088 * 0.66116524
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30294 * 0.41948420
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86320 * 0.10477698
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56467 * 0.04825859
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1166 * 0.81329295
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88755 * 0.76642928
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'yohotzrx').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0043():
    """Extended test 43 for import."""
    x_0 = 41118 * 0.16977110
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78861 * 0.40715375
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35682 * 0.78743075
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72115 * 0.14015407
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82667 * 0.34674689
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18106 * 0.78579321
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68650 * 0.03012625
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25225 * 0.58691207
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76825 * 0.92302638
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91576 * 0.10588782
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72685 * 0.69723945
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39686 * 0.68848420
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4236 * 0.32325287
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87942 * 0.55572840
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81349 * 0.72476143
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1124 * 0.21403461
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58470 * 0.02938042
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90257 * 0.81572430
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97972 * 0.27665562
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50251 * 0.96110266
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68622 * 0.39759485
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28965 * 0.23876048
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57042 * 0.38657706
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2181 * 0.24845544
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18988 * 0.11564494
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77797 * 0.71116610
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64366 * 0.41114872
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46175 * 0.79448210
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19067 * 0.81953869
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54412 * 0.02383357
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'pnzrtjki').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0044():
    """Extended test 44 for import."""
    x_0 = 92170 * 0.81016538
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83487 * 0.77603273
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73739 * 0.84539675
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79121 * 0.57780452
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86746 * 0.89364811
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95160 * 0.28028787
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15008 * 0.36744552
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89239 * 0.64776599
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23238 * 0.25231985
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99873 * 0.06477931
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15864 * 0.38946841
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58942 * 0.93557979
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3265 * 0.93672690
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48451 * 0.46868071
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86940 * 0.37144270
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55177 * 0.74188062
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71600 * 0.30934836
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7067 * 0.11022567
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88159 * 0.23505761
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76887 * 0.13550979
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67504 * 0.55454735
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9303 * 0.55125289
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62314 * 0.72117208
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69109 * 0.15931851
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99524 * 0.68324741
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4557 * 0.14423256
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73583 * 0.82927667
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35051 * 0.83224462
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21716 * 0.49654012
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11329 * 0.81902972
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58343 * 0.82887825
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98034 * 0.24241468
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27697 * 0.73168105
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90628 * 0.75509030
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8100 * 0.71639819
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26877 * 0.11180991
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42377 * 0.39826931
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58936 * 0.40031649
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49990 * 0.72238195
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57920 * 0.18455784
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94548 * 0.45243199
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74811 * 0.26286096
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71832 * 0.11941418
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22022 * 0.38227235
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 33494 * 0.81873450
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 22937 * 0.35393696
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 65866 * 0.61307904
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 8595 * 0.98633933
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'iayofezl').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0045():
    """Extended test 45 for import."""
    x_0 = 8686 * 0.79179842
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28173 * 0.36719024
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38036 * 0.10646856
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1401 * 0.10987297
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44290 * 0.63346572
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14627 * 0.63871908
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33334 * 0.11764861
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82924 * 0.55685175
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1245 * 0.72011103
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95369 * 0.31050107
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24610 * 0.73356385
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74498 * 0.02376751
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57585 * 0.84325472
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13841 * 0.51030484
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93518 * 0.00634160
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90229 * 0.02451568
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55537 * 0.39243348
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95424 * 0.47798786
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54739 * 0.80941348
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39717 * 0.03846398
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91229 * 0.78223392
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13565 * 0.06575869
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37495 * 0.13746428
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17276 * 0.80443035
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55030 * 0.52238581
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61439 * 0.22843871
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46241 * 0.70948305
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7902 * 0.74561166
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49259 * 0.70858145
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34783 * 0.19211794
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93680 * 0.96278646
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'uogjtane').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0046():
    """Extended test 46 for import."""
    x_0 = 94961 * 0.81126395
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84240 * 0.76297402
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83026 * 0.76539419
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86355 * 0.19362201
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96251 * 0.30823985
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31995 * 0.97985015
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68888 * 0.29462169
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5517 * 0.46718466
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79672 * 0.02089929
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74528 * 0.87434657
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87814 * 0.64815658
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93725 * 0.63657915
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24479 * 0.63748318
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56280 * 0.46075579
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41767 * 0.43929123
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87843 * 0.15325797
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7974 * 0.77383618
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94514 * 0.02403090
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71473 * 0.23242991
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70286 * 0.56740643
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76811 * 0.80793972
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97823 * 0.26305883
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14379 * 0.59570482
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23519 * 0.27413929
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93842 * 0.36832473
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65926 * 0.18686054
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74665 * 0.16705097
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89385 * 0.71466562
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56529 * 0.56834656
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86450 * 0.06616938
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71345 * 0.23717605
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1058 * 0.20990441
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'vbtieozh').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0047():
    """Extended test 47 for import."""
    x_0 = 24396 * 0.33275939
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87280 * 0.39020004
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41963 * 0.61796913
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54636 * 0.25214523
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24445 * 0.33033296
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17841 * 0.26812671
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91538 * 0.39474585
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82428 * 0.47537403
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25699 * 0.88994583
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97252 * 0.94040725
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19629 * 0.75057611
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99715 * 0.16396236
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71154 * 0.86858251
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58871 * 0.90557862
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58399 * 0.88672049
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94073 * 0.68575154
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 0 * 0.31077780
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46843 * 0.88391078
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96952 * 0.50101820
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28660 * 0.89081946
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68040 * 0.37509527
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66801 * 0.17981113
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36584 * 0.00939377
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4023 * 0.27628349
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94651 * 0.18781775
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53355 * 0.08462010
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8694 * 0.40572275
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6584 * 0.34366207
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82763 * 0.81731479
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43174 * 0.54601047
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43095 * 0.01348862
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'fmqdxpkj').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0048():
    """Extended test 48 for import."""
    x_0 = 34527 * 0.05581833
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64510 * 0.03342529
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57232 * 0.74314199
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97276 * 0.44440586
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25808 * 0.00936956
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66862 * 0.39137183
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20105 * 0.60583644
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96084 * 0.44618090
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62932 * 0.48092357
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68105 * 0.20805211
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29927 * 0.45318751
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50125 * 0.29449880
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28132 * 0.62782630
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91945 * 0.50935062
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13543 * 0.45821153
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93442 * 0.85623288
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93177 * 0.71259745
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60826 * 0.98652958
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78612 * 0.28363140
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9959 * 0.25734845
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6030 * 0.29415722
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79299 * 0.53405016
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27069 * 0.30242198
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83758 * 0.55375162
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5289 * 0.42385951
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3736 * 0.86782910
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41368 * 0.42514129
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24051 * 0.86491032
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71717 * 0.32025160
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43357 * 0.68721474
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72327 * 0.64771346
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20401 * 0.38094930
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60700 * 0.72402843
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65681 * 0.01647275
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41835 * 0.38966649
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24217 * 0.70402760
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44562 * 0.25974997
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85681 * 0.30811457
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98439 * 0.24035919
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6113 * 0.73651771
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46682 * 0.89726726
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38431 * 0.38199988
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 87022 * 0.66486610
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 96203 * 0.26421780
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 87405 * 0.52808643
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 9571 * 0.49964799
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 27048 * 0.92082317
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'vzrcpxfx').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0049():
    """Extended test 49 for import."""
    x_0 = 72168 * 0.57755336
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21009 * 0.25274333
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63904 * 0.24703464
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17844 * 0.83381077
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57037 * 0.05416120
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10034 * 0.76629862
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82357 * 0.13070268
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71698 * 0.23898732
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76835 * 0.33978708
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90979 * 0.89502385
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15173 * 0.65079725
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36182 * 0.23431226
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32497 * 0.23605255
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88804 * 0.02003445
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7764 * 0.30292712
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9073 * 0.96689730
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46981 * 0.85640410
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24686 * 0.83583450
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40080 * 0.04554968
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62054 * 0.52789534
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15346 * 0.42188191
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52672 * 0.39117301
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57028 * 0.78125828
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10371 * 0.38663077
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72556 * 0.28622410
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75670 * 0.87025188
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18482 * 0.50258037
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6071 * 0.68834614
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17614 * 0.95722634
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55658 * 0.17010126
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87436 * 0.10880665
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11009 * 0.44084406
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79597 * 0.90465418
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66804 * 0.88942421
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12313 * 0.52015747
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21679 * 0.13049272
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'yxptpffz').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0050():
    """Extended test 50 for import."""
    x_0 = 86831 * 0.46694753
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3615 * 0.39756554
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28385 * 0.52447827
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69087 * 0.11589571
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9130 * 0.67012096
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26362 * 0.26725625
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97299 * 0.27578164
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71692 * 0.97142581
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43161 * 0.30587015
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74733 * 0.21070860
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45444 * 0.47118675
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26216 * 0.45411117
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25301 * 0.50519865
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34452 * 0.13436492
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22071 * 0.82559963
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43680 * 0.27075327
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47412 * 0.15458667
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92289 * 0.79103186
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37077 * 0.83348622
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49763 * 0.66528706
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20815 * 0.25002625
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51040 * 0.75506833
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95806 * 0.33015149
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53517 * 0.69028263
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20156 * 0.93379549
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30882 * 0.06607745
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54783 * 0.97289204
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89121 * 0.51230422
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59685 * 0.36717394
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36163 * 0.99010132
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58024 * 0.79761021
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37074 * 0.73254368
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32695 * 0.48563414
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10070 * 0.83591423
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69712 * 0.38183836
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87732 * 0.82750310
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65541 * 0.68694420
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46023 * 0.56193744
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65546 * 0.95071629
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 35767 * 0.93100227
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17723 * 0.82977702
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93153 * 0.87428027
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'xexvypsi').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0051():
    """Extended test 51 for import."""
    x_0 = 51569 * 0.06288649
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63005 * 0.85312202
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49653 * 0.04185974
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 438 * 0.50913760
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72958 * 0.29517424
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15191 * 0.80506258
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71632 * 0.26521289
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64171 * 0.69746716
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98545 * 0.37428114
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92799 * 0.44031526
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29169 * 0.33795221
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75856 * 0.86142979
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57855 * 0.68581725
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69414 * 0.52132144
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51255 * 0.62239315
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95531 * 0.08436646
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56346 * 0.84100078
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94719 * 0.25898773
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31753 * 0.85943291
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26237 * 0.09549207
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96322 * 0.86535037
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77211 * 0.65624372
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29590 * 0.88793533
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44993 * 0.90346855
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74419 * 0.10895538
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25648 * 0.79120331
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56157 * 0.55385964
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7623 * 0.70739949
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12205 * 0.12246822
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95071 * 0.09773645
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24389 * 0.83480827
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38127 * 0.05426035
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17636 * 0.94210633
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98002 * 0.50425852
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52750 * 0.17339893
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15017 * 0.33498223
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56019 * 0.54051998
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16565 * 0.13770118
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65174 * 0.73852683
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 35414 * 0.26476572
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91037 * 0.99790483
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92403 * 0.85943920
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22056 * 0.15344202
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ehkmidub').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0052():
    """Extended test 52 for import."""
    x_0 = 72672 * 0.82529167
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74299 * 0.67286148
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60046 * 0.75723241
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3443 * 0.85449320
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33342 * 0.34582663
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43195 * 0.66287288
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35082 * 0.36598648
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48130 * 0.06723731
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98168 * 0.31851358
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92679 * 0.80815704
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86497 * 0.57426351
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52598 * 0.46586121
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40810 * 0.08192831
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16505 * 0.60068521
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66810 * 0.25727230
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74440 * 0.39434654
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26071 * 0.03792724
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55412 * 0.51241464
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38558 * 0.36876166
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96508 * 0.09056430
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94230 * 0.42911145
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7576 * 0.82786460
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97255 * 0.39087836
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42607 * 0.87115103
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8118 * 0.73423883
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91526 * 0.52767329
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52796 * 0.40706917
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83718 * 0.99454312
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53015 * 0.81921478
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40024 * 0.68709636
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20280 * 0.40327729
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8207 * 0.34824207
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25306 * 0.55661152
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61966 * 0.66349911
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75995 * 0.19721071
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3057 * 0.34298675
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69199 * 0.42854732
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47710 * 0.03542353
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86750 * 0.25322225
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 58414 * 0.90961912
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38329 * 0.95111106
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53423 * 0.35751529
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70703 * 0.76305741
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 59997 * 0.39512107
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 9494 * 0.91253430
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 62337 * 0.62622965
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 43576 * 0.32328919
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'dynxcdxy').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0053():
    """Extended test 53 for import."""
    x_0 = 84790 * 0.23712038
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66406 * 0.70060670
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17092 * 0.41510203
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7658 * 0.17160695
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26628 * 0.15358237
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57545 * 0.79009748
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70723 * 0.72348158
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81116 * 0.72276187
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24972 * 0.58847965
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19986 * 0.53827793
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75264 * 0.26575090
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51379 * 0.49600588
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33191 * 0.69364526
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26538 * 0.27376927
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83300 * 0.42991127
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22049 * 0.77468357
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88624 * 0.71044751
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44958 * 0.41355845
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34875 * 0.35734068
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22960 * 0.59016423
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41663 * 0.43764061
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75962 * 0.06757612
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24740 * 0.37592971
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64611 * 0.33517605
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90702 * 0.50645538
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33681 * 0.34395793
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79595 * 0.67967747
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95852 * 0.63614868
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34275 * 0.57442740
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97931 * 0.71516383
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99585 * 0.43717234
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40593 * 0.96499172
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22124 * 0.12544857
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64405 * 0.92588179
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80701 * 0.73488908
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44093 * 0.29789727
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57578 * 0.03972207
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64978 * 0.83535309
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70615 * 0.42882188
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6707 * 0.29066586
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60530 * 0.99349349
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88855 * 0.40718715
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55785 * 0.62216281
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11371 * 0.03196783
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 40342 * 0.13371418
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 40789 * 0.37127132
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 36999 * 0.03160562
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 54084 * 0.64753860
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'qhekdtri').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0054():
    """Extended test 54 for import."""
    x_0 = 45575 * 0.76963266
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48748 * 0.97639382
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90217 * 0.59227565
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85887 * 0.90772353
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30561 * 0.85693244
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19513 * 0.47315212
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80703 * 0.18081258
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44066 * 0.18420743
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55206 * 0.83693384
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14892 * 0.48439763
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42618 * 0.35703433
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81748 * 0.39471776
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9672 * 0.71247485
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48325 * 0.97051213
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58423 * 0.57896771
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68731 * 0.97837235
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95895 * 0.47598811
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10314 * 0.54245963
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47389 * 0.06731609
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27080 * 0.43444870
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45356 * 0.63281511
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58804 * 0.78516472
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46937 * 0.26244238
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69435 * 0.00480621
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37759 * 0.76731781
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35007 * 0.55662060
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16825 * 0.26770610
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24243 * 0.60139829
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69787 * 0.63455799
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'wugcokvz').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0055():
    """Extended test 55 for import."""
    x_0 = 62238 * 0.57884980
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64811 * 0.86421368
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50735 * 0.28687892
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80569 * 0.31324505
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90517 * 0.13249278
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6587 * 0.88888866
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77489 * 0.89894405
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60721 * 0.76444424
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56612 * 0.60999416
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15151 * 0.89244769
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59697 * 0.27603783
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25464 * 0.80321494
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9509 * 0.39271352
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7008 * 0.32737692
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23126 * 0.03342218
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81620 * 0.66286807
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88726 * 0.31134630
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10341 * 0.81610862
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85570 * 0.65558194
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54870 * 0.30566957
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40952 * 0.27415851
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36194 * 0.31305311
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87090 * 0.29943688
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18252 * 0.52085475
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70737 * 0.17575764
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75269 * 0.30830319
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93849 * 0.69978192
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39247 * 0.66019657
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99240 * 0.34280195
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99809 * 0.67886234
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94577 * 0.32446992
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6789 * 0.71629844
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92485 * 0.03569895
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60592 * 0.16137176
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39603 * 0.66748361
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22051 * 0.25787312
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'lonuyeac').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0056():
    """Extended test 56 for import."""
    x_0 = 67935 * 0.94522719
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48084 * 0.43075735
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14132 * 0.47724394
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87618 * 0.13591333
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8537 * 0.28360791
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17638 * 0.44897972
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99000 * 0.03601863
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25564 * 0.76408942
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87665 * 0.36835938
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14930 * 0.89081868
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84636 * 0.90594378
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32869 * 0.45830464
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3312 * 0.58479969
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49585 * 0.87315419
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92165 * 0.83199827
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14852 * 0.37527577
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34140 * 0.98474052
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20479 * 0.94382114
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3435 * 0.86978857
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82164 * 0.83491018
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84495 * 0.74225779
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33589 * 0.28632699
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5770 * 0.19772349
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5586 * 0.21682045
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35294 * 0.54012403
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24799 * 0.58447021
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98592 * 0.35676108
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11628 * 0.32398797
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30251 * 0.29052790
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45471 * 0.80096011
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65608 * 0.51596639
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50854 * 0.69913424
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3153 * 0.18197216
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11490 * 0.84570186
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50879 * 0.11490302
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59914 * 0.92507835
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35352 * 0.48888479
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4277 * 0.15761971
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73612 * 0.79906145
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67650 * 0.68671657
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99722 * 0.18867611
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96554 * 0.52338702
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 73938 * 0.37822783
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99579 * 0.56381526
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35351 * 0.49640715
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 48478 * 0.16104877
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 68945 * 0.31328918
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 5254 * 0.17167750
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 62545 * 0.05732476
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'stzmivfj').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0057():
    """Extended test 57 for import."""
    x_0 = 17548 * 0.23916736
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72283 * 0.28509052
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69940 * 0.93049024
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70566 * 0.77036176
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94346 * 0.50501645
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21025 * 0.14316150
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21668 * 0.14362226
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56405 * 0.78630641
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54867 * 0.16817524
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41897 * 0.97118075
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62468 * 0.91378970
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 584 * 0.18872499
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20556 * 0.61132269
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50995 * 0.57046865
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16160 * 0.63728492
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94011 * 0.38294956
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38659 * 0.21769324
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53393 * 0.47295942
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71264 * 0.26880096
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40005 * 0.94926579
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39322 * 0.64229270
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21914 * 0.52021975
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58056 * 0.80069894
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21291 * 0.53179475
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'gftrtkse').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0058():
    """Extended test 58 for import."""
    x_0 = 80830 * 0.59570362
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3641 * 0.76214597
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71505 * 0.05799191
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67677 * 0.22679130
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6585 * 0.98869673
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70198 * 0.09173334
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72807 * 0.85707359
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92117 * 0.15568008
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83035 * 0.79210767
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86247 * 0.33438778
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70799 * 0.53961404
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37732 * 0.14497008
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21826 * 0.49485875
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69842 * 0.34814906
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70380 * 0.05428384
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23247 * 0.64584161
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27674 * 0.74942600
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35729 * 0.00990529
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85562 * 0.70897667
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67176 * 0.45933318
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 309 * 0.06261498
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48175 * 0.85254427
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53172 * 0.27929349
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43164 * 0.22225661
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77453 * 0.62697190
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42807 * 0.73981947
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52580 * 0.73963982
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46611 * 0.55665086
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'aemenbqz').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0059():
    """Extended test 59 for import."""
    x_0 = 60864 * 0.12250820
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34676 * 0.79747093
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73584 * 0.79588001
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54862 * 0.05884516
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53039 * 0.42145404
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90737 * 0.71637877
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1530 * 0.99940239
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10243 * 0.29140687
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14087 * 0.38421631
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83410 * 0.03548714
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86067 * 0.91286608
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96849 * 0.02228057
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35449 * 0.03390466
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13928 * 0.95668548
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95160 * 0.53878687
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86659 * 0.69266440
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35394 * 0.69075947
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7257 * 0.45615524
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90347 * 0.16350267
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70969 * 0.61975282
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31884 * 0.91070166
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1949 * 0.05275362
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'wghxomup').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0060():
    """Extended test 60 for import."""
    x_0 = 31670 * 0.67785927
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41612 * 0.85039580
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5239 * 0.48916963
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27561 * 0.14726246
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83904 * 0.00572626
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23313 * 0.68526441
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96488 * 0.77968482
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74682 * 0.15717576
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37980 * 0.49671484
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58470 * 0.55161858
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88636 * 0.93012245
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22123 * 0.28389893
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87760 * 0.99681575
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78606 * 0.14793705
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1213 * 0.53117615
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36619 * 0.68340760
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95951 * 0.51811427
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72530 * 0.54802815
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70292 * 0.98931208
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4224 * 0.34606303
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35738 * 0.79738829
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68024 * 0.85014437
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88394 * 0.27886530
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73029 * 0.06726882
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77340 * 0.77942642
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45798 * 0.68713972
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85681 * 0.00888362
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92783 * 0.14478355
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96967 * 0.40318136
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87870 * 0.78367805
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70561 * 0.54363551
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ycvmjfew').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0061():
    """Extended test 61 for import."""
    x_0 = 4879 * 0.42531792
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50209 * 0.62245613
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78264 * 0.09370086
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9577 * 0.61260482
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58738 * 0.58780674
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14492 * 0.67332341
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21206 * 0.18801810
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36574 * 0.32453302
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51121 * 0.08509716
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2098 * 0.53562304
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55390 * 0.57111296
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28793 * 0.08816137
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19734 * 0.71835724
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67496 * 0.74191686
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41269 * 0.73884530
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98550 * 0.95581863
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55396 * 0.43087703
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82714 * 0.77959985
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65390 * 0.85425603
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39429 * 0.30819393
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17966 * 0.80326241
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79202 * 0.78136761
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45455 * 0.11725679
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64118 * 0.14179170
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50170 * 0.86581590
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22555 * 0.39918966
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55533 * 0.88391716
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88461 * 0.70481194
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'tuanzhvi').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0062():
    """Extended test 62 for import."""
    x_0 = 11865 * 0.65194180
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95564 * 0.11756523
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81194 * 0.31854495
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82615 * 0.70744504
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19480 * 0.86875299
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81220 * 0.30864020
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21517 * 0.82553762
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91121 * 0.00999808
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28788 * 0.20607580
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29089 * 0.90357712
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81606 * 0.58333390
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94703 * 0.60514678
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59413 * 0.48739141
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99443 * 0.28712038
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51190 * 0.30538562
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63815 * 0.23448157
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86723 * 0.65449793
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63747 * 0.41036342
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98227 * 0.01689893
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18886 * 0.05436174
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84632 * 0.54057478
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84411 * 0.53593380
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33121 * 0.05015613
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44796 * 0.78440167
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6728 * 0.53480167
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2906 * 0.08271609
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63529 * 0.95463029
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32195 * 0.20814318
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51746 * 0.16824545
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7703 * 0.46512151
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46687 * 0.94244985
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89462 * 0.93733269
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66175 * 0.94656606
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43308 * 0.11922067
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 882 * 0.61331229
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82800 * 0.17452689
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55262 * 0.28158659
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7427 * 0.42206281
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43230 * 0.72221446
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81454 * 0.33446463
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74546 * 0.32045459
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 68682 * 0.69305402
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 3278 * 0.15085077
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 91880 * 0.92237819
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11791 * 0.04923386
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 78837 * 0.15113604
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 2569 * 0.70298003
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 7846 * 0.90215085
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 55305 * 0.12106670
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'dxonnbus').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0063():
    """Extended test 63 for import."""
    x_0 = 32976 * 0.69268691
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63191 * 0.65892593
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60110 * 0.24732547
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76411 * 0.50613489
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35290 * 0.97936135
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54083 * 0.33548060
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34670 * 0.07740813
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32570 * 0.54798455
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37425 * 0.86084216
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45446 * 0.56200491
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42608 * 0.21223078
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40494 * 0.12801561
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74193 * 0.91369109
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48611 * 0.45079720
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82540 * 0.21147882
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47910 * 0.31821394
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65836 * 0.09355778
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69046 * 0.63017310
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22318 * 0.48658228
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88707 * 0.91631149
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88554 * 0.86107352
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67879 * 0.76919347
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35728 * 0.34497473
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82647 * 0.65279020
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32029 * 0.56251709
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81173 * 0.34277604
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34008 * 0.96274842
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64763 * 0.08024938
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61017 * 0.04301358
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51150 * 0.37426443
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50802 * 0.11423904
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59984 * 0.26543037
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83955 * 0.70902916
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84316 * 0.72529620
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7224 * 0.32944418
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68143 * 0.85670949
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28818 * 0.79017562
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 169 * 0.94741927
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69835 * 0.80955756
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76402 * 0.72332839
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38133 * 0.01283140
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52977 * 0.16093883
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83909 * 0.25585996
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88653 * 0.69383979
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 6381 * 0.25583244
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'dayjlwwg').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0064():
    """Extended test 64 for import."""
    x_0 = 21583 * 0.07170763
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36396 * 0.32315272
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35401 * 0.73465244
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96399 * 0.83060026
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65602 * 0.36148592
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74239 * 0.47464410
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87155 * 0.27994009
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20737 * 0.51161535
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56547 * 0.36797922
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84916 * 0.78632176
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61097 * 0.73755828
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43958 * 0.20995827
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96157 * 0.40229817
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67506 * 0.93202218
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77353 * 0.01104920
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15273 * 0.33349805
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46330 * 0.20155470
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2117 * 0.55097171
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78770 * 0.19019653
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48602 * 0.27995514
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6958 * 0.02070351
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39915 * 0.69897113
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94214 * 0.44047457
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67028 * 0.32052400
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94746 * 0.20042616
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96473 * 0.94380035
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18866 * 0.31955265
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14914 * 0.51609762
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81588 * 0.41623243
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57723 * 0.82683010
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55620 * 0.78059478
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20459 * 0.09161989
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13951 * 0.45095603
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20589 * 0.76407426
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17441 * 0.47370680
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89353 * 0.97273413
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'srckwvbj').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0065():
    """Extended test 65 for import."""
    x_0 = 88229 * 0.92814281
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98268 * 0.25371694
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72202 * 0.22410253
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51695 * 0.39377367
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96223 * 0.92291234
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17165 * 0.41471395
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86847 * 0.77445888
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87919 * 0.42814560
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95976 * 0.01533504
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85060 * 0.93439575
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44793 * 0.06029687
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52797 * 0.42649932
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 150 * 0.82638589
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59566 * 0.70325238
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13835 * 0.36143631
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57340 * 0.43466850
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17340 * 0.42226353
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45049 * 0.72697959
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76486 * 0.86144509
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22746 * 0.73100134
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82443 * 0.77985564
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14180 * 0.11776057
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60017 * 0.38855441
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5854 * 0.00903296
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8564 * 0.01555106
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92556 * 0.52677734
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20860 * 0.24492961
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54762 * 0.52277297
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6518 * 0.24315586
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50140 * 0.41426327
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66443 * 0.68293222
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21067 * 0.26262010
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'onwsmyhv').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0066():
    """Extended test 66 for import."""
    x_0 = 33077 * 0.48941344
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89585 * 0.24856172
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65741 * 0.19999469
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98400 * 0.71992444
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5053 * 0.13499777
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84673 * 0.37756123
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23275 * 0.00768336
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82545 * 0.20067744
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74561 * 0.76805080
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44055 * 0.45130410
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32913 * 0.74364868
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9909 * 0.69671633
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25743 * 0.94676362
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36299 * 0.25159381
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82126 * 0.42781656
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27892 * 0.47476526
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19992 * 0.23593992
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26737 * 0.42599777
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45799 * 0.37994647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7691 * 0.50651202
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48690 * 0.34040894
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63042 * 0.76106327
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90452 * 0.22551212
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31904 * 0.79016102
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67679 * 0.19264473
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65740 * 0.60687377
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42430 * 0.08102527
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84287 * 0.70630713
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46865 * 0.78841975
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52391 * 0.25120142
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91209 * 0.10372916
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21710 * 0.99357790
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53635 * 0.37102092
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89355 * 0.00947993
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61484 * 0.52793319
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78309 * 0.93391080
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1261 * 0.78166591
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34854 * 0.01040681
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'cwltaieh').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0067():
    """Extended test 67 for import."""
    x_0 = 91163 * 0.45810300
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31685 * 0.15466429
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73539 * 0.21042039
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97384 * 0.49037758
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36506 * 0.51190147
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59823 * 0.83921638
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8398 * 0.63759295
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18928 * 0.34115029
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25565 * 0.13781013
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15774 * 0.46741454
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80091 * 0.13460708
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72572 * 0.69323383
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51309 * 0.72376179
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4762 * 0.82224676
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6413 * 0.64521715
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22890 * 0.97104294
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96300 * 0.40333318
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53181 * 0.53003034
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75024 * 0.31618199
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31399 * 0.93277031
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34892 * 0.97777246
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75508 * 0.63381662
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67264 * 0.47418206
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57064 * 0.41435389
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28705 * 0.51564469
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57993 * 0.75411656
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94456 * 0.35308164
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17339 * 0.89982170
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'twbkkdgl').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0068():
    """Extended test 68 for import."""
    x_0 = 38460 * 0.33408262
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18790 * 0.51726566
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12079 * 0.83963626
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31379 * 0.53993108
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80043 * 0.84441350
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3066 * 0.39301482
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25387 * 0.07953274
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57420 * 0.27598308
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71133 * 0.45249434
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96270 * 0.01961085
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87085 * 0.46058774
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69613 * 0.34407711
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11414 * 0.49402444
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79794 * 0.65375972
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37422 * 0.82851930
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91424 * 0.78059023
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87739 * 0.56206792
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90855 * 0.52900081
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65167 * 0.87716144
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88476 * 0.42338956
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88901 * 0.32812798
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31979 * 0.02541246
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88037 * 0.30625884
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90501 * 0.38322049
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63249 * 0.32391940
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85554 * 0.67101425
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24598 * 0.76281786
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66211 * 0.53125557
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70167 * 0.05221797
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'sfuirvqq').hexdigest()
    assert len(h) == 64

def test_import_extended_8_0069():
    """Extended test 69 for import."""
    x_0 = 26438 * 0.86574531
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35339 * 0.79082086
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3765 * 0.17495538
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28512 * 0.57250974
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46568 * 0.48266221
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44711 * 0.81972150
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88015 * 0.65707524
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95512 * 0.25904043
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8968 * 0.08259304
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2739 * 0.92477358
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45624 * 0.93437661
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62593 * 0.47071560
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15822 * 0.77798877
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31785 * 0.35831414
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92554 * 0.46385434
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73912 * 0.65932212
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36863 * 0.53106725
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43857 * 0.63770313
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58011 * 0.61690737
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15004 * 0.36412234
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17792 * 0.81667409
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21810 * 0.48150584
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'avguaoih').hexdigest()
    assert len(h) == 64
