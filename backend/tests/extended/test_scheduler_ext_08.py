"""Extended tests for scheduler suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_scheduler_extended_8_0000():
    """Extended test 0 for scheduler."""
    x_0 = 42636 * 0.24032318
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80128 * 0.84518053
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28213 * 0.13349338
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69643 * 0.28996616
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28032 * 0.77299630
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62162 * 0.31932715
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84848 * 0.31671974
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86657 * 0.66216147
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46145 * 0.67837108
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71338 * 0.69617180
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85432 * 0.13973171
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81637 * 0.72038668
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50082 * 0.96999739
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15557 * 0.31671211
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3692 * 0.67171636
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55291 * 0.59180044
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27825 * 0.48896286
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86006 * 0.28302982
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15468 * 0.80412201
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8206 * 0.52959511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87435 * 0.51384390
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53368 * 0.38213413
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12513 * 0.77093762
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88442 * 0.01544088
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53961 * 0.39386367
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81737 * 0.13576021
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11519 * 0.94407433
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38767 * 0.44256774
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56232 * 0.10508819
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'cujqclcu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0001():
    """Extended test 1 for scheduler."""
    x_0 = 63706 * 0.96318889
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17879 * 0.50710673
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5573 * 0.06505475
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43083 * 0.55656299
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66255 * 0.24363434
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99926 * 0.26350241
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26442 * 0.13028138
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6726 * 0.02922143
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27680 * 0.61568288
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78950 * 0.43787217
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90468 * 0.67277107
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98606 * 0.78926575
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 728 * 0.58961850
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64350 * 0.07767128
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63703 * 0.00989664
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79312 * 0.66960153
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81529 * 0.03682927
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16333 * 0.17243076
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50232 * 0.07913170
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9072 * 0.57386286
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21591 * 0.08519981
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3367 * 0.65773402
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65667 * 0.26758973
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1545 * 0.98000616
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54184 * 0.85934961
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71946 * 0.02715260
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22155 * 0.40931884
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47714 * 0.16671674
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31120 * 0.55851927
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82504 * 0.12592387
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73818 * 0.26843719
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47498 * 0.11405856
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50570 * 0.34543815
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9681 * 0.64696033
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52005 * 0.09654416
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94743 * 0.61749557
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5402 * 0.74394102
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69161 * 0.63351518
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'lfkhinfy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0002():
    """Extended test 2 for scheduler."""
    x_0 = 96450 * 0.19392449
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4508 * 0.91308103
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10390 * 0.92748980
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42759 * 0.28555810
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17882 * 0.84880213
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88383 * 0.27343752
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66149 * 0.78803440
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83782 * 0.22884688
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64038 * 0.41011770
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86427 * 0.74830621
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24170 * 0.39100366
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62141 * 0.10330287
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65542 * 0.44663011
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94099 * 0.42813509
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3812 * 0.13249905
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95756 * 0.23573277
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67952 * 0.17204092
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75561 * 0.64135187
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18338 * 0.95974538
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95958 * 0.73395003
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63769 * 0.96307552
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16770 * 0.50775981
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63 * 0.75057137
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44248 * 0.49022676
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65462 * 0.00094061
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29381 * 0.61940613
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50030 * 0.61943403
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6131 * 0.81006593
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91042 * 0.44036887
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22243 * 0.59798784
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50447 * 0.26177872
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'jzxbtwst').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0003():
    """Extended test 3 for scheduler."""
    x_0 = 36156 * 0.05574660
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8388 * 0.29732388
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62904 * 0.58388759
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20599 * 0.17809534
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13931 * 0.34026340
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35696 * 0.26595208
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93758 * 0.89017406
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82374 * 0.19085515
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58376 * 0.35424468
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9893 * 0.38527633
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90466 * 0.88754781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42019 * 0.20232193
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60643 * 0.37081331
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70271 * 0.94122243
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49888 * 0.80281996
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47959 * 0.64563180
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56226 * 0.91164347
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72585 * 0.73851796
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38830 * 0.68090574
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30436 * 0.44361907
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23207 * 0.74138235
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89206 * 0.73922158
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83360 * 0.95320337
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 751 * 0.97072918
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9612 * 0.43408211
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75595 * 0.07081423
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78634 * 0.40928009
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23829 * 0.56127027
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27785 * 0.34464226
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91058 * 0.60767857
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34462 * 0.16360917
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4648 * 0.57257416
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90167 * 0.38577051
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15821 * 0.82259331
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98119 * 0.09786394
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46038 * 0.59153125
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91650 * 0.92960901
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90595 * 0.45983614
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24948 * 0.85967804
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'feofadrh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0004():
    """Extended test 4 for scheduler."""
    x_0 = 67 * 0.98205475
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26442 * 0.65850262
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75063 * 0.70637336
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86867 * 0.34345993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17388 * 0.85289275
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46473 * 0.90389859
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45515 * 0.13842366
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 699 * 0.13106586
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92942 * 0.09967368
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25271 * 0.64330789
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35119 * 0.23835980
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79110 * 0.33253527
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26896 * 0.33533071
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81213 * 0.57227223
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68596 * 0.09971126
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39626 * 0.67200320
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55663 * 0.75808126
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45031 * 0.65837614
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88039 * 0.90859957
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74522 * 0.72814788
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64096 * 0.02622500
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32873 * 0.75410392
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42120 * 0.08709350
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46745 * 0.35394559
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55720 * 0.37737891
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21104 * 0.31146597
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72495 * 0.19186490
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2823 * 0.68519293
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15170 * 0.10665470
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61877 * 0.95934374
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77065 * 0.21212032
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43087 * 0.95058647
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79299 * 0.30969717
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43604 * 0.99253803
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52278 * 0.54730986
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21382 * 0.75320156
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97552 * 0.64640152
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40656 * 0.08761172
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42306 * 0.46628917
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94135 * 0.79701383
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42404 * 0.33816766
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4331 * 0.17122929
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'znzffvxo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0005():
    """Extended test 5 for scheduler."""
    x_0 = 78330 * 0.41849196
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52757 * 0.62067064
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62546 * 0.89111884
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77286 * 0.86654135
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98780 * 0.85524851
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9977 * 0.24509488
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99514 * 0.62180611
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67143 * 0.93612069
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19905 * 0.17293736
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43986 * 0.20482747
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7796 * 0.46208671
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44100 * 0.21278203
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50772 * 0.71711727
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94934 * 0.67907332
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20019 * 0.88006852
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62822 * 0.69747335
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26471 * 0.34179982
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98832 * 0.98991206
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81617 * 0.72968127
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17328 * 0.50866726
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33953 * 0.70507090
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84958 * 0.83385623
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45211 * 0.42352561
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67820 * 0.92955823
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6519 * 0.40490731
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 412 * 0.37000847
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30691 * 0.27913705
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7505 * 0.23811525
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2476 * 0.66379005
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 788 * 0.30496812
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96935 * 0.97557372
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71870 * 0.36040579
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8990 * 0.60990568
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46514 * 0.35546670
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83385 * 0.03488321
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15619 * 0.26040653
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78305 * 0.25013506
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80820 * 0.29188934
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2101 * 0.25870260
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80406 * 0.55229823
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 57555 * 0.84492897
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 382 * 0.18493274
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'rgjimssi').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0006():
    """Extended test 6 for scheduler."""
    x_0 = 16851 * 0.33200904
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58885 * 0.35527035
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31105 * 0.59380553
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85453 * 0.49322837
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9329 * 0.18980136
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44677 * 0.92044762
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5436 * 0.33177197
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70215 * 0.44815189
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56392 * 0.95339448
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48339 * 0.62762681
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95755 * 0.34208816
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37046 * 0.44097463
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39806 * 0.14979404
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35375 * 0.37631685
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21472 * 0.96798282
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18166 * 0.45027973
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47152 * 0.38999745
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33464 * 0.90615441
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35632 * 0.71472197
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46328 * 0.44664692
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47926 * 0.76689922
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11358 * 0.85888905
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71055 * 0.03443332
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35375 * 0.50906267
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27645 * 0.22175534
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28787 * 0.19911070
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85351 * 0.76557810
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51366 * 0.15291230
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66717 * 0.67676924
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86866 * 0.92205511
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83673 * 0.44089828
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30557 * 0.61626170
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15405 * 0.14297582
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49985 * 0.30309525
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'aczmuynd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0007():
    """Extended test 7 for scheduler."""
    x_0 = 55230 * 0.25722204
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79567 * 0.80856026
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59965 * 0.75799521
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63341 * 0.36041767
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44847 * 0.99669316
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20763 * 0.57609351
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96377 * 0.03091382
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74777 * 0.11598694
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95427 * 0.08312869
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88460 * 0.32642904
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75950 * 0.72627046
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24692 * 0.88467078
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87492 * 0.59740428
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51081 * 0.05469218
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8132 * 0.51622326
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56886 * 0.20094479
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31726 * 0.58051045
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57755 * 0.41402351
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4400 * 0.77831902
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24584 * 0.50184460
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41891 * 0.14859965
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63286 * 0.60427764
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96315 * 0.68784064
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6616 * 0.88872694
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42445 * 0.28246551
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5250 * 0.79307301
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9466 * 0.94415273
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4332 * 0.35533697
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47342 * 0.20443679
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68624 * 0.77386424
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55728 * 0.07256834
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47954 * 0.76267083
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80522 * 0.91508372
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ixcsoxkk').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0008():
    """Extended test 8 for scheduler."""
    x_0 = 43200 * 0.19311131
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56999 * 0.50151908
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59985 * 0.26269518
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93999 * 0.19302962
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10315 * 0.83328648
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58974 * 0.21653213
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42192 * 0.55340139
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53408 * 0.75508135
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50350 * 0.22134609
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28743 * 0.14531125
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75767 * 0.95682094
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48546 * 0.56157077
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24967 * 0.13646967
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48451 * 0.93096457
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87790 * 0.16985030
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40427 * 0.70811179
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34512 * 0.11415654
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97782 * 0.24325429
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64949 * 0.46836974
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11234 * 0.32939866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3108 * 0.07702968
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29979 * 0.06001856
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67998 * 0.75906564
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29355 * 0.14287918
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93339 * 0.75653248
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31167 * 0.49450502
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61311 * 0.05158083
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21730 * 0.06291167
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70360 * 0.72894788
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71334 * 0.67220496
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31592 * 0.18165301
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65600 * 0.96436510
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47919 * 0.07933092
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36054 * 0.00243091
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78506 * 0.67652009
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22022 * 0.76992156
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73501 * 0.21619979
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65630 * 0.56526403
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76247 * 0.97390461
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45752 * 0.46477613
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ignfrlmh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0009():
    """Extended test 9 for scheduler."""
    x_0 = 2344 * 0.37746962
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97020 * 0.51176151
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15179 * 0.88494224
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3904 * 0.94708011
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35234 * 0.14891229
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7892 * 0.98636251
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73384 * 0.00108477
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6288 * 0.09497086
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87203 * 0.22023354
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67618 * 0.73626050
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27928 * 0.52665044
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52434 * 0.13216736
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49144 * 0.41804611
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68421 * 0.75721672
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97032 * 0.53135754
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33401 * 0.31046497
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48117 * 0.82487249
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13663 * 0.45361207
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93942 * 0.61231515
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10581 * 0.61191263
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91877 * 0.94360167
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12881 * 0.07684452
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37938 * 0.73432332
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1121 * 0.67747412
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59016 * 0.23949165
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28329 * 0.63071992
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49578 * 0.38375640
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35522 * 0.38302150
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35188 * 0.89508264
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70092 * 0.94073482
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70914 * 0.75661020
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17640 * 0.25857427
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68843 * 0.97963601
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78394 * 0.13640033
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'pevhcvbx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0010():
    """Extended test 10 for scheduler."""
    x_0 = 32262 * 0.84341219
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48370 * 0.49539788
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92790 * 0.64854018
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48001 * 0.00714692
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54978 * 0.64041417
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34242 * 0.89729598
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63575 * 0.89839618
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81475 * 0.07722864
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46548 * 0.91655914
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78144 * 0.15908503
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92862 * 0.05564653
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8342 * 0.19480285
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26681 * 0.15585710
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14864 * 0.30032798
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48552 * 0.17801835
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49183 * 0.99391059
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2355 * 0.89927340
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19136 * 0.59559205
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5632 * 0.87498950
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2192 * 0.64382027
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84762 * 0.50621501
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92790 * 0.70251779
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91265 * 0.91449736
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15060 * 0.11378824
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49354 * 0.00854298
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96466 * 0.48191440
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39974 * 0.81748579
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21584 * 0.06192199
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39516 * 0.68682910
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55633 * 0.04582208
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86324 * 0.83217975
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71822 * 0.22564966
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75268 * 0.14427278
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39359 * 0.36132579
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84749 * 0.18514199
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81395 * 0.83249541
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7168 * 0.94922322
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83073 * 0.90739561
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'lukrcdba').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0011():
    """Extended test 11 for scheduler."""
    x_0 = 1763 * 0.22730793
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32319 * 0.52793091
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82063 * 0.38088673
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56459 * 0.44481013
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 470 * 0.64711530
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55932 * 0.45605377
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99935 * 0.94171112
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82571 * 0.48683307
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10539 * 0.75713075
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28754 * 0.34990524
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68149 * 0.28103751
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52067 * 0.31044488
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81484 * 0.09913924
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19220 * 0.57462461
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65277 * 0.30595131
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48815 * 0.43978269
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66379 * 0.13349993
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57311 * 0.88408236
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28604 * 0.03245708
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86756 * 0.42146680
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45731 * 0.05598924
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71127 * 0.81562923
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71370 * 0.00279240
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39699 * 0.02196518
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75759 * 0.36796716
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68175 * 0.13935146
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66606 * 0.22618441
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15846 * 0.20006908
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59551 * 0.13504845
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89012 * 0.21227619
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82453 * 0.56333967
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55290 * 0.80465115
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15983 * 0.94547272
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67132 * 0.45266729
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12134 * 0.24490024
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36261 * 0.78176078
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65249 * 0.17967935
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38151 * 0.01272622
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'yqmciefn').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0012():
    """Extended test 12 for scheduler."""
    x_0 = 8518 * 0.36325966
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70738 * 0.91446206
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63690 * 0.87142235
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53807 * 0.38043195
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1860 * 0.97786655
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32068 * 0.76949202
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87330 * 0.85584346
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94669 * 0.13690290
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18676 * 0.00244211
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77855 * 0.03495184
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67354 * 0.52407673
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34286 * 0.57555543
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76657 * 0.73986261
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73095 * 0.03842087
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81746 * 0.06546453
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4634 * 0.33900803
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97437 * 0.86763373
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54996 * 0.72660427
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29813 * 0.99090962
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40270 * 0.86774184
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6158 * 0.91149100
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97636 * 0.70696989
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68740 * 0.42007009
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19640 * 0.40880364
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66635 * 0.93459949
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53350 * 0.19419146
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'kryhzqpg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0013():
    """Extended test 13 for scheduler."""
    x_0 = 30379 * 0.64319807
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35487 * 0.86924564
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19138 * 0.33710641
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57507 * 0.71104868
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18648 * 0.67181966
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8388 * 0.20685357
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56861 * 0.97809372
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16936 * 0.65674260
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68048 * 0.61500145
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97956 * 0.14938223
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36017 * 0.38588785
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23870 * 0.66678061
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54185 * 0.80649766
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91184 * 0.30629900
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35944 * 0.13138864
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19419 * 0.98884449
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91181 * 0.54451803
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17251 * 0.79863841
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99438 * 0.84432586
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18055 * 0.30851461
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50086 * 0.01676853
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90159 * 0.71179045
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32379 * 0.89901462
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63826 * 0.66524118
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96015 * 0.05574077
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 279 * 0.95396929
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72112 * 0.31465827
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29148 * 0.95351507
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91383 * 0.20784016
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8561 * 0.51977825
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31641 * 0.83084980
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65536 * 0.58896331
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47194 * 0.27282605
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98890 * 0.82137862
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83779 * 0.07823456
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78510 * 0.98009608
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51136 * 0.68025592
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70875 * 0.53144930
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1839 * 0.70393628
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44011 * 0.86460937
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34501 * 0.95494333
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'dsunlrug').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0014():
    """Extended test 14 for scheduler."""
    x_0 = 34786 * 0.80201967
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14448 * 0.94341898
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58038 * 0.38443684
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98506 * 0.40953366
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88936 * 0.87911166
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8883 * 0.16647130
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83190 * 0.67275238
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25559 * 0.05792730
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23811 * 0.51341084
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17732 * 0.15084589
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28685 * 0.47989606
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91962 * 0.66604797
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45397 * 0.54133301
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90705 * 0.90924842
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14851 * 0.76701077
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65927 * 0.28686374
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83003 * 0.77002957
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47647 * 0.51386046
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93382 * 0.60784389
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29909 * 0.15351358
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14526 * 0.63900775
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59598 * 0.58556813
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77712 * 0.27169826
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14182 * 0.94844770
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21461 * 0.67682484
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51187 * 0.13805684
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34895 * 0.93377752
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83985 * 0.12715177
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77875 * 0.50895842
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87126 * 0.12521768
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83130 * 0.62038632
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31341 * 0.00627543
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81989 * 0.71805601
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3200 * 0.97802502
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53213 * 0.48699930
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10162 * 0.17102870
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71396 * 0.25240970
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5340 * 0.25059772
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28748 * 0.11761247
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44631 * 0.61911327
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 67985 * 0.60286100
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36882 * 0.84721744
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65964 * 0.77707983
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'hpqincbl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0015():
    """Extended test 15 for scheduler."""
    x_0 = 18715 * 0.32085664
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25527 * 0.71327957
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97576 * 0.13047860
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26622 * 0.05901937
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90472 * 0.53592593
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93510 * 0.17254812
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91356 * 0.74108389
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 167 * 0.29152900
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88525 * 0.95597408
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80155 * 0.58299407
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46036 * 0.03686285
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73448 * 0.88835609
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49984 * 0.32188185
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94450 * 0.60386250
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28983 * 0.65857808
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11327 * 0.34374514
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84464 * 0.01980144
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43204 * 0.67270345
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75885 * 0.48065703
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73700 * 0.46101225
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4034 * 0.38553646
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92193 * 0.99032259
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66397 * 0.79096411
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89821 * 0.55499347
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91454 * 0.33864646
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68367 * 0.70931804
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19825 * 0.08165991
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6380 * 0.87209781
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16506 * 0.05903619
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97107 * 0.19776380
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46394 * 0.23423782
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47802 * 0.30075221
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69170 * 0.29664896
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15305 * 0.60096714
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14791 * 0.79880805
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67014 * 0.53351885
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69003 * 0.64807570
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 51176 * 0.02880741
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29066 * 0.38366313
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 61914 * 0.03441847
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 96395 * 0.34175576
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72741 * 0.40269925
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10766 * 0.02690551
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 10821 * 0.46747766
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92062 * 0.56302834
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 22835 * 0.44054319
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'ataqgzbi').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0016():
    """Extended test 16 for scheduler."""
    x_0 = 96531 * 0.48888361
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73468 * 0.09655398
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53032 * 0.04681696
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22452 * 0.74780529
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66512 * 0.99139351
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45109 * 0.97143821
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79622 * 0.98415873
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90071 * 0.21394145
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2508 * 0.15462738
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47842 * 0.92001653
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8302 * 0.65776560
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42326 * 0.75774751
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76803 * 0.37286441
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72433 * 0.19079526
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30900 * 0.29838073
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29935 * 0.28942369
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14422 * 0.45065167
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46762 * 0.37915989
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53597 * 0.66273216
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84364 * 0.26955400
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98605 * 0.34194594
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20674 * 0.71557671
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60175 * 0.86330558
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71582 * 0.89625959
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16329 * 0.98713081
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55734 * 0.43597119
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38484 * 0.16539886
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25863 * 0.32112152
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33267 * 0.49775450
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78849 * 0.24015099
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26249 * 0.70616845
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24600 * 0.39688965
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54302 * 0.24747989
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26604 * 0.86803813
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93476 * 0.95052436
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74052 * 0.11465650
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98862 * 0.85711965
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90497 * 0.06333683
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43714 * 0.69826091
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30344 * 0.24083140
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 97166 * 0.88023240
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3560 * 0.47967844
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 31685 * 0.72020497
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61300 * 0.05397031
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 56707 * 0.58606090
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 88142 * 0.40843069
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'aaqubteu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0017():
    """Extended test 17 for scheduler."""
    x_0 = 74149 * 0.78987732
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52041 * 0.41947678
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91656 * 0.74442417
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81876 * 0.28842280
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7994 * 0.59828894
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15267 * 0.51181056
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10820 * 0.19448183
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37034 * 0.39612894
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82340 * 0.42219650
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36516 * 0.71833131
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35629 * 0.95258029
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18138 * 0.77331712
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40054 * 0.46061228
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34050 * 0.22028661
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79458 * 0.94269831
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56027 * 0.04617849
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7527 * 0.89158623
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90005 * 0.87492764
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54273 * 0.65137810
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84816 * 0.05394156
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5744 * 0.04615881
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8479 * 0.58975099
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95571 * 0.00791614
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2709 * 0.58290636
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85257 * 0.29219554
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84145 * 0.92249068
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45178 * 0.19978697
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73736 * 0.91567790
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7542 * 0.66548541
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44264 * 0.03317354
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40075 * 0.62541546
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83993 * 0.70190300
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15131 * 0.67958241
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29498 * 0.59172629
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39161 * 0.12725916
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36807 * 0.89702697
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33534 * 0.62634125
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98106 * 0.00119609
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34116 * 0.54101470
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92477 * 0.04693494
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49921 * 0.76807171
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96040 * 0.41333715
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 89107 * 0.94806885
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'yevklvvf').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0018():
    """Extended test 18 for scheduler."""
    x_0 = 66996 * 0.47410119
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61308 * 0.66406685
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5708 * 0.90664709
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36622 * 0.21038636
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68955 * 0.81584463
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83819 * 0.69024276
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27754 * 0.02452490
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98573 * 0.24481808
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84522 * 0.86203225
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18341 * 0.05394446
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63711 * 0.68911877
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9157 * 0.40140734
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10223 * 0.34870624
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41908 * 0.18264310
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81243 * 0.62824063
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63362 * 0.75970142
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76987 * 0.78722200
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35329 * 0.22368059
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39670 * 0.16186779
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41194 * 0.44607013
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'iqzmmeze').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0019():
    """Extended test 19 for scheduler."""
    x_0 = 94349 * 0.21273122
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95523 * 0.95948902
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29525 * 0.20414982
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65015 * 0.18893913
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49802 * 0.02380480
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81145 * 0.27459638
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25486 * 0.40463967
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68353 * 0.92422644
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91540 * 0.51461377
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54867 * 0.57238835
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52553 * 0.59226270
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48193 * 0.12269315
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96578 * 0.46424688
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14508 * 0.81001775
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98254 * 0.84071538
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77803 * 0.24499931
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50603 * 0.67470915
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61592 * 0.52283417
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54289 * 0.83037471
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28034 * 0.24768751
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50926 * 0.29602802
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96349 * 0.91607894
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57443 * 0.41256903
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18658 * 0.91678852
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56182 * 0.97081058
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29599 * 0.53262777
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'gsqavfpg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0020():
    """Extended test 20 for scheduler."""
    x_0 = 71528 * 0.25700879
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2321 * 0.01664692
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11967 * 0.63140899
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32028 * 0.84862398
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57194 * 0.98400533
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45458 * 0.22442163
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74087 * 0.20234777
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84391 * 0.65988186
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59174 * 0.83415592
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11258 * 0.31385281
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8209 * 0.60537717
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21624 * 0.81855347
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33259 * 0.04742599
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12293 * 0.31656792
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17484 * 0.81050651
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50977 * 0.98762512
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29344 * 0.83016929
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22140 * 0.70751225
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18538 * 0.44625707
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1264 * 0.91754629
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81634 * 0.72609064
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50713 * 0.71791340
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27893 * 0.51701116
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98030 * 0.87436021
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52052 * 0.60830532
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7315 * 0.57635850
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3113 * 0.59170295
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14577 * 0.51383624
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67577 * 0.89225670
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79307 * 0.34473224
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95791 * 0.47982722
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67160 * 0.87278587
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73944 * 0.39957095
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2986 * 0.57221210
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28215 * 0.45896396
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36740 * 0.35699004
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58000 * 0.56631068
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95781 * 0.61433189
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72057 * 0.80402315
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'vuzcdzdy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0021():
    """Extended test 21 for scheduler."""
    x_0 = 3374 * 0.20291634
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68265 * 0.86754121
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64650 * 0.59396224
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30788 * 0.87530619
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89349 * 0.69392090
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34329 * 0.73018775
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48126 * 0.46773092
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18577 * 0.68912328
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14913 * 0.71947789
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57792 * 0.08943470
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49446 * 0.22640968
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57454 * 0.43417165
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92361 * 0.67784172
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83097 * 0.93904103
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22004 * 0.79837101
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7385 * 0.38347939
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75536 * 0.47519646
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3458 * 0.32459365
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80713 * 0.32463810
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23862 * 0.10473580
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7305 * 0.63933280
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69174 * 0.11462384
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85625 * 0.14268428
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29962 * 0.03084733
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50196 * 0.55570958
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62420 * 0.74297004
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32490 * 0.84166016
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4451 * 0.53095060
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5522 * 0.84057536
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71242 * 0.74234681
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97074 * 0.69516293
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41088 * 0.35298282
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29950 * 0.34846482
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56319 * 0.43275094
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11394 * 0.84238301
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12789 * 0.18721674
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18310 * 0.85963452
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80108 * 0.83813948
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28574 * 0.53676727
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52990 * 0.19670721
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69677 * 0.23055681
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58114 * 0.20205932
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 8711 * 0.68952753
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 29680 * 0.83139364
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79023 * 0.03714537
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 54097 * 0.36254749
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 86513 * 0.05360345
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 98836 * 0.82466848
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ldbqdabr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0022():
    """Extended test 22 for scheduler."""
    x_0 = 25635 * 0.22098793
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39917 * 0.39503535
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89089 * 0.08826165
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31972 * 0.23083771
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88432 * 0.60723220
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23780 * 0.66761001
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35495 * 0.52016153
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94223 * 0.81988597
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13633 * 0.27302126
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91399 * 0.28275688
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41657 * 0.42615697
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25118 * 0.41968507
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37187 * 0.25205129
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20959 * 0.59145061
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73189 * 0.24848460
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54001 * 0.74490105
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90073 * 0.43965899
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11050 * 0.36653206
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64937 * 0.45118576
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33889 * 0.02404749
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16027 * 0.19414091
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97595 * 0.83043700
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94787 * 0.26337250
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82958 * 0.28957287
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93256 * 0.09414058
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62131 * 0.86683331
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96861 * 0.76370193
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46986 * 0.91176700
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55365 * 0.32376252
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85618 * 0.46596677
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77708 * 0.71083833
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77205 * 0.07439553
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58320 * 0.79005197
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85954 * 0.65208782
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99638 * 0.32432060
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62157 * 0.11403883
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31418 * 0.61351199
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16109 * 0.46786726
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5072 * 0.48674671
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87170 * 0.49900576
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8100 * 0.26280872
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5906 * 0.41129071
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 43830 * 0.79565061
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27706 * 0.68522228
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 19500 * 0.96825264
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 69054 * 0.76108784
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 21803 * 0.70393301
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 66548 * 0.72898250
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 96611 * 0.40926453
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 55110 * 0.62035619
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'rmjoxsqo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0023():
    """Extended test 23 for scheduler."""
    x_0 = 81389 * 0.62309746
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96929 * 0.28861448
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81406 * 0.73211182
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18513 * 0.79988925
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8263 * 0.17071108
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59814 * 0.01848260
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74719 * 0.15396158
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88307 * 0.69091086
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3475 * 0.16692327
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50248 * 0.82897164
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27174 * 0.56639846
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31812 * 0.02352820
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58755 * 0.04801761
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42682 * 0.61947227
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32753 * 0.53823668
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90820 * 0.51690860
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40051 * 0.78483595
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30225 * 0.22524076
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30583 * 0.63321894
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71280 * 0.22054145
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4376 * 0.77375995
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47572 * 0.40254669
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98600 * 0.85585594
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61318 * 0.47501026
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84395 * 0.88486661
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25225 * 0.58115745
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25695 * 0.03741031
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3873 * 0.89259023
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10976 * 0.10505373
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31121 * 0.60879742
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33091 * 0.34344610
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25551 * 0.56637826
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33112 * 0.22662822
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45956 * 0.87802257
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lqvuzxks').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0024():
    """Extended test 24 for scheduler."""
    x_0 = 27208 * 0.57991112
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52714 * 0.36289250
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88774 * 0.14765652
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60880 * 0.52387945
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84474 * 0.19363058
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7268 * 0.95422574
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44490 * 0.88102564
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35190 * 0.11078388
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58414 * 0.90898259
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72631 * 0.51484219
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70295 * 0.21428751
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6589 * 0.21509133
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79476 * 0.19674026
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4732 * 0.62745633
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45605 * 0.17323189
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71306 * 0.08404484
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58257 * 0.58703442
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71903 * 0.45771701
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59939 * 0.52266751
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96018 * 0.28388033
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60301 * 0.70043871
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79082 * 0.23304015
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66664 * 0.53328473
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70312 * 0.28148053
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59730 * 0.32976172
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63328 * 0.25112715
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48933 * 0.61758235
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31036 * 0.33929205
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57277 * 0.49652303
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13489 * 0.75295976
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38593 * 0.62818126
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41883 * 0.58822472
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64868 * 0.87822940
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87437 * 0.27323461
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'ojhwkudr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0025():
    """Extended test 25 for scheduler."""
    x_0 = 32412 * 0.15740351
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45468 * 0.15414261
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33766 * 0.14483199
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73911 * 0.59310283
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86033 * 0.52452876
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50817 * 0.37540834
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69418 * 0.27909219
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66623 * 0.65051176
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76819 * 0.06464135
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26111 * 0.82552912
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3385 * 0.31658919
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13856 * 0.17547466
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96695 * 0.98657527
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94420 * 0.06184648
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67404 * 0.50512167
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42567 * 0.17423323
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3536 * 0.84826967
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25164 * 0.69437309
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74215 * 0.15604051
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19025 * 0.48745593
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9784 * 0.94808678
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22714 * 0.03216386
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17780 * 0.57028933
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60805 * 0.02491388
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22947 * 0.97674797
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83045 * 0.06277071
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34238 * 0.67126971
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93284 * 0.08357155
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29859 * 0.68140681
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77331 * 0.56467797
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40173 * 0.34681906
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73650 * 0.39191095
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65213 * 0.04460000
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92574 * 0.20905764
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'tpuveyll').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0026():
    """Extended test 26 for scheduler."""
    x_0 = 46456 * 0.97807840
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86238 * 0.19148022
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90763 * 0.10311120
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96370 * 0.42793404
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93322 * 0.07546290
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81604 * 0.74379083
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22891 * 0.88228759
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74763 * 0.07846021
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44487 * 0.07997074
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36553 * 0.73224580
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7939 * 0.18984452
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7696 * 0.57428878
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36716 * 0.80477784
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11603 * 0.40209289
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75617 * 0.28045633
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48053 * 0.42962296
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87987 * 0.56314893
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66475 * 0.11160908
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38223 * 0.95981407
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24790 * 0.56080405
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86708 * 0.06746837
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 165 * 0.39127402
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6119 * 0.49872296
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54646 * 0.07000274
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30879 * 0.37502413
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24148 * 0.79915772
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46969 * 0.11418926
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53679 * 0.23787739
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96246 * 0.53052073
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64695 * 0.71778330
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5895 * 0.59120526
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32621 * 0.77626562
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60859 * 0.44205084
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35356 * 0.48657685
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12739 * 0.34498725
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75351 * 0.89785011
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3503 * 0.03351610
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18034 * 0.21878618
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4075 * 0.60568964
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7998 * 0.29509287
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89913 * 0.75139491
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 94605 * 0.40453041
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'mrzwefvv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0027():
    """Extended test 27 for scheduler."""
    x_0 = 75115 * 0.53252730
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13456 * 0.61529668
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35926 * 0.23611700
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78828 * 0.82643178
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79640 * 0.75813874
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94486 * 0.04662952
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62163 * 0.45991815
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60063 * 0.58279177
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74995 * 0.49236147
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12165 * 0.60468760
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59064 * 0.30246798
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73936 * 0.81240722
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18952 * 0.34952327
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15287 * 0.48367099
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54126 * 0.42865375
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95480 * 0.58368647
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60749 * 0.25045401
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76407 * 0.39018420
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65820 * 0.28460518
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40394 * 0.70905942
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35932 * 0.61939161
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20241 * 0.15729511
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5492 * 0.81979852
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51955 * 0.61768254
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34184 * 0.66040541
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65703 * 0.25125198
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9453 * 0.08675269
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57362 * 0.83245845
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82490 * 0.00566104
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9630 * 0.84866113
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20626 * 0.42086989
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86840 * 0.58213322
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78988 * 0.23590785
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56779 * 0.58816733
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27196 * 0.05638667
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83493 * 0.10405052
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80634 * 0.08469731
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3609 * 0.10091917
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ebgbwcab').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0028():
    """Extended test 28 for scheduler."""
    x_0 = 40906 * 0.44035250
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72362 * 0.53596796
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46484 * 0.77875439
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57577 * 0.56028898
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7938 * 0.45018565
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34201 * 0.27648253
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84203 * 0.22970484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96042 * 0.32492281
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34100 * 0.43996742
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98401 * 0.28514296
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27178 * 0.12342300
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13443 * 0.20404549
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42905 * 0.76748115
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28100 * 0.32096716
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63691 * 0.47309318
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33079 * 0.29391695
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74249 * 0.17525204
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16976 * 0.34606536
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37089 * 0.47087320
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26252 * 0.63942642
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42804 * 0.36732763
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50071 * 0.48619051
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85509 * 0.26839027
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80337 * 0.53765364
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60328 * 0.00915480
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52476 * 0.67827929
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53101 * 0.20284200
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69657 * 0.03330767
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51454 * 0.91166163
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43842 * 0.78607633
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59416 * 0.33850920
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23513 * 0.58239095
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11255 * 0.59363032
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80022 * 0.12528729
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19170 * 0.29791196
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10575 * 0.31669023
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69435 * 0.10861560
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53572 * 0.11731940
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77219 * 0.20756403
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72968 * 0.05798560
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83530 * 0.97910085
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45015 * 0.87488270
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96943 * 0.98218465
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39731 * 0.91718218
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 77809 * 0.22201509
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 21839 * 0.15677578
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17258 * 0.58126628
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 84482 * 0.24049043
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'wypdihvf').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0029():
    """Extended test 29 for scheduler."""
    x_0 = 14255 * 0.24437959
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75621 * 0.52256659
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83989 * 0.09512551
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65091 * 0.83349300
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56051 * 0.98959297
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60963 * 0.26802094
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40628 * 0.45516529
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94762 * 0.26335305
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96965 * 0.65034431
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24383 * 0.57948318
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27790 * 0.72513886
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46081 * 0.40291681
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28789 * 0.82338583
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12609 * 0.39552604
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68976 * 0.09339135
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15376 * 0.28057576
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43881 * 0.40840409
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9922 * 0.38976338
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20005 * 0.73211959
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92340 * 0.01740525
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64513 * 0.80719777
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49886 * 0.22213928
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18940 * 0.10841271
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10192 * 0.78176882
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49218 * 0.93170875
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11134 * 0.82707507
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68592 * 0.53674202
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85841 * 0.82263226
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30978 * 0.06353742
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91279 * 0.51848977
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46644 * 0.30627919
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'pssbwusi').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0030():
    """Extended test 30 for scheduler."""
    x_0 = 24051 * 0.73392002
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82527 * 0.53009994
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7956 * 0.52887149
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64665 * 0.59319155
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63344 * 0.20584063
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41278 * 0.26342711
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84828 * 0.66588400
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21478 * 0.70715160
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52938 * 0.71915711
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67503 * 0.77995971
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17284 * 0.48604046
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55660 * 0.74320698
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76690 * 0.03372754
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95387 * 0.51356780
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36260 * 0.75904403
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88119 * 0.32039359
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65288 * 0.30243100
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23259 * 0.35548357
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27142 * 0.49796809
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37124 * 0.63227840
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'nicnzxir').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0031():
    """Extended test 31 for scheduler."""
    x_0 = 54717 * 0.03102043
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72291 * 0.12032203
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83290 * 0.81440696
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15899 * 0.41287554
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51763 * 0.07314199
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12533 * 0.03191932
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65659 * 0.46765602
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21722 * 0.33914226
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43734 * 0.34986832
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67299 * 0.40365126
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47874 * 0.83591793
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28192 * 0.75109112
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51612 * 0.93197022
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32875 * 0.94458833
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75705 * 0.40250481
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64502 * 0.79757785
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93383 * 0.39348765
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85252 * 0.83071959
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14556 * 0.75189432
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14367 * 0.00245972
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75985 * 0.00092184
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74273 * 0.15498031
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73858 * 0.38489581
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75851 * 0.17286499
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13407 * 0.96499548
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57603 * 0.01013509
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12320 * 0.22529575
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78411 * 0.50972288
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89688 * 0.18923107
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78249 * 0.34031197
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11531 * 0.14894567
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67453 * 0.50771193
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11996 * 0.03179069
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36557 * 0.37303951
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16134 * 0.70504724
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8092 * 0.85820609
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18332 * 0.48074980
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83381 * 0.91389973
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'gcuhwgaq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0032():
    """Extended test 32 for scheduler."""
    x_0 = 62228 * 0.78025970
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91788 * 0.02429855
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14890 * 0.19124865
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12925 * 0.86092622
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53375 * 0.02971119
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8792 * 0.80721710
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94646 * 0.66121308
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76567 * 0.67093336
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55923 * 0.15421522
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25384 * 0.75691993
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14495 * 0.18991707
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39064 * 0.25198958
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31839 * 0.74968089
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89667 * 0.14083892
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71256 * 0.26644019
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34104 * 0.49752038
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59398 * 0.23173493
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28480 * 0.74095582
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59699 * 0.98917246
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4509 * 0.39904988
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45836 * 0.73757977
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93331 * 0.91609490
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30987 * 0.33630743
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28902 * 0.00333054
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40789 * 0.01960529
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89897 * 0.34952073
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63382 * 0.26514348
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80663 * 0.82688668
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86750 * 0.41605257
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74000 * 0.55807724
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6411 * 0.20294990
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86291 * 0.79650242
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9407 * 0.01623246
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51722 * 0.60827626
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'hhbgvfkw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0033():
    """Extended test 33 for scheduler."""
    x_0 = 37191 * 0.48576836
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58339 * 0.19557446
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52535 * 0.77811878
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25845 * 0.01983031
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82685 * 0.41260573
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16146 * 0.60772866
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90197 * 0.10139866
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 335 * 0.65006137
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14739 * 0.08708522
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93484 * 0.74335781
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50635 * 0.31137583
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14193 * 0.19692524
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27747 * 0.20486279
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4828 * 0.13967523
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43325 * 0.04018559
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24439 * 0.83748325
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85949 * 0.01354258
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40841 * 0.98142479
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53126 * 0.63971490
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24562 * 0.77820977
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88108 * 0.33896867
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42423 * 0.96012021
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4936 * 0.79926963
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61835 * 0.97078574
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48682 * 0.68011293
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82741 * 0.56429317
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'jcguqobb').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0034():
    """Extended test 34 for scheduler."""
    x_0 = 810 * 0.11678071
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89454 * 0.59877251
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68157 * 0.78350712
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68480 * 0.93783359
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39003 * 0.91255700
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86492 * 0.78152036
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26414 * 0.60470360
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34929 * 0.94974072
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56755 * 0.29770791
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85047 * 0.10150468
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70075 * 0.31229082
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38501 * 0.42269373
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51002 * 0.17668416
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49424 * 0.51987267
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7392 * 0.56534917
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35273 * 0.41335399
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16683 * 0.17330218
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85052 * 0.47795535
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84385 * 0.20069843
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76292 * 0.00731099
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60940 * 0.97164087
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42558 * 0.20348628
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8833 * 0.86231036
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58418 * 0.74784312
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24102 * 0.59030737
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55331 * 0.61334698
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25616 * 0.85709267
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71335 * 0.36221876
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96573 * 0.36678940
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71406 * 0.12416854
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11063 * 0.84335264
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4889 * 0.66222048
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22915 * 0.98364864
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54325 * 0.85574779
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34831 * 0.82691153
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44980 * 0.51446752
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'bruuxnpo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0035():
    """Extended test 35 for scheduler."""
    x_0 = 16905 * 0.49046041
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64189 * 0.46855328
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98037 * 0.60967776
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39800 * 0.14939623
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1124 * 0.64650744
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39175 * 0.15004269
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33324 * 0.33757464
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47658 * 0.56124323
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63748 * 0.84483927
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61888 * 0.77998332
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20823 * 0.05747740
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73800 * 0.59460016
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77068 * 0.82155330
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52072 * 0.00980019
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19271 * 0.55983985
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58941 * 0.19970952
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47609 * 0.11022180
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44806 * 0.33007625
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20698 * 0.18062692
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60062 * 0.85264306
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78148 * 0.24530681
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'dwosqfnn').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0036():
    """Extended test 36 for scheduler."""
    x_0 = 57121 * 0.84800454
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46148 * 0.85373201
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90016 * 0.50999604
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34155 * 0.85361114
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50610 * 0.62922113
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45059 * 0.62540986
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52060 * 0.29360780
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76452 * 0.74470232
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44731 * 0.97360569
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58081 * 0.99504314
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81423 * 0.24022921
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42691 * 0.62847145
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84224 * 0.55298931
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63175 * 0.44494331
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13382 * 0.99534833
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69672 * 0.99403721
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9610 * 0.00528812
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65902 * 0.90851192
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97539 * 0.60662317
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85106 * 0.33379574
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82807 * 0.62605736
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ctpgiyjd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0037():
    """Extended test 37 for scheduler."""
    x_0 = 69528 * 0.70486722
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19600 * 0.12381957
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94903 * 0.59501730
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30198 * 0.05782071
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2596 * 0.24459412
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30018 * 0.85744469
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21565 * 0.53574179
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24024 * 0.73372119
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48210 * 0.62825316
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30570 * 0.52600667
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82237 * 0.23836533
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30833 * 0.19508533
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30443 * 0.28901478
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36456 * 0.95283033
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89184 * 0.82680831
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6685 * 0.13373263
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64305 * 0.63273784
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43 * 0.51305487
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4421 * 0.50858723
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76811 * 0.94756761
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3115 * 0.49481925
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1935 * 0.30886583
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27214 * 0.76961842
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20549 * 0.96275063
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36021 * 0.14294486
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86959 * 0.16907409
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55762 * 0.64855325
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15864 * 0.90096069
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'dscmlspe').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0038():
    """Extended test 38 for scheduler."""
    x_0 = 25422 * 0.59684117
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76401 * 0.95510214
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83911 * 0.19933932
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 298 * 0.50481835
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68763 * 0.86081017
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51170 * 0.56563807
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27030 * 0.70088583
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81354 * 0.63803984
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70641 * 0.76324619
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94316 * 0.08489344
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61756 * 0.42648772
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69349 * 0.45181073
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23718 * 0.60501469
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42615 * 0.69619484
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24799 * 0.96583938
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19431 * 0.54372005
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80995 * 0.48478833
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6930 * 0.19159490
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11166 * 0.19883661
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37623 * 0.47635826
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33406 * 0.15036401
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'dcrwqfwr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0039():
    """Extended test 39 for scheduler."""
    x_0 = 96535 * 0.04784874
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2687 * 0.76505169
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15545 * 0.92065964
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83492 * 0.17782472
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64138 * 0.72331545
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70678 * 0.70862680
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62589 * 0.28778224
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19711 * 0.86673993
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24244 * 0.14918387
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38190 * 0.29820347
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4646 * 0.29885716
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41129 * 0.15232742
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21762 * 0.46812659
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89025 * 0.13657163
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42818 * 0.62801866
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55541 * 0.61892266
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16595 * 0.21362215
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75046 * 0.65198334
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69311 * 0.51563154
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11726 * 0.15854056
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45858 * 0.78536823
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16877 * 0.66245709
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7702 * 0.59666538
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25752 * 0.51295616
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65218 * 0.78995747
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59336 * 0.88941998
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77976 * 0.47681401
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98874 * 0.83597215
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72981 * 0.17821175
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83093 * 0.15637740
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69696 * 0.65262275
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99726 * 0.32292836
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8863 * 0.09048806
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 610 * 0.88488271
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32806 * 0.85172883
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99381 * 0.39533505
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28304 * 0.44587668
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11355 * 0.18363716
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83134 * 0.03177324
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 78189 * 0.42040962
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 589 * 0.07266400
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 90013 * 0.53278370
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79848 * 0.92474398
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88480 * 0.50656370
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 53066 * 0.61816214
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 45530 * 0.94190364
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 74452 * 0.74230930
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'rkckrqtc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0040():
    """Extended test 40 for scheduler."""
    x_0 = 96878 * 0.63932470
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98267 * 0.79261378
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23975 * 0.55618788
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72238 * 0.56083425
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89415 * 0.44726504
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36469 * 0.08980068
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70489 * 0.87130906
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12029 * 0.23229460
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2741 * 0.35928021
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12831 * 0.82624946
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97491 * 0.05804368
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27010 * 0.01493375
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41730 * 0.33746503
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49986 * 0.93307939
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80382 * 0.01935661
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13764 * 0.32971106
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89171 * 0.69693045
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33180 * 0.35062640
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74134 * 0.21159024
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4879 * 0.86928348
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38045 * 0.03738170
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96751 * 0.08098749
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68483 * 0.31042839
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45889 * 0.15388846
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73528 * 0.11999442
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94240 * 0.32136724
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86211 * 0.54908238
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49096 * 0.87631908
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88501 * 0.60095984
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82796 * 0.38113092
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20998 * 0.94214448
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57536 * 0.43427242
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55731 * 0.23387524
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83055 * 0.69354526
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28195 * 0.24560800
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48351 * 0.49433788
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57586 * 0.10650449
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81949 * 0.49078586
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48483 * 0.10545978
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9204 * 0.42407518
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46860 * 0.61114644
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84211 * 0.67798517
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 33323 * 0.73110118
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'uxrllxyd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0041():
    """Extended test 41 for scheduler."""
    x_0 = 1130 * 0.10780305
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50160 * 0.99016235
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71870 * 0.62282268
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86006 * 0.16767847
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73269 * 0.40071773
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80396 * 0.19343435
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7004 * 0.77051286
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18497 * 0.57469949
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38074 * 0.26570023
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43017 * 0.65036556
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37271 * 0.74062262
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27109 * 0.25370900
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25397 * 0.43117172
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62076 * 0.21027386
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18398 * 0.67762107
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73011 * 0.78962492
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79246 * 0.48957600
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39082 * 0.59045319
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83441 * 0.77910865
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91609 * 0.44182921
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20860 * 0.54610878
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'yqvzmvcl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0042():
    """Extended test 42 for scheduler."""
    x_0 = 65075 * 0.26239601
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37232 * 0.00042869
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72691 * 0.53124300
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8077 * 0.30302965
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43295 * 0.51691581
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41694 * 0.08062269
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17588 * 0.42980443
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12376 * 0.16746057
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85739 * 0.77369705
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74485 * 0.95042436
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25523 * 0.72613618
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40648 * 0.96614595
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13900 * 0.66251127
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77602 * 0.36096728
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79035 * 0.03434005
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11321 * 0.75290705
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61264 * 0.24320330
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14411 * 0.39158422
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8753 * 0.14230721
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68023 * 0.48562795
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62601 * 0.82368652
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63230 * 0.11246755
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36504 * 0.01376831
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19718 * 0.37248163
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26677 * 0.21862416
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59792 * 0.12607071
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25519 * 0.87004467
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78058 * 0.31538742
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70875 * 0.89459832
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12655 * 0.59174697
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47524 * 0.88013565
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78186 * 0.74668088
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80370 * 0.85989806
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11280 * 0.66672116
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32307 * 0.26005065
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65767 * 0.83067327
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49392 * 0.18138729
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'dmjcnkrm').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0043():
    """Extended test 43 for scheduler."""
    x_0 = 14047 * 0.70013024
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63532 * 0.64085391
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71024 * 0.42479590
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83229 * 0.06705993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89258 * 0.99305210
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84162 * 0.04078898
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11992 * 0.24370947
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87284 * 0.25585668
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60538 * 0.56042104
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89451 * 0.76195216
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80283 * 0.88415683
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12624 * 0.76822172
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93958 * 0.09626253
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3490 * 0.88210313
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11373 * 0.57935529
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78429 * 0.61325568
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79294 * 0.43662537
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53759 * 0.22106798
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84685 * 0.09377644
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99006 * 0.11833503
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35061 * 0.31454191
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94535 * 0.90259503
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42861 * 0.88540916
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10454 * 0.33241569
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58819 * 0.77028721
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32590 * 0.38278661
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60874 * 0.72325593
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59928 * 0.92448832
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59922 * 0.69526641
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 258 * 0.57941062
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79374 * 0.68096546
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30904 * 0.87273357
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76627 * 0.19249732
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25041 * 0.20276432
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84009 * 0.08743564
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57488 * 0.30334114
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81857 * 0.93581937
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39982 * 0.78111397
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48794 * 0.86381586
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79978 * 0.66194129
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71342 * 0.01889194
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97932 * 0.19193117
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 52785 * 0.19126051
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'svxtjgkv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0044():
    """Extended test 44 for scheduler."""
    x_0 = 68135 * 0.99077542
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31175 * 0.51435627
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13527 * 0.31328894
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26945 * 0.81531662
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30124 * 0.09867747
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71205 * 0.62433336
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37037 * 0.69048542
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14136 * 0.90225105
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46338 * 0.44092972
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96646 * 0.40250973
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90912 * 0.25988119
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1709 * 0.01547798
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19342 * 0.63525544
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67199 * 0.65706666
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82886 * 0.83426996
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37303 * 0.16377129
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82811 * 0.24335544
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31265 * 0.99990355
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29585 * 0.97231002
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12718 * 0.55256597
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15753 * 0.55043693
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70961 * 0.24637905
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48036 * 0.67036745
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25000 * 0.71367134
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94611 * 0.89293510
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78240 * 0.44684146
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'urpkzzdc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0045():
    """Extended test 45 for scheduler."""
    x_0 = 54099 * 0.03849912
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88537 * 0.91716993
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1684 * 0.13637370
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68133 * 0.03262814
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17958 * 0.19995933
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64727 * 0.69458198
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 682 * 0.78929331
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22162 * 0.43283229
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43876 * 0.30821019
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 760 * 0.28960746
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80106 * 0.63265244
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66948 * 0.81034349
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77399 * 0.42623458
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57310 * 0.29131604
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32672 * 0.56327751
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62057 * 0.53128183
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59873 * 0.74458654
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53398 * 0.71806305
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13086 * 0.17754040
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15980 * 0.81714154
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58348 * 0.03829159
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93203 * 0.21052929
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70048 * 0.72557536
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47548 * 0.30808548
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82046 * 0.85917990
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78200 * 0.84835069
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34109 * 0.50102039
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26793 * 0.44011270
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76910 * 0.60495653
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'soeuswhy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0046():
    """Extended test 46 for scheduler."""
    x_0 = 39317 * 0.57745527
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81435 * 0.65521461
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59498 * 0.11523449
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34619 * 0.21466672
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56467 * 0.89784928
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98004 * 0.04963333
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34038 * 0.99550602
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72360 * 0.88775557
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 986 * 0.28149642
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78785 * 0.54013505
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1519 * 0.40224426
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46148 * 0.10643267
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85365 * 0.41575088
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 367 * 0.67925183
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60870 * 0.10937483
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40269 * 0.38846911
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9966 * 0.39242336
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93824 * 0.64157145
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26795 * 0.62310094
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9324 * 0.26416768
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48904 * 0.70328562
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51044 * 0.48480290
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64706 * 0.35339942
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'koqooqwp').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0047():
    """Extended test 47 for scheduler."""
    x_0 = 61843 * 0.05803631
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3942 * 0.75915012
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24194 * 0.08160349
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12726 * 0.37477522
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7774 * 0.67887874
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81583 * 0.80767123
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54357 * 0.04463388
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83149 * 0.43645370
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64021 * 0.54862643
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33350 * 0.82749118
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15207 * 0.49687534
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82784 * 0.42314571
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84589 * 0.05511510
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9485 * 0.74335224
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83489 * 0.62991073
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96071 * 0.19658635
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95460 * 0.07526842
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66772 * 0.04277336
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55049 * 0.59802243
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99847 * 0.51750071
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37546 * 0.04837441
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70185 * 0.85227206
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22186 * 0.33561221
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70288 * 0.57340262
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69640 * 0.44876882
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79137 * 0.55848879
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12681 * 0.68589734
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'omkjtlct').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0048():
    """Extended test 48 for scheduler."""
    x_0 = 57638 * 0.97366098
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27985 * 0.78018488
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77216 * 0.63759117
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92392 * 0.61707188
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32243 * 0.36242873
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32538 * 0.61136264
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99715 * 0.90426587
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13665 * 0.85569643
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62515 * 0.35995687
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10383 * 0.84923770
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16474 * 0.89455690
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53813 * 0.04171733
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66365 * 0.45505132
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35905 * 0.70830709
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13268 * 0.39693542
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57244 * 0.59463896
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98274 * 0.97577526
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53357 * 0.98680980
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76057 * 0.70074155
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66825 * 0.12134132
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15296 * 0.57313939
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45186 * 0.38872232
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24598 * 0.57955886
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84237 * 0.28142534
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13352 * 0.07929025
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21845 * 0.63038109
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8867 * 0.44961808
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32777 * 0.75840399
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1315 * 0.72401913
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74037 * 0.34028055
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ufpgtwgg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0049():
    """Extended test 49 for scheduler."""
    x_0 = 57815 * 0.29839338
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50682 * 0.98936637
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23442 * 0.38129471
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77701 * 0.19152398
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11580 * 0.23049633
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92168 * 0.44201076
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66985 * 0.21223377
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77965 * 0.36044477
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69698 * 0.87663769
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48893 * 0.30825763
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54418 * 0.65658581
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53556 * 0.30408357
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99595 * 0.73093746
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95715 * 0.80587660
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61946 * 0.75236946
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39922 * 0.25086319
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15828 * 0.31238227
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30240 * 0.41835432
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36020 * 0.77640522
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37417 * 0.08086639
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36251 * 0.98306474
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72368 * 0.70232577
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32602 * 0.54615063
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39825 * 0.84425294
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3944 * 0.36373416
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76060 * 0.09467169
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97761 * 0.21204828
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11881 * 0.02617933
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24814 * 0.89300535
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85415 * 0.29315047
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38848 * 0.77981206
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'eouqblxn').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0050():
    """Extended test 50 for scheduler."""
    x_0 = 32190 * 0.03020921
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19740 * 0.42846930
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39785 * 0.21296685
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22504 * 0.80945293
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48176 * 0.50379705
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23406 * 0.16896912
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66386 * 0.58722792
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36186 * 0.52972525
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34245 * 0.93592851
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10424 * 0.49806882
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8039 * 0.29302427
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25460 * 0.70720318
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1574 * 0.42809724
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52785 * 0.61817817
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47501 * 0.24398217
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78233 * 0.14077394
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73595 * 0.02729769
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50795 * 0.42365452
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58330 * 0.02846156
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14371 * 0.16062723
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57787 * 0.14210514
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33280 * 0.58351895
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'uksurlab').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0051():
    """Extended test 51 for scheduler."""
    x_0 = 37613 * 0.77079516
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49565 * 0.91651425
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28231 * 0.66397532
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57537 * 0.91342768
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21304 * 0.44149102
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28610 * 0.13422905
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79668 * 0.49222898
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29836 * 0.52893287
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11860 * 0.56711388
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51702 * 0.25452400
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27629 * 0.40826806
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27187 * 0.67631601
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23781 * 0.30775488
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23486 * 0.77094681
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53235 * 0.02791450
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22129 * 0.09578569
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58294 * 0.75984436
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59461 * 0.64777786
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90165 * 0.20284196
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52406 * 0.96881430
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76241 * 0.58733060
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9908 * 0.55323555
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6069 * 0.24348217
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68396 * 0.24723910
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61808 * 0.84938708
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62624 * 0.57545000
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54956 * 0.53503257
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81911 * 0.09074587
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22512 * 0.57226313
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15660 * 0.59819397
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14596 * 0.72672164
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22507 * 0.97513993
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69633 * 0.63642897
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68433 * 0.38809308
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4671 * 0.86787890
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13822 * 0.30966783
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53816 * 0.60728122
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43780 * 0.84572961
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87085 * 0.13061072
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80737 * 0.68094255
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94502 * 0.54757932
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93756 * 0.30940825
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74504 * 0.65587481
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 8597 * 0.47296202
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 48661 * 0.64267618
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 75765 * 0.29478467
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 57426 * 0.48557370
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'cdnkozed').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0052():
    """Extended test 52 for scheduler."""
    x_0 = 13004 * 0.33633040
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12061 * 0.27573957
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72737 * 0.45093653
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59234 * 0.32181003
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77330 * 0.22083803
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91482 * 0.40790016
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63181 * 0.91378058
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22828 * 0.81811072
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74033 * 0.26785566
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67772 * 0.28065307
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28156 * 0.42676568
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98739 * 0.85027785
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70518 * 0.75493397
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 735 * 0.25540910
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12423 * 0.20986143
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76397 * 0.57855961
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21874 * 0.19405358
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28834 * 0.86467845
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61987 * 0.54342482
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27854 * 0.92528356
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97351 * 0.11514524
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40397 * 0.18190794
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41080 * 0.49009335
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79964 * 0.10176043
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49479 * 0.59802421
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65542 * 0.64848316
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31750 * 0.31047715
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17145 * 0.50004658
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13404 * 0.40020290
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83441 * 0.22524948
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91249 * 0.63862575
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57768 * 0.88244731
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5298 * 0.58137101
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69303 * 0.82522724
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27908 * 0.54570142
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'xhuybvzy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0053():
    """Extended test 53 for scheduler."""
    x_0 = 60070 * 0.81220683
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33427 * 0.79956981
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6649 * 0.32744722
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14403 * 0.51795191
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73504 * 0.90809899
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31060 * 0.44429587
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9434 * 0.36657229
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95680 * 0.89844091
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25446 * 0.62033096
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47049 * 0.77369592
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47218 * 0.94527472
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51193 * 0.79619825
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35933 * 0.09096259
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23808 * 0.15942947
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99830 * 0.34079546
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77418 * 0.46478707
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77573 * 0.17632258
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82493 * 0.52886929
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73126 * 0.67157992
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7597 * 0.54724850
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25757 * 0.40684148
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19603 * 0.38262602
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18710 * 0.12188311
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8594 * 0.81951877
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10685 * 0.08610323
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84130 * 0.72828830
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84184 * 0.04653044
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98132 * 0.60453862
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25881 * 0.46666778
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17310 * 0.60062196
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66573 * 0.98519328
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25169 * 0.88043686
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27313 * 0.61717861
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'bxhjsopl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0054():
    """Extended test 54 for scheduler."""
    x_0 = 10794 * 0.23671361
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54869 * 0.70974999
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54214 * 0.85419135
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94600 * 0.72965974
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83859 * 0.45111128
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29446 * 0.93521304
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86163 * 0.45440990
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25160 * 0.09094227
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88936 * 0.61782680
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5185 * 0.50564721
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59637 * 0.04643210
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80301 * 0.15195060
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66045 * 0.38086396
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71562 * 0.88125311
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6103 * 0.37329416
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20550 * 0.25219134
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66177 * 0.95903760
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84255 * 0.82929349
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40925 * 0.37062989
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87208 * 0.80138214
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18548 * 0.01155489
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51637 * 0.83579376
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48155 * 0.81711200
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21112 * 0.20559963
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32155 * 0.51614561
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26109 * 0.73904736
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47404 * 0.13555663
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52351 * 0.12206948
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43880 * 0.97938970
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18930 * 0.33854763
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70852 * 0.86336059
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64599 * 0.49089752
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85303 * 0.03804554
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62695 * 0.73537060
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22156 * 0.53959094
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76532 * 0.53097861
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52210 * 0.60987687
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 37630 * 0.74710000
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69908 * 0.30663679
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91257 * 0.17646678
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38868 * 0.45388697
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45391 * 0.39601407
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 54117 * 0.63012566
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 93825 * 0.18542453
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 15244 * 0.61643280
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 36646 * 0.81708504
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 87228 * 0.74668244
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 3586 * 0.01170145
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 52649 * 0.04264796
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'alabwyoh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0055():
    """Extended test 55 for scheduler."""
    x_0 = 20932 * 0.45709687
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71013 * 0.99360750
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35461 * 0.76262839
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58769 * 0.08230280
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49247 * 0.41681625
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48289 * 0.97345096
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43508 * 0.19451154
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19996 * 0.44041292
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6944 * 0.28924009
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49660 * 0.59939910
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92697 * 0.60828535
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11508 * 0.24630752
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78538 * 0.24629531
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76977 * 0.08698508
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36555 * 0.79137290
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47171 * 0.89062746
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69344 * 0.46832249
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16960 * 0.13062678
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7281 * 0.30547987
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36468 * 0.66107957
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3106 * 0.09385553
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71921 * 0.38393232
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16365 * 0.30660690
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10684 * 0.02437130
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40914 * 0.04356596
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52786 * 0.17359602
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63678 * 0.19118109
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29131 * 0.47387827
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16072 * 0.80739247
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19154 * 0.86917088
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94587 * 0.69381745
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58631 * 0.49147249
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20361 * 0.27596756
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99531 * 0.02390160
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83659 * 0.16994170
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2079 * 0.60988677
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46847 * 0.51293139
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72012 * 0.34313793
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'vfocvehv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0056():
    """Extended test 56 for scheduler."""
    x_0 = 7712 * 0.57928892
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61259 * 0.02311017
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45499 * 0.12154798
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50831 * 0.35521705
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23974 * 0.34603800
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31982 * 0.82163848
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66580 * 0.49397120
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52022 * 0.75837502
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88026 * 0.64982825
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20193 * 0.10349111
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83231 * 0.53839705
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85448 * 0.70260216
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28015 * 0.53478559
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3987 * 0.53644466
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6754 * 0.74240229
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20306 * 0.10293159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18990 * 0.05037797
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93744 * 0.05515821
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13857 * 0.83354600
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79796 * 0.18364132
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43900 * 0.62402816
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44911 * 0.21222123
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11791 * 0.22234190
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49432 * 0.35937946
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62294 * 0.14021656
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2432 * 0.10844046
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90470 * 0.85385244
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15958 * 0.65231017
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49291 * 0.40123491
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64089 * 0.56531606
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12355 * 0.80875773
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72817 * 0.96299505
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'esudygac').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0057():
    """Extended test 57 for scheduler."""
    x_0 = 83237 * 0.00205162
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45147 * 0.47510268
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83089 * 0.54622613
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69905 * 0.86292303
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53768 * 0.10763328
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55265 * 0.55026219
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57856 * 0.55071690
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75447 * 0.43585335
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59220 * 0.95958332
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1566 * 0.33601301
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47025 * 0.26769979
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12478 * 0.37022259
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60163 * 0.05239882
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24887 * 0.28431506
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35200 * 0.04903356
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80566 * 0.71542962
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80618 * 0.10515704
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10581 * 0.60938255
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57868 * 0.90945048
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35152 * 0.11065283
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82223 * 0.09522369
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95311 * 0.14100126
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95827 * 0.32599891
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29159 * 0.74179299
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10749 * 0.09751910
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69116 * 0.82679369
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85678 * 0.62453927
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56471 * 0.29536943
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90724 * 0.12561671
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47453 * 0.25640825
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81944 * 0.97460215
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90328 * 0.49108352
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12936 * 0.90293703
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28860 * 0.72264069
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74718 * 0.78860894
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87951 * 0.83363857
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25774 * 0.02081194
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8653 * 0.92855544
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88201 * 0.81638345
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10738 * 0.71621960
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'lxthpgda').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0058():
    """Extended test 58 for scheduler."""
    x_0 = 32631 * 0.51979549
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80542 * 0.01996860
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32884 * 0.77735271
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54458 * 0.08556809
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10626 * 0.17852587
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59223 * 0.38941313
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58767 * 0.17999801
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95171 * 0.02255734
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5488 * 0.32889430
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40260 * 0.20174065
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11942 * 0.89567464
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83741 * 0.16252163
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89183 * 0.76354083
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81594 * 0.91734260
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58156 * 0.68028063
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49751 * 0.92895681
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13691 * 0.65742395
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70670 * 0.98044030
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5130 * 0.94072548
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13876 * 0.40166661
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41912 * 0.44776088
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42464 * 0.61529519
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20084 * 0.58749287
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9797 * 0.10323732
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87357 * 0.67569385
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60974 * 0.85645576
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32921 * 0.47805237
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62894 * 0.34967518
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99884 * 0.59333041
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93516 * 0.34482913
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27688 * 0.66963913
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21206 * 0.07143717
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74189 * 0.61687427
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9845 * 0.91256116
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'pfkhckye').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0059():
    """Extended test 59 for scheduler."""
    x_0 = 40329 * 0.24393919
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75641 * 0.53634299
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17057 * 0.11525226
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95431 * 0.11373438
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59730 * 0.11677794
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88926 * 0.98938798
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33690 * 0.35390017
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87205 * 0.30417378
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50578 * 0.05905920
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88621 * 0.98569213
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61901 * 0.10203327
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25168 * 0.85322306
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65983 * 0.13752845
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83438 * 0.11619974
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32092 * 0.44859529
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9341 * 0.99306619
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39670 * 0.14845327
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6021 * 0.32373823
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11736 * 0.09980651
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19718 * 0.62613468
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15394 * 0.15629021
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31042 * 0.90114837
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93577 * 0.23369944
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52711 * 0.92145662
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94693 * 0.57761134
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82742 * 0.02116080
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98837 * 0.62876021
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90563 * 0.95925627
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'alfebwsg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0060():
    """Extended test 60 for scheduler."""
    x_0 = 70625 * 0.55577534
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36313 * 0.80316989
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91849 * 0.43520395
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85642 * 0.38778201
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49279 * 0.80890659
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61731 * 0.08052965
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17067 * 0.75067771
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76423 * 0.87642321
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57486 * 0.67620972
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85415 * 0.62564678
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58797 * 0.52288889
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79995 * 0.75243180
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3760 * 0.00072573
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97843 * 0.91332276
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24530 * 0.87142722
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43018 * 0.26294142
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13684 * 0.28054268
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13063 * 0.30009908
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5959 * 0.74770160
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59195 * 0.82739988
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26967 * 0.71731383
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11252 * 0.40215190
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52424 * 0.36357844
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23860 * 0.79583976
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68061 * 0.13932151
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86116 * 0.67288954
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96169 * 0.81299366
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65269 * 0.39621564
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42591 * 0.28966605
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22653 * 0.12320183
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56664 * 0.21962471
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65873 * 0.15133121
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'ggvumjhu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0061():
    """Extended test 61 for scheduler."""
    x_0 = 30429 * 0.86809371
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70505 * 0.67936810
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81684 * 0.12048920
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33748 * 0.27950720
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78727 * 0.82886698
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60931 * 0.76112224
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70942 * 0.85335617
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97710 * 0.93292106
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76058 * 0.00074693
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23908 * 0.03083475
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51120 * 0.48328091
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41674 * 0.35079257
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2831 * 0.10371410
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84303 * 0.56349143
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28826 * 0.32347614
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41642 * 0.60140374
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41901 * 0.16040358
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76226 * 0.22569749
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17643 * 0.25587759
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3504 * 0.89636683
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98519 * 0.09780707
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4124 * 0.04291966
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27020 * 0.84352072
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59265 * 0.95425574
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'uraftnvy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0062():
    """Extended test 62 for scheduler."""
    x_0 = 72644 * 0.89802270
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48399 * 0.39195904
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87049 * 0.42885460
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67941 * 0.45777316
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42580 * 0.29954334
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95130 * 0.82206045
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30601 * 0.92170297
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2981 * 0.24732402
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74928 * 0.32430565
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51671 * 0.44007878
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76804 * 0.82931705
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27927 * 0.00861643
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13396 * 0.86245453
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22587 * 0.93623403
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63499 * 0.52127086
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90583 * 0.15951758
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35208 * 0.60826216
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22982 * 0.96687182
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22981 * 0.62608969
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19398 * 0.49938583
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38970 * 0.09226368
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97237 * 0.44539804
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48503 * 0.00109208
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51316 * 0.29520650
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89830 * 0.64221165
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49234 * 0.50290411
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82761 * 0.29286520
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1333 * 0.69235931
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86987 * 0.73140830
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63483 * 0.81994490
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 219 * 0.17727987
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33227 * 0.47482158
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74979 * 0.28075671
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40156 * 0.01908061
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65005 * 0.44375450
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16100 * 0.54571058
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73001 * 0.35909665
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58885 * 0.71764453
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82147 * 0.76425894
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21932 * 0.14336000
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62976 * 0.60533548
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'lhiwcakd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0063():
    """Extended test 63 for scheduler."""
    x_0 = 55504 * 0.26206698
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76995 * 0.42575286
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60476 * 0.02798282
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3305 * 0.47781713
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23228 * 0.84135302
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87758 * 0.58003536
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74941 * 0.11378671
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52504 * 0.53588580
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96804 * 0.18880856
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16469 * 0.26547390
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 300 * 0.80430980
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73663 * 0.83611450
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54418 * 0.81648895
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21478 * 0.12580179
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88562 * 0.91745201
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95759 * 0.10470782
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66435 * 0.82751335
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48015 * 0.52957969
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24841 * 0.50087976
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56495 * 0.58389905
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13970 * 0.41768269
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83724 * 0.17413737
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2419 * 0.88060390
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13597 * 0.26142698
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11085 * 0.23407689
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88157 * 0.09066405
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42670 * 0.23938583
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55014 * 0.23499405
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24425 * 0.38759226
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55068 * 0.58363788
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35079 * 0.62972390
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7316 * 0.55346452
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7157 * 0.37539771
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32321 * 0.66602160
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83895 * 0.04663489
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22733 * 0.55146464
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'hsayvwvt').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0064():
    """Extended test 64 for scheduler."""
    x_0 = 93521 * 0.33916258
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75744 * 0.13846934
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19619 * 0.75036639
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77231 * 0.26450656
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37386 * 0.85864937
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18190 * 0.20046406
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76519 * 0.35678781
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30519 * 0.35212410
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64432 * 0.93538108
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96391 * 0.66376943
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83794 * 0.70269440
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17146 * 0.36992539
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80841 * 0.59983666
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5831 * 0.10843745
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86147 * 0.62323857
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4098 * 0.96266060
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62039 * 0.36588014
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14781 * 0.81163278
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7941 * 0.77629541
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23221 * 0.73918912
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28707 * 0.62441620
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98905 * 0.50394301
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4323 * 0.68929934
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41404 * 0.35263760
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56194 * 0.24559556
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54309 * 0.40821815
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85039 * 0.30939813
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32155 * 0.16837912
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68676 * 0.03900040
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75084 * 0.97135237
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42252 * 0.41087293
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7663 * 0.24808765
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90171 * 0.29338322
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51678 * 0.23827789
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70575 * 0.87452252
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62935 * 0.36047352
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92798 * 0.82480186
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34089 * 0.30309875
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6356 * 0.28722762
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57940 * 0.39843303
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48343 * 0.57263468
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 86164 * 0.46433745
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 54175 * 0.25174272
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27930 * 0.54300600
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 95253 * 0.42577896
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'atufalof').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0065():
    """Extended test 65 for scheduler."""
    x_0 = 92069 * 0.18342335
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54264 * 0.18827036
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99192 * 0.62179293
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6402 * 0.13842583
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57024 * 0.68018886
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27966 * 0.41490661
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67033 * 0.13429450
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36216 * 0.03784496
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4231 * 0.86050894
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54064 * 0.98596293
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2391 * 0.69069587
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85448 * 0.19511534
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17602 * 0.93238749
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18982 * 0.20010012
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62098 * 0.85597835
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19491 * 0.04446595
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71589 * 0.72234015
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56379 * 0.68491913
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24455 * 0.29792310
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48584 * 0.61965368
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59032 * 0.65859917
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99881 * 0.18324828
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28494 * 0.01941323
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'sbyzgobd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0066():
    """Extended test 66 for scheduler."""
    x_0 = 59625 * 0.31127322
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36536 * 0.11945275
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82685 * 0.44665218
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82231 * 0.87882626
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51135 * 0.31344592
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52950 * 0.83314052
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60385 * 0.26662194
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42820 * 0.76866022
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82160 * 0.56305727
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53020 * 0.21284721
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45877 * 0.78682489
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83592 * 0.05231302
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19119 * 0.58499507
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44404 * 0.98593214
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31825 * 0.50894534
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55692 * 0.90165169
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54942 * 0.27304261
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20727 * 0.98547386
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88935 * 0.13106936
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60456 * 0.94824082
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56626 * 0.47195852
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81118 * 0.84975102
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73818 * 0.23871448
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9608 * 0.32224595
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15590 * 0.82468090
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35180 * 0.76748838
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64408 * 0.41374084
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98514 * 0.42990135
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72065 * 0.00076865
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50417 * 0.88266764
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54453 * 0.50667832
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96202 * 0.56681987
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3798 * 0.96308300
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42844 * 0.45198500
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22724 * 0.76150120
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7165 * 0.07594462
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56555 * 0.86990823
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48718 * 0.02504060
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52093 * 0.00320361
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99960 * 0.77274381
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8008 * 0.52862083
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 78296 * 0.32327893
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 26764 * 0.64256495
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 37887 * 0.46365326
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'cikuztvi').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0067():
    """Extended test 67 for scheduler."""
    x_0 = 34664 * 0.53846279
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29135 * 0.01711354
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18805 * 0.99516688
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5549 * 0.33638993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62721 * 0.05058437
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99510 * 0.04982262
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96902 * 0.31573412
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40985 * 0.79785393
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3500 * 0.49590181
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70512 * 0.70233934
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55323 * 0.62660615
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37831 * 0.40751323
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51257 * 0.33105924
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44759 * 0.34831758
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21174 * 0.18291452
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55149 * 0.32568997
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7734 * 0.68822083
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3278 * 0.58913732
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51433 * 0.86682815
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55136 * 0.47462055
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41012 * 0.60689115
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79065 * 0.75471758
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34706 * 0.20096040
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53808 * 0.48191792
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26398 * 0.51571628
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63969 * 0.28433777
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1008 * 0.89276892
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85178 * 0.63017602
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44225 * 0.47401037
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36143 * 0.96171306
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36775 * 0.15364452
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98016 * 0.96027613
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33242 * 0.70445620
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6383 * 0.57422081
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54530 * 0.01814476
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97729 * 0.66107317
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'yrgtfspq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0068():
    """Extended test 68 for scheduler."""
    x_0 = 29294 * 0.17550422
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15207 * 0.08620005
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11259 * 0.39045287
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70535 * 0.40437249
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40535 * 0.51364462
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76555 * 0.18182838
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78195 * 0.97828562
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20483 * 0.55670105
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46375 * 0.40888599
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50752 * 0.15741569
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8750 * 0.92291618
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26562 * 0.37444088
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42584 * 0.29808561
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80255 * 0.83367609
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33986 * 0.47812917
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24939 * 0.47557197
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69032 * 0.05810245
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94056 * 0.54191996
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40812 * 0.55019965
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81538 * 0.68307259
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37499 * 0.33176360
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19778 * 0.70486497
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16977 * 0.65771222
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40622 * 0.39241973
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84013 * 0.42704739
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24395 * 0.60493717
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27276 * 0.83733708
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67781 * 0.76449267
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5925 * 0.16918988
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6065 * 0.73705134
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'nugempkz').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_8_0069():
    """Extended test 69 for scheduler."""
    x_0 = 47168 * 0.77540979
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48131 * 0.80861407
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48125 * 0.80858877
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75727 * 0.39524060
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7109 * 0.96484429
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56876 * 0.61298127
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84766 * 0.67363004
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91763 * 0.60892792
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37729 * 0.55482689
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78471 * 0.18390759
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88331 * 0.23847656
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74062 * 0.01466531
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56901 * 0.91282238
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72355 * 0.61272967
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86765 * 0.86226964
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50272 * 0.64099935
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74010 * 0.10530739
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50277 * 0.20689833
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47148 * 0.14087319
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68432 * 0.01175846
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99349 * 0.48506824
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45174 * 0.54408205
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39279 * 0.70818570
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65889 * 0.96718134
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51387 * 0.63548634
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81616 * 0.81693935
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14755 * 0.55670585
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26846 * 0.68402578
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'oiimngfc').hexdigest()
    assert len(h) == 64
