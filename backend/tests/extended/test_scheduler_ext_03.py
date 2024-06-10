"""Extended tests for scheduler suite 3."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_scheduler_extended_3_0000():
    """Extended test 0 for scheduler."""
    x_0 = 57327 * 0.41023445
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61386 * 0.75100101
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37123 * 0.83135128
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39157 * 0.01267409
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40692 * 0.97173631
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14881 * 0.50763123
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42060 * 0.74783666
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55897 * 0.37357786
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74126 * 0.64958459
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29874 * 0.62732121
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82533 * 0.22550737
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83911 * 0.63012516
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65373 * 0.44509406
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62602 * 0.62333440
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9715 * 0.58986661
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43903 * 0.43659296
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96404 * 0.38391304
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98875 * 0.99863162
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38833 * 0.77509410
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51950 * 0.02309487
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27828 * 0.35523326
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2217 * 0.38156218
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28466 * 0.36050736
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69067 * 0.28655558
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8482 * 0.75885649
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'pcorlbzq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0001():
    """Extended test 1 for scheduler."""
    x_0 = 94270 * 0.44111132
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19282 * 0.35940256
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40829 * 0.59485688
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49967 * 0.35651888
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94835 * 0.74586868
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23064 * 0.17357835
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96444 * 0.97431960
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60002 * 0.88443813
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69389 * 0.75534384
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33060 * 0.52157957
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93482 * 0.64089753
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3847 * 0.48389152
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47910 * 0.34592616
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17620 * 0.56337749
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81811 * 0.55968060
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69102 * 0.56629631
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90468 * 0.67780596
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28511 * 0.71590575
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89862 * 0.08830942
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65079 * 0.18012502
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2811 * 0.35886794
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51437 * 0.62584265
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99477 * 0.49143480
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1617 * 0.77350020
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13222 * 0.17516719
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95647 * 0.41804869
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76146 * 0.06170435
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62481 * 0.45481269
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50727 * 0.13501303
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65552 * 0.36697983
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20374 * 0.60415879
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15980 * 0.90758318
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41837 * 0.74691884
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'pdoaapff').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0002():
    """Extended test 2 for scheduler."""
    x_0 = 56226 * 0.17016405
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72177 * 0.72949099
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12644 * 0.00919240
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48377 * 0.31691395
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31999 * 0.30439220
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77596 * 0.18868761
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15694 * 0.76979164
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69927 * 0.54878655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37590 * 0.68513098
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74377 * 0.02104403
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67251 * 0.94467263
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76482 * 0.22769919
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5619 * 0.74668742
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51705 * 0.40619227
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 775 * 0.33258750
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36260 * 0.85793974
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45740 * 0.98819964
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73809 * 0.04079660
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26616 * 0.27117053
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83500 * 0.68206882
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64102 * 0.23425659
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74766 * 0.80657997
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2646 * 0.69260257
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66589 * 0.06218279
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95486 * 0.38256699
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76886 * 0.88730085
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33215 * 0.60353985
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3164 * 0.03846627
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72674 * 0.97710268
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24789 * 0.04781252
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75415 * 0.75273804
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41470 * 0.32336248
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18010 * 0.67080849
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2842 * 0.42101104
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46781 * 0.41817051
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90641 * 0.36291302
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96070 * 0.77314315
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45272 * 0.42178034
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94481 * 0.18555868
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45217 * 0.22242439
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60794 * 0.64110314
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92146 * 0.92352665
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18166 * 0.71168328
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 71750 * 0.73446572
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'ubjykxlr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0003():
    """Extended test 3 for scheduler."""
    x_0 = 51150 * 0.90212963
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80579 * 0.23408426
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43131 * 0.48968024
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36414 * 0.28601437
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23643 * 0.96120857
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7680 * 0.07976301
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79677 * 0.25034089
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13105 * 0.40575931
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46316 * 0.84697697
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26757 * 0.02927083
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37325 * 0.45314891
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93753 * 0.53482320
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42694 * 0.27407497
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89950 * 0.75842665
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12129 * 0.76365253
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8690 * 0.42423481
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36320 * 0.11474754
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27776 * 0.80096790
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21352 * 0.75643533
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59377 * 0.96063978
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59552 * 0.85242927
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31360 * 0.77857055
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98097 * 0.27542186
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57414 * 0.94329182
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51480 * 0.61205841
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94079 * 0.27023201
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61340 * 0.84821255
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24800 * 0.63139092
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50750 * 0.79259368
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40638 * 0.32040182
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51160 * 0.35020869
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37514 * 0.76682466
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57716 * 0.02984764
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42775 * 0.26671343
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51756 * 0.67135151
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18020 * 0.87226463
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42972 * 0.87765677
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 14139 * 0.49708946
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 50160 * 0.19072720
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79057 * 0.93051469
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 30893 * 0.99896916
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71175 * 0.16126463
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 482 * 0.96637275
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'wemzoour').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0004():
    """Extended test 4 for scheduler."""
    x_0 = 22439 * 0.02963509
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19888 * 0.56831664
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68454 * 0.44435787
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68527 * 0.96106066
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32960 * 0.73479157
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19386 * 0.74897016
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91562 * 0.22130447
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93138 * 0.03181892
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44090 * 0.53386362
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68919 * 0.37052337
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50202 * 0.46322916
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72582 * 0.88082307
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25483 * 0.08162632
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47091 * 0.82744165
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39822 * 0.22992070
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89286 * 0.06812513
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92233 * 0.37692787
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68802 * 0.16714444
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24672 * 0.38948104
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80658 * 0.32108940
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12391 * 0.54602729
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14821 * 0.00671581
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54440 * 0.38122946
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33762 * 0.57026974
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66780 * 0.44896905
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43467 * 0.96025772
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78132 * 0.09884281
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76131 * 0.95602251
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44587 * 0.17332159
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14480 * 0.29952833
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88190 * 0.90245172
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4895 * 0.64021423
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11911 * 0.54140478
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'nakwmott').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0005():
    """Extended test 5 for scheduler."""
    x_0 = 64816 * 0.83145001
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76214 * 0.60374564
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75483 * 0.98048014
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18908 * 0.90287723
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82979 * 0.60328274
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52906 * 0.29146414
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53339 * 0.95637567
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17819 * 0.14602709
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9585 * 0.32132374
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69749 * 0.78473187
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89942 * 0.57749655
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37949 * 0.42092674
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34550 * 0.44073244
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18994 * 0.12758387
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11938 * 0.41292238
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77764 * 0.64943461
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14744 * 0.80099486
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71150 * 0.20814806
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74012 * 0.24000180
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54579 * 0.25639345
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26532 * 0.00313322
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15390 * 0.51459221
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15233 * 0.78523342
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85625 * 0.16295006
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1742 * 0.14373987
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3538 * 0.28704431
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14908 * 0.48130128
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85688 * 0.07690790
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45661 * 0.69186032
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4775 * 0.59142668
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87368 * 0.05239030
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30822 * 0.82954670
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6888 * 0.16874311
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60180 * 0.13595994
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36211 * 0.81324888
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28687 * 0.23380048
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9527 * 0.27421992
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64193 * 0.23858819
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77113 * 0.89343715
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2283 * 0.24817951
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51984 * 0.94989433
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88396 * 0.43630923
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36528 * 0.37756468
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99878 * 0.60520893
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 99985 * 0.39501410
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 84310 * 0.88896544
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 37405 * 0.45218704
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 88987 * 0.52056125
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 30063 * 0.92875485
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'nynbxzpt').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0006():
    """Extended test 6 for scheduler."""
    x_0 = 81079 * 0.89687241
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91678 * 0.97846489
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66123 * 0.95945313
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78732 * 0.67303537
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69629 * 0.77761716
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70547 * 0.90382411
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10620 * 0.38607224
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12317 * 0.91208992
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48602 * 0.08503221
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98473 * 0.04808734
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31134 * 0.54266386
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37044 * 0.36855005
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64403 * 0.28584757
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34517 * 0.18411166
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8466 * 0.55436180
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19711 * 0.40414784
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84641 * 0.48576917
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45295 * 0.87685626
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11816 * 0.80678976
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2264 * 0.08462658
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38122 * 0.86496532
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99499 * 0.78331832
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61358 * 0.93740466
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99374 * 0.35589518
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6739 * 0.38109575
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1443 * 0.06542470
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46625 * 0.22357012
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22701 * 0.34020860
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60581 * 0.87108980
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11340 * 0.40676043
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50889 * 0.80945743
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33082 * 0.10257239
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14559 * 0.25993249
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46090 * 0.77750164
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73299 * 0.83413120
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20411 * 0.84737461
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72552 * 0.09205375
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66702 * 0.06966194
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47778 * 0.35115334
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28062 * 0.89121244
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17913 * 0.95849586
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67218 * 0.72048741
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 97644 * 0.47154155
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 31462 * 0.97480935
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 97423 * 0.03386341
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 31442 * 0.57789146
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 27775 * 0.95773723
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'jpqzsofp').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0007():
    """Extended test 7 for scheduler."""
    x_0 = 76855 * 0.41648765
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14101 * 0.91696520
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27148 * 0.71176422
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88995 * 0.18801682
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2452 * 0.92962644
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58398 * 0.78976055
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24622 * 0.76141746
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49574 * 0.64341768
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46844 * 0.90125840
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47012 * 0.98477863
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58192 * 0.99142040
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65898 * 0.28375265
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93048 * 0.25345289
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53081 * 0.46557733
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1949 * 0.06791871
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14917 * 0.58264609
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46161 * 0.17731334
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42124 * 0.14544698
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69242 * 0.08219089
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9348 * 0.34867377
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85362 * 0.89789625
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92010 * 0.54250145
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79201 * 0.24253398
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38786 * 0.90608859
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65574 * 0.84062869
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80047 * 0.65065122
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63140 * 0.07325467
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2191 * 0.91707536
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'jfriwaas').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0008():
    """Extended test 8 for scheduler."""
    x_0 = 5779 * 0.64874549
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83529 * 0.33805800
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89508 * 0.71871485
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14859 * 0.20915486
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37344 * 0.84493759
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71048 * 0.35573591
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9705 * 0.82626834
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29100 * 0.93201805
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48610 * 0.30253915
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89713 * 0.33188628
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25124 * 0.49845587
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8422 * 0.76977681
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12508 * 0.43605329
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21981 * 0.29808234
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58018 * 0.44405296
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97094 * 0.85410738
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61981 * 0.30711290
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59121 * 0.47539922
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55025 * 0.64407468
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60219 * 0.88276105
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20707 * 0.89016276
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8749 * 0.01441323
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'hklkhmll').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0009():
    """Extended test 9 for scheduler."""
    x_0 = 88331 * 0.43362297
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79105 * 0.61550517
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16598 * 0.05265036
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18967 * 0.61205940
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14541 * 0.39461928
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76552 * 0.89323289
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76639 * 0.94188245
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61741 * 0.31217303
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66747 * 0.98191087
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54114 * 0.40019519
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58350 * 0.38959584
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49931 * 0.23539385
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29643 * 0.88042438
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8063 * 0.06423487
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39451 * 0.69730107
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59 * 0.55144623
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40711 * 0.58654828
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97424 * 0.40354700
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2920 * 0.63953583
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89573 * 0.59799561
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70060 * 0.18767886
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71445 * 0.38650338
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1540 * 0.35477659
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85712 * 0.36556395
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23142 * 0.16342509
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45744 * 0.34854353
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38996 * 0.80351989
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42078 * 0.38434304
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18672 * 0.02415252
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2267 * 0.62991552
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11142 * 0.85240155
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63217 * 0.63269813
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41327 * 0.90989101
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11128 * 0.40173964
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43738 * 0.65225122
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'upxldtby').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0010():
    """Extended test 10 for scheduler."""
    x_0 = 13746 * 0.96715884
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67634 * 0.82184703
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70598 * 0.26015746
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53770 * 0.34287178
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78255 * 0.98701053
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92550 * 0.15050673
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91838 * 0.55706437
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66152 * 0.76408115
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64561 * 0.12705398
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15446 * 0.41385428
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96179 * 0.33642703
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86976 * 0.68414673
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56047 * 0.29262675
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62208 * 0.66773911
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59114 * 0.18854408
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66955 * 0.47428129
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31936 * 0.27591077
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27337 * 0.68446190
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37280 * 0.33901973
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80851 * 0.83544569
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89766 * 0.46205495
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83191 * 0.47848386
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75602 * 0.55885150
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43686 * 0.56891030
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19851 * 0.55056022
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53654 * 0.35823050
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67611 * 0.75618615
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15896 * 0.75345986
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23965 * 0.83309144
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36126 * 0.60662778
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47173 * 0.15475595
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74323 * 0.99865732
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25753 * 0.81468466
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78270 * 0.60078617
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33598 * 0.90371386
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65232 * 0.44704644
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73496 * 0.67748347
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44099 * 0.65774150
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44181 * 0.73561678
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42203 * 0.96160651
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65785 * 0.26340477
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42904 * 0.95041664
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 85866 * 0.01361086
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 33109 * 0.51611324
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 25868 * 0.23800099
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 72490 * 0.03761318
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 44840 * 0.38396245
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'hotwmxhj').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0011():
    """Extended test 11 for scheduler."""
    x_0 = 49303 * 0.83653582
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80990 * 0.17169743
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8477 * 0.73700783
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86365 * 0.44924631
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43807 * 0.85073243
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54247 * 0.36218663
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13381 * 0.88389493
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22290 * 0.56505408
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52711 * 0.97848789
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10206 * 0.84362605
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61949 * 0.06877965
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65645 * 0.68734575
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71320 * 0.66562430
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44904 * 0.95141386
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75140 * 0.94394956
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10125 * 0.89697916
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33762 * 0.80502552
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29955 * 0.13515918
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50127 * 0.51042521
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22665 * 0.04502428
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61768 * 0.90774990
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9395 * 0.37749247
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56894 * 0.90098508
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13593 * 0.08798760
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'uhcavxse').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0012():
    """Extended test 12 for scheduler."""
    x_0 = 28086 * 0.69546074
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26750 * 0.19649614
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41064 * 0.47342260
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14679 * 0.09559981
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5816 * 0.76028281
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88777 * 0.89688622
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33464 * 0.46944751
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53543 * 0.00055112
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48191 * 0.73405110
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44728 * 0.64261804
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62397 * 0.85328974
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68352 * 0.53403952
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12993 * 0.45220397
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26517 * 0.88845056
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82348 * 0.34997525
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80053 * 0.21572620
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29686 * 0.04303838
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31250 * 0.36938834
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73691 * 0.70850408
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39393 * 0.58614694
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53064 * 0.74377525
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22987 * 0.87128736
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4503 * 0.29816571
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93428 * 0.20639543
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71278 * 0.90206745
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52955 * 0.51059200
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11777 * 0.38225354
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32612 * 0.43755906
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95614 * 0.69471483
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95090 * 0.78094068
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39366 * 0.27953870
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26955 * 0.21586088
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3345 * 0.23146584
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3599 * 0.05594077
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77324 * 0.47951019
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70004 * 0.74365783
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79468 * 0.37019170
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 14946 * 0.64495716
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5132 * 0.46414246
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64903 * 0.29272146
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85836 * 0.54548395
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14906 * 0.48032387
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16413 * 0.32708187
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 5731 * 0.60485698
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 98805 * 0.66016376
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 80908 * 0.22482382
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 11214 * 0.14694396
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 38690 * 0.92078801
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'yrztqfhu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0013():
    """Extended test 13 for scheduler."""
    x_0 = 31058 * 0.40138414
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52029 * 0.22300880
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91725 * 0.20574453
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90387 * 0.69467683
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80504 * 0.63849364
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38733 * 0.98136814
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43835 * 0.49735731
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8705 * 0.57168848
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99706 * 0.47730679
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17500 * 0.95005448
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60035 * 0.69571540
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8212 * 0.99357577
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77956 * 0.34885947
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18105 * 0.99598020
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18565 * 0.85766140
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71316 * 0.54407330
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22401 * 0.69556957
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68927 * 0.17965704
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28148 * 0.66637035
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39945 * 0.24912728
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2154 * 0.46250202
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2871 * 0.37205363
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78471 * 0.38501556
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89506 * 0.23927632
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'oiehjlxo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0014():
    """Extended test 14 for scheduler."""
    x_0 = 58670 * 0.77369310
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45543 * 0.55479830
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73885 * 0.38303450
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32369 * 0.67222250
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64713 * 0.81775740
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79342 * 0.83452660
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81130 * 0.65424747
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90908 * 0.55250159
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15808 * 0.86383837
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52209 * 0.26388289
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15211 * 0.61638289
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31234 * 0.21381221
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57796 * 0.11515652
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97706 * 0.26596200
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70194 * 0.03441309
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41319 * 0.93141771
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5587 * 0.78261417
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43566 * 0.18885577
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67708 * 0.88513751
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13418 * 0.82882331
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10185 * 0.19226898
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77443 * 0.18421710
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63131 * 0.21513927
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44537 * 0.13379738
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53589 * 0.06167033
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82930 * 0.98304625
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19877 * 0.95359332
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88792 * 0.47809413
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40020 * 0.36180490
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90943 * 0.69569906
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'jegaxcom').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0015():
    """Extended test 15 for scheduler."""
    x_0 = 20800 * 0.17231762
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38401 * 0.60121852
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59122 * 0.86485883
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90671 * 0.91268958
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32987 * 0.10551511
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14122 * 0.44493094
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44897 * 0.02455511
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83890 * 0.17024243
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57544 * 0.77679545
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63383 * 0.55976855
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84164 * 0.49108625
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35789 * 0.85487370
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98372 * 0.70366613
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2368 * 0.24168349
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29034 * 0.89474115
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24089 * 0.26434216
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94964 * 0.62370010
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75324 * 0.82402092
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76205 * 0.85924311
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37808 * 0.29523361
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84945 * 0.10969225
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40403 * 0.08779170
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70588 * 0.95487347
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89091 * 0.52263474
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49430 * 0.89155768
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85637 * 0.95808114
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89552 * 0.33344870
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68736 * 0.72763509
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3435 * 0.85382150
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80750 * 0.46865751
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5032 * 0.12437500
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43574 * 0.01975239
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5143 * 0.19328338
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20563 * 0.43773966
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89298 * 0.83027077
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48976 * 0.56388075
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23704 * 0.09933427
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'qugbrdba').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0016():
    """Extended test 16 for scheduler."""
    x_0 = 94365 * 0.56838126
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66437 * 0.01493203
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97827 * 0.68365651
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91783 * 0.73146929
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45901 * 0.30312411
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1969 * 0.95536688
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91793 * 0.48120123
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71584 * 0.71350725
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21322 * 0.14547330
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31717 * 0.89846638
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8576 * 0.01828655
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72409 * 0.20094044
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84446 * 0.25137036
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27043 * 0.88233313
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4151 * 0.82750212
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99215 * 0.66441728
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50225 * 0.77310661
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46282 * 0.82720650
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6412 * 0.64513263
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65599 * 0.90339327
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51021 * 0.66333578
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69296 * 0.60051363
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82526 * 0.03783220
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79218 * 0.87431692
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29721 * 0.46926849
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69077 * 0.93231277
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15239 * 0.09155026
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28354 * 0.04172476
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10067 * 0.98278240
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34108 * 0.72287132
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65184 * 0.41138313
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62098 * 0.32468091
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81345 * 0.64943511
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11505 * 0.20297202
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85002 * 0.66269646
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18266 * 0.27867673
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20915 * 0.44875059
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8793 * 0.62549486
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93598 * 0.92195492
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90870 * 0.26773604
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 7530 * 0.13643263
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14786 * 0.88819822
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 58605 * 0.49973955
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 50341 * 0.64708535
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 3520 * 0.89240849
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 57614 * 0.73502922
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 74283 * 0.08274328
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 22637 * 0.22003610
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'cfeymufd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0017():
    """Extended test 17 for scheduler."""
    x_0 = 43811 * 0.17592390
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52709 * 0.04270261
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2983 * 0.09605841
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92098 * 0.75568697
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11033 * 0.58182165
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88264 * 0.77596430
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50096 * 0.00960852
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38105 * 0.29664111
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62156 * 0.54882500
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29029 * 0.89284342
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89566 * 0.59904332
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40250 * 0.69250984
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99645 * 0.05596826
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35647 * 0.68286053
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18316 * 0.13886532
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54778 * 0.12394421
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93847 * 0.08989366
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84233 * 0.64984323
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15778 * 0.73011288
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34985 * 0.74436449
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38503 * 0.34495546
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39431 * 0.04059432
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35400 * 0.35336634
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50037 * 0.31200190
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61281 * 0.87362728
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32470 * 0.37437961
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89287 * 0.92264469
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42999 * 0.35799789
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41017 * 0.70322720
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44764 * 0.83601591
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45595 * 0.36771175
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5897 * 0.88638608
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71075 * 0.87305884
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80450 * 0.19829035
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52877 * 0.78505420
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46665 * 0.50637039
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1994 * 0.61353744
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87188 * 0.81705393
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67574 * 0.95184198
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3981 * 0.50899364
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53112 * 0.52897597
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 51603 * 0.71399526
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'plkcewhc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0018():
    """Extended test 18 for scheduler."""
    x_0 = 71080 * 0.02795373
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67335 * 0.49233529
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9726 * 0.47553199
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25122 * 0.34394108
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50660 * 0.68550647
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35123 * 0.21069851
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61217 * 0.96521557
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4816 * 0.62026120
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24710 * 0.24248515
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35065 * 0.42219950
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63056 * 0.54799960
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79775 * 0.85877449
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87268 * 0.88014490
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78700 * 0.76306908
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53517 * 0.07538605
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68042 * 0.94919755
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65112 * 0.15535986
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31139 * 0.08263566
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5911 * 0.24891837
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14235 * 0.67099136
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62404 * 0.64958986
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36170 * 0.99144223
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2619 * 0.19421095
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7096 * 0.89294986
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34936 * 0.24712993
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81804 * 0.39521687
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50108 * 0.81415859
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60927 * 0.57331975
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28396 * 0.63522107
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29871 * 0.79407872
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78441 * 0.23183860
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84372 * 0.11178081
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93948 * 0.87316452
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85287 * 0.55034131
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'hdvsyukj').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0019():
    """Extended test 19 for scheduler."""
    x_0 = 37623 * 0.16994607
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10936 * 0.05219995
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64823 * 0.15675456
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16798 * 0.79709486
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83312 * 0.96568673
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19443 * 0.07593899
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91876 * 0.84571118
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53504 * 0.93727614
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15390 * 0.03344768
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82777 * 0.16099329
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19733 * 0.66048436
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60586 * 0.84691020
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38529 * 0.80955507
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97038 * 0.69673010
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31490 * 0.33059979
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8945 * 0.80885089
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41126 * 0.48076785
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17752 * 0.48636946
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55359 * 0.45388509
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63093 * 0.16630714
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29491 * 0.94469374
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17851 * 0.27334662
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69929 * 0.75913773
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1987 * 0.04996182
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83974 * 0.96503330
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59482 * 0.64237401
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84262 * 0.33914202
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20164 * 0.53096477
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16406 * 0.45456942
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20972 * 0.58029673
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21618 * 0.65922472
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7867 * 0.33589029
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21127 * 0.67643836
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81957 * 0.67656254
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61780 * 0.57580795
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94093 * 0.41699038
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87435 * 0.60472784
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84210 * 0.58508810
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5788 * 0.61858157
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52147 * 0.66648956
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81823 * 0.20237903
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 75950 * 0.77944782
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 31591 * 0.51175107
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 80331 * 0.76728146
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 90968 * 0.26590686
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 40218 * 0.64600128
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 8472 * 0.56454646
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ndhbsdlf').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0020():
    """Extended test 20 for scheduler."""
    x_0 = 20418 * 0.83273101
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10446 * 0.86327819
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46212 * 0.60853769
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18977 * 0.68078927
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62875 * 0.75505484
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46177 * 0.82656071
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86767 * 0.40335684
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86812 * 0.33549532
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72372 * 0.12146666
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56683 * 0.84767152
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42391 * 0.07382558
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69120 * 0.17752882
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14623 * 0.92095003
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25766 * 0.69576091
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63017 * 0.98392118
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92499 * 0.31048849
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63499 * 0.02740063
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51900 * 0.53963314
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43372 * 0.72153785
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2103 * 0.21824535
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28854 * 0.62404327
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10049 * 0.11915045
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5549 * 0.99767114
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93836 * 0.65047143
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24638 * 0.85795862
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'lntwneep').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0021():
    """Extended test 21 for scheduler."""
    x_0 = 93285 * 0.80459619
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31449 * 0.33260512
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19557 * 0.01638781
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64119 * 0.27135319
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25592 * 0.10105412
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91809 * 0.74733014
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77987 * 0.04574490
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45546 * 0.82164262
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64184 * 0.19717231
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86508 * 0.02867351
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71942 * 0.70562298
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87778 * 0.64856838
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10602 * 0.64374922
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65635 * 0.16773079
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2572 * 0.30669584
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38290 * 0.82287175
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3308 * 0.89473055
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65965 * 0.26115660
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94503 * 0.47497608
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87397 * 0.70435456
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67744 * 0.54625853
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94909 * 0.32791827
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64997 * 0.79204045
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73571 * 0.44764962
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17168 * 0.35821329
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48419 * 0.30468786
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83334 * 0.40398485
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42853 * 0.17435287
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53370 * 0.85343548
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'aiikbrbp').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0022():
    """Extended test 22 for scheduler."""
    x_0 = 18962 * 0.76729368
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95557 * 0.68180590
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61713 * 0.53782842
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17182 * 0.44837178
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60769 * 0.04303491
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42570 * 0.29304990
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14989 * 0.67263672
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18614 * 0.21104635
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51399 * 0.78855489
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37095 * 0.22957280
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37669 * 0.48419887
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54856 * 0.70762819
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20717 * 0.27476765
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60417 * 0.07286274
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44500 * 0.42089437
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69393 * 0.35854308
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16642 * 0.02282764
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62051 * 0.04793761
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71788 * 0.72077850
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76693 * 0.57536469
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17620 * 0.21610571
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24167 * 0.07037833
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65199 * 0.77905733
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 169 * 0.15967382
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19944 * 0.78539620
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84341 * 0.74328326
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4550 * 0.30133886
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75934 * 0.79151478
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28770 * 0.94106214
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56111 * 0.62954559
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5258 * 0.12895549
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36444 * 0.58393438
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29200 * 0.08493533
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71089 * 0.08402816
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10878 * 0.03825694
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24142 * 0.23874309
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3983 * 0.18520942
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8640 * 0.04907573
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67904 * 0.35472088
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81026 * 0.67616963
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88487 * 0.16339903
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 61957 * 0.67493999
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18053 * 0.81231295
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 35118 * 0.33747750
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'yfrltyeb').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0023():
    """Extended test 23 for scheduler."""
    x_0 = 40665 * 0.54621885
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44750 * 0.13383238
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45182 * 0.06151578
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23378 * 0.86135897
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13591 * 0.11697590
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54069 * 0.87212790
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69407 * 0.29643434
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91034 * 0.38035512
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4464 * 0.88432219
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56537 * 0.17019830
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44403 * 0.66438390
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82050 * 0.74056654
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92280 * 0.45909662
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87121 * 0.24175576
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50384 * 0.11834653
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59288 * 0.88529260
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84961 * 0.61941305
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75151 * 0.34015098
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39809 * 0.17484957
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36695 * 0.24754164
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11184 * 0.88087583
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36921 * 0.42558567
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1343 * 0.72776952
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46252 * 0.68989762
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31225 * 0.06968581
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29965 * 0.70655814
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66295 * 0.71086604
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74022 * 0.82744559
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66856 * 0.59976753
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56437 * 0.24267753
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56684 * 0.89098609
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51671 * 0.58414863
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38016 * 0.17932470
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79947 * 0.69976273
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99156 * 0.62794767
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10776 * 0.91648533
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78286 * 0.32876745
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63587 * 0.54529246
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94980 * 0.61678305
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21268 * 0.85252953
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 30552 * 0.79175871
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57023 * 0.58370806
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11747 * 0.55280398
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 81581 * 0.74335792
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 46046 * 0.94849600
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 76376 * 0.68254356
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 98730 * 0.38700615
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 91021 * 0.89290171
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 25894 * 0.75743200
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'izrpqjbg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0024():
    """Extended test 24 for scheduler."""
    x_0 = 2313 * 0.10056733
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58042 * 0.08206867
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91732 * 0.68019418
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91783 * 0.36923234
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19403 * 0.74798977
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79286 * 0.75173054
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65095 * 0.47135215
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76959 * 0.46341587
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97735 * 0.91365457
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31531 * 0.31814472
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86536 * 0.31763048
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75611 * 0.08031696
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43255 * 0.59277885
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57686 * 0.11858361
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52816 * 0.00739063
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47178 * 0.25665160
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5964 * 0.60034013
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37291 * 0.03796720
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21646 * 0.27805413
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40026 * 0.62781336
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81497 * 0.18869328
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15748 * 0.98945616
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57758 * 0.03250914
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18808 * 0.69773918
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69938 * 0.44504201
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58250 * 0.06173705
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2339 * 0.26554612
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11418 * 0.22482945
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90299 * 0.40383216
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79436 * 0.75440881
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53444 * 0.91768327
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25580 * 0.58328822
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19192 * 0.90008747
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40571 * 0.84634170
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97746 * 0.51901027
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88604 * 0.75880022
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13030 * 0.48556859
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89249 * 0.45363844
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39704 * 0.24388664
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87202 * 0.77810793
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85637 * 0.38750885
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41395 * 0.38435662
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1532 * 0.39649274
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 43522 * 0.46235287
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 46377 * 0.82643074
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'jlqvlxxy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0025():
    """Extended test 25 for scheduler."""
    x_0 = 53519 * 0.96199394
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41885 * 0.10036512
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22065 * 0.83890971
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63352 * 0.00075366
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40801 * 0.08240683
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96751 * 0.83712276
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53915 * 0.32144457
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33428 * 0.54306990
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49410 * 0.34545615
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53555 * 0.05326254
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87644 * 0.25372324
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98295 * 0.89314938
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98825 * 0.54141756
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50035 * 0.12459070
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7632 * 0.05436206
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75798 * 0.84262902
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96149 * 0.92110273
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39806 * 0.87004662
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51740 * 0.67611738
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96349 * 0.35225805
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65619 * 0.52166857
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62332 * 0.60224635
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83192 * 0.38698040
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22392 * 0.31436749
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14169 * 0.45358829
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2928 * 0.29291093
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76499 * 0.66055911
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10556 * 0.10073085
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35945 * 0.37329336
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15318 * 0.56545760
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'bgnlbhqr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0026():
    """Extended test 26 for scheduler."""
    x_0 = 89937 * 0.47004708
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13067 * 0.34458122
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40157 * 0.03472153
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36128 * 0.48585488
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52776 * 0.91302233
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4469 * 0.12349556
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43942 * 0.20406026
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48777 * 0.71494300
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49671 * 0.76842591
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11460 * 0.13160686
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86980 * 0.78453900
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36606 * 0.76380181
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66635 * 0.41114209
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13031 * 0.04335378
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11228 * 0.44905645
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88748 * 0.72512441
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10826 * 0.90232748
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12711 * 0.88723010
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90346 * 0.62259962
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94796 * 0.53177308
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67288 * 0.97914070
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37162 * 0.78433487
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32268 * 0.21530153
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95236 * 0.40563905
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63534 * 0.30903145
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75092 * 0.86508122
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12381 * 0.46271582
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23846 * 0.10325959
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20559 * 0.28540957
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90073 * 0.40384813
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4183 * 0.60307185
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80653 * 0.31994032
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22115 * 0.11259937
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59043 * 0.64451785
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69713 * 0.89787550
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'qfhziimz').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0027():
    """Extended test 27 for scheduler."""
    x_0 = 8784 * 0.83390984
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45585 * 0.03496307
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68013 * 0.99502832
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44677 * 0.16853475
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65974 * 0.51158679
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98281 * 0.16888073
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21594 * 0.32356585
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24929 * 0.53873234
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25002 * 0.21829972
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73159 * 0.36546293
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99751 * 0.96736294
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65358 * 0.60285003
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69302 * 0.96730080
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12795 * 0.37538082
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61276 * 0.35462194
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33969 * 0.79634988
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16402 * 0.80477419
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58929 * 0.58136888
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65952 * 0.43045369
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25995 * 0.94351731
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98187 * 0.02455998
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'vfsrmphd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0028():
    """Extended test 28 for scheduler."""
    x_0 = 33197 * 0.10497207
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39229 * 0.81965503
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57638 * 0.44851329
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24881 * 0.98085254
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12890 * 0.56642997
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45227 * 0.00471450
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46548 * 0.88139546
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75927 * 0.27647142
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62361 * 0.68606667
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6903 * 0.96186205
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53826 * 0.78208746
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62358 * 0.93670634
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62975 * 0.28588479
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15983 * 0.76222370
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81562 * 0.91617674
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96122 * 0.67052585
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92042 * 0.19414002
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18323 * 0.51363036
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16622 * 0.13116925
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37511 * 0.49876843
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70435 * 0.69588150
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67664 * 0.15098784
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8963 * 0.47474431
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9859 * 0.50860120
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26483 * 0.68867508
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86703 * 0.05942262
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27072 * 0.07543307
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78459 * 0.58011898
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20970 * 0.69071724
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80581 * 0.41842008
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86714 * 0.85373137
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38780 * 0.03057469
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9197 * 0.54511777
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56532 * 0.76579487
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47640 * 0.32888598
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96104 * 0.46966523
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33924 * 0.28124771
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32881 * 0.70689290
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2518 * 0.40222387
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59526 * 0.71941952
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95351 * 0.37158411
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 87120 * 0.77535970
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12656 * 0.68890676
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 65561 * 0.71824950
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 58012 * 0.87883876
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 28651 * 0.63667629
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 97605 * 0.97325176
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 96524 * 0.55672489
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'tlppfgqr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0029():
    """Extended test 29 for scheduler."""
    x_0 = 13118 * 0.08266283
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27292 * 0.71940141
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80512 * 0.67265996
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86120 * 0.54141578
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42994 * 0.58363440
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56048 * 0.76197643
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96841 * 0.73820963
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34958 * 0.41974103
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39213 * 0.30960440
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11670 * 0.59921564
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50709 * 0.03791407
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56068 * 0.90803266
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20597 * 0.76903554
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60713 * 0.60960085
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15250 * 0.65128795
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94752 * 0.82807284
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36865 * 0.51701832
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12929 * 0.16147110
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27635 * 0.26395929
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19521 * 0.07276422
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33329 * 0.17606738
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6013 * 0.29912240
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15483 * 0.97282462
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71498 * 0.94699522
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56743 * 0.37443034
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22291 * 0.53952697
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34949 * 0.65308969
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55722 * 0.19497565
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83285 * 0.82132537
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33658 * 0.72729614
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20863 * 0.19079197
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79445 * 0.59553040
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54905 * 0.54331126
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97175 * 0.24983361
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91347 * 0.83501423
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26651 * 0.61611605
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35669 * 0.32974146
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64471 * 0.24352229
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77196 * 0.46823898
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73052 * 0.61325277
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64987 * 0.72922266
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42219 * 0.10688019
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 91801 * 0.40501487
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 86989 * 0.34183440
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50463 * 0.20717236
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10516 * 0.91205038
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 38775 * 0.11843729
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'yovxbcxx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0030():
    """Extended test 30 for scheduler."""
    x_0 = 18500 * 0.25584381
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68435 * 0.87744823
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 406 * 0.56158127
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77512 * 0.60540871
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36449 * 0.39292185
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26800 * 0.22212053
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16022 * 0.90949261
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87180 * 0.33734890
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77362 * 0.39764944
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50444 * 0.42096439
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30422 * 0.54830645
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93102 * 0.72139022
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76577 * 0.95014982
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61156 * 0.18883805
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43785 * 0.14208749
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17512 * 0.76947994
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93668 * 0.73082300
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17502 * 0.06371716
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26834 * 0.86437637
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75858 * 0.78769620
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40018 * 0.25097343
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27716 * 0.26095082
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2141 * 0.49962343
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73145 * 0.97843913
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23941 * 0.44446510
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26549 * 0.56224975
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'axvdnnvz').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0031():
    """Extended test 31 for scheduler."""
    x_0 = 19334 * 0.32141497
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20719 * 0.14759379
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39087 * 0.32899310
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98317 * 0.27128893
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20961 * 0.67832077
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99255 * 0.94395908
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85200 * 0.28376514
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93130 * 0.88492070
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 314 * 0.13258114
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61072 * 0.01476773
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59706 * 0.48400899
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60239 * 0.06576075
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53832 * 0.30977542
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99960 * 0.50166608
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58618 * 0.59120653
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43476 * 0.99926690
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39785 * 0.28978891
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42805 * 0.14904918
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27364 * 0.03702656
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91155 * 0.13823975
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 167 * 0.47033718
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29543 * 0.57863863
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41571 * 0.58827027
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'qceexzut').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0032():
    """Extended test 32 for scheduler."""
    x_0 = 20706 * 0.33232350
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55652 * 0.30205127
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34442 * 0.17288273
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51047 * 0.84311431
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70282 * 0.02379501
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9206 * 0.36358990
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83753 * 0.00351267
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70078 * 0.34097883
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58403 * 0.86869048
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88531 * 0.56113816
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11286 * 0.33520379
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30560 * 0.28613257
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96093 * 0.65773714
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81483 * 0.29350834
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36497 * 0.44064494
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51982 * 0.42333252
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57174 * 0.81246850
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40691 * 0.31634304
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50088 * 0.33400660
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78316 * 0.71332609
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74594 * 0.76657714
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75475 * 0.89158114
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40787 * 0.00647477
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90183 * 0.44509717
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26102 * 0.95211843
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'qlfvedrl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0033():
    """Extended test 33 for scheduler."""
    x_0 = 78930 * 0.17684496
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29587 * 0.41181429
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97474 * 0.29043158
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74627 * 0.15536584
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58510 * 0.75152860
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70262 * 0.99077902
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31050 * 0.57804422
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38958 * 0.50201736
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46665 * 0.72133602
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96125 * 0.62892911
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53926 * 0.75906980
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86458 * 0.57221793
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35823 * 0.33365404
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37899 * 0.99654435
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61088 * 0.32093489
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98909 * 0.99694268
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82397 * 0.20657812
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82945 * 0.62147857
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10873 * 0.23679091
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77408 * 0.04230981
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85519 * 0.80202497
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'jiddkriv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0034():
    """Extended test 34 for scheduler."""
    x_0 = 84375 * 0.72751087
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87328 * 0.01384941
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50854 * 0.94100031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8011 * 0.56962866
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41434 * 0.92749737
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92661 * 0.47919947
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92959 * 0.41459786
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4483 * 0.12741304
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70838 * 0.63491083
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24540 * 0.74900902
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65531 * 0.94886017
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85054 * 0.12117033
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73700 * 0.89912099
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48493 * 0.33320546
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69779 * 0.13604190
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58364 * 0.94144361
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34466 * 0.45026558
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52372 * 0.99756732
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58175 * 0.20052595
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59369 * 0.41189284
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50143 * 0.42086500
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88781 * 0.42567012
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79161 * 0.80387180
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36510 * 0.55145020
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57617 * 0.41122223
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39535 * 0.72713528
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39474 * 0.80720994
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'mceiiyys').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0035():
    """Extended test 35 for scheduler."""
    x_0 = 73602 * 0.26297771
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76556 * 0.52111508
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34334 * 0.02052923
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68953 * 0.43374967
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15798 * 0.11972677
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93555 * 0.44558203
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3242 * 0.90203217
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70927 * 0.77959971
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26480 * 0.18966379
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63035 * 0.20280397
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63619 * 0.96514991
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5282 * 0.11088811
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43968 * 0.63204190
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8174 * 0.09363004
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90489 * 0.24724627
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96897 * 0.21127049
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87601 * 0.00004387
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86800 * 0.74644248
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12422 * 0.64696518
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34380 * 0.08744613
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'nzgwrjym').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0036():
    """Extended test 36 for scheduler."""
    x_0 = 81275 * 0.56457819
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31021 * 0.90934268
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93521 * 0.33077200
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93796 * 0.68756594
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94175 * 0.68114189
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26821 * 0.34913929
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51272 * 0.17746164
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20805 * 0.61296983
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58819 * 0.68833101
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70225 * 0.06167189
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31361 * 0.20449963
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10196 * 0.10536176
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75499 * 0.94609592
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81979 * 0.56234003
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81373 * 0.49430686
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67079 * 0.91664928
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66017 * 0.30082504
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40561 * 0.97307678
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32458 * 0.35150682
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74956 * 0.50977788
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26019 * 0.14191312
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12630 * 0.46320928
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16663 * 0.19400722
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29628 * 0.91436754
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4069 * 0.35571953
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32803 * 0.52035914
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99343 * 0.40711050
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22174 * 0.96297624
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22211 * 0.85152645
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32103 * 0.83629573
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72177 * 0.83949259
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61415 * 0.76609977
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95729 * 0.28757714
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66089 * 0.37817211
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92057 * 0.05437240
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5422 * 0.33086186
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6347 * 0.47650984
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5150 * 0.49034962
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70900 * 0.36548318
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90836 * 0.88023302
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68260 * 0.01531664
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12420 * 0.01450039
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18051 * 0.47813065
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88973 * 0.50410571
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 6668 * 0.53270913
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 99545 * 0.28522324
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 68200 * 0.16997810
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 99611 * 0.48678484
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 67915 * 0.04369411
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'awxloikg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0037():
    """Extended test 37 for scheduler."""
    x_0 = 36131 * 0.77999271
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74205 * 0.39631307
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95507 * 0.88230298
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4146 * 0.31599435
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9171 * 0.14591170
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99047 * 0.05351467
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15549 * 0.24877356
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97157 * 0.32416810
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6731 * 0.50867112
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58329 * 0.97048761
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78984 * 0.66588325
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84699 * 0.97831436
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30919 * 0.93079087
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4209 * 0.19109939
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2802 * 0.96460943
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85078 * 0.68600480
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39092 * 0.31867142
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10259 * 0.15693108
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56047 * 0.14691756
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40019 * 0.05414218
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'acpmiema').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0038():
    """Extended test 38 for scheduler."""
    x_0 = 1946 * 0.75638456
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98094 * 0.23441085
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13344 * 0.25245474
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24425 * 0.49783166
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37034 * 0.69187270
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25253 * 0.77482285
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83699 * 0.09583383
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28457 * 0.25967152
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59208 * 0.42163649
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70024 * 0.41266549
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14263 * 0.94563083
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65211 * 0.90773172
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2575 * 0.15966562
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92886 * 0.53533654
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56993 * 0.93262884
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8820 * 0.88662461
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48587 * 0.71615278
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58406 * 0.17345550
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83503 * 0.53823297
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93979 * 0.03990753
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5862 * 0.25509519
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41749 * 0.78716450
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82883 * 0.57102880
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34982 * 0.92670414
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4924 * 0.53086879
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7062 * 0.77039524
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78310 * 0.43887137
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34723 * 0.33130046
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98314 * 0.48103360
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74828 * 0.58005905
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44644 * 0.64181447
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92307 * 0.37828776
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7760 * 0.44575815
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'xutuvdkt').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0039():
    """Extended test 39 for scheduler."""
    x_0 = 41921 * 0.49489091
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63221 * 0.27052980
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40255 * 0.70727482
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68384 * 0.43984703
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62633 * 0.93732611
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51183 * 0.64123272
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51187 * 0.27126331
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61803 * 0.58473648
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45634 * 0.51754304
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21524 * 0.92616680
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24464 * 0.45523862
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29075 * 0.06145912
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84117 * 0.81170488
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66974 * 0.15801005
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67525 * 0.53039871
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26420 * 0.86994581
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52428 * 0.30534860
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50670 * 0.36609646
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67794 * 0.66413822
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45258 * 0.05783590
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23126 * 0.82358634
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36892 * 0.86929335
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84282 * 0.53838430
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60931 * 0.42428930
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45197 * 0.62477924
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84119 * 0.55442072
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48169 * 0.24868920
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16895 * 0.18716922
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26576 * 0.22042399
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85609 * 0.87661803
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85369 * 0.86103020
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18669 * 0.40718360
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26156 * 0.93648470
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34721 * 0.21117637
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81503 * 0.85363484
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80214 * 0.11547917
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4112 * 0.34308292
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68976 * 0.61515640
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81065 * 0.41451965
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'iqbjteuy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0040():
    """Extended test 40 for scheduler."""
    x_0 = 2090 * 0.03058392
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67133 * 0.10287193
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24623 * 0.69544178
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71189 * 0.08571570
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12207 * 0.26631201
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59867 * 0.04135461
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71419 * 0.09655132
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6321 * 0.99771329
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59945 * 0.43755043
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79582 * 0.88754774
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28618 * 0.60702700
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55461 * 0.77011030
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66472 * 0.01419163
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43032 * 0.02486557
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70113 * 0.59754998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71369 * 0.22037345
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30784 * 0.54530291
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17797 * 0.46395113
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8089 * 0.56371297
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84591 * 0.73485974
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90854 * 0.27381715
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98304 * 0.80581397
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20662 * 0.43534103
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97270 * 0.95510309
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79960 * 0.82560645
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89389 * 0.31299689
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22552 * 0.17707957
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71190 * 0.10021905
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74256 * 0.49759346
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25057 * 0.78223380
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56514 * 0.26245590
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63688 * 0.18459836
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'vjyhymej').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0041():
    """Extended test 41 for scheduler."""
    x_0 = 74595 * 0.82858375
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46531 * 0.09509902
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46587 * 0.57045208
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10117 * 0.68355882
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34834 * 0.83265852
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14341 * 0.68445895
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94291 * 0.43964476
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99045 * 0.87624848
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66821 * 0.18712814
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40837 * 0.73823573
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14041 * 0.03036071
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4082 * 0.07526867
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71464 * 0.50159978
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92085 * 0.21336076
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55392 * 0.83676781
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87691 * 0.26079470
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30387 * 0.44689617
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16682 * 0.56995870
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89508 * 0.65395153
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2637 * 0.97375927
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98435 * 0.84040604
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31009 * 0.49609473
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65964 * 0.03041668
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28618 * 0.41973865
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35893 * 0.53565838
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'slblkiak').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0042():
    """Extended test 42 for scheduler."""
    x_0 = 59374 * 0.14769367
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80624 * 0.93361856
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17378 * 0.24327764
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66638 * 0.72631184
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6297 * 0.13842862
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19156 * 0.48396108
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10155 * 0.53035382
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8378 * 0.74668182
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83693 * 0.40906670
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9594 * 0.59511700
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87452 * 0.77103838
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81562 * 0.37321923
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8410 * 0.32963249
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72758 * 0.38111282
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49007 * 0.91019406
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41271 * 0.04333215
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66905 * 0.47590691
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3460 * 0.05060569
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51308 * 0.25072800
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50856 * 0.62929082
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88626 * 0.75443525
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49500 * 0.56736530
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47836 * 0.91600708
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10206 * 0.19615716
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28819 * 0.51876386
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95865 * 0.82752774
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73441 * 0.59088582
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 337 * 0.25712913
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16595 * 0.95994795
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'fzhvlwut').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0043():
    """Extended test 43 for scheduler."""
    x_0 = 14553 * 0.72385358
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9703 * 0.75113492
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58824 * 0.85706047
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11104 * 0.05033869
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54247 * 0.87593647
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44546 * 0.99266309
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98317 * 0.64721039
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81110 * 0.91765941
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17763 * 0.13447297
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57866 * 0.04671115
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59985 * 0.15935707
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45138 * 0.32405556
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98153 * 0.96337580
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90814 * 0.28378557
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20840 * 0.52768317
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89994 * 0.19558671
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82154 * 0.46153843
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51957 * 0.30482073
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17411 * 0.05708920
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48952 * 0.58316146
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64718 * 0.95898448
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51605 * 0.55936759
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77604 * 0.39847956
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73460 * 0.93747868
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79935 * 0.65642430
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25217 * 0.74813090
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71321 * 0.27490306
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43881 * 0.09795012
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3677 * 0.94140205
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55864 * 0.49917264
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58628 * 0.78592130
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 778 * 0.69128396
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24409 * 0.88865515
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2221 * 0.75777899
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15242 * 0.35610259
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 92403 * 0.23914125
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94207 * 0.35429950
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87531 * 0.37781140
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'slysscnk').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0044():
    """Extended test 44 for scheduler."""
    x_0 = 83608 * 0.88851276
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49465 * 0.13769395
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92720 * 0.88681006
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18293 * 0.08132503
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57732 * 0.00880771
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68801 * 0.60002598
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13892 * 0.20658677
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73971 * 0.28493763
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9908 * 0.79360068
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33385 * 0.71207373
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97290 * 0.43578189
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27491 * 0.60641117
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39406 * 0.15632721
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97542 * 0.64824996
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85228 * 0.58368018
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27159 * 0.14281671
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35289 * 0.26184849
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92648 * 0.45797781
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39803 * 0.17739253
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87293 * 0.42499471
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54868 * 0.97443803
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69378 * 0.21708915
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92440 * 0.23683753
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82816 * 0.04502585
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25626 * 0.37393299
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33306 * 0.51759738
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34352 * 0.50824187
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'huynmhmg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0045():
    """Extended test 45 for scheduler."""
    x_0 = 4847 * 0.86116868
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76910 * 0.00424736
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33510 * 0.23157473
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8803 * 0.84872021
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77907 * 0.15474559
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71017 * 0.28883014
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23557 * 0.41478851
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96894 * 0.84124004
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41599 * 0.40375923
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22508 * 0.66628803
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11275 * 0.25529793
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40679 * 0.28574316
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2539 * 0.56055563
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58076 * 0.46382767
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55902 * 0.40174237
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71605 * 0.97739289
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90712 * 0.56534314
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44481 * 0.32248095
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32340 * 0.09294800
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66604 * 0.95533442
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77474 * 0.64776698
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63026 * 0.89761121
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'ahxgviii').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0046():
    """Extended test 46 for scheduler."""
    x_0 = 15947 * 0.85535103
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54664 * 0.32244216
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13616 * 0.55498101
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84835 * 0.68975127
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40959 * 0.59864544
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21035 * 0.44174243
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70937 * 0.70084824
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74429 * 0.51971477
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29731 * 0.97443922
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55740 * 0.84710644
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65127 * 0.69307103
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73727 * 0.26131970
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75928 * 0.91463950
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84853 * 0.42468547
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37190 * 0.51237798
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46337 * 0.54251757
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56177 * 0.57876266
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96005 * 0.97286627
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80345 * 0.39334660
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22395 * 0.90393169
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96083 * 0.49123166
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81581 * 0.79215971
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5535 * 0.73715044
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87721 * 0.58251190
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42690 * 0.83596983
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47413 * 0.09312489
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39654 * 0.82451436
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62798 * 0.56539536
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28445 * 0.48021041
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55975 * 0.34173371
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1438 * 0.09214901
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84986 * 0.58535310
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19717 * 0.42644199
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22009 * 0.53125362
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44297 * 0.73956677
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98021 * 0.98298353
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48539 * 0.41667817
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79593 * 0.11594817
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96618 * 0.52430175
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76009 * 0.45812440
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'gskbgshs').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0047():
    """Extended test 47 for scheduler."""
    x_0 = 60427 * 0.82706851
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21401 * 0.45718845
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32857 * 0.27610210
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11417 * 0.44711485
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92134 * 0.79958812
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52867 * 0.33551523
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78159 * 0.45897318
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44529 * 0.09840372
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99318 * 0.32882271
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35943 * 0.16705818
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13178 * 0.41544559
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35033 * 0.03689160
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7184 * 0.79926203
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97911 * 0.72191465
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11739 * 0.73072202
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51353 * 0.89628793
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45991 * 0.33537244
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14992 * 0.43461767
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55024 * 0.43187636
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3059 * 0.93322036
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90541 * 0.16441756
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78492 * 0.30298831
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10186 * 0.82496104
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28637 * 0.68780081
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32864 * 0.45369164
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81289 * 0.43153177
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77216 * 0.15338936
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28918 * 0.13588899
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82180 * 0.74933956
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70001 * 0.46879989
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35445 * 0.15264525
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55200 * 0.41973039
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58000 * 0.71602646
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87133 * 0.09888394
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39715 * 0.47143021
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60489 * 0.87532498
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85455 * 0.29596413
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52243 * 0.57228637
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4053 * 0.79254148
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'byoetxam').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0048():
    """Extended test 48 for scheduler."""
    x_0 = 7699 * 0.13435178
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99668 * 0.00597515
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73757 * 0.49216971
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54727 * 0.51362366
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56240 * 0.24499212
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30262 * 0.34865637
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1318 * 0.18637822
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48270 * 0.98271042
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25185 * 0.46990104
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4967 * 0.19475473
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57316 * 0.88755047
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14960 * 0.52018174
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35512 * 0.08637637
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40216 * 0.57370642
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24346 * 0.20649161
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81373 * 0.09932814
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88892 * 0.10820772
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19188 * 0.09783074
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44203 * 0.15783595
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86515 * 0.87978383
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55113 * 0.71479902
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78563 * 0.67197997
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55938 * 0.69571125
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75830 * 0.00143684
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54108 * 0.92009719
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7798 * 0.36352332
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61924 * 0.85644721
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4028 * 0.06505706
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20171 * 0.38176611
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72532 * 0.54520178
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3564 * 0.00979624
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95354 * 0.83790411
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41482 * 0.73368367
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86352 * 0.27027031
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85610 * 0.66252110
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70318 * 0.62230082
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'dxgmnepr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0049():
    """Extended test 49 for scheduler."""
    x_0 = 86019 * 0.78202693
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76206 * 0.78794871
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2474 * 0.84326681
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7585 * 0.62354907
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71218 * 0.89132332
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42025 * 0.09801880
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55001 * 0.04959990
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17271 * 0.27860320
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67446 * 0.89067281
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85230 * 0.55742932
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36785 * 0.58134227
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84648 * 0.05373285
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39394 * 0.22289929
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86448 * 0.92970355
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38438 * 0.19681364
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81841 * 0.44515045
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84103 * 0.55606669
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8191 * 0.85298909
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24753 * 0.95996825
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63699 * 0.71229445
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5117 * 0.15358982
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19553 * 0.38143444
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87414 * 0.33164702
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85153 * 0.70351109
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41172 * 0.13841958
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79534 * 0.91738921
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3300 * 0.03615660
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97231 * 0.36143145
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13077 * 0.94994158
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46132 * 0.61866448
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16127 * 0.67988543
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95508 * 0.75440009
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26089 * 0.87410166
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47755 * 0.98055303
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61686 * 0.58635746
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5151 * 0.91241490
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65459 * 0.68667871
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9529 * 0.28218771
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77216 * 0.23647595
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11845 * 0.89508091
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8319 * 0.23914922
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81202 * 0.90198233
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 78266 * 0.67184748
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 91885 * 0.30244266
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71446 * 0.66031097
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 91431 * 0.49612617
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 76565 * 0.96593673
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 10357 * 0.58120938
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'zcbobdmq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0050():
    """Extended test 50 for scheduler."""
    x_0 = 28332 * 0.88864965
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80917 * 0.12429298
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24864 * 0.17741782
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30864 * 0.06943608
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30284 * 0.47501990
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76932 * 0.65001366
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87197 * 0.83504012
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20935 * 0.27775833
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10558 * 0.33417904
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34148 * 0.58864183
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31676 * 0.75390559
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29739 * 0.81399377
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23638 * 0.88125886
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9879 * 0.06659344
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29126 * 0.50885163
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57064 * 0.04990229
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62812 * 0.76133247
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23807 * 0.12789939
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19874 * 0.69497016
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38424 * 0.52323617
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25196 * 0.58201308
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19063 * 0.03024162
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46906 * 0.81378466
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85257 * 0.88096825
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12670 * 0.80949340
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53076 * 0.75069633
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48142 * 0.89838984
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42472 * 0.20034602
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'oveddubl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0051():
    """Extended test 51 for scheduler."""
    x_0 = 29925 * 0.20943261
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78918 * 0.97377463
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25002 * 0.71883610
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25726 * 0.88838764
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82530 * 0.41211203
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52976 * 0.53580186
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57208 * 0.10357767
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45352 * 0.26959386
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6466 * 0.53399447
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74874 * 0.95834471
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94691 * 0.40891745
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76686 * 0.97701338
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8474 * 0.20635335
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95926 * 0.51611957
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59677 * 0.54957666
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25207 * 0.33999264
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56771 * 0.78448768
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71489 * 0.27307164
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46780 * 0.35845301
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31708 * 0.98400896
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41671 * 0.09683517
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81787 * 0.48635847
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3858 * 0.62386698
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58895 * 0.77321181
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'pelwzzhr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0052():
    """Extended test 52 for scheduler."""
    x_0 = 23928 * 0.16257391
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36798 * 0.46980551
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35601 * 0.74634898
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58160 * 0.55605119
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19363 * 0.29807208
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35493 * 0.20844776
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91895 * 0.18619808
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80335 * 0.61395985
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56336 * 0.36301211
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10697 * 0.23316925
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18260 * 0.45985371
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91933 * 0.09835246
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42524 * 0.64096702
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61758 * 0.68139583
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85617 * 0.08443568
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39150 * 0.67054380
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72631 * 0.39498672
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50362 * 0.32835599
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77981 * 0.90290425
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46579 * 0.13261667
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3306 * 0.16207151
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21216 * 0.68002544
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74912 * 0.14355511
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43218 * 0.39837021
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93067 * 0.73029491
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19783 * 0.30274495
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31720 * 0.49223692
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70339 * 0.41146248
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28975 * 0.81701289
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48191 * 0.01014073
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4121 * 0.70101596
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10810 * 0.34386093
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76874 * 0.13284848
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76076 * 0.10793294
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22466 * 0.08957686
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51511 * 0.85295960
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85058 * 0.26620707
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87577 * 0.71235212
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47362 * 0.93003568
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 53597 * 0.57862524
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ricvneis').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0053():
    """Extended test 53 for scheduler."""
    x_0 = 48762 * 0.89967265
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12833 * 0.28305533
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29560 * 0.01552407
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35114 * 0.69352179
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37377 * 0.08628109
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97572 * 0.29408782
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54072 * 0.94736113
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99534 * 0.35830107
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39389 * 0.08624637
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4494 * 0.03608920
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98578 * 0.83117745
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37105 * 0.67895625
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2345 * 0.44919297
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75459 * 0.06873040
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31366 * 0.51953272
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59811 * 0.24476602
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12976 * 0.09981051
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80319 * 0.09744649
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4959 * 0.82867581
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78761 * 0.10910404
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99232 * 0.09867913
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53525 * 0.34710943
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98361 * 0.52106897
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87808 * 0.49063093
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82184 * 0.83597548
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'zmbhplwg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0054():
    """Extended test 54 for scheduler."""
    x_0 = 76547 * 0.59442798
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5481 * 0.37962553
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44923 * 0.88790418
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70681 * 0.94627153
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50932 * 0.59318442
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13994 * 0.75490445
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63325 * 0.71069717
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66068 * 0.74258236
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47115 * 0.19967161
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96984 * 0.12253747
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22357 * 0.75404059
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18139 * 0.31643895
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37499 * 0.80909753
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91470 * 0.50361982
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63612 * 0.82605429
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63339 * 0.70758533
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61149 * 0.69721824
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72269 * 0.86441078
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41488 * 0.00864057
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55876 * 0.02986731
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72398 * 0.60714621
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71438 * 0.05687775
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36329 * 0.55365190
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65659 * 0.70055742
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66969 * 0.98236205
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3137 * 0.45527396
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31426 * 0.51710003
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75918 * 0.11317290
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47350 * 0.63087370
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29465 * 0.15629016
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'cksqphfi').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0055():
    """Extended test 55 for scheduler."""
    x_0 = 17502 * 0.41874169
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51085 * 0.69270909
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62814 * 0.91142492
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65142 * 0.65641920
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70995 * 0.88174322
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 769 * 0.53236237
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25044 * 0.02445190
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48707 * 0.84157731
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8865 * 0.85953018
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69414 * 0.67429867
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14313 * 0.76413738
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44974 * 0.08498085
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17958 * 0.70089635
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75199 * 0.31662442
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63404 * 0.52938867
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91764 * 0.34925168
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37206 * 0.38367539
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29607 * 0.76578991
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41210 * 0.07350472
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40700 * 0.14114040
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18314 * 0.15159172
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39645 * 0.38276090
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3855 * 0.07146783
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80959 * 0.01583291
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28505 * 0.66143336
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59992 * 0.95824862
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25930 * 0.87003966
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54990 * 0.68247868
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'cfiryqul').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0056():
    """Extended test 56 for scheduler."""
    x_0 = 189 * 0.89523474
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73370 * 0.78620522
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17947 * 0.08717363
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94294 * 0.79558649
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84316 * 0.39961514
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4002 * 0.01883988
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55808 * 0.58899834
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40774 * 0.22845732
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23140 * 0.20360733
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15020 * 0.08086064
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32442 * 0.95420061
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55837 * 0.49065863
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11318 * 0.51746244
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51113 * 0.08712664
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46323 * 0.24375800
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14465 * 0.55399460
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48556 * 0.76498497
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66967 * 0.04630096
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96712 * 0.21320718
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11352 * 0.18802523
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33288 * 0.12891276
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71777 * 0.43411446
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77480 * 0.48381049
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58847 * 0.94317501
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51154 * 0.33003821
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66049 * 0.71130117
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10137 * 0.81506722
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17828 * 0.38356231
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92793 * 0.32363240
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37778 * 0.99839781
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'yobqypkq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0057():
    """Extended test 57 for scheduler."""
    x_0 = 46759 * 0.21264747
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66488 * 0.26860218
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80304 * 0.71989683
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81725 * 0.08632232
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55293 * 0.97331003
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1131 * 0.21086997
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82860 * 0.85690621
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78935 * 0.08175316
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2874 * 0.13319999
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48389 * 0.68308057
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85262 * 0.35140066
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88484 * 0.53904708
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12006 * 0.89388954
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41464 * 0.42015488
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83711 * 0.96032501
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70225 * 0.39431686
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99594 * 0.85278194
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2237 * 0.56665841
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33528 * 0.66895266
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19153 * 0.48699144
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50572 * 0.66529212
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'hxdeweny').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0058():
    """Extended test 58 for scheduler."""
    x_0 = 91052 * 0.09490686
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4197 * 0.69096813
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51072 * 0.08754276
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73095 * 0.41709257
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98080 * 0.54895849
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80439 * 0.91246567
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99924 * 0.42751701
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11333 * 0.27096574
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55934 * 0.44112115
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81807 * 0.91666934
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88060 * 0.43734209
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75941 * 0.75645127
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3543 * 0.13383365
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25398 * 0.86931445
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97214 * 0.17625780
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19457 * 0.94991412
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34395 * 0.80083017
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8708 * 0.96022774
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28820 * 0.49784016
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46241 * 0.79527156
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93360 * 0.19411310
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25339 * 0.94937248
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31289 * 0.41016570
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36972 * 0.95230610
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34206 * 0.27867367
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79850 * 0.20380119
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8336 * 0.68187564
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30838 * 0.81827225
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43570 * 0.92188132
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1668 * 0.76396995
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11625 * 0.86428141
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66466 * 0.86465054
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87485 * 0.11003013
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55697 * 0.44501084
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13565 * 0.64958330
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44997 * 0.02561054
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95006 * 0.72661045
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19614 * 0.00612959
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'bgojadci').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0059():
    """Extended test 59 for scheduler."""
    x_0 = 4639 * 0.13491803
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64810 * 0.83527330
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93387 * 0.50498866
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62193 * 0.53946583
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4472 * 0.15650346
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55352 * 0.64455637
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3835 * 0.96076556
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13794 * 0.44650638
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99716 * 0.76285630
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85790 * 0.23437084
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93893 * 0.52096302
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8257 * 0.51248641
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66407 * 0.15645733
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74614 * 0.27400012
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81448 * 0.10749039
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98949 * 0.33335717
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 211 * 0.63215759
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89244 * 0.00356556
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69775 * 0.48752400
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14557 * 0.23396901
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77191 * 0.49572432
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57517 * 0.30968524
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87477 * 0.11060139
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56547 * 0.85541361
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55662 * 0.38504019
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60268 * 0.95087303
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29303 * 0.85354906
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3094 * 0.27583864
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94313 * 0.45911630
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9456 * 0.27418694
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97542 * 0.82369247
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88139 * 0.95661310
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29893 * 0.94376805
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81175 * 0.21426222
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13571 * 0.58763941
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30856 * 0.22728579
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81932 * 0.16848359
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55403 * 0.12367821
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80287 * 0.43823171
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6421 * 0.99098287
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 67148 * 0.28452960
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20903 * 0.63528895
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ihojcqty').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0060():
    """Extended test 60 for scheduler."""
    x_0 = 51326 * 0.48774712
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21366 * 0.46072359
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67480 * 0.07928049
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76348 * 0.88451532
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53809 * 0.93493566
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70611 * 0.42809226
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60234 * 0.12215728
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90013 * 0.19479884
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55364 * 0.89422254
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29983 * 0.59900570
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 674 * 0.46665078
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48461 * 0.06486527
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25039 * 0.71020734
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33475 * 0.64414073
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97140 * 0.18802730
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15802 * 0.51260891
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73803 * 0.60853451
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92266 * 0.10250464
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43246 * 0.87546345
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50978 * 0.96129188
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68186 * 0.88648162
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48017 * 0.98688148
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92682 * 0.14046575
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1597 * 0.25649024
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63111 * 0.72592661
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93212 * 0.92649875
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11170 * 0.94598818
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44872 * 0.61340733
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86263 * 0.61406513
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25135 * 0.36475651
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45680 * 0.99808826
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20344 * 0.09671124
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81434 * 0.92191558
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7279 * 0.12126193
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92235 * 0.39600577
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'nccgxslb').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0061():
    """Extended test 61 for scheduler."""
    x_0 = 69264 * 0.66905002
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19836 * 0.68601296
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34264 * 0.43770580
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16804 * 0.97819266
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1409 * 0.94254135
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96962 * 0.20796333
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84502 * 0.23750389
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70345 * 0.73951397
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67286 * 0.21824464
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66410 * 0.06964665
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83379 * 0.76252996
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99675 * 0.63062918
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92460 * 0.38289609
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49807 * 0.30119529
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35698 * 0.55824206
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62775 * 0.55174259
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71863 * 0.64858454
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12948 * 0.07592412
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78195 * 0.34062451
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26772 * 0.24142987
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16896 * 0.65821766
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17144 * 0.96497012
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66178 * 0.13514592
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68269 * 0.98364751
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67074 * 0.32056776
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29832 * 0.35653248
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35345 * 0.82439845
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65584 * 0.77595621
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6893 * 0.27886764
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28741 * 0.39921236
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79440 * 0.33500955
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44103 * 0.36278714
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67526 * 0.28289433
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96296 * 0.31871577
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96548 * 0.46069016
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'twobdydj').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0062():
    """Extended test 62 for scheduler."""
    x_0 = 60272 * 0.42606564
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9229 * 0.97496912
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39159 * 0.45885908
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62680 * 0.17114351
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30075 * 0.97012200
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94987 * 0.50820452
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38671 * 0.82261434
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 882 * 0.16371734
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87603 * 0.21049872
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17530 * 0.34858420
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16123 * 0.64291580
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98804 * 0.66419981
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49093 * 0.80415498
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89095 * 0.82570825
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26972 * 0.84375593
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69572 * 0.97308565
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68584 * 0.82538065
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18004 * 0.07071714
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8971 * 0.60905724
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79608 * 0.03592335
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26831 * 0.36361514
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44120 * 0.52220526
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76766 * 0.03096637
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4699 * 0.15288049
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54793 * 0.73243518
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81374 * 0.52138644
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47385 * 0.58912777
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17991 * 0.91178714
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31487 * 0.04906388
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29022 * 0.45341737
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15772 * 0.09567508
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33495 * 0.72223069
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52849 * 0.17639416
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97645 * 0.99829187
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61660 * 0.18478692
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99304 * 0.99911777
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80315 * 0.47787359
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32577 * 0.49696344
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65906 * 0.42736067
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32337 * 0.06983199
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 15739 * 0.02117833
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81955 * 0.90785872
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42987 * 0.05005762
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 29996 * 0.65702185
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 15581 * 0.89753169
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 28019 * 0.39583901
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 4783 * 0.59004568
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ozuykghl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0063():
    """Extended test 63 for scheduler."""
    x_0 = 40064 * 0.82142625
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80677 * 0.21185202
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49563 * 0.69281846
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98971 * 0.02095035
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80680 * 0.25911094
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10376 * 0.43068922
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57501 * 0.92398330
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16202 * 0.98908624
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27100 * 0.44404093
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5908 * 0.04504972
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69486 * 0.50678970
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95503 * 0.08239403
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60976 * 0.96737729
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44495 * 0.27431285
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60983 * 0.21094702
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68700 * 0.78145462
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25365 * 0.94522632
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91078 * 0.14846447
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10012 * 0.31097448
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36418 * 0.00013608
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5107 * 0.79463150
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14226 * 0.37090304
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79844 * 0.87793332
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47993 * 0.74282656
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'onctsnov').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0064():
    """Extended test 64 for scheduler."""
    x_0 = 13821 * 0.99644484
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30414 * 0.34665238
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9637 * 0.32361211
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57153 * 0.04039027
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24969 * 0.65268991
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33241 * 0.88906314
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21017 * 0.04383907
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41666 * 0.92994806
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68742 * 0.57523932
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7290 * 0.58652749
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39937 * 0.12055745
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96343 * 0.52824161
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26809 * 0.96704525
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37908 * 0.51710438
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76369 * 0.69142079
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48566 * 0.39497331
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51496 * 0.10970913
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51665 * 0.18047219
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4823 * 0.42862249
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68966 * 0.26651717
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61462 * 0.55530299
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49369 * 0.18661846
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70789 * 0.69992743
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62643 * 0.43792201
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22008 * 0.11531665
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71177 * 0.04355742
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74233 * 0.83147242
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29454 * 0.67161482
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37877 * 0.20979104
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98942 * 0.10761013
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80803 * 0.31307430
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22537 * 0.52131697
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72571 * 0.83205605
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35230 * 0.02722844
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29355 * 0.04839419
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68645 * 0.93522079
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87410 * 0.46344156
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49299 * 0.00464989
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53711 * 0.08880749
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22049 * 0.64849763
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5930 * 0.93300666
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 78762 * 0.60770489
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 19236 * 0.08495617
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 24797 * 0.19011630
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'ihhnvznj').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0065():
    """Extended test 65 for scheduler."""
    x_0 = 17962 * 0.69526206
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98835 * 0.23760772
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53206 * 0.66303311
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75037 * 0.84807830
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44306 * 0.98085332
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6561 * 0.13414827
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13592 * 0.15025218
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97022 * 0.50964551
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13412 * 0.29013206
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55603 * 0.88510758
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5520 * 0.55410339
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75281 * 0.34460306
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98470 * 0.32727627
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54698 * 0.82681385
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 770 * 0.64703237
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95619 * 0.01461537
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20767 * 0.89741792
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40942 * 0.64471520
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71648 * 0.72006059
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26592 * 0.35568037
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58577 * 0.95882964
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47710 * 0.31937733
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'kofottpv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0066():
    """Extended test 66 for scheduler."""
    x_0 = 23012 * 0.72631683
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8324 * 0.13834457
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77328 * 0.97367822
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91700 * 0.13077957
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10999 * 0.85493999
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36994 * 0.51007844
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83512 * 0.09597698
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76704 * 0.15415139
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96028 * 0.44643639
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54544 * 0.49174903
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28558 * 0.40524589
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93288 * 0.67712557
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19780 * 0.43813300
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10035 * 0.03551766
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25470 * 0.95124941
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67623 * 0.28390674
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27664 * 0.68679548
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36974 * 0.80410906
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82589 * 0.96467459
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61883 * 0.28240680
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19452 * 0.90404932
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88139 * 0.61295899
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89408 * 0.16559603
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68508 * 0.09523413
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8163 * 0.98016666
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 758 * 0.82921082
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24739 * 0.36337261
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52159 * 0.34945680
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48908 * 0.52440981
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20613 * 0.21821039
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91154 * 0.01667977
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31761 * 0.46271200
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37773 * 0.12331277
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79237 * 0.97154988
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31863 * 0.19046849
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87391 * 0.06413242
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27237 * 0.30962064
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90812 * 0.85584879
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91975 * 0.28138105
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38571 * 0.14405992
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13989 * 0.36659981
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 29290 * 0.55894727
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 80572 * 0.46804489
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 64263 * 0.62307213
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 15684 * 0.00947956
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 95095 * 0.46080209
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 86720 * 0.50739892
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 73117 * 0.75190931
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'lympaemn').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0067():
    """Extended test 67 for scheduler."""
    x_0 = 67832 * 0.93291487
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24832 * 0.09231117
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24445 * 0.65003478
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84733 * 0.04901920
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46322 * 0.77566721
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24373 * 0.13096147
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70276 * 0.29672535
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11737 * 0.62009811
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52291 * 0.65284855
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31319 * 0.89610862
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71333 * 0.30952067
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45673 * 0.70096877
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73812 * 0.48185642
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75794 * 0.49574023
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91518 * 0.00488480
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76665 * 0.40822418
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62895 * 0.23769245
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36840 * 0.31467517
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66969 * 0.68904501
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8993 * 0.49770818
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89642 * 0.51944002
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54944 * 0.43962531
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18499 * 0.74823042
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95856 * 0.84219029
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94363 * 0.49521277
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19999 * 0.01385670
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41701 * 0.86179211
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49461 * 0.70608255
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64909 * 0.81722299
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71489 * 0.05179395
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13976 * 0.43048810
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6232 * 0.90158296
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90777 * 0.99468313
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50055 * 0.27726565
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66010 * 0.65617460
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32567 * 0.57657842
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66134 * 0.94919056
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9611 * 0.74009316
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61999 * 0.03338894
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 49786 * 0.37826978
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48038 * 0.06598068
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'kmsnkjio').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0068():
    """Extended test 68 for scheduler."""
    x_0 = 8468 * 0.29176295
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73737 * 0.29943956
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47301 * 0.24593628
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54187 * 0.66486502
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27170 * 0.05587638
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2779 * 0.10980604
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47256 * 0.12972751
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32956 * 0.71801311
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77518 * 0.61042890
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97919 * 0.83642640
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98712 * 0.43954360
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79371 * 0.35489497
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37801 * 0.44651529
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15798 * 0.93055238
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11215 * 0.18472116
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90751 * 0.51117997
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25511 * 0.58718675
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90443 * 0.73388975
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58386 * 0.79517302
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4560 * 0.99311491
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14001 * 0.93726966
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78440 * 0.41342107
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'ottwvavw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_3_0069():
    """Extended test 69 for scheduler."""
    x_0 = 17930 * 0.30940667
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65300 * 0.35592757
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73589 * 0.47443086
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97781 * 0.85734770
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84413 * 0.44270629
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57040 * 0.05241143
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41995 * 0.62799895
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13593 * 0.13041234
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3986 * 0.08612666
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23014 * 0.93183807
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61417 * 0.64632589
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12324 * 0.13512442
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86099 * 0.62497608
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43005 * 0.64219038
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48870 * 0.57828792
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67846 * 0.82820776
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92763 * 0.98404708
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10281 * 0.68931812
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97385 * 0.08468689
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96244 * 0.41266271
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32390 * 0.09669584
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32374 * 0.34392007
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89722 * 0.71861067
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17754 * 0.69590293
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35839 * 0.29649710
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33749 * 0.65794280
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31405 * 0.80990026
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65448 * 0.10635834
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'llodbqpq').hexdigest()
    assert len(h) == 64
