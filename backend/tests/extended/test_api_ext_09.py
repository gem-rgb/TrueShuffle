"""Extended tests for api suite 9."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_api_extended_9_0000():
    """Extended test 0 for api."""
    x_0 = 79283 * 0.12553670
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79558 * 0.93510982
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37344 * 0.80650368
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30337 * 0.52575432
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38877 * 0.15260936
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39652 * 0.39285829
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71108 * 0.10845200
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78740 * 0.04084156
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87477 * 0.71256169
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36278 * 0.61922171
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19093 * 0.87707052
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39199 * 0.72803323
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11479 * 0.02832628
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69198 * 0.07681049
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76414 * 0.39864700
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66910 * 0.99416912
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35507 * 0.96779307
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20573 * 0.58939616
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17042 * 0.26875914
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49199 * 0.30730005
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92889 * 0.24960035
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92887 * 0.71763130
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40693 * 0.26366191
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7133 * 0.25972070
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12805 * 0.58803760
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17977 * 0.54071682
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58953 * 0.80756378
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72977 * 0.36424399
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79621 * 0.99799377
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80415 * 0.95745394
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7265 * 0.26388303
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77613 * 0.11939523
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73409 * 0.00273851
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86452 * 0.49066227
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18818 * 0.98417875
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82744 * 0.21660290
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14362 * 0.20280420
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'wjhcqzph').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0001():
    """Extended test 1 for api."""
    x_0 = 48680 * 0.56723046
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38770 * 0.61652036
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42354 * 0.95495940
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24990 * 0.45664145
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76211 * 0.05699516
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22315 * 0.82189099
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55595 * 0.31137475
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98890 * 0.53597588
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80157 * 0.06018160
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98847 * 0.33746978
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1088 * 0.79895477
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92281 * 0.03651748
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30450 * 0.92615953
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25901 * 0.92890735
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84045 * 0.30063329
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13266 * 0.79342207
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4053 * 0.81670319
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91920 * 0.87696851
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95260 * 0.43475082
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42366 * 0.88785601
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93648 * 0.88053496
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90825 * 0.58891735
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98944 * 0.46765262
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14509 * 0.97045617
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68100 * 0.00698772
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40714 * 0.53919057
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96505 * 0.83442836
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41589 * 0.42228987
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62605 * 0.05842324
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57943 * 0.98266370
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55088 * 0.03190905
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15960 * 0.62224690
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72207 * 0.49426637
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23554 * 0.35917176
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19680 * 0.10468135
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67834 * 0.26877092
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'tazfbvjq').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0002():
    """Extended test 2 for api."""
    x_0 = 51548 * 0.76832357
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2231 * 0.93508893
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70784 * 0.68369760
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75154 * 0.65995931
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52359 * 0.61993010
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74004 * 0.06965968
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21734 * 0.08406742
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31422 * 0.55247670
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52875 * 0.26278056
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97333 * 0.56476314
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13340 * 0.90485374
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61538 * 0.20216923
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91928 * 0.08734416
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4333 * 0.66406903
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5759 * 0.71157972
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8627 * 0.64265875
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87824 * 0.60946438
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36500 * 0.32094545
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57352 * 0.60293020
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77600 * 0.34118078
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75374 * 0.02893917
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1753 * 0.40220224
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79246 * 0.20239103
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81987 * 0.74859764
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5949 * 0.44591117
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25703 * 0.86982400
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35932 * 0.04073030
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78002 * 0.06700352
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59646 * 0.38757619
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43883 * 0.50102226
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59836 * 0.67142268
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67463 * 0.77608731
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7480 * 0.47931859
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76112 * 0.19114650
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67143 * 0.25037959
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5869 * 0.87034867
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45193 * 0.65663282
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97668 * 0.39464203
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26338 * 0.70829834
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92340 * 0.71335255
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74639 * 0.87598333
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 91574 * 0.52291721
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24441 * 0.04356890
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 33460 * 0.68454226
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 87830 * 0.68152582
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 49740 * 0.84824937
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 92767 * 0.83466518
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 19516 * 0.55839799
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 92286 * 0.55748973
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'aqhvtzqn').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0003():
    """Extended test 3 for api."""
    x_0 = 49367 * 0.91456627
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38732 * 0.21072637
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3227 * 0.81192473
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49008 * 0.61995608
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43524 * 0.72887612
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60214 * 0.35352386
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39765 * 0.82135998
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17688 * 0.19272813
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24067 * 0.71178142
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45283 * 0.55528332
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52032 * 0.80277234
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71787 * 0.12776705
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95529 * 0.21534003
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31133 * 0.73875327
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95200 * 0.99139382
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80037 * 0.85508744
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75776 * 0.84761014
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40738 * 0.19753292
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17131 * 0.07118757
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17458 * 0.18454378
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66798 * 0.05890675
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86145 * 0.09679495
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91398 * 0.04078652
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22869 * 0.03486075
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67587 * 0.58167098
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69068 * 0.65593768
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69529 * 0.30355776
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90131 * 0.80974823
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'xurheugk').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0004():
    """Extended test 4 for api."""
    x_0 = 72194 * 0.12596391
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76671 * 0.75340184
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37942 * 0.45225749
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7710 * 0.65031000
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56861 * 0.60942854
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64640 * 0.74160868
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54397 * 0.05370313
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59206 * 0.07229549
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51408 * 0.69688906
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43152 * 0.92028430
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91498 * 0.50767217
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59405 * 0.26697486
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81057 * 0.88243969
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74028 * 0.31520979
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92974 * 0.90706340
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19295 * 0.36016859
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55267 * 0.20041305
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56167 * 0.28641755
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38035 * 0.96159965
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20978 * 0.91263433
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90948 * 0.12215997
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43177 * 0.98691885
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34734 * 0.97710934
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84452 * 0.39032163
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2215 * 0.67870476
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28161 * 0.04110189
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26095 * 0.36437639
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9262 * 0.62626512
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2857 * 0.71554151
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74453 * 0.66574160
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86610 * 0.13114434
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93776 * 0.62216310
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52619 * 0.18336633
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68075 * 0.56485484
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36939 * 0.84762196
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51898 * 0.80101861
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58129 * 0.56416545
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'fjjtxtyg').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0005():
    """Extended test 5 for api."""
    x_0 = 83497 * 0.22063413
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57886 * 0.72726774
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83839 * 0.78225674
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15382 * 0.75841624
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33290 * 0.07188607
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91444 * 0.09805561
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17377 * 0.81443878
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72505 * 0.18564319
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97735 * 0.89184328
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61805 * 0.63894520
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34634 * 0.40248159
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2229 * 0.65989808
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45481 * 0.33652009
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52850 * 0.79104778
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38103 * 0.97756414
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58665 * 0.35090056
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20077 * 0.43919512
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70356 * 0.64572773
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20130 * 0.49659333
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76034 * 0.04208566
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34321 * 0.50530305
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35137 * 0.72299711
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70949 * 0.52689391
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23093 * 0.92014079
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50538 * 0.26270397
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15504 * 0.24472238
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76638 * 0.21715197
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11973 * 0.79806281
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25857 * 0.01978438
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52313 * 0.41503925
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9701 * 0.06677110
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31367 * 0.21871146
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70253 * 0.13457050
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67776 * 0.36142332
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8750 * 0.64706188
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32631 * 0.39309739
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80247 * 0.83501271
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39391 * 0.71338648
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86266 * 0.81574163
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75733 * 0.30601932
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'atcigqva').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0006():
    """Extended test 6 for api."""
    x_0 = 69624 * 0.32118069
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95829 * 0.40920063
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25987 * 0.71236719
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53331 * 0.55023436
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38568 * 0.75868210
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8012 * 0.91890659
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69371 * 0.26829493
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12278 * 0.37872119
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44657 * 0.54853022
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83574 * 0.73343904
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58051 * 0.07750818
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60782 * 0.05624054
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27883 * 0.38736328
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68707 * 0.57370846
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14577 * 0.83306343
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16722 * 0.12520596
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58427 * 0.85004668
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67573 * 0.75303936
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9675 * 0.62054382
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31956 * 0.92882069
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31238 * 0.00526738
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98982 * 0.79483523
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13205 * 0.90910501
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98189 * 0.97031943
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64805 * 0.90732817
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62018 * 0.05573672
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65269 * 0.61324091
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29811 * 0.27871193
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90657 * 0.83331423
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29885 * 0.27228884
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29166 * 0.99349306
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20352 * 0.53994259
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25007 * 0.55702981
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38136 * 0.01431694
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43909 * 0.57393785
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66102 * 0.47617152
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99023 * 0.63494417
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4241 * 0.21574180
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 3657 * 0.65400779
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95285 * 0.48348648
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 16652 * 0.43765025
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77090 * 0.92892286
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 39246 * 0.36581509
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75651 * 0.78081181
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 68518 * 0.15552381
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 22273 * 0.89822812
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 66974 * 0.79502026
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 2900 * 0.18552242
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'hltooltt').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0007():
    """Extended test 7 for api."""
    x_0 = 83309 * 0.92875018
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32481 * 0.36493673
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23562 * 0.15505666
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17208 * 0.62467273
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39702 * 0.05906460
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79255 * 0.64472996
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50284 * 0.48770484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42120 * 0.88048611
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29612 * 0.14414441
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37324 * 0.11193058
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53672 * 0.58732116
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30814 * 0.40033344
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47233 * 0.60174257
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22174 * 0.51382987
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62247 * 0.15366339
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23247 * 0.00960767
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84842 * 0.51653290
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45702 * 0.72602026
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11807 * 0.33265039
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61544 * 0.28843001
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10596 * 0.74124748
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47047 * 0.45302579
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23339 * 0.77912051
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18045 * 0.17007723
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52720 * 0.38886390
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31924 * 0.45722195
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52043 * 0.04610325
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'bpnhtzgz').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0008():
    """Extended test 8 for api."""
    x_0 = 40911 * 0.18174161
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34622 * 0.69827949
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4427 * 0.90601870
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32238 * 0.63532250
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79853 * 0.89644512
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17841 * 0.19995916
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89790 * 0.15264718
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46014 * 0.53954712
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2053 * 0.03300567
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38430 * 0.98526077
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83559 * 0.02475157
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9231 * 0.60904810
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26060 * 0.39791122
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76216 * 0.66901812
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96516 * 0.36036235
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33469 * 0.19708404
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3630 * 0.73962567
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37867 * 0.86965023
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66588 * 0.18221478
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61141 * 0.78899416
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12293 * 0.98922043
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49601 * 0.07376386
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36551 * 0.61137302
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2073 * 0.36469585
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24451 * 0.06959164
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31170 * 0.48350196
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74954 * 0.21013404
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7347 * 0.79831342
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39965 * 0.56798416
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97320 * 0.21044120
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65017 * 0.87681646
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81714 * 0.16218142
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14237 * 0.31652641
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22946 * 0.19996450
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9949 * 0.64880883
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78494 * 0.27152484
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56671 * 0.31301319
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88198 * 0.54984857
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21477 * 0.43053979
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21419 * 0.32281536
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60862 * 0.88663757
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50295 * 0.04626034
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 21788 * 0.95732582
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 31715 * 0.67923350
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'fkeunkqp').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0009():
    """Extended test 9 for api."""
    x_0 = 97327 * 0.20478895
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70375 * 0.30516421
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66920 * 0.67323583
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41637 * 0.14605247
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90952 * 0.32625680
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57472 * 0.41052506
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52686 * 0.79547642
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72258 * 0.04920980
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16509 * 0.75726601
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27344 * 0.92215668
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22237 * 0.30436319
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26595 * 0.22083956
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91874 * 0.01402473
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41412 * 0.64416265
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51915 * 0.10123742
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3172 * 0.92211617
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39381 * 0.61560891
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7759 * 0.83440973
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21736 * 0.43673432
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56959 * 0.95299465
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86596 * 0.19327306
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79616 * 0.88494729
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90211 * 0.58862963
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61912 * 0.75069487
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53582 * 0.90370049
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31831 * 0.28991130
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2102 * 0.10453071
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74886 * 0.86732846
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66857 * 0.06964213
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83282 * 0.93036786
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33811 * 0.72981076
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20896 * 0.86920143
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29251 * 0.25626345
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88689 * 0.00466785
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10914 * 0.78380834
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89463 * 0.33629771
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48387 * 0.66014905
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72441 * 0.97960675
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69268 * 0.64906859
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54132 * 0.21623330
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 9070 * 0.81553597
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 11488 * 0.23518720
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93954 * 0.28322089
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11127 * 0.51924223
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 84709 * 0.66027135
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 20217 * 0.11653913
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 96368 * 0.82842449
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'zjzwtcag').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0010():
    """Extended test 10 for api."""
    x_0 = 75909 * 0.15851868
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38828 * 0.11117180
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42718 * 0.66836624
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68071 * 0.94353139
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63084 * 0.68956132
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38004 * 0.30398605
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57873 * 0.55150844
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23877 * 0.70373345
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34584 * 0.38103003
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49550 * 0.93707895
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71396 * 0.84875815
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11053 * 0.88028503
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10323 * 0.76472941
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85579 * 0.39307232
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98821 * 0.60770012
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60772 * 0.94111190
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37072 * 0.84999522
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24048 * 0.89533257
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70371 * 0.36567233
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47565 * 0.67677024
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46289 * 0.83602686
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26570 * 0.55768338
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98380 * 0.84313093
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26616 * 0.25421812
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52275 * 0.76960205
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3065 * 0.70562017
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53126 * 0.60869425
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29057 * 0.11228680
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92713 * 0.84826790
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24632 * 0.56757371
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69978 * 0.17335549
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22309 * 0.93763764
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57626 * 0.11005153
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16111 * 0.91425242
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95337 * 0.18078554
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95026 * 0.17805856
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94196 * 0.44730184
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85511 * 0.93233193
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57599 * 0.15189298
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55084 * 0.46028704
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47980 * 0.99099987
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13173 * 0.77530772
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 38245 * 0.30464574
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 64853 * 0.49760347
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 75532 * 0.18092337
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 87651 * 0.83492557
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 61099 * 0.31001563
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 27635 * 0.19968833
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 50160 * 0.93881142
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 15830 * 0.42347847
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'umjodppw').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0011():
    """Extended test 11 for api."""
    x_0 = 92106 * 0.09463789
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1668 * 0.71541324
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66422 * 0.45679661
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63176 * 0.65645715
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87762 * 0.38819312
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70756 * 0.79434024
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74046 * 0.10261525
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84521 * 0.30554836
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58866 * 0.77807360
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1697 * 0.87729635
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47309 * 0.00532912
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23708 * 0.10780711
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88199 * 0.46282913
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22515 * 0.27370636
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83508 * 0.19463813
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32043 * 0.60656903
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97103 * 0.22135413
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84275 * 0.42814347
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3255 * 0.43397226
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85460 * 0.73756044
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45184 * 0.97677783
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20106 * 0.78471751
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86640 * 0.81891784
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40251 * 0.58342057
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34685 * 0.36533496
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68257 * 0.20613491
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73221 * 0.07262539
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79323 * 0.11324635
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63977 * 0.23826045
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78586 * 0.44100266
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2158 * 0.58026672
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39527 * 0.75382896
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86844 * 0.79827949
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67748 * 0.98820192
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6879 * 0.75428473
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99800 * 0.29819108
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72401 * 0.69426332
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28251 * 0.90728621
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55657 * 0.58146416
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32984 * 0.57582684
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19821 * 0.21776591
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14472 * 0.70686023
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96236 * 0.61116285
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 9155 * 0.84047883
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59104 * 0.20011111
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 80040 * 0.26906323
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 2143 * 0.15453280
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'npnoxrdk').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0012():
    """Extended test 12 for api."""
    x_0 = 43763 * 0.57081273
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39097 * 0.26160766
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89872 * 0.01105745
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16770 * 0.62023358
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53633 * 0.03616229
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15551 * 0.78360920
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7791 * 0.57848553
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23383 * 0.50771401
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64892 * 0.21729456
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42369 * 0.39768347
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92809 * 0.17736664
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66147 * 0.85018802
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47679 * 0.27239993
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52229 * 0.68692787
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74904 * 0.36843750
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27553 * 0.11798016
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66845 * 0.66043198
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66751 * 0.72445050
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38602 * 0.87734784
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94331 * 0.42279721
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13028 * 0.61017893
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72602 * 0.05023037
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2978 * 0.71140553
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ulrexxzs').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0013():
    """Extended test 13 for api."""
    x_0 = 64921 * 0.17538286
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53427 * 0.56267619
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20938 * 0.47630668
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72776 * 0.52680594
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31373 * 0.15940123
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29749 * 0.21685191
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5806 * 0.36142041
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63496 * 0.50151771
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18821 * 0.59102550
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1485 * 0.03247733
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59456 * 0.91620072
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60778 * 0.96717791
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 876 * 0.55731865
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70328 * 0.26644450
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45783 * 0.80092342
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76146 * 0.05938202
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41442 * 0.12133036
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29511 * 0.43449914
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79889 * 0.18959669
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86690 * 0.11121019
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37060 * 0.50610665
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5787 * 0.43727870
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71706 * 0.14676293
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21289 * 0.29366948
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47610 * 0.53505723
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16400 * 0.04445381
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47203 * 0.72266059
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75469 * 0.46397676
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37060 * 0.62932158
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47949 * 0.35321485
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50828 * 0.69124259
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5499 * 0.68908277
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43116 * 0.92678466
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9886 * 0.80583453
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89446 * 0.03992120
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37562 * 0.24337902
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15212 * 0.44528493
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19071 * 0.99284156
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66858 * 0.18080488
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16268 * 0.93594168
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12774 * 0.77210723
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22991 * 0.72123518
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 56972 * 0.69961083
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 76975 * 0.17747430
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'onlykxff').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0014():
    """Extended test 14 for api."""
    x_0 = 21344 * 0.87489220
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58458 * 0.81047962
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39345 * 0.92283472
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46201 * 0.33126717
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39138 * 0.49455145
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93086 * 0.16329489
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3611 * 0.79106175
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21747 * 0.52173648
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1581 * 0.41886056
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9894 * 0.52121615
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74987 * 0.95962360
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30277 * 0.46896180
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87603 * 0.89608819
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35022 * 0.16017274
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64355 * 0.81459205
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11773 * 0.95376185
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35269 * 0.44603347
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68092 * 0.52339558
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64651 * 0.88390672
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11125 * 0.25210594
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9304 * 0.55911221
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10201 * 0.86928607
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41532 * 0.04152211
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78538 * 0.48471647
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67558 * 0.96868856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5742 * 0.04411788
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4625 * 0.40643742
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49644 * 0.30713852
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27756 * 0.28244833
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92163 * 0.33252374
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91972 * 0.52000167
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19279 * 0.62171886
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54458 * 0.75306756
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78204 * 0.20061688
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60433 * 0.05511191
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94862 * 0.58986125
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85583 * 0.54835344
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92884 * 0.65794834
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39093 * 0.76423067
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85585 * 0.81681087
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 59356 * 0.04780455
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 23088 * 0.52932385
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75992 * 0.30585917
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36822 * 0.15653933
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 32164 * 0.99268674
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 3435 * 0.60935222
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 80208 * 0.22900600
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 6167 * 0.95786222
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 37186 * 0.06545661
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'xwzjadyb').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0015():
    """Extended test 15 for api."""
    x_0 = 64087 * 0.82679768
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92767 * 0.46812320
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36986 * 0.22084056
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97202 * 0.35037254
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11097 * 0.44266302
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97336 * 0.13248618
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78987 * 0.33348310
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21511 * 0.34626439
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92592 * 0.16919764
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5300 * 0.72428600
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95591 * 0.91757635
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89483 * 0.56460243
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36047 * 0.05733947
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6850 * 0.99156830
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52543 * 0.77060495
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95129 * 0.25462629
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74953 * 0.04933704
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27211 * 0.23489902
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18232 * 0.55307974
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68499 * 0.75852294
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97197 * 0.69302963
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99332 * 0.80630502
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'pqksatnm').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0016():
    """Extended test 16 for api."""
    x_0 = 39401 * 0.40674922
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96359 * 0.31772502
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63323 * 0.65299461
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22320 * 0.91911991
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85046 * 0.82902877
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20233 * 0.03962016
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91851 * 0.25866483
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83426 * 0.43012085
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81515 * 0.63988524
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87958 * 0.51466385
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57951 * 0.20455879
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53409 * 0.94503010
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76160 * 0.93851650
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96257 * 0.88961468
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96816 * 0.63003972
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56213 * 0.52560763
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50530 * 0.23731819
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48976 * 0.00077732
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43577 * 0.19739703
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49998 * 0.65318200
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89468 * 0.74825266
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57044 * 0.13623173
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56477 * 0.25273675
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12457 * 0.41620071
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99016 * 0.72733083
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79126 * 0.49267571
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77975 * 0.90041455
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67331 * 0.03240281
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36888 * 0.48174323
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9505 * 0.60340635
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63183 * 0.77296706
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'fbkcwhqj').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0017():
    """Extended test 17 for api."""
    x_0 = 34112 * 0.88506620
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48794 * 0.28199819
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73020 * 0.03012808
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24293 * 0.03978714
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44177 * 0.82438145
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76559 * 0.93185158
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77898 * 0.60516868
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80541 * 0.13588796
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96102 * 0.59038818
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38921 * 0.05662560
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23038 * 0.06041099
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 231 * 0.68680400
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17994 * 0.08435400
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91092 * 0.34943600
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5314 * 0.04339654
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8772 * 0.16785199
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33075 * 0.41373523
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50586 * 0.89777645
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2971 * 0.08338097
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89720 * 0.98161122
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30366 * 0.72091602
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74964 * 0.11657656
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5642 * 0.88764351
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47045 * 0.70346493
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49358 * 0.10427798
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13976 * 0.64918815
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59703 * 0.09762708
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1521 * 0.94084657
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52879 * 0.15325178
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35643 * 0.15724647
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87764 * 0.92183418
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95900 * 0.81853206
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97205 * 0.36301042
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84935 * 0.06587823
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12213 * 0.76010204
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25537 * 0.28158302
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39582 * 0.79270104
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74985 * 0.20816626
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51609 * 0.97322344
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51167 * 0.46398393
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19954 * 0.83669348
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3021 * 0.81355382
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ubysfjfn').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0018():
    """Extended test 18 for api."""
    x_0 = 27055 * 0.64952404
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15986 * 0.01955649
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29682 * 0.77882588
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39976 * 0.14398541
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82324 * 0.46849304
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29999 * 0.58006389
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68505 * 0.02882803
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5689 * 0.80002764
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61037 * 0.94893674
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30615 * 0.20124045
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6211 * 0.42261446
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76193 * 0.35732319
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20805 * 0.59790385
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37764 * 0.93529965
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14293 * 0.80647108
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95907 * 0.42536931
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81095 * 0.36925029
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87697 * 0.65369644
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38131 * 0.49751050
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6958 * 0.41090090
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61286 * 0.46969269
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2057 * 0.26725231
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52977 * 0.74156570
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36822 * 0.16466298
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23367 * 0.59637916
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16966 * 0.16051048
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46979 * 0.18649718
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71282 * 0.51848645
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55937 * 0.45012685
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71702 * 0.36177839
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8179 * 0.22934456
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23614 * 0.47041583
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60595 * 0.99232781
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55115 * 0.87037758
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48168 * 0.11582765
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'bvctjuvw').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0019():
    """Extended test 19 for api."""
    x_0 = 17112 * 0.25294093
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43416 * 0.61043403
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25995 * 0.11131635
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53911 * 0.32076028
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27001 * 0.02047877
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85678 * 0.08327977
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25172 * 0.20769363
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86954 * 0.99028020
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35204 * 0.36099291
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56423 * 0.66381555
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15361 * 0.60692799
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23254 * 0.14644651
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51898 * 0.91312067
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74072 * 0.00573772
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4989 * 0.54490786
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41388 * 0.39130552
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27381 * 0.24264573
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5721 * 0.79176349
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85488 * 0.98175795
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18637 * 0.91048311
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29090 * 0.73539584
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31839 * 0.87705877
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85623 * 0.66490913
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95376 * 0.14253677
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85004 * 0.84549454
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14275 * 0.43622600
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60626 * 0.00715390
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93609 * 0.95210409
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11152 * 0.70683523
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69721 * 0.05503264
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87140 * 0.18301777
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60498 * 0.96629736
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59436 * 0.68642631
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73528 * 0.42023440
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8089 * 0.01546973
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21578 * 0.78038334
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31312 * 0.18675762
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92555 * 0.06882494
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51565 * 0.21748298
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62059 * 0.35493312
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'fthbzaye').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0020():
    """Extended test 20 for api."""
    x_0 = 39560 * 0.43193968
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98071 * 0.89539667
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1847 * 0.92266022
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42251 * 0.36297645
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4235 * 0.09376092
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44498 * 0.29569316
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14744 * 0.49605961
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94198 * 0.10712057
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81533 * 0.49183601
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78789 * 0.02955546
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61763 * 0.73059184
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42385 * 0.51088706
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81247 * 0.54802535
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50307 * 0.56234825
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52297 * 0.83661665
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87314 * 0.99029184
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5150 * 0.38180687
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84525 * 0.67309751
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65926 * 0.41597647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88979 * 0.35652479
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94210 * 0.41937363
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77664 * 0.82653818
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16027 * 0.39943596
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41308 * 0.89932519
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33721 * 0.35795053
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78933 * 0.09632769
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58295 * 0.09324738
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68911 * 0.39915203
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1540 * 0.88413287
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'nnivzbfg').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0021():
    """Extended test 21 for api."""
    x_0 = 18360 * 0.89176095
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99612 * 0.32411243
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92465 * 0.36051425
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62948 * 0.75511955
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42604 * 0.13690330
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17270 * 0.44251982
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10294 * 0.33100597
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7488 * 0.51303425
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87895 * 0.00795952
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85596 * 0.98016875
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91425 * 0.33793977
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39875 * 0.43369541
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84018 * 0.00362211
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68411 * 0.98890279
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71523 * 0.73231909
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 243 * 0.58959269
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90247 * 0.90807807
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6305 * 0.45904016
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72045 * 0.58936913
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42751 * 0.85963581
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49106 * 0.79602132
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13784 * 0.71305977
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94806 * 0.40087217
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21506 * 0.28388590
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 517 * 0.15038104
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83252 * 0.38415640
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51541 * 0.55955875
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34480 * 0.16568443
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36541 * 0.34861042
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65052 * 0.09916851
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4094 * 0.52629858
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96402 * 0.17505386
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84113 * 0.51240735
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60350 * 0.74741408
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32693 * 0.05787503
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14870 * 0.59038047
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'bnunomep').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0022():
    """Extended test 22 for api."""
    x_0 = 97259 * 0.10360209
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56663 * 0.72643535
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98020 * 0.14067381
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13589 * 0.26444133
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31453 * 0.92499575
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95622 * 0.61107727
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31346 * 0.58357715
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33530 * 0.66599478
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64676 * 0.40016877
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41635 * 0.50678397
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69582 * 0.65045646
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46037 * 0.37554691
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66167 * 0.53922197
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28177 * 0.44688146
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93112 * 0.03724433
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50434 * 0.67070120
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51685 * 0.73764202
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95436 * 0.61665860
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38716 * 0.46154277
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55797 * 0.77967548
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45269 * 0.64000270
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46766 * 0.62410026
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23904 * 0.63935032
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87985 * 0.49576624
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57340 * 0.15287648
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31403 * 0.28612734
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12463 * 0.97163224
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29283 * 0.08686405
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64618 * 0.45224195
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79639 * 0.19505244
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47995 * 0.42301252
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18095 * 0.08457457
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68121 * 0.38530156
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'cfavlbmp').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0023():
    """Extended test 23 for api."""
    x_0 = 36677 * 0.21806247
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36600 * 0.49710608
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46284 * 0.11063207
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51576 * 0.99499188
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56774 * 0.72961891
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61249 * 0.56301170
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51606 * 0.91219450
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28891 * 0.63069091
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5909 * 0.01861018
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99981 * 0.15072623
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41080 * 0.78040834
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56199 * 0.16311659
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99282 * 0.87058396
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6172 * 0.13224500
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85657 * 0.49391093
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98983 * 0.17068382
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7084 * 0.65333993
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53047 * 0.39864322
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82861 * 0.29445335
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94683 * 0.44329002
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41934 * 0.24956753
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31108 * 0.87391119
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'hazkicry').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0024():
    """Extended test 24 for api."""
    x_0 = 18282 * 0.03254351
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70611 * 0.87717832
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62540 * 0.02608592
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99169 * 0.14485340
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48514 * 0.18547805
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42609 * 0.33842984
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14586 * 0.67055780
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9485 * 0.30043333
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82296 * 0.06549386
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33917 * 0.48656327
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29747 * 0.15398057
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79149 * 0.07922189
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62522 * 0.91214123
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69805 * 0.91658596
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81927 * 0.64605355
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48799 * 0.20438153
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25177 * 0.79661001
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6365 * 0.45447112
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11515 * 0.55928970
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 960 * 0.12220199
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58814 * 0.89966211
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93024 * 0.92365579
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3675 * 0.77831894
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12646 * 0.88365862
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99221 * 0.78899816
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8179 * 0.30460218
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61063 * 0.98573442
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27813 * 0.93133286
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22760 * 0.31515172
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29086 * 0.62748446
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28422 * 0.51850344
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17330 * 0.53188701
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68860 * 0.33161012
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72612 * 0.86185839
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73063 * 0.96250184
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34714 * 0.83196461
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22184 * 0.59190885
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2978 * 0.40449441
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80050 * 0.89961050
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23556 * 0.70169206
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19007 * 0.72095318
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72734 * 0.50643475
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57433 * 0.30340927
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97412 * 0.64915359
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 24212 * 0.75631077
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 39488 * 0.99353494
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'bmfkkuvu').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0025():
    """Extended test 25 for api."""
    x_0 = 6755 * 0.08744687
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33561 * 0.92533776
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91880 * 0.85818092
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78810 * 0.84539754
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57169 * 0.28476978
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49662 * 0.36192191
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13798 * 0.27965175
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49540 * 0.08166324
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13686 * 0.60307230
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61271 * 0.62374676
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74317 * 0.06661759
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97866 * 0.96948914
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63776 * 0.30203661
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36189 * 0.97212041
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92470 * 0.03320317
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36142 * 0.59822815
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57002 * 0.14240324
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75885 * 0.31332893
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17419 * 0.82407817
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82428 * 0.82964932
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ovixjqvv').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0026():
    """Extended test 26 for api."""
    x_0 = 61239 * 0.52800769
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83127 * 0.49930718
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95389 * 0.29732305
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95002 * 0.39237508
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18512 * 0.84594681
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53494 * 0.20713169
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19690 * 0.91000473
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94768 * 0.74495602
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12012 * 0.25350274
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65621 * 0.24138909
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30739 * 0.20116509
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74894 * 0.91061391
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70642 * 0.91626642
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28554 * 0.49505506
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15805 * 0.86091924
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38025 * 0.08717205
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24064 * 0.70562800
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31089 * 0.48362361
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16717 * 0.32658652
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34564 * 0.62761083
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3427 * 0.84587886
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7661 * 0.81265537
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56627 * 0.38095742
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29512 * 0.07870759
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74039 * 0.46484513
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38292 * 0.36550912
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73692 * 0.75464039
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51500 * 0.51612272
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57177 * 0.71685524
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18469 * 0.54205323
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39113 * 0.29224201
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16830 * 0.93489982
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98592 * 0.28898277
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'brabgyiz').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0027():
    """Extended test 27 for api."""
    x_0 = 36050 * 0.00368551
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30812 * 0.62607494
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9622 * 0.94427335
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40328 * 0.62914547
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27634 * 0.24498125
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17633 * 0.38975917
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67724 * 0.59838073
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32807 * 0.60127535
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90686 * 0.43171811
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55508 * 0.99424072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63313 * 0.41420691
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79623 * 0.55331663
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42991 * 0.89140588
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41855 * 0.37424297
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91667 * 0.58608019
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32371 * 0.94855090
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86544 * 0.99874545
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21132 * 0.28485291
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1422 * 0.70118299
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26233 * 0.95955385
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74163 * 0.99635382
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64207 * 0.44029994
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71674 * 0.55860237
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13669 * 0.73916938
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7182 * 0.51887407
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26022 * 0.25499172
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6874 * 0.60426730
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89421 * 0.54071411
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49658 * 0.80074829
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54531 * 0.95986182
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54442 * 0.06335833
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22634 * 0.94118765
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32494 * 0.08134097
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41742 * 0.65601190
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23388 * 0.07303697
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8073 * 0.88172070
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47672 * 0.79541235
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'zovehtqv').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0028():
    """Extended test 28 for api."""
    x_0 = 24351 * 0.72225355
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36379 * 0.52743552
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29663 * 0.16920660
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55663 * 0.93827908
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96107 * 0.61301761
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46130 * 0.80994955
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48537 * 0.62317938
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64563 * 0.43166975
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28027 * 0.20400043
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35871 * 0.37081568
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67022 * 0.33090621
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69977 * 0.05208071
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 510 * 0.45627755
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 381 * 0.83280434
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63382 * 0.53361606
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14728 * 0.25533117
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85913 * 0.45618384
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36985 * 0.52862474
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37067 * 0.28835917
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22892 * 0.94205403
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29762 * 0.53089434
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13465 * 0.35661733
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1529 * 0.82029478
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30732 * 0.51645393
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69036 * 0.07853923
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10525 * 0.21044193
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72288 * 0.25737933
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76390 * 0.53706252
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68574 * 0.33927638
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2556 * 0.92190658
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2219 * 0.53383823
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41126 * 0.88620189
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62666 * 0.83296387
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66311 * 0.40169091
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3504 * 0.52925604
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'irfwvfyj').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0029():
    """Extended test 29 for api."""
    x_0 = 7808 * 0.88027618
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1530 * 0.30252655
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87306 * 0.51520571
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92674 * 0.96478893
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97493 * 0.82140537
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7101 * 0.91418198
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93944 * 0.77591165
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62621 * 0.60468514
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36934 * 0.21058735
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59677 * 0.30865311
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66451 * 0.91213936
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74221 * 0.28244352
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68700 * 0.47647801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40049 * 0.17693841
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30422 * 0.69571691
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50698 * 0.91018783
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44088 * 0.28785659
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93178 * 0.88229509
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61347 * 0.18976961
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52565 * 0.71757525
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27760 * 0.62046785
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7225 * 0.84921631
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37995 * 0.88183239
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73383 * 0.94654692
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18095 * 0.55565780
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46820 * 0.08084544
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27287 * 0.92732538
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26131 * 0.86240164
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36806 * 0.66253891
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26292 * 0.45093570
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88778 * 0.33542045
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39476 * 0.92171273
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24529 * 0.88643500
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37777 * 0.76442215
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33128 * 0.87077467
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11676 * 0.74056191
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79915 * 0.46831679
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6114 * 0.09025365
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82331 * 0.88152724
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55759 * 0.12842894
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 39436 * 0.11144995
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70126 * 0.45904978
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93332 * 0.00136021
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'xzrrdfzw').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0030():
    """Extended test 30 for api."""
    x_0 = 10036 * 0.52207481
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52689 * 0.81032194
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94586 * 0.27640386
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50754 * 0.10055956
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3595 * 0.24898990
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92600 * 0.11160590
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74893 * 0.00990134
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81727 * 0.47131130
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76523 * 0.59729695
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18552 * 0.48634469
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25517 * 0.37335220
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1154 * 0.40488253
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74517 * 0.68194264
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97720 * 0.42842923
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49134 * 0.51279805
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17773 * 0.74434813
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20266 * 0.86436825
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24791 * 0.70684500
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72770 * 0.00316636
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25991 * 0.62402671
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8571 * 0.84143041
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61745 * 0.53036752
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96922 * 0.70946777
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29600 * 0.90401220
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83458 * 0.74359836
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9048 * 0.09293774
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87813 * 0.28475660
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84960 * 0.71795608
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19785 * 0.19601090
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13870 * 0.71554384
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 953 * 0.15307562
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25071 * 0.83172252
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38354 * 0.58857972
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41104 * 0.30886806
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91510 * 0.48373344
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71497 * 0.56603941
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86104 * 0.57222042
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5975 * 0.91443925
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74039 * 0.50372118
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94265 * 0.88944597
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27796 * 0.38248815
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26226 * 0.94821037
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 87349 * 0.30952536
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 6526 * 0.46078255
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 52992 * 0.51961187
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 78498 * 0.83242812
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 75808 * 0.52265549
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 24921 * 0.32652439
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 80428 * 0.01163143
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'vkzqnatu').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0031():
    """Extended test 31 for api."""
    x_0 = 92590 * 0.66611389
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61569 * 0.61570200
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90953 * 0.70419241
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41162 * 0.48210440
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1895 * 0.30873606
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30700 * 0.53465138
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73586 * 0.62963161
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58209 * 0.49009922
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37040 * 0.39214977
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77371 * 0.59626550
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77308 * 0.48182573
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72231 * 0.62102461
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57676 * 0.62470548
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8118 * 0.27298287
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59326 * 0.57538467
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10858 * 0.13885547
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69127 * 0.82473758
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81823 * 0.23077934
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34318 * 0.01175644
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61072 * 0.71602920
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25947 * 0.84273306
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64528 * 0.26651234
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90931 * 0.39129290
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98780 * 0.45477999
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61271 * 0.60037105
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67874 * 0.51993439
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40873 * 0.07204336
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25806 * 0.69773386
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34961 * 0.93335953
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46869 * 0.24106678
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1147 * 0.32533320
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29973 * 0.70882171
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61699 * 0.47836475
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91229 * 0.35080178
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88495 * 0.94383042
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44521 * 0.22262223
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30899 * 0.43477215
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'hqijhppn').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0032():
    """Extended test 32 for api."""
    x_0 = 84531 * 0.85910719
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91227 * 0.29058175
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64168 * 0.39289500
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65249 * 0.28031057
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33776 * 0.71396425
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96055 * 0.41478991
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8087 * 0.87423385
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19144 * 0.59962149
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43920 * 0.69545378
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53410 * 0.55328321
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69502 * 0.99919559
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85633 * 0.01764711
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85470 * 0.44840660
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84749 * 0.77927936
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40750 * 0.08885939
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44463 * 0.71127698
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95259 * 0.40916346
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71109 * 0.82577021
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23218 * 0.95181109
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47898 * 0.78389127
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53869 * 0.45976810
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43867 * 0.16121956
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17875 * 0.61401853
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37397 * 0.53125044
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82686 * 0.05796858
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70161 * 0.70889067
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89250 * 0.63950134
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98566 * 0.11346169
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20227 * 0.52956190
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39676 * 0.50594277
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51278 * 0.06041324
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99470 * 0.97149494
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 815 * 0.29824339
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79005 * 0.00065733
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95584 * 0.90171271
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98695 * 0.00824565
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31046 * 0.29900206
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94496 * 0.18183556
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18847 * 0.00923803
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74204 * 0.65845543
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'xphofauu').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0033():
    """Extended test 33 for api."""
    x_0 = 50375 * 0.03602666
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6389 * 0.58781652
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14626 * 0.70177625
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91091 * 0.08053895
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20484 * 0.09433069
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84870 * 0.23460061
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74610 * 0.88470179
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25548 * 0.43938504
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64633 * 0.98400104
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70370 * 0.69756621
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58594 * 0.87892850
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51516 * 0.63471031
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55612 * 0.28577940
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82312 * 0.06099903
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92525 * 0.04069933
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74115 * 0.21326515
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98085 * 0.72512582
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 410 * 0.97914467
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60589 * 0.27701452
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80077 * 0.36481701
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25105 * 0.40739076
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35447 * 0.61314690
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85681 * 0.10996052
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30972 * 0.33319600
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37646 * 0.40136888
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85471 * 0.75054987
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61997 * 0.42258662
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22342 * 0.38857504
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57448 * 0.51636362
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99472 * 0.70213752
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85404 * 0.47064655
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58278 * 0.97830089
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8345 * 0.10940307
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24367 * 0.61278246
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'fpwrvrhx').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0034():
    """Extended test 34 for api."""
    x_0 = 69258 * 0.34041858
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53062 * 0.38732305
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2058 * 0.43782155
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89436 * 0.43317283
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67560 * 0.31105956
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47856 * 0.37728237
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85385 * 0.37937692
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68897 * 0.38143350
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28525 * 0.38608651
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10104 * 0.39830348
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59406 * 0.55381429
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40906 * 0.75357310
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69784 * 0.68678466
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60289 * 0.24092420
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35545 * 0.02398502
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2505 * 0.08153815
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48008 * 0.64632719
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43383 * 0.15761580
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15201 * 0.06325332
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62929 * 0.09262719
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92741 * 0.72322701
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98739 * 0.57550587
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74324 * 0.16299139
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79903 * 0.34050682
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11521 * 0.21558804
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11723 * 0.69946653
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84755 * 0.55639775
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44533 * 0.94570000
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36597 * 0.12503317
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58384 * 0.43706891
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52372 * 0.81782181
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74497 * 0.74638181
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39026 * 0.57794480
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'zfmdakbe').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0035():
    """Extended test 35 for api."""
    x_0 = 2129 * 0.52182656
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20982 * 0.99322410
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52416 * 0.00932389
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30663 * 0.97780378
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7138 * 0.56500484
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3544 * 0.70642886
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77401 * 0.58198510
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86991 * 0.44150520
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8053 * 0.27559947
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91551 * 0.21733869
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70975 * 0.27397717
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50342 * 0.51470287
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19363 * 0.93881008
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 801 * 0.82486646
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12043 * 0.48399672
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92303 * 0.08367558
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63755 * 0.89882262
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63945 * 0.35830513
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56929 * 0.21291401
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73277 * 0.61967748
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30513 * 0.91329049
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12262 * 0.39719138
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71851 * 0.08394642
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67713 * 0.36378122
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16999 * 0.85623893
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73385 * 0.03125894
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55023 * 0.82088795
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9015 * 0.79454220
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91528 * 0.67954760
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8890 * 0.81846705
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47141 * 0.67906031
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9656 * 0.93609466
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19910 * 0.04603701
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65372 * 0.38808238
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8651 * 0.07779990
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15334 * 0.76369259
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75295 * 0.81556744
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 37793 * 0.63810128
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49294 * 0.14943575
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80009 * 0.05695827
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ybjvkzhs').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0036():
    """Extended test 36 for api."""
    x_0 = 53929 * 0.33329534
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41753 * 0.99958656
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56098 * 0.58331362
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80101 * 0.33291586
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32514 * 0.30800984
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81315 * 0.49811346
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72916 * 0.33078986
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47611 * 0.47650651
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71240 * 0.55444586
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78117 * 0.11030406
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82524 * 0.38032849
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34377 * 0.51448718
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27878 * 0.38489205
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13211 * 0.14879740
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47063 * 0.78022587
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47526 * 0.29921046
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49251 * 0.74388635
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79546 * 0.87606203
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94288 * 0.31143689
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76493 * 0.05036543
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46566 * 0.22942279
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61907 * 0.66917019
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'mqhgfwjr').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0037():
    """Extended test 37 for api."""
    x_0 = 63343 * 0.07759007
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3781 * 0.43377131
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97552 * 0.32399017
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69239 * 0.68035034
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72714 * 0.01162605
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8048 * 0.83118461
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50957 * 0.65778007
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76468 * 0.75489250
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29181 * 0.23362521
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84030 * 0.29315071
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36493 * 0.09926599
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99713 * 0.96104047
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36298 * 0.59913951
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36590 * 0.46084684
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81640 * 0.30324332
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84580 * 0.23370417
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51898 * 0.40313727
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88171 * 0.58909204
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48705 * 0.58655187
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67507 * 0.62533875
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71797 * 0.33270842
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95606 * 0.21420750
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68619 * 0.26243620
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6948 * 0.24057032
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58227 * 0.32873370
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ycbylzmm').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0038():
    """Extended test 38 for api."""
    x_0 = 81379 * 0.53445728
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5768 * 0.56504384
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34827 * 0.50755508
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87690 * 0.41355455
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87441 * 0.72762815
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63846 * 0.39589961
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52998 * 0.43586859
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35408 * 0.29970783
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12121 * 0.77623598
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88412 * 0.45751317
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39269 * 0.08006424
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65664 * 0.93100194
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10755 * 0.49185954
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66921 * 0.70843746
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58668 * 0.00039745
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88718 * 0.26392034
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66996 * 0.98669255
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44132 * 0.00979813
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2729 * 0.24622050
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50240 * 0.22914982
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89545 * 0.57024681
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10966 * 0.16714356
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37204 * 0.58803415
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7316 * 0.72731531
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47955 * 0.40071913
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14981 * 0.06976238
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15985 * 0.61290550
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84557 * 0.74155562
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85125 * 0.82161290
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58479 * 0.41871308
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66648 * 0.31966469
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54105 * 0.79345733
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32378 * 0.61053147
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15088 * 0.50966185
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71263 * 0.30401883
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65557 * 0.49356152
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43588 * 0.28095313
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'kzgpyqmx').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0039():
    """Extended test 39 for api."""
    x_0 = 26093 * 0.15737007
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71818 * 0.79039481
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90110 * 0.42577957
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 599 * 0.80775257
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36518 * 0.24312953
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61192 * 0.80104040
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75848 * 0.56290436
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51476 * 0.39527762
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41027 * 0.20006366
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82615 * 0.47815729
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88042 * 0.10416870
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7149 * 0.15233409
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11012 * 0.80671064
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18072 * 0.65167201
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62004 * 0.67490483
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46327 * 0.00771628
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 507 * 0.35141055
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64843 * 0.22965997
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98761 * 0.69588985
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97343 * 0.20332856
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59666 * 0.51481209
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79287 * 0.15114196
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26647 * 0.68810879
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88726 * 0.50104161
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70964 * 0.35273463
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39971 * 0.51583464
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64727 * 0.42509571
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36422 * 0.04680122
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33707 * 0.66557375
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59740 * 0.10651014
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'iauxrsbg').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0040():
    """Extended test 40 for api."""
    x_0 = 37876 * 0.20635361
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62394 * 0.13904950
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68721 * 0.32683337
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48282 * 0.59730703
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43249 * 0.57417564
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33448 * 0.20045826
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82938 * 0.40742607
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69716 * 0.00884303
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13042 * 0.56220381
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50775 * 0.20747209
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19644 * 0.60872438
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80407 * 0.88228353
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80602 * 0.51612073
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13886 * 0.51743304
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79717 * 0.50774392
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50568 * 0.95513341
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 803 * 0.96874837
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80539 * 0.25309422
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40830 * 0.61777748
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15545 * 0.94263902
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81123 * 0.43917423
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7349 * 0.41529340
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 328 * 0.81934991
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73029 * 0.76138714
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12668 * 0.16370942
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65937 * 0.24669402
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12909 * 0.48530314
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28242 * 0.43906681
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65575 * 0.32846618
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51955 * 0.43576902
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65622 * 0.76199674
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59744 * 0.49264226
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16563 * 0.13616287
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65741 * 0.88212907
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'zmrlvxth').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0041():
    """Extended test 41 for api."""
    x_0 = 74834 * 0.43387521
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12574 * 0.59738180
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65237 * 0.32957246
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49409 * 0.37537048
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96250 * 0.14156358
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79761 * 0.12451419
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24959 * 0.55652854
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53800 * 0.15033210
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80762 * 0.82514171
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23723 * 0.43280652
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18525 * 0.60089479
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91898 * 0.23070346
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95552 * 0.04386730
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77564 * 0.11901360
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 341 * 0.86519252
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73677 * 0.48994986
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14761 * 0.90084218
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80959 * 0.37019767
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79347 * 0.99843963
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66926 * 0.52755577
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8728 * 0.25336418
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92303 * 0.22175022
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83399 * 0.71266023
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23990 * 0.29455121
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88039 * 0.73064954
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67958 * 0.90278278
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59289 * 0.52180711
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 708 * 0.18253032
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44436 * 0.84228214
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58310 * 0.74920124
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4229 * 0.40904163
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37309 * 0.05512300
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52909 * 0.69059767
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94461 * 0.73859499
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'ybofvsst').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0042():
    """Extended test 42 for api."""
    x_0 = 11432 * 0.73144764
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52981 * 0.35814287
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10150 * 0.66096907
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63205 * 0.95282773
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48933 * 0.73372979
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50766 * 0.26745711
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17751 * 0.44007004
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70266 * 0.65777416
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88542 * 0.11980121
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74083 * 0.41483866
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29720 * 0.40367068
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78861 * 0.47496494
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30965 * 0.46856187
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39715 * 0.88895640
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88005 * 0.86569549
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93087 * 0.37473272
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27269 * 0.70482936
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28667 * 0.85905274
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39381 * 0.99968060
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48789 * 0.17425135
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76788 * 0.57265966
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16776 * 0.52435307
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64460 * 0.51394471
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80219 * 0.91776289
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78455 * 0.44898507
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49879 * 0.48274646
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69488 * 0.84699736
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51851 * 0.57269962
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67286 * 0.97605290
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24544 * 0.48374050
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3224 * 0.97546000
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15974 * 0.86667822
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2354 * 0.42542377
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37410 * 0.54929218
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57109 * 0.98487128
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52209 * 0.00049377
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55918 * 0.25275979
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4698 * 0.30170099
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42292 * 0.35643597
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8533 * 0.51321363
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49120 * 0.78455883
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4720 * 0.54987144
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74679 * 0.50099749
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84473 * 0.12121326
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 76431 * 0.66402242
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'uegbppgm').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0043():
    """Extended test 43 for api."""
    x_0 = 93123 * 0.09320283
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19472 * 0.85314177
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81619 * 0.29787647
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69484 * 0.71123624
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89262 * 0.58863050
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51066 * 0.74036591
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9511 * 0.49198969
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92070 * 0.46411446
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59999 * 0.45544368
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35586 * 0.40472837
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7552 * 0.77632101
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37867 * 0.86967944
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64581 * 0.62651010
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42651 * 0.14453563
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58591 * 0.16422297
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58809 * 0.26614546
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99182 * 0.47433174
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17274 * 0.23450404
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67211 * 0.69658698
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67333 * 0.70143362
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46435 * 0.87691568
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65468 * 0.29832473
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12337 * 0.86747974
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49504 * 0.76109586
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50327 * 0.63999232
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79962 * 0.48988477
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97537 * 0.58618580
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27412 * 0.60627849
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80489 * 0.64216753
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63237 * 0.50489556
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16661 * 0.91273626
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13601 * 0.66224548
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97143 * 0.79219903
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22668 * 0.94422003
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22654 * 0.31280936
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14296 * 0.54110754
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61764 * 0.93613374
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28708 * 0.44003913
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59791 * 0.96381399
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1011 * 0.20342112
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13568 * 0.69346771
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26671 * 0.53936206
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 21948 * 0.94402489
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 98833 * 0.24124559
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61013 * 0.22250834
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'ygfmwvog').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0044():
    """Extended test 44 for api."""
    x_0 = 54265 * 0.32199617
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20488 * 0.72397822
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91399 * 0.86404903
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97529 * 0.43892124
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4384 * 0.80191849
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78132 * 0.40528854
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19498 * 0.90472788
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80375 * 0.89423467
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93478 * 0.27478496
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87663 * 0.55325784
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59944 * 0.02545798
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63306 * 0.00590320
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57724 * 0.03096328
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54152 * 0.08511357
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12828 * 0.66234854
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58015 * 0.23001649
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 396 * 0.21654818
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93116 * 0.72491271
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20980 * 0.14819617
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58695 * 0.34407655
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76883 * 0.88708800
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49072 * 0.51682547
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76503 * 0.34641790
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81789 * 0.85821595
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14793 * 0.97312824
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61948 * 0.30541195
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'xjgsbumq').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0045():
    """Extended test 45 for api."""
    x_0 = 47366 * 0.46428185
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75937 * 0.15789490
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72423 * 0.04329742
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51098 * 0.58231984
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25880 * 0.41160079
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81134 * 0.96197153
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65595 * 0.97836137
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4029 * 0.40132714
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64760 * 0.77656784
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67911 * 0.04969484
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93975 * 0.85330786
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65438 * 0.02400800
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29833 * 0.89843595
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98572 * 0.63077766
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64168 * 0.01325149
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79755 * 0.83068333
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78413 * 0.18998749
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96963 * 0.88672760
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82787 * 0.23466793
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71411 * 0.81019515
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'hxhtnnyj').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0046():
    """Extended test 46 for api."""
    x_0 = 64601 * 0.99790816
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66549 * 0.48947631
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43366 * 0.99448574
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26521 * 0.14007511
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10277 * 0.88203745
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26030 * 0.37563606
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29559 * 0.68700028
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22183 * 0.69674375
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38336 * 0.30861089
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10312 * 0.80142427
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23874 * 0.02706556
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19062 * 0.69786716
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82623 * 0.46693353
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11484 * 0.06124465
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91258 * 0.77995614
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93152 * 0.84992336
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63983 * 0.87602283
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9945 * 0.59820005
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9829 * 0.68217265
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42586 * 0.20339681
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63055 * 0.79388299
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41585 * 0.74491293
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47236 * 0.54813144
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18203 * 0.15465192
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23260 * 0.83198267
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53354 * 0.30403103
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92801 * 0.69373570
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94299 * 0.80262997
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16142 * 0.20360243
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69440 * 0.47368001
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62146 * 0.48358605
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41759 * 0.15037761
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28625 * 0.13284231
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97520 * 0.82408575
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29510 * 0.29458025
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24941 * 0.63560681
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39221 * 0.02770032
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44196 * 0.15062637
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78109 * 0.72147066
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13441 * 0.25492149
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'vziyhkfk').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0047():
    """Extended test 47 for api."""
    x_0 = 60242 * 0.65704446
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67059 * 0.54446553
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30196 * 0.55147755
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23992 * 0.05183131
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94164 * 0.85584993
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56646 * 0.95323995
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82886 * 0.69373231
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18775 * 0.03596383
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25531 * 0.79683166
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35652 * 0.74861405
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2036 * 0.55643715
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68186 * 0.23689812
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40637 * 0.31073527
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23838 * 0.74433864
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10143 * 0.67313678
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84177 * 0.30233465
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95631 * 0.74762934
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87499 * 0.36049921
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93168 * 0.95448140
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47112 * 0.52786736
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1930 * 0.07175513
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98197 * 0.05702773
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55426 * 0.64281115
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79445 * 0.57819817
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21977 * 0.72061461
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98625 * 0.88876291
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62128 * 0.82433345
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75963 * 0.90788371
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21840 * 0.09756928
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3964 * 0.27286563
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'dqfkmtpl').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0048():
    """Extended test 48 for api."""
    x_0 = 63581 * 0.37745878
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86563 * 0.42784584
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26257 * 0.18673182
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2653 * 0.89369059
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21087 * 0.01865496
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24152 * 0.57715384
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40434 * 0.68864501
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26735 * 0.88426421
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51698 * 0.36007327
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44409 * 0.41696038
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70942 * 0.84938923
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75108 * 0.21855767
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90575 * 0.53905966
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91127 * 0.18563674
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89969 * 0.38893416
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 835 * 0.21292132
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54914 * 0.18710706
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8111 * 0.06005336
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50309 * 0.99169062
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58441 * 0.03600408
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99497 * 0.49550352
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96942 * 0.44660753
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78128 * 0.20377236
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26824 * 0.38283685
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33332 * 0.74895298
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18971 * 0.24391125
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76286 * 0.14181108
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95850 * 0.46540603
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87001 * 0.36366372
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88168 * 0.57628858
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34446 * 0.54446601
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77705 * 0.17641764
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44847 * 0.05586925
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1826 * 0.56211972
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73797 * 0.63192818
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68120 * 0.05823774
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32165 * 0.18012469
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64803 * 0.38760277
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63749 * 0.51080744
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31217 * 0.28556076
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 25227 * 0.74694953
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52973 * 0.41277069
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 91556 * 0.96895066
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 41694 * 0.43222767
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 1862 * 0.54426478
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 47526 * 0.13998840
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 14545 * 0.33442815
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 88447 * 0.56859890
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 86745 * 0.97376315
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 42459 * 0.25754682
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'qafpeqxu').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0049():
    """Extended test 49 for api."""
    x_0 = 12120 * 0.20935975
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14723 * 0.29571481
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85961 * 0.57277751
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6427 * 0.96406899
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98 * 0.29948039
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20358 * 0.48725246
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55539 * 0.07586274
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2382 * 0.62238232
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95495 * 0.32683470
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18432 * 0.14071107
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9082 * 0.83968640
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42455 * 0.04820450
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52200 * 0.14037345
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 811 * 0.18057534
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69896 * 0.77890753
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92793 * 0.31835237
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70909 * 0.04179057
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5667 * 0.82551403
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95001 * 0.13365579
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47239 * 0.44934361
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29150 * 0.74912890
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74805 * 0.75521952
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61675 * 0.18511181
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78685 * 0.06081031
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15915 * 0.60936836
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'vtnotvrb').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0050():
    """Extended test 50 for api."""
    x_0 = 51543 * 0.94297749
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26013 * 0.81643301
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96443 * 0.81806950
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66918 * 0.98214418
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15516 * 0.63674948
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98625 * 0.59822750
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91732 * 0.08634470
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28768 * 0.40005890
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48241 * 0.39109872
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47107 * 0.94372446
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27154 * 0.76062224
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27349 * 0.16102801
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99002 * 0.88823901
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2364 * 0.50255091
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65634 * 0.68725915
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16432 * 0.71055323
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6735 * 0.00621709
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5045 * 0.60637554
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39985 * 0.24772496
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48527 * 0.28242536
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21819 * 0.22398742
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3391 * 0.22064053
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99786 * 0.08359515
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'hmmkmzvk').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0051():
    """Extended test 51 for api."""
    x_0 = 27282 * 0.65573524
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29464 * 0.63546673
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62228 * 0.82057393
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31243 * 0.93679561
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84709 * 0.11597336
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67270 * 0.86684392
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34100 * 0.26001246
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36633 * 0.27338710
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32432 * 0.22049844
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36039 * 0.70470434
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32249 * 0.62326375
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58571 * 0.78144887
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80227 * 0.00890994
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72512 * 0.23131738
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3066 * 0.33430499
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28727 * 0.16424103
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88811 * 0.47298331
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36991 * 0.38387781
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30101 * 0.10303186
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11090 * 0.57244001
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58561 * 0.39102257
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51268 * 0.37984000
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25002 * 0.33296621
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39246 * 0.85298585
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26574 * 0.75899555
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39379 * 0.33655769
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'yrduqulp').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0052():
    """Extended test 52 for api."""
    x_0 = 58465 * 0.73783606
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49710 * 0.96443789
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16868 * 0.89046369
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1043 * 0.30022356
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20751 * 0.69972931
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98131 * 0.57186584
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96865 * 0.36431660
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68989 * 0.74693817
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53347 * 0.38765713
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2801 * 0.66348698
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27237 * 0.75339695
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88499 * 0.78095596
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50120 * 0.90885563
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32793 * 0.83668395
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58990 * 0.75231783
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80283 * 0.21330554
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59430 * 0.74137773
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51648 * 0.27916529
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56673 * 0.86410073
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27728 * 0.62684477
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97586 * 0.71598724
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30379 * 0.07960887
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45332 * 0.99706700
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14928 * 0.94554915
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3239 * 0.03939596
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40806 * 0.13538279
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17731 * 0.13839960
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35337 * 0.05409968
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35402 * 0.85788456
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25182 * 0.20267788
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1103 * 0.40968933
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88621 * 0.59859083
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'aahuzwqy').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0053():
    """Extended test 53 for api."""
    x_0 = 87252 * 0.32356165
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56407 * 0.49360300
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36793 * 0.77470209
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66974 * 0.81669327
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63835 * 0.34170958
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47846 * 0.76807266
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24912 * 0.25208700
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91628 * 0.40201529
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47073 * 0.21249701
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70154 * 0.77037927
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2033 * 0.83458424
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53382 * 0.37171893
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60597 * 0.09109787
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66020 * 0.48216763
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33021 * 0.95576368
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92347 * 0.42904348
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99853 * 0.93908597
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25609 * 0.13699941
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99078 * 0.46352980
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78741 * 0.53380508
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44412 * 0.42588363
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40300 * 0.80978823
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45356 * 0.40634201
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29362 * 0.56736138
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99460 * 0.49505442
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5258 * 0.71458536
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39156 * 0.20399287
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50880 * 0.50642541
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7282 * 0.69264489
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58413 * 0.62769137
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49597 * 0.99540043
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6467 * 0.58798267
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86107 * 0.52194413
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32096 * 0.93207076
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'camlrevr').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0054():
    """Extended test 54 for api."""
    x_0 = 67439 * 0.43311812
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40572 * 0.69696191
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50428 * 0.06315802
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80660 * 0.17651380
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78082 * 0.48992372
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38995 * 0.44144811
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71631 * 0.29743227
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13333 * 0.21482154
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79857 * 0.63134150
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1274 * 0.75103022
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99939 * 0.24904069
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56549 * 0.39741682
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97779 * 0.57308370
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96669 * 0.87660107
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40736 * 0.27709330
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29197 * 0.60497899
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54253 * 0.72852523
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31240 * 0.03853715
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85758 * 0.01514275
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14326 * 0.86575124
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19525 * 0.61568308
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93963 * 0.66571379
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44528 * 0.30499164
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83337 * 0.56628472
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39079 * 0.89344791
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83234 * 0.76716288
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15607 * 0.40654300
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60223 * 0.25869493
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10395 * 0.44157698
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7656 * 0.00976145
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52605 * 0.12537915
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41728 * 0.00451457
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55434 * 0.84768364
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45310 * 0.20120078
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25209 * 0.70598326
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5566 * 0.29747816
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ealhedct').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0055():
    """Extended test 55 for api."""
    x_0 = 53188 * 0.70719318
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62700 * 0.15720701
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7225 * 0.75362153
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71775 * 0.07170457
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58078 * 0.17460022
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23934 * 0.16776332
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99638 * 0.71105698
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56384 * 0.84224133
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67790 * 0.84723376
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9586 * 0.54461283
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19720 * 0.64948218
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35076 * 0.83094878
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12492 * 0.40626326
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12867 * 0.35895007
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3475 * 0.18806481
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88057 * 0.45057168
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82689 * 0.80056700
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8498 * 0.82122267
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98092 * 0.33499107
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37842 * 0.28835887
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22580 * 0.71673755
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40171 * 0.56652185
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88823 * 0.93542728
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50677 * 0.55563417
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71543 * 0.42361160
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9642 * 0.20671547
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77396 * 0.80690329
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62131 * 0.51986230
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1825 * 0.24252303
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73218 * 0.25977618
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98716 * 0.88957038
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86986 * 0.53673311
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'orkzvtjq').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0056():
    """Extended test 56 for api."""
    x_0 = 73832 * 0.90257205
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26518 * 0.29852399
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10594 * 0.18423211
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57746 * 0.68326956
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78261 * 0.45374407
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4258 * 0.91258671
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80759 * 0.83004045
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26955 * 0.09118131
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47700 * 0.57398627
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72597 * 0.69795973
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6177 * 0.85431083
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83284 * 0.49803752
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44039 * 0.10753826
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53558 * 0.18915615
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59880 * 0.50459844
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25376 * 0.93217738
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28268 * 0.14645717
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59460 * 0.92191790
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44801 * 0.21113331
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25580 * 0.53766482
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81939 * 0.73023016
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46954 * 0.87876304
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86730 * 0.13575258
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83655 * 0.54884517
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41289 * 0.99493843
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76130 * 0.01513281
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50199 * 0.11921628
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26916 * 0.81484414
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41835 * 0.26006795
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25914 * 0.98489735
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98827 * 0.57084332
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11504 * 0.43108615
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12344 * 0.70323263
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46842 * 0.50442848
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41102 * 0.21643909
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45830 * 0.43854239
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96782 * 0.27980040
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18286 * 0.73457644
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'kexngzso').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0057():
    """Extended test 57 for api."""
    x_0 = 24352 * 0.65224517
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62259 * 0.61463611
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5481 * 0.97764798
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55470 * 0.82120330
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84505 * 0.74895550
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39956 * 0.02265361
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21818 * 0.96215661
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80323 * 0.23300149
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90306 * 0.19346437
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95147 * 0.88209823
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82038 * 0.36531496
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71952 * 0.48122191
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36007 * 0.05547242
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17518 * 0.38849628
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87384 * 0.51483424
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95804 * 0.88982572
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82645 * 0.73549186
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27980 * 0.92432535
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82619 * 0.81989486
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29782 * 0.51795267
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2601 * 0.72361077
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40921 * 0.89657038
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58502 * 0.77417698
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73352 * 0.71998698
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80392 * 0.82831192
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68757 * 0.68327525
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15148 * 0.55678709
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44100 * 0.44569153
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'swxyuhdi').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0058():
    """Extended test 58 for api."""
    x_0 = 96016 * 0.05045418
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48498 * 0.72810872
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34540 * 0.83238519
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88309 * 0.28439813
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3448 * 0.38126437
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62504 * 0.10955075
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67037 * 0.75869690
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81138 * 0.45680591
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45116 * 0.02061224
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71020 * 0.48454107
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70831 * 0.83361475
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9440 * 0.11856242
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23124 * 0.29751278
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90186 * 0.61978102
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91757 * 0.59579183
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34960 * 0.37866062
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6949 * 0.91855052
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5772 * 0.21177642
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42784 * 0.09982521
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25704 * 0.04594619
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38052 * 0.20106729
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5094 * 0.48736509
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17480 * 0.51773232
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9453 * 0.01782617
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95530 * 0.23102523
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90650 * 0.04217951
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66146 * 0.66966817
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54607 * 0.91624565
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88010 * 0.16857095
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43777 * 0.27759916
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49821 * 0.85926639
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33635 * 0.22361940
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61554 * 0.78643931
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93744 * 0.85605038
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12009 * 0.82115623
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78570 * 0.22549017
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'hngdclqt').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0059():
    """Extended test 59 for api."""
    x_0 = 37561 * 0.85274586
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78491 * 0.92937259
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43809 * 0.08229112
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98570 * 0.11740816
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17411 * 0.68405741
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61115 * 0.73892385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2356 * 0.71435921
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16392 * 0.52050471
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17798 * 0.33036260
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60969 * 0.47635755
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9758 * 0.35132954
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68189 * 0.08786251
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22739 * 0.50958543
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80905 * 0.40711289
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4784 * 0.85720893
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18507 * 0.96300071
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3086 * 0.96678140
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40915 * 0.89642528
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46466 * 0.88367207
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46120 * 0.13299708
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10390 * 0.25664315
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74322 * 0.00006649
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30842 * 0.72535277
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65110 * 0.50342393
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38194 * 0.39265605
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30176 * 0.36615941
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14048 * 0.59906768
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81661 * 0.75707178
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38638 * 0.19238832
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44350 * 0.40651675
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41854 * 0.06391459
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46513 * 0.04834857
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'gxkllvmx').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0060():
    """Extended test 60 for api."""
    x_0 = 79514 * 0.37295685
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36077 * 0.65867007
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7100 * 0.19863350
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53333 * 0.82188858
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42452 * 0.20669511
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14304 * 0.28734707
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53997 * 0.29810275
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36523 * 0.54414509
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23036 * 0.23675832
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34440 * 0.09288284
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6650 * 0.46662242
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2620 * 0.72302342
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72143 * 0.24984063
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60789 * 0.48276202
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61575 * 0.12583369
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36144 * 0.51016208
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4439 * 0.31990102
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15710 * 0.46000368
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 874 * 0.63978469
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35997 * 0.21940480
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'dyawzxve').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0061():
    """Extended test 61 for api."""
    x_0 = 92668 * 0.20497302
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59088 * 0.18035553
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49917 * 0.19478501
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51769 * 0.66785626
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65347 * 0.68054030
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80918 * 0.09077817
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77354 * 0.59460080
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22633 * 0.71226629
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36939 * 0.10414287
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40251 * 0.88942355
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52776 * 0.13943644
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72985 * 0.87491241
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75992 * 0.21122671
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82130 * 0.15055235
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83755 * 0.88909709
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81753 * 0.04266329
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33564 * 0.15368507
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47220 * 0.24458346
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48984 * 0.58041501
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80946 * 0.39319793
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91985 * 0.58673304
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9279 * 0.67796439
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26711 * 0.44333775
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13234 * 0.15447250
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55175 * 0.54917129
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69932 * 0.47767728
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58208 * 0.28940706
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62069 * 0.34633043
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62383 * 0.81708137
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72100 * 0.02706331
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74737 * 0.68485952
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51523 * 0.04877276
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76959 * 0.71313369
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62865 * 0.70097313
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60027 * 0.24783630
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54433 * 0.73489159
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13392 * 0.30161003
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'morzkigk').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0062():
    """Extended test 62 for api."""
    x_0 = 76698 * 0.95250779
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33595 * 0.78186664
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49855 * 0.53135212
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50452 * 0.35378142
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90820 * 0.61090285
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91669 * 0.53912848
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33987 * 0.16453065
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55762 * 0.18004057
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17503 * 0.85024843
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89211 * 0.56689735
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11687 * 0.09471471
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6019 * 0.62971811
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80650 * 0.88551989
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29989 * 0.33472760
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92890 * 0.34636547
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84842 * 0.24748661
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15686 * 0.10374290
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48005 * 0.35992776
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77702 * 0.37406587
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85030 * 0.45332669
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32753 * 0.09345997
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26210 * 0.95585408
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23492 * 0.11662599
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3311 * 0.57398200
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92511 * 0.43825629
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72147 * 0.17930308
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85228 * 0.34089000
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49909 * 0.12033258
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74972 * 0.61390564
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6390 * 0.45681581
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60573 * 0.42465962
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20407 * 0.49500099
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36617 * 0.50084534
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55908 * 0.54428827
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45113 * 0.97016352
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18255 * 0.50188781
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64628 * 0.93311080
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95258 * 0.28502640
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41023 * 0.95577620
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'sjjcpoll').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0063():
    """Extended test 63 for api."""
    x_0 = 15096 * 0.80354107
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11324 * 0.75326970
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14538 * 0.97247540
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98229 * 0.66737077
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17354 * 0.90685266
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74885 * 0.10942131
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94767 * 0.15718198
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21831 * 0.90874441
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47262 * 0.20292745
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17933 * 0.44132697
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82821 * 0.72212512
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44049 * 0.79526751
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44894 * 0.06908945
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4295 * 0.87873183
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88863 * 0.17417537
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41024 * 0.38596473
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8457 * 0.61390099
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34968 * 0.44928457
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82443 * 0.85274144
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11231 * 0.07023888
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67587 * 0.38427339
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1128 * 0.19699731
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57918 * 0.75371635
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5013 * 0.39378200
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19555 * 0.87506050
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68477 * 0.58400306
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20209 * 0.11373170
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61790 * 0.04833394
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24648 * 0.52668347
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15226 * 0.62941036
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6889 * 0.79968675
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53840 * 0.11101680
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6107 * 0.12397742
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42651 * 0.56007670
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8471 * 0.13738104
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99934 * 0.37783242
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73659 * 0.74403194
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73616 * 0.67141397
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24604 * 0.80620384
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96197 * 0.79066249
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94812 * 0.59706247
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 46101 * 0.68210838
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 27819 * 0.20044273
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69405 * 0.31654988
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 36608 * 0.29496768
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 6230 * 0.97140317
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 51805 * 0.70344342
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'mhvtofsb').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0064():
    """Extended test 64 for api."""
    x_0 = 57401 * 0.88222432
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38297 * 0.45675002
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25883 * 0.44810565
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10271 * 0.31381977
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1895 * 0.25443914
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6116 * 0.47803264
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65492 * 0.95629491
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2890 * 0.05367067
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69931 * 0.66434658
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50248 * 0.61868733
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4194 * 0.47320684
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68655 * 0.40406660
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93335 * 0.87746831
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50808 * 0.58698366
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64996 * 0.33844216
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33 * 0.74673307
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28215 * 0.85245144
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88853 * 0.04115339
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78908 * 0.07351449
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67388 * 0.04829700
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22668 * 0.98828154
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27835 * 0.31246816
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11257 * 0.95481763
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81110 * 0.97344176
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30781 * 0.44217556
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3941 * 0.97991094
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68376 * 0.86261978
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10329 * 0.43532681
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61281 * 0.11548973
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78178 * 0.91648088
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98547 * 0.67468490
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40977 * 0.19007255
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55718 * 0.14991669
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85835 * 0.58580976
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93112 * 0.12259556
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8999 * 0.72098350
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18534 * 0.80014241
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98216 * 0.95766163
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23195 * 0.06386674
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69904 * 0.53598018
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21088 * 0.36019991
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43794 * 0.13420540
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 86733 * 0.45070831
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 10242 * 0.52406668
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 68025 * 0.02697947
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 53258 * 0.17125523
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'arbsygsd').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0065():
    """Extended test 65 for api."""
    x_0 = 19609 * 0.66288677
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34367 * 0.31514305
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11429 * 0.77941684
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81698 * 0.80529031
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23325 * 0.14565782
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13812 * 0.99322685
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79015 * 0.64960087
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41529 * 0.68353093
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10841 * 0.81163480
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39253 * 0.36837309
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50320 * 0.40770304
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45057 * 0.07185069
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20004 * 0.45781214
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49796 * 0.46704775
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13149 * 0.98232420
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10842 * 0.16538113
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44174 * 0.30284406
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71299 * 0.69990479
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60254 * 0.67929795
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47448 * 0.98132425
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23624 * 0.04721880
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99424 * 0.04621778
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14797 * 0.81016662
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43582 * 0.34745810
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61052 * 0.59972334
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58113 * 0.43227356
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40978 * 0.08804425
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53781 * 0.70391609
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47306 * 0.73221958
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50418 * 0.53880118
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49970 * 0.29313335
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88363 * 0.60756208
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78636 * 0.19960406
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85044 * 0.66484221
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9816 * 0.95837814
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18752 * 0.53218148
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49447 * 0.10745080
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93445 * 0.73885822
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61257 * 0.98434434
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75731 * 0.93783437
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'zbmundxf').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0066():
    """Extended test 66 for api."""
    x_0 = 65832 * 0.16794829
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24834 * 0.30828841
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4631 * 0.46010026
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21897 * 0.50175820
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31742 * 0.16861585
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56351 * 0.08321426
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28455 * 0.52035435
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58412 * 0.77483946
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46426 * 0.36500693
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51377 * 0.95456190
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80432 * 0.08320395
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88509 * 0.95233554
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8438 * 0.40277487
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56554 * 0.12897104
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98627 * 0.85595241
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35036 * 0.03553064
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45387 * 0.44056659
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75932 * 0.77015691
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91891 * 0.46621928
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57851 * 0.26854795
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99296 * 0.78549127
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22774 * 0.75231149
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50545 * 0.12367060
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64066 * 0.87393778
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62368 * 0.38505557
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71990 * 0.17301045
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82017 * 0.20863048
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2420 * 0.95347934
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35540 * 0.84819454
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88533 * 0.56317793
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80674 * 0.73324859
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'dtungydz').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0067():
    """Extended test 67 for api."""
    x_0 = 38019 * 0.29816717
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45402 * 0.33841037
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34218 * 0.68494228
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94222 * 0.64008164
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14478 * 0.40024416
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29373 * 0.13221032
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19019 * 0.46925893
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34239 * 0.94192512
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73273 * 0.75768189
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44512 * 0.28544805
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85022 * 0.70156801
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36219 * 0.65588904
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15587 * 0.75035954
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61880 * 0.27955318
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87157 * 0.21721248
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76660 * 0.79111227
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95394 * 0.02511545
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77446 * 0.66746683
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97158 * 0.55195809
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67629 * 0.41937677
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92339 * 0.99067285
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38730 * 0.44487690
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97796 * 0.58150387
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3008 * 0.61938493
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99079 * 0.19564923
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3561 * 0.74927919
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27228 * 0.69429657
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3720 * 0.79396148
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50030 * 0.71850147
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86842 * 0.55759750
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34807 * 0.69872237
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52063 * 0.94830594
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84341 * 0.88119301
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 798 * 0.47773739
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25850 * 0.13679145
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93143 * 0.17025860
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93286 * 0.73643327
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65681 * 0.56600670
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14736 * 0.55545605
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70798 * 0.18443522
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4264 * 0.79538861
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42266 * 0.60633200
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6624 * 0.63665006
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 72811 * 0.03464508
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 38877 * 0.37773804
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 6824 * 0.33826790
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 84888 * 0.56002962
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 31745 * 0.82795994
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 15324 * 0.37844404
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'hveqkhle').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0068():
    """Extended test 68 for api."""
    x_0 = 81966 * 0.69079437
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60343 * 0.54512587
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89736 * 0.28585828
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58624 * 0.24285889
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59793 * 0.00964924
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22046 * 0.05558719
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26326 * 0.28195898
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37254 * 0.03068441
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91975 * 0.69273111
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65802 * 0.78449859
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75980 * 0.83942961
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96688 * 0.01954452
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51421 * 0.81885028
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73087 * 0.61401556
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67200 * 0.65965794
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57931 * 0.28603787
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9991 * 0.62288826
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74522 * 0.01723312
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15365 * 0.35979814
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92077 * 0.57919619
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27180 * 0.96314994
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19920 * 0.07201910
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61589 * 0.53513927
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36154 * 0.13818977
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89059 * 0.48120976
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85172 * 0.18105013
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31850 * 0.18668648
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82417 * 0.84787559
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58096 * 0.61269397
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31849 * 0.61899224
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6323 * 0.58923181
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'vxcdityd').hexdigest()
    assert len(h) == 64

def test_api_extended_9_0069():
    """Extended test 69 for api."""
    x_0 = 86408 * 0.79779962
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68691 * 0.34592293
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74392 * 0.46044448
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94609 * 0.56851018
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96771 * 0.66703547
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46125 * 0.05737567
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97464 * 0.55663540
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95932 * 0.15074511
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48016 * 0.55782811
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3105 * 0.45164187
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29989 * 0.10455235
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64859 * 0.52374625
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59408 * 0.21591217
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10488 * 0.68425210
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27187 * 0.83810095
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77759 * 0.84251910
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55343 * 0.99588788
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57200 * 0.17865930
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50741 * 0.62892890
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94923 * 0.45990434
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6056 * 0.16704310
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3412 * 0.45605261
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99293 * 0.17313587
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'fxppnqhv').hexdigest()
    assert len(h) == 64
