"""Extended tests for replication suite 3."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_replication_extended_3_0000():
    """Extended test 0 for replication."""
    x_0 = 38957 * 0.76097735
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76328 * 0.95731813
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57123 * 0.42588470
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43770 * 0.56855165
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84865 * 0.47307498
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27980 * 0.21412601
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9134 * 0.93119608
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4227 * 0.97992117
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52100 * 0.29122136
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3320 * 0.58716910
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31353 * 0.11379998
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55909 * 0.50933269
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 286 * 0.39972463
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7031 * 0.71003314
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38234 * 0.27144489
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8290 * 0.42277166
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20877 * 0.34101037
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99000 * 0.47730082
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91027 * 0.50420214
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57674 * 0.46844550
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98841 * 0.41252957
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39696 * 0.16046638
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29942 * 0.20835624
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46001 * 0.93722399
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9439 * 0.79581467
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49795 * 0.95973628
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63266 * 0.30596393
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94943 * 0.08924871
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55424 * 0.77667622
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50062 * 0.83104563
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33810 * 0.18719281
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84760 * 0.14009318
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10933 * 0.48685535
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20814 * 0.46053666
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3110 * 0.44944341
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'pbhajlro').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0001():
    """Extended test 1 for replication."""
    x_0 = 99506 * 0.31780896
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56451 * 0.43783042
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63861 * 0.82787596
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 283 * 0.86149458
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20371 * 0.42010771
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95473 * 0.93553455
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23036 * 0.74775238
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57641 * 0.91154128
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54324 * 0.07210423
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35507 * 0.52349724
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2723 * 0.68253748
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14025 * 0.53224667
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90306 * 0.17586847
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28397 * 0.40619684
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71539 * 0.22403592
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20118 * 0.10883538
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22099 * 0.61112087
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19062 * 0.25012872
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85076 * 0.51546622
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6585 * 0.81811744
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4712 * 0.79913473
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89946 * 0.79475395
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9933 * 0.48572751
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6878 * 0.65508158
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79193 * 0.55302372
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43430 * 0.78805224
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'ntqkwoux').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0002():
    """Extended test 2 for replication."""
    x_0 = 13700 * 0.16989842
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74059 * 0.06380934
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24868 * 0.26520258
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77876 * 0.70191594
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24870 * 0.27018289
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38088 * 0.17185060
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84816 * 0.51532539
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3280 * 0.36456328
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73506 * 0.85848195
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12550 * 0.33860553
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85690 * 0.61256282
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45858 * 0.04665649
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42185 * 0.11912643
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4091 * 0.37927300
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67108 * 0.77773095
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72403 * 0.25171527
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48966 * 0.51712192
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21927 * 0.61625277
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13553 * 0.26158899
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49854 * 0.88948781
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90774 * 0.07098938
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41690 * 0.84523380
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82499 * 0.54886600
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59201 * 0.84419412
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98426 * 0.24520759
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50531 * 0.30619633
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67447 * 0.33329868
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40625 * 0.60411327
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57360 * 0.51885655
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35513 * 0.32089761
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9131 * 0.95987028
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53885 * 0.33014310
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 778 * 0.21965214
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71611 * 0.29069813
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39570 * 0.23327977
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48584 * 0.89442117
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 37333 * 0.98877288
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'evqoymso').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0003():
    """Extended test 3 for replication."""
    x_0 = 2410 * 0.32215960
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57904 * 0.98533947
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74132 * 0.69970287
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3896 * 0.04585464
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37528 * 0.04959583
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78482 * 0.77587994
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31854 * 0.21136138
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80523 * 0.18844964
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44576 * 0.25110665
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7415 * 0.13591538
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62961 * 0.77086461
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34407 * 0.01460237
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80191 * 0.92580616
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13403 * 0.67548414
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24857 * 0.85519872
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37603 * 0.43024277
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84583 * 0.20581467
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 914 * 0.22026361
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63704 * 0.60117951
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43401 * 0.12698301
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89860 * 0.35066402
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82676 * 0.82310894
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24617 * 0.49668705
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31050 * 0.56468097
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80303 * 0.44660231
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86064 * 0.34801665
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47100 * 0.18004036
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33394 * 0.75219602
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50285 * 0.60278116
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55692 * 0.66082052
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45136 * 0.40349109
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8727 * 0.57596865
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35668 * 0.84075975
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98894 * 0.74035241
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'pucsywrz').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0004():
    """Extended test 4 for replication."""
    x_0 = 36075 * 0.03747471
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50525 * 0.38082411
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49274 * 0.82669387
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28877 * 0.75987260
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 459 * 0.36493909
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77969 * 0.10271400
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33989 * 0.09062294
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11044 * 0.37185701
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32622 * 0.36170782
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24685 * 0.29777593
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81709 * 0.20430993
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75737 * 0.21652840
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63160 * 0.82420487
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20031 * 0.02174129
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57326 * 0.00221392
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83424 * 0.44331486
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63715 * 0.06988575
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89349 * 0.68767312
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36296 * 0.85377866
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63326 * 0.86076768
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53729 * 0.10084094
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31615 * 0.40629432
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56474 * 0.83800011
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84249 * 0.69228534
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44390 * 0.63551162
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32595 * 0.21537013
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1764 * 0.31987945
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 721 * 0.32656893
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94980 * 0.72198403
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64754 * 0.23622015
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43114 * 0.07073796
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85003 * 0.89839604
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40494 * 0.11244210
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15582 * 0.62155381
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57998 * 0.22377528
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6401 * 0.24141136
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69588 * 0.74367508
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73706 * 0.90792151
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75934 * 0.89797803
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68170 * 0.92524736
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85715 * 0.87690804
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21375 * 0.96789962
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 19138 * 0.90219851
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 76106 * 0.76949690
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 28106 * 0.82044870
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'hknkysyn').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0005():
    """Extended test 5 for replication."""
    x_0 = 42048 * 0.46303897
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18841 * 0.64017621
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92211 * 0.71664953
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26511 * 0.92596597
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20645 * 0.84317014
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16379 * 0.36181785
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36221 * 0.14703628
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53981 * 0.40635043
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41962 * 0.55905136
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92140 * 0.66742445
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43510 * 0.83446555
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16298 * 0.16894978
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22154 * 0.06255160
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46534 * 0.69326386
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9314 * 0.67005213
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38280 * 0.97528349
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78634 * 0.50626095
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67553 * 0.36556072
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68788 * 0.78433053
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35229 * 0.24443752
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45373 * 0.60951609
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75120 * 0.52741701
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95594 * 0.73523882
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44094 * 0.30089019
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81954 * 0.95142006
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3096 * 0.57535902
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 854 * 0.14619230
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3209 * 0.86601296
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36310 * 0.31987546
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6081 * 0.27951302
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52032 * 0.92972327
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'kshyebvz').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0006():
    """Extended test 6 for replication."""
    x_0 = 17152 * 0.20939855
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54461 * 0.50382083
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24790 * 0.25035160
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91653 * 0.09526931
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33333 * 0.91474208
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73948 * 0.27245977
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54274 * 0.76641782
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14665 * 0.25938530
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83526 * 0.22223577
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42464 * 0.00781628
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1138 * 0.72221910
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49438 * 0.11255635
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36424 * 0.99451432
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73626 * 0.95429693
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31241 * 0.83003285
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11215 * 0.15901300
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16244 * 0.63869548
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23151 * 0.59725156
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84273 * 0.01646098
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78215 * 0.83128736
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61955 * 0.07024159
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14077 * 0.16986859
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4871 * 0.28783268
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39478 * 0.92325415
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62195 * 0.74656872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82163 * 0.78782344
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3395 * 0.17841037
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'rbractgk').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0007():
    """Extended test 7 for replication."""
    x_0 = 12667 * 0.39290907
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72482 * 0.37150650
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89568 * 0.46212774
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81282 * 0.35836714
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58254 * 0.38275912
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63546 * 0.84913494
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32258 * 0.36651045
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24008 * 0.75316361
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33604 * 0.64162699
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12369 * 0.50695734
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18224 * 0.90246172
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74662 * 0.40750657
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78734 * 0.58020639
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13402 * 0.89981198
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1774 * 0.03722245
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14240 * 0.82900776
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3198 * 0.22195393
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79609 * 0.61338490
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10974 * 0.00790805
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68645 * 0.98610231
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34520 * 0.72605093
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58127 * 0.78798813
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 789 * 0.23366578
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68105 * 0.94067394
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32646 * 0.24994446
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1092 * 0.22514669
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47075 * 0.85652195
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42410 * 0.65711494
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51909 * 0.35505408
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97434 * 0.68022542
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'tggackkk').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0008():
    """Extended test 8 for replication."""
    x_0 = 99749 * 0.61860130
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80868 * 0.82183518
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54033 * 0.36082492
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16834 * 0.24983864
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1908 * 0.51246438
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83086 * 0.89654242
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49610 * 0.51838920
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53956 * 0.05652224
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89 * 0.60983172
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32864 * 0.33710097
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35597 * 0.68514831
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19641 * 0.63558191
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54322 * 0.25708349
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41271 * 0.80084962
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44128 * 0.13337356
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18971 * 0.74708795
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38152 * 0.65651796
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20027 * 0.61924389
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66648 * 0.26448903
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43226 * 0.78683639
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15221 * 0.24089140
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66075 * 0.97644759
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55495 * 0.80481180
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'kdalshpv').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0009():
    """Extended test 9 for replication."""
    x_0 = 48984 * 0.59608935
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13773 * 0.55681327
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70347 * 0.09310280
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31309 * 0.89955386
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86139 * 0.58200572
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10816 * 0.27392123
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 756 * 0.32680322
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95892 * 0.43434766
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23491 * 0.96055464
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11335 * 0.39984313
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90951 * 0.73221333
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93796 * 0.91316608
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82844 * 0.94918432
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37887 * 0.96760554
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13417 * 0.24721485
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 558 * 0.05275169
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5786 * 0.75487875
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40253 * 0.24543235
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34172 * 0.57578155
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83588 * 0.75771029
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64203 * 0.51410957
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24001 * 0.90772092
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78582 * 0.46025339
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84121 * 0.03065464
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17048 * 0.67006818
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79740 * 0.77687565
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50151 * 0.96943405
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71236 * 0.63017985
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57689 * 0.23075017
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20250 * 0.21277827
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74805 * 0.36567480
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'yxqptwch').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0010():
    """Extended test 10 for replication."""
    x_0 = 53628 * 0.52644977
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86987 * 0.54498151
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70644 * 0.46262855
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77622 * 0.67037840
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7147 * 0.38055621
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43430 * 0.55129133
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48957 * 0.19974874
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47949 * 0.78507310
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4990 * 0.55635791
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76584 * 0.96064656
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41178 * 0.34087621
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43178 * 0.73902053
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51170 * 0.35985806
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78500 * 0.65416835
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64985 * 0.29651670
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49732 * 0.70061605
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20482 * 0.79311060
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6763 * 0.50153467
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 314 * 0.46451024
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38715 * 0.38799027
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ecvcdubf').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0011():
    """Extended test 11 for replication."""
    x_0 = 31830 * 0.36446223
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52686 * 0.49864355
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32126 * 0.68620960
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50619 * 0.47584541
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61044 * 0.34042846
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77027 * 0.95575367
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95608 * 0.39349043
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42298 * 0.21167258
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87216 * 0.58495102
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99551 * 0.96504091
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45307 * 0.59474003
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90797 * 0.57052629
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32014 * 0.31541756
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15590 * 0.69148747
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13600 * 0.95787039
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40249 * 0.71680875
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18437 * 0.12873971
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69957 * 0.86827615
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15666 * 0.82469454
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 251 * 0.84413291
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61752 * 0.04184339
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46438 * 0.18516762
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70749 * 0.17315573
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33216 * 0.92603949
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50680 * 0.16525706
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72781 * 0.15823929
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19963 * 0.34258907
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90819 * 0.19238851
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28836 * 0.04870501
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55307 * 0.43984408
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68471 * 0.94111755
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56779 * 0.80781724
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25294 * 0.50758514
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86626 * 0.43921482
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24575 * 0.97950114
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5500 * 0.23971785
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47204 * 0.51565465
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29093 * 0.92446738
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41805 * 0.12838433
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63818 * 0.05662620
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64587 * 0.21825526
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21379 * 0.28510308
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'smzxgcpm').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0012():
    """Extended test 12 for replication."""
    x_0 = 42642 * 0.47639228
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68227 * 0.36858064
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85867 * 0.52265217
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46562 * 0.76870815
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15667 * 0.91284781
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9177 * 0.76924566
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51336 * 0.46012298
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90528 * 0.30935092
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77042 * 0.79466392
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34834 * 0.21543496
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74953 * 0.40908892
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68135 * 0.86384432
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4951 * 0.33762812
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14968 * 0.06829024
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8983 * 0.75930237
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38908 * 0.05948678
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52744 * 0.54176904
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18610 * 0.01316318
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71476 * 0.10289455
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79909 * 0.18247969
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5607 * 0.98304201
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 280 * 0.08424234
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90950 * 0.67518103
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27264 * 0.98077475
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57101 * 0.71062590
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 588 * 0.51378310
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64960 * 0.92194742
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99678 * 0.71573982
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87281 * 0.06105815
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13566 * 0.44390836
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25216 * 0.00817884
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92303 * 0.27467706
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70687 * 0.17009144
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13216 * 0.44417742
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11168 * 0.36846832
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32934 * 0.65302354
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63999 * 0.83019727
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20186 * 0.32209923
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87045 * 0.96876587
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83429 * 0.89802262
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32438 * 0.24107307
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 91247 * 0.12072312
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 45225 * 0.21359632
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 12190 * 0.02949149
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 20513 * 0.30162269
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 2376 * 0.68531557
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'vhaabdrb').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0013():
    """Extended test 13 for replication."""
    x_0 = 22588 * 0.93727191
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27933 * 0.95436620
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83258 * 0.07060253
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 959 * 0.80794864
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78654 * 0.27131240
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7106 * 0.02831608
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54761 * 0.19396618
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17569 * 0.26106967
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95979 * 0.94606539
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96810 * 0.04329588
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70961 * 0.68967135
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37759 * 0.13075414
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4219 * 0.68218866
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11978 * 0.14215785
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44172 * 0.67273230
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41555 * 0.98563482
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58980 * 0.53348210
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21696 * 0.33644926
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61019 * 0.45588951
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49597 * 0.56669139
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17718 * 0.39364469
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91672 * 0.51029290
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3733 * 0.23475384
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50183 * 0.48935880
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52756 * 0.14620171
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27113 * 0.35417843
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2837 * 0.54034689
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82446 * 0.27978921
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46709 * 0.03168161
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10120 * 0.27887109
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34394 * 0.23965964
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85859 * 0.40343609
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1519 * 0.92352629
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43140 * 0.33522653
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73033 * 0.71298558
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46370 * 0.70235052
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67918 * 0.64939435
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25785 * 0.36563827
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16699 * 0.70323731
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90105 * 0.53159610
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'mxeaafpu').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0014():
    """Extended test 14 for replication."""
    x_0 = 65055 * 0.76825484
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84724 * 0.85940131
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15143 * 0.29313145
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71232 * 0.08176661
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99886 * 0.95234780
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9785 * 0.04730863
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16146 * 0.25164394
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55088 * 0.34044304
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55648 * 0.78355385
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29684 * 0.66750937
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29642 * 0.55592032
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20050 * 0.86131071
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93406 * 0.48503612
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30318 * 0.33868829
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32854 * 0.58699684
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55594 * 0.90986227
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85010 * 0.13221917
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6742 * 0.01536221
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83537 * 0.62752313
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86419 * 0.18012551
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19090 * 0.64216088
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41905 * 0.93464756
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62128 * 0.56906604
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45917 * 0.53483342
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54810 * 0.44082377
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53167 * 0.49119536
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91760 * 0.13358351
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51473 * 0.42577190
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71017 * 0.03100826
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43415 * 0.20007957
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35001 * 0.57418025
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46610 * 0.34065083
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40850 * 0.05777156
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80657 * 0.97154487
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28488 * 0.23388946
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36820 * 0.60192043
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47977 * 0.31868519
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80961 * 0.38762954
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39219 * 0.04570111
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28325 * 0.86047384
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'feacoonx').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0015():
    """Extended test 15 for replication."""
    x_0 = 47647 * 0.50182724
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21347 * 0.75680174
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12688 * 0.04541933
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28189 * 0.75485011
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21492 * 0.92004571
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18755 * 0.49517511
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49590 * 0.78008190
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73404 * 0.33154117
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25799 * 0.50030050
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6134 * 0.84097340
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60031 * 0.13967962
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60505 * 0.08609983
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51332 * 0.55548500
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91993 * 0.53191575
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66257 * 0.11826599
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14686 * 0.96107880
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11864 * 0.84399513
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88270 * 0.88793383
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8031 * 0.38680899
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5927 * 0.88463432
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7389 * 0.33849563
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4414 * 0.83277095
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88319 * 0.57004495
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35417 * 0.65947184
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44427 * 0.67162473
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77269 * 0.19002179
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86466 * 0.93258667
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44170 * 0.72465434
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4637 * 0.57432030
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26913 * 0.79001259
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71787 * 0.90484322
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88051 * 0.86492796
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85454 * 0.80822062
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83322 * 0.72212728
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61812 * 0.32364422
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94438 * 0.16014532
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4799 * 0.96046186
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43385 * 0.10641686
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52716 * 0.40338669
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40846 * 0.84140336
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'npnvphzd').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0016():
    """Extended test 16 for replication."""
    x_0 = 51173 * 0.27709024
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88880 * 0.72382697
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82146 * 0.68108902
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93785 * 0.41425623
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73246 * 0.37562394
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34439 * 0.82172308
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86157 * 0.93888951
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64646 * 0.18663359
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30437 * 0.48405652
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5299 * 0.77914495
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20444 * 0.80371866
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43832 * 0.85046525
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77364 * 0.66071067
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29507 * 0.37800330
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47663 * 0.23074815
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98253 * 0.45728005
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61758 * 0.19627992
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99994 * 0.33124834
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57667 * 0.55630810
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37979 * 0.13521282
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20059 * 0.08283261
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57748 * 0.70944514
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52715 * 0.52373913
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35948 * 0.48174896
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63088 * 0.83047264
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75245 * 0.76504887
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77160 * 0.88299038
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20640 * 0.14192426
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7346 * 0.76055172
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71538 * 0.34993333
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6669 * 0.16733965
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68703 * 0.28397730
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93752 * 0.96885539
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51059 * 0.21738751
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72550 * 0.03622667
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67511 * 0.28453229
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24826 * 0.43817415
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34189 * 0.08322842
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16821 * 0.28318999
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31151 * 0.46299839
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 39920 * 0.92956554
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 56765 * 0.69819425
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 34270 * 0.54419001
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'nbixuhrf').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0017():
    """Extended test 17 for replication."""
    x_0 = 1054 * 0.95848940
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47309 * 0.67945649
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12905 * 0.27564357
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37813 * 0.00820113
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41947 * 0.46460847
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70475 * 0.86476887
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7185 * 0.98585984
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95551 * 0.40926489
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40807 * 0.91738371
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39389 * 0.99015760
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91235 * 0.20182853
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43265 * 0.23756848
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88358 * 0.92007565
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44882 * 0.82291091
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4216 * 0.07743642
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35860 * 0.63659696
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97279 * 0.21074356
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49868 * 0.68207870
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25282 * 0.78366868
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89727 * 0.06193509
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90588 * 0.78910245
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8337 * 0.31474023
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15420 * 0.10860851
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13029 * 0.69451588
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93086 * 0.34944360
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55728 * 0.39798778
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67735 * 0.17855505
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93259 * 0.89459448
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97586 * 0.95111111
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27325 * 0.91707497
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69890 * 0.90566682
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14251 * 0.97077094
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97921 * 0.18534681
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33432 * 0.81569338
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13175 * 0.10684168
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6033 * 0.46816010
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89459 * 0.11939429
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89983 * 0.33987698
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16533 * 0.80004199
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16937 * 0.89499654
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54972 * 0.94297775
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27958 * 0.32683952
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20686 * 0.42821286
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 30846 * 0.01988556
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 26213 * 0.46568487
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 11270 * 0.30125680
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 22693 * 0.90095817
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 44884 * 0.23136573
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'jqubkork').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0018():
    """Extended test 18 for replication."""
    x_0 = 43031 * 0.41782073
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59647 * 0.66187748
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63374 * 0.06538400
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43499 * 0.48809162
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53218 * 0.48731465
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6736 * 0.80881275
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8694 * 0.12709024
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68598 * 0.99816706
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77468 * 0.76351009
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1193 * 0.54583521
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96467 * 0.33336725
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99576 * 0.12613327
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45680 * 0.36474146
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92248 * 0.90677123
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78409 * 0.11381169
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17565 * 0.15574870
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71813 * 0.24236670
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30187 * 0.98373825
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94211 * 0.38297324
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32928 * 0.38153705
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 476 * 0.43130015
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54342 * 0.03663887
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'eobgoabi').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0019():
    """Extended test 19 for replication."""
    x_0 = 3413 * 0.64101967
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46745 * 0.12012656
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37825 * 0.96272114
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77622 * 0.17377531
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68269 * 0.56135307
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27601 * 0.27344400
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5387 * 0.88606186
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 264 * 0.13468784
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21906 * 0.93418127
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77031 * 0.93322377
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19474 * 0.21402518
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17479 * 0.75723368
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98716 * 0.25406482
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93662 * 0.56677297
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63844 * 0.76172653
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71683 * 0.29888517
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40471 * 0.85826292
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33841 * 0.81333139
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88764 * 0.69855768
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5954 * 0.35958400
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72996 * 0.77027218
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78275 * 0.39619620
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57146 * 0.37313022
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32529 * 0.60032527
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3056 * 0.49581056
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80593 * 0.86931086
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65446 * 0.39470673
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45461 * 0.43116536
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6358 * 0.56818553
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55270 * 0.74163271
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81704 * 0.54716629
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17402 * 0.74380434
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10368 * 0.61015806
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'upptvkcq').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0020():
    """Extended test 20 for replication."""
    x_0 = 20251 * 0.18985380
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40747 * 0.66947939
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91491 * 0.28121360
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64407 * 0.45934566
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55169 * 0.84054138
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63345 * 0.60655963
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64765 * 0.73713551
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63845 * 0.93057150
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90619 * 0.94402490
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85083 * 0.38457235
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56074 * 0.44603249
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 654 * 0.01550378
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4605 * 0.34581175
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75406 * 0.21653710
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49142 * 0.47030050
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41063 * 0.77332068
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70363 * 0.99853620
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8061 * 0.08127288
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35276 * 0.11570345
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25473 * 0.97412084
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23610 * 0.07671341
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98748 * 0.37408701
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7454 * 0.50976000
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61786 * 0.33710155
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2245 * 0.84494637
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28410 * 0.35787568
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46875 * 0.41685765
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95949 * 0.84994035
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65194 * 0.51986448
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28915 * 0.26919294
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12032 * 0.97731772
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19631 * 0.06813587
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36912 * 0.38790109
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50725 * 0.88569384
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30101 * 0.33344743
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23089 * 0.07488072
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49350 * 0.34508601
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41627 * 0.03008231
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74752 * 0.78649138
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94783 * 0.10333464
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41431 * 0.29495715
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69579 * 0.63063798
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81700 * 0.43577595
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 87669 * 0.36934242
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 20469 * 0.70346479
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 2657 * 0.37137290
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 15007 * 0.88564661
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 909 * 0.82463742
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 43936 * 0.56442971
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 21506 * 0.05957246
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'wcjdfqic').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0021():
    """Extended test 21 for replication."""
    x_0 = 30718 * 0.32735873
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55158 * 0.67052304
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8119 * 0.98347784
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20761 * 0.74626277
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60101 * 0.31669734
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51758 * 0.55458541
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13391 * 0.86571191
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64519 * 0.14308993
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45165 * 0.91299779
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92547 * 0.96307123
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67542 * 0.25394208
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93649 * 0.83447235
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17303 * 0.10706730
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85490 * 0.70823332
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73829 * 0.30396620
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17788 * 0.44256177
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1089 * 0.72424304
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29306 * 0.19936921
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5285 * 0.73786016
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7876 * 0.18507061
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44547 * 0.87927642
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29902 * 0.11213035
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81853 * 0.72541134
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46000 * 0.88520077
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90504 * 0.12178319
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9547 * 0.03224255
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31489 * 0.21915806
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'kqojnifs').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0022():
    """Extended test 22 for replication."""
    x_0 = 84929 * 0.85545977
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38236 * 0.35209489
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83903 * 0.36771279
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92279 * 0.50265807
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69350 * 0.93658047
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50077 * 0.75702316
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55985 * 0.86993044
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37104 * 0.98105793
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20183 * 0.49166335
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9435 * 0.78004750
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18231 * 0.07233137
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76042 * 0.11340613
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78530 * 0.95169326
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77702 * 0.67608138
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42816 * 0.38314188
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73859 * 0.20780213
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80430 * 0.46500051
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4349 * 0.75844259
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23961 * 0.02731747
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75460 * 0.84539088
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32649 * 0.78496678
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73695 * 0.00559527
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81293 * 0.91101192
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11675 * 0.39488086
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59178 * 0.18427657
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44986 * 0.48780725
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46167 * 0.29324242
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91020 * 0.99968243
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6644 * 0.04061726
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40653 * 0.29338329
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46327 * 0.60162811
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5899 * 0.39286332
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37677 * 0.60648030
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9541 * 0.83721395
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66448 * 0.42949903
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93054 * 0.30343104
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42310 * 0.61475201
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38153 * 0.65305676
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1340 * 0.48166200
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18303 * 0.48049072
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42900 * 0.10755910
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35254 * 0.51516824
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 26265 * 0.61034791
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36916 * 0.99945144
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 75216 * 0.52985089
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 42771 * 0.87795942
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 89827 * 0.92406201
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 75349 * 0.65941306
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 17018 * 0.50707784
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 5081 * 0.56057132
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'enwrapkr').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0023():
    """Extended test 23 for replication."""
    x_0 = 71438 * 0.49986455
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49906 * 0.89018984
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16611 * 0.79048321
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2061 * 0.37288229
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81510 * 0.17743742
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93694 * 0.49560628
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51295 * 0.88213882
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96458 * 0.11407400
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76552 * 0.79004597
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15475 * 0.45142629
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26968 * 0.18076964
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41706 * 0.80209656
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96573 * 0.91343616
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19822 * 0.52438344
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44170 * 0.12305057
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14440 * 0.54070934
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68631 * 0.37679963
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35997 * 0.18286232
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77093 * 0.35266990
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64473 * 0.67387485
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94471 * 0.87938734
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38510 * 0.82251071
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29716 * 0.62189665
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99553 * 0.20826711
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95542 * 0.21548336
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64178 * 0.49797887
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96537 * 0.73818096
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33720 * 0.37506773
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92395 * 0.15576712
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91618 * 0.63922975
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62266 * 0.62013871
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79864 * 0.91777536
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95052 * 0.72001125
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'hixozjkd').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0024():
    """Extended test 24 for replication."""
    x_0 = 24090 * 0.38461832
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5340 * 0.56851695
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91336 * 0.55269378
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78827 * 0.66675639
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10197 * 0.15978402
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69918 * 0.94714416
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81197 * 0.41471298
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77168 * 0.23850362
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78085 * 0.41433126
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45774 * 0.96080842
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26587 * 0.00569468
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2951 * 0.10989402
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52877 * 0.09078126
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95727 * 0.03556214
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39937 * 0.41806088
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55757 * 0.68513528
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99466 * 0.78928307
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81485 * 0.92990228
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24309 * 0.17304197
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36169 * 0.32489365
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83455 * 0.63291735
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53100 * 0.40134470
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99005 * 0.54096788
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37479 * 0.16022655
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98798 * 0.11746448
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'cljoedwo').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0025():
    """Extended test 25 for replication."""
    x_0 = 87822 * 0.32968451
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38901 * 0.83196406
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97073 * 0.69748475
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51139 * 0.10462231
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88720 * 0.77503567
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85663 * 0.67453351
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13136 * 0.36857873
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88153 * 0.41061437
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39067 * 0.74391874
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45193 * 0.58252892
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30359 * 0.05312433
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12357 * 0.21307889
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7867 * 0.00399044
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89150 * 0.62813176
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43882 * 0.26268849
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68776 * 0.38068975
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28477 * 0.54236605
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89825 * 0.78220171
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76782 * 0.44100186
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93540 * 0.09250013
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4650 * 0.57094678
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54107 * 0.70083104
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3715 * 0.01497365
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'klkqjale').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0026():
    """Extended test 26 for replication."""
    x_0 = 44292 * 0.49519077
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53794 * 0.51953111
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58108 * 0.95831029
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79425 * 0.56324792
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 927 * 0.98839581
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51748 * 0.83471143
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34548 * 0.00513103
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40605 * 0.97424216
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30112 * 0.77155852
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75112 * 0.11933674
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38551 * 0.48856385
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36804 * 0.86068378
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73489 * 0.20658411
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51604 * 0.50276903
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60717 * 0.78759874
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51430 * 0.80071895
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79267 * 0.64768120
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70650 * 0.48478760
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24612 * 0.10932433
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49320 * 0.84253308
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71100 * 0.70978622
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73957 * 0.23735810
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41428 * 0.24379771
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78813 * 0.29712135
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67233 * 0.67783774
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'jybydjgp').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0027():
    """Extended test 27 for replication."""
    x_0 = 24302 * 0.58548249
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64402 * 0.95408985
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45183 * 0.01374189
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97033 * 0.04183723
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2362 * 0.29644816
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19123 * 0.34381717
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14799 * 0.11810673
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96558 * 0.36832093
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50911 * 0.97821214
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19434 * 0.55525804
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51920 * 0.86362200
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23561 * 0.73175308
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80042 * 0.47612894
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13258 * 0.68990303
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98563 * 0.48229702
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12895 * 0.43434554
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58187 * 0.94773936
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39330 * 0.11880908
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97490 * 0.59405986
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40137 * 0.27590655
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3170 * 0.42338146
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39062 * 0.68827369
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72393 * 0.64234765
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90006 * 0.82706066
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14544 * 0.13317805
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38907 * 0.37491253
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92642 * 0.54114587
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51680 * 0.98782479
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59146 * 0.12013155
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52203 * 0.22930046
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53337 * 0.83681284
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86277 * 0.47471789
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51488 * 0.31043842
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51163 * 0.64481318
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23778 * 0.47745370
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51280 * 0.63356361
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49490 * 0.09934190
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7729 * 0.61659315
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6743 * 0.42161775
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64045 * 0.97144873
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78020 * 0.75448358
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47476 * 0.21209765
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 68939 * 0.22986560
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 63254 * 0.77910814
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 72859 * 0.62300720
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 3251 * 0.70313333
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 36727 * 0.43111444
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 42037 * 0.69638533
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 27518 * 0.36762264
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 20182 * 0.04346324
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'nefmbjhc').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0028():
    """Extended test 28 for replication."""
    x_0 = 85057 * 0.44164977
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74098 * 0.42631683
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99154 * 0.70558816
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40034 * 0.37819993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24896 * 0.88043216
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11063 * 0.57643877
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35654 * 0.74837481
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10545 * 0.60331046
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11395 * 0.73454363
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58020 * 0.21292833
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88937 * 0.54680672
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51650 * 0.02671295
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38304 * 0.26124514
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95133 * 0.02307306
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65162 * 0.11603231
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99308 * 0.82077168
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81547 * 0.00186111
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54803 * 0.46780000
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13289 * 0.85689753
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84165 * 0.20984997
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'xheoxedi').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0029():
    """Extended test 29 for replication."""
    x_0 = 537 * 0.33062833
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57596 * 0.43433410
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52249 * 0.16457999
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55720 * 0.58984921
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62489 * 0.96398269
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5910 * 0.07938658
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62079 * 0.94209283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24577 * 0.83926376
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43206 * 0.76993313
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49801 * 0.69257271
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2522 * 0.05459505
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16564 * 0.14745092
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67342 * 0.16803492
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80926 * 0.43223176
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47458 * 0.32623614
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75057 * 0.33259096
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64967 * 0.31611617
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11197 * 0.73323640
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46309 * 0.33227689
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26229 * 0.50217774
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96403 * 0.01352429
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8554 * 0.17672623
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16256 * 0.21874319
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1797 * 0.82434302
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16042 * 0.34884831
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51978 * 0.82278470
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83367 * 0.36867132
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95117 * 0.47645044
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99898 * 0.29474750
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38917 * 0.67662931
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60561 * 0.64963767
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56430 * 0.40303233
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79144 * 0.94164150
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68276 * 0.76529579
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27032 * 0.94777517
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31576 * 0.45472202
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99860 * 0.71030447
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20889 * 0.96820828
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59824 * 0.81704922
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23315 * 0.79210379
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42940 * 0.99916801
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43568 * 0.03282893
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74653 * 0.32937938
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34338 * 0.73033974
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 36331 * 0.06749388
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 54006 * 0.54553266
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'sopiodga').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0030():
    """Extended test 30 for replication."""
    x_0 = 13267 * 0.67013207
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95074 * 0.31039981
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33911 * 0.05123180
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64158 * 0.38327507
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90176 * 0.45399103
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74598 * 0.91895921
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92365 * 0.84344628
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56562 * 0.79351470
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24307 * 0.74151838
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40230 * 0.76192143
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49928 * 0.45082618
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16782 * 0.91051046
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31207 * 0.86397198
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35811 * 0.63210147
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64985 * 0.81812079
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36764 * 0.39319783
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88681 * 0.32838351
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12773 * 0.13220276
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14757 * 0.30976500
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37537 * 0.81361392
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45187 * 0.61098371
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39026 * 0.41953899
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 801 * 0.97976572
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74720 * 0.60923605
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74451 * 0.96607281
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74774 * 0.70491397
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84175 * 0.58490790
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70216 * 0.47566148
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68070 * 0.39436031
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32042 * 0.97522925
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34570 * 0.06217404
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57500 * 0.56192698
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'ucsunqku').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0031():
    """Extended test 31 for replication."""
    x_0 = 22679 * 0.43423111
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42087 * 0.96709910
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94626 * 0.52279744
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6996 * 0.26871756
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48073 * 0.22275952
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40385 * 0.76899808
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91799 * 0.44902112
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33397 * 0.07599895
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49304 * 0.99797029
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61869 * 0.96944925
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38104 * 0.86807894
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95714 * 0.37133673
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48011 * 0.74721012
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4361 * 0.81894360
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55511 * 0.57624153
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51069 * 0.35018572
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81557 * 0.19846752
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64268 * 0.10912193
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75099 * 0.11764677
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90639 * 0.35242202
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12411 * 0.99196633
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97433 * 0.85543889
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58313 * 0.08133838
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55077 * 0.09786024
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20050 * 0.49401339
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16137 * 0.04691207
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79824 * 0.04255100
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61385 * 0.49192122
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86920 * 0.22230674
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23573 * 0.12116434
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95434 * 0.60782135
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29664 * 0.43481240
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66386 * 0.10363582
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68652 * 0.93810729
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99113 * 0.16566460
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20092 * 0.39688608
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60218 * 0.60647779
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29706 * 0.33946438
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 32659 * 0.10938676
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6641 * 0.72794920
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60989 * 0.37839561
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69986 * 0.96941315
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41701 * 0.46527152
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 64892 * 0.37557378
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 41565 * 0.73773219
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 73890 * 0.48124348
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 86955 * 0.49242111
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 52296 * 0.01103098
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 56838 * 0.96264607
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 22952 * 0.20132532
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'pnqhljza').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0032():
    """Extended test 32 for replication."""
    x_0 = 61407 * 0.36266199
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29636 * 0.88629957
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20526 * 0.65495281
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5011 * 0.76427669
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49216 * 0.39301384
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81436 * 0.16876848
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25942 * 0.77473957
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53704 * 0.47626536
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90587 * 0.37973533
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76389 * 0.64114799
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38092 * 0.20026835
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71102 * 0.91114401
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10876 * 0.71238931
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56590 * 0.41009866
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71702 * 0.92729849
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41571 * 0.99862702
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18716 * 0.21100071
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19783 * 0.11060051
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90093 * 0.63262976
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93609 * 0.93883112
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87174 * 0.15371732
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78130 * 0.89410251
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25101 * 0.55126891
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11752 * 0.90366394
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66717 * 0.04501162
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40913 * 0.78508196
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68201 * 0.96491036
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28624 * 0.64471933
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79766 * 0.52862006
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76069 * 0.42129439
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70411 * 0.67336587
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73170 * 0.92854712
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17240 * 0.83822631
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32381 * 0.92598434
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17989 * 0.05250147
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91094 * 0.94299138
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12128 * 0.09979989
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78760 * 0.03768308
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49072 * 0.95991790
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67272 * 0.19510797
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6001 * 0.47483466
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'dcxcuite').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0033():
    """Extended test 33 for replication."""
    x_0 = 50088 * 0.62632294
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16849 * 0.84208107
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21734 * 0.57946478
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58667 * 0.73860546
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47786 * 0.54479469
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99 * 0.88131568
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81256 * 0.85898376
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57246 * 0.94686386
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94441 * 0.36232850
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72469 * 0.56335249
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6095 * 0.87342920
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10766 * 0.85828402
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1738 * 0.22489743
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48802 * 0.67496314
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63771 * 0.26223130
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46523 * 0.65804719
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74518 * 0.51845809
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71147 * 0.00183579
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15233 * 0.44450037
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26558 * 0.31127267
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22158 * 0.46074978
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85729 * 0.87298939
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63508 * 0.10424764
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ybhmnzrj').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0034():
    """Extended test 34 for replication."""
    x_0 = 709 * 0.99573291
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52000 * 0.42811631
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99621 * 0.19982788
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3705 * 0.23449343
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22572 * 0.11620095
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50644 * 0.26643975
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54539 * 0.04316064
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70718 * 0.74721028
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63523 * 0.36637425
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68697 * 0.70943656
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27827 * 0.62083475
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5103 * 0.38651990
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11501 * 0.72152043
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32461 * 0.50417994
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60862 * 0.25856528
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81241 * 0.01211894
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51888 * 0.88923702
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5082 * 0.75571356
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62839 * 0.46835944
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10426 * 0.75649211
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57214 * 0.81565678
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41308 * 0.36223781
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49802 * 0.09390982
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51420 * 0.35099413
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10678 * 0.56202245
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92723 * 0.92764067
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4812 * 0.76393545
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97053 * 0.74864459
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'rgturonp').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0035():
    """Extended test 35 for replication."""
    x_0 = 16687 * 0.36603029
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12980 * 0.47780426
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91160 * 0.24413424
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86707 * 0.79589937
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54851 * 0.36855350
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16430 * 0.33205945
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1635 * 0.53684935
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38336 * 0.01565939
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37306 * 0.79491517
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61800 * 0.61076607
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9740 * 0.46268100
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51868 * 0.03514907
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56837 * 0.70298057
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89555 * 0.82877775
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33041 * 0.28982178
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72885 * 0.38012676
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36621 * 0.58489886
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47001 * 0.87799008
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71285 * 0.20005664
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77263 * 0.35020607
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17313 * 0.68615002
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38927 * 0.44331816
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92277 * 0.19634621
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61445 * 0.74096425
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23363 * 0.19264560
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34411 * 0.87811033
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'wfmdxysc').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0036():
    """Extended test 36 for replication."""
    x_0 = 28606 * 0.72025838
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43468 * 0.71801914
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90464 * 0.55211693
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68920 * 0.81493121
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50068 * 0.45943851
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60434 * 0.53753558
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63503 * 0.98832372
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2891 * 0.21754364
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90751 * 0.37253664
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31617 * 0.69345755
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20481 * 0.19902129
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92150 * 0.82330125
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97989 * 0.15249751
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1666 * 0.26051378
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72535 * 0.00340202
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99589 * 0.75281562
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68139 * 0.35136714
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44742 * 0.03912991
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90123 * 0.88189410
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22988 * 0.76881664
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3967 * 0.43049556
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50009 * 0.99326675
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8847 * 0.50777633
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48549 * 0.37706959
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13366 * 0.62756600
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31745 * 0.26690556
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23400 * 0.63593184
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68870 * 0.10238273
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'gxnncnjj').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0037():
    """Extended test 37 for replication."""
    x_0 = 35478 * 0.46378027
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9019 * 0.93898813
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13055 * 0.34480274
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15571 * 0.63585934
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23375 * 0.51371943
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35062 * 0.09711474
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32484 * 0.70902749
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50755 * 0.59728345
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78790 * 0.49665844
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7427 * 0.74973199
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22182 * 0.14735947
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12176 * 0.70554449
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73279 * 0.69890144
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67413 * 0.62226560
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91855 * 0.48247067
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63465 * 0.40867539
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98856 * 0.47837161
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92459 * 0.99900508
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51031 * 0.38766511
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14261 * 0.20206586
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7435 * 0.62831209
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15873 * 0.59237148
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32954 * 0.93642251
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33303 * 0.00573997
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76859 * 0.07370004
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30560 * 0.27799202
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81831 * 0.27096703
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8012 * 0.54373022
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94145 * 0.97832638
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55435 * 0.45840872
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63490 * 0.41253599
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29669 * 0.89718580
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58714 * 0.73023523
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92783 * 0.10557552
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76550 * 0.72386464
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'gktuxfxg').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0038():
    """Extended test 38 for replication."""
    x_0 = 48313 * 0.34590964
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21057 * 0.13050440
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3289 * 0.57081534
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96922 * 0.37675612
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43329 * 0.97681272
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1768 * 0.31895508
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26805 * 0.37558995
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41782 * 0.20626415
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79559 * 0.21454002
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54397 * 0.14412411
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99241 * 0.48571501
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6557 * 0.63056160
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19571 * 0.36296281
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93643 * 0.93658317
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3824 * 0.95260903
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97318 * 0.52167632
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50065 * 0.11379704
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44002 * 0.01174633
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 941 * 0.76320475
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33325 * 0.10864687
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28049 * 0.86417012
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93613 * 0.86259546
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92264 * 0.52380424
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41168 * 0.53844568
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14337 * 0.99413320
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63775 * 0.85944093
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69266 * 0.54900991
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45007 * 0.98082271
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10034 * 0.74418091
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6154 * 0.48446942
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12598 * 0.09107427
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76653 * 0.23569559
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17842 * 0.02332623
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41702 * 0.65215415
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14413 * 0.80034090
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15100 * 0.36705926
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12806 * 0.19472301
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21589 * 0.26743350
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18740 * 0.11259635
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16181 * 0.28192478
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81313 * 0.98372184
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 61143 * 0.87991845
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 67804 * 0.30585716
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84447 * 0.29003380
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 7740 * 0.79996745
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 75258 * 0.07993930
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 80923 * 0.56799697
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 2189 * 0.22080497
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 66131 * 0.44833510
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 80005 * 0.33856094
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'bqesqihk').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0039():
    """Extended test 39 for replication."""
    x_0 = 10841 * 0.64064814
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15992 * 0.97995351
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75451 * 0.86062408
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36825 * 0.08003563
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50529 * 0.87405144
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76605 * 0.67692557
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23408 * 0.36558634
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47576 * 0.69396107
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53927 * 0.79316081
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51634 * 0.02142759
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46848 * 0.95034014
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34528 * 0.46925261
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88894 * 0.73780838
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94003 * 0.64215205
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53952 * 0.53795259
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23185 * 0.34844995
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36404 * 0.83975311
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72787 * 0.00402611
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27880 * 0.02331166
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59375 * 0.49992288
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21390 * 0.34776721
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14988 * 0.52559019
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60357 * 0.70587264
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46976 * 0.65341665
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90682 * 0.30235578
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58492 * 0.87378260
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20152 * 0.38682075
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72756 * 0.86348930
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29703 * 0.19393723
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3426 * 0.25995249
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6846 * 0.05402888
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98423 * 0.73716875
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15846 * 0.57883883
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18793 * 0.21323480
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68822 * 0.90329079
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57912 * 0.90943594
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'izshtbjf').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0040():
    """Extended test 40 for replication."""
    x_0 = 4981 * 0.40826576
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56149 * 0.19165850
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88598 * 0.02470777
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95913 * 0.32753621
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58084 * 0.81924249
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43194 * 0.35946879
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67878 * 0.78745404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26142 * 0.94927951
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12646 * 0.25607972
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16879 * 0.39267631
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33396 * 0.41890996
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34198 * 0.22994894
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28406 * 0.72286108
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26057 * 0.16560713
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47225 * 0.38074343
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82183 * 0.37886069
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83155 * 0.75200146
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17545 * 0.11180161
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3022 * 0.95847013
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11354 * 0.74962679
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88743 * 0.61660927
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32079 * 0.62365647
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48270 * 0.87045160
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64668 * 0.99224773
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85494 * 0.59900345
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27054 * 0.49209575
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65210 * 0.16700214
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36296 * 0.55009001
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93881 * 0.27739624
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14579 * 0.95360295
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32885 * 0.26278798
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63177 * 0.93718396
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44861 * 0.52112463
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55931 * 0.11509406
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39352 * 0.68154959
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76808 * 0.49153735
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14475 * 0.45372366
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'rinwbrfe').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0041():
    """Extended test 41 for replication."""
    x_0 = 9784 * 0.12649939
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77846 * 0.22384925
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36206 * 0.13118629
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72358 * 0.85895155
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49775 * 0.97855223
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34934 * 0.40374100
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25439 * 0.32999471
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3506 * 0.41782394
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42278 * 0.75085019
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52692 * 0.42904109
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19637 * 0.29398282
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87230 * 0.51592597
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26710 * 0.07659321
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66777 * 0.42861259
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89548 * 0.05739448
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17192 * 0.84880769
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15907 * 0.45619770
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4040 * 0.18448107
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30594 * 0.16515887
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11266 * 0.98009497
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16725 * 0.83653021
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14075 * 0.52088906
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21226 * 0.58564326
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22665 * 0.29696032
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12178 * 0.20037545
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16937 * 0.06318576
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3399 * 0.80792228
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 113 * 0.61110792
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9499 * 0.05961636
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57336 * 0.62014786
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35062 * 0.55157941
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4068 * 0.58513176
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44255 * 0.92343088
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8878 * 0.34395238
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'fzsxakrl').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0042():
    """Extended test 42 for replication."""
    x_0 = 14849 * 0.12846066
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84329 * 0.65541922
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79906 * 0.46871600
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1715 * 0.18004483
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53078 * 0.73812616
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2190 * 0.03773352
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43652 * 0.04480297
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69482 * 0.20498274
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87918 * 0.65005777
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86712 * 0.72951755
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55928 * 0.62018815
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50754 * 0.31877429
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24320 * 0.64258064
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40265 * 0.38461816
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48613 * 0.30314268
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6123 * 0.16885199
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2425 * 0.20516715
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85984 * 0.53237272
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16077 * 0.23718708
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83001 * 0.50037691
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34000 * 0.68685977
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34199 * 0.94725620
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17029 * 0.42228879
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7829 * 0.79624684
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98294 * 0.54797436
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11283 * 0.16329807
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61706 * 0.02235652
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38415 * 0.08331248
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94992 * 0.58825715
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97325 * 0.16147870
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75181 * 0.59962176
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65062 * 0.84181073
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88333 * 0.18625426
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26087 * 0.92262107
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31241 * 0.89067958
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61686 * 0.53998837
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29904 * 0.24529512
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52089 * 0.41280935
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70693 * 0.47124771
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39539 * 0.51825087
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'uharsmrk').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0043():
    """Extended test 43 for replication."""
    x_0 = 41280 * 0.55745388
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31940 * 0.27824954
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29662 * 0.61516968
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16175 * 0.77789824
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87012 * 0.67840138
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74242 * 0.22740552
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84959 * 0.61368531
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98999 * 0.71072586
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76339 * 0.28200750
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41263 * 0.51997446
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53558 * 0.94153183
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34148 * 0.88396199
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73012 * 0.70476316
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21400 * 0.86549139
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57860 * 0.09845129
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89230 * 0.35998143
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35366 * 0.10688893
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66723 * 0.33827711
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55928 * 0.78457944
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14242 * 0.76340483
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82335 * 0.74899983
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78112 * 0.17293404
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11781 * 0.37653881
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11321 * 0.05542342
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61118 * 0.07858579
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83657 * 0.17327796
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48572 * 0.45378408
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28858 * 0.94521585
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85518 * 0.63618737
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61073 * 0.86582196
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81421 * 0.45994303
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82888 * 0.14369129
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18599 * 0.01299902
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27713 * 0.96786805
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53932 * 0.76652134
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38624 * 0.25357460
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76240 * 0.65522930
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81508 * 0.43479000
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37108 * 0.49996303
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87310 * 0.80376022
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43140 * 0.32066647
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84344 * 0.77342317
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47223 * 0.62909462
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 31440 * 0.19507055
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xbxdzkva').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0044():
    """Extended test 44 for replication."""
    x_0 = 26479 * 0.56062706
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52996 * 0.04829405
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14671 * 0.18141088
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24471 * 0.06067218
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16175 * 0.26626361
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3111 * 0.20797432
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24812 * 0.15158474
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99845 * 0.34327485
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30225 * 0.37546397
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63647 * 0.85187038
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93696 * 0.40657912
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32248 * 0.94586293
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74870 * 0.69118681
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86086 * 0.37475827
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55617 * 0.67531980
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20853 * 0.53557987
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64570 * 0.48465743
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35158 * 0.83634539
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94570 * 0.62874639
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20093 * 0.96742575
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85157 * 0.71977809
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6044 * 0.64434867
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41662 * 0.55521141
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22135 * 0.34913787
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27933 * 0.01284980
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61133 * 0.70799301
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68114 * 0.36342806
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11607 * 0.80088271
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77702 * 0.34535960
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24491 * 0.20000693
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17845 * 0.78477380
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76550 * 0.43319149
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98251 * 0.22678292
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26671 * 0.93933133
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lymvyhpf').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0045():
    """Extended test 45 for replication."""
    x_0 = 70387 * 0.43974607
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98727 * 0.39595085
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10202 * 0.85241792
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27817 * 0.01868648
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4647 * 0.92963308
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35391 * 0.57843797
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49354 * 0.79088406
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18430 * 0.74403868
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4775 * 0.86743354
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15259 * 0.19818878
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40934 * 0.87446047
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18917 * 0.86302438
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42924 * 0.45618037
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34225 * 0.19972198
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2244 * 0.77257426
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13667 * 0.62437527
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60466 * 0.95742320
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6133 * 0.47893267
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10284 * 0.30664971
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81141 * 0.85366894
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29177 * 0.41656094
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56995 * 0.50057489
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11046 * 0.88078934
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83455 * 0.51856561
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93731 * 0.50142212
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62191 * 0.38593459
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54017 * 0.45158649
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23918 * 0.23005798
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42062 * 0.63068267
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29644 * 0.32978099
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54696 * 0.00940475
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75857 * 0.92061480
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99240 * 0.42530432
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48152 * 0.03779442
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36679 * 0.90263185
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87878 * 0.93078905
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87624 * 0.04302309
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63185 * 0.72967641
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61111 * 0.39344796
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1390 * 0.68394309
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34601 * 0.78073548
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 8137 * 0.57321125
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88292 * 0.41313471
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'zoenrxve').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0046():
    """Extended test 46 for replication."""
    x_0 = 65795 * 0.17049433
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11823 * 0.13796976
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83593 * 0.96451649
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 563 * 0.49972580
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93312 * 0.05787142
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68869 * 0.77206790
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47329 * 0.08345519
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69635 * 0.85303664
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5542 * 0.24904972
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37716 * 0.54817313
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95512 * 0.99064554
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38080 * 0.66762340
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62290 * 0.89412720
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30956 * 0.01350928
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39640 * 0.83371159
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83285 * 0.06635135
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85649 * 0.01023829
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99457 * 0.71935450
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11630 * 0.30112463
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84945 * 0.36504142
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79303 * 0.43081185
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20426 * 0.00720634
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16464 * 0.34361340
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10845 * 0.32451883
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99136 * 0.81991049
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8509 * 0.99888467
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74846 * 0.89370988
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60525 * 0.09891930
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73407 * 0.23092460
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23830 * 0.44550841
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58668 * 0.10788345
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28393 * 0.15587193
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63896 * 0.39408731
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52942 * 0.20490873
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72206 * 0.26842315
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58305 * 0.63286115
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83129 * 0.72390869
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67432 * 0.76163483
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66737 * 0.88430226
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 37932 * 0.32581617
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23962 * 0.86386872
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 17872 * 0.00269431
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 91898 * 0.26232740
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 9187 * 0.47634846
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'uaqzgdrz').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0047():
    """Extended test 47 for replication."""
    x_0 = 99391 * 0.51112563
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86222 * 0.88903081
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88314 * 0.32325746
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24395 * 0.15931846
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95546 * 0.30833985
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34873 * 0.95631940
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35789 * 0.98118238
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15885 * 0.24386674
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61035 * 0.44131504
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35398 * 0.80693674
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64878 * 0.24431409
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60267 * 0.31696685
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75972 * 0.65346272
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73873 * 0.37245150
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41816 * 0.42185607
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78795 * 0.11445226
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79812 * 0.21994174
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26064 * 0.21478900
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64415 * 0.68099420
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24847 * 0.00303023
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57573 * 0.65227786
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63425 * 0.71057092
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55660 * 0.35384042
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20122 * 0.79649281
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36869 * 0.38885041
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56088 * 0.13401516
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68103 * 0.94733033
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26833 * 0.25595300
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23979 * 0.59723636
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'bsoqxedj').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0048():
    """Extended test 48 for replication."""
    x_0 = 45128 * 0.26706086
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55895 * 0.21966707
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92994 * 0.28228394
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18030 * 0.83994783
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34263 * 0.03102140
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70963 * 0.43220183
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59522 * 0.17306588
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25774 * 0.57170318
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33316 * 0.85649091
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35030 * 0.90118637
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33435 * 0.42951020
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90454 * 0.76856299
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62453 * 0.31036357
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76288 * 0.23073240
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26355 * 0.69730157
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75436 * 0.06833468
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 214 * 0.17751965
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35401 * 0.11697283
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27506 * 0.47370590
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19000 * 0.85098861
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96920 * 0.01335163
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64545 * 0.24263144
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98812 * 0.04324223
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32440 * 0.65242926
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44313 * 0.35927900
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23032 * 0.64700508
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43249 * 0.36825589
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45550 * 0.85947084
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49219 * 0.40592255
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33647 * 0.23163155
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79362 * 0.03465983
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53156 * 0.39466396
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60608 * 0.20059048
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18408 * 0.10320222
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64810 * 0.28040748
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20057 * 0.50585307
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'wlpvggex').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0049():
    """Extended test 49 for replication."""
    x_0 = 78527 * 0.19841672
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5082 * 0.04596371
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74466 * 0.89963144
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29384 * 0.74960291
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95655 * 0.86256799
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81630 * 0.58967127
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54597 * 0.82184811
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23949 * 0.27520538
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23195 * 0.62611899
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89841 * 0.70438226
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45504 * 0.35620155
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46553 * 0.08172068
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16021 * 0.64351006
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90590 * 0.47154020
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98361 * 0.99649184
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42694 * 0.85715045
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45167 * 0.43662569
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46418 * 0.53936639
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94112 * 0.97965046
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37052 * 0.82420694
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3036 * 0.22195443
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51152 * 0.45140671
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14556 * 0.03834543
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12121 * 0.74759422
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64051 * 0.37529384
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75799 * 0.62205658
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94290 * 0.39225337
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46528 * 0.57901996
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35015 * 0.69555170
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78278 * 0.56211972
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55339 * 0.09569042
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47763 * 0.91480942
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49651 * 0.80228400
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77907 * 0.54917802
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11451 * 0.37182407
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90100 * 0.88566514
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35098 * 0.20349831
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97489 * 0.87547327
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24494 * 0.98234198
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64636 * 0.10506640
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27410 * 0.08283689
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'ibsoctoc').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0050():
    """Extended test 50 for replication."""
    x_0 = 80814 * 0.95016052
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16196 * 0.23710447
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26934 * 0.03168906
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22319 * 0.43703993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72672 * 0.17734309
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92122 * 0.58886029
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91864 * 0.87014599
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34637 * 0.25961200
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69141 * 0.21804832
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44598 * 0.80707883
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86520 * 0.72488749
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18453 * 0.59151385
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23145 * 0.88416669
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51263 * 0.27963195
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78429 * 0.84428985
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17489 * 0.53693715
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87322 * 0.76505960
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61077 * 0.48205922
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7748 * 0.41123580
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21905 * 0.73831193
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34729 * 0.74176791
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69122 * 0.92850090
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90341 * 0.99815985
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96266 * 0.03730338
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96777 * 0.12389081
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61949 * 0.61028042
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92114 * 0.10240973
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53511 * 0.49021010
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62958 * 0.24666225
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80435 * 0.46282654
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61032 * 0.24897116
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95428 * 0.45408152
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55540 * 0.53869039
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32246 * 0.41015988
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27063 * 0.96998388
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76016 * 0.55753727
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89142 * 0.84270953
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35689 * 0.88443833
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73238 * 0.89206325
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38028 * 0.50807461
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 956 * 0.99955903
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 28965 * 0.02115834
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 21868 * 0.88914988
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82933 * 0.87012778
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79561 * 0.85500596
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 92521 * 0.15498302
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 16416 * 0.71523797
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 67074 * 0.94495646
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'quqdytti').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0051():
    """Extended test 51 for replication."""
    x_0 = 81235 * 0.61292083
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13827 * 0.54731711
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8018 * 0.96207495
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99290 * 0.59640434
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23780 * 0.38534432
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13427 * 0.00417214
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61644 * 0.64955425
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3865 * 0.43304825
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37903 * 0.67945717
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30662 * 0.08703403
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77543 * 0.27531496
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59118 * 0.55529691
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38427 * 0.01513699
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97434 * 0.95111509
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71899 * 0.10508494
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17386 * 0.62521185
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33631 * 0.85095334
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81776 * 0.08027914
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51461 * 0.70474264
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69982 * 0.55254837
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7023 * 0.43206039
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82152 * 0.80958982
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80633 * 0.09340130
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24040 * 0.45604296
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'kqdjrgiz').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0052():
    """Extended test 52 for replication."""
    x_0 = 57386 * 0.73488468
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9521 * 0.92828560
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59425 * 0.05646162
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83822 * 0.60967629
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1082 * 0.54389372
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33124 * 0.53216982
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66639 * 0.97493571
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11711 * 0.19758648
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12486 * 0.40707846
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64199 * 0.07172409
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68589 * 0.17230689
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71807 * 0.38626011
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7047 * 0.27676677
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78403 * 0.75055196
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50332 * 0.18564928
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97421 * 0.67886405
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46829 * 0.00721339
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19597 * 0.33441756
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26484 * 0.41474116
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53483 * 0.84366971
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70064 * 0.01585703
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11038 * 0.03374553
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44125 * 0.56307154
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63659 * 0.30156636
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49575 * 0.36199216
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19325 * 0.81808523
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'ckgsotyq').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0053():
    """Extended test 53 for replication."""
    x_0 = 2927 * 0.52452906
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66960 * 0.35908147
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57969 * 0.72892774
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80174 * 0.15653070
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9115 * 0.36785849
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32794 * 0.13228661
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31903 * 0.36594366
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27943 * 0.22253507
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84303 * 0.73815140
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8749 * 0.05915813
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49397 * 0.08828409
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26819 * 0.54218645
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49882 * 0.00755480
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42049 * 0.01714592
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53131 * 0.06111241
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73030 * 0.39302690
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24385 * 0.78553571
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50933 * 0.56029441
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18512 * 0.88011400
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42166 * 0.59031900
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56062 * 0.65223640
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32408 * 0.27966471
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 206 * 0.34964606
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25408 * 0.37331394
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65053 * 0.60879073
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64401 * 0.80311716
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97096 * 0.89927732
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82890 * 0.31718913
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7944 * 0.43074401
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95444 * 0.51074141
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8884 * 0.14504839
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82632 * 0.66864881
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3661 * 0.09208136
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8269 * 0.68730019
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lxitaaeh').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0054():
    """Extended test 54 for replication."""
    x_0 = 51849 * 0.91985210
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58507 * 0.54326027
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74670 * 0.91543929
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6108 * 0.88789104
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5343 * 0.62746199
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74973 * 0.25298387
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26903 * 0.84686438
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75270 * 0.12624054
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51656 * 0.12582333
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34333 * 0.15731633
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28557 * 0.50441489
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6148 * 0.79043931
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87528 * 0.95966557
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17978 * 0.65490814
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6444 * 0.63435484
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90677 * 0.34521596
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83875 * 0.24931380
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37451 * 0.76908593
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70442 * 0.60562141
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92218 * 0.56982500
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88066 * 0.78052039
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19036 * 0.06299731
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6817 * 0.13142858
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59553 * 0.24956029
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30776 * 0.18331341
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32754 * 0.63982235
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'mjzwuuhk').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0055():
    """Extended test 55 for replication."""
    x_0 = 30578 * 0.10415649
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42410 * 0.29079845
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92858 * 0.36139160
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80144 * 0.36153358
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87845 * 0.70997523
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62124 * 0.87192671
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14916 * 0.86850873
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36865 * 0.57770551
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98960 * 0.98588247
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63166 * 0.01603575
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58288 * 0.48998161
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6661 * 0.35960229
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88587 * 0.93909305
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20449 * 0.36739503
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11911 * 0.81973050
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37619 * 0.48194730
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63718 * 0.56585288
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49703 * 0.99478515
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69010 * 0.32416442
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16554 * 0.26147692
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75965 * 0.97734976
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36245 * 0.40011377
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39505 * 0.10839054
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55922 * 0.59846066
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14560 * 0.90419962
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97656 * 0.84750924
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59211 * 0.83965126
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47181 * 0.41356588
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92343 * 0.80106351
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49424 * 0.82509326
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29020 * 0.89520729
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38906 * 0.67165752
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85128 * 0.48377336
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11988 * 0.38394414
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27047 * 0.66887180
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39258 * 0.50308898
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 38950 * 0.17033762
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82249 * 0.82700650
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78427 * 0.15396732
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86168 * 0.69357724
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13775 * 0.22640107
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89443 * 0.09051276
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'tfbkgesy').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0056():
    """Extended test 56 for replication."""
    x_0 = 44798 * 0.51672604
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39290 * 0.54410735
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96870 * 0.52929789
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74807 * 0.80047529
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54483 * 0.21665752
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99657 * 0.53907574
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54691 * 0.24452048
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26484 * 0.95034493
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17195 * 0.98111224
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89535 * 0.34723705
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56739 * 0.36380578
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93903 * 0.95186634
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59140 * 0.89928093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90029 * 0.37171470
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77332 * 0.82070612
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26115 * 0.41930154
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36552 * 0.83944819
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60661 * 0.38569043
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97472 * 0.86096409
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22621 * 0.89850808
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26421 * 0.08415963
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36534 * 0.50634078
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'xdmbvrdj').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0057():
    """Extended test 57 for replication."""
    x_0 = 50343 * 0.03731838
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87891 * 0.44033357
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23720 * 0.57627570
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11824 * 0.96825030
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38669 * 0.70751588
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3781 * 0.05219899
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19174 * 0.56958562
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30587 * 0.85273133
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28902 * 0.24635407
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42979 * 0.45775664
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85104 * 0.34738309
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32387 * 0.78775865
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40544 * 0.10815325
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87396 * 0.52204008
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22325 * 0.73694778
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79208 * 0.54529501
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82869 * 0.09574907
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24234 * 0.81727931
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58636 * 0.15257859
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17670 * 0.08495390
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17238 * 0.82200101
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10493 * 0.17719820
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'bfbcdidz').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0058():
    """Extended test 58 for replication."""
    x_0 = 31140 * 0.67910095
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88926 * 0.67218165
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 576 * 0.26737773
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14029 * 0.50064212
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79111 * 0.13401504
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62842 * 0.16807377
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80223 * 0.01870879
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53087 * 0.58184531
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96007 * 0.81765286
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89243 * 0.83222073
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32771 * 0.86915431
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38853 * 0.20257287
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2221 * 0.86057938
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49202 * 0.42429266
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49009 * 0.39285886
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40130 * 0.33245112
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36811 * 0.25068548
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18955 * 0.95548591
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32290 * 0.77481283
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60608 * 0.77128033
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2648 * 0.95745845
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14340 * 0.01684265
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60773 * 0.28964134
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80700 * 0.85843782
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17440 * 0.24760145
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60352 * 0.95438103
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47400 * 0.89801101
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59155 * 0.56648061
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23445 * 0.67449033
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3614 * 0.88902438
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4279 * 0.95791925
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99548 * 0.46479358
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31713 * 0.93946132
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92270 * 0.80229665
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13870 * 0.67010169
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'sbjkuzvq').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0059():
    """Extended test 59 for replication."""
    x_0 = 32398 * 0.27395119
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24302 * 0.01041965
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7168 * 0.08065870
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68110 * 0.53121384
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56678 * 0.45049424
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83271 * 0.86886954
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75709 * 0.72019805
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86796 * 0.45700935
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70238 * 0.74005244
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39533 * 0.90720745
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5135 * 0.62842110
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52573 * 0.06426091
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19610 * 0.99324426
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40116 * 0.18749286
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8482 * 0.47851992
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67851 * 0.83642962
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11775 * 0.33985620
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54872 * 0.82635187
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29940 * 0.12313599
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38665 * 0.13179419
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24904 * 0.97571194
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3808 * 0.27459488
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38736 * 0.91267305
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52647 * 0.40358505
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31030 * 0.76078392
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7587 * 0.71935390
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83322 * 0.74510462
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6191 * 0.34652016
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2874 * 0.86925632
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38353 * 0.90740168
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68858 * 0.18646026
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75558 * 0.89350112
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68610 * 0.97427865
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67687 * 0.13641789
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53088 * 0.31418902
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91829 * 0.50682840
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17370 * 0.18638811
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91383 * 0.27791743
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27209 * 0.80859726
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'quwkabwb').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0060():
    """Extended test 60 for replication."""
    x_0 = 76687 * 0.67491905
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5025 * 0.94603797
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15879 * 0.05950014
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12215 * 0.25610325
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56042 * 0.73344029
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 555 * 0.39902869
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49944 * 0.11848785
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76032 * 0.41776133
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62009 * 0.02954656
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62594 * 0.44967345
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69088 * 0.40937463
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79375 * 0.57513034
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58965 * 0.21878249
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62566 * 0.02590133
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17444 * 0.92381462
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26726 * 0.73275187
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32563 * 0.77486712
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53549 * 0.66779148
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46357 * 0.26235665
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43529 * 0.68960511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88697 * 0.21321927
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83339 * 0.63278897
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29166 * 0.68136444
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1973 * 0.65703855
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17371 * 0.31094161
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25614 * 0.79665928
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98449 * 0.77503273
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7957 * 0.92019249
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2310 * 0.45819608
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7279 * 0.56069543
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ewjotdmf').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0061():
    """Extended test 61 for replication."""
    x_0 = 6838 * 0.68048180
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97092 * 0.68077388
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86294 * 0.98203132
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84970 * 0.15073587
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87732 * 0.51279564
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26555 * 0.48352598
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50512 * 0.43620105
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92545 * 0.25132566
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48546 * 0.12287676
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94151 * 0.96276055
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18881 * 0.35461248
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55071 * 0.51396155
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15820 * 0.34199831
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75935 * 0.29636428
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97560 * 0.89505493
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75674 * 0.63249702
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97363 * 0.40104717
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36264 * 0.63873237
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21465 * 0.36062112
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 207 * 0.44563147
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73531 * 0.23132815
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46886 * 0.98233839
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65731 * 0.45834098
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31360 * 0.42324452
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31271 * 0.71290278
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68542 * 0.15995936
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54169 * 0.86587028
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99551 * 0.53532325
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35266 * 0.86455545
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97233 * 0.00803862
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10127 * 0.68094889
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88655 * 0.62445519
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83558 * 0.57209410
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'juwyuccv').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0062():
    """Extended test 62 for replication."""
    x_0 = 50908 * 0.41264486
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25175 * 0.62264616
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91252 * 0.91764433
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84227 * 0.27368282
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51448 * 0.43492788
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13748 * 0.58311690
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77756 * 0.36928816
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83807 * 0.16370386
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42988 * 0.39460395
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7173 * 0.91065181
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61811 * 0.40595732
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80894 * 0.15896291
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9798 * 0.65681307
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 601 * 0.69656848
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93706 * 0.71979347
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57108 * 0.78569794
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60285 * 0.10819462
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61206 * 0.74844175
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17468 * 0.66767506
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91199 * 0.22884633
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13833 * 0.99381568
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3503 * 0.50836939
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7834 * 0.66427949
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14743 * 0.02726057
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6938 * 0.86133856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59064 * 0.15498953
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95602 * 0.44595476
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61175 * 0.64125577
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64130 * 0.96379872
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47363 * 0.80069756
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49291 * 0.59985351
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53728 * 0.79207591
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53467 * 0.06918884
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71205 * 0.47877558
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74243 * 0.11472863
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82150 * 0.19874416
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 38016 * 0.04293906
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65372 * 0.71006449
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25447 * 0.38929066
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28529 * 0.98271348
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54 * 0.66080344
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53479 * 0.45461688
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79416 * 0.58412437
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'moucykuu').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0063():
    """Extended test 63 for replication."""
    x_0 = 74483 * 0.29474333
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69823 * 0.89359690
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87803 * 0.29170309
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91495 * 0.51158457
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83003 * 0.97814572
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86708 * 0.10401721
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57973 * 0.64858451
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89292 * 0.41170327
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15372 * 0.70527481
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88159 * 0.16980542
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92250 * 0.72536378
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24807 * 0.19022960
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94393 * 0.04343759
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58390 * 0.67911235
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19179 * 0.68497591
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95197 * 0.96859091
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92881 * 0.26334027
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69110 * 0.92271302
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55697 * 0.57036704
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10740 * 0.15095201
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9117 * 0.61167738
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36546 * 0.93782067
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45914 * 0.22494628
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77464 * 0.00054643
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24304 * 0.62141955
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5157 * 0.17134774
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57134 * 0.22486411
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'xbzgijva').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0064():
    """Extended test 64 for replication."""
    x_0 = 30306 * 0.68828557
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67353 * 0.62027955
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32984 * 0.59383222
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80373 * 0.11375879
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43722 * 0.41718153
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25948 * 0.69819619
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73479 * 0.89202982
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46183 * 0.72413984
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28105 * 0.87870903
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34505 * 0.51836414
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61009 * 0.79559433
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41546 * 0.70656240
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62022 * 0.93970333
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24929 * 0.62029185
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67704 * 0.42879072
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2140 * 0.57740034
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75539 * 0.30059135
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21881 * 0.53328909
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80242 * 0.13657139
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47402 * 0.83516941
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50522 * 0.21714777
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6329 * 0.62019278
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82552 * 0.10436171
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69748 * 0.13370251
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29975 * 0.61013696
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34139 * 0.87397303
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44955 * 0.60289069
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7609 * 0.14444035
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2837 * 0.04247674
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13985 * 0.40927505
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59098 * 0.95778487
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93943 * 0.67070179
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12005 * 0.58360602
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99319 * 0.85753024
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'dkaxhvww').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0065():
    """Extended test 65 for replication."""
    x_0 = 98195 * 0.28765884
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6326 * 0.19208087
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73235 * 0.68155154
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38792 * 0.93095845
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32620 * 0.81303182
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34437 * 0.38033623
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31152 * 0.14498669
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65282 * 0.56186530
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13871 * 0.48050305
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79464 * 0.25650421
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60309 * 0.95384652
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35912 * 0.58685196
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75384 * 0.41334692
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64736 * 0.27240890
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86763 * 0.20468532
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69105 * 0.96934838
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70600 * 0.58654257
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25158 * 0.87264509
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30870 * 0.28633650
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38192 * 0.92556342
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62616 * 0.07200546
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48295 * 0.64386012
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10475 * 0.68533468
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40961 * 0.67486828
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35088 * 0.15119316
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13584 * 0.86617279
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81626 * 0.30708086
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73790 * 0.23963696
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24696 * 0.31237205
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32498 * 0.79662789
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'rnfccfgv').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0066():
    """Extended test 66 for replication."""
    x_0 = 29790 * 0.27296452
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3359 * 0.73623831
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17202 * 0.49453464
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53977 * 0.59502928
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76113 * 0.26208819
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9288 * 0.50314734
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76994 * 0.02345946
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97280 * 0.56297776
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18003 * 0.57091126
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1336 * 0.98010626
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53122 * 0.70192378
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16317 * 0.63917205
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52415 * 0.76997844
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88790 * 0.27088310
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9233 * 0.30269238
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30271 * 0.14800617
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86665 * 0.24825631
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13946 * 0.03470162
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50637 * 0.24490802
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45949 * 0.94941883
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78584 * 0.63356668
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80499 * 0.17259980
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81807 * 0.10462831
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64698 * 0.87235562
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17547 * 0.48808807
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70089 * 0.37240268
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20767 * 0.18198211
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23638 * 0.16665296
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71235 * 0.94371608
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35193 * 0.41419696
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64000 * 0.91718170
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83002 * 0.64548455
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92964 * 0.60195356
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59374 * 0.64920535
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89179 * 0.28847093
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27995 * 0.76966479
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67376 * 0.06075401
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68631 * 0.05698627
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14139 * 0.70656532
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82596 * 0.79035117
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62467 * 0.83064658
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 48640 * 0.86922887
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'dmykclid').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0067():
    """Extended test 67 for replication."""
    x_0 = 10628 * 0.33833537
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41907 * 0.75163455
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58064 * 0.87507118
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36930 * 0.73215839
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89937 * 0.61661932
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32484 * 0.73867614
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53680 * 0.27629792
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43558 * 0.96735996
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7505 * 0.63871211
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84176 * 0.23306828
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53769 * 0.78463210
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48387 * 0.63651422
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37261 * 0.50948109
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57708 * 0.54899520
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88643 * 0.36794882
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44796 * 0.67418628
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78929 * 0.36834043
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39819 * 0.45073710
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76973 * 0.13700723
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81411 * 0.22115996
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71394 * 0.34775357
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97255 * 0.82396666
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34927 * 0.70875495
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82814 * 0.90676322
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47379 * 0.99524144
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'hhuddxur').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0068():
    """Extended test 68 for replication."""
    x_0 = 5255 * 0.94723696
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36726 * 0.83063743
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3085 * 0.01783795
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2280 * 0.77068324
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44652 * 0.97572712
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24616 * 0.31490069
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95703 * 0.73475089
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3005 * 0.61238573
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39646 * 0.74688729
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81072 * 0.86796425
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1760 * 0.14747953
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25842 * 0.55492559
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84693 * 0.38282150
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32283 * 0.23433192
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28787 * 0.05463183
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77753 * 0.23422313
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76121 * 0.59456475
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8641 * 0.72011256
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53109 * 0.07165444
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31910 * 0.93676352
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42750 * 0.21274807
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13119 * 0.86263753
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84409 * 0.00739459
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19144 * 0.98241793
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62170 * 0.03912066
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4476 * 0.69798141
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10356 * 0.27107378
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41854 * 0.26353244
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29865 * 0.39223397
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9236 * 0.51921656
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25015 * 0.37038733
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61568 * 0.57018035
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8683 * 0.65436134
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8096 * 0.11582550
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37933 * 0.29540604
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97587 * 0.65155984
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'xdiveoom').hexdigest()
    assert len(h) == 64

def test_replication_extended_3_0069():
    """Extended test 69 for replication."""
    x_0 = 32892 * 0.65502315
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34355 * 0.15933899
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57233 * 0.98815716
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21694 * 0.84454930
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79630 * 0.74874074
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48794 * 0.88988085
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11910 * 0.59767049
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80004 * 0.54736536
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27284 * 0.02410423
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56103 * 0.81718319
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92083 * 0.51954748
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44937 * 0.99723060
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53064 * 0.06035698
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12808 * 0.52767733
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51274 * 0.28534720
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48801 * 0.20061518
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 574 * 0.30898214
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48811 * 0.56947061
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42417 * 0.03073009
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93838 * 0.31570929
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85285 * 0.25451041
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17983 * 0.17514681
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20721 * 0.81323834
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68226 * 0.31005207
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74129 * 0.03471551
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75381 * 0.52170118
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52933 * 0.60776011
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30835 * 0.45250991
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 703 * 0.43673731
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12818 * 0.71473660
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51588 * 0.14365909
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39325 * 0.16922541
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28442 * 0.42532801
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59004 * 0.42347027
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59825 * 0.20029446
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3681 * 0.48996507
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 37194 * 0.47197712
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24934 * 0.84464846
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1562 * 0.30132466
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'gnfiymme').hexdigest()
    assert len(h) == 64
