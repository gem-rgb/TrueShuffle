"""Extended tests for api suite 4."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_api_extended_4_0000():
    """Extended test 0 for api."""
    x_0 = 23496 * 0.75064870
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10400 * 0.30812996
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21968 * 0.93008053
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92338 * 0.38221127
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42502 * 0.70724209
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4083 * 0.28489938
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26565 * 0.52235958
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27052 * 0.57651968
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38325 * 0.55494299
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48704 * 0.41578921
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15763 * 0.44703939
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53462 * 0.66846938
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11204 * 0.80985756
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52237 * 0.37772284
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47738 * 0.58445556
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77847 * 0.23275529
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63677 * 0.64703226
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36111 * 0.45706186
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34749 * 0.69525846
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40692 * 0.09048422
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4045 * 0.82770678
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51752 * 0.58824982
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97155 * 0.14710031
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47485 * 0.11501197
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40385 * 0.09093041
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95727 * 0.87155982
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99175 * 0.01514993
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92363 * 0.50872875
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64781 * 0.54864376
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73340 * 0.83705244
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17453 * 0.02636166
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41204 * 0.84622035
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63929 * 0.20123216
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23111 * 0.64209428
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65715 * 0.46627468
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54701 * 0.54210583
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7581 * 0.66521481
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39743 * 0.55715806
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12946 * 0.23199492
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56452 * 0.84454249
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68955 * 0.56238038
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47253 * 0.69040736
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46302 * 0.01391429
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84560 * 0.50927152
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'fixntgon').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0001():
    """Extended test 1 for api."""
    x_0 = 22732 * 0.96733996
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 192 * 0.54446093
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57749 * 0.63436225
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48471 * 0.12765019
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26623 * 0.88475858
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1092 * 0.61531084
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24541 * 0.91417016
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93424 * 0.39857989
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9227 * 0.69442659
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50142 * 0.80954944
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55023 * 0.61796591
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34970 * 0.55421583
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98253 * 0.66693513
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19900 * 0.45158260
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54733 * 0.51804051
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20596 * 0.40906860
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91555 * 0.44244678
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23881 * 0.24582601
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94058 * 0.00467472
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59108 * 0.86399496
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40065 * 0.73839679
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7262 * 0.80830213
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10839 * 0.20711576
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15491 * 0.44898035
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60486 * 0.61231706
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60199 * 0.76059010
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23965 * 0.87713986
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28174 * 0.36204695
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86920 * 0.09860582
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92850 * 0.01657274
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4234 * 0.31165907
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89063 * 0.30619034
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94224 * 0.51177858
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4159 * 0.86260171
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25099 * 0.39212255
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'hzzdxzyc').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0002():
    """Extended test 2 for api."""
    x_0 = 87533 * 0.27902560
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69313 * 0.51622801
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36934 * 0.26734597
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89651 * 0.82631545
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88089 * 0.63846951
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6268 * 0.73248722
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1391 * 0.82973936
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97954 * 0.65657757
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2892 * 0.19343697
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57939 * 0.61784695
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76188 * 0.63569242
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90471 * 0.28573260
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8176 * 0.60161244
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75796 * 0.87860052
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45339 * 0.02592502
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77557 * 0.61307475
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88078 * 0.50462169
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6847 * 0.09085146
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45336 * 0.51385004
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45506 * 0.30887511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69029 * 0.77053314
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52635 * 0.95801310
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64041 * 0.80685056
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20766 * 0.16467759
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49806 * 0.45050115
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92354 * 0.60757199
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79402 * 0.51641084
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59704 * 0.53820640
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84279 * 0.74183380
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74125 * 0.78991083
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55213 * 0.01121286
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9145 * 0.15106677
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21912 * 0.89703092
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97252 * 0.85962940
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22871 * 0.28043789
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15475 * 0.32624956
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59004 * 0.27372792
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21287 * 0.07117396
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44096 * 0.74869670
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85917 * 0.74288183
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'afxoqias').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0003():
    """Extended test 3 for api."""
    x_0 = 14586 * 0.64332993
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40986 * 0.51727172
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81421 * 0.07706689
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78734 * 0.69865530
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89711 * 0.41344698
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12183 * 0.40877353
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88343 * 0.15966725
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57393 * 0.69292147
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5152 * 0.56076563
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56896 * 0.18958172
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31218 * 0.73193927
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11876 * 0.02065335
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5255 * 0.32491052
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78146 * 0.78173318
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96069 * 0.15277743
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90902 * 0.57138793
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17637 * 0.87263301
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36274 * 0.91686037
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77793 * 0.76681585
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96300 * 0.98908771
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68191 * 0.60709600
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38363 * 0.54250622
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13771 * 0.55871773
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17194 * 0.37584962
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24078 * 0.85711628
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27645 * 0.64521777
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38061 * 0.22520510
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86520 * 0.88230442
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72960 * 0.37743769
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32105 * 0.90327385
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50886 * 0.97904591
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1585 * 0.79379852
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 974 * 0.69956230
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15620 * 0.74324485
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72939 * 0.96645198
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39033 * 0.67275102
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33710 * 0.05450084
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98723 * 0.58155770
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97788 * 0.41351704
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76622 * 0.32862318
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12461 * 0.64667976
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63911 * 0.87475280
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'gfmoqeeb').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0004():
    """Extended test 4 for api."""
    x_0 = 79394 * 0.71150408
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45997 * 0.93213827
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4700 * 0.49012649
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37024 * 0.43142931
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17194 * 0.03516291
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84400 * 0.33107718
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32640 * 0.39494590
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58611 * 0.54689677
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24768 * 0.42667435
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64340 * 0.16001552
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20128 * 0.68227149
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37756 * 0.87212361
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26632 * 0.96812866
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4324 * 0.47646347
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89493 * 0.26549000
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23364 * 0.32146155
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73896 * 0.94497028
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86373 * 0.06325534
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27105 * 0.00505495
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10133 * 0.93815477
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6871 * 0.63529915
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79304 * 0.62504868
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38717 * 0.55193863
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28774 * 0.89917388
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65952 * 0.85543472
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28389 * 0.25543546
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74904 * 0.65374159
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54913 * 0.38552755
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83716 * 0.54220966
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51953 * 0.10200951
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44801 * 0.08999719
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28431 * 0.24501241
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12049 * 0.88442568
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5526 * 0.32659162
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47796 * 0.26738199
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15362 * 0.80418802
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'hxoyfwdk').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0005():
    """Extended test 5 for api."""
    x_0 = 51064 * 0.00931241
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67559 * 0.54509721
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2181 * 0.41468116
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38542 * 0.11091464
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75566 * 0.81723901
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48593 * 0.28656663
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91236 * 0.12926380
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90653 * 0.07594958
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64162 * 0.73373666
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48222 * 0.64501841
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65902 * 0.20492491
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49205 * 0.11436725
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74849 * 0.43248921
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34474 * 0.18624457
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22023 * 0.92365582
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6593 * 0.76723003
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15632 * 0.80024094
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45333 * 0.84044300
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96715 * 0.78529396
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73164 * 0.98321952
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64548 * 0.49068387
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11031 * 0.30588235
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17161 * 0.12717645
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21774 * 0.65607446
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 179 * 0.85768618
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'kqqeiwnd').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0006():
    """Extended test 6 for api."""
    x_0 = 85593 * 0.02580468
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41547 * 0.11646075
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52270 * 0.58323700
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55384 * 0.81036081
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67354 * 0.39187185
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68447 * 0.06524195
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62143 * 0.89802486
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6480 * 0.90522831
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81851 * 0.70108259
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48935 * 0.48254684
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72441 * 0.88441749
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33163 * 0.99585235
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18913 * 0.20835827
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82484 * 0.25812374
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63575 * 0.57266712
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41244 * 0.10223715
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3678 * 0.62223186
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24349 * 0.82821245
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99932 * 0.88920995
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30200 * 0.88305974
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74508 * 0.48673034
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44809 * 0.94822437
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44515 * 0.85415886
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97409 * 0.45401958
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36574 * 0.72037303
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44789 * 0.65452692
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89562 * 0.06132858
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85052 * 0.27697481
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4914 * 0.65375224
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76219 * 0.62519707
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68825 * 0.98883896
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40547 * 0.63611777
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62463 * 0.16824758
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35823 * 0.66271109
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34359 * 0.93349200
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43435 * 0.62395536
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23247 * 0.70054516
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82988 * 0.54415163
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74427 * 0.75151974
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13873 * 0.66041318
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5713 * 0.65828672
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43920 * 0.81646678
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22594 * 0.42795986
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 5942 * 0.84695627
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86768 * 0.86637081
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 67258 * 0.57627799
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 28179 * 0.28145312
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 88042 * 0.99521335
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'hhfhgszg').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0007():
    """Extended test 7 for api."""
    x_0 = 57482 * 0.29411795
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28227 * 0.30230621
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79933 * 0.73951561
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91487 * 0.62825094
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78900 * 0.09446447
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25152 * 0.58782833
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67248 * 0.86881943
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87620 * 0.19578934
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64246 * 0.11439399
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12060 * 0.78576487
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37656 * 0.11504831
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22280 * 0.57650220
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39463 * 0.56535792
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92716 * 0.24933239
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10875 * 0.58374968
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7486 * 0.93263606
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95017 * 0.26358431
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46704 * 0.06910599
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63318 * 0.63819407
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97992 * 0.26730840
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32823 * 0.97983919
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 732 * 0.76377419
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53561 * 0.84400839
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36709 * 0.49071234
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40579 * 0.37365085
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76364 * 0.98255667
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47771 * 0.09216783
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16715 * 0.01460714
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15957 * 0.96455622
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86463 * 0.53565624
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85363 * 0.31224999
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20843 * 0.02184017
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31494 * 0.11747184
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80803 * 0.85632821
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71030 * 0.24009284
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28571 * 0.75696387
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33464 * 0.34337192
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10991 * 0.90093867
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45901 * 0.46104724
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80819 * 0.07968129
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 50611 * 0.46038754
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43043 * 0.24146600
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29172 * 0.73127842
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 63165 * 0.01133960
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 25949 * 0.76169121
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'wxaidqwl').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0008():
    """Extended test 8 for api."""
    x_0 = 30758 * 0.62660196
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5497 * 0.77665034
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89979 * 0.96844649
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45553 * 0.88076424
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84112 * 0.18183427
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75603 * 0.57618560
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38856 * 0.77067573
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1473 * 0.86397614
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86333 * 0.51511804
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33342 * 0.21494435
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81998 * 0.35130733
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25532 * 0.03955092
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73673 * 0.97877311
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9825 * 0.54275826
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43889 * 0.59612194
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48717 * 0.11135333
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41598 * 0.70830347
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42801 * 0.42121349
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35305 * 0.55778833
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57272 * 0.87894845
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91573 * 0.40082698
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17320 * 0.30930445
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36882 * 0.13138708
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90879 * 0.34122735
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83295 * 0.34930126
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42356 * 0.44212899
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72337 * 0.33326497
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45568 * 0.50184632
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24804 * 0.06022540
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6719 * 0.66793966
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66692 * 0.70971583
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52052 * 0.84980788
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66158 * 0.78556812
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20675 * 0.42383633
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53635 * 0.76419683
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84544 * 0.08920659
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51860 * 0.85235733
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94035 * 0.19548013
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73334 * 0.76102335
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4623 * 0.93620706
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47198 * 0.44877316
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69343 * 0.04916448
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 73022 * 0.90529182
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99197 * 0.92409122
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 31907 * 0.70916633
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 44475 * 0.58521735
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 39880 * 0.90402095
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 49963 * 0.62969366
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 82132 * 0.75980253
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'gztdbplf').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0009():
    """Extended test 9 for api."""
    x_0 = 18025 * 0.29287851
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59870 * 0.89808861
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59024 * 0.53622119
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28634 * 0.40041972
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20869 * 0.89315682
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 802 * 0.56210685
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93745 * 0.27755155
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94599 * 0.34790176
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95938 * 0.59873833
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17580 * 0.55196405
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82755 * 0.45959479
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6753 * 0.11697875
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54882 * 0.91349080
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81185 * 0.29301780
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11020 * 0.13127473
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29024 * 0.03282334
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55065 * 0.34453970
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53397 * 0.06074367
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37243 * 0.69983493
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99132 * 0.39124554
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46371 * 0.81206169
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71621 * 0.09405921
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3371 * 0.92328873
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55678 * 0.90787644
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88636 * 0.39236052
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63149 * 0.21747626
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1809 * 0.20047156
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69563 * 0.57698224
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85775 * 0.93068926
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2918 * 0.00308591
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9753 * 0.35991533
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81606 * 0.43546568
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48943 * 0.94926718
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24279 * 0.40260123
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36706 * 0.48307969
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18361 * 0.70643722
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14504 * 0.41366946
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11969 * 0.44380097
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2949 * 0.35493384
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'zxmqifyk').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0010():
    """Extended test 10 for api."""
    x_0 = 18138 * 0.57178057
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31700 * 0.37765862
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99974 * 0.47283543
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22985 * 0.77408755
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62458 * 0.09508819
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7866 * 0.52632840
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25066 * 0.20447302
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21137 * 0.75956176
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50342 * 0.52816774
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14502 * 0.26795357
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1859 * 0.46927843
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36974 * 0.80931050
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87735 * 0.99505693
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69532 * 0.08165480
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88240 * 0.57008509
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42283 * 0.73349793
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77032 * 0.22660389
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40526 * 0.67843072
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30106 * 0.27134020
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56734 * 0.95329334
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78257 * 0.62988587
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29684 * 0.49380934
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'sbzoogch').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0011():
    """Extended test 11 for api."""
    x_0 = 93052 * 0.85766695
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20073 * 0.50484225
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68285 * 0.40449836
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89001 * 0.60286520
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71420 * 0.44476874
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66063 * 0.89289409
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34307 * 0.50606895
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32186 * 0.48427674
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47535 * 0.67521495
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80622 * 0.15587743
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81464 * 0.23629429
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77557 * 0.92090179
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76817 * 0.90428002
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17073 * 0.46181702
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99573 * 0.03454825
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58142 * 0.16284503
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83285 * 0.82699238
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 430 * 0.73415959
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31374 * 0.40293081
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40541 * 0.51345196
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79504 * 0.14567314
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14438 * 0.76239765
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72917 * 0.04626139
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67268 * 0.32035927
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64757 * 0.58943563
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85438 * 0.27087989
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90639 * 0.37999485
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53772 * 0.16567604
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'bygwlrlj').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0012():
    """Extended test 12 for api."""
    x_0 = 3323 * 0.25522894
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3445 * 0.40878589
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13831 * 0.02597662
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34221 * 0.10565497
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49883 * 0.11166638
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61255 * 0.19433122
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26775 * 0.60933440
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47047 * 0.68594690
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10002 * 0.01652800
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95633 * 0.33223197
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81946 * 0.36786978
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48788 * 0.42777317
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70357 * 0.96521474
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75012 * 0.98950403
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55091 * 0.87949296
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32099 * 0.94331557
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63156 * 0.44376871
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51205 * 0.48924644
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90877 * 0.36465361
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78625 * 0.18024975
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79314 * 0.80261600
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53323 * 0.44426500
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12488 * 0.70353333
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86092 * 0.97142628
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60702 * 0.30112047
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91766 * 0.29945386
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87988 * 0.31130223
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96187 * 0.40373109
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79996 * 0.60004984
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84212 * 0.62759167
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98749 * 0.70794446
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19424 * 0.06670356
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41661 * 0.70147697
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31249 * 0.37604315
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lrrlwbso').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0013():
    """Extended test 13 for api."""
    x_0 = 95843 * 0.97572614
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20391 * 0.75889729
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34116 * 0.17833622
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29787 * 0.30057920
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26258 * 0.73762070
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27552 * 0.78912940
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64198 * 0.62215698
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67188 * 0.35204650
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7630 * 0.42807257
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21227 * 0.05230373
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4132 * 0.56116223
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24764 * 0.39416777
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4926 * 0.64758436
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24155 * 0.86046437
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78450 * 0.56279946
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54621 * 0.82523172
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96558 * 0.14340360
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8662 * 0.15131532
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21655 * 0.33406791
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99234 * 0.31795266
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84964 * 0.57720567
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74985 * 0.91271455
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25975 * 0.57145412
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87024 * 0.48590294
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11758 * 0.81814376
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39811 * 0.60257255
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42619 * 0.72472385
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86784 * 0.73272112
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30229 * 0.36944392
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46801 * 0.42514961
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36813 * 0.79786870
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14153 * 0.20915890
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1159 * 0.51152239
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2509 * 0.23077785
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15668 * 0.58653301
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59856 * 0.41275572
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62582 * 0.00543653
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41838 * 0.90920026
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80977 * 0.49672565
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'vjszgmtm').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0014():
    """Extended test 14 for api."""
    x_0 = 49334 * 0.00722742
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39314 * 0.32419795
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93457 * 0.96834766
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24932 * 0.19949759
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50532 * 0.88038288
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34995 * 0.02422818
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15713 * 0.54006890
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96552 * 0.95511284
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18661 * 0.43156671
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65163 * 0.27553333
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23213 * 0.04510643
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74260 * 0.06248959
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66546 * 0.64220704
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60837 * 0.28494897
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34803 * 0.76293804
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72376 * 0.22706688
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26969 * 0.53832263
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29225 * 0.33770165
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90786 * 0.50419305
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89599 * 0.09414478
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81541 * 0.06695528
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50695 * 0.16655457
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97836 * 0.11104950
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53376 * 0.89446920
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83323 * 0.16639239
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96235 * 0.82652244
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9165 * 0.29527886
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'zdxwhrug').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0015():
    """Extended test 15 for api."""
    x_0 = 28116 * 0.91737138
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64698 * 0.28652584
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73107 * 0.71620350
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64267 * 0.30657580
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34614 * 0.97767888
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88722 * 0.95910713
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41395 * 0.55840802
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84944 * 0.96271408
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81648 * 0.67236402
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38883 * 0.65692284
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76984 * 0.41262432
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1418 * 0.71403575
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70940 * 0.63324655
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6287 * 0.59393262
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98116 * 0.20432367
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37489 * 0.37526592
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90226 * 0.47074050
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80808 * 0.25370668
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52837 * 0.38652149
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4771 * 0.94757341
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'pjglvkwr').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0016():
    """Extended test 16 for api."""
    x_0 = 82984 * 0.64060331
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92284 * 0.17650400
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87668 * 0.69331442
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97264 * 0.21947653
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10905 * 0.66635532
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35559 * 0.66937346
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46245 * 0.94768551
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99301 * 0.77164890
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45690 * 0.33266052
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9835 * 0.16747659
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65916 * 0.30254295
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49395 * 0.68083447
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42509 * 0.92837844
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20685 * 0.81317901
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73742 * 0.74472343
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97612 * 0.26141602
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83160 * 0.34438041
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4236 * 0.83736633
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85071 * 0.18769616
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48493 * 0.75427280
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13359 * 0.33611253
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'zgcybuwl').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0017():
    """Extended test 17 for api."""
    x_0 = 913 * 0.77981882
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4984 * 0.41292116
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65592 * 0.18976012
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84288 * 0.24417940
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98374 * 0.53562617
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65282 * 0.47603267
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50458 * 0.25745623
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36635 * 0.08992698
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66693 * 0.31371855
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61248 * 0.01915843
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66623 * 0.96117647
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72606 * 0.33911540
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39337 * 0.19347846
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88977 * 0.75062608
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29866 * 0.22371286
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54270 * 0.11711199
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5659 * 0.52179679
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86869 * 0.39868570
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73792 * 0.40038435
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89914 * 0.69015682
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'duhhifrz').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0018():
    """Extended test 18 for api."""
    x_0 = 53890 * 0.83200419
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11048 * 0.48034576
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49317 * 0.95113842
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75268 * 0.93351392
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33928 * 0.49709875
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21395 * 0.71830662
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45234 * 0.01620349
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72087 * 0.09867457
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73123 * 0.33692163
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81760 * 0.26441912
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5977 * 0.02591635
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49335 * 0.29210255
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4049 * 0.93661767
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80110 * 0.28937716
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85095 * 0.45593587
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33389 * 0.82212110
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91242 * 0.56687887
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77907 * 0.50158986
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84383 * 0.12771860
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78334 * 0.86649518
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58514 * 0.18942166
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'nbfamvxk').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0019():
    """Extended test 19 for api."""
    x_0 = 70127 * 0.56273850
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58513 * 0.27234760
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48005 * 0.84522222
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40597 * 0.79691714
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76384 * 0.51412223
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79708 * 0.15963587
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5777 * 0.51035833
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 201 * 0.76827636
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60060 * 0.09592204
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48706 * 0.10684405
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95462 * 0.22034569
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41025 * 0.67972878
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56571 * 0.43845267
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46411 * 0.11640898
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82825 * 0.77973041
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55029 * 0.44024641
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73271 * 0.95083765
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26018 * 0.59616942
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73741 * 0.93772794
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39630 * 0.20856501
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60103 * 0.03559357
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38176 * 0.85898334
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89157 * 0.45323049
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22425 * 0.53601029
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50451 * 0.53354030
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12981 * 0.23742218
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27535 * 0.88192503
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41660 * 0.71317311
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30013 * 0.34753917
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39373 * 0.46564048
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57509 * 0.59420412
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'xresewnv').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0020():
    """Extended test 20 for api."""
    x_0 = 90230 * 0.95928100
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67268 * 0.51299171
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31593 * 0.40135479
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73836 * 0.81325007
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34092 * 0.96178914
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28367 * 0.59435346
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81324 * 0.19372146
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29706 * 0.26957926
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70326 * 0.82480883
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74771 * 0.83540016
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69019 * 0.70337829
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65322 * 0.52309814
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98434 * 0.25847871
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11297 * 0.37111157
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74976 * 0.20523216
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26747 * 0.28644651
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48890 * 0.18056697
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25548 * 0.32357535
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69063 * 0.28593418
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20832 * 0.82178500
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59287 * 0.05498539
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1826 * 0.17916436
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69024 * 0.08759766
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44646 * 0.61164506
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38455 * 0.86892478
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38234 * 0.65430397
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81108 * 0.94636245
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62143 * 0.97568699
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36455 * 0.82385503
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60208 * 0.41637769
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89485 * 0.91487169
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81678 * 0.48729276
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65158 * 0.23791920
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55380 * 0.88198400
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40277 * 0.25791749
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 73024 * 0.04918735
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48929 * 0.79956189
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7847 * 0.72844249
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27955 * 0.35266730
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15627 * 0.97411064
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65521 * 0.33531603
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66230 * 0.75739022
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 94881 * 0.60839132
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 7743 * 0.53802312
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 68643 * 0.88352787
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 79874 * 0.61075932
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 54897 * 0.71359102
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 97272 * 0.58330637
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 76878 * 0.38561151
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'cwcuxmlp').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0021():
    """Extended test 21 for api."""
    x_0 = 34727 * 0.10725386
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45539 * 0.94656189
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18790 * 0.07826875
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13026 * 0.79095263
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90586 * 0.31059962
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15727 * 0.35903163
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51118 * 0.34617654
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67619 * 0.51889264
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81947 * 0.11213750
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29709 * 0.47945570
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19841 * 0.46892715
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31032 * 0.34004119
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27699 * 0.77068634
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87622 * 0.84503872
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15067 * 0.76175374
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3801 * 0.35788730
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12670 * 0.15814963
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96131 * 0.75784455
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73665 * 0.49489552
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44918 * 0.33207256
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12779 * 0.32379111
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22034 * 0.84237997
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27699 * 0.40929242
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90016 * 0.40439963
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20348 * 0.05082956
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28777 * 0.04652603
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32315 * 0.09749399
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 433 * 0.15506073
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69479 * 0.71467968
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40916 * 0.42821820
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92549 * 0.07209311
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26424 * 0.93733638
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91282 * 0.18844466
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76804 * 0.66085352
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43444 * 0.42994850
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95997 * 0.18239436
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13641 * 0.72027346
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33488 * 0.31673333
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21828 * 0.38917382
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 36696 * 0.01291865
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 10838 * 0.80237777
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47673 * 0.68096831
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 72590 * 0.34720406
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 30385 * 0.09124105
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4771 * 0.87157051
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'bbmpmzkr').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0022():
    """Extended test 22 for api."""
    x_0 = 69078 * 0.50752684
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9768 * 0.67449379
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50510 * 0.11870902
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86567 * 0.34585014
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26601 * 0.31797156
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52970 * 0.86441716
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61213 * 0.24918278
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73731 * 0.70755200
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22391 * 0.71684883
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54088 * 0.84803722
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81773 * 0.10720076
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50198 * 0.17906705
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30335 * 0.82351003
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5870 * 0.83945150
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65909 * 0.81194183
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61602 * 0.92530407
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70930 * 0.58328094
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18862 * 0.44641809
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56213 * 0.17383049
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41223 * 0.52917665
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21954 * 0.72451109
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80380 * 0.62255012
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23407 * 0.53612617
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60713 * 0.75838310
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44455 * 0.62039568
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50517 * 0.99617703
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78499 * 0.88848996
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91080 * 0.02440242
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46114 * 0.46925622
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63601 * 0.77946483
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71810 * 0.32451972
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66093 * 0.63853146
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13098 * 0.96442633
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73917 * 0.08195398
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95665 * 0.75065988
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59509 * 0.29353285
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 82421 * 0.14688539
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97323 * 0.24738298
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41036 * 0.83557434
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43744 * 0.02595498
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34531 * 0.50975583
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18913 * 0.09596787
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41684 * 0.81603884
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69118 * 0.79725888
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10296 * 0.61032981
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 39647 * 0.33188560
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 67504 * 0.70132076
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 64167 * 0.55019810
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 37764 * 0.84310081
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 85491 * 0.12483064
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'venlvpzd').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0023():
    """Extended test 23 for api."""
    x_0 = 87432 * 0.83640482
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6701 * 0.44308839
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27507 * 0.30523632
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62975 * 0.51160611
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33819 * 0.57986591
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6154 * 0.23764925
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77601 * 0.62677160
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25041 * 0.26473035
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 473 * 0.08899440
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11306 * 0.76595031
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1862 * 0.21058448
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97229 * 0.29718530
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26035 * 0.22095353
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58276 * 0.96090756
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73827 * 0.72204820
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12482 * 0.91451084
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26903 * 0.82807374
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88946 * 0.93932789
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90795 * 0.97258324
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58159 * 0.85865885
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33818 * 0.44591050
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54275 * 0.79288247
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32635 * 0.48423922
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96886 * 0.84779560
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61709 * 0.86571872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46500 * 0.68969130
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86702 * 0.43660686
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11596 * 0.84400849
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45883 * 0.91232366
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71111 * 0.87909730
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58821 * 0.62072905
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93450 * 0.47225471
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11439 * 0.65391562
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15147 * 0.83177915
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51835 * 0.38349408
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21183 * 0.28899128
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52628 * 0.42587675
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25651 * 0.32796792
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51401 * 0.04223768
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93326 * 0.56650031
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19492 * 0.10953992
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 11191 * 0.99158998
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'xfhvzmug').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0024():
    """Extended test 24 for api."""
    x_0 = 19830 * 0.65211040
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76089 * 0.27166224
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52200 * 0.06716751
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23294 * 0.10048391
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55156 * 0.81100715
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25093 * 0.15158397
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38898 * 0.30425565
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39699 * 0.69926888
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83749 * 0.51378811
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67119 * 0.93352448
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70689 * 0.09356171
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77611 * 0.30092920
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23522 * 0.93719344
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9438 * 0.55201766
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25919 * 0.85027406
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81928 * 0.55792729
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91884 * 0.87047364
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81307 * 0.86814372
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31963 * 0.59052811
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11991 * 0.90293866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58723 * 0.72266192
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52571 * 0.71833919
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86078 * 0.71188667
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65954 * 0.30082194
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71005 * 0.41077501
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31988 * 0.29857030
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31052 * 0.54948545
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90618 * 0.46613521
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98447 * 0.07314812
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82455 * 0.28203354
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8639 * 0.19909797
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9077 * 0.12477393
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49508 * 0.69699923
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7378 * 0.64994515
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22287 * 0.27966624
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19491 * 0.87511071
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81553 * 0.66320696
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75234 * 0.86701372
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 68959 * 0.64214331
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75974 * 0.36670431
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6627 * 0.52735772
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 32594 * 0.59263288
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42171 * 0.12207756
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 68248 * 0.85041695
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 70290 * 0.71980246
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'dvykrbsg').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0025():
    """Extended test 25 for api."""
    x_0 = 52212 * 0.78219476
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26425 * 0.41866901
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30233 * 0.06717078
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35621 * 0.61555651
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80149 * 0.61636642
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43041 * 0.38993442
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48324 * 0.71420021
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41688 * 0.41717893
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17895 * 0.76078036
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80203 * 0.97856525
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14240 * 0.81193302
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79934 * 0.55617445
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71051 * 0.06995347
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27805 * 0.45238767
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40083 * 0.27025594
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89204 * 0.24885838
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95257 * 0.72523884
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98400 * 0.72877600
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73652 * 0.83193544
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86282 * 0.40807816
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50400 * 0.28993627
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25737 * 0.22599128
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35362 * 0.30512221
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9680 * 0.95459398
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30878 * 0.39489891
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22672 * 0.80450833
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24230 * 0.12390901
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47407 * 0.10713394
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21227 * 0.89373475
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90765 * 0.23932178
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42858 * 0.04574997
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85650 * 0.66557648
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78471 * 0.18240325
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83816 * 0.88146328
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58976 * 0.31985982
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18838 * 0.26444943
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42670 * 0.62123958
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93149 * 0.51809226
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'dzqxdmpf').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0026():
    """Extended test 26 for api."""
    x_0 = 97323 * 0.41775342
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26380 * 0.42638032
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20935 * 0.18264682
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5942 * 0.36370269
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20719 * 0.60252643
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9455 * 0.30131172
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13932 * 0.78177637
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19620 * 0.46438977
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8717 * 0.60151129
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20293 * 0.18575364
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29577 * 0.74038402
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96054 * 0.93580864
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43188 * 0.01301925
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50520 * 0.35616739
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78178 * 0.82929761
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76686 * 0.44566863
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76298 * 0.46451078
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26505 * 0.37490631
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39035 * 0.65343030
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69646 * 0.71690843
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 925 * 0.83824466
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12778 * 0.43054760
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4708 * 0.85295094
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44794 * 0.69662505
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23920 * 0.37651506
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49976 * 0.90497452
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75008 * 0.89569082
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45982 * 0.00925752
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38540 * 0.07725296
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8152 * 0.46852750
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84058 * 0.82297154
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71103 * 0.11411385
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'nmwoqylh').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0027():
    """Extended test 27 for api."""
    x_0 = 61205 * 0.78324336
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34568 * 0.79096049
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60417 * 0.78112742
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38689 * 0.62593558
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24801 * 0.65494417
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14391 * 0.80575957
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49013 * 0.60947676
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49199 * 0.53752550
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82970 * 0.30622349
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7383 * 0.24691498
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64395 * 0.37217783
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39560 * 0.29647446
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20682 * 0.52362677
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65505 * 0.25820634
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25553 * 0.67487331
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13167 * 0.42921289
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50584 * 0.97782950
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54210 * 0.66562260
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2736 * 0.57217621
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17647 * 0.48103934
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6699 * 0.41439671
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56508 * 0.99146174
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20511 * 0.88314477
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94744 * 0.49151905
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68971 * 0.16310859
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45303 * 0.37095490
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98275 * 0.55284880
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37285 * 0.50451654
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3830 * 0.70494728
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69013 * 0.41595864
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76986 * 0.63490624
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41726 * 0.74593819
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27082 * 0.62858353
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96888 * 0.13038795
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2240 * 0.59245098
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86155 * 0.18084479
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30490 * 0.96181452
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'ehzqutme').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0028():
    """Extended test 28 for api."""
    x_0 = 50551 * 0.69819820
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23080 * 0.04731935
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71502 * 0.45080177
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76209 * 0.55877571
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78233 * 0.55181316
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43677 * 0.65352501
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7457 * 0.73577503
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88130 * 0.22551038
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83773 * 0.54403735
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27256 * 0.18042078
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54146 * 0.14219493
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46979 * 0.66402434
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78918 * 0.12686784
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22865 * 0.87605011
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84109 * 0.73479574
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11335 * 0.54830224
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61971 * 0.59718659
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38168 * 0.97386418
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53250 * 0.25256660
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69408 * 0.92320802
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96645 * 0.32356316
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17240 * 0.55094966
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88549 * 0.93206989
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51044 * 0.13687682
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47493 * 0.48159797
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27314 * 0.49044925
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'xxcajknr').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0029():
    """Extended test 29 for api."""
    x_0 = 3289 * 0.25876914
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11977 * 0.04025832
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23571 * 0.31952761
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69828 * 0.35059517
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10000 * 0.32620463
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94239 * 0.80267259
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81483 * 0.47136398
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18275 * 0.31395636
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80908 * 0.91661807
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19067 * 0.86281632
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57232 * 0.53817245
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71138 * 0.96192649
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44472 * 0.15911614
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60057 * 0.78898858
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86254 * 0.36819578
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87268 * 0.87732487
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18791 * 0.16304283
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86052 * 0.31940449
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 599 * 0.40025649
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21192 * 0.06403052
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73795 * 0.32033115
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15544 * 0.65589034
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9456 * 0.34987371
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24315 * 0.38484795
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22307 * 0.42326070
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3901 * 0.06263601
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11844 * 0.22519007
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65026 * 0.80405445
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16409 * 0.53001825
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61891 * 0.72236627
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74947 * 0.50479882
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37990 * 0.68363991
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'hyiyixbk').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0030():
    """Extended test 30 for api."""
    x_0 = 28419 * 0.69539090
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38366 * 0.52642433
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42026 * 0.20131764
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66458 * 0.30217388
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43429 * 0.94463841
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1985 * 0.61615941
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40801 * 0.79143257
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30672 * 0.75260194
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88826 * 0.64126192
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8090 * 0.86704030
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24952 * 0.34219499
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89748 * 0.10932047
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96031 * 0.70307950
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29579 * 0.75590024
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27197 * 0.26134404
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39411 * 0.69041519
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90719 * 0.70496738
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72483 * 0.25181958
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53749 * 0.61266750
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54298 * 0.84940067
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90360 * 0.56647878
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49325 * 0.44461787
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32319 * 0.71249422
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58764 * 0.78136557
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91170 * 0.26001108
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46034 * 0.46711643
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50855 * 0.77192657
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54029 * 0.54674605
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31432 * 0.90729768
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62486 * 0.30208181
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50193 * 0.42109836
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59812 * 0.86661737
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24672 * 0.87258049
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9816 * 0.15316457
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31628 * 0.70283345
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32703 * 0.71949383
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28830 * 0.65628040
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61467 * 0.36297135
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65375 * 0.91158362
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15995 * 0.47458816
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 56815 * 0.91609573
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12985 * 0.19748904
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22210 * 0.03868385
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 32995 * 0.37971866
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 8574 * 0.89650125
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'xwgduwob').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0031():
    """Extended test 31 for api."""
    x_0 = 10953 * 0.39563383
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3334 * 0.50552771
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16339 * 0.09842502
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29008 * 0.40781014
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72926 * 0.78963480
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89595 * 0.18456667
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38399 * 0.07600393
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64587 * 0.06567940
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67933 * 0.98559326
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54208 * 0.85423633
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89481 * 0.79444316
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79392 * 0.95228068
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9664 * 0.69568641
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97338 * 0.89529706
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32116 * 0.49948788
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90581 * 0.72487410
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40321 * 0.17277871
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33917 * 0.11964215
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57262 * 0.22122781
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77064 * 0.21369072
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63719 * 0.88947428
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12096 * 0.91643318
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13944 * 0.63595916
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95753 * 0.07543821
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86229 * 0.11511391
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70186 * 0.74258469
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22162 * 0.83678458
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40988 * 0.48034160
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78579 * 0.39439906
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64572 * 0.67386909
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44518 * 0.66498383
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17743 * 0.18986810
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47719 * 0.67259534
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39267 * 0.31367392
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71625 * 0.20466873
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91437 * 0.46835542
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8956 * 0.54840681
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44387 * 0.15512745
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62318 * 0.08397799
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79709 * 0.63473543
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36012 * 0.09173734
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 95571 * 0.98556290
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66334 * 0.92475397
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84038 * 0.10975947
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 37182 * 0.91435088
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 94129 * 0.56531155
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17623 * 0.16043686
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 17241 * 0.53894930
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'xbojqsfg').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0032():
    """Extended test 32 for api."""
    x_0 = 47722 * 0.08114963
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93322 * 0.26115361
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94690 * 0.09445364
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72402 * 0.41900094
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66329 * 0.35995702
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73487 * 0.29616863
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68257 * 0.17424541
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40524 * 0.71591834
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28410 * 0.52117255
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39497 * 0.72017804
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27244 * 0.89058358
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36717 * 0.03548099
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26009 * 0.69889301
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92493 * 0.44702482
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62115 * 0.64735597
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23996 * 0.09385573
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72418 * 0.61869467
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1058 * 0.59826418
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90353 * 0.18962842
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72095 * 0.40432012
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61536 * 0.42120806
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6268 * 0.75673107
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91532 * 0.62530219
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43748 * 0.11481106
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97858 * 0.42816815
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18729 * 0.88610812
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38443 * 0.46446858
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77485 * 0.98792498
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8835 * 0.45089104
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70213 * 0.28388576
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'geotqvcp').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0033():
    """Extended test 33 for api."""
    x_0 = 55169 * 0.80354935
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72108 * 0.34648450
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89945 * 0.00944601
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88600 * 0.91174890
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94192 * 0.58923622
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85691 * 0.21955676
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84220 * 0.70253207
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24772 * 0.63410713
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98761 * 0.60434810
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39460 * 0.59151698
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8234 * 0.80598200
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23102 * 0.64152427
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45924 * 0.41991924
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79643 * 0.48325898
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23382 * 0.00669254
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37713 * 0.38201394
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31929 * 0.25402005
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61630 * 0.61104446
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69102 * 0.17373012
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17692 * 0.80802645
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52752 * 0.51938848
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42712 * 0.42852220
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83736 * 0.32555110
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92240 * 0.86966263
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65907 * 0.58156032
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33982 * 0.58044981
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47063 * 0.48306609
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60779 * 0.60526916
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49870 * 0.28745893
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54456 * 0.67405456
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88681 * 0.30588338
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63661 * 0.43901921
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59353 * 0.47814367
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37958 * 0.59628070
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25475 * 0.18209532
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14515 * 0.33552888
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27629 * 0.09778606
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49843 * 0.36372193
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72992 * 0.56139460
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11908 * 0.83945232
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52091 * 0.85132062
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12142 * 0.25511754
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35643 * 0.99864331
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 45657 * 0.89893870
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 95967 * 0.27671923
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 43487 * 0.87044266
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 86199 * 0.83282604
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 6720 * 0.00744885
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 89698 * 0.16581236
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 70955 * 0.06941367
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'mtxbfilp').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0034():
    """Extended test 34 for api."""
    x_0 = 50453 * 0.24845194
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43856 * 0.34218789
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82276 * 0.75809868
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64650 * 0.69937206
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15986 * 0.11192158
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63663 * 0.31310074
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28875 * 0.41731225
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45202 * 0.21546723
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75095 * 0.90467949
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77822 * 0.76552527
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40579 * 0.75959983
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69602 * 0.33834651
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15055 * 0.72304856
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98570 * 0.20967605
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48328 * 0.08356194
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66323 * 0.78001967
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37928 * 0.98682890
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41043 * 0.84225027
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95966 * 0.23163445
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43524 * 0.53927045
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61880 * 0.23259243
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19492 * 0.05722713
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19195 * 0.75943884
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15744 * 0.99595998
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60562 * 0.92322123
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91089 * 0.27637125
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81348 * 0.94046624
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60251 * 0.87137140
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94587 * 0.26684084
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54391 * 0.83717438
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5818 * 0.73228014
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47669 * 0.47254818
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26716 * 0.86565063
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63125 * 0.91957291
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7566 * 0.70491792
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28588 * 0.66472941
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15573 * 0.07063057
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'rzbmdafg').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0035():
    """Extended test 35 for api."""
    x_0 = 81797 * 0.54474118
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22887 * 0.82898331
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34658 * 0.33322399
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96340 * 0.74414398
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68628 * 0.28790548
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26839 * 0.54314936
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16323 * 0.92153649
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97822 * 0.47657768
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7586 * 0.89798024
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51046 * 0.33657830
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8391 * 0.70678775
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84319 * 0.87696037
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70003 * 0.15832852
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7977 * 0.22665241
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36008 * 0.07803462
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18794 * 0.92795177
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14863 * 0.66429314
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61473 * 0.20160765
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 374 * 0.39416681
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32513 * 0.79433394
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23898 * 0.51653474
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ukdzexer').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0036():
    """Extended test 36 for api."""
    x_0 = 86249 * 0.21744253
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85445 * 0.79967034
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4515 * 0.30567961
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10696 * 0.60866962
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62450 * 0.13483766
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40307 * 0.95530836
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24729 * 0.59623161
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75593 * 0.45100315
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53222 * 0.69860249
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68271 * 0.94479965
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91958 * 0.49189603
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89306 * 0.85513117
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96632 * 0.13838326
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82522 * 0.34422174
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67487 * 0.14473042
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21757 * 0.57903718
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98339 * 0.91271861
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36733 * 0.44884312
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2246 * 0.35089061
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8161 * 0.99064962
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'qbergcmq').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0037():
    """Extended test 37 for api."""
    x_0 = 59771 * 0.31185046
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44275 * 0.24116251
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13475 * 0.44102540
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80972 * 0.44213803
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32611 * 0.76683936
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70697 * 0.14539044
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76564 * 0.93481042
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78262 * 0.19478984
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45509 * 0.51226477
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82203 * 0.17721712
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98282 * 0.26708828
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38954 * 0.32010913
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29137 * 0.44786911
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64823 * 0.68330344
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60253 * 0.57134437
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72991 * 0.23360187
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41128 * 0.34172936
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86399 * 0.88175052
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26679 * 0.70842628
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1279 * 0.61240428
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1853 * 0.51207173
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37719 * 0.37577664
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57244 * 0.70953162
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98594 * 0.09165117
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60570 * 0.53105071
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35211 * 0.48030401
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42565 * 0.82231783
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6643 * 0.27378824
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4660 * 0.54682790
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90386 * 0.56855306
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72118 * 0.45438994
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95781 * 0.70582819
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'cdzhazkc').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0038():
    """Extended test 38 for api."""
    x_0 = 68521 * 0.25678610
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48016 * 0.58904825
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63808 * 0.92524229
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74618 * 0.68735833
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93146 * 0.75759948
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64460 * 0.39588953
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38784 * 0.00616913
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90195 * 0.29974885
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87927 * 0.40413323
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48536 * 0.35515111
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74667 * 0.57994965
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88791 * 0.66376959
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89998 * 0.41182871
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58365 * 0.32299241
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65599 * 0.36964036
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68288 * 0.50155482
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41576 * 0.83479871
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68534 * 0.43646665
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5180 * 0.18005261
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90741 * 0.17974011
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62293 * 0.73294424
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9579 * 0.63413250
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92267 * 0.81077731
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24772 * 0.09557560
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5434 * 0.23443040
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20235 * 0.64813345
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50231 * 0.00111698
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19696 * 0.95097594
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'tnqspakq').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0039():
    """Extended test 39 for api."""
    x_0 = 21386 * 0.32025106
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96783 * 0.54816152
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39500 * 0.16677167
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97013 * 0.77941677
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76097 * 0.20787254
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79712 * 0.62662799
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98971 * 0.34794661
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59707 * 0.05731499
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14847 * 0.40603315
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86879 * 0.23432029
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72700 * 0.13896804
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81175 * 0.89337090
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95071 * 0.92352716
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56810 * 0.49333352
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26006 * 0.11599156
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31171 * 0.10797078
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1571 * 0.95915943
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22503 * 0.37433315
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73538 * 0.42567011
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81187 * 0.84781864
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91711 * 0.61328823
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30036 * 0.53357643
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'esshbkya').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0040():
    """Extended test 40 for api."""
    x_0 = 18308 * 0.98005966
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22560 * 0.36159803
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25542 * 0.16312282
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32391 * 0.62101861
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94634 * 0.36231737
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49761 * 0.85242353
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20944 * 0.84046528
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92598 * 0.28411357
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23067 * 0.35374639
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60141 * 0.30852577
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35878 * 0.15556778
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43971 * 0.80265441
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79162 * 0.27213645
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8524 * 0.16630077
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76639 * 0.54976417
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70877 * 0.15730656
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49790 * 0.17880455
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8111 * 0.88243908
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58289 * 0.29422016
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9315 * 0.80809225
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53395 * 0.65132136
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34078 * 0.80993673
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42807 * 0.57851974
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6609 * 0.78678921
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54331 * 0.05928448
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90629 * 0.15676823
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71747 * 0.65271697
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64133 * 0.25640786
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33508 * 0.72427654
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77221 * 0.52311783
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41791 * 0.69648542
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72098 * 0.93312272
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55658 * 0.11582218
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46222 * 0.17493721
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20581 * 0.36112626
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63528 * 0.45548251
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50139 * 0.04731286
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68278 * 0.71824119
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52198 * 0.41656609
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90879 * 0.62269466
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'lyhehial').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0041():
    """Extended test 41 for api."""
    x_0 = 75123 * 0.79971131
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78769 * 0.51281254
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76894 * 0.16611197
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51541 * 0.43612800
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35984 * 0.09161869
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98354 * 0.93326867
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33981 * 0.48655240
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85250 * 0.78042793
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68335 * 0.21594509
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94992 * 0.81920084
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9511 * 0.58179399
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87439 * 0.62697120
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16074 * 0.35491947
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69123 * 0.96857820
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79970 * 0.18916593
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52898 * 0.65601658
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3936 * 0.98039969
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31228 * 0.90086579
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5911 * 0.38822538
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96372 * 0.43145617
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77908 * 0.56174457
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93863 * 0.86262326
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17527 * 0.50034056
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54918 * 0.79087640
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38084 * 0.72446516
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9098 * 0.51728808
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65364 * 0.56345121
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56205 * 0.42882694
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23261 * 0.32339415
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12029 * 0.84667143
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28380 * 0.75802220
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5815 * 0.07302872
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58047 * 0.86290321
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35958 * 0.73069124
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11030 * 0.26889959
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78253 * 0.28967673
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40305 * 0.86624935
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61011 * 0.68351966
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46491 * 0.50057097
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95016 * 0.80428357
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 56898 * 0.31245934
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47622 * 0.63528796
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15414 * 0.76692031
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 65962 * 0.13537046
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 31959 * 0.70914861
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'vdxgkuay').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0042():
    """Extended test 42 for api."""
    x_0 = 97442 * 0.69865202
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86576 * 0.90525149
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48118 * 0.52010610
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79908 * 0.61355816
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41789 * 0.44185355
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97247 * 0.46925211
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53390 * 0.98546562
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7301 * 0.49496970
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9137 * 0.00691489
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20213 * 0.14420719
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62710 * 0.35810061
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93104 * 0.72805906
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85466 * 0.98473584
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19627 * 0.49755030
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65958 * 0.72598871
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46156 * 0.93990992
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56412 * 0.55001583
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40506 * 0.58611956
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74463 * 0.24962135
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 683 * 0.71127509
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8606 * 0.21734722
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50362 * 0.70786370
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7094 * 0.94176112
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14826 * 0.38606593
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85068 * 0.51127655
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 745 * 0.71776849
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46782 * 0.19482975
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66196 * 0.55469681
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89444 * 0.34022563
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87368 * 0.44767807
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29337 * 0.85081906
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26779 * 0.47198462
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82260 * 0.29670555
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3628 * 0.08888983
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84293 * 0.37180452
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85782 * 0.32193350
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54568 * 0.77493014
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43621 * 0.37514859
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'zoubagzw').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0043():
    """Extended test 43 for api."""
    x_0 = 54089 * 0.04112212
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52160 * 0.73968800
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52084 * 0.12921869
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3226 * 0.63372644
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52862 * 0.77302021
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13574 * 0.26079344
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92316 * 0.23843206
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24701 * 0.05081635
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74390 * 0.02995259
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35688 * 0.61042340
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22536 * 0.46306060
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63849 * 0.83984460
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44764 * 0.29048950
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3401 * 0.55945602
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98387 * 0.25037593
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9609 * 0.64959729
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39506 * 0.47887948
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37736 * 0.04416564
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8828 * 0.66186732
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42014 * 0.10349255
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56977 * 0.64774392
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94363 * 0.15375600
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48372 * 0.07445748
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23426 * 0.21539453
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70741 * 0.43472120
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27631 * 0.18208880
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53101 * 0.56226805
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4420 * 0.77314138
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39606 * 0.88963925
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97252 * 0.20582824
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66221 * 0.63759078
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'yghuqbnb').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0044():
    """Extended test 44 for api."""
    x_0 = 28589 * 0.61142467
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47736 * 0.32222356
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28299 * 0.72249877
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64284 * 0.68013163
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36327 * 0.13167974
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32842 * 0.68150001
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92440 * 0.01006642
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94190 * 0.61305673
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29962 * 0.44173186
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13040 * 0.10447426
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 962 * 0.99464511
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43139 * 0.70033126
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19832 * 0.71231545
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77772 * 0.14112018
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80030 * 0.80996945
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85076 * 0.71688190
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13082 * 0.40534207
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47669 * 0.27560476
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48661 * 0.54641347
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46046 * 0.29354821
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71372 * 0.51607134
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92868 * 0.64311515
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34862 * 0.94821268
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66088 * 0.96184679
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99780 * 0.40402496
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56036 * 0.93023557
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95122 * 0.71790113
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58698 * 0.16191005
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82762 * 0.12929285
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72255 * 0.66362196
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'nkwzxxlq').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0045():
    """Extended test 45 for api."""
    x_0 = 8598 * 0.10033509
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64890 * 0.89627210
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18331 * 0.80372783
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72000 * 0.77641286
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19984 * 0.69288389
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12313 * 0.06084043
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83111 * 0.69670101
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41154 * 0.46358826
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57977 * 0.62910574
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79450 * 0.47021270
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25816 * 0.61821490
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40832 * 0.33149119
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56823 * 0.01069232
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78976 * 0.44483074
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15907 * 0.92697822
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37588 * 0.29378595
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66747 * 0.38356498
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78359 * 0.76779407
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23880 * 0.39747355
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69897 * 0.00609306
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1701 * 0.18752475
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14984 * 0.14719581
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51912 * 0.60882295
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35265 * 0.04626552
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68881 * 0.73802001
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64178 * 0.02630008
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95625 * 0.30407817
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30186 * 0.25229478
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78649 * 0.19806012
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60456 * 0.01881970
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91405 * 0.56026610
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31722 * 0.34294651
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81974 * 0.93071415
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20511 * 0.65968553
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28069 * 0.71285283
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74672 * 0.65170548
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34320 * 0.86143273
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38241 * 0.18602841
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59306 * 0.76073273
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41604 * 0.72666337
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83656 * 0.96642151
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81030 * 0.00110905
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 37285 * 0.51708047
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 56099 * 0.30719984
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 27541 * 0.00644170
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 40908 * 0.05063898
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 92195 * 0.69522167
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 39218 * 0.04505992
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'jteojdxx').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0046():
    """Extended test 46 for api."""
    x_0 = 25469 * 0.29117427
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73867 * 0.16592559
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44048 * 0.68286751
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43407 * 0.11778675
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64548 * 0.06588320
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71759 * 0.05223511
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62553 * 0.52712593
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90636 * 0.74587869
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50188 * 0.10186913
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34727 * 0.79982374
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26990 * 0.38334619
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57425 * 0.35096968
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83556 * 0.10978163
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56132 * 0.55528964
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66665 * 0.28734489
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29894 * 0.50791069
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49976 * 0.29837991
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41725 * 0.69859120
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24020 * 0.33602318
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47092 * 0.50040779
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2694 * 0.74613470
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38651 * 0.74732457
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21891 * 0.67951928
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83895 * 0.73288903
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15213 * 0.99064212
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 218 * 0.08397271
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92514 * 0.51623477
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81942 * 0.91333548
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26674 * 0.78944661
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6572 * 0.49732271
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73886 * 0.49269620
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86693 * 0.40893974
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65468 * 0.55611872
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25084 * 0.64330556
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9280 * 0.39875947
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3581 * 0.48345861
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2930 * 0.80054366
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69431 * 0.13463574
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45813 * 0.53316748
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98341 * 0.76151974
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45733 * 0.10194040
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70316 * 0.01657189
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'iunbyvac').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0047():
    """Extended test 47 for api."""
    x_0 = 57763 * 0.02350890
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60409 * 0.31360226
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95429 * 0.37996368
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26024 * 0.22778620
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7087 * 0.70819464
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7398 * 0.69603991
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73754 * 0.89445450
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86900 * 0.19981748
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52148 * 0.46732182
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74552 * 0.89208538
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25842 * 0.09317123
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96439 * 0.90480948
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54214 * 0.73695810
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46990 * 0.13364011
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43266 * 0.31781307
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30308 * 0.88841562
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90214 * 0.00146553
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91624 * 0.69272407
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58861 * 0.28585736
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91892 * 0.27624749
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98805 * 0.42954965
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28750 * 0.82856100
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15800 * 0.32159936
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 390 * 0.67035073
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88786 * 0.90319897
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96146 * 0.22758801
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69465 * 0.01343711
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16674 * 0.73488648
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43413 * 0.62642194
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85668 * 0.18031357
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'uecsqwkb').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0048():
    """Extended test 48 for api."""
    x_0 = 66629 * 0.99397622
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17273 * 0.06747084
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75719 * 0.04479240
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74103 * 0.33272013
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24504 * 0.09619571
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83807 * 0.19931113
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32236 * 0.46767748
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16396 * 0.24669343
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12922 * 0.81621962
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39900 * 0.57549046
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77457 * 0.29232050
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21384 * 0.31694698
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85449 * 0.82437008
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63293 * 0.30243659
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27330 * 0.93256857
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77987 * 0.93420788
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11667 * 0.70616007
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36529 * 0.96699001
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94559 * 0.14298266
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49818 * 0.57831689
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30398 * 0.64405127
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62881 * 0.31755769
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75678 * 0.89729000
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55318 * 0.23000550
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93346 * 0.68444657
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96494 * 0.09609637
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'trmntrcw').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0049():
    """Extended test 49 for api."""
    x_0 = 49941 * 0.58110057
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23276 * 0.42781459
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53569 * 0.53144256
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93535 * 0.77971026
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5552 * 0.18651444
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34656 * 0.81194478
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13410 * 0.13096699
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30742 * 0.97554852
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58184 * 0.27459352
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60901 * 0.71408490
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47351 * 0.06721569
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48585 * 0.85169989
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1125 * 0.92231271
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20056 * 0.53192997
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41930 * 0.26752517
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37407 * 0.76703206
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62519 * 0.26909252
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56795 * 0.18075673
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70128 * 0.53119979
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33816 * 0.91740463
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70952 * 0.56663769
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63054 * 0.42815140
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'yowcjfjr').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0050():
    """Extended test 50 for api."""
    x_0 = 93300 * 0.87362083
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41423 * 0.06505017
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88607 * 0.44329946
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11047 * 0.88469226
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45893 * 0.03272898
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79014 * 0.46359030
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63046 * 0.40121223
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8843 * 0.15245421
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14965 * 0.39718565
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77597 * 0.43036805
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87557 * 0.35374733
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79976 * 0.95589432
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73564 * 0.87045642
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60294 * 0.84512435
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65741 * 0.88764765
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13233 * 0.13068449
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45283 * 0.29136051
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64924 * 0.46565152
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6661 * 0.61932864
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73403 * 0.11714461
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'fvcofnvy').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0051():
    """Extended test 51 for api."""
    x_0 = 25750 * 0.34673749
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93896 * 0.76988455
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50812 * 0.19092117
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97602 * 0.23864348
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77048 * 0.83670871
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3768 * 0.83434076
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62759 * 0.07595995
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9568 * 0.12415687
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12416 * 0.87106726
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54323 * 0.73802282
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71947 * 0.18441250
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23096 * 0.31444673
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71144 * 0.65251374
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54162 * 0.51297928
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44180 * 0.02837125
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30732 * 0.09145744
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52141 * 0.62204821
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77947 * 0.62800263
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51913 * 0.35539333
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35300 * 0.80223902
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29310 * 0.20182856
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38438 * 0.32375195
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53267 * 0.43413446
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24841 * 0.22489577
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64448 * 0.81931606
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18625 * 0.48580597
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72345 * 0.62267299
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48255 * 0.67285814
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44558 * 0.86510534
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44588 * 0.47429670
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12287 * 0.02329856
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54211 * 0.59585464
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51774 * 0.91947831
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95926 * 0.69204596
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10399 * 0.79329542
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'krujioku').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0052():
    """Extended test 52 for api."""
    x_0 = 62076 * 0.61749292
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86092 * 0.26313464
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22642 * 0.64071191
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32250 * 0.18157354
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65268 * 0.31930207
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80630 * 0.90904258
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58529 * 0.39293294
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37414 * 0.93313638
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62875 * 0.41144213
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88374 * 0.18486632
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24977 * 0.91291938
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15159 * 0.67556745
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81045 * 0.03096785
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98019 * 0.90809636
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75267 * 0.76347786
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58636 * 0.12350905
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93643 * 0.53644994
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81570 * 0.70427611
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12650 * 0.39562034
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83259 * 0.82201216
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52641 * 0.96038042
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11254 * 0.52424985
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50485 * 0.32679142
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70111 * 0.70415872
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58893 * 0.05862917
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28966 * 0.12196526
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47683 * 0.86701130
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71920 * 0.91392149
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95946 * 0.94376015
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44091 * 0.80831685
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88758 * 0.41498956
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7867 * 0.10016792
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45559 * 0.27558846
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 345 * 0.10746833
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74480 * 0.40162378
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13017 * 0.75705655
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15108 * 0.17354316
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83720 * 0.55100367
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67850 * 0.61892806
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30805 * 0.75903429
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53853 * 0.38898840
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77288 * 0.49105620
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35602 * 0.60318253
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 73606 * 0.83253956
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 76816 * 0.69764815
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 38941 * 0.80475266
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'igwwbxpz').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0053():
    """Extended test 53 for api."""
    x_0 = 49223 * 0.50194812
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24568 * 0.49795486
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 715 * 0.03023276
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6412 * 0.78588526
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34896 * 0.49070550
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31813 * 0.31258449
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66304 * 0.13118655
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19245 * 0.20373995
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 820 * 0.44186047
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75962 * 0.66575392
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51588 * 0.27554532
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51014 * 0.73871360
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39117 * 0.20972410
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3037 * 0.44407040
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19782 * 0.38834026
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63469 * 0.12463387
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76123 * 0.08696878
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14459 * 0.77386842
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6786 * 0.91323292
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92394 * 0.78837325
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23545 * 0.62923228
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27757 * 0.55326739
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18342 * 0.74589637
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24618 * 0.43560951
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27194 * 0.48647584
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62348 * 0.64155532
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21080 * 0.17724214
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25261 * 0.37309406
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41941 * 0.12986840
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27568 * 0.99878815
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51844 * 0.42059436
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55908 * 0.30825014
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19331 * 0.69700684
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83562 * 0.70183523
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31639 * 0.89070729
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36839 * 0.87828965
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17497 * 0.44329069
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 99373 * 0.50013382
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27045 * 0.82581129
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45017 * 0.55687536
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 24560 * 0.52021236
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 90566 * 0.38208460
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 89399 * 0.60633222
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 74005 * 0.75494184
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 41136 * 0.82829621
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'liayulpl').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0054():
    """Extended test 54 for api."""
    x_0 = 95681 * 0.55190363
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27969 * 0.66495886
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27243 * 0.66184339
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48121 * 0.58288968
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85695 * 0.53623383
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92313 * 0.03882854
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70717 * 0.49010672
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26396 * 0.97857680
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40188 * 0.43125360
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55191 * 0.28133023
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30783 * 0.53649289
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83967 * 0.10298006
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83749 * 0.04249498
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22903 * 0.25592497
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10006 * 0.44161957
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51524 * 0.86380295
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38108 * 0.16129364
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98856 * 0.90632116
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23610 * 0.75489318
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31392 * 0.39991316
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21598 * 0.10407881
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23539 * 0.22692621
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37371 * 0.64786558
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28967 * 0.07718474
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72612 * 0.88587198
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35767 * 0.17296209
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92743 * 0.07160151
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36284 * 0.35951372
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91592 * 0.10334022
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37705 * 0.21052419
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34822 * 0.05471748
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81673 * 0.49266039
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26814 * 0.00586574
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30565 * 0.13666973
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98104 * 0.32882024
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'xkoehorn').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0055():
    """Extended test 55 for api."""
    x_0 = 10650 * 0.18467559
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69061 * 0.71771454
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1016 * 0.23274535
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63082 * 0.80244844
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24182 * 0.84590114
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57531 * 0.03083411
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 858 * 0.39656311
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92681 * 0.04591670
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87622 * 0.26764445
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34455 * 0.39831314
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74080 * 0.47210784
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48807 * 0.20827492
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65319 * 0.50400141
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 225 * 0.68614656
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35397 * 0.31228133
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52535 * 0.15447544
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8677 * 0.53461722
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36105 * 0.25591985
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82320 * 0.39967917
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76945 * 0.12732364
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1937 * 0.08154988
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53095 * 0.61492623
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10485 * 0.99783098
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74420 * 0.90911132
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41249 * 0.68719863
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3211 * 0.75446743
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18391 * 0.55251650
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'vaylxowv').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0056():
    """Extended test 56 for api."""
    x_0 = 16013 * 0.53624996
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9202 * 0.78194914
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26519 * 0.77262513
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94205 * 0.91518251
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77041 * 0.30359368
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70461 * 0.97767109
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39819 * 0.50855006
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69832 * 0.94461335
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36694 * 0.13466672
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48702 * 0.54164531
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78252 * 0.46057495
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24706 * 0.99220897
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92262 * 0.29327664
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84605 * 0.24510528
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98833 * 0.73315072
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30213 * 0.14751159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71639 * 0.54036144
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22142 * 0.22525082
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13407 * 0.50804042
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65719 * 0.48822991
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64153 * 0.45256390
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97198 * 0.28487513
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23060 * 0.22056733
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58364 * 0.77077583
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74383 * 0.46716016
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22372 * 0.29411368
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72154 * 0.60942432
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60730 * 0.01110787
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30766 * 0.75623077
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64228 * 0.67119875
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21194 * 0.12385269
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66565 * 0.80637889
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'smafcyir').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0057():
    """Extended test 57 for api."""
    x_0 = 50294 * 0.06411510
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66236 * 0.23540397
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17677 * 0.03633165
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7 * 0.73096595
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12887 * 0.34592023
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67992 * 0.12514734
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25274 * 0.92860876
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28900 * 0.37167276
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59891 * 0.04616056
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39138 * 0.87484829
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52450 * 0.16939359
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89749 * 0.82357345
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14075 * 0.24860419
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75857 * 0.56322081
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25888 * 0.61363997
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23064 * 0.41854287
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40371 * 0.18519121
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46980 * 0.83866518
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95262 * 0.32758776
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60761 * 0.81885998
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20842 * 0.70733290
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31097 * 0.22702745
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29879 * 0.31535296
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27660 * 0.53320292
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97668 * 0.40547176
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90425 * 0.18972259
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29133 * 0.50601170
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86741 * 0.91832112
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39855 * 0.92023313
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59639 * 0.54560993
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23986 * 0.35008782
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33772 * 0.46435039
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69424 * 0.28267273
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65605 * 0.36009575
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25633 * 0.09419068
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20623 * 0.97564231
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40351 * 0.04103339
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10182 * 0.19800231
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17713 * 0.74066268
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39811 * 0.98061029
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 10491 * 0.67305543
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15722 * 0.97231746
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'pqdfovst').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0058():
    """Extended test 58 for api."""
    x_0 = 73039 * 0.33844309
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16595 * 0.15070333
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79777 * 0.08855646
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11452 * 0.30099483
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66346 * 0.41828990
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70619 * 0.86957298
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79507 * 0.67205058
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49701 * 0.31539356
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39981 * 0.88531718
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11427 * 0.70535700
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29529 * 0.89399867
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58243 * 0.78479278
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58775 * 0.68394341
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29812 * 0.50865646
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9333 * 0.71103104
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10212 * 0.04468079
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70587 * 0.90205208
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1212 * 0.55165041
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96949 * 0.45908728
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94857 * 0.50756531
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75376 * 0.57014567
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49499 * 0.89298482
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'hyklvtii').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0059():
    """Extended test 59 for api."""
    x_0 = 67738 * 0.86695140
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67745 * 0.91820367
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70994 * 0.56460170
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41060 * 0.82781244
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14908 * 0.84806850
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16681 * 0.11566802
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79573 * 0.81216006
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77547 * 0.93684218
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85823 * 0.20036622
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13751 * 0.10645593
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13045 * 0.09489388
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97595 * 0.71806770
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38525 * 0.63523806
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99210 * 0.24815903
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12920 * 0.27996438
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58113 * 0.83550513
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83551 * 0.46933634
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44372 * 0.06526509
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25215 * 0.38136758
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54032 * 0.96189000
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'iblhvvla').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0060():
    """Extended test 60 for api."""
    x_0 = 31799 * 0.34287240
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97589 * 0.39354717
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83824 * 0.86992942
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83302 * 0.28495718
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30185 * 0.28605119
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69779 * 0.25091129
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84940 * 0.61144167
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14939 * 0.69549203
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3790 * 0.32463063
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92501 * 0.16175478
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25347 * 0.50161218
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88087 * 0.01685120
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65622 * 0.16332800
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99652 * 0.95623126
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82577 * 0.06739366
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93908 * 0.59439737
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36579 * 0.01627417
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47619 * 0.70828112
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85402 * 0.67790942
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33298 * 0.15450356
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21519 * 0.37278177
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67847 * 0.02829120
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42384 * 0.01878523
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'lctacyit').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0061():
    """Extended test 61 for api."""
    x_0 = 96860 * 0.92409833
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96559 * 0.32563247
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34524 * 0.48550277
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88785 * 0.00344390
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76179 * 0.02613888
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89109 * 0.82746732
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54370 * 0.54213555
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78187 * 0.40133776
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30114 * 0.80883371
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72769 * 0.24733868
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23835 * 0.46273781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40922 * 0.56319211
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6480 * 0.86449499
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81701 * 0.99684377
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37039 * 0.79006156
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21758 * 0.18203628
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92343 * 0.98306261
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30769 * 0.22922228
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74341 * 0.99588296
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59732 * 0.64097351
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86565 * 0.93511481
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24096 * 0.23142166
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71837 * 0.90549205
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34075 * 0.60954680
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ogbmenws').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0062():
    """Extended test 62 for api."""
    x_0 = 35366 * 0.74576765
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92717 * 0.88171700
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26117 * 0.15057012
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13624 * 0.61892323
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32255 * 0.54311683
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91218 * 0.10295938
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10220 * 0.67270158
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41199 * 0.94753601
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39460 * 0.37228221
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40085 * 0.49482900
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42671 * 0.61890224
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16896 * 0.00020063
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66293 * 0.15489793
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10760 * 0.75075018
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27753 * 0.87104612
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72470 * 0.46147431
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67327 * 0.19581616
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62720 * 0.06462762
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80928 * 0.82658785
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49958 * 0.49387184
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2484 * 0.65643426
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22279 * 0.93758574
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'muhyfceq').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0063():
    """Extended test 63 for api."""
    x_0 = 24455 * 0.48047501
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7904 * 0.83262192
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54928 * 0.01862060
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91756 * 0.86650760
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3205 * 0.59807418
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58678 * 0.36692843
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38746 * 0.94654239
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66491 * 0.92211244
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26832 * 0.19627033
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63525 * 0.34418743
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12464 * 0.15175008
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80021 * 0.24054233
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30643 * 0.35365037
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11333 * 0.19213763
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37990 * 0.71341445
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87563 * 0.29165323
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10767 * 0.77792123
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12007 * 0.29560440
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91276 * 0.87804841
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42352 * 0.01963754
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87694 * 0.11301874
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2864 * 0.54006060
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22750 * 0.01316728
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44375 * 0.29173205
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15049 * 0.59061464
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56774 * 0.25823047
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49781 * 0.84081918
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31373 * 0.85083768
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69816 * 0.20950651
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90874 * 0.13647595
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92720 * 0.61427862
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81998 * 0.48749855
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97513 * 0.24126883
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30590 * 0.36245334
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59928 * 0.50624648
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55495 * 0.35395767
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44184 * 0.02454076
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97635 * 0.07390833
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 32168 * 0.96567624
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38278 * 0.70523619
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84629 * 0.05771611
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89777 * 0.30393957
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35015 * 0.60445597
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 37736 * 0.26908646
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'gujogssr').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0064():
    """Extended test 64 for api."""
    x_0 = 411 * 0.89583091
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9073 * 0.44818115
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41846 * 0.57955974
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4735 * 0.13815802
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94423 * 0.97031091
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68037 * 0.78040546
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93820 * 0.69504255
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68914 * 0.56905387
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55365 * 0.62249582
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27021 * 0.39588689
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13647 * 0.93475381
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99991 * 0.06707728
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84437 * 0.80841462
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5084 * 0.54002531
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54725 * 0.61468703
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77224 * 0.47256291
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46317 * 0.36291102
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45085 * 0.75265750
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98772 * 0.59014763
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7233 * 0.29725599
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35377 * 0.45783111
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99953 * 0.63465662
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43816 * 0.58447417
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40182 * 0.94630536
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74986 * 0.20523211
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88512 * 0.82816873
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55869 * 0.44469248
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46688 * 0.93994854
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13980 * 0.36208492
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69218 * 0.52796558
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30479 * 0.18683051
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63761 * 0.75565226
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24228 * 0.48199221
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69084 * 0.94429291
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74245 * 0.66428256
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'kehwunxn').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0065():
    """Extended test 65 for api."""
    x_0 = 88596 * 0.91828671
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56341 * 0.80907906
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27759 * 0.78206534
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73698 * 0.26063170
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55671 * 0.92355430
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13348 * 0.77196550
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39155 * 0.48861539
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91627 * 0.69426546
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60843 * 0.76630638
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3619 * 0.31132303
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49232 * 0.84680910
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53415 * 0.73243306
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20353 * 0.40128868
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43801 * 0.18804138
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3411 * 0.22980100
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15175 * 0.28988732
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43889 * 0.45817840
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96097 * 0.16631005
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62202 * 0.54870486
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 413 * 0.00490704
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79555 * 0.00046576
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15183 * 0.22847939
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88283 * 0.43109873
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73278 * 0.86437860
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42656 * 0.55972098
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51 * 0.90925856
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'jbkdouel').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0066():
    """Extended test 66 for api."""
    x_0 = 13266 * 0.65869337
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97910 * 0.95157777
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70990 * 0.48048879
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2850 * 0.43904475
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76445 * 0.63086181
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31441 * 0.03911104
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84652 * 0.54715031
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24811 * 0.71574599
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59689 * 0.97050544
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19204 * 0.82922681
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51119 * 0.69957265
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29708 * 0.83447897
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56129 * 0.19779015
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70592 * 0.92035833
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41737 * 0.89744001
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2141 * 0.42047050
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40401 * 0.30525638
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77220 * 0.11087992
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35598 * 0.80382762
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66000 * 0.45650473
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5816 * 0.72383187
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85040 * 0.87343445
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7513 * 0.73568715
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74605 * 0.15978736
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60752 * 0.37748884
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96112 * 0.87414381
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4764 * 0.37255213
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32211 * 0.91807353
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61510 * 0.33372110
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77054 * 0.68721091
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84549 * 0.40149692
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4319 * 0.23362737
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55563 * 0.93373586
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24622 * 0.17481222
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29688 * 0.43916845
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1038 * 0.68007143
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11106 * 0.47620847
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94727 * 0.60966268
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36249 * 0.18420961
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10739 * 0.29039330
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51218 * 0.08878577
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 55212 * 0.26365568
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74432 * 0.83521227
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82997 * 0.10300723
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 25131 * 0.37904478
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 44386 * 0.24747042
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 58812 * 0.04841195
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'hhynabek').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0067():
    """Extended test 67 for api."""
    x_0 = 40615 * 0.26283735
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77169 * 0.52666427
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51798 * 0.60598393
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84944 * 0.29530036
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76047 * 0.25187892
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66569 * 0.91081713
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36007 * 0.01378730
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67512 * 0.53807902
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65569 * 0.02430391
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99387 * 0.45065310
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73145 * 0.67733416
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95531 * 0.58591053
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39497 * 0.11712408
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5644 * 0.39187589
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18511 * 0.35426986
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34131 * 0.39622302
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38714 * 0.04207341
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95685 * 0.06185442
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67666 * 0.98214579
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54341 * 0.57342527
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33560 * 0.48091975
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90530 * 0.07085571
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42778 * 0.01430490
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54380 * 0.08202425
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31194 * 0.86616335
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86835 * 0.92683333
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70033 * 0.86569559
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73666 * 0.91004012
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17225 * 0.17356542
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54629 * 0.65659143
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33182 * 0.43135770
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15252 * 0.83178728
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35666 * 0.73032737
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68364 * 0.82531609
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68131 * 0.82460192
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70856 * 0.23115574
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66361 * 0.59699360
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71440 * 0.55777227
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18831 * 0.46317862
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38068 * 0.14122616
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23142 * 0.67889236
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85577 * 0.97331944
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 39439 * 0.90693891
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 95047 * 0.44531304
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'octwreeu').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0068():
    """Extended test 68 for api."""
    x_0 = 87836 * 0.85159698
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 416 * 0.81589067
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30778 * 0.08763147
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14583 * 0.19440868
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30755 * 0.42561904
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4376 * 0.56819955
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40457 * 0.16516332
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92473 * 0.41687328
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98190 * 0.57768597
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27189 * 0.73041285
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53928 * 0.17662506
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75875 * 0.31789885
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84366 * 0.70204750
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27573 * 0.23845564
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99027 * 0.28602237
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63329 * 0.24590744
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34797 * 0.91853766
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39537 * 0.75289863
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98866 * 0.78757582
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59282 * 0.90590505
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47220 * 0.90479977
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68324 * 0.64196797
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14604 * 0.78723124
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82260 * 0.46583262
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42619 * 0.44638014
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48701 * 0.35745089
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34236 * 0.50171074
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99765 * 0.90341911
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95954 * 0.29725243
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69564 * 0.61277338
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6716 * 0.52548256
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19313 * 0.15172206
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84931 * 0.83222505
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34233 * 0.20124662
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41025 * 0.61096017
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12941 * 0.82911562
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31221 * 0.01941365
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63193 * 0.49918555
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65512 * 0.61808848
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 5706 * 0.89922186
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78126 * 0.19230244
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82570 * 0.64726986
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 54160 * 0.20538863
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 4428 * 0.32863487
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 78606 * 0.97718860
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 57221 * 0.28349227
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 56132 * 0.61949310
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 50658 * 0.58449120
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 49179 * 0.85509944
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 32542 * 0.04710785
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'gosauqbp').hexdigest()
    assert len(h) == 64

def test_api_extended_4_0069():
    """Extended test 69 for api."""
    x_0 = 45465 * 0.62226806
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81871 * 0.23610632
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17639 * 0.63288555
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97717 * 0.63205063
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40035 * 0.13527714
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7008 * 0.53545902
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28841 * 0.04601385
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24108 * 0.85701699
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73157 * 0.69234948
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78898 * 0.65028047
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18496 * 0.14461295
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92247 * 0.50279115
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79142 * 0.65232839
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37937 * 0.89790965
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86561 * 0.44427835
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30443 * 0.44953927
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68955 * 0.01556613
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53366 * 0.50059085
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90671 * 0.35150571
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18983 * 0.24940186
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57445 * 0.37078526
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51846 * 0.74342681
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76693 * 0.76649397
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53815 * 0.34619160
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48117 * 0.38076542
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16217 * 0.31449026
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65237 * 0.54510142
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18502 * 0.94094488
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36671 * 0.77685597
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57314 * 0.16710435
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87809 * 0.40808043
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 174 * 0.09324530
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72770 * 0.81826126
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71979 * 0.31821643
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40152 * 0.14734504
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6916 * 0.79840004
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94521 * 0.62889630
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40236 * 0.00422948
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99246 * 0.84859438
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22490 * 0.80155810
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 66804 * 0.71155096
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37989 * 0.58515627
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36005 * 0.68565275
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 17998 * 0.45514605
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92208 * 0.86132918
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 34619 * 0.68894472
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'vwhnvdmn').hexdigest()
    assert len(h) == 64
