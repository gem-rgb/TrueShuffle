"""Extended tests for scheduler suite 4."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_scheduler_extended_4_0000():
    """Extended test 0 for scheduler."""
    x_0 = 60878 * 0.35378543
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89562 * 0.38182608
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44649 * 0.36612982
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87880 * 0.90358116
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87293 * 0.33424225
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 834 * 0.47270086
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25557 * 0.45039150
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92279 * 0.21513826
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81609 * 0.29740717
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6478 * 0.87441354
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5788 * 0.13399783
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75568 * 0.03008205
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46263 * 0.33962005
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27027 * 0.89867340
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66234 * 0.53909852
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87661 * 0.10335180
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8541 * 0.17028081
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46431 * 0.40541165
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96717 * 0.69382785
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39319 * 0.20930789
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84753 * 0.15733933
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27294 * 0.33248493
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73628 * 0.04464546
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63910 * 0.59907118
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99298 * 0.60395293
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59266 * 0.73540338
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70927 * 0.72055225
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78693 * 0.98729429
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78044 * 0.97955781
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64214 * 0.22039555
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7865 * 0.29091898
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19163 * 0.10208634
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82265 * 0.97544009
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27691 * 0.08235334
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93257 * 0.41151689
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'gtzhxllh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0001():
    """Extended test 1 for scheduler."""
    x_0 = 25837 * 0.06480358
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19178 * 0.89769604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93114 * 0.06976332
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25605 * 0.07402069
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18264 * 0.73201021
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90382 * 0.28225322
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8817 * 0.88787893
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85007 * 0.88535529
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55670 * 0.38755348
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35135 * 0.55461043
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27753 * 0.47319837
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52433 * 0.70960288
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13310 * 0.80193812
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82073 * 0.73232469
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35609 * 0.13457242
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76680 * 0.00157867
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77934 * 0.85213716
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88256 * 0.66740901
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18504 * 0.05107610
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96994 * 0.91716302
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54155 * 0.81998770
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96747 * 0.35208154
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72946 * 0.97060772
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86796 * 0.85381853
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5398 * 0.44667504
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63951 * 0.84010156
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56920 * 0.51968677
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48133 * 0.01831095
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62506 * 0.71102490
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84412 * 0.49965266
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94407 * 0.77983381
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66758 * 0.96988287
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69537 * 0.91065694
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69823 * 0.15337247
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58657 * 0.96841280
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47041 * 0.57152443
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54253 * 0.29437145
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35611 * 0.09344323
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66674 * 0.18999059
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99819 * 0.05997117
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 70307 * 0.23245121
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77428 * 0.37783105
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22910 * 0.21025363
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'cgszhwtq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0002():
    """Extended test 2 for scheduler."""
    x_0 = 71102 * 0.46293096
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28985 * 0.62933167
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75507 * 0.69427161
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8939 * 0.90114975
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22222 * 0.63332212
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35092 * 0.65728621
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84929 * 0.54498315
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67036 * 0.47380808
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87746 * 0.83276939
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35667 * 0.16456270
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73962 * 0.21950419
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95169 * 0.37174633
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14823 * 0.46060058
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5655 * 0.53260220
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85573 * 0.33298124
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79399 * 0.83091529
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68800 * 0.15096571
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85470 * 0.44811058
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40830 * 0.28478141
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29148 * 0.04723923
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'looqxksk').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0003():
    """Extended test 3 for scheduler."""
    x_0 = 43300 * 0.26680171
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62708 * 0.19948965
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9598 * 0.61188975
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34380 * 0.14675142
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70746 * 0.26690418
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87754 * 0.35915315
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17268 * 0.70596026
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12404 * 0.96165017
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31950 * 0.19240926
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22906 * 0.08337025
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95701 * 0.78563596
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60901 * 0.58659012
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24789 * 0.82468607
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69472 * 0.85682110
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8643 * 0.71324906
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67056 * 0.97632188
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28265 * 0.89498663
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46911 * 0.51281834
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13404 * 0.19652618
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15269 * 0.72990044
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14846 * 0.03447340
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53694 * 0.26797589
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86702 * 0.18268022
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37691 * 0.13200179
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99183 * 0.80483246
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35789 * 0.41730452
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45673 * 0.54777825
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77328 * 0.46571545
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39431 * 0.20753317
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89983 * 0.32034147
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12646 * 0.94851884
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79822 * 0.92796734
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'wwbxorjj').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0004():
    """Extended test 4 for scheduler."""
    x_0 = 40379 * 0.48558123
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85972 * 0.84095430
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84856 * 0.13415509
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61627 * 0.56861998
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95281 * 0.87132772
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17853 * 0.48956712
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12607 * 0.08804986
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34358 * 0.69589458
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4719 * 0.13007644
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96784 * 0.93642201
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7921 * 0.07445385
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9805 * 0.28362912
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63012 * 0.85348227
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42881 * 0.05014691
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84280 * 0.99259508
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78196 * 0.60231562
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31839 * 0.87373506
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98459 * 0.68602470
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68086 * 0.99737443
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31090 * 0.73638230
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7680 * 0.37183875
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12381 * 0.91067493
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25832 * 0.90799428
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61423 * 0.79562550
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33464 * 0.55911843
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29214 * 0.47517105
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12846 * 0.07583532
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63791 * 0.81420817
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35466 * 0.05610544
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29152 * 0.15815613
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96829 * 0.17878944
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'hqywiezj').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0005():
    """Extended test 5 for scheduler."""
    x_0 = 96630 * 0.53129824
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6191 * 0.29050522
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3829 * 0.92872908
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63560 * 0.68962957
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61251 * 0.36117909
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61547 * 0.70408349
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64109 * 0.27259916
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19089 * 0.25846834
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76426 * 0.94280889
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29949 * 0.51721773
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96027 * 0.90642411
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37514 * 0.61467712
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85937 * 0.85010839
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54310 * 0.02926907
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95912 * 0.13521203
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78702 * 0.83391665
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25214 * 0.18357379
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65526 * 0.33519362
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6997 * 0.00267143
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19347 * 0.09332698
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27551 * 0.03796909
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67709 * 0.11800276
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66742 * 0.41039911
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97475 * 0.29332183
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34004 * 0.31434305
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84127 * 0.35887045
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63524 * 0.78797037
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65987 * 0.63116902
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89560 * 0.87300416
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72205 * 0.58484538
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11263 * 0.37077307
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36468 * 0.18475089
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'abnphjgv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0006():
    """Extended test 6 for scheduler."""
    x_0 = 54536 * 0.64058129
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60173 * 0.80162411
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25726 * 0.79735492
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10194 * 0.88609752
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78417 * 0.44310589
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26261 * 0.20425265
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15027 * 0.07913616
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67801 * 0.18314417
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90516 * 0.50410786
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62466 * 0.66487811
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45882 * 0.63850041
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38312 * 0.81921903
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94462 * 0.36641847
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53888 * 0.22870826
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29858 * 0.08679982
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7866 * 0.51993562
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99287 * 0.98742949
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74206 * 0.91365127
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2442 * 0.68502390
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41586 * 0.13163581
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2432 * 0.54426552
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18051 * 0.94224704
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59430 * 0.80330721
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37726 * 0.55026870
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'xfphxybt').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0007():
    """Extended test 7 for scheduler."""
    x_0 = 88694 * 0.13492963
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71535 * 0.11012585
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29479 * 0.68835313
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83818 * 0.59969728
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49303 * 0.89089007
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51045 * 0.50853301
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63863 * 0.52717943
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82 * 0.79808827
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46771 * 0.80182598
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96872 * 0.47142927
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16051 * 0.32844163
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53358 * 0.15099855
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85448 * 0.87823810
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99769 * 0.24401128
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82475 * 0.70192004
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24718 * 0.11986990
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48136 * 0.05235614
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84790 * 0.96441867
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1597 * 0.73293804
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60301 * 0.15768157
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19871 * 0.97346263
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25785 * 0.99943640
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92720 * 0.41983838
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12940 * 0.28345487
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74829 * 0.05067026
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13948 * 0.55590952
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68027 * 0.63726383
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51223 * 0.96067573
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 373 * 0.64872848
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64116 * 0.38452420
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94741 * 0.00365491
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33875 * 0.80406840
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72154 * 0.40451278
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19674 * 0.52256510
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45242 * 0.61131284
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26855 * 0.04059892
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27417 * 0.12986808
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'svwtzhha').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0008():
    """Extended test 8 for scheduler."""
    x_0 = 52883 * 0.95003348
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84372 * 0.04438987
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45894 * 0.02138226
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40837 * 0.50432472
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73485 * 0.98946615
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10277 * 0.23957352
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22219 * 0.17167346
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75343 * 0.31880905
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13944 * 0.37104419
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65410 * 0.87007538
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42766 * 0.02677654
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74532 * 0.44111289
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70463 * 0.61879297
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34260 * 0.66827908
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27692 * 0.34048610
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85120 * 0.89397342
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59815 * 0.31000713
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27207 * 0.03978848
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81312 * 0.61701490
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35135 * 0.94688025
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27853 * 0.32918350
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4376 * 0.19885494
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20013 * 0.42010872
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62227 * 0.83577497
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5737 * 0.47696951
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66296 * 0.97935426
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45047 * 0.39310619
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95095 * 0.91582494
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73826 * 0.22521000
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65967 * 0.29687465
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27313 * 0.68946592
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89045 * 0.12815983
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58684 * 0.74099988
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99460 * 0.68755131
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31673 * 0.12902911
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22317 * 0.98975275
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40077 * 0.33280943
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32771 * 0.25169839
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93455 * 0.85222465
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1631 * 0.89755090
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 39911 * 0.88278032
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 56232 * 0.54464248
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23787 * 0.02057382
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 50211 * 0.86824396
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92674 * 0.47950487
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 19199 * 0.93947636
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 32433 * 0.69534904
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'tnvqoetq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0009():
    """Extended test 9 for scheduler."""
    x_0 = 12152 * 0.54259193
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29243 * 0.15919184
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93237 * 0.74221484
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16317 * 0.70150022
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84114 * 0.31796918
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17362 * 0.23346677
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14353 * 0.11338868
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43580 * 0.70725120
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91939 * 0.50256997
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70878 * 0.46022993
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10695 * 0.63377006
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20631 * 0.87391570
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50464 * 0.10102180
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56535 * 0.51134331
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94630 * 0.03664108
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48262 * 0.40593183
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19498 * 0.81166675
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51411 * 0.14345978
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60216 * 0.49147426
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33568 * 0.80667209
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23820 * 0.83442412
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64016 * 0.91812731
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91753 * 0.81666795
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85992 * 0.64729752
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64869 * 0.23501273
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46121 * 0.81586519
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74022 * 0.69902848
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63668 * 0.16036733
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13951 * 0.63799483
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39841 * 0.93815687
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17146 * 0.54003021
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'lhewbbuz').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0010():
    """Extended test 10 for scheduler."""
    x_0 = 54556 * 0.03437360
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20998 * 0.44285192
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64053 * 0.22391950
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49326 * 0.27526148
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6152 * 0.63086670
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75474 * 0.62966618
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41147 * 0.22009987
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41871 * 0.88580761
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81904 * 0.54918073
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69748 * 0.47741610
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65637 * 0.30704333
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55203 * 0.73753451
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33459 * 0.21545739
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17334 * 0.64871887
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50576 * 0.67758081
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56498 * 0.85311274
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19859 * 0.95096146
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3697 * 0.22502894
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7255 * 0.65752071
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10834 * 0.87879558
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55013 * 0.03392317
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51225 * 0.25105460
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46179 * 0.38128754
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29701 * 0.74946342
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74896 * 0.41109296
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18761 * 0.10219164
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47894 * 0.35229279
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6180 * 0.63986553
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16986 * 0.15146576
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51084 * 0.61818249
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94268 * 0.78974680
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11349 * 0.40701228
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53513 * 0.85966131
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51201 * 0.31056831
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78447 * 0.34746061
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5205 * 0.52853574
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1992 * 0.35902550
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36407 * 0.64252058
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 85206 * 0.73704371
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95998 * 0.54644143
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 58203 * 0.29339640
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 86157 * 0.34306998
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62133 * 0.76438322
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'mckxvria').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0011():
    """Extended test 11 for scheduler."""
    x_0 = 60067 * 0.69729325
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36228 * 0.26575040
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20369 * 0.60737486
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4706 * 0.05728636
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9059 * 0.70728706
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13090 * 0.76891105
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83921 * 0.33749697
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28116 * 0.60080232
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87870 * 0.68580190
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67776 * 0.38027215
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34667 * 0.76502678
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85028 * 0.63292551
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35262 * 0.59971291
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36914 * 0.63411012
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43648 * 0.31828537
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17171 * 0.76255664
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24331 * 0.21756272
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64448 * 0.48041510
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51306 * 0.82476329
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59659 * 0.26348782
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78650 * 0.32889689
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64543 * 0.67638118
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26330 * 0.44600065
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9986 * 0.74435623
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59342 * 0.77940404
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92883 * 0.37351215
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45926 * 0.07281788
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96939 * 0.93895556
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76082 * 0.18681672
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95612 * 0.51656255
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16267 * 0.88965420
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'htqgvuri').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0012():
    """Extended test 12 for scheduler."""
    x_0 = 47294 * 0.57833773
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79518 * 0.24393182
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14026 * 0.85894595
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86102 * 0.10479355
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53607 * 0.88045858
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18399 * 0.10665771
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53922 * 0.82555891
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24595 * 0.45212282
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45645 * 0.19533586
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22885 * 0.15503591
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47082 * 0.81447012
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10538 * 0.14534035
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56420 * 0.06207684
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28878 * 0.56859037
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4186 * 0.68324865
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3655 * 0.37044914
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60862 * 0.06993659
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49098 * 0.41970998
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24292 * 0.49497606
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28360 * 0.67135497
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32578 * 0.93395233
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32734 * 0.01836400
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15558 * 0.41891334
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90085 * 0.54926025
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'vwgffjok').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0013():
    """Extended test 13 for scheduler."""
    x_0 = 18632 * 0.14212549
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66484 * 0.70734566
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90588 * 0.51745359
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8788 * 0.74442469
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56702 * 0.27726227
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49720 * 0.16014406
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66198 * 0.37733823
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76382 * 0.20476412
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58145 * 0.28388726
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18520 * 0.75489763
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26975 * 0.78766590
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55856 * 0.51655252
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59254 * 0.36675508
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47358 * 0.98310177
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74656 * 0.59170497
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17238 * 0.18247091
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20112 * 0.65020366
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79991 * 0.94877193
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58578 * 0.67055395
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27146 * 0.86414792
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35952 * 0.14924657
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75486 * 0.35051119
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43348 * 0.08657907
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42520 * 0.06057969
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6461 * 0.00124150
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92107 * 0.53410294
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35504 * 0.43586781
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80643 * 0.32708332
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12223 * 0.66542160
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81939 * 0.83680193
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7187 * 0.51125419
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2647 * 0.69196180
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'iragdhbd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0014():
    """Extended test 14 for scheduler."""
    x_0 = 21313 * 0.91657179
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56940 * 0.48251690
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17982 * 0.95007333
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62597 * 0.87769062
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20062 * 0.06309391
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82520 * 0.07489496
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19379 * 0.02674005
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12483 * 0.75390377
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60897 * 0.61711483
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20503 * 0.52749141
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34960 * 0.85311105
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52461 * 0.32895862
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36522 * 0.26791811
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67514 * 0.75554918
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73993 * 0.01067051
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69116 * 0.50989980
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46890 * 0.39334672
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20376 * 0.44381587
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59993 * 0.43283231
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97220 * 0.17309178
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22147 * 0.98757582
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38271 * 0.10887851
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57009 * 0.46165247
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58173 * 0.92245047
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45245 * 0.10263357
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41002 * 0.37335465
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11604 * 0.72470733
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55352 * 0.18295510
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91780 * 0.59082659
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 212 * 0.54748273
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26770 * 0.24504146
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33781 * 0.05629616
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82496 * 0.40147958
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35988 * 0.38668646
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34446 * 0.66438373
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'dnpiuppu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0015():
    """Extended test 15 for scheduler."""
    x_0 = 63558 * 0.78384608
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10562 * 0.35418241
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19963 * 0.70528486
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80146 * 0.89334499
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4159 * 0.21516691
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66579 * 0.69259522
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84204 * 0.42609134
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75055 * 0.28117038
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56920 * 0.53327769
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2589 * 0.76073497
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88078 * 0.09896828
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58608 * 0.50321625
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47155 * 0.26795893
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19332 * 0.83311368
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91433 * 0.72491251
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39098 * 0.08226719
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58615 * 0.35345718
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90902 * 0.86551965
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38418 * 0.68870001
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52081 * 0.03109190
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31848 * 0.96099131
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65865 * 0.32087510
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45893 * 0.56542820
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58650 * 0.54844350
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25055 * 0.35966915
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70850 * 0.82210927
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51440 * 0.59064315
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34022 * 0.02888891
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75013 * 0.86707921
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36536 * 0.11690163
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4293 * 0.29839088
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68591 * 0.04278153
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6293 * 0.09334139
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52728 * 0.41468899
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69973 * 0.00965318
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62532 * 0.96956153
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81375 * 0.77583197
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7165 * 0.12155897
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14296 * 0.85162349
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'dbsoefwx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0016():
    """Extended test 16 for scheduler."""
    x_0 = 13141 * 0.51177971
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33973 * 0.49191246
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8780 * 0.31705129
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24991 * 0.01793426
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51383 * 0.74331747
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13518 * 0.60607670
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16365 * 0.14902858
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9448 * 0.73638452
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48716 * 0.05689593
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98669 * 0.97937128
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97826 * 0.36707393
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95449 * 0.04237370
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40855 * 0.60368749
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25947 * 0.59921151
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53413 * 0.21230027
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96290 * 0.19968008
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30794 * 0.07622056
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51069 * 0.02778143
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7889 * 0.84532500
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11957 * 0.49026610
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95450 * 0.64265748
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48272 * 0.70057289
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22128 * 0.56528328
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38334 * 0.22090917
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17060 * 0.90878718
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66708 * 0.63240360
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33714 * 0.80978335
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30991 * 0.69817883
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87790 * 0.12082694
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93886 * 0.66837668
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17270 * 0.55747756
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80836 * 0.75444411
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67396 * 0.00849097
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94259 * 0.43455808
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94524 * 0.81957819
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21464 * 0.29968364
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98466 * 0.86291456
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 57900 * 0.22641110
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15462 * 0.32706001
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21130 * 0.15989543
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13933 * 0.01892915
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26950 * 0.67534131
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 78403 * 0.68922832
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 79054 * 0.08532590
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 76668 * 0.36361316
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 65874 * 0.03894454
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'qheiltem').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0017():
    """Extended test 17 for scheduler."""
    x_0 = 37659 * 0.68949376
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7463 * 0.30091531
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41483 * 0.05935642
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4593 * 0.64476015
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75723 * 0.74862385
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58635 * 0.21900383
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 812 * 0.40916749
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55782 * 0.63461018
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38357 * 0.71166101
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90701 * 0.02371110
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10638 * 0.07694429
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82569 * 0.05295743
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8459 * 0.46574776
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49968 * 0.71470634
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55846 * 0.51872059
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60230 * 0.09023112
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2708 * 0.51899058
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60638 * 0.46917361
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3261 * 0.41005890
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28972 * 0.71555369
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75853 * 0.97799830
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9559 * 0.96175983
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45923 * 0.38474116
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93210 * 0.04939315
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91540 * 0.98138610
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4591 * 0.04486401
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43313 * 0.02211427
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7356 * 0.32977715
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54219 * 0.10143173
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14412 * 0.34775682
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99187 * 0.86505365
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51874 * 0.82259064
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24681 * 0.70085205
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87608 * 0.53366677
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59321 * 0.49446041
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81918 * 0.34978821
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44784 * 0.33832189
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32864 * 0.84051584
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11899 * 0.83248513
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68505 * 0.03656657
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29466 * 0.63277802
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85877 * 0.15882547
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88271 * 0.56456881
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 14587 * 0.90348307
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 31711 * 0.32417595
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 14996 * 0.45259971
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 74895 * 0.85636876
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 53824 * 0.89243038
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 14607 * 0.58151967
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 46679 * 0.06779652
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'oqgmdcns').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0018():
    """Extended test 18 for scheduler."""
    x_0 = 78599 * 0.15623080
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23376 * 0.13137235
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48077 * 0.65029834
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10627 * 0.48748630
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73560 * 0.91145850
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18168 * 0.55830157
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10639 * 0.27266356
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87651 * 0.69411689
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23964 * 0.46679989
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68279 * 0.96926395
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94284 * 0.09160629
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4068 * 0.82348468
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9784 * 0.68444747
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74305 * 0.11475716
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86440 * 0.18765709
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16180 * 0.39225977
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8203 * 0.46932349
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10115 * 0.02999532
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55807 * 0.15673840
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58399 * 0.44600114
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13065 * 0.70714603
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37315 * 0.83060478
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4268 * 0.53634774
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71338 * 0.95954100
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70595 * 0.41507592
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4607 * 0.09783724
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64754 * 0.04348796
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4351 * 0.79046090
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52523 * 0.14681556
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11588 * 0.39526568
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33936 * 0.24487199
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35041 * 0.51391156
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22204 * 0.36412407
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88003 * 0.81244886
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26872 * 0.76205468
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12711 * 0.69610520
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2833 * 0.35729472
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36683 * 0.24526577
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'suysuztd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0019():
    """Extended test 19 for scheduler."""
    x_0 = 91240 * 0.82209058
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88608 * 0.41476698
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84438 * 0.83984908
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57046 * 0.71324083
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7644 * 0.98292712
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81588 * 0.27460369
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69310 * 0.67100723
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77172 * 0.46076353
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48401 * 0.28509803
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46664 * 0.19116997
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45246 * 0.64110269
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85380 * 0.00233184
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29757 * 0.44300368
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27378 * 0.89130440
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36601 * 0.22650467
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51845 * 0.41189334
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4639 * 0.46900070
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3110 * 0.48948806
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40077 * 0.87492457
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71309 * 0.44138373
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18791 * 0.47230635
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68904 * 0.69689559
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13630 * 0.16342110
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10512 * 0.33943582
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68005 * 0.53769118
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82168 * 0.83527310
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27717 * 0.09314909
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5007 * 0.84060770
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98710 * 0.82576660
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31163 * 0.50081327
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27266 * 0.16369569
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ossgkfhh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0020():
    """Extended test 20 for scheduler."""
    x_0 = 98031 * 0.00689592
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74000 * 0.78813347
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68952 * 0.68540791
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39790 * 0.30292313
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26787 * 0.32429189
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35726 * 0.14140735
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79184 * 0.92119058
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14785 * 0.32641818
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56423 * 0.21148679
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88991 * 0.93659117
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78365 * 0.34064309
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95154 * 0.31815359
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23470 * 0.87385796
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89188 * 0.84498560
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50954 * 0.04301398
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52131 * 0.15485554
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37480 * 0.19834049
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20789 * 0.05750538
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50882 * 0.18408617
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78933 * 0.71217540
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29769 * 0.71251877
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80145 * 0.73306349
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63833 * 0.28757976
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8372 * 0.64691071
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75766 * 0.20122281
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73676 * 0.76011196
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67789 * 0.25293290
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6188 * 0.15720186
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30936 * 0.24825234
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99637 * 0.31719008
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85599 * 0.17698258
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16130 * 0.25039975
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27660 * 0.69425333
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41708 * 0.99067641
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38128 * 0.93973906
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99537 * 0.72030217
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3436 * 0.69099099
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31055 * 0.41680188
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'stddlvyb').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0021():
    """Extended test 21 for scheduler."""
    x_0 = 94466 * 0.92708280
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51953 * 0.21681852
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1074 * 0.38225726
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48353 * 0.87097933
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56514 * 0.89025789
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62628 * 0.33695021
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48668 * 0.19149834
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43452 * 0.29688647
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29376 * 0.47013111
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1637 * 0.00939310
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5842 * 0.63158848
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18653 * 0.81167542
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84780 * 0.09715024
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23102 * 0.52094747
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69934 * 0.98553827
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84403 * 0.39238476
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26521 * 0.61613276
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80993 * 0.78465746
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86078 * 0.73409590
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62611 * 0.45872286
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18639 * 0.49192950
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69495 * 0.31922289
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3980 * 0.31065414
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68857 * 0.46994229
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46846 * 0.53158214
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12955 * 0.95613718
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28678 * 0.95655125
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27737 * 0.07663315
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16359 * 0.67210425
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54067 * 0.78663753
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45960 * 0.43834730
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43626 * 0.66494762
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18877 * 0.13445353
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47148 * 0.24924408
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91432 * 0.48811264
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27779 * 0.11764099
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90971 * 0.08404094
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87616 * 0.41905725
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71138 * 0.98513616
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 35706 * 0.68531560
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43277 * 0.67871767
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'iujlhskj').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0022():
    """Extended test 22 for scheduler."""
    x_0 = 40105 * 0.17479722
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39443 * 0.96893845
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48168 * 0.53823044
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5422 * 0.95184314
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74900 * 0.51023850
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34552 * 0.31977098
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42515 * 0.82161740
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40036 * 0.09173718
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4764 * 0.37365573
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70886 * 0.82457880
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79731 * 0.58893769
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89046 * 0.96381317
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18009 * 0.45644651
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40265 * 0.72903908
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21102 * 0.52296586
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54391 * 0.47015674
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83768 * 0.71782221
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91474 * 0.74988539
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65682 * 0.78477901
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22606 * 0.23870442
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93676 * 0.44175274
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18862 * 0.04996961
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80653 * 0.26838307
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56981 * 0.17410961
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68416 * 0.07525687
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11908 * 0.50599607
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41315 * 0.46504395
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93164 * 0.82316477
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'dycjqtvk').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0023():
    """Extended test 23 for scheduler."""
    x_0 = 79644 * 0.15199079
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98953 * 0.22188715
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74622 * 0.95785931
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83856 * 0.83674238
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14077 * 0.87457134
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3027 * 0.32557773
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64250 * 0.11926764
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52015 * 0.42900732
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76912 * 0.38268080
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76803 * 0.29409802
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14818 * 0.97687036
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78675 * 0.64058715
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54858 * 0.74856858
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13976 * 0.35770618
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92649 * 0.37258582
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67451 * 0.51238458
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45378 * 0.64457322
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57539 * 0.59380732
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33918 * 0.60066129
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74109 * 0.73021076
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79985 * 0.26052667
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72557 * 0.11172046
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74806 * 0.02860888
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88676 * 0.42582449
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35501 * 0.56975974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1672 * 0.99171321
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68246 * 0.25576902
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59651 * 0.81870040
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89926 * 0.52060480
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75310 * 0.16644093
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99419 * 0.53570236
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98386 * 0.67434846
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17579 * 0.27645199
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37644 * 0.40067889
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41070 * 0.82955545
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1164 * 0.74039858
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48955 * 0.80251770
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81878 * 0.59661761
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56457 * 0.74204156
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11592 * 0.58392426
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 66911 * 0.20841244
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'juwegqol').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0024():
    """Extended test 24 for scheduler."""
    x_0 = 96003 * 0.07620424
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98582 * 0.76592787
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37609 * 0.28032689
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44633 * 0.69879693
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22581 * 0.61487681
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16715 * 0.14669303
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97700 * 0.29710912
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40334 * 0.36258217
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90832 * 0.93755583
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11092 * 0.46628263
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88207 * 0.24825045
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51880 * 0.72174796
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21950 * 0.49313417
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1418 * 0.43364796
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61892 * 0.08398025
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38016 * 0.20114090
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20207 * 0.51520541
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62360 * 0.08723898
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75180 * 0.05039385
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13738 * 0.85242950
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99705 * 0.68735824
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2468 * 0.33195051
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54247 * 0.96229311
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59275 * 0.99179121
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38783 * 0.72435626
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58961 * 0.21807507
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84472 * 0.09247285
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65801 * 0.48088864
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98421 * 0.08393162
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74609 * 0.61537250
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37482 * 0.55051552
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10202 * 0.59269217
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75224 * 0.38377690
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97270 * 0.89128642
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25982 * 0.27687784
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74697 * 0.38055180
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89763 * 0.83006340
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'jrtmozqd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0025():
    """Extended test 25 for scheduler."""
    x_0 = 63876 * 0.14939111
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64515 * 0.57986337
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85761 * 0.66358542
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36885 * 0.32085853
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7907 * 0.09320573
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14733 * 0.80283654
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50281 * 0.44339579
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57920 * 0.28103927
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5134 * 0.28815944
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38667 * 0.46945877
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37279 * 0.21805655
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67372 * 0.54180292
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73574 * 0.87575556
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80894 * 0.54465639
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91141 * 0.74380803
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66912 * 0.24671462
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24249 * 0.93852911
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66132 * 0.60510120
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54419 * 0.46828219
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35451 * 0.07192157
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'hevcsxhp').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0026():
    """Extended test 26 for scheduler."""
    x_0 = 18311 * 0.30179152
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62565 * 0.78570404
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87813 * 0.40822515
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40470 * 0.50368709
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13543 * 0.78791499
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36800 * 0.16577072
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61153 * 0.46876128
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49576 * 0.74207231
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97987 * 0.07109534
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41175 * 0.80465764
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1182 * 0.30706374
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56136 * 0.31939940
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74686 * 0.24359357
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65391 * 0.58751500
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59906 * 0.65308938
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86904 * 0.71470105
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43635 * 0.12974529
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85667 * 0.74878124
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61576 * 0.04090076
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88253 * 0.06371624
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38719 * 0.75734170
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71535 * 0.67014274
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85209 * 0.18854305
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'rpcftotp').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0027():
    """Extended test 27 for scheduler."""
    x_0 = 78722 * 0.14138732
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45092 * 0.45092219
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61587 * 0.98197697
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33483 * 0.40949129
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74502 * 0.91235715
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3765 * 0.72746627
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69368 * 0.41797957
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87443 * 0.23522894
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12691 * 0.79568066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58238 * 0.09442990
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67272 * 0.09135347
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84818 * 0.88817416
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76906 * 0.80548656
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80951 * 0.70163934
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12051 * 0.71943434
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11562 * 0.14501135
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31329 * 0.65976563
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44226 * 0.07083847
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4526 * 0.00579066
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27333 * 0.59029907
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30830 * 0.18674857
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40462 * 0.38399514
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33706 * 0.43205314
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63861 * 0.13700867
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53065 * 0.42077754
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98796 * 0.80417019
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54251 * 0.28614835
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43182 * 0.83330259
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'tbnmqmsv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0028():
    """Extended test 28 for scheduler."""
    x_0 = 74684 * 0.57077620
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55140 * 0.97462756
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46673 * 0.17151348
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65012 * 0.50973791
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65605 * 0.73791162
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 774 * 0.18650077
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61492 * 0.26323600
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14519 * 0.02935368
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15051 * 0.67405165
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88949 * 0.85330578
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92488 * 0.86186682
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25397 * 0.82228737
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96768 * 0.05712437
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52661 * 0.19778388
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68503 * 0.28844284
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57698 * 0.80188460
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86580 * 0.50825008
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85732 * 0.38237969
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81569 * 0.39002932
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23819 * 0.41132973
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83032 * 0.87589421
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31039 * 0.64242432
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96421 * 0.18326858
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16440 * 0.89012300
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4911 * 0.06835172
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35761 * 0.93429691
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5131 * 0.92800149
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27385 * 0.47966812
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72098 * 0.54134118
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55739 * 0.22715965
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25218 * 0.40773048
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57875 * 0.60769669
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23044 * 0.06852640
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'houbkltq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0029():
    """Extended test 29 for scheduler."""
    x_0 = 29875 * 0.47675990
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99480 * 0.65007222
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86119 * 0.07098662
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74420 * 0.43993218
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15832 * 0.06762059
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50408 * 0.38319381
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43915 * 0.26091973
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57586 * 0.20827230
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34506 * 0.79529150
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76208 * 0.55999395
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44564 * 0.30337596
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89329 * 0.63498467
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36534 * 0.89312756
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16774 * 0.36238026
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52368 * 0.32621833
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35012 * 0.05365197
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15030 * 0.78112047
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52571 * 0.64518419
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10041 * 0.38100992
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94568 * 0.73410321
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60623 * 0.46423094
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25347 * 0.93489977
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17886 * 0.59462735
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74739 * 0.80383060
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1493 * 0.88459743
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76562 * 0.47664546
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1108 * 0.86314733
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86383 * 0.75112048
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74007 * 0.03559244
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88832 * 0.10841018
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23103 * 0.33784881
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51060 * 0.81850021
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34285 * 0.71461214
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79638 * 0.68890775
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45501 * 0.13173866
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45455 * 0.87584296
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27603 * 0.39639348
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42639 * 0.10954515
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'xzhbgaef').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0030():
    """Extended test 30 for scheduler."""
    x_0 = 60810 * 0.82850950
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86147 * 0.23174796
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74032 * 0.02268309
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3244 * 0.22671383
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82490 * 0.83526311
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40162 * 0.51890390
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35957 * 0.97442805
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34086 * 0.23680681
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90735 * 0.49045313
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15387 * 0.75455494
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20328 * 0.98316457
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27539 * 0.96235863
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82045 * 0.81310703
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48040 * 0.52522957
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52581 * 0.02623575
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46763 * 0.66895893
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14260 * 0.15375497
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96334 * 0.20407304
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36715 * 0.86029998
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9797 * 0.16523433
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82956 * 0.52176139
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52160 * 0.06193376
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86880 * 0.14845029
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83979 * 0.50196518
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50034 * 0.35411355
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99424 * 0.10035886
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88197 * 0.20892247
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65330 * 0.90931936
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66346 * 0.11276207
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79320 * 0.34680449
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78699 * 0.37629968
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45083 * 0.39194004
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57629 * 0.81402192
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'phvivopn').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0031():
    """Extended test 31 for scheduler."""
    x_0 = 8556 * 0.85839142
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92809 * 0.74617052
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65165 * 0.09799834
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45091 * 0.90892682
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49942 * 0.37312773
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45771 * 0.32080103
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51594 * 0.04340828
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12296 * 0.67271930
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59697 * 0.70702482
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44983 * 0.53750730
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79639 * 0.58111827
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97274 * 0.02211068
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26027 * 0.71141105
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30405 * 0.67608798
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93552 * 0.39848056
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63694 * 0.88742375
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64258 * 0.41036081
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89829 * 0.55744604
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12421 * 0.91283647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69580 * 0.62835765
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4356 * 0.55297349
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73026 * 0.99402294
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34349 * 0.98062739
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52131 * 0.37713225
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97733 * 0.02917690
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22245 * 0.60584391
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79293 * 0.75000338
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28918 * 0.32469872
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74183 * 0.99190172
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34754 * 0.92667238
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92366 * 0.18234054
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8147 * 0.33619680
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70425 * 0.76191519
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48769 * 0.40950157
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48735 * 0.56880444
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51740 * 0.63420213
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35783 * 0.77687171
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85302 * 0.92385966
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6602 * 0.59518816
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 58830 * 0.66168850
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60428 * 0.76206831
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22931 * 0.56162543
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55561 * 0.55256026
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'oqjvigrr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0032():
    """Extended test 32 for scheduler."""
    x_0 = 85885 * 0.64774349
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78219 * 0.59941233
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76080 * 0.39680491
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1558 * 0.14925487
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43969 * 0.54483441
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97849 * 0.40260173
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18587 * 0.86912510
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87535 * 0.16518161
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50524 * 0.26539189
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44888 * 0.46626667
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38016 * 0.26730229
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1359 * 0.18002907
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93076 * 0.16988390
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65366 * 0.94992388
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86067 * 0.07730779
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89469 * 0.89622360
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15021 * 0.34882096
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38967 * 0.09983088
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82927 * 0.29448862
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5184 * 0.31186718
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19862 * 0.43946272
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52432 * 0.94276052
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40101 * 0.58618349
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18633 * 0.83591243
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76448 * 0.80958446
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40105 * 0.68733862
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70963 * 0.79315357
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25350 * 0.22936415
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69097 * 0.31546915
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58521 * 0.61934916
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'qfzcehto').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0033():
    """Extended test 33 for scheduler."""
    x_0 = 74872 * 0.55242094
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72075 * 0.80356606
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79746 * 0.52065540
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91767 * 0.98675200
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76332 * 0.93495778
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80973 * 0.98819597
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32588 * 0.80917516
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18388 * 0.21825958
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26828 * 0.96532740
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28313 * 0.01648371
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24648 * 0.15094515
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72721 * 0.84770705
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66151 * 0.95189945
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17307 * 0.02322211
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92351 * 0.85849987
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62933 * 0.94612594
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65833 * 0.05128012
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10918 * 0.57188321
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83102 * 0.29970995
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11531 * 0.24850086
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18218 * 0.63923863
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63384 * 0.14214178
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35407 * 0.16381548
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54739 * 0.94755904
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68946 * 0.02173364
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58453 * 0.63779891
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21224 * 0.93812421
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97812 * 0.57099241
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70572 * 0.37868029
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76743 * 0.18401501
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19138 * 0.90463545
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96123 * 0.88323634
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39342 * 0.39807453
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5907 * 0.02439982
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31664 * 0.09296782
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37074 * 0.80323830
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50362 * 0.61146863
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 37833 * 0.50342425
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82215 * 0.44730999
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7805 * 0.45707664
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77240 * 0.48333834
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60846 * 0.93847051
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'wmonapkg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0034():
    """Extended test 34 for scheduler."""
    x_0 = 58494 * 0.28959680
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91592 * 0.57431916
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38117 * 0.24007308
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71288 * 0.32804758
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11773 * 0.46239511
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19356 * 0.44467793
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33013 * 0.73963540
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46475 * 0.24474084
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46701 * 0.40015939
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57194 * 0.34782422
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82538 * 0.81835501
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 787 * 0.85722393
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55223 * 0.46393793
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55981 * 0.59169574
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33062 * 0.74374955
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23404 * 0.31804750
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47543 * 0.27740744
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53788 * 0.11570760
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71684 * 0.91632767
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39467 * 0.94874876
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51987 * 0.96773463
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73823 * 0.70803407
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'khznzfyg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0035():
    """Extended test 35 for scheduler."""
    x_0 = 50123 * 0.03296780
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42495 * 0.17630861
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78810 * 0.29162903
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73352 * 0.41490006
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65685 * 0.62989763
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16767 * 0.04261560
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51078 * 0.46693222
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48358 * 0.77919499
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50863 * 0.00315627
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70468 * 0.01836578
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91170 * 0.15637410
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66652 * 0.90488540
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70819 * 0.92741776
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21411 * 0.48483900
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79465 * 0.40733530
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18807 * 0.03046418
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96516 * 0.37659019
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26027 * 0.50939048
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61878 * 0.59326251
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9212 * 0.84553882
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29518 * 0.42176811
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61804 * 0.19091843
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43111 * 0.63087005
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74439 * 0.32456762
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17882 * 0.66883046
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45848 * 0.41483508
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82542 * 0.21805754
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17062 * 0.28965465
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32438 * 0.75224745
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72154 * 0.69454335
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12639 * 0.28659078
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89230 * 0.79013887
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62550 * 0.06574397
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71570 * 0.53706738
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67362 * 0.14617582
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98667 * 0.62917502
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49797 * 0.11502676
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49160 * 0.75210595
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66793 * 0.55523836
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88326 * 0.41466534
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64539 * 0.47964387
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58603 * 0.46729908
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 5386 * 0.23383731
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75279 * 0.32706424
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86503 * 0.07881074
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 7848 * 0.48948409
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 7602 * 0.97878943
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 96167 * 0.94344354
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 30053 * 0.52202894
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'lvpclpoj').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0036():
    """Extended test 36 for scheduler."""
    x_0 = 92010 * 0.01941902
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57792 * 0.68647745
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79250 * 0.36035188
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28298 * 0.32383198
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56532 * 0.58379141
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29410 * 0.98852730
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89559 * 0.51995172
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34841 * 0.81497727
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37537 * 0.69211818
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87609 * 0.40974212
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50908 * 0.51794698
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1069 * 0.83160112
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42592 * 0.35572058
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59522 * 0.29168103
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97955 * 0.84323010
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70855 * 0.69916982
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34880 * 0.00607816
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24008 * 0.94483823
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9721 * 0.93535786
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42537 * 0.81415292
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62212 * 0.64441347
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8401 * 0.08390532
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62889 * 0.15237328
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18235 * 0.35032179
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42996 * 0.56437697
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33479 * 0.29704583
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45167 * 0.94204174
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33479 * 0.66799689
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19295 * 0.78487472
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18042 * 0.54200748
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79293 * 0.83843969
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84991 * 0.41514240
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33931 * 0.26459646
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'fqbpdqms').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0037():
    """Extended test 37 for scheduler."""
    x_0 = 95122 * 0.60383508
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71346 * 0.19203231
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28592 * 0.63909481
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66807 * 0.72560334
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33494 * 0.16848405
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87464 * 0.98980685
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47305 * 0.89211512
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26639 * 0.83351918
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70032 * 0.35804393
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5974 * 0.99200731
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9448 * 0.08727131
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76297 * 0.15264715
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25769 * 0.20519995
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67169 * 0.17845629
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55688 * 0.30507276
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63083 * 0.33324957
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16731 * 0.67335719
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20007 * 0.27102507
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31467 * 0.53351137
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20141 * 0.69706812
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86517 * 0.72472904
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5612 * 0.30929581
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24942 * 0.93374333
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7776 * 0.11367779
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28180 * 0.40250174
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87098 * 0.20296016
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94943 * 0.93289153
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96174 * 0.45653538
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19453 * 0.08535604
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31127 * 0.84836499
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30990 * 0.15432496
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'bhavfbbz').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0038():
    """Extended test 38 for scheduler."""
    x_0 = 90589 * 0.59477395
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97505 * 0.70676521
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97651 * 0.81611718
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53646 * 0.89210848
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97657 * 0.78636195
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84274 * 0.13880809
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70153 * 0.96130339
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32035 * 0.61863047
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3212 * 0.37225680
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10774 * 0.87635563
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60010 * 0.07062679
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86700 * 0.41761924
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52687 * 0.56404803
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48015 * 0.84364375
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37652 * 0.99999787
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91618 * 0.93572708
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21249 * 0.41794345
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1277 * 0.59646473
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46425 * 0.40230294
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20497 * 0.86888833
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79340 * 0.55412896
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26812 * 0.30811219
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58431 * 0.89395406
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6597 * 0.87842630
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21972 * 0.24602694
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6417 * 0.98753024
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29969 * 0.13966698
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8613 * 0.88658734
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64 * 0.16192653
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53819 * 0.96430905
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34435 * 0.91643112
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80154 * 0.11711574
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15750 * 0.56363984
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52624 * 0.61171719
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13774 * 0.44494991
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 73143 * 0.86639962
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20463 * 0.74644161
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'qpxeyigy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0039():
    """Extended test 39 for scheduler."""
    x_0 = 15353 * 0.98059458
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96585 * 0.99374415
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94615 * 0.75623260
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72583 * 0.75369871
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65045 * 0.72660368
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95523 * 0.39550264
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77366 * 0.53349512
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48370 * 0.79912428
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5676 * 0.17336118
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83545 * 0.07789975
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15431 * 0.30568560
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99308 * 0.97849099
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67110 * 0.40680159
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6874 * 0.50893683
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7978 * 0.79423579
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30808 * 0.01431706
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65947 * 0.37739013
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25342 * 0.27564589
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7345 * 0.65176958
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17486 * 0.48902850
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63032 * 0.13137679
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24961 * 0.50784059
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17440 * 0.24448813
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90730 * 0.90890410
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26664 * 0.98284750
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92818 * 0.38587571
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61748 * 0.17630794
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32604 * 0.27045982
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39459 * 0.83167419
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79017 * 0.78718505
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49135 * 0.93052398
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72762 * 0.50046915
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87824 * 0.96355428
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8299 * 0.92762590
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44538 * 0.95858791
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7258 * 0.19678584
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80708 * 0.42230819
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68118 * 0.16845667
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16626 * 0.79839195
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43999 * 0.60746113
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44200 * 0.02177669
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 78350 * 0.31348278
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81714 * 0.65120339
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11830 * 0.02169044
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 54082 * 0.50028441
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 40981 * 0.10196357
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 13976 * 0.87057511
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 12504 * 0.91443970
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'nianonip').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0040():
    """Extended test 40 for scheduler."""
    x_0 = 18541 * 0.77066951
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71466 * 0.86540842
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23587 * 0.54336763
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45006 * 0.06010303
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69094 * 0.73042929
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63261 * 0.69331468
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79933 * 0.20863343
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20967 * 0.52848584
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97078 * 0.59662782
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38423 * 0.06815523
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51579 * 0.07212122
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91175 * 0.08493895
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56382 * 0.87100477
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28944 * 0.14656754
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81510 * 0.41487114
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81559 * 0.13921222
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78750 * 0.82902761
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51337 * 0.26484541
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7171 * 0.62218843
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18282 * 0.43008246
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54877 * 0.58652674
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65133 * 0.62329209
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66058 * 0.08754745
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56956 * 0.32197986
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66142 * 0.94259499
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38216 * 0.67721377
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54977 * 0.43710810
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47899 * 0.44965411
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74400 * 0.93038365
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76654 * 0.65938669
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43227 * 0.03880250
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22897 * 0.53526835
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80188 * 0.04827212
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34540 * 0.30173132
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 49743 * 0.37326654
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35299 * 0.09800104
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48503 * 0.49498943
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31186 * 0.04302449
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63614 * 0.75664488
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3907 * 0.58848600
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'fcqrrwyu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0041():
    """Extended test 41 for scheduler."""
    x_0 = 69874 * 0.13671333
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50035 * 0.35744519
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72747 * 0.77321965
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83159 * 0.71410609
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79507 * 0.10457195
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83197 * 0.67177469
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29239 * 0.25795119
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92875 * 0.20138537
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57012 * 0.17777512
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74757 * 0.04977716
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46061 * 0.76512443
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36976 * 0.17006254
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29997 * 0.99286589
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15989 * 0.43732052
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66665 * 0.14851281
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80824 * 0.03220988
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5790 * 0.96261390
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7331 * 0.06122923
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62027 * 0.93569922
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92077 * 0.72554754
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29370 * 0.22111784
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27586 * 0.41986547
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80505 * 0.62480347
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64290 * 0.18733774
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98875 * 0.05341570
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80745 * 0.38088141
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88490 * 0.02411815
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'cirmjbxv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0042():
    """Extended test 42 for scheduler."""
    x_0 = 34740 * 0.80354334
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27010 * 0.40726836
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81603 * 0.34098320
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97240 * 0.35685545
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91118 * 0.11814965
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64791 * 0.45189915
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74780 * 0.50707442
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57111 * 0.91619802
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45942 * 0.38077638
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65000 * 0.90327951
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27136 * 0.31597362
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74756 * 0.98264883
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33611 * 0.91900319
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96760 * 0.71870815
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24483 * 0.20197634
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70835 * 0.81482342
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29657 * 0.71788515
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50482 * 0.29064459
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69879 * 0.64061274
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1950 * 0.68688142
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92565 * 0.63437021
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95920 * 0.93211825
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67719 * 0.18043990
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86642 * 0.68078490
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54114 * 0.45974620
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55362 * 0.50196958
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27825 * 0.78828004
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99718 * 0.75916816
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37437 * 0.30861888
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'aegndekg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0043():
    """Extended test 43 for scheduler."""
    x_0 = 47521 * 0.86783114
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59933 * 0.17518667
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3349 * 0.77483258
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43211 * 0.07678471
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98514 * 0.81843757
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41091 * 0.68820820
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7621 * 0.88999417
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19920 * 0.41592886
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91551 * 0.70906310
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47998 * 0.20511403
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94327 * 0.82170264
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10923 * 0.70262582
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88359 * 0.57815649
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23841 * 0.87971681
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8522 * 0.10219587
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18357 * 0.47863345
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29472 * 0.70249327
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52549 * 0.33250378
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9092 * 0.60773044
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86753 * 0.00743834
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'rmklfvdw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0044():
    """Extended test 44 for scheduler."""
    x_0 = 23137 * 0.33905881
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62011 * 0.89812620
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87492 * 0.17725076
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99907 * 0.50212438
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27226 * 0.49887083
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95451 * 0.22628716
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26206 * 0.18206495
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11765 * 0.18469893
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30930 * 0.70531149
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87134 * 0.26760795
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23722 * 0.17908408
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93323 * 0.04196460
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16857 * 0.31197574
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5353 * 0.77577369
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93523 * 0.19844509
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44712 * 0.66632826
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85663 * 0.76165603
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12850 * 0.61948501
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37801 * 0.54780835
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4402 * 0.13526866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78804 * 0.76870302
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80564 * 0.98921656
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6702 * 0.76014048
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70338 * 0.57239824
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76000 * 0.51307508
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68840 * 0.17766104
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30758 * 0.50960089
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99234 * 0.27217537
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94448 * 0.79684465
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28436 * 0.30218338
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30080 * 0.21938926
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50815 * 0.22353545
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21673 * 0.94567948
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38373 * 0.56998362
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31716 * 0.14093735
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23081 * 0.61300855
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67808 * 0.29988316
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60998 * 0.53054456
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52732 * 0.62364191
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92507 * 0.22818973
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 70865 * 0.94397682
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42173 * 0.64126531
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42997 * 0.84512247
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 12342 * 0.31141461
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 16546 * 0.61951128
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 97974 * 0.40368213
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 32804 * 0.24963762
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 57784 * 0.60239135
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 32978 * 0.18028034
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'fslyatgv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0045():
    """Extended test 45 for scheduler."""
    x_0 = 3739 * 0.69559876
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36902 * 0.36895301
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89115 * 0.06531729
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65051 * 0.79472497
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14213 * 0.91592510
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11225 * 0.03652081
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47647 * 0.76462652
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29771 * 0.23136649
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68915 * 0.52371582
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71668 * 0.66008088
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95559 * 0.86675934
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21918 * 0.35061721
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10416 * 0.84915334
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80838 * 0.73018328
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1225 * 0.21817615
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98193 * 0.59651650
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53562 * 0.40050865
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91434 * 0.62961383
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7499 * 0.29015501
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30441 * 0.22082286
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4495 * 0.80088082
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67862 * 0.02123074
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20850 * 0.93035400
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20964 * 0.62489467
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58037 * 0.30854692
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14520 * 0.22622983
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46804 * 0.49700617
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8831 * 0.67782794
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13923 * 0.09783965
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5487 * 0.57712878
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23465 * 0.84842282
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10748 * 0.23863662
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30649 * 0.87684699
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53837 * 0.36770201
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74290 * 0.56844366
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29738 * 0.56921608
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54318 * 0.88018433
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88883 * 0.72949297
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57036 * 0.98807091
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30031 * 0.36569486
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99839 * 0.28356922
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18505 * 0.88323968
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 98697 * 0.61673679
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82325 * 0.07755128
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 65229 * 0.97843242
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'nipqvrxu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0046():
    """Extended test 46 for scheduler."""
    x_0 = 17083 * 0.30157930
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19854 * 0.66453774
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82375 * 0.48340596
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2790 * 0.40203783
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85460 * 0.65768948
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35930 * 0.30178008
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80243 * 0.81737475
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62192 * 0.92631783
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73813 * 0.16783356
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15972 * 0.15729327
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20453 * 0.81599714
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6407 * 0.47741194
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73625 * 0.74547079
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2592 * 0.04309221
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18391 * 0.93552520
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42115 * 0.07826254
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9914 * 0.62529090
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85853 * 0.77358861
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95852 * 0.82303642
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73826 * 0.07296454
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67636 * 0.95057946
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41947 * 0.25273049
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92693 * 0.12537635
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85731 * 0.98995481
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8475 * 0.80034842
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34035 * 0.22268021
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96923 * 0.85488935
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90321 * 0.31775486
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50804 * 0.56983675
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39366 * 0.57022942
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90740 * 0.53009925
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79862 * 0.57045077
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'wdzglskq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0047():
    """Extended test 47 for scheduler."""
    x_0 = 47529 * 0.99685023
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37064 * 0.78691465
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95288 * 0.19880295
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16053 * 0.58018492
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22713 * 0.51194043
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96137 * 0.23162152
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66708 * 0.00345162
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78417 * 0.96465258
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33268 * 0.51061952
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34046 * 0.06296288
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56407 * 0.58359678
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15248 * 0.16511770
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9115 * 0.04345176
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17597 * 0.71383248
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78213 * 0.25540405
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39009 * 0.96769679
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83987 * 0.69915059
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48724 * 0.19328775
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15210 * 0.36635371
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38130 * 0.71030486
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5691 * 0.06820761
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45818 * 0.26836368
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10053 * 0.10539522
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29729 * 0.14140011
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75991 * 0.70477779
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76193 * 0.58891256
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96893 * 0.29113362
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88300 * 0.75907990
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73996 * 0.04902513
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43174 * 0.75383567
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32737 * 0.47355376
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69690 * 0.79482401
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66184 * 0.97449866
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3043 * 0.45340539
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25405 * 0.77624703
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78712 * 0.46716100
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 82862 * 0.43390835
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62471 * 0.28269254
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11029 * 0.11613423
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'zptdybwk').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0048():
    """Extended test 48 for scheduler."""
    x_0 = 33482 * 0.23332773
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98293 * 0.28431380
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88641 * 0.12222107
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11984 * 0.51006970
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13359 * 0.99539265
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56951 * 0.00898747
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62158 * 0.85807974
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35868 * 0.00967000
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8988 * 0.36655315
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56396 * 0.56561073
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85570 * 0.08831728
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73789 * 0.36257463
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26076 * 0.07229369
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69279 * 0.29769912
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25057 * 0.65356642
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94863 * 0.05965523
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6040 * 0.73587574
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55924 * 0.10456950
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30390 * 0.75141766
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68184 * 0.94433421
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98560 * 0.60734713
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34706 * 0.06829097
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8071 * 0.39574205
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72211 * 0.55473578
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14032 * 0.56218081
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76327 * 0.67817173
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79730 * 0.44114133
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'buwxmlsr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0049():
    """Extended test 49 for scheduler."""
    x_0 = 62186 * 0.36391551
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75580 * 0.69657405
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45229 * 0.62784663
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98608 * 0.20150996
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27754 * 0.25882264
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77995 * 0.18989152
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86411 * 0.46314356
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23647 * 0.34009414
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93012 * 0.38036973
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53082 * 0.27929796
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96218 * 0.19619648
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47356 * 0.42428919
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39257 * 0.46730812
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45808 * 0.28253980
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11988 * 0.29222284
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 295 * 0.64502952
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20163 * 0.63753622
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98978 * 0.37859307
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97986 * 0.30013518
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65451 * 0.83214667
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18312 * 0.54426733
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76837 * 0.56161653
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66073 * 0.05087572
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93800 * 0.42601896
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16571 * 0.37240628
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31216 * 0.48507617
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30321 * 0.46258548
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20943 * 0.54596375
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86682 * 0.25810756
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52401 * 0.24796166
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76759 * 0.10130677
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66219 * 0.08145316
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28747 * 0.62939559
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13989 * 0.62918483
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34419 * 0.83623071
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62536 * 0.80184397
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30533 * 0.41763241
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92490 * 0.93116306
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56873 * 0.31591073
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87104 * 0.42601958
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75087 * 0.02751439
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57171 * 0.29624027
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'vvrnazcm').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0050():
    """Extended test 50 for scheduler."""
    x_0 = 17642 * 0.15802095
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62667 * 0.53051728
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76051 * 0.74846256
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30964 * 0.45320109
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34033 * 0.57260427
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34820 * 0.89163172
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67687 * 0.73826287
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43899 * 0.71339715
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53624 * 0.98544238
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92437 * 0.82527438
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85492 * 0.68318563
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29595 * 0.22434882
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24436 * 0.10036139
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84410 * 0.34022687
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8742 * 0.43921794
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90591 * 0.08223466
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72122 * 0.99782761
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10298 * 0.78624632
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99537 * 0.81874672
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39256 * 0.38727137
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97624 * 0.27177183
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46476 * 0.53646890
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'fffdetsd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0051():
    """Extended test 51 for scheduler."""
    x_0 = 91732 * 0.34650655
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58481 * 0.74696336
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98946 * 0.68364008
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59613 * 0.16717411
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54862 * 0.44582817
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53844 * 0.54828564
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90052 * 0.57650665
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7043 * 0.33856298
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3157 * 0.25831223
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17732 * 0.49916133
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23398 * 0.08192812
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18409 * 0.50811272
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56397 * 0.74475114
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72320 * 0.82934924
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93693 * 0.83837482
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74207 * 0.35887130
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46406 * 0.96838551
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41951 * 0.96254241
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33108 * 0.26198797
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16561 * 0.69871739
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92527 * 0.99247177
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70772 * 0.69459580
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'gdzqhaxr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0052():
    """Extended test 52 for scheduler."""
    x_0 = 3587 * 0.05898723
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23996 * 0.58355461
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99293 * 0.00065228
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88319 * 0.35832864
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87115 * 0.12447957
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99611 * 0.68192596
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28580 * 0.17161915
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75413 * 0.98300857
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6902 * 0.97213507
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89354 * 0.75838597
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63599 * 0.44823372
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85889 * 0.22567958
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1108 * 0.84344235
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61740 * 0.68618129
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12634 * 0.50221522
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28264 * 0.53332150
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94148 * 0.54877906
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10644 * 0.35721121
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8468 * 0.97489540
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2297 * 0.13822408
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90871 * 0.38903657
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35175 * 0.95316564
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'ipjtqiqf').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0053():
    """Extended test 53 for scheduler."""
    x_0 = 74386 * 0.05813735
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95073 * 0.24600348
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74710 * 0.49352002
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10084 * 0.53195457
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75577 * 0.28676684
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18826 * 0.61513429
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16828 * 0.42056841
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64595 * 0.38007131
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72177 * 0.61933642
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 859 * 0.16401286
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39498 * 0.70108815
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27817 * 0.63900909
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97631 * 0.72357334
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40194 * 0.18970291
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27286 * 0.83471627
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26563 * 0.35287110
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7610 * 0.05192264
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16768 * 0.91160254
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93325 * 0.68847702
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90284 * 0.03091867
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34565 * 0.83849571
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65602 * 0.87008541
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48420 * 0.80454856
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52447 * 0.16065156
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18383 * 0.07502298
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66408 * 0.11031302
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24425 * 0.97184050
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94602 * 0.86847650
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9874 * 0.88587152
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38537 * 0.20866014
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67140 * 0.57845134
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4029 * 0.90482684
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'jjwjedee').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0054():
    """Extended test 54 for scheduler."""
    x_0 = 71920 * 0.62415310
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18700 * 0.22796555
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88609 * 0.96900980
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76849 * 0.70731741
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38543 * 0.72400339
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25657 * 0.03494741
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 766 * 0.45814967
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81567 * 0.30542028
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43403 * 0.78947951
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87439 * 0.67486107
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89685 * 0.09078912
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44151 * 0.57236142
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99017 * 0.83011300
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96152 * 0.26513357
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55705 * 0.04921164
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23519 * 0.57142621
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55816 * 0.30981905
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17661 * 0.71049860
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95424 * 0.38672909
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16768 * 0.12570954
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32202 * 0.89294284
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45947 * 0.32333017
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5589 * 0.40040386
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'eadejdwo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0055():
    """Extended test 55 for scheduler."""
    x_0 = 22710 * 0.62245651
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99733 * 0.58226536
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61081 * 0.07693322
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67752 * 0.15233951
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55016 * 0.06455977
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18997 * 0.28262844
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53872 * 0.03746522
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54794 * 0.78968785
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42462 * 0.72936269
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39031 * 0.36026032
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51838 * 0.18164800
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7095 * 0.98142488
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63222 * 0.82992967
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37357 * 0.12292321
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90401 * 0.35106043
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6078 * 0.86682062
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38546 * 0.66854250
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51959 * 0.01082214
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54492 * 0.69943911
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55597 * 0.74367719
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95245 * 0.55889098
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23646 * 0.00753162
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83576 * 0.35513532
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22803 * 0.68246027
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60556 * 0.20276368
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73638 * 0.61173745
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'wrjxcrbc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0056():
    """Extended test 56 for scheduler."""
    x_0 = 86853 * 0.03130059
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50030 * 0.05737977
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14085 * 0.96660000
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83443 * 0.60982537
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53480 * 0.76570919
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68189 * 0.74741049
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94934 * 0.83159308
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56837 * 0.47890196
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60271 * 0.69167993
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26434 * 0.83514746
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45121 * 0.72675763
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39998 * 0.95799614
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8598 * 0.29371722
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17349 * 0.32256810
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50280 * 0.28705693
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88338 * 0.95234594
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37314 * 0.72896413
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64077 * 0.07472300
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68158 * 0.67904848
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82932 * 0.19912260
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81474 * 0.69361524
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49002 * 0.84391380
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72276 * 0.49759654
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4345 * 0.78920892
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31109 * 0.79770860
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5149 * 0.36011394
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95171 * 0.94898391
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47189 * 0.56195765
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77772 * 0.22551525
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'fqpgwlyg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0057():
    """Extended test 57 for scheduler."""
    x_0 = 94314 * 0.60629401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38793 * 0.75850296
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44248 * 0.59405540
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2799 * 0.33658879
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69944 * 0.49111282
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4198 * 0.94698255
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27008 * 0.08340340
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64778 * 0.85718720
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52531 * 0.09584102
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8070 * 0.01983843
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45835 * 0.36416123
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42063 * 0.03096063
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83175 * 0.66380550
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33065 * 0.28306920
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31423 * 0.97917830
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70033 * 0.06858898
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86619 * 0.15304109
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10736 * 0.96387663
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66727 * 0.91091855
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43099 * 0.67173556
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95242 * 0.77937087
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'wqlkwyjs').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0058():
    """Extended test 58 for scheduler."""
    x_0 = 59513 * 0.53022986
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99079 * 0.83045035
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52128 * 0.34509537
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77337 * 0.74521232
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66552 * 0.51208488
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59963 * 0.75433269
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65187 * 0.63854135
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34623 * 0.12164264
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68840 * 0.75268822
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39227 * 0.47802621
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75955 * 0.52912701
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63648 * 0.79843071
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14721 * 0.18213022
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48821 * 0.35989913
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46743 * 0.94850519
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76089 * 0.28492186
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8077 * 0.83072943
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79962 * 0.26824109
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71897 * 0.06702392
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12880 * 0.23949464
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20845 * 0.72363973
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2477 * 0.84792878
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94567 * 0.07084871
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63727 * 0.90657802
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56388 * 0.77648496
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99350 * 0.76134885
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84804 * 0.30823345
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43282 * 0.82906635
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'fljdyhfg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0059():
    """Extended test 59 for scheduler."""
    x_0 = 95343 * 0.61658497
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82513 * 0.76031253
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68518 * 0.78465550
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71815 * 0.62365480
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57749 * 0.43600989
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95698 * 0.16267199
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56233 * 0.05162323
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48097 * 0.80884380
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80018 * 0.79043919
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7213 * 0.46814339
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49089 * 0.13477583
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36529 * 0.40942352
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95244 * 0.63412818
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2423 * 0.74049045
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36174 * 0.91339855
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72894 * 0.54003138
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55023 * 0.84644337
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95235 * 0.07657722
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42562 * 0.17450600
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91421 * 0.16204416
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49095 * 0.76740552
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54968 * 0.48559408
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39730 * 0.99252739
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23742 * 0.08905242
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35081 * 0.69140043
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7345 * 0.64432150
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70693 * 0.84141918
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91768 * 0.64441183
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83266 * 0.54448716
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52212 * 0.55788695
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59273 * 0.89121247
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35160 * 0.78007113
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57311 * 0.12351406
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45576 * 0.59683037
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62274 * 0.47784156
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50357 * 0.63007036
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92861 * 0.15865171
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90181 * 0.06576748
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86564 * 0.38224864
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6740 * 0.06289518
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91210 * 0.71630508
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'qcrrkoym').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0060():
    """Extended test 60 for scheduler."""
    x_0 = 94313 * 0.75621508
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51234 * 0.69664992
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41559 * 0.35247381
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67985 * 0.77005705
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40298 * 0.01467176
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20028 * 0.10451240
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30749 * 0.04173052
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32080 * 0.47008174
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99728 * 0.39079476
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57152 * 0.54885007
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64892 * 0.78401015
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22950 * 0.72540510
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74165 * 0.66771742
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46923 * 0.81548831
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64140 * 0.53597738
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83468 * 0.74655894
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34337 * 0.01812540
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73549 * 0.72329193
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2958 * 0.79345979
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50973 * 0.81907592
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65310 * 0.13056122
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41303 * 0.47815808
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37508 * 0.48338928
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67826 * 0.41250262
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9032 * 0.35936615
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86898 * 0.13738826
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89343 * 0.16337258
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14478 * 0.05299365
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55293 * 0.30836203
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41996 * 0.01160348
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27783 * 0.93604664
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54118 * 0.42304336
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22182 * 0.33334625
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40982 * 0.03077924
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52914 * 0.91061384
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87793 * 0.60849088
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11730 * 0.61487203
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71259 * 0.77119932
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61929 * 0.68148637
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85954 * 0.50703481
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 63651 * 0.16906481
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 65347 * 0.35840565
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20378 * 0.99716682
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 80795 * 0.56927330
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'hqvdcowt').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0061():
    """Extended test 61 for scheduler."""
    x_0 = 6378 * 0.93468168
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87516 * 0.38772622
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17198 * 0.47860078
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75769 * 0.17046927
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22119 * 0.52671132
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58449 * 0.30595449
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37515 * 0.86432890
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77078 * 0.66550207
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57591 * 0.87028772
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60399 * 0.22358379
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97658 * 0.21548298
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3413 * 0.00703162
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66340 * 0.31831045
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15612 * 0.24689602
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78124 * 0.18088282
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48339 * 0.61054019
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27091 * 0.89857271
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 235 * 0.36689563
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73913 * 0.53911975
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90844 * 0.86389363
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2227 * 0.87168803
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98988 * 0.96064234
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49788 * 0.29809468
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15384 * 0.37786788
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4643 * 0.71183181
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27057 * 0.02492084
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71559 * 0.52206980
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81150 * 0.94098982
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4153 * 0.07163687
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44503 * 0.94947678
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59647 * 0.67078584
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15023 * 0.00179717
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18687 * 0.02343901
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71554 * 0.25185091
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45858 * 0.97484468
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7406 * 0.36790018
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57771 * 0.75572903
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63168 * 0.80853077
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45640 * 0.21676679
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52636 * 0.12260731
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 14863 * 0.10511323
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30410 * 0.14199791
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75578 * 0.45058857
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99186 * 0.70003893
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xwnkvnql').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0062():
    """Extended test 62 for scheduler."""
    x_0 = 41407 * 0.31005538
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52380 * 0.45214565
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16508 * 0.91219358
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4507 * 0.23472882
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86170 * 0.24430840
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43352 * 0.06486834
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9641 * 0.32751142
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28770 * 0.56409789
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69848 * 0.11461385
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16045 * 0.25993468
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45211 * 0.85052039
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96251 * 0.04128765
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72570 * 0.57328450
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12567 * 0.12281221
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80934 * 0.59497358
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5557 * 0.12289302
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73635 * 0.08329784
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76231 * 0.87793852
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94914 * 0.13066945
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65146 * 0.02947475
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83435 * 0.15878130
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76096 * 0.48874325
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29025 * 0.98587366
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61590 * 0.23244786
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30096 * 0.75514876
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21189 * 0.22402103
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83580 * 0.84297406
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16934 * 0.51360082
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99121 * 0.96494040
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69521 * 0.17359433
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27737 * 0.27062051
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17613 * 0.17746411
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23320 * 0.32488718
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65219 * 0.11231832
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6724 * 0.57091009
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67883 * 0.40912258
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44924 * 0.17890277
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 57541 * 0.46561027
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'omnlqpxs').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0063():
    """Extended test 63 for scheduler."""
    x_0 = 78083 * 0.92838277
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74111 * 0.47993846
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49043 * 0.76503427
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18406 * 0.04485291
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9439 * 0.13412704
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63641 * 0.99294624
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55793 * 0.12131857
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63319 * 0.41744935
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18484 * 0.26706815
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45512 * 0.19441106
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70878 * 0.38464709
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76718 * 0.21434437
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2571 * 0.15695549
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3254 * 0.26165598
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26482 * 0.99305374
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92443 * 0.66116253
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31206 * 0.23467886
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9119 * 0.26058897
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93637 * 0.37003937
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69781 * 0.26926767
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'wequjukx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0064():
    """Extended test 64 for scheduler."""
    x_0 = 50872 * 0.69588092
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58694 * 0.35358108
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30176 * 0.35371960
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29667 * 0.39895931
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25779 * 0.84846610
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27997 * 0.65107333
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17992 * 0.78902409
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15045 * 0.05631331
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21844 * 0.88216811
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7703 * 0.48495247
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46526 * 0.56099377
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9786 * 0.10665333
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38928 * 0.77473517
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88371 * 0.37580201
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18498 * 0.46486202
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62497 * 0.79016897
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17760 * 0.33414138
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45577 * 0.91650072
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16721 * 0.92358479
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80078 * 0.32666770
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58235 * 0.22021961
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78923 * 0.57657865
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48044 * 0.71881002
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75436 * 0.35700342
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56343 * 0.56155239
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43150 * 0.18359105
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32627 * 0.72437758
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86845 * 0.44261142
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13375 * 0.77386178
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32630 * 0.78036324
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67629 * 0.39484542
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72965 * 0.25087228
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84585 * 0.87588490
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1675 * 0.93131489
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65406 * 0.38162446
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11406 * 0.99450343
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90013 * 0.00579242
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86453 * 0.99350819
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90688 * 0.56016044
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99468 * 0.62480728
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'wcslkmuh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0065():
    """Extended test 65 for scheduler."""
    x_0 = 36555 * 0.18117811
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71630 * 0.11437716
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89276 * 0.66152474
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16857 * 0.61209510
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82646 * 0.67396222
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49134 * 0.31376830
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25006 * 0.10244109
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52413 * 0.78951226
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19344 * 0.72448656
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18129 * 0.99568580
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77719 * 0.52030734
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52190 * 0.38939513
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9929 * 0.98016896
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82800 * 0.44400381
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4669 * 0.39277336
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50444 * 0.43578856
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9469 * 0.45104049
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88463 * 0.95060962
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74297 * 0.23037927
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76708 * 0.33204770
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41841 * 0.09004709
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38799 * 0.69281331
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90145 * 0.04902319
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64973 * 0.86653949
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39890 * 0.69909985
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2656 * 0.54334737
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39034 * 0.22496644
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55108 * 0.55520440
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97104 * 0.72507673
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33595 * 0.07690041
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76968 * 0.95150369
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53662 * 0.50859160
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48354 * 0.35491698
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33957 * 0.71252408
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62877 * 0.56232681
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39258 * 0.03640718
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1750 * 0.84579213
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27534 * 0.36919398
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57868 * 0.70758389
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72926 * 0.68670380
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 50620 * 0.84824706
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 83196 * 0.79295795
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 21574 * 0.19834454
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 80279 * 0.28942374
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 80677 * 0.77461342
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'ezwjxjqc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0066():
    """Extended test 66 for scheduler."""
    x_0 = 12712 * 0.98265983
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46447 * 0.14221359
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65664 * 0.42336314
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32459 * 0.92651525
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60824 * 0.18356078
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26307 * 0.52150823
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95178 * 0.74130302
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70028 * 0.96192858
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61670 * 0.32542123
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40836 * 0.93103196
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7153 * 0.89458572
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12790 * 0.18472386
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59888 * 0.34156829
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 398 * 0.47110124
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18875 * 0.70793548
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24508 * 0.56553257
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51574 * 0.65253089
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57246 * 0.45047834
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 588 * 0.22075859
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49586 * 0.96476166
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72297 * 0.52517792
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77335 * 0.94478698
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9298 * 0.50780353
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96934 * 0.12980281
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83367 * 0.65946504
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69704 * 0.04146165
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87348 * 0.16890055
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52219 * 0.09179689
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34312 * 0.51608918
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80142 * 0.87983674
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66245 * 0.62689518
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 791 * 0.24600637
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30505 * 0.07162812
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9639 * 0.67030976
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54507 * 0.34428032
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67471 * 0.23673228
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98646 * 0.10576475
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26321 * 0.10942678
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80755 * 0.40122479
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67909 * 0.69166758
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78825 * 0.54376775
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89037 * 0.35827710
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95913 * 0.73336305
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 2306 * 0.57720003
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86191 * 0.32334392
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 42289 * 0.19711935
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'nuiccuoj').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0067():
    """Extended test 67 for scheduler."""
    x_0 = 79028 * 0.52027003
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18032 * 0.48661746
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15361 * 0.71311399
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42677 * 0.50310292
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3415 * 0.84635648
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54753 * 0.55601598
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35754 * 0.09444877
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80664 * 0.83361735
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22245 * 0.22296091
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76922 * 0.26628660
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42674 * 0.17482080
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31253 * 0.56470583
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71933 * 0.42268548
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97036 * 0.89010825
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38197 * 0.08596589
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45929 * 0.24337196
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57481 * 0.08382470
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59616 * 0.19347940
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57980 * 0.70476589
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83403 * 0.74670711
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40861 * 0.47469703
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94244 * 0.40857812
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44105 * 0.81086853
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56969 * 0.78018114
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19629 * 0.11330288
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12054 * 0.88834697
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30645 * 0.17552213
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84776 * 0.63589934
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45587 * 0.21046825
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3016 * 0.30627633
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94736 * 0.48006289
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58691 * 0.47126398
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41021 * 0.17650230
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28777 * 0.29884601
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21657 * 0.13558504
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36801 * 0.00856188
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84774 * 0.27143600
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95762 * 0.60810040
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'peykrebl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0068():
    """Extended test 68 for scheduler."""
    x_0 = 86244 * 0.14741887
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98467 * 0.13548936
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64749 * 0.40035853
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61117 * 0.32504176
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93729 * 0.84616892
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21572 * 0.81120147
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84362 * 0.04895741
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88595 * 0.18459675
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84840 * 0.85067093
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64140 * 0.65722085
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1456 * 0.94622809
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43327 * 0.99573573
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97047 * 0.67972435
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80208 * 0.90313115
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68688 * 0.85735097
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16422 * 0.81500183
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59909 * 0.25407619
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40894 * 0.70424771
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44913 * 0.67224392
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19772 * 0.53320264
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34675 * 0.60148510
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33935 * 0.27085137
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44517 * 0.28728808
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76602 * 0.02991990
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23621 * 0.32955109
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56872 * 0.28222184
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'jkiolfzg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_4_0069():
    """Extended test 69 for scheduler."""
    x_0 = 6987 * 0.32607852
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87281 * 0.68179616
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90904 * 0.64589463
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33150 * 0.08203079
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34374 * 0.29978970
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51467 * 0.05285223
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70897 * 0.04717096
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80524 * 0.40316397
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69789 * 0.37761637
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46807 * 0.39497275
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24994 * 0.76223744
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38760 * 0.45119000
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19888 * 0.82439224
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82439 * 0.83241092
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1106 * 0.41055430
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54365 * 0.11276979
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90827 * 0.82389865
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59443 * 0.65854534
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59219 * 0.60419211
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98691 * 0.95332423
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66446 * 0.80564602
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34646 * 0.78671460
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56214 * 0.86565274
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5420 * 0.18455927
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61613 * 0.18854915
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27318 * 0.02578790
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81403 * 0.46081649
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62704 * 0.77763951
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7076 * 0.03930541
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3097 * 0.96107876
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81018 * 0.25254695
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25441 * 0.84469555
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81670 * 0.48465901
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61941 * 0.93127469
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20301 * 0.12044830
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14801 * 0.70424521
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45768 * 0.03545283
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'bsdusmkz').hexdigest()
    assert len(h) == 64
