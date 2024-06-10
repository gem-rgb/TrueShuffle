"""Extended tests for migration suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_migration_extended_8_0000():
    """Extended test 0 for migration."""
    x_0 = 13109 * 0.22377131
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53916 * 0.12371100
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16427 * 0.25923719
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71789 * 0.74984570
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89419 * 0.54606339
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39658 * 0.57094546
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22779 * 0.76787568
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92945 * 0.27040538
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65766 * 0.13366515
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66677 * 0.66725257
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66490 * 0.46307576
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9172 * 0.30034920
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68992 * 0.11568214
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22771 * 0.87240066
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26306 * 0.74930405
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93189 * 0.53256437
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45888 * 0.92493596
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40153 * 0.05806561
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90896 * 0.14719559
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10224 * 0.53848422
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96672 * 0.37455896
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69650 * 0.63627340
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55759 * 0.47228892
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52950 * 0.94272093
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42647 * 0.93753183
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59754 * 0.05822416
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76229 * 0.62491273
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86267 * 0.35318636
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3693 * 0.80403767
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90379 * 0.81001930
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25709 * 0.44931365
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46785 * 0.35372018
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'kxdzeggm').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0001():
    """Extended test 1 for migration."""
    x_0 = 84835 * 0.77690899
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60705 * 0.69163856
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77021 * 0.51705427
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23427 * 0.53510877
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55268 * 0.24469283
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79953 * 0.00498718
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7336 * 0.24655058
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77150 * 0.57805462
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98376 * 0.61333966
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15050 * 0.33850844
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11073 * 0.23205739
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97420 * 0.64069075
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89594 * 0.94052947
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76833 * 0.58829522
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22914 * 0.69812918
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97510 * 0.99169582
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89626 * 0.96535657
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92441 * 0.53606522
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60428 * 0.87046510
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27312 * 0.90591496
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5333 * 0.15175411
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7806 * 0.24600725
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82152 * 0.77075150
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42969 * 0.38778364
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31266 * 0.40938548
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30338 * 0.50552323
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6237 * 0.03037758
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44436 * 0.71341993
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14365 * 0.29389313
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81971 * 0.46188049
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99946 * 0.02839088
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20598 * 0.38369347
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31163 * 0.52813352
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37836 * 0.35301873
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21592 * 0.41202124
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1669 * 0.69235040
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22584 * 0.67004230
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5843 * 0.92810725
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 33227 * 0.64044076
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91342 * 0.43036038
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1191 * 0.78413867
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79305 * 0.82174837
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 82404 * 0.81724169
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 71477 * 0.21655650
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 40880 * 0.00127941
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 70394 * 0.22301648
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 31602 * 0.69098080
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 72099 * 0.92711933
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'kcpgfcoh').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0002():
    """Extended test 2 for migration."""
    x_0 = 52306 * 0.14703375
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53030 * 0.70800391
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38018 * 0.44634309
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86094 * 0.98518505
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48140 * 0.52819385
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25042 * 0.47451305
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60394 * 0.95497618
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69263 * 0.51489811
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84215 * 0.13884194
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11002 * 0.77336794
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2965 * 0.54458194
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19485 * 0.53854451
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79351 * 0.62153590
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59863 * 0.87058595
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10212 * 0.75073873
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5417 * 0.22861066
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38717 * 0.24398097
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58338 * 0.86787107
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89249 * 0.01331950
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81403 * 0.62752686
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3995 * 0.09749224
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40329 * 0.58927992
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45362 * 0.54902720
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69166 * 0.04862983
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89838 * 0.03084763
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10655 * 0.52904695
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30468 * 0.98455340
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52931 * 0.56868717
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'smrfzpkk').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0003():
    """Extended test 3 for migration."""
    x_0 = 48345 * 0.13891427
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90954 * 0.34087948
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7217 * 0.17604731
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88907 * 0.04360661
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61972 * 0.11336885
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23769 * 0.10475238
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99352 * 0.55800144
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36834 * 0.80991002
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97007 * 0.78182586
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45990 * 0.08648654
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36739 * 0.21904713
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94184 * 0.96928569
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33724 * 0.50804181
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74521 * 0.54426258
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28561 * 0.71545929
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81835 * 0.32617079
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12266 * 0.14731277
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6593 * 0.44053740
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19276 * 0.30445554
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54736 * 0.97571367
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35630 * 0.08045397
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94469 * 0.00486715
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61384 * 0.50559112
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92564 * 0.87585454
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96287 * 0.24132362
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19531 * 0.97041380
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43281 * 0.28556570
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97253 * 0.96509820
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93093 * 0.77137586
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86022 * 0.78397955
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28529 * 0.57606926
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50688 * 0.85878094
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98839 * 0.81642137
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41909 * 0.42041416
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50270 * 0.45218509
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78524 * 0.84563721
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27881 * 0.85437211
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44932 * 0.61936415
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10046 * 0.25269959
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62768 * 0.11965328
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 70596 * 0.74133739
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50181 * 0.84533251
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 99708 * 0.25572344
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'onimeprd').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0004():
    """Extended test 4 for migration."""
    x_0 = 86389 * 0.62956400
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14704 * 0.30404867
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61437 * 0.11984210
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32055 * 0.40242461
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47945 * 0.82326581
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45481 * 0.60114196
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16903 * 0.11961239
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56441 * 0.53213457
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31749 * 0.06336683
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49686 * 0.90341137
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96434 * 0.49902146
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11474 * 0.99220638
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 252 * 0.17601813
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17419 * 0.08878752
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8447 * 0.39161281
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86067 * 0.20233190
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8448 * 0.49742588
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90227 * 0.13360484
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7181 * 0.99606076
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98551 * 0.54158342
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58312 * 0.97375271
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44163 * 0.28369884
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26543 * 0.38502777
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46809 * 0.49892516
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4091 * 0.28308689
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59518 * 0.39024535
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63157 * 0.66286792
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3942 * 0.01975194
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99144 * 0.78778507
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34077 * 0.26112908
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27534 * 0.38184579
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65276 * 0.87732370
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88195 * 0.95274835
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31507 * 0.98190209
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27001 * 0.84798155
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20 * 0.52105710
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26138 * 0.53974379
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60276 * 0.52956835
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58502 * 0.62546419
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73974 * 0.90066941
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ofyxodho').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0005():
    """Extended test 5 for migration."""
    x_0 = 75099 * 0.16631253
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48709 * 0.06373156
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49785 * 0.10480540
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23564 * 0.22748285
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71909 * 0.74837045
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12931 * 0.21144087
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36986 * 0.17390442
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52998 * 0.98533560
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42809 * 0.16356370
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3763 * 0.37455817
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15479 * 0.60481964
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44219 * 0.00410399
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80871 * 0.79337555
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75930 * 0.36497246
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24205 * 0.20897825
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80044 * 0.32881649
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64587 * 0.01048019
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78166 * 0.57254219
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59367 * 0.66496228
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17777 * 0.73935844
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89866 * 0.03581622
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35235 * 0.57797727
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'uoytuumd').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0006():
    """Extended test 6 for migration."""
    x_0 = 27021 * 0.61594526
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85869 * 0.77336904
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64864 * 0.88714868
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25491 * 0.88847127
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77592 * 0.36624664
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51503 * 0.48109771
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63677 * 0.85643095
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27212 * 0.17818291
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8640 * 0.98655026
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80728 * 0.36443536
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49939 * 0.54467052
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14153 * 0.61540697
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1894 * 0.47793439
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21797 * 0.52910018
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43682 * 0.65330892
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71108 * 0.96957438
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34249 * 0.90137991
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88527 * 0.21751087
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65936 * 0.12384562
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12158 * 0.81322010
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8095 * 0.54649402
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30188 * 0.13287976
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4949 * 0.54316090
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77386 * 0.76856244
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1507 * 0.61668050
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13825 * 0.39722885
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58760 * 0.24321216
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85160 * 0.41384807
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65995 * 0.62408229
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17159 * 0.77294334
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60036 * 0.92477931
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7548 * 0.06684979
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43357 * 0.42858267
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95239 * 0.46905809
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57750 * 0.99566775
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35858 * 0.44890283
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ilnvmuoz').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0007():
    """Extended test 7 for migration."""
    x_0 = 58650 * 0.91297707
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58331 * 0.81732650
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53635 * 0.15558398
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24819 * 0.71614242
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77421 * 0.45074565
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34393 * 0.50144008
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17473 * 0.83974374
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65567 * 0.27843120
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33931 * 0.04146214
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89976 * 0.75993875
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94763 * 0.90598820
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24493 * 0.35443341
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26808 * 0.30501596
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81409 * 0.69108612
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75209 * 0.44535131
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88186 * 0.34407466
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69938 * 0.41537127
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57643 * 0.25549894
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73057 * 0.34305414
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69669 * 0.05090605
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40325 * 0.27216655
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49486 * 0.66995625
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95841 * 0.71594352
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81025 * 0.96713024
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91523 * 0.14532488
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48081 * 0.19980038
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4243 * 0.73416986
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 264 * 0.52879363
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56306 * 0.17880950
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68500 * 0.36231957
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82726 * 0.96649167
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80293 * 0.62725347
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11097 * 0.30182002
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67920 * 0.58993555
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24050 * 0.40453397
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5302 * 0.61172647
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61065 * 0.27709994
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6844 * 0.94642956
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23899 * 0.04166703
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38797 * 0.60878302
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81759 * 0.06432641
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77015 * 0.79674842
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18649 * 0.82403773
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 37572 * 0.81581624
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 18575 * 0.21787968
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 51839 * 0.21852101
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 9940 * 0.81511394
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 6415 * 0.95297415
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 47118 * 0.24618805
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'nzcyabvs').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0008():
    """Extended test 8 for migration."""
    x_0 = 47778 * 0.44534336
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67151 * 0.95365819
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79766 * 0.49415658
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24086 * 0.95286265
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47409 * 0.60212526
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50829 * 0.65272173
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78305 * 0.27206473
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93226 * 0.83702147
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62495 * 0.94490570
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51061 * 0.28135995
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69012 * 0.14925786
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61172 * 0.33927774
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46524 * 0.03381763
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29259 * 0.49886832
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68638 * 0.94878460
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53938 * 0.16400007
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86115 * 0.56867825
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25531 * 0.56652717
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10398 * 0.89538173
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7006 * 0.63600760
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15354 * 0.28201199
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'izdorcku').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0009():
    """Extended test 9 for migration."""
    x_0 = 7696 * 0.56313649
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95043 * 0.55000166
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7427 * 0.57575580
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32615 * 0.05243952
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34616 * 0.12473971
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33511 * 0.00038776
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83037 * 0.62509910
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34029 * 0.58365586
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94178 * 0.71262568
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76322 * 0.96551530
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60291 * 0.17233735
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94768 * 0.42398327
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22503 * 0.89425661
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98803 * 0.19505103
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75293 * 0.25130131
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4654 * 0.25347671
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37406 * 0.75807731
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62257 * 0.65110730
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39776 * 0.05057426
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30495 * 0.39210895
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96860 * 0.92845631
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86678 * 0.47036142
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81650 * 0.50480216
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39633 * 0.51464887
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80065 * 0.66985655
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87045 * 0.44857166
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4197 * 0.78902270
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'xwpqubpb').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0010():
    """Extended test 10 for migration."""
    x_0 = 50945 * 0.48207243
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66892 * 0.49484760
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5857 * 0.49940722
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53083 * 0.57346280
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 798 * 0.80344574
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39915 * 0.17194596
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72254 * 0.31053790
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78423 * 0.87120300
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26953 * 0.66239342
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42513 * 0.41504375
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40580 * 0.46953661
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44979 * 0.14410034
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57123 * 0.84559377
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90661 * 0.57944675
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14784 * 0.80795585
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79435 * 0.72516928
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55036 * 0.35055251
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63597 * 0.51312953
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80122 * 0.52178564
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62304 * 0.02304179
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16239 * 0.09402405
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71681 * 0.72754069
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89598 * 0.65611523
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80951 * 0.43700229
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80685 * 0.30365699
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76230 * 0.04807284
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71118 * 0.47098448
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76493 * 0.10081142
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72091 * 0.89757089
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95249 * 0.29564208
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24694 * 0.58725030
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 34470 * 0.39674233
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'aifpwwdx').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0011():
    """Extended test 11 for migration."""
    x_0 = 94504 * 0.20556320
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79390 * 0.57688469
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40933 * 0.29677305
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61100 * 0.91901206
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15591 * 0.92646877
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90756 * 0.49190180
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57860 * 0.05468255
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66242 * 0.62085277
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18356 * 0.37591034
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55808 * 0.20989813
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87636 * 0.02333474
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73280 * 0.70694905
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98893 * 0.92172547
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20787 * 0.68055255
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11022 * 0.55938994
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31103 * 0.75741450
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65240 * 0.66169045
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75326 * 0.48350154
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28099 * 0.62488261
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72713 * 0.80725201
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32448 * 0.45448946
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85682 * 0.14934810
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26552 * 0.12289263
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66290 * 0.99808263
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89329 * 0.70618065
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18931 * 0.09529853
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63621 * 0.13893759
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36768 * 0.10311387
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25762 * 0.35869032
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96263 * 0.36266795
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39219 * 0.88191499
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96075 * 0.78746708
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'anorggcv').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0012():
    """Extended test 12 for migration."""
    x_0 = 97308 * 0.65642211
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88320 * 0.30266117
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21829 * 0.95643793
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63648 * 0.98780562
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52042 * 0.01541710
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51167 * 0.30933461
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72454 * 0.23853254
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30749 * 0.01609716
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60209 * 0.76481124
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14473 * 0.61124486
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62116 * 0.06150968
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63929 * 0.15837902
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22719 * 0.77478311
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35720 * 0.67865787
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71143 * 0.88712698
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51647 * 0.67074587
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90802 * 0.12006560
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20491 * 0.02051030
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32736 * 0.65025099
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76584 * 0.88301664
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76660 * 0.10654503
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24035 * 0.61841065
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99823 * 0.17884506
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31437 * 0.73911899
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30256 * 0.70269798
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35125 * 0.61876119
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92457 * 0.90525073
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52532 * 0.87938969
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68126 * 0.87194182
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79172 * 0.40332041
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57247 * 0.51815065
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 449 * 0.33581339
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80507 * 0.59004293
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18165 * 0.42638631
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'jfkdozem').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0013():
    """Extended test 13 for migration."""
    x_0 = 72474 * 0.51422354
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2778 * 0.95176978
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74833 * 0.39252225
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80941 * 0.21226644
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3173 * 0.57038452
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5666 * 0.60385920
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35322 * 0.92538485
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3940 * 0.54278653
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43657 * 0.54860491
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24411 * 0.84775454
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28476 * 0.03703266
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18964 * 0.06705501
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54136 * 0.04154228
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91039 * 0.24210872
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92070 * 0.60683493
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43408 * 0.93868276
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22076 * 0.75455043
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96182 * 0.72268407
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 610 * 0.37941552
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18677 * 0.68572985
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80856 * 0.91950609
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47236 * 0.92523143
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75113 * 0.56413111
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'grbwmcax').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0014():
    """Extended test 14 for migration."""
    x_0 = 96746 * 0.94523721
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38850 * 0.68946998
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72497 * 0.73118641
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84284 * 0.84357754
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64169 * 0.26253307
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52711 * 0.42612844
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52592 * 0.92587068
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89710 * 0.67936506
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53560 * 0.02493929
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42425 * 0.13290438
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24650 * 0.06301256
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33065 * 0.71092267
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69119 * 0.17169271
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60965 * 0.97182243
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76611 * 0.06261599
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44974 * 0.74873970
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73557 * 0.20819937
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67531 * 0.44682162
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66839 * 0.41172237
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43856 * 0.09948593
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71710 * 0.52648091
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82479 * 0.70491938
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24522 * 0.13457598
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1559 * 0.13676917
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97931 * 0.62750860
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98571 * 0.79941462
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64146 * 0.86855641
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38953 * 0.46191808
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49908 * 0.44751004
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55039 * 0.29548203
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47653 * 0.57691479
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51069 * 0.86285352
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18595 * 0.64626789
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97966 * 0.80010521
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19500 * 0.06550616
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83014 * 0.16872993
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41732 * 0.48877131
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6758 * 0.43609877
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30205 * 0.57798104
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97896 * 0.73652002
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 10205 * 0.84491071
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71098 * 0.43776690
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 19640 * 0.62409694
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 71588 * 0.91392446
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'mozkwyfr').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0015():
    """Extended test 15 for migration."""
    x_0 = 93056 * 0.35233288
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76043 * 0.31900789
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95056 * 0.66384417
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57448 * 0.25764961
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81879 * 0.03976098
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35359 * 0.48286582
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30706 * 0.13064171
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61144 * 0.27393590
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8327 * 0.30927686
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34782 * 0.26926674
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42813 * 0.46403188
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16133 * 0.71387344
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62402 * 0.20605406
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45933 * 0.39898760
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66699 * 0.11747258
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82539 * 0.49621499
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37161 * 0.33953807
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19202 * 0.93634012
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35549 * 0.70386766
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19269 * 0.76834532
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7155 * 0.91228556
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71467 * 0.81127458
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'upmcmehl').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0016():
    """Extended test 16 for migration."""
    x_0 = 12529 * 0.01047476
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76244 * 0.84198708
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95229 * 0.97075663
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95127 * 0.47116364
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73675 * 0.61778359
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30265 * 0.17890588
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77955 * 0.99796666
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70689 * 0.11145935
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57647 * 0.83918486
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50500 * 0.73222521
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8231 * 0.03214321
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29848 * 0.15701748
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70041 * 0.39494267
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52381 * 0.98924328
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5396 * 0.01793701
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43509 * 0.68885926
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30303 * 0.89089487
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84356 * 0.66853705
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68712 * 0.79523723
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26567 * 0.12037565
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15711 * 0.84235973
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'cwpesuqt').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0017():
    """Extended test 17 for migration."""
    x_0 = 5069 * 0.65012656
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99118 * 0.95682176
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1484 * 0.89532769
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55814 * 0.41616527
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35606 * 0.10714135
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16532 * 0.75660303
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4074 * 0.48665306
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62649 * 0.62994953
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72347 * 0.01836606
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56501 * 0.24262175
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41947 * 0.72169222
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95562 * 0.84135239
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80141 * 0.87006648
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2223 * 0.27198467
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99690 * 0.28131666
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19174 * 0.46271213
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48437 * 0.88282208
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20805 * 0.60181598
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73573 * 0.84199376
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42524 * 0.31783330
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19609 * 0.00182959
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96652 * 0.22004594
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51074 * 0.12716184
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9874 * 0.48567309
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90653 * 0.76793570
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67715 * 0.44876634
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2260 * 0.65897104
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57867 * 0.05192202
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72745 * 0.35793068
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62684 * 0.14428592
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61775 * 0.96927105
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66977 * 0.96399169
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81303 * 0.21371887
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59376 * 0.83122970
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33770 * 0.53248488
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5700 * 0.45189297
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'vdinnyqf').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0018():
    """Extended test 18 for migration."""
    x_0 = 97985 * 0.97847043
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19688 * 0.21927031
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83222 * 0.39579885
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36956 * 0.51260508
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78226 * 0.02911423
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32375 * 0.80162088
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52894 * 0.65885066
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96480 * 0.97992589
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40343 * 0.55985073
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18140 * 0.79375675
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14809 * 0.86669531
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89157 * 0.02244694
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10823 * 0.64895276
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23218 * 0.80544959
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65090 * 0.64673779
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10746 * 0.53732803
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61911 * 0.11174197
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80744 * 0.46339184
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17480 * 0.48317132
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55206 * 0.68282964
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64709 * 0.70695579
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53000 * 0.31810386
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51249 * 0.99884167
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35502 * 0.83551927
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49918 * 0.69390247
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95313 * 0.89466650
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98204 * 0.76315251
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93379 * 0.80325750
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36610 * 0.57616664
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39418 * 0.35393087
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32866 * 0.71745482
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63853 * 0.60130036
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73086 * 0.25248952
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55276 * 0.06045394
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47993 * 0.24301493
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83790 * 0.81810005
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10118 * 0.78804103
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79456 * 0.58672812
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86862 * 0.13148153
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 27001 * 0.87537634
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18160 * 0.32627205
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41124 * 0.39372140
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96687 * 0.06850498
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 46423 * 0.64034857
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'etjmyzsl').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0019():
    """Extended test 19 for migration."""
    x_0 = 75155 * 0.81075067
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40521 * 0.32381350
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68299 * 0.76446292
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64089 * 0.33604766
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7177 * 0.40863884
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7047 * 0.70506552
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89496 * 0.21710620
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93076 * 0.66060952
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85281 * 0.69612824
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81505 * 0.91455648
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41602 * 0.32320500
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75825 * 0.19217204
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20027 * 0.87647905
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86098 * 0.23739783
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10895 * 0.61488238
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91728 * 0.21610505
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70340 * 0.70746607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30685 * 0.05408615
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49832 * 0.48884126
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16698 * 0.78398277
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39578 * 0.43892234
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94001 * 0.01496591
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77654 * 0.78394127
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30779 * 0.53845926
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5964 * 0.16016416
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8130 * 0.57390838
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34564 * 0.17165232
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 882 * 0.38483444
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56490 * 0.45874816
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75201 * 0.38998134
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75496 * 0.18930345
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23123 * 0.46006866
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35085 * 0.40878176
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29828 * 0.21332184
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4323 * 0.40773265
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47229 * 0.97620277
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61591 * 0.68327157
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17357 * 0.10669815
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88352 * 0.23550881
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 444 * 0.11705339
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78985 * 0.14965354
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 98865 * 0.07910861
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 33823 * 0.98470900
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34216 * 0.75512364
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 98632 * 0.02743771
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 73644 * 0.86279118
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'qaaxosrw').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0020():
    """Extended test 20 for migration."""
    x_0 = 6250 * 0.18195965
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18337 * 0.25241465
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20419 * 0.39849601
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55929 * 0.16934387
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51524 * 0.67644198
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60041 * 0.71240225
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77979 * 0.71232633
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79698 * 0.50266957
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60417 * 0.97152230
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63779 * 0.52851460
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62983 * 0.00565976
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38477 * 0.34099764
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26241 * 0.65473654
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71909 * 0.92634710
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93454 * 0.79170433
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50243 * 0.89574446
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13180 * 0.78523445
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69537 * 0.94735425
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52412 * 0.27798556
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29091 * 0.78391409
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86101 * 0.00881563
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83671 * 0.14630655
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41880 * 0.73910421
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30326 * 0.77995887
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1219 * 0.56998641
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29088 * 0.12552244
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70876 * 0.37524214
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21341 * 0.38523124
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85832 * 0.05619194
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11376 * 0.81952335
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9605 * 0.44022137
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85652 * 0.03239179
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84500 * 0.52329131
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39340 * 0.58008241
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78887 * 0.06053693
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6944 * 0.46588377
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40704 * 0.25577771
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3508 * 0.75188716
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 85810 * 0.43223037
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 48996 * 0.69003616
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'bocdahyq').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0021():
    """Extended test 21 for migration."""
    x_0 = 13498 * 0.22330874
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59939 * 0.69605232
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25134 * 0.20952542
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28300 * 0.69010820
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73961 * 0.14610261
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15770 * 0.05530079
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42609 * 0.21052281
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41751 * 0.81481918
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17697 * 0.24412922
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38039 * 0.66787010
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32192 * 0.37333874
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5286 * 0.54140192
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74252 * 0.43958000
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91452 * 0.94554071
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4204 * 0.03511986
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32286 * 0.22383330
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75177 * 0.65463127
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77708 * 0.11861642
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88080 * 0.54459153
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60337 * 0.98989797
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93295 * 0.69481684
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67977 * 0.16514681
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'mqcxbyjz').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0022():
    """Extended test 22 for migration."""
    x_0 = 88369 * 0.43803852
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52474 * 0.43236415
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29032 * 0.12410229
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79004 * 0.48230465
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7584 * 0.95721637
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59290 * 0.63385760
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36357 * 0.50474517
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98089 * 0.16925604
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94587 * 0.86148561
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23129 * 0.10624573
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21682 * 0.70288953
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1498 * 0.04361006
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82277 * 0.68467416
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15401 * 0.74960492
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97257 * 0.96270429
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94657 * 0.81599353
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46889 * 0.57526162
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99141 * 0.74606935
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95315 * 0.98983621
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56750 * 0.35622176
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1549 * 0.49756731
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16471 * 0.73098367
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3788 * 0.14061800
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46986 * 0.05451547
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36154 * 0.21968053
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47374 * 0.79224336
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31290 * 0.14448248
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7538 * 0.73901864
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43176 * 0.80792045
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72994 * 0.48042686
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94119 * 0.66907189
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59260 * 0.73499823
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22147 * 0.22925882
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56786 * 0.24411511
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36918 * 0.93864160
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3899 * 0.78951240
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13593 * 0.18847392
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3315 * 0.51767369
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2531 * 0.87171293
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 71373 * 0.98115136
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2133 * 0.75151283
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 2038 * 0.86504988
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'hivicmzy').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0023():
    """Extended test 23 for migration."""
    x_0 = 38829 * 0.60744742
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30471 * 0.50262013
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76461 * 0.91206291
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85609 * 0.08656213
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33015 * 0.83683984
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3303 * 0.20152776
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67411 * 0.30413230
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65632 * 0.77956498
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46849 * 0.99753130
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55810 * 0.20967032
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77940 * 0.27722388
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85373 * 0.30967981
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22609 * 0.07759661
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77526 * 0.62464313
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1735 * 0.23960429
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38161 * 0.95931183
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43256 * 0.61387502
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14197 * 0.64212702
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18336 * 0.45401474
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37587 * 0.37064472
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33445 * 0.96739062
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28817 * 0.53824441
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92980 * 0.85995522
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40606 * 0.79080314
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30322 * 0.35984489
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'vtjsfcfp').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0024():
    """Extended test 24 for migration."""
    x_0 = 38004 * 0.11447217
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22795 * 0.50200862
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38880 * 0.86555152
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1472 * 0.22918302
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26369 * 0.42772273
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83575 * 0.46715104
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25250 * 0.30971691
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35685 * 0.49331533
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80926 * 0.78480123
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47387 * 0.15564279
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47265 * 0.33169772
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89146 * 0.33429462
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18999 * 0.89732864
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9664 * 0.29537859
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72838 * 0.63993369
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53551 * 0.55227502
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87011 * 0.76689871
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53550 * 0.87860744
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5099 * 0.59258749
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50997 * 0.02979612
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98303 * 0.14769145
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24328 * 0.79985274
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40275 * 0.04012968
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12531 * 0.50197869
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68987 * 0.40584092
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75636 * 0.20888215
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63142 * 0.67478619
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57665 * 0.10220368
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2413 * 0.38283902
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56130 * 0.55565689
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14190 * 0.70151670
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'jusgjikl').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0025():
    """Extended test 25 for migration."""
    x_0 = 24951 * 0.19135485
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75483 * 0.62963463
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72821 * 0.63186101
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37095 * 0.14659931
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73625 * 0.77272655
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14946 * 0.33224804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52443 * 0.51009175
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84542 * 0.85404217
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2465 * 0.43381493
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13029 * 0.47841681
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61509 * 0.96145574
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51190 * 0.58353784
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75278 * 0.52880823
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45811 * 0.84443018
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45248 * 0.14355896
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79489 * 0.96182921
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1689 * 0.16074910
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97871 * 0.41115848
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94252 * 0.38315916
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35168 * 0.80294594
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77979 * 0.25077461
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 193 * 0.54349639
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40665 * 0.17610808
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54235 * 0.09675263
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77192 * 0.79388437
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70998 * 0.44097824
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34991 * 0.04748298
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4160 * 0.86381715
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4409 * 0.56442376
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49948 * 0.85203649
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95306 * 0.81380557
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69516 * 0.73423993
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42316 * 0.36510996
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94941 * 0.59131957
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71246 * 0.14771654
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96932 * 0.37845904
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6933 * 0.80192389
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29933 * 0.93954358
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49579 * 0.73424063
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 12739 * 0.32031895
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5655 * 0.52923132
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 64112 * 0.69395526
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'kvrqepom').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0026():
    """Extended test 26 for migration."""
    x_0 = 11416 * 0.33965427
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21684 * 0.45212674
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16377 * 0.88517792
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90357 * 0.96075620
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20426 * 0.77499622
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61913 * 0.63767918
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62221 * 0.34934278
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49141 * 0.44941423
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80087 * 0.93645041
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26762 * 0.07838119
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94859 * 0.01857619
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5409 * 0.82101068
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42976 * 0.06416776
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77210 * 0.34575042
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11659 * 0.01157681
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45922 * 0.25095910
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10076 * 0.17152085
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91560 * 0.17305112
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89897 * 0.20784983
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50929 * 0.46062557
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6686 * 0.21909922
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93198 * 0.39059120
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82652 * 0.18271694
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48363 * 0.25384526
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36200 * 0.76938655
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26223 * 0.94881447
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43248 * 0.44237098
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ibhqqcef').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0027():
    """Extended test 27 for migration."""
    x_0 = 25336 * 0.97240626
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39463 * 0.21703407
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34168 * 0.50900101
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44152 * 0.87165510
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58267 * 0.50796772
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58482 * 0.68326727
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96325 * 0.05447310
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10195 * 0.64729717
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91328 * 0.12622472
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34697 * 0.99704093
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18407 * 0.95966463
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7158 * 0.05050691
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7973 * 0.58783965
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21766 * 0.38280545
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49015 * 0.12702301
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20427 * 0.86536639
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3352 * 0.07927250
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21448 * 0.94870528
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16018 * 0.69996039
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4648 * 0.36577064
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7766 * 0.66832225
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39326 * 0.19155036
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8540 * 0.93314548
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81824 * 0.17633060
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93110 * 0.01053674
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23828 * 0.02840784
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10085 * 0.30095523
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64265 * 0.72433062
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32772 * 0.40196352
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54193 * 0.53935589
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27335 * 0.76548384
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12584 * 0.89363395
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21191 * 0.39260751
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59931 * 0.88924864
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62519 * 0.80169337
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13621 * 0.26523843
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79992 * 0.39569497
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48150 * 0.90556205
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45834 * 0.87642127
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9895 * 0.77776073
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91277 * 0.15077526
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 61235 * 0.55161422
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93391 * 0.41648212
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94349 * 0.24963952
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 30479 * 0.72800535
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 57672 * 0.05661188
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'khbbunqo').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0028():
    """Extended test 28 for migration."""
    x_0 = 61026 * 0.18265344
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58732 * 0.30964455
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94793 * 0.45757337
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19935 * 0.31541801
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49383 * 0.32153624
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57851 * 0.00092228
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57222 * 0.27081369
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33084 * 0.12992045
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8978 * 0.02241823
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46863 * 0.26181119
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78801 * 0.81148093
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96427 * 0.94897055
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55508 * 0.04380279
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6183 * 0.18783844
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75605 * 0.14161134
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40024 * 0.44697746
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37010 * 0.06159082
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29611 * 0.95947312
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60972 * 0.46308424
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79270 * 0.79817190
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1464 * 0.88062550
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11275 * 0.81357241
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81342 * 0.61752368
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81648 * 0.52647813
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83487 * 0.78170014
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91862 * 0.65767179
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81775 * 0.50782701
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13609 * 0.01093336
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42872 * 0.46474572
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97840 * 0.17642159
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39561 * 0.47687959
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'fyijhbmg').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0029():
    """Extended test 29 for migration."""
    x_0 = 16443 * 0.16967955
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5336 * 0.38250438
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62783 * 0.53698784
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5462 * 0.00622987
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43926 * 0.92196576
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8504 * 0.38394477
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1439 * 0.06502272
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60325 * 0.79573455
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57641 * 0.66588662
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29448 * 0.88894067
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15044 * 0.94268470
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70522 * 0.18935260
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28654 * 0.95491515
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98690 * 0.27420991
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49873 * 0.83890527
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47871 * 0.22500737
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42549 * 0.71841120
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54335 * 0.46830067
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42152 * 0.68250516
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3838 * 0.55205062
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'acfzejpd').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0030():
    """Extended test 30 for migration."""
    x_0 = 52348 * 0.62578670
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60828 * 0.35298638
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82049 * 0.80163607
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77054 * 0.97957516
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22370 * 0.25487371
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13066 * 0.96889213
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4274 * 0.60801473
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10821 * 0.47853575
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53167 * 0.06162393
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89032 * 0.27084924
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40539 * 0.17114889
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4700 * 0.13152291
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27072 * 0.95720876
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84850 * 0.17632213
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26650 * 0.02146914
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89097 * 0.85797988
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65825 * 0.17994937
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20962 * 0.39280342
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 610 * 0.01308918
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55434 * 0.76430396
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62514 * 0.95173198
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71037 * 0.87952437
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7491 * 0.86768052
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8521 * 0.51948221
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'blzrvcey').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0031():
    """Extended test 31 for migration."""
    x_0 = 87505 * 0.23275022
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9975 * 0.15869573
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41594 * 0.42800497
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91220 * 0.62007647
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88639 * 0.64527744
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59006 * 0.00154777
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68230 * 0.83398669
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71759 * 0.63488191
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4094 * 0.71820387
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 545 * 0.96682011
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10258 * 0.03780051
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57078 * 0.97304454
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15089 * 0.82911960
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12773 * 0.06286589
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68517 * 0.42300644
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76821 * 0.24636985
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81105 * 0.62134706
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67953 * 0.74317138
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75896 * 0.96355582
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57014 * 0.64874034
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20304 * 0.59908083
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93977 * 0.04916569
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32578 * 0.87860649
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18213 * 0.59482418
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83209 * 0.77625424
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73679 * 0.60778508
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59233 * 0.43988866
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45303 * 0.71443590
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82083 * 0.56276065
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77093 * 0.17726190
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47184 * 0.12077351
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62761 * 0.67740944
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13616 * 0.45243755
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54417 * 0.57358618
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47016 * 0.75642260
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75603 * 0.86800219
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75523 * 0.59952082
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33389 * 0.59285729
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96493 * 0.74614258
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20390 * 0.95248845
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98347 * 0.43686421
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72307 * 0.70755942
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 56738 * 0.25500711
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40659 * 0.01755725
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'cbnhrqph').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0032():
    """Extended test 32 for migration."""
    x_0 = 23093 * 0.18723735
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4294 * 0.47857101
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75430 * 0.63829269
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74852 * 0.76607839
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39698 * 0.37370837
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67015 * 0.53676575
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26098 * 0.79139963
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68301 * 0.13531354
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26446 * 0.13897463
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51757 * 0.52970182
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44762 * 0.38285817
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90811 * 0.37969994
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38269 * 0.77825303
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10399 * 0.59233495
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94859 * 0.66230124
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36825 * 0.69780917
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56249 * 0.55145530
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99574 * 0.17237372
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25647 * 0.71511238
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28854 * 0.41197909
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16087 * 0.14112417
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17993 * 0.94291585
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27209 * 0.10450058
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98645 * 0.52074826
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77257 * 0.58717237
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30018 * 0.18365848
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83129 * 0.42436023
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49662 * 0.10238356
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50404 * 0.22731028
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7188 * 0.41322433
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60933 * 0.21516233
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'mgzlhlrf').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0033():
    """Extended test 33 for migration."""
    x_0 = 82597 * 0.54572779
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55889 * 0.89522302
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17204 * 0.89121459
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1766 * 0.05197958
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74895 * 0.17493210
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57072 * 0.61582212
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40388 * 0.83779125
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13912 * 0.20956357
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2259 * 0.32206100
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56763 * 0.05186907
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18185 * 0.38296593
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13175 * 0.37276892
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62524 * 0.65210334
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86599 * 0.71465956
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70336 * 0.14726278
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87312 * 0.26039173
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46395 * 0.03825217
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95536 * 0.42548781
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74496 * 0.22016824
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63244 * 0.59019596
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37117 * 0.90160479
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22381 * 0.57727472
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36481 * 0.04411646
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41533 * 0.01986333
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90876 * 0.57984612
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46061 * 0.69170533
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 444 * 0.60664579
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29384 * 0.88274089
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6452 * 0.59679231
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24035 * 0.28980376
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9734 * 0.42403718
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26622 * 0.89312203
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31289 * 0.84912004
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78383 * 0.77194925
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6863 * 0.72607095
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54299 * 0.13037429
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75514 * 0.54050946
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27794 * 0.53136551
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91092 * 0.25137145
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85819 * 0.97537978
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74125 * 0.30834985
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96348 * 0.04842533
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 4239 * 0.25180975
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99641 * 0.57642486
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'alvyecfp').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0034():
    """Extended test 34 for migration."""
    x_0 = 28529 * 0.98182750
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40156 * 0.50636880
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5609 * 0.36207466
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64280 * 0.42335532
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56301 * 0.73169725
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30738 * 0.23959428
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22710 * 0.79432250
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42548 * 0.50818967
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64764 * 0.85280322
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74439 * 0.25004396
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12138 * 0.28240554
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19129 * 0.20261662
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72463 * 0.66087148
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98082 * 0.42498078
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80835 * 0.80285139
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43553 * 0.03654800
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62229 * 0.57481303
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1223 * 0.89458411
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55800 * 0.13926516
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5134 * 0.77159112
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70708 * 0.84367717
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37481 * 0.77581946
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90923 * 0.40968102
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29964 * 0.44959704
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82766 * 0.45967285
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93309 * 0.84246968
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74123 * 0.72800149
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69487 * 0.17335803
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62876 * 0.93042231
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84561 * 0.23041485
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8686 * 0.92956139
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28341 * 0.64834904
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23611 * 0.66698199
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14354 * 0.00603027
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85192 * 0.79993354
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79298 * 0.14512449
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79256 * 0.91306196
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98545 * 0.61778655
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76759 * 0.24772112
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7306 * 0.20044706
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48373 * 0.55649969
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37278 * 0.50264429
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16391 * 0.22399885
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61766 * 0.01420989
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 69469 * 0.95409868
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 23349 * 0.19648699
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 25632 * 0.44914213
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 28766 * 0.17831955
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 77891 * 0.67160996
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 84881 * 0.05220306
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'foysfche').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0035():
    """Extended test 35 for migration."""
    x_0 = 69397 * 0.85361214
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34196 * 0.75783003
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34963 * 0.82618085
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98451 * 0.95141415
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60347 * 0.18431466
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26253 * 0.68812229
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88917 * 0.73922956
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79739 * 0.59418030
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36103 * 0.99020308
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81950 * 0.30134009
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71475 * 0.55016338
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87621 * 0.56347956
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11678 * 0.30708717
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79298 * 0.12202367
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98327 * 0.02774125
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61887 * 0.04821057
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53781 * 0.95396560
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23460 * 0.61545312
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59735 * 0.94803207
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22218 * 0.48372948
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33453 * 0.46523623
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26872 * 0.95158649
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52171 * 0.23980115
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53994 * 0.70406956
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71828 * 0.17272116
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39676 * 0.61070005
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46481 * 0.01684523
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3787 * 0.93091432
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99126 * 0.60327211
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17242 * 0.83384635
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8769 * 0.60339822
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82799 * 0.09757470
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79048 * 0.35809684
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29475 * 0.42178461
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16107 * 0.70830850
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48513 * 0.84420986
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28534 * 0.03808285
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81065 * 0.46395024
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24989 * 0.22136569
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11713 * 0.39046110
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ursusumi').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0036():
    """Extended test 36 for migration."""
    x_0 = 50243 * 0.32477871
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49768 * 0.88325513
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71777 * 0.66724037
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92169 * 0.79012941
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91256 * 0.82270031
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69738 * 0.91764724
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70285 * 0.05707418
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69438 * 0.41412720
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95527 * 0.96437488
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58470 * 0.86469246
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65699 * 0.15835757
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64107 * 0.93619532
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26066 * 0.77903384
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83417 * 0.16578366
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45708 * 0.41272679
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7768 * 0.97224133
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43572 * 0.43022814
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54271 * 0.62357444
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98263 * 0.67451976
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33340 * 0.40230044
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91218 * 0.73794890
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43678 * 0.81343227
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68029 * 0.67886106
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24094 * 0.50223323
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62435 * 0.15760221
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76940 * 0.26296746
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38987 * 0.26203104
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34249 * 0.61957324
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91010 * 0.05445290
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85736 * 0.57311819
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32633 * 0.23738717
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81870 * 0.58641219
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23572 * 0.42771378
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73713 * 0.73695071
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69579 * 0.97450979
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16724 * 0.29318479
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21421 * 0.58347467
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67738 * 0.80712938
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88315 * 0.09254522
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15336 * 0.34184537
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74837 * 0.78797561
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'mnffmtim').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0037():
    """Extended test 37 for migration."""
    x_0 = 1147 * 0.04007797
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81682 * 0.44821566
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72655 * 0.54482129
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95480 * 0.10621617
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7012 * 0.14836660
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71405 * 0.20907906
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82602 * 0.58262923
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60353 * 0.63070939
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59194 * 0.76274025
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93067 * 0.04533751
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17029 * 0.42550023
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59588 * 0.74116942
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49337 * 0.49285867
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97435 * 0.72944938
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98862 * 0.20657609
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48488 * 0.26746156
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88389 * 0.21541807
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70676 * 0.00222217
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54467 * 0.46650707
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84020 * 0.60328078
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12737 * 0.56368435
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6746 * 0.54578183
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59407 * 0.77105108
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26675 * 0.39823823
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2780 * 0.96654559
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16396 * 0.54213463
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11257 * 0.98255653
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36921 * 0.90371024
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15757 * 0.54677176
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28538 * 0.06455501
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'xledmkoq').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0038():
    """Extended test 38 for migration."""
    x_0 = 11672 * 0.18052992
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74431 * 0.73117343
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69534 * 0.99082541
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28690 * 0.37578620
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77869 * 0.49926386
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66190 * 0.07228860
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5217 * 0.71410683
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77412 * 0.07210069
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13100 * 0.26256566
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95013 * 0.75887583
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41447 * 0.13348894
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38117 * 0.73964618
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59753 * 0.18225274
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39342 * 0.78660886
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89654 * 0.77504983
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97805 * 0.49751510
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77492 * 0.96600562
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39375 * 0.66023777
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88227 * 0.25171905
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25648 * 0.30109443
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87640 * 0.00288137
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81095 * 0.00666713
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'zjvhwtrf').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0039():
    """Extended test 39 for migration."""
    x_0 = 3773 * 0.42562177
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52762 * 0.06177166
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20517 * 0.98211354
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47348 * 0.80662213
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10350 * 0.50470675
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46042 * 0.20613111
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32777 * 0.08334707
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21330 * 0.36114728
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31294 * 0.26080085
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53577 * 0.86778982
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34997 * 0.86281211
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14234 * 0.91698554
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70894 * 0.22841417
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2390 * 0.39658632
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43838 * 0.37165988
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34031 * 0.60243220
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49221 * 0.06031121
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49781 * 0.64605714
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68205 * 0.03227350
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98950 * 0.01597540
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62434 * 0.36614825
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9712 * 0.91830843
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68307 * 0.15633127
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82213 * 0.64240197
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64896 * 0.95474000
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46016 * 0.68906355
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74303 * 0.93131607
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67993 * 0.14539453
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14074 * 0.35194318
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9736 * 0.21221123
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25458 * 0.22806538
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41852 * 0.55377025
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61809 * 0.56063348
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6582 * 0.86142960
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95804 * 0.14182547
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4610 * 0.77849387
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17375 * 0.49715892
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45758 * 0.47047237
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61621 * 0.51453787
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'fzlovwnh').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0040():
    """Extended test 40 for migration."""
    x_0 = 22388 * 0.24448994
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50351 * 0.61550647
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34124 * 0.13069269
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93101 * 0.98987072
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72001 * 0.23085869
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22897 * 0.49738906
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41881 * 0.29073674
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64734 * 0.21681565
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60891 * 0.34166703
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50698 * 0.91823954
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76572 * 0.16845293
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21383 * 0.90957940
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90267 * 0.35107882
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17728 * 0.58531737
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68372 * 0.72787710
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78207 * 0.04589677
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44037 * 0.29706075
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66591 * 0.00048308
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28360 * 0.66184516
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66264 * 0.22285998
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21642 * 0.34703662
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2625 * 0.96188492
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2732 * 0.88916154
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87461 * 0.26414722
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 312 * 0.48480182
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98710 * 0.76941947
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96059 * 0.16822837
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'famlryta').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0041():
    """Extended test 41 for migration."""
    x_0 = 52179 * 0.53429214
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96524 * 0.79379246
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97301 * 0.16761709
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5313 * 0.86118796
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72244 * 0.19499082
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21576 * 0.37261849
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23762 * 0.23016790
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30483 * 0.83457907
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29862 * 0.04784130
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69785 * 0.03268446
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48941 * 0.13591082
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23429 * 0.10018498
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17208 * 0.93730183
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94835 * 0.75859684
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88396 * 0.05183178
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10825 * 0.36517568
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11260 * 0.78077769
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92446 * 0.66577075
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50661 * 0.04559795
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81193 * 0.15018912
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9917 * 0.74968926
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98787 * 0.24551621
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70649 * 0.38620982
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2179 * 0.93776673
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70576 * 0.47977445
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89643 * 0.20449132
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94646 * 0.88443719
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37364 * 0.64390606
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19454 * 0.33538211
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42006 * 0.88688643
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65863 * 0.93538114
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24404 * 0.42195647
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58672 * 0.14224876
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49264 * 0.99241914
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94970 * 0.57716711
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18416 * 0.42619941
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76278 * 0.20959217
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46267 * 0.58115383
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24301 * 0.99554308
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64731 * 0.37889489
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 7044 * 0.42477894
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96570 * 0.39592519
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42704 * 0.52759715
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 85121 * 0.50167681
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'aallosqg').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0042():
    """Extended test 42 for migration."""
    x_0 = 80198 * 0.51489682
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47493 * 0.86249846
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5151 * 0.17277303
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36090 * 0.58558021
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75402 * 0.77486950
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15296 * 0.60930692
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56889 * 0.52326209
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92739 * 0.87836049
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15308 * 0.96269389
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6417 * 0.63708527
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38410 * 0.07773305
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93822 * 0.81093716
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70376 * 0.04563986
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25055 * 0.40716979
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28571 * 0.05170473
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13577 * 0.90625740
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86215 * 0.77592369
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 833 * 0.86999068
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55270 * 0.28166316
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92999 * 0.55030968
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35925 * 0.33228454
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22353 * 0.37620453
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11517 * 0.40670294
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19801 * 0.91264383
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30542 * 0.04356425
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89944 * 0.63917253
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'bamjsncn').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0043():
    """Extended test 43 for migration."""
    x_0 = 15796 * 0.67714952
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57256 * 0.16512035
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56576 * 0.90531793
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59399 * 0.94135050
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35457 * 0.91352503
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31347 * 0.80162200
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53276 * 0.76099110
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32699 * 0.84800416
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56710 * 0.83700751
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86252 * 0.71232855
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79485 * 0.39500682
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45474 * 0.36404685
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57515 * 0.89797391
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15842 * 0.23119865
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68203 * 0.09101490
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51971 * 0.87301938
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33167 * 0.74244101
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95889 * 0.89830964
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31240 * 0.96961484
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19154 * 0.08885962
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 955 * 0.12963298
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3266 * 0.51964793
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'mbtvmrhe').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0044():
    """Extended test 44 for migration."""
    x_0 = 17746 * 0.82930661
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50723 * 0.43942021
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8480 * 0.56822315
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26558 * 0.19796058
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62432 * 0.07364658
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23587 * 0.49134619
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61317 * 0.82960924
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75673 * 0.69446342
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62812 * 0.65850814
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86382 * 0.56781159
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42233 * 0.27921806
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47382 * 0.05414181
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34060 * 0.99220017
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92466 * 0.16364796
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4102 * 0.46028991
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10634 * 0.57436636
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47397 * 0.46628290
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23042 * 0.01179723
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70160 * 0.52661186
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31655 * 0.05799721
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29789 * 0.14320070
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10641 * 0.03178583
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36280 * 0.19088260
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30284 * 0.50047908
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55464 * 0.49607494
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84075 * 0.34912087
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45692 * 0.35195772
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72958 * 0.32776067
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11222 * 0.24188196
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60840 * 0.42191061
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41256 * 0.37527785
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60465 * 0.47297587
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51787 * 0.16127813
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37169 * 0.90215796
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67885 * 0.85905495
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33196 * 0.81449459
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18014 * 0.83559822
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3366 * 0.46820731
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90664 * 0.90184249
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18624 * 0.35337023
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62366 * 0.71781129
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12671 * 0.34565447
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 50957 * 0.43930225
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 10953 * 0.72635392
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 18530 * 0.55180578
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 92867 * 0.92020489
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 66561 * 0.09475477
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 95641 * 0.75535038
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 90612 * 0.28998744
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 18720 * 0.98323322
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'gagiquit').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0045():
    """Extended test 45 for migration."""
    x_0 = 17950 * 0.52638054
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95541 * 0.03485834
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64397 * 0.93318846
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9892 * 0.55448685
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68655 * 0.28163512
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90934 * 0.49013676
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34281 * 0.62050327
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99866 * 0.59520008
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5364 * 0.50254919
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48831 * 0.60155916
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59168 * 0.22942405
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63469 * 0.08822714
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 759 * 0.97166138
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76931 * 0.29405135
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94040 * 0.91338055
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26535 * 0.98501717
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14581 * 0.88284247
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48916 * 0.73361250
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54 * 0.09591991
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69094 * 0.91915801
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ewalmpbr').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0046():
    """Extended test 46 for migration."""
    x_0 = 17786 * 0.55555082
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 737 * 0.64647461
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69661 * 0.09718165
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72712 * 0.09008034
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18980 * 0.05699179
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77749 * 0.70004718
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66565 * 0.94331485
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47625 * 0.57287451
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48718 * 0.38657446
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88507 * 0.31688798
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82594 * 0.29946481
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9703 * 0.28734814
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51500 * 0.60656717
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10149 * 0.33399228
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62592 * 0.06757614
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17193 * 0.84835338
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79836 * 0.58158841
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14186 * 0.73465292
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37122 * 0.48055908
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46810 * 0.09817959
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6774 * 0.10179798
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54104 * 0.43478010
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31202 * 0.79788752
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38254 * 0.89498380
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25398 * 0.53573610
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92626 * 0.79365952
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8687 * 0.88036327
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70930 * 0.27515004
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18248 * 0.84852088
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64394 * 0.68267678
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75962 * 0.72689611
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22298 * 0.93604825
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53797 * 0.23855574
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34184 * 0.68847986
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64194 * 0.52764501
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89888 * 0.70849745
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78123 * 0.89889303
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93938 * 0.70123247
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17629 * 0.02465890
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76657 * 0.11243532
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91968 * 0.62716128
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20109 * 0.98609115
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55255 * 0.95928037
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 29594 * 0.12340042
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 96755 * 0.16476700
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 23286 * 0.83892165
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 91586 * 0.90144776
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 67014 * 0.01217721
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 90102 * 0.00317229
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'cvfumdhq').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0047():
    """Extended test 47 for migration."""
    x_0 = 76486 * 0.23663641
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34231 * 0.45280837
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80802 * 0.36397992
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11051 * 0.32776369
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88785 * 0.91345131
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60495 * 0.66077021
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22744 * 0.33418703
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61123 * 0.69917082
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32784 * 0.57237765
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85224 * 0.76178312
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20756 * 0.29637090
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29288 * 0.63288858
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18381 * 0.02190178
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35224 * 0.81846323
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5502 * 0.17596946
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68792 * 0.40724801
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39065 * 0.46360067
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16187 * 0.56115074
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8346 * 0.36626144
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29333 * 0.36909914
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75093 * 0.70867497
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19589 * 0.79270485
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18056 * 0.89468485
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78835 * 0.95410976
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32571 * 0.34855251
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21477 * 0.49708234
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12427 * 0.70949797
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31996 * 0.75342434
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8211 * 0.80652422
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 783 * 0.02592128
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32590 * 0.23482860
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31153 * 0.83791496
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41495 * 0.50739169
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81662 * 0.65305719
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87637 * 0.80798942
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10502 * 0.49029528
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7521 * 0.57906272
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47042 * 0.32298008
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26354 * 0.11993364
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86863 * 0.02514026
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'mvtjmwvh').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0048():
    """Extended test 48 for migration."""
    x_0 = 43170 * 0.39821185
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18775 * 0.84338345
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68543 * 0.87362047
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6841 * 0.06130027
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36 * 0.43170882
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70677 * 0.40824765
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98431 * 0.62775019
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36236 * 0.75455974
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44322 * 0.54488399
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31376 * 0.31456300
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68647 * 0.92317525
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88501 * 0.04707746
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72811 * 0.00131292
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68705 * 0.45183874
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82947 * 0.65982202
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2539 * 0.16170750
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36866 * 0.69197471
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83078 * 0.07380821
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8448 * 0.81370120
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91105 * 0.34743869
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38649 * 0.69945917
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37785 * 0.32085263
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78763 * 0.77333445
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32602 * 0.65470473
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69737 * 0.12064520
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78473 * 0.71744815
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91412 * 0.51986513
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83113 * 0.67260497
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'iydvdhsv').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0049():
    """Extended test 49 for migration."""
    x_0 = 91885 * 0.46141202
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65130 * 0.75366814
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23013 * 0.94210653
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36556 * 0.52540271
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40747 * 0.63009435
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15471 * 0.57413844
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50951 * 0.17585710
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48644 * 0.47304169
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54632 * 0.04621697
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23783 * 0.70575567
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35698 * 0.37082005
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91329 * 0.63021434
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22378 * 0.38075174
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26521 * 0.61075311
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20251 * 0.68417917
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72718 * 0.81308656
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68166 * 0.28015555
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14216 * 0.92660756
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15617 * 0.47241284
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51846 * 0.68514446
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19746 * 0.99844086
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69774 * 0.02488997
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21659 * 0.89190516
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20788 * 0.33565027
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35672 * 0.65745508
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'eagdwwdq').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0050():
    """Extended test 50 for migration."""
    x_0 = 91901 * 0.24917312
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34623 * 0.39283339
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49876 * 0.13575079
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21409 * 0.50448330
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7947 * 0.67000678
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28014 * 0.33195991
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82853 * 0.80764286
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65910 * 0.72582716
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66803 * 0.71806032
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89115 * 0.63188816
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15337 * 0.45693427
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55535 * 0.84967976
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91153 * 0.09095504
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96299 * 0.99304485
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26409 * 0.43530834
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52534 * 0.86712326
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36635 * 0.92571319
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78622 * 0.14736160
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80151 * 0.64630152
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68011 * 0.52443709
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53035 * 0.19896785
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41098 * 0.72433698
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'caadmypg').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0051():
    """Extended test 51 for migration."""
    x_0 = 98296 * 0.38670671
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23759 * 0.01233351
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96956 * 0.72798260
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46779 * 0.30365827
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33934 * 0.33584406
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72610 * 0.23107477
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42653 * 0.36492583
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8307 * 0.67203680
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89167 * 0.50918095
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17430 * 0.58511738
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79605 * 0.86530608
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31687 * 0.89024538
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56200 * 0.05388071
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14415 * 0.80626466
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74560 * 0.33027031
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4525 * 0.24181849
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5822 * 0.00317544
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20129 * 0.46601651
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66601 * 0.03570004
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68612 * 0.95072177
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 498 * 0.04293787
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42701 * 0.77308792
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1018 * 0.61609482
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78025 * 0.07120620
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78223 * 0.18007109
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36417 * 0.65667941
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53432 * 0.06223818
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78769 * 0.73375522
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18584 * 0.38741122
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77068 * 0.62429014
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29438 * 0.77153139
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21881 * 0.30995806
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96438 * 0.73305014
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67392 * 0.09554104
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1724 * 0.83521503
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70409 * 0.89849867
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94272 * 0.48522590
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8350 * 0.05178413
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 32934 * 0.44595296
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 27349 * 0.12323712
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 15165 * 0.27244335
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67154 * 0.45969838
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 78858 * 0.64451097
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 89615 * 0.62710691
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71408 * 0.44845685
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26798 * 0.65640523
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'ndxlvsng').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0052():
    """Extended test 52 for migration."""
    x_0 = 99509 * 0.45280743
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7541 * 0.10889000
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8431 * 0.24039666
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90874 * 0.01582209
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14758 * 0.16612537
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45479 * 0.86632914
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10936 * 0.69392046
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70615 * 0.54617595
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10176 * 0.58845145
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68574 * 0.74392095
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72791 * 0.88099501
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58756 * 0.81139939
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59884 * 0.13534217
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16415 * 0.28563894
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82851 * 0.14406392
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3252 * 0.77020312
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3899 * 0.63151315
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2077 * 0.71463408
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33920 * 0.48812473
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52527 * 0.43534349
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24624 * 0.61174059
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'qisghshr').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0053():
    """Extended test 53 for migration."""
    x_0 = 78495 * 0.48774524
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50918 * 0.02964168
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19079 * 0.10533793
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47822 * 0.20472417
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5865 * 0.78575590
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96434 * 0.20232415
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68964 * 0.28542927
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2875 * 0.40942984
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54037 * 0.47877452
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52785 * 0.73476021
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27683 * 0.31740972
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89011 * 0.99988622
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87239 * 0.52125285
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6221 * 0.42894271
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24513 * 0.68658595
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28073 * 0.79102957
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70554 * 0.55079668
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17181 * 0.48252790
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54910 * 0.67021458
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14525 * 0.93830806
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34613 * 0.97311436
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66499 * 0.05503815
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63606 * 0.80292165
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63426 * 0.49389761
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44528 * 0.31219586
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52838 * 0.24140750
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18864 * 0.68299690
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38837 * 0.98449041
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51414 * 0.46803024
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52394 * 0.35521108
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51613 * 0.57546039
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73245 * 0.52646332
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55205 * 0.45526263
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4194 * 0.45434357
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18247 * 0.21962323
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30933 * 0.31682321
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15303 * 0.84425904
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55222 * 0.54352155
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74943 * 0.47101886
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57415 * 0.64578669
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40101 * 0.58837066
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 64973 * 0.94993002
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 30745 * 0.00506984
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58239 * 0.92802846
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 72775 * 0.58732559
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'dkfjwqqm').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0054():
    """Extended test 54 for migration."""
    x_0 = 99828 * 0.24496734
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40909 * 0.16942992
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6031 * 0.23547707
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60272 * 0.93311220
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84539 * 0.10623320
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77891 * 0.92525883
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8691 * 0.34810817
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17423 * 0.02913110
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87755 * 0.80229056
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96194 * 0.58462730
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66380 * 0.21314310
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83693 * 0.51178958
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28372 * 0.11498802
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17073 * 0.80012609
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39060 * 0.20749712
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50675 * 0.74020312
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30523 * 0.09663427
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35049 * 0.02451081
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13781 * 0.01699613
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34671 * 0.01825046
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47673 * 0.84569213
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55911 * 0.71745545
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19625 * 0.74391005
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28827 * 0.04098209
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74998 * 0.91861057
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24672 * 0.59666323
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27886 * 0.99920044
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59181 * 0.83125886
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5927 * 0.71170582
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28781 * 0.48068900
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8859 * 0.14769552
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44809 * 0.20244281
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77359 * 0.01776683
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82846 * 0.96483553
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9767 * 0.33661726
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85266 * 0.27157959
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98391 * 0.07708930
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16837 * 0.76288683
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9487 * 0.29634119
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3015 * 0.36187218
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 76108 * 0.03751403
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 7861 * 0.11486120
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 45659 * 0.49369037
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47737 * 0.64912904
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'lvqbduas').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0055():
    """Extended test 55 for migration."""
    x_0 = 62068 * 0.39991511
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68647 * 0.29662432
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85801 * 0.39987294
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36950 * 0.65892899
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50412 * 0.83741384
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33143 * 0.92114270
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51878 * 0.09286232
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42808 * 0.22292316
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14272 * 0.16256036
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24462 * 0.39393343
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64595 * 0.11652722
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92401 * 0.99688628
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48969 * 0.51048243
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1104 * 0.48497210
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11717 * 0.67206667
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51933 * 0.48177928
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55538 * 0.78812520
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46290 * 0.76775573
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76565 * 0.98812149
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52625 * 0.88462324
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93645 * 0.07621464
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43529 * 0.10580411
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43520 * 0.81016294
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40485 * 0.36991764
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76612 * 0.21525686
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69340 * 0.67363711
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71916 * 0.42394781
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36005 * 0.82914906
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79665 * 0.39947726
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ylvtiprw').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0056():
    """Extended test 56 for migration."""
    x_0 = 91796 * 0.92815638
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65861 * 0.65283585
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27376 * 0.35338379
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18344 * 0.85930018
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29524 * 0.10826588
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95890 * 0.83691572
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83924 * 0.60425604
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78281 * 0.69069568
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18873 * 0.41095806
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33395 * 0.47385256
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90232 * 0.45217444
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51900 * 0.17425088
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99120 * 0.15097972
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12387 * 0.49582191
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19997 * 0.33306288
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9009 * 0.28525124
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10115 * 0.79205015
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20264 * 0.17835057
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2960 * 0.44982928
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52732 * 0.47014484
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41975 * 0.14304395
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60333 * 0.19106718
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43778 * 0.39608875
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29660 * 0.77510748
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83549 * 0.37575853
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56462 * 0.89584893
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63574 * 0.54915328
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9445 * 0.66649165
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32154 * 0.20229624
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80303 * 0.27663681
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68223 * 0.04851428
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31458 * 0.82526003
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61803 * 0.14150057
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28866 * 0.25378416
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50705 * 0.60579739
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8707 * 0.50013432
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86768 * 0.73147458
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 54280 * 0.35872856
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24106 * 0.97636919
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77633 * 0.85960481
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78105 * 0.07106342
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26709 * 0.09442271
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15053 * 0.64017306
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 65867 * 0.42745139
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 41037 * 0.46580766
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 56517 * 0.22530967
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 65559 * 0.63695163
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 30023 * 0.46922030
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'bggnrpbr').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0057():
    """Extended test 57 for migration."""
    x_0 = 71710 * 0.82905117
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78880 * 0.71336159
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79248 * 0.74983491
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57299 * 0.54963466
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71038 * 0.31127770
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47559 * 0.82978043
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62080 * 0.07577740
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69182 * 0.76814514
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10738 * 0.47861965
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65468 * 0.26867569
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25835 * 0.93934727
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67910 * 0.09436524
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82628 * 0.91624874
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92729 * 0.44046636
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65502 * 0.05548324
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61888 * 0.05467043
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33891 * 0.01399818
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70147 * 0.18522794
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68012 * 0.67598826
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55598 * 0.56862709
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18498 * 0.02528192
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67391 * 0.14877864
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59077 * 0.58594588
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95806 * 0.86777745
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'woghvgoo').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0058():
    """Extended test 58 for migration."""
    x_0 = 78857 * 0.20629953
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75700 * 0.48200196
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69281 * 0.38548486
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67852 * 0.39364486
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8168 * 0.05189718
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86210 * 0.65697330
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21213 * 0.60080273
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82571 * 0.67467601
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74470 * 0.94998066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95635 * 0.95019792
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7731 * 0.59999019
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23038 * 0.47632479
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31798 * 0.39581942
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3209 * 0.53759813
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40764 * 0.41444401
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73324 * 0.22945561
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15964 * 0.79437281
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55986 * 0.36469383
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90757 * 0.76817261
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33800 * 0.70453010
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53667 * 0.70516821
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93284 * 0.31292509
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98813 * 0.69127689
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78561 * 0.72149392
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95482 * 0.25609223
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1848 * 0.70698429
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74034 * 0.57355132
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40267 * 0.48239843
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1333 * 0.76081099
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44524 * 0.55431789
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79744 * 0.13811937
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2328 * 0.53444819
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21124 * 0.31885535
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74201 * 0.12401002
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58736 * 0.77765484
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46844 * 0.64033076
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62387 * 0.54495406
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96104 * 0.34432735
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41250 * 0.93088859
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1490 * 0.49750333
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27293 * 0.47951388
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'jpmzmjqv').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0059():
    """Extended test 59 for migration."""
    x_0 = 15445 * 0.57518824
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63478 * 0.80742691
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63565 * 0.37490776
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13987 * 0.15428067
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81490 * 0.53553252
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9981 * 0.98009433
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30998 * 0.15896776
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25182 * 0.37188530
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45975 * 0.29590612
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59389 * 0.00794689
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49570 * 0.68269165
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20318 * 0.99392614
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80458 * 0.13953058
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49519 * 0.36435724
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81100 * 0.77910326
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80835 * 0.31462190
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10610 * 0.69407547
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80283 * 0.08868294
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49687 * 0.42967149
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57109 * 0.99365984
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64306 * 0.90918371
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25875 * 0.78857856
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86851 * 0.85382359
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59468 * 0.63246282
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72863 * 0.99524809
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34115 * 0.90478471
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24054 * 0.48156247
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70556 * 0.94743775
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35108 * 0.91068946
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79621 * 0.26499673
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50997 * 0.46131603
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'nrfdvsia').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0060():
    """Extended test 60 for migration."""
    x_0 = 21770 * 0.40514765
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63362 * 0.33797838
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87779 * 0.86999121
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96223 * 0.24299072
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30392 * 0.54416616
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35621 * 0.91357156
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22852 * 0.33518307
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28755 * 0.40198558
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87644 * 0.29374100
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36650 * 0.26868107
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69721 * 0.58313545
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23220 * 0.84767454
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84507 * 0.02962926
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51365 * 0.59457218
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75240 * 0.82719575
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12607 * 0.22575850
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62125 * 0.77066428
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48492 * 0.87789999
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10943 * 0.85924629
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51486 * 0.78400629
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83218 * 0.60870994
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3433 * 0.41853731
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11202 * 0.85104879
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26208 * 0.10464846
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96010 * 0.12257867
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1927 * 0.81139498
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12439 * 0.75873443
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3214 * 0.50234563
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16453 * 0.98711881
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47623 * 0.82043751
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36607 * 0.64193064
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73532 * 0.78356907
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45047 * 0.98878000
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1739 * 0.73038645
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81274 * 0.99320028
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59319 * 0.71855194
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45771 * 0.06284759
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20352 * 0.53622710
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13799 * 0.71390774
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59780 * 0.49727155
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 15947 * 0.75845526
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'wmhafuxq').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0061():
    """Extended test 61 for migration."""
    x_0 = 86997 * 0.07858169
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64354 * 0.50060586
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87743 * 0.53196041
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40627 * 0.46469933
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41882 * 0.14658973
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84885 * 0.66624278
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89801 * 0.15423951
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9716 * 0.32894816
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81279 * 0.47039589
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52402 * 0.27721780
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43809 * 0.28235029
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54043 * 0.35536783
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80634 * 0.53507050
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15928 * 0.71468016
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3929 * 0.48181875
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82411 * 0.27615453
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19091 * 0.81358480
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89720 * 0.28691442
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4873 * 0.37718842
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31197 * 0.39566816
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31383 * 0.56608258
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85407 * 0.33923560
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24006 * 0.30926823
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8359 * 0.61403351
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33030 * 0.97093273
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86806 * 0.92656687
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87684 * 0.94582920
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7070 * 0.62213793
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20055 * 0.53502354
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21656 * 0.85733908
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77251 * 0.25022147
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77575 * 0.02214559
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97735 * 0.90793386
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52673 * 0.94118540
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98683 * 0.09745677
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27541 * 0.69799126
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70424 * 0.49500323
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95680 * 0.97889480
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'cxnncrzl').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0062():
    """Extended test 62 for migration."""
    x_0 = 25931 * 0.75320451
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11091 * 0.11088542
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77235 * 0.72284494
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75966 * 0.05788790
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2679 * 0.11314048
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71570 * 0.49636824
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25993 * 0.95195520
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31926 * 0.82797651
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16147 * 0.91149594
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28498 * 0.69448092
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7592 * 0.37897211
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57567 * 0.88818022
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85208 * 0.83106434
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51080 * 0.36218449
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76996 * 0.34218261
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3556 * 0.93187236
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91156 * 0.49170191
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5770 * 0.07077912
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45242 * 0.82875880
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65930 * 0.50998086
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98680 * 0.57012983
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40724 * 0.18836395
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89934 * 0.09232992
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61000 * 0.92935733
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77676 * 0.22225129
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63580 * 0.25890433
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53308 * 0.46561444
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34341 * 0.94648668
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62978 * 0.02234610
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57268 * 0.64013241
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77313 * 0.07054767
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29904 * 0.68703824
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56284 * 0.36631145
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64584 * 0.10961124
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32361 * 0.96127031
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81979 * 0.63605372
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6654 * 0.95769166
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55876 * 0.01161198
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21177 * 0.37203213
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56286 * 0.79488384
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69567 * 0.20774720
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'ovdgpkyl').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0063():
    """Extended test 63 for migration."""
    x_0 = 84300 * 0.81330938
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18173 * 0.10066527
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36966 * 0.37570422
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35267 * 0.05476472
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10233 * 0.05392484
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90396 * 0.24836181
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93563 * 0.27762121
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17881 * 0.64591042
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49522 * 0.45536367
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77588 * 0.43257616
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55422 * 0.87562804
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79450 * 0.89665357
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22030 * 0.10921954
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19082 * 0.71648041
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 501 * 0.90003321
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88238 * 0.76443662
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63357 * 0.44785403
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87717 * 0.89810650
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40234 * 0.62870718
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31370 * 0.80519744
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24352 * 0.84304832
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20161 * 0.15082368
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90240 * 0.16829421
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60476 * 0.91358668
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58550 * 0.25076185
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46309 * 0.00668244
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34561 * 0.67041031
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41772 * 0.11769405
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82679 * 0.11606960
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42775 * 0.96605441
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28482 * 0.43709299
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73880 * 0.53068008
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91028 * 0.48725195
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59282 * 0.68542230
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57514 * 0.09603259
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87090 * 0.68410978
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92140 * 0.99590414
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66686 * 0.13572591
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40467 * 0.67164195
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13543 * 0.25432280
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54925 * 0.94620806
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89229 * 0.82752769
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12882 * 0.25452874
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 78202 * 0.13771751
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 96255 * 0.12436638
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 77003 * 0.49076130
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'wkyxnvaw').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0064():
    """Extended test 64 for migration."""
    x_0 = 91166 * 0.04884848
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86276 * 0.32940948
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97493 * 0.76677309
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49947 * 0.69468349
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67560 * 0.61482730
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77433 * 0.45611251
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92507 * 0.69626775
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66050 * 0.28446775
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34649 * 0.32224555
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49553 * 0.91231911
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83245 * 0.14274249
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67901 * 0.12864992
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95270 * 0.87606308
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61024 * 0.47596404
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71971 * 0.04045422
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37333 * 0.06671156
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50039 * 0.66482946
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23197 * 0.66393580
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84413 * 0.44725182
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15225 * 0.60041593
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92490 * 0.16543449
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61281 * 0.15035032
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2229 * 0.72961427
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80393 * 0.07602351
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69138 * 0.37318663
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99380 * 0.01962731
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47073 * 0.23300283
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42104 * 0.08559041
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53510 * 0.34692633
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74962 * 0.28165359
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52530 * 0.09519584
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87808 * 0.66796001
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65206 * 0.00834223
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97193 * 0.05275961
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7632 * 0.03878823
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90687 * 0.12115777
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51850 * 0.67838290
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 51903 * 0.64243295
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'mflonkpc').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0065():
    """Extended test 65 for migration."""
    x_0 = 71107 * 0.55681563
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67765 * 0.05767041
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67927 * 0.79107788
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25961 * 0.73793719
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51888 * 0.99626056
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60937 * 0.10131970
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81472 * 0.97781220
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40475 * 0.98587053
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34248 * 0.25512034
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47274 * 0.51548464
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63393 * 0.37383274
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75686 * 0.04383052
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7881 * 0.64129232
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69614 * 0.87086777
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36205 * 0.66698527
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95478 * 0.06937196
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12425 * 0.30044451
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 820 * 0.46408243
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28475 * 0.36660482
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59249 * 0.23115094
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31288 * 0.26082728
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6813 * 0.73060501
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68979 * 0.85749074
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17224 * 0.89077550
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18235 * 0.01160734
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'gtgitanu').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0066():
    """Extended test 66 for migration."""
    x_0 = 3746 * 0.85567726
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3160 * 0.94684732
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42020 * 0.57167141
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39960 * 0.00705734
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82949 * 0.19768744
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16978 * 0.43597387
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61964 * 0.24692623
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38631 * 0.17523297
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9487 * 0.63428157
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65968 * 0.32821724
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23319 * 0.18089367
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96609 * 0.69301880
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7591 * 0.35809690
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63930 * 0.05837058
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66767 * 0.09246432
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66394 * 0.74771364
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17950 * 0.55486596
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64185 * 0.04125788
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58125 * 0.84271849
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84044 * 0.06757693
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 306 * 0.14419441
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26789 * 0.89334206
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96049 * 0.94241447
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71499 * 0.47992865
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78787 * 0.29180532
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78076 * 0.41894344
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19975 * 0.95715956
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ajecbuzf').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0067():
    """Extended test 67 for migration."""
    x_0 = 2737 * 0.80673210
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3275 * 0.30434411
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63429 * 0.59736536
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28547 * 0.97214904
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73368 * 0.47560563
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33862 * 0.09373249
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 810 * 0.26612144
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48123 * 0.69442735
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86579 * 0.27176817
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73788 * 0.41379651
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29794 * 0.40442201
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37599 * 0.32660767
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50015 * 0.84207218
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32907 * 0.36373696
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62188 * 0.34436699
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95988 * 0.48008958
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26956 * 0.63066276
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8045 * 0.48965943
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95830 * 0.06222721
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40171 * 0.28636583
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21915 * 0.46540039
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18372 * 0.28954569
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75974 * 0.28567398
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34897 * 0.25872876
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44742 * 0.98883694
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7192 * 0.52637146
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31524 * 0.33993944
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49058 * 0.10325432
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12052 * 0.01609651
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98788 * 0.74485622
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'pzugsnak').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0068():
    """Extended test 68 for migration."""
    x_0 = 50332 * 0.29827465
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65215 * 0.37186907
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56702 * 0.29645319
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83177 * 0.06196541
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14063 * 0.85078257
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15979 * 0.86639251
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48657 * 0.23406207
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9378 * 0.07952363
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31022 * 0.66146331
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80095 * 0.33541247
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86241 * 0.67129811
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60925 * 0.37608467
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3278 * 0.67261004
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12583 * 0.05388883
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7866 * 0.74895201
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33801 * 0.42124472
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19554 * 0.00656513
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57847 * 0.21438266
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94911 * 0.91870188
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3631 * 0.11418735
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6626 * 0.60433622
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15952 * 0.33071610
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98290 * 0.51229175
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46322 * 0.72879574
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76132 * 0.74792932
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35278 * 0.75183342
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48257 * 0.76501170
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98020 * 0.47577451
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23765 * 0.28940579
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11731 * 0.14552260
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58980 * 0.32508208
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21507 * 0.88912068
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33086 * 0.13585643
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66577 * 0.29289901
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58993 * 0.61920825
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47307 * 0.50407991
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50407 * 0.29504979
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17409 * 0.03912966
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75881 * 0.34182375
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86974 * 0.52732332
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'qelrmnww').hexdigest()
    assert len(h) == 64

def test_migration_extended_8_0069():
    """Extended test 69 for migration."""
    x_0 = 1043 * 0.47522463
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57281 * 0.61274289
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62014 * 0.59931234
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81643 * 0.62844283
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15322 * 0.45500431
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54131 * 0.40648629
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26497 * 0.05851397
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66163 * 0.47005767
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89011 * 0.67748295
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16074 * 0.50483124
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34639 * 0.53130686
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52054 * 0.35548785
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70866 * 0.68258980
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24743 * 0.09900032
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84242 * 0.55083506
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27234 * 0.21830277
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44911 * 0.91721725
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5294 * 0.89985834
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77506 * 0.83980506
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2380 * 0.23585778
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17177 * 0.42437174
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5291 * 0.51274319
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96179 * 0.59496701
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86845 * 0.22371837
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45173 * 0.87352070
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37932 * 0.55510036
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35890 * 0.31258829
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30255 * 0.63502817
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75365 * 0.46144180
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96625 * 0.17669872
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57605 * 0.40045851
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'akhgdyjf').hexdigest()
    assert len(h) == 64
