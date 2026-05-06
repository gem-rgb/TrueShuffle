"""Extended tests for scheduler suite 0."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_scheduler_extended_0_0000():
    """Extended test 0 for scheduler."""
    x_0 = 67130 * 0.40089805
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76933 * 0.48310396
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43797 * 0.08903767
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68097 * 0.67264945
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61933 * 0.79471054
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48418 * 0.94677285
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78955 * 0.72830881
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84467 * 0.47916921
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73162 * 0.60209733
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75865 * 0.46202698
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54821 * 0.02491865
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21383 * 0.49821007
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50186 * 0.24972948
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34300 * 0.23065289
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23935 * 0.29465343
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95174 * 0.88593775
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12110 * 0.94248426
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51778 * 0.65631209
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42002 * 0.21545884
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50483 * 0.33690023
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'kovafpqq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0001():
    """Extended test 1 for scheduler."""
    x_0 = 20099 * 0.06008910
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44914 * 0.15077950
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15242 * 0.29086105
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21267 * 0.31638379
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96442 * 0.84297671
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46345 * 0.31201346
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72981 * 0.79702365
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25640 * 0.98329528
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11588 * 0.43203848
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45697 * 0.89012680
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40077 * 0.78477731
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57161 * 0.15652475
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32772 * 0.15053876
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85657 * 0.12834348
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20030 * 0.87853527
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50216 * 0.31929896
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85668 * 0.23103417
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67633 * 0.75034362
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61213 * 0.51185316
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53655 * 0.56535310
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58491 * 0.65020569
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26591 * 0.92135918
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2546 * 0.01669091
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32819 * 0.83679768
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98998 * 0.07787119
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88092 * 0.08445369
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38699 * 0.23489733
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10023 * 0.43120320
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29654 * 0.04844022
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85834 * 0.64486171
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31284 * 0.96342947
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85321 * 0.16887584
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96375 * 0.20086650
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'rolodccg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0002():
    """Extended test 2 for scheduler."""
    x_0 = 41646 * 0.29274669
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36395 * 0.75992545
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28734 * 0.02058071
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61204 * 0.71814112
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58748 * 0.77290298
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8906 * 0.36966071
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48512 * 0.72865459
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46394 * 0.43423816
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9291 * 0.98275240
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88804 * 0.31098506
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56208 * 0.28009418
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77805 * 0.17282871
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62459 * 0.01314494
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47139 * 0.70393088
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75006 * 0.27996454
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40345 * 0.14742809
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39679 * 0.01733618
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60049 * 0.81076025
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51883 * 0.27675033
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55926 * 0.67251181
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87771 * 0.91265197
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58198 * 0.73477800
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86375 * 0.21339271
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44927 * 0.16251867
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84623 * 0.67801846
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42919 * 0.21254496
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50393 * 0.75261208
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75831 * 0.41157656
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26168 * 0.11567316
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98989 * 0.56036525
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12956 * 0.22110346
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62677 * 0.98552978
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87844 * 0.98742294
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42781 * 0.81350187
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92130 * 0.92394963
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46630 * 0.25613476
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15242 * 0.67768993
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93359 * 0.28819059
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13460 * 0.93858545
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11978 * 0.68868552
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36029 * 0.54712790
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13259 * 0.51116832
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20722 * 0.84036055
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 80806 * 0.28617395
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 49911 * 0.76492773
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 13238 * 0.66135147
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 52261 * 0.32205052
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'dxmnzwij').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0003():
    """Extended test 3 for scheduler."""
    x_0 = 46818 * 0.41114047
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7719 * 0.54235642
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35307 * 0.76657682
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22475 * 0.55643971
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83359 * 0.32134396
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14481 * 0.58910146
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93581 * 0.40337918
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26812 * 0.09554034
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41067 * 0.36191785
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96132 * 0.78460354
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2869 * 0.54518619
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28956 * 0.96162800
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36407 * 0.08379230
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53615 * 0.62773505
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40824 * 0.75966773
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67804 * 0.11178945
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72850 * 0.27346741
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97914 * 0.76303188
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79976 * 0.35950086
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82638 * 0.64330225
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22549 * 0.76638474
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68570 * 0.82792985
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51610 * 0.35433027
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38128 * 0.67601965
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42308 * 0.78449480
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72966 * 0.97367660
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 912 * 0.30070969
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80102 * 0.26398681
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24158 * 0.33068578
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'dxcsqtsc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0004():
    """Extended test 4 for scheduler."""
    x_0 = 24805 * 0.00313052
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35187 * 0.78176355
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80584 * 0.55645670
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65812 * 0.48496347
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6114 * 0.65271778
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41806 * 0.89623138
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71154 * 0.42422391
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7728 * 0.87080824
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47804 * 0.77719174
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70483 * 0.17106318
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69218 * 0.82185214
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36865 * 0.38395699
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9121 * 0.84772101
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89562 * 0.48700143
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2054 * 0.68459647
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31972 * 0.68165477
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46667 * 0.81237859
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97901 * 0.01881907
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38735 * 0.23912337
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82704 * 0.51517858
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65622 * 0.90119728
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71161 * 0.88827884
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'zqaqqarm').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0005():
    """Extended test 5 for scheduler."""
    x_0 = 49243 * 0.62543692
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18713 * 0.94508299
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41693 * 0.00488571
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22439 * 0.51569645
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74695 * 0.28165801
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38830 * 0.96682272
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52696 * 0.00455971
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62829 * 0.37890898
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31185 * 0.96778519
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28713 * 0.10094709
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52371 * 0.89053041
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19688 * 0.23242805
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44060 * 0.67031695
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90410 * 0.63952272
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75172 * 0.32715660
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59548 * 0.74871418
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51563 * 0.62049738
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51154 * 0.47590234
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62053 * 0.17720388
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9803 * 0.53358559
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6036 * 0.22647768
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85424 * 0.18887144
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93262 * 0.30361772
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8607 * 0.61039897
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16838 * 0.63370688
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13288 * 0.99450094
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15062 * 0.46363556
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91419 * 0.02265631
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57421 * 0.14787380
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74003 * 0.13461963
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76391 * 0.80899920
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53206 * 0.56696056
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10001 * 0.84875481
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42179 * 0.74003591
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56076 * 0.97122132
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6112 * 0.92296822
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9299 * 0.02597768
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'gdsismlx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0006():
    """Extended test 6 for scheduler."""
    x_0 = 3524 * 0.85157416
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29699 * 0.89135243
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25718 * 0.48491831
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98564 * 0.05296227
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84449 * 0.34036199
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69987 * 0.33574876
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5461 * 0.46453477
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47078 * 0.44592916
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25243 * 0.46053040
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83727 * 0.22943788
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66316 * 0.71427373
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 279 * 0.09413650
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32770 * 0.20431803
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40888 * 0.39781385
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29496 * 0.30246201
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69376 * 0.99449590
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77652 * 0.17876803
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44215 * 0.85946287
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18700 * 0.56309637
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83955 * 0.53072522
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92746 * 0.87106733
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87751 * 0.33377987
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88402 * 0.27916494
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51841 * 0.77321481
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36410 * 0.07590128
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44985 * 0.62825492
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70755 * 0.24678326
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75562 * 0.61628933
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12439 * 0.68415986
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42212 * 0.61295206
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37014 * 0.12030639
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93222 * 0.92140184
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30871 * 0.18343303
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36235 * 0.27030367
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'mbfcfedc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0007():
    """Extended test 7 for scheduler."""
    x_0 = 7580 * 0.67667177
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13697 * 0.77723796
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93662 * 0.44270934
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33310 * 0.51871875
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7243 * 0.19112119
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77789 * 0.63602903
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45789 * 0.93795462
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85680 * 0.80110755
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79385 * 0.95191925
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43650 * 0.22092384
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33034 * 0.68613168
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97733 * 0.96639191
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12242 * 0.86464040
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33663 * 0.05097227
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9367 * 0.26974377
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19655 * 0.90825949
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34224 * 0.67124373
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9237 * 0.07170562
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65336 * 0.94656426
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54240 * 0.42891033
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50265 * 0.90395743
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30239 * 0.44011908
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40315 * 0.42428554
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13168 * 0.26119638
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36505 * 0.02728593
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83272 * 0.94468059
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69580 * 0.40166710
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43301 * 0.08722095
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76750 * 0.11029697
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17920 * 0.97165365
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69413 * 0.61624350
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82866 * 0.10360296
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84223 * 0.95336503
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6990 * 0.26665031
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28630 * 0.09991330
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64444 * 0.59383186
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65387 * 0.62279283
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61615 * 0.92611637
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'gvxmkiel').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0008():
    """Extended test 8 for scheduler."""
    x_0 = 52851 * 0.54232346
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71330 * 0.42225953
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91304 * 0.05669091
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76995 * 0.95358625
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38492 * 0.82123736
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22005 * 0.84102799
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14038 * 0.07122206
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58715 * 0.67030510
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94146 * 0.85431931
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9885 * 0.04174194
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27289 * 0.83447799
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5408 * 0.28131165
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71272 * 0.32152747
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8465 * 0.56838749
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87051 * 0.01474864
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52864 * 0.73970248
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61234 * 0.38633876
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13840 * 0.55761026
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55382 * 0.95307869
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13720 * 0.60758278
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20218 * 0.89123675
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29827 * 0.05572908
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91284 * 0.82871977
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32426 * 0.25978425
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48474 * 0.29514916
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58861 * 0.80367871
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28055 * 0.93713553
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22432 * 0.23484301
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18961 * 0.16694054
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52375 * 0.30462043
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38624 * 0.99467706
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97781 * 0.33837421
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'comrfxev').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0009():
    """Extended test 9 for scheduler."""
    x_0 = 61599 * 0.71133275
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41852 * 0.43090021
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11314 * 0.01639813
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45809 * 0.68281886
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51669 * 0.72190918
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68756 * 0.42709296
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95309 * 0.79791806
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43040 * 0.17215455
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32163 * 0.52463011
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46609 * 0.03182920
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13597 * 0.69416795
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78565 * 0.22446268
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85601 * 0.40237372
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51340 * 0.18310265
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76048 * 0.30137756
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54660 * 0.03797880
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6176 * 0.49173666
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91363 * 0.15031806
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87539 * 0.41394986
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35039 * 0.42005159
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81338 * 0.34307718
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86436 * 0.35555249
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8109 * 0.57373095
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77281 * 0.66546531
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21648 * 0.04062320
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56801 * 0.49796744
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53071 * 0.97357624
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28172 * 0.19223554
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32971 * 0.36245068
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59040 * 0.43862081
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27173 * 0.73813938
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30544 * 0.70001522
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'ydfpfspq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0010():
    """Extended test 10 for scheduler."""
    x_0 = 61604 * 0.23778801
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44971 * 0.33184742
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73835 * 0.61200546
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1144 * 0.39628964
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57683 * 0.34690990
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61297 * 0.90423854
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6506 * 0.53437495
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72392 * 0.07849986
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1811 * 0.70228709
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53725 * 0.07972540
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93749 * 0.69801835
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31591 * 0.76632397
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28278 * 0.50881217
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33380 * 0.10339136
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75661 * 0.40507447
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71267 * 0.61407530
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70232 * 0.93576349
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12621 * 0.41178856
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4369 * 0.45652945
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58925 * 0.93556294
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24786 * 0.07135346
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63413 * 0.49978523
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56449 * 0.14347445
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39117 * 0.76463673
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28057 * 0.31797998
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55414 * 0.62889800
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11569 * 0.17803188
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20891 * 0.60360500
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70807 * 0.94656516
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79551 * 0.25313572
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73212 * 0.32346569
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57987 * 0.98253799
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16332 * 0.80800154
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7788 * 0.04987928
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39051 * 0.67814413
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22426 * 0.50842642
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24488 * 0.10192999
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87052 * 0.88419512
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1492 * 0.45939277
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52107 * 0.77621626
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 66153 * 0.13481284
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 55697 * 0.19902011
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'cdlnvirp').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0011():
    """Extended test 11 for scheduler."""
    x_0 = 42899 * 0.80999830
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8943 * 0.18841728
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85212 * 0.05829021
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59387 * 0.41497669
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39397 * 0.81312164
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68745 * 0.07547045
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49088 * 0.71304260
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48217 * 0.43109094
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57052 * 0.97705539
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96351 * 0.00361908
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29095 * 0.97320597
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56019 * 0.92147603
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30204 * 0.33716392
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3938 * 0.75440870
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44249 * 0.88746688
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4259 * 0.44582583
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94303 * 0.72957482
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44836 * 0.61496352
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96954 * 0.86949025
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81823 * 0.04080524
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44200 * 0.30735693
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4953 * 0.86854560
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8902 * 0.14052714
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59361 * 0.51841346
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6437 * 0.31075225
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91070 * 0.20187384
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80998 * 0.68665821
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72919 * 0.29610334
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28797 * 0.09627385
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20118 * 0.97496995
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98598 * 0.17716894
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30254 * 0.49721015
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81036 * 0.27756778
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59141 * 0.50072525
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54557 * 0.64829239
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36783 * 0.19611696
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25105 * 0.81642624
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41383 * 0.77304374
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17815 * 0.14217369
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21917 * 0.87085617
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 93052 * 0.78782731
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82684 * 0.74545141
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 80164 * 0.26350407
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 68700 * 0.72774058
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11788 * 0.46182853
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 17892 * 0.84705160
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 95130 * 0.33845321
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'sunycvxh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0012():
    """Extended test 12 for scheduler."""
    x_0 = 10095 * 0.06017960
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84502 * 0.61919650
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28163 * 0.86512826
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3457 * 0.11083643
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99165 * 0.99869139
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37743 * 0.11715582
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10915 * 0.96567403
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99057 * 0.62583825
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87145 * 0.68641051
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36984 * 0.15729487
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2476 * 0.97431584
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97498 * 0.50514249
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48774 * 0.82626665
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8323 * 0.16739452
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27168 * 0.96267797
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15204 * 0.58446421
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16277 * 0.22915180
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6881 * 0.63971197
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53004 * 0.72176989
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34632 * 0.70564964
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26418 * 0.06003610
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90127 * 0.19980892
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85400 * 0.12598207
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11413 * 0.26320363
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23807 * 0.40707956
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62728 * 0.47452512
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 866 * 0.63235814
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 367 * 0.99408165
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46596 * 0.35295393
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19584 * 0.53499843
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74617 * 0.21768425
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'zxmkprhq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0013():
    """Extended test 13 for scheduler."""
    x_0 = 96570 * 0.17507179
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20664 * 0.91275992
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61890 * 0.16894730
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9257 * 0.97851585
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56212 * 0.45453506
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18414 * 0.80227698
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66133 * 0.06449458
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12626 * 0.34567286
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64509 * 0.57441603
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61968 * 0.77955173
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3727 * 0.75942901
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22247 * 0.17246556
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90668 * 0.55791613
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40851 * 0.39720962
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66975 * 0.18582386
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73510 * 0.23914168
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65575 * 0.75198206
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51812 * 0.11181229
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25781 * 0.99778359
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45452 * 0.16559108
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56069 * 0.54428449
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26110 * 0.61713381
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44276 * 0.57219252
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93128 * 0.94820735
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57388 * 0.45500725
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93108 * 0.86076658
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1374 * 0.85063036
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9702 * 0.76103503
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45345 * 0.80144841
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94444 * 0.80754330
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63054 * 0.79841449
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3733 * 0.09161124
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52061 * 0.73512820
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73619 * 0.26868414
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lffjwswa').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0014():
    """Extended test 14 for scheduler."""
    x_0 = 90207 * 0.00102735
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52365 * 0.45655643
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58259 * 0.59920413
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26271 * 0.92852061
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87416 * 0.51954334
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30604 * 0.40566027
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78368 * 0.59389806
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25825 * 0.66482595
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68399 * 0.79894261
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17863 * 0.67798250
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66220 * 0.39028969
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94566 * 0.10191137
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11717 * 0.05792281
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62466 * 0.45054016
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42599 * 0.61857114
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29199 * 0.33001710
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35973 * 0.01764484
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34954 * 0.61566259
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53014 * 0.90057810
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32738 * 0.01289323
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75873 * 0.97415607
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'pfpqhiki').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0015():
    """Extended test 15 for scheduler."""
    x_0 = 94273 * 0.38738166
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81072 * 0.53502128
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22505 * 0.19363882
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49054 * 0.14772484
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3671 * 0.60535539
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13644 * 0.59607020
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82985 * 0.78290020
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97782 * 0.77708631
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57236 * 0.43576364
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7226 * 0.90138090
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71696 * 0.72410020
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14485 * 0.98087355
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19137 * 0.04348300
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67622 * 0.86503708
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74054 * 0.51628483
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84576 * 0.93456506
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44478 * 0.90230315
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78647 * 0.01086652
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75870 * 0.05899631
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13112 * 0.36312306
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2485 * 0.66734800
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78403 * 0.50571702
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22117 * 0.05578624
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46420 * 0.72217022
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95130 * 0.85786980
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25719 * 0.46494049
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89520 * 0.30186969
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58748 * 0.03968423
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28013 * 0.75624172
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88329 * 0.16714296
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83780 * 0.06082209
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'rmjvzmhv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0016():
    """Extended test 16 for scheduler."""
    x_0 = 94312 * 0.32534957
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96467 * 0.06611420
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46545 * 0.56991300
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95640 * 0.85371200
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21078 * 0.89835657
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81684 * 0.88126532
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23750 * 0.63383641
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53717 * 0.79344540
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21009 * 0.23635145
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82501 * 0.59098233
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54150 * 0.78593975
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57632 * 0.26946149
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59466 * 0.60572735
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25896 * 0.48957577
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53063 * 0.33339054
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99353 * 0.71748249
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75393 * 0.64422569
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90098 * 0.91156392
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13763 * 0.04175803
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32776 * 0.74896655
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57248 * 0.85097504
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82903 * 0.39905576
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84674 * 0.08435774
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59605 * 0.03703337
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68688 * 0.76893039
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64651 * 0.13647515
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96732 * 0.61875980
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68468 * 0.41227386
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6101 * 0.50001522
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68785 * 0.09980661
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44707 * 0.88305879
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87179 * 0.45506927
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34176 * 0.93049943
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1236 * 0.12858687
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90646 * 0.80409253
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32052 * 0.77459416
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6491 * 0.99799187
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66979 * 0.58998500
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'yjyvsrwm').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0017():
    """Extended test 17 for scheduler."""
    x_0 = 15221 * 0.92275883
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92717 * 0.93819899
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63546 * 0.69420942
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53164 * 0.92053230
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79060 * 0.04776426
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22710 * 0.73008788
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33421 * 0.88082653
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9098 * 0.07456094
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86375 * 0.48279280
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29190 * 0.61950391
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48222 * 0.51714147
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64415 * 0.12069516
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99858 * 0.45370921
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80631 * 0.64954809
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8699 * 0.88180410
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53023 * 0.32092526
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29895 * 0.34150524
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95509 * 0.48031663
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69811 * 0.65778686
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65153 * 0.88282585
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20166 * 0.89488836
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10474 * 0.48439350
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51228 * 0.19871430
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52141 * 0.55330462
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32323 * 0.63922228
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48902 * 0.86231617
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16925 * 0.29815800
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33717 * 0.69241247
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15488 * 0.57179902
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56651 * 0.94852410
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28529 * 0.23105545
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39650 * 0.34782177
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57375 * 0.82900747
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72609 * 0.29201463
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15072 * 0.62031468
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 335 * 0.90714481
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56548 * 0.76699882
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5624 * 0.97199259
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92347 * 0.47836532
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84596 * 0.96714050
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37973 * 0.35109413
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93179 * 0.58023970
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81843 * 0.13092726
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 73979 * 0.60769153
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 31205 * 0.52560043
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 18677 * 0.57682121
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 14492 * 0.90907100
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 87451 * 0.41214230
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 58394 * 0.21976089
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'ptyhmeya').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0018():
    """Extended test 18 for scheduler."""
    x_0 = 63437 * 0.96752563
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20631 * 0.68503578
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26087 * 0.33427382
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86426 * 0.17561569
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61246 * 0.66193868
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36382 * 0.25229450
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4869 * 0.01918861
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62503 * 0.36610328
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57960 * 0.76831587
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2871 * 0.30684883
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79342 * 0.32111066
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37298 * 0.03534326
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37709 * 0.55926392
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89703 * 0.75953747
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67752 * 0.70383935
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64153 * 0.91794691
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50979 * 0.69372887
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33455 * 0.98671167
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18683 * 0.75516012
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62654 * 0.42505991
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88782 * 0.33886253
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29321 * 0.33278966
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72777 * 0.99925084
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46231 * 0.10468506
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32311 * 0.65631975
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14749 * 0.87955568
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34887 * 0.96392396
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70357 * 0.40215333
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45499 * 0.26801485
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66602 * 0.25583326
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37488 * 0.65798305
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19087 * 0.87908525
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67266 * 0.34148504
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43345 * 0.06553566
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63572 * 0.56446673
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58620 * 0.14378254
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83101 * 0.90465236
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82516 * 0.82377009
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63213 * 0.28502759
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1496 * 0.03110211
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69714 * 0.87202159
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 68767 * 0.50849097
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1878 * 0.64629822
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83728 * 0.91133054
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 7929 * 0.57979112
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 75500 * 0.75300477
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 96902 * 0.81397552
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 77242 * 0.58381486
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 89008 * 0.13165703
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'wocvbelo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0019():
    """Extended test 19 for scheduler."""
    x_0 = 19530 * 0.46235801
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84975 * 0.16965539
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89624 * 0.78228915
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68410 * 0.64935392
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94690 * 0.25067134
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68161 * 0.49790463
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87232 * 0.29299514
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73605 * 0.07824343
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23103 * 0.84365334
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16670 * 0.57546072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55515 * 0.00763741
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61948 * 0.76600592
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80007 * 0.73841809
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77282 * 0.50076718
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18891 * 0.38358045
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77378 * 0.16812138
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41291 * 0.12372752
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25708 * 0.28730354
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63068 * 0.29717850
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38594 * 0.89693592
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 240 * 0.34542202
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86182 * 0.58611775
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43816 * 0.69198865
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83594 * 0.91233448
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18023 * 0.47875291
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48581 * 0.22829798
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11834 * 0.25123140
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53667 * 0.62137746
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'pkkcnpqh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0020():
    """Extended test 20 for scheduler."""
    x_0 = 49378 * 0.76861645
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39266 * 0.54662084
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15752 * 0.00743893
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35557 * 0.26634106
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75594 * 0.28009342
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82170 * 0.66508593
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61355 * 0.37992365
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21612 * 0.84033465
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37611 * 0.87071735
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65331 * 0.67641130
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16941 * 0.76011640
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86851 * 0.14278795
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88342 * 0.68939870
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3926 * 0.67691794
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17470 * 0.85059478
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3825 * 0.16354484
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90429 * 0.57452797
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26060 * 0.12924506
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94010 * 0.36072249
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95715 * 0.28820389
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16604 * 0.37567586
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54994 * 0.10096079
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94998 * 0.49514834
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77109 * 0.35927794
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11354 * 0.92334541
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74530 * 0.59954170
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82858 * 0.55147024
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41729 * 0.27529828
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41647 * 0.75988889
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72717 * 0.35925913
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88152 * 0.07307648
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99519 * 0.87958431
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60061 * 0.30827300
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46608 * 0.35321192
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1576 * 0.31681077
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68988 * 0.25258716
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'zfyvfzzy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0021():
    """Extended test 21 for scheduler."""
    x_0 = 52057 * 0.65640038
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82252 * 0.78217302
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27606 * 0.23650578
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86836 * 0.85559046
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95933 * 0.90576384
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9969 * 0.52617226
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47611 * 0.57405485
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58878 * 0.32161028
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98554 * 0.05911202
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25274 * 0.61467483
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22010 * 0.50908608
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43206 * 0.52135372
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29325 * 0.51221557
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29384 * 0.15534838
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92242 * 0.86661749
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94021 * 0.21663978
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51498 * 0.42713894
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88915 * 0.76319510
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54434 * 0.01355185
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28863 * 0.84504233
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55714 * 0.34382198
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97766 * 0.89383509
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54457 * 0.26352572
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'wladzzea').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0022():
    """Extended test 22 for scheduler."""
    x_0 = 41253 * 0.10541089
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12956 * 0.36226811
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27902 * 0.05206492
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90763 * 0.41494161
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18406 * 0.54339917
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33220 * 0.23607114
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88891 * 0.54827348
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75257 * 0.61156535
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23421 * 0.12053515
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30397 * 0.65891313
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98778 * 0.65964063
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30396 * 0.62125812
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95824 * 0.09506998
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58545 * 0.53931481
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40084 * 0.65232863
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16581 * 0.17777179
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58591 * 0.57595114
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49988 * 0.67499434
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2831 * 0.04389722
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74359 * 0.42261361
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62852 * 0.56432564
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7674 * 0.46865487
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27706 * 0.93114914
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69210 * 0.89737707
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53506 * 0.88733883
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5747 * 0.56174315
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95631 * 0.65248707
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79133 * 0.29528131
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83542 * 0.06662498
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66667 * 0.24013173
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93979 * 0.17184946
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81957 * 0.96990374
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67634 * 0.98775214
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51744 * 0.85029150
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14053 * 0.01830983
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35527 * 0.22616838
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'kydjoero').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0023():
    """Extended test 23 for scheduler."""
    x_0 = 22226 * 0.57596047
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86326 * 0.97493770
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92819 * 0.36109150
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93011 * 0.05414641
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82859 * 0.01184636
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76140 * 0.98549987
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46411 * 0.30264561
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38999 * 0.81145019
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6761 * 0.95990129
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20315 * 0.18073149
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75963 * 0.31310377
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9716 * 0.05391832
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53329 * 0.74840766
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58238 * 0.90225566
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87505 * 0.06064316
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8621 * 0.28662348
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15750 * 0.64232435
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91078 * 0.88119944
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97229 * 0.65736576
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8881 * 0.81690899
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52171 * 0.84916612
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65758 * 0.83754746
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 629 * 0.10535859
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6414 * 0.98928270
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78104 * 0.32284854
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26564 * 0.18005879
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6903 * 0.67679625
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51789 * 0.66253313
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'hjpkpjoo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0024():
    """Extended test 24 for scheduler."""
    x_0 = 41920 * 0.36055804
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92425 * 0.17963935
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92239 * 0.44464711
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17547 * 0.51853988
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64478 * 0.16514042
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17603 * 0.37282464
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65420 * 0.90621175
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71886 * 0.29206393
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1190 * 0.08727016
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22898 * 0.51986503
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21045 * 0.18808186
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3023 * 0.19548939
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61954 * 0.21452330
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49316 * 0.09900221
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65187 * 0.37120895
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48790 * 0.79130427
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27210 * 0.54970954
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69548 * 0.47355636
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84694 * 0.88359198
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2490 * 0.08591251
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23787 * 0.17168015
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66175 * 0.35993755
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51107 * 0.45693133
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1301 * 0.74563120
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13126 * 0.13728454
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10333 * 0.67750155
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40625 * 0.81168615
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53715 * 0.45925913
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10558 * 0.43346566
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37688 * 0.37686391
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76944 * 0.15402691
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80113 * 0.32613778
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15860 * 0.77513091
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51786 * 0.02272885
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77030 * 0.81808662
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39289 * 0.28641075
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50087 * 0.00874198
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52056 * 0.57294338
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60640 * 0.04487450
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86752 * 0.48224155
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 73553 * 0.14075268
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25430 * 0.93386802
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 48853 * 0.31590163
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 80005 * 0.97263060
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 21558 * 0.91946866
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 74787 * 0.16300607
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'ogdfxgal').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0025():
    """Extended test 25 for scheduler."""
    x_0 = 74450 * 0.04222635
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50204 * 0.03235970
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82856 * 0.95981243
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1541 * 0.34054002
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48894 * 0.20638238
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9183 * 0.92180010
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51075 * 0.77647741
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81810 * 0.14997776
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9006 * 0.24188270
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7186 * 0.86042257
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47753 * 0.84681802
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22650 * 0.49470642
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30488 * 0.87750396
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61611 * 0.98245564
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95600 * 0.42390265
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53401 * 0.25816620
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86808 * 0.81664382
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53609 * 0.10818488
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93209 * 0.99055275
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54664 * 0.50424489
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 167 * 0.04567475
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85308 * 0.41893428
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73472 * 0.84973027
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84763 * 0.89572295
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98710 * 0.10574403
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24541 * 0.76293214
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63927 * 0.14389629
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33625 * 0.28021455
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'mbzuegyn').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0026():
    """Extended test 26 for scheduler."""
    x_0 = 83299 * 0.91549847
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26131 * 0.93663823
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52094 * 0.40857385
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65730 * 0.25543207
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25471 * 0.11997577
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23798 * 0.94504996
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51190 * 0.13835972
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25451 * 0.95158480
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16982 * 0.08743133
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13230 * 0.31440231
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98058 * 0.66737706
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6845 * 0.73956816
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34847 * 0.88676124
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91141 * 0.70512167
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66004 * 0.10608601
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42079 * 0.47685298
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99257 * 0.36551827
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73381 * 0.44216998
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39040 * 0.96899784
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17729 * 0.52760247
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73311 * 0.08721086
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6377 * 0.83145649
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'kcbnwoqo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0027():
    """Extended test 27 for scheduler."""
    x_0 = 6921 * 0.40096518
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79643 * 0.91428172
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5742 * 0.37441057
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25130 * 0.75110464
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94706 * 0.96097922
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15411 * 0.74813739
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56774 * 0.87084538
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13494 * 0.14928984
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33356 * 0.94460107
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77103 * 0.66995626
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83663 * 0.00664372
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24860 * 0.43812554
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45314 * 0.60105101
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33606 * 0.98768347
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26595 * 0.43142013
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54358 * 0.74774987
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94829 * 0.90515943
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83051 * 0.22238876
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64723 * 0.43026994
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22840 * 0.40816134
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27345 * 0.73015349
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50279 * 0.69913363
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54596 * 0.04626176
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10412 * 0.57030275
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9019 * 0.51403349
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11460 * 0.43567377
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76857 * 0.59188346
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15457 * 0.86832562
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47558 * 0.60184673
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 814 * 0.18998196
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87671 * 0.93918766
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88865 * 0.83039860
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12084 * 0.39128390
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62505 * 0.13890591
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52036 * 0.01832540
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79717 * 0.86509557
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14656 * 0.39048973
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19297 * 0.96240817
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11457 * 0.85968836
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34252 * 0.08715575
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19730 * 0.26189519
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9274 * 0.92179795
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16216 * 0.11567013
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 52287 * 0.58798287
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'tvqqnqze').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0028():
    """Extended test 28 for scheduler."""
    x_0 = 67086 * 0.62256166
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77496 * 0.05554603
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34195 * 0.78280692
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32494 * 0.43681177
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83521 * 0.64657541
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96750 * 0.12979370
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56740 * 0.02945756
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62212 * 0.83789147
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44118 * 0.93203539
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86787 * 0.47365836
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89284 * 0.92583693
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16666 * 0.03635693
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78682 * 0.28263622
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10018 * 0.17660805
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13352 * 0.05583786
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24976 * 0.54243562
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34333 * 0.05263869
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91571 * 0.02886978
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79066 * 0.50962834
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7626 * 0.97603807
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4910 * 0.84219496
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4474 * 0.62093898
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75808 * 0.59069639
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57467 * 0.17672817
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41285 * 0.44529204
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64275 * 0.62082552
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61999 * 0.95876571
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12069 * 0.41650309
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88105 * 0.83177260
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35435 * 0.01919472
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3496 * 0.77619228
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63258 * 0.35000298
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43507 * 0.67544810
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49879 * 0.91002175
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50881 * 0.26701155
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20499 * 0.38697646
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61499 * 0.22419394
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6371 * 0.61317502
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28030 * 0.15560057
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 50935 * 0.23011798
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71037 * 0.78303825
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25985 * 0.33235992
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20453 * 0.04222648
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47444 * 0.67209874
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 99396 * 0.71151903
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 29625 * 0.30899612
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 27605 * 0.41908832
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 60972 * 0.58187639
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 80965 * 0.73063362
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 27610 * 0.22670070
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'whkyzowq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0029():
    """Extended test 29 for scheduler."""
    x_0 = 10038 * 0.46172802
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51110 * 0.18507463
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36108 * 0.91832206
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58618 * 0.10094493
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64341 * 0.85653852
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68759 * 0.82313060
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12481 * 0.21154971
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78871 * 0.66843176
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66061 * 0.41335907
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5175 * 0.80330557
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73462 * 0.01702798
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29214 * 0.87734500
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43921 * 0.01951194
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56294 * 0.39313812
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17509 * 0.08662521
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47874 * 0.63333244
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48904 * 0.38372073
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71941 * 0.20197769
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29493 * 0.60405601
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5819 * 0.18855518
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71047 * 0.39766723
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54692 * 0.48612877
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77819 * 0.30396718
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16802 * 0.03657901
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80389 * 0.16559858
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22325 * 0.92320163
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93889 * 0.84692235
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46072 * 0.01163702
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6152 * 0.08819057
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22117 * 0.83945528
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97924 * 0.96679708
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'vprprsqx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0030():
    """Extended test 30 for scheduler."""
    x_0 = 39457 * 0.85882737
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78168 * 0.94048098
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83460 * 0.68232547
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82789 * 0.92828701
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73288 * 0.04977784
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26588 * 0.66131147
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50239 * 0.47546336
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9023 * 0.54350279
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75286 * 0.74208040
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45312 * 0.89015488
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70882 * 0.29459789
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20151 * 0.47249832
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86218 * 0.68546869
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56489 * 0.25216785
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87130 * 0.74369279
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95956 * 0.30331208
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88299 * 0.63052936
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56033 * 0.11250475
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98064 * 0.42792675
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5460 * 0.88372254
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48752 * 0.76808976
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5171 * 0.91822675
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16000 * 0.39210017
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27950 * 0.37464161
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91446 * 0.47839964
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18297 * 0.68300167
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14999 * 0.92784146
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24898 * 0.49392948
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65393 * 0.91577746
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86974 * 0.03204894
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55914 * 0.67938783
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44145 * 0.91241759
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83063 * 0.63087356
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3593 * 0.13060806
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64944 * 0.98602040
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89145 * 0.03004898
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51292 * 0.70937939
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24090 * 0.52077218
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97153 * 0.91720188
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33148 * 0.29134386
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 67810 * 0.26753602
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58578 * 0.53638524
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36074 * 0.10915893
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83001 * 0.30898909
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'utykknac').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0031():
    """Extended test 31 for scheduler."""
    x_0 = 90024 * 0.82597300
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46731 * 0.15721097
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37360 * 0.26352434
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71446 * 0.62118668
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18316 * 0.33499429
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73440 * 0.99585061
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10061 * 0.55007471
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77136 * 0.95013847
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24971 * 0.52271026
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63158 * 0.47183170
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96856 * 0.36395978
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50780 * 0.75311804
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78607 * 0.65413468
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57491 * 0.24043798
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10127 * 0.74973988
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47278 * 0.89093524
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5227 * 0.27282458
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52294 * 0.11382388
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95823 * 0.60649266
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92901 * 0.42250647
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27164 * 0.35007932
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41631 * 0.61639245
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77315 * 0.95527526
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44162 * 0.94853555
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70973 * 0.08876622
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48156 * 0.60241506
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9962 * 0.51116668
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22684 * 0.34270853
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55133 * 0.01924140
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1258 * 0.65871118
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'klvjvmzw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0032():
    """Extended test 32 for scheduler."""
    x_0 = 40987 * 0.16782370
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72760 * 0.75056537
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30562 * 0.18437029
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14352 * 0.49735073
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31426 * 0.39223880
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63359 * 0.85036016
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27312 * 0.33658563
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89123 * 0.95903770
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79042 * 0.82751525
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8924 * 0.79219943
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34774 * 0.25583321
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13113 * 0.61899348
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1714 * 0.40683948
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94683 * 0.59978732
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30303 * 0.47035885
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98576 * 0.91270964
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93941 * 0.63564075
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44330 * 0.44898135
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22425 * 0.97257553
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93988 * 0.91538765
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94449 * 0.79108977
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84740 * 0.08491533
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55070 * 0.84326090
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74624 * 0.17302030
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88447 * 0.58575008
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23202 * 0.84689356
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48188 * 0.89017205
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25332 * 0.18935972
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17257 * 0.72041422
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78881 * 0.68840993
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28313 * 0.32964419
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68872 * 0.31504626
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'kbpedger').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0033():
    """Extended test 33 for scheduler."""
    x_0 = 39556 * 0.21383230
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16171 * 0.55991716
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17730 * 0.83824471
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47466 * 0.05864777
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33256 * 0.75464412
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99858 * 0.64563747
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 425 * 0.83504309
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57477 * 0.03065328
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81653 * 0.06604934
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9692 * 0.67184680
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42501 * 0.29097693
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40921 * 0.54140786
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32921 * 0.77562105
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93213 * 0.28942790
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39025 * 0.69558430
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29752 * 0.61942251
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 359 * 0.67244455
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5370 * 0.65406199
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34551 * 0.92580164
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2044 * 0.19685775
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86060 * 0.61941368
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22734 * 0.03481728
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13551 * 0.53914665
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7995 * 0.86244301
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85638 * 0.34257112
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91187 * 0.20964529
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86634 * 0.64861751
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12318 * 0.18855168
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 426 * 0.70467079
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47445 * 0.78845525
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38049 * 0.03501494
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35865 * 0.97587688
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30000 * 0.67170355
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4994 * 0.45833015
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91627 * 0.68121169
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25623 * 0.96865949
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25305 * 0.79424731
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58507 * 0.68472138
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97274 * 0.53531830
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23098 * 0.88832254
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75176 * 0.20239178
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 90663 * 0.93256726
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44056 * 0.60144726
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 45394 * 0.55951235
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71319 * 0.95276952
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 68519 * 0.53213955
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 90113 * 0.20127323
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 24454 * 0.44126350
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'aduhwcgn').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0034():
    """Extended test 34 for scheduler."""
    x_0 = 90026 * 0.12681706
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22685 * 0.07180107
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36130 * 0.25678089
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67172 * 0.19646646
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71555 * 0.46713701
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2478 * 0.93483744
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93173 * 0.03632742
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62604 * 0.73809974
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73894 * 0.22477455
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18097 * 0.72994951
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17610 * 0.78201178
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23786 * 0.63295516
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56982 * 0.42547231
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94700 * 0.25863530
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55037 * 0.04774321
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49519 * 0.87726943
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24656 * 0.40454844
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62384 * 0.23631622
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37645 * 0.90773689
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59711 * 0.00420436
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62342 * 0.95505943
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93771 * 0.08019180
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4490 * 0.96842516
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'nvigieqq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0035():
    """Extended test 35 for scheduler."""
    x_0 = 15771 * 0.20498784
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71120 * 0.03753012
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48227 * 0.87716844
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33720 * 0.49463305
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90426 * 0.28514037
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77757 * 0.72765185
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91485 * 0.19485515
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31724 * 0.26917805
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89745 * 0.96634595
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93875 * 0.39755688
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64808 * 0.30680312
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50492 * 0.83601205
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40735 * 0.76055690
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62990 * 0.00845509
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65494 * 0.79089241
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17214 * 0.93499723
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6655 * 0.15211275
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28697 * 0.24347590
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82403 * 0.67631805
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92487 * 0.02613881
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12508 * 0.43462126
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'zxfytbvz').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0036():
    """Extended test 36 for scheduler."""
    x_0 = 85071 * 0.00580706
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47134 * 0.25262874
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13449 * 0.84565903
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43391 * 0.66001920
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13658 * 0.37514344
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95720 * 0.86475396
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73682 * 0.47590412
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90576 * 0.59723173
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5836 * 0.17671468
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28397 * 0.37351260
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58024 * 0.36310170
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80468 * 0.48531752
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35420 * 0.10929849
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14578 * 0.48333664
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93304 * 0.84520556
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38574 * 0.74077271
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65199 * 0.11520017
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86035 * 0.09927453
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32977 * 0.79336573
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84962 * 0.10694009
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67941 * 0.06024338
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8949 * 0.59537295
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7676 * 0.93086272
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96917 * 0.22327473
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23137 * 0.36815265
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67498 * 0.52872983
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91203 * 0.25764040
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90371 * 0.50647135
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93719 * 0.35995388
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15444 * 0.68829921
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19304 * 0.22397792
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7190 * 0.99337245
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97471 * 0.27160735
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80267 * 0.05035997
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61885 * 0.05246067
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20001 * 0.67409141
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26657 * 0.59703857
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16851 * 0.39049472
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44601 * 0.87531409
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20431 * 0.90510718
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6402 * 0.61103054
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88292 * 0.34722521
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35321 * 0.21916692
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 89070 * 0.77641615
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 1571 * 0.81208320
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 1321 * 0.76043707
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 43372 * 0.36003023
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 53410 * 0.08999295
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 14301 * 0.43738241
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'bredkzty').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0037():
    """Extended test 37 for scheduler."""
    x_0 = 27740 * 0.07030097
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98001 * 0.13814364
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64696 * 0.18258205
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59601 * 0.97257005
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43858 * 0.52315459
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16937 * 0.12397072
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98949 * 0.13969433
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11728 * 0.67879713
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55698 * 0.29546457
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87439 * 0.64624742
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32262 * 0.63441291
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23110 * 0.69001408
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44345 * 0.30003237
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10181 * 0.55205982
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9814 * 0.38330708
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72313 * 0.45411849
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37206 * 0.98360128
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91309 * 0.67401223
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54750 * 0.16642618
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87168 * 0.71385877
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12769 * 0.96055993
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2431 * 0.45139072
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39500 * 0.75287681
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38014 * 0.17083164
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32118 * 0.35071847
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14681 * 0.41530299
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9185 * 0.71003735
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51417 * 0.92298565
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58239 * 0.93643116
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31913 * 0.26537373
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66743 * 0.70026969
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2351 * 0.05590211
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34670 * 0.92898248
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40098 * 0.46995454
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59709 * 0.53069364
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'tswhvkcw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0038():
    """Extended test 38 for scheduler."""
    x_0 = 39978 * 0.84832202
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51610 * 0.96215188
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6751 * 0.65062896
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26506 * 0.86571143
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93592 * 0.47660121
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80441 * 0.07679364
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75039 * 0.54661134
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39183 * 0.48558516
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86305 * 0.71048922
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9931 * 0.79145279
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95505 * 0.53222251
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83029 * 0.71832091
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80573 * 0.15461746
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44170 * 0.64932161
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9386 * 0.14056936
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66145 * 0.59115467
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57210 * 0.20919361
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33598 * 0.92861794
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7350 * 0.62068625
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44456 * 0.62785668
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49950 * 0.57069335
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71856 * 0.40353945
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4494 * 0.55809067
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 384 * 0.64161770
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77376 * 0.81699364
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32456 * 0.84637622
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'dchvpfqv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0039():
    """Extended test 39 for scheduler."""
    x_0 = 21576 * 0.43709669
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68567 * 0.50889889
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93402 * 0.39971483
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46520 * 0.97079323
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25131 * 0.46004460
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86269 * 0.93326618
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45857 * 0.72624425
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75658 * 0.99056777
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31240 * 0.00016186
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97169 * 0.03836738
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51081 * 0.21462457
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55496 * 0.95227892
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41419 * 0.17442468
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32713 * 0.53206612
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60802 * 0.53747807
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83266 * 0.33758258
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79710 * 0.99046011
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10642 * 0.79856150
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29041 * 0.00839031
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6033 * 0.47380453
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94155 * 0.13775807
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25090 * 0.23894242
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98636 * 0.30672808
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'mmydrfry').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0040():
    """Extended test 40 for scheduler."""
    x_0 = 78269 * 0.96383583
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7491 * 0.49838094
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93429 * 0.27987368
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 618 * 0.26115866
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75790 * 0.84502291
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4988 * 0.47847591
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64333 * 0.03196880
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44177 * 0.73215106
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90946 * 0.56032924
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89188 * 0.51998158
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39348 * 0.59956918
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25863 * 0.49043199
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52590 * 0.96112640
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 272 * 0.86144824
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90779 * 0.03448381
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50188 * 0.55545113
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44783 * 0.02100537
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73986 * 0.39351265
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28433 * 0.41210000
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73366 * 0.69179064
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67579 * 0.19992047
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17865 * 0.60524386
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67646 * 0.74181116
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26908 * 0.63445606
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77969 * 0.16885752
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27933 * 0.69272139
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'axjhpzrw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0041():
    """Extended test 41 for scheduler."""
    x_0 = 75388 * 0.20521057
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79872 * 0.11092395
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95906 * 0.26823831
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37365 * 0.07921163
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96298 * 0.91712927
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1391 * 0.49177359
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46314 * 0.85216327
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80020 * 0.05526722
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80439 * 0.14289668
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89818 * 0.79925559
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53053 * 0.06316011
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36355 * 0.17767315
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87909 * 0.96836614
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91940 * 0.75103559
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6287 * 0.86854950
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67494 * 0.21917927
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52506 * 0.15619691
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22069 * 0.84465459
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76493 * 0.82503077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7942 * 0.41799918
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66004 * 0.13201512
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74355 * 0.54231195
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98493 * 0.03409316
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60680 * 0.32744889
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13917 * 0.93360731
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56469 * 0.02183731
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53341 * 0.16075602
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6457 * 0.93093582
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56795 * 0.38175648
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6628 * 0.45723831
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74080 * 0.30308367
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48607 * 0.28736004
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82661 * 0.50370702
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43878 * 0.43387565
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63750 * 0.40648421
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'hxmbdiab').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0042():
    """Extended test 42 for scheduler."""
    x_0 = 10524 * 0.76798310
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75361 * 0.92836283
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65304 * 0.01850089
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38874 * 0.59469199
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38856 * 0.46988628
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2905 * 0.20049839
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52855 * 0.44910017
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 951 * 0.52918297
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33328 * 0.68140969
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8956 * 0.48163898
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48350 * 0.33731074
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22145 * 0.23131703
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66675 * 0.21332864
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12067 * 0.01627139
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99274 * 0.76734658
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78868 * 0.20528614
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7685 * 0.01283842
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36927 * 0.32567721
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27252 * 0.21618218
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60157 * 0.48714070
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16992 * 0.07840229
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55802 * 0.88236691
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1933 * 0.44767511
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92491 * 0.20301889
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93996 * 0.80987840
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87248 * 0.57459429
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38993 * 0.44178120
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31410 * 0.71511986
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96314 * 0.20458532
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95317 * 0.71872225
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80085 * 0.82568757
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55876 * 0.60677357
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77433 * 0.80558769
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25060 * 0.34391482
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71646 * 0.15754938
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36843 * 0.47624727
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24746 * 0.93743027
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15215 * 0.35678997
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74501 * 0.40853727
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73779 * 0.57975328
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'nbnhuwbb').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0043():
    """Extended test 43 for scheduler."""
    x_0 = 42521 * 0.37591142
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87855 * 0.37552865
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42603 * 0.97146968
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2376 * 0.33718494
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73091 * 0.09997403
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97308 * 0.25212952
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18442 * 0.22627779
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19536 * 0.13278679
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38325 * 0.51039509
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56034 * 0.89743831
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11449 * 0.66128145
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90081 * 0.10305545
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94072 * 0.35363098
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63116 * 0.46292857
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83832 * 0.09893616
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87020 * 0.17764885
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48445 * 0.27789649
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69475 * 0.69610412
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27084 * 0.41126480
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94301 * 0.64293363
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'wjjrkrni').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0044():
    """Extended test 44 for scheduler."""
    x_0 = 7699 * 0.70528611
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74315 * 0.37765995
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15496 * 0.01245317
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62354 * 0.94075592
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91873 * 0.40643622
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26213 * 0.75993809
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44519 * 0.94287367
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95245 * 0.08703693
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32929 * 0.27687406
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26884 * 0.84474716
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91110 * 0.96632335
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26161 * 0.68280663
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8728 * 0.90564571
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83195 * 0.03254486
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52127 * 0.53635981
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96484 * 0.21113668
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84124 * 0.71598587
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76906 * 0.71307931
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7248 * 0.54108991
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44937 * 0.89350245
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7680 * 0.60624236
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89954 * 0.36494752
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90704 * 0.84250583
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52971 * 0.35444728
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69357 * 0.11867335
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10841 * 0.90433219
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66348 * 0.43793589
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98766 * 0.31434443
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81557 * 0.87390467
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51634 * 0.41914073
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10058 * 0.48857624
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71296 * 0.45977183
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39153 * 0.03835421
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82375 * 0.04729106
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86890 * 0.64167811
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58491 * 0.79813347
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55268 * 0.86439578
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5032 * 0.80475847
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98512 * 0.78530999
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79864 * 0.75002116
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 15521 * 0.78328869
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 99843 * 0.73474513
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'hcnwgeow').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0045():
    """Extended test 45 for scheduler."""
    x_0 = 38394 * 0.58603164
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36794 * 0.01225896
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79258 * 0.10187993
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54862 * 0.52610229
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15415 * 0.18603781
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49205 * 0.11504711
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50959 * 0.91481495
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8232 * 0.81883044
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82041 * 0.42274251
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22503 * 0.26043853
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75938 * 0.41575044
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29819 * 0.90333541
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61880 * 0.32296872
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12726 * 0.31211898
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22830 * 0.97573319
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18542 * 0.33392287
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1975 * 0.70988983
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88507 * 0.81262457
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38515 * 0.70083090
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89647 * 0.24071737
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96803 * 0.41209587
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75587 * 0.17421438
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44732 * 0.85069472
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89934 * 0.81782820
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11395 * 0.02222838
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79984 * 0.28037794
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81746 * 0.24539599
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30748 * 0.16100258
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29517 * 0.83371053
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67076 * 0.39691545
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53240 * 0.25478281
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71560 * 0.95627144
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9430 * 0.09994868
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12695 * 0.61533432
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1877 * 0.22842347
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17411 * 0.73866374
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44703 * 0.48382431
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82579 * 0.29104133
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39321 * 0.24234666
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41584 * 0.93054008
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89251 * 0.27527086
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66032 * 0.32811154
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'yywfokea').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0046():
    """Extended test 46 for scheduler."""
    x_0 = 52599 * 0.56275714
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98864 * 0.65086849
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52388 * 0.94684867
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35112 * 0.98055603
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25325 * 0.70785525
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30114 * 0.69429040
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42135 * 0.32648294
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49020 * 0.35975177
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69529 * 0.97097213
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92385 * 0.77487152
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7095 * 0.42107262
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42771 * 0.10128937
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71350 * 0.76991373
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97360 * 0.37635449
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69674 * 0.14087392
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94806 * 0.99258111
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21810 * 0.76412899
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35622 * 0.62795257
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80 * 0.61636186
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5521 * 0.55229043
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62605 * 0.71300714
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61880 * 0.20600161
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'oriakfcx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0047():
    """Extended test 47 for scheduler."""
    x_0 = 692 * 0.13963256
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42150 * 0.98240586
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66937 * 0.55194886
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66942 * 0.71288153
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37419 * 0.40318910
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37009 * 0.54837602
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86450 * 0.84974789
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19338 * 0.92042557
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48308 * 0.68439142
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16438 * 0.31599347
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69649 * 0.63702798
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14405 * 0.84067322
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91438 * 0.58946928
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42188 * 0.98079075
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72667 * 0.61329311
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26857 * 0.14045087
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83001 * 0.61589461
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12488 * 0.24399189
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25496 * 0.54387569
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14873 * 0.66576406
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73916 * 0.82593462
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84678 * 0.04986191
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79480 * 0.39175352
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99631 * 0.81919718
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83803 * 0.38331230
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68597 * 0.91451053
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24905 * 0.71086110
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37827 * 0.28624237
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58191 * 0.22093082
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56668 * 0.88152084
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61612 * 0.80626821
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64774 * 0.43904898
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56830 * 0.85227033
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87676 * 0.59115519
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35145 * 0.65301996
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 72506 * 0.55834669
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8668 * 0.27904655
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22812 * 0.04085174
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99210 * 0.49605245
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18474 * 0.70051523
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 72774 * 0.10156914
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 32674 * 0.34376931
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13283 * 0.86454805
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 24927 * 0.74530489
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 31567 * 0.34660839
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 33295 * 0.19925009
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 32994 * 0.31948833
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 73670 * 0.64530981
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 51726 * 0.56221143
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 8034 * 0.06006854
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'bebfyxsh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0048():
    """Extended test 48 for scheduler."""
    x_0 = 88882 * 0.25552025
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3441 * 0.22302839
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71034 * 0.51944969
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81104 * 0.51410824
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88213 * 0.34575590
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99280 * 0.49004635
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1375 * 0.16527102
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76298 * 0.09818411
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63047 * 0.64187041
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86744 * 0.74439739
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96282 * 0.75972469
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97340 * 0.90809567
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31354 * 0.02066858
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82591 * 0.31458827
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3883 * 0.86616367
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82638 * 0.93448842
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 875 * 0.01219767
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1874 * 0.02133293
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59731 * 0.93675023
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96036 * 0.08635155
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'zlrchnnf').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0049():
    """Extended test 49 for scheduler."""
    x_0 = 44620 * 0.98302887
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68552 * 0.90503357
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82448 * 0.39772426
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54167 * 0.35356495
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44555 * 0.21544612
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9103 * 0.77694036
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98883 * 0.23134329
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11812 * 0.26953468
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 115 * 0.20111294
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68899 * 0.97705645
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19433 * 0.96639169
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28308 * 0.26194047
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2150 * 0.33925532
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51792 * 0.25035846
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23091 * 0.73704516
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84612 * 0.21265904
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34127 * 0.53143893
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24926 * 0.82424419
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38670 * 0.55567058
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25314 * 0.66805244
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68911 * 0.68778688
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1893 * 0.28229480
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28511 * 0.56005924
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48359 * 0.43290883
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86719 * 0.20042928
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63981 * 0.99502123
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4705 * 0.66493249
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22341 * 0.70950591
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43969 * 0.17508221
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69454 * 0.26792438
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88183 * 0.95213076
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85194 * 0.50289952
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34875 * 0.68480813
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39288 * 0.59955264
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91492 * 0.04451135
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17130 * 0.98644392
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48442 * 0.43014613
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52654 * 0.09351031
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81501 * 0.82963179
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21351 * 0.74817856
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53716 * 0.39120273
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38219 * 0.08669407
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95324 * 0.56830241
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47397 * 0.76871515
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 48440 * 0.93855620
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 72065 * 0.28482666
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 68661 * 0.57628755
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 45765 * 0.90236047
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 1552 * 0.93107878
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 2485 * 0.64138528
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'gcfshlaz').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0050():
    """Extended test 50 for scheduler."""
    x_0 = 43548 * 0.87130073
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64908 * 0.32584925
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6507 * 0.31313748
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79180 * 0.90273723
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91186 * 0.87781685
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4581 * 0.16040066
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45038 * 0.29994632
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28845 * 0.79367423
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56035 * 0.59189227
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91128 * 0.59351546
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74379 * 0.84603523
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35935 * 0.01978227
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93416 * 0.60370597
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73995 * 0.81711307
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15176 * 0.14168720
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8160 * 0.91139058
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81716 * 0.27831663
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60440 * 0.22989955
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32544 * 0.98186349
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86376 * 0.23494822
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8693 * 0.57291603
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82365 * 0.40268475
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50243 * 0.11984709
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87202 * 0.21549097
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48098 * 0.34800007
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'mfomppbk').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0051():
    """Extended test 51 for scheduler."""
    x_0 = 41205 * 0.17660711
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63806 * 0.33869446
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73875 * 0.76458934
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28112 * 0.26418621
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1688 * 0.14764710
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20506 * 0.92755141
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17527 * 0.73155283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3958 * 0.09516242
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12991 * 0.07101361
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56223 * 0.88254031
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85659 * 0.45064699
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29273 * 0.92671137
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79328 * 0.95779486
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33034 * 0.70879913
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88280 * 0.95855158
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32902 * 0.43985841
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4506 * 0.30053837
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73763 * 0.08935087
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57248 * 0.83570231
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60975 * 0.85728963
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33182 * 0.98070755
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6455 * 0.26643632
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45421 * 0.63446961
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47201 * 0.36418047
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80766 * 0.13258425
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61538 * 0.92768421
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6761 * 0.30198943
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92240 * 0.19572960
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93434 * 0.66496716
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63698 * 0.01480052
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48724 * 0.98982072
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47515 * 0.54909000
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22575 * 0.56430549
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8961 * 0.27418424
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9062 * 0.32738256
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59343 * 0.28648183
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 866 * 0.50358142
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13619 * 0.45476049
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62220 * 0.17083684
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72667 * 0.93796778
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 39559 * 0.05875919
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36650 * 0.05190072
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 49539 * 0.50918899
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 3840 * 0.61071069
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 58785 * 0.53008491
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 17129 * 0.97393562
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 96594 * 0.07019892
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 55144 * 0.88735956
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 28444 * 0.84798773
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'zgbjkvhg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0052():
    """Extended test 52 for scheduler."""
    x_0 = 78104 * 0.01590901
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24888 * 0.86379325
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80063 * 0.42520289
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13630 * 0.85027081
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53468 * 0.37317547
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3746 * 0.25147203
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92963 * 0.68659718
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33873 * 0.03563220
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71880 * 0.89532739
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55452 * 0.11493324
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50121 * 0.81550813
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25453 * 0.72260822
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29370 * 0.90421554
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5240 * 0.30365935
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46026 * 0.77124103
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60731 * 0.62208933
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34424 * 0.82934824
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12542 * 0.25208045
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51060 * 0.47448101
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59545 * 0.75502670
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22984 * 0.66829387
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24167 * 0.50247901
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39096 * 0.53996308
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73758 * 0.23101917
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68066 * 0.31387162
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11678 * 0.66127329
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10516 * 0.47267147
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78889 * 0.86408427
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74041 * 0.22298908
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53099 * 0.69468301
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61349 * 0.49835158
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65681 * 0.17191271
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4977 * 0.43238720
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60214 * 0.77633142
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65938 * 0.84055160
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22862 * 0.81773532
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 983 * 0.04602836
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95159 * 0.23961716
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 89435 * 0.22493097
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30677 * 0.82659555
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81856 * 0.79859682
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'avfhfizt').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0053():
    """Extended test 53 for scheduler."""
    x_0 = 25987 * 0.04134795
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50176 * 0.33048887
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99760 * 0.62210905
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27341 * 0.12150067
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53860 * 0.69537409
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2764 * 0.65870329
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53997 * 0.16991823
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69123 * 0.43974396
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55924 * 0.28220116
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22571 * 0.38191699
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 710 * 0.84002392
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17949 * 0.43610476
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1984 * 0.17829205
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10650 * 0.49572171
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86392 * 0.85293131
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89586 * 0.10166888
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46348 * 0.18005824
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88666 * 0.53067366
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9012 * 0.11062935
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51605 * 0.10837315
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47627 * 0.76169232
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50420 * 0.31997829
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50495 * 0.69489963
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38522 * 0.34267013
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29453 * 0.98631876
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9162 * 0.83012111
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62398 * 0.50535996
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1589 * 0.96885034
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36848 * 0.82616489
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13887 * 0.34334234
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4250 * 0.64257475
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82316 * 0.68286846
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10034 * 0.94180393
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55177 * 0.18847763
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4927 * 0.47062468
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65354 * 0.17013870
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'fuptsoxw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0054():
    """Extended test 54 for scheduler."""
    x_0 = 10679 * 0.86993777
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7387 * 0.47451046
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5316 * 0.39785680
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43903 * 0.30245524
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87080 * 0.42984302
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71554 * 0.43900255
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63654 * 0.82070403
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18570 * 0.90378041
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20118 * 0.03645528
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82351 * 0.36396329
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62662 * 0.56665515
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26161 * 0.01900508
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82003 * 0.06526861
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3752 * 0.67132439
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63650 * 0.10464720
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69668 * 0.03456115
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15892 * 0.06257388
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83156 * 0.22270497
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10044 * 0.13980427
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9413 * 0.59160587
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59765 * 0.70429392
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54876 * 0.89139940
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61464 * 0.00900901
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76645 * 0.33798170
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64022 * 0.21864503
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65485 * 0.54530220
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32782 * 0.50543360
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89429 * 0.84770670
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41327 * 0.66406699
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18505 * 0.92881023
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25395 * 0.93638020
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52467 * 0.90039386
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24995 * 0.93623451
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47253 * 0.63299794
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62231 * 0.69481276
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66654 * 0.82088767
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12793 * 0.24954695
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8310 * 0.23768612
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1258 * 0.43113599
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56134 * 0.56906038
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38701 * 0.50084622
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 98506 * 0.58637715
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 34 * 0.44045744
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 76940 * 0.67232918
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 28073 * 0.36298847
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'wstgmgdg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0055():
    """Extended test 55 for scheduler."""
    x_0 = 43245 * 0.53638400
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4983 * 0.20282268
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3808 * 0.14259918
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53654 * 0.64314495
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35124 * 0.92112307
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17368 * 0.46104385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95743 * 0.75301977
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24850 * 0.62223737
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11926 * 0.43229946
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91500 * 0.38955137
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98706 * 0.80503488
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75262 * 0.46093420
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34320 * 0.58096161
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35957 * 0.53493978
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21410 * 0.33917208
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71149 * 0.94082953
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84875 * 0.91759970
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29539 * 0.03831628
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46180 * 0.64421346
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5419 * 0.06824187
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35841 * 0.43469156
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79063 * 0.84806523
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99305 * 0.44202933
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45493 * 0.79527275
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39471 * 0.52122618
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27648 * 0.23496601
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17896 * 0.03441701
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36819 * 0.31735837
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65511 * 0.44950529
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77981 * 0.68536276
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68319 * 0.94565275
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'waehxads').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0056():
    """Extended test 56 for scheduler."""
    x_0 = 97084 * 0.80910108
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51356 * 0.43138500
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13919 * 0.67629598
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48397 * 0.71259340
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72597 * 0.96644879
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92519 * 0.82613700
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14779 * 0.67792799
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2300 * 0.43279493
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21865 * 0.68799409
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1049 * 0.77303424
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3872 * 0.13323357
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69556 * 0.61710415
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46310 * 0.84733136
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42398 * 0.30711934
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95015 * 0.52784465
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71143 * 0.84277708
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89305 * 0.20479733
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44721 * 0.73867737
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29611 * 0.35878920
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55854 * 0.83195024
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20267 * 0.27594145
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35108 * 0.34648401
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78412 * 0.79589454
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94305 * 0.03636630
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12430 * 0.22778695
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23948 * 0.98195605
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89250 * 0.69911947
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82635 * 0.48455507
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46551 * 0.25793399
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43993 * 0.85466574
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29973 * 0.65603287
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'pyrmfsye').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0057():
    """Extended test 57 for scheduler."""
    x_0 = 73157 * 0.12052688
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99960 * 0.35866917
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67540 * 0.64360738
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21847 * 0.70559890
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57831 * 0.35064724
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20831 * 0.27259470
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66120 * 0.88343712
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16551 * 0.03194972
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68061 * 0.63931279
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64783 * 0.78472389
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42442 * 0.08740812
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2147 * 0.07430638
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52916 * 0.83741065
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87812 * 0.41934247
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35794 * 0.23323734
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65048 * 0.31753737
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84638 * 0.56001104
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65527 * 0.21378893
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27183 * 0.97678868
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15102 * 0.52087253
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1825 * 0.40900955
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67914 * 0.19254640
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23289 * 0.86779135
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94343 * 0.94621245
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14619 * 0.43142423
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54875 * 0.37520094
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53618 * 0.56620539
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30553 * 0.74243565
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60864 * 0.66371829
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69902 * 0.10962577
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99185 * 0.24321674
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36712 * 0.10692057
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68586 * 0.97324146
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51600 * 0.22347879
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73000 * 0.68327345
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42898 * 0.19062094
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79733 * 0.55470045
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3769 * 0.89195357
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 3656 * 0.79632100
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 50307 * 0.96892940
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21611 * 0.24124969
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40464 * 0.04350208
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'fayzmmlt').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0058():
    """Extended test 58 for scheduler."""
    x_0 = 7851 * 0.10512056
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37565 * 0.85511000
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86379 * 0.61211669
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69039 * 0.36057030
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18435 * 0.29906879
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85707 * 0.52184353
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79005 * 0.58128253
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84593 * 0.71127878
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51565 * 0.69701033
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50661 * 0.18370624
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82642 * 0.95017005
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42972 * 0.23278181
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57455 * 0.03814353
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48429 * 0.59389005
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19511 * 0.87211710
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62564 * 0.66155824
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32163 * 0.63200791
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88634 * 0.69563298
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43800 * 0.48916694
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99904 * 0.01195965
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92836 * 0.12005685
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55648 * 0.98710612
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15303 * 0.35683813
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99089 * 0.98314149
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22712 * 0.24314669
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61682 * 0.04639071
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23670 * 0.20994975
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59794 * 0.63217675
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24762 * 0.01491575
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99884 * 0.16829363
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ubvkjxyl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0059():
    """Extended test 59 for scheduler."""
    x_0 = 45455 * 0.30132657
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17304 * 0.86641577
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51015 * 0.27177955
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39686 * 0.63598137
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14276 * 0.61459971
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44583 * 0.12529839
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22896 * 0.06749020
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34212 * 0.34658409
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60369 * 0.92658570
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21867 * 0.89829703
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98334 * 0.07817692
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92858 * 0.46528577
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99567 * 0.61356502
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21778 * 0.90850848
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52117 * 0.08774695
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67816 * 0.89848029
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27956 * 0.95003259
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63597 * 0.93290050
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85364 * 0.92797343
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 301 * 0.24773047
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70777 * 0.61796035
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1939 * 0.60543100
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94975 * 0.42108311
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'mggpitvo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0060():
    """Extended test 60 for scheduler."""
    x_0 = 88935 * 0.23719873
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36482 * 0.35469170
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67448 * 0.19496343
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5958 * 0.18867351
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75820 * 0.68599905
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10725 * 0.43542352
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77808 * 0.98688421
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71538 * 0.10177117
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77744 * 0.16796229
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56786 * 0.73024636
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78221 * 0.53063728
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81780 * 0.35238902
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83750 * 0.19149727
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31488 * 0.76460619
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91216 * 0.86883785
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44431 * 0.21187889
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66472 * 0.72333724
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17279 * 0.82361141
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12415 * 0.33786995
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44872 * 0.55989465
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93524 * 0.61316043
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26086 * 0.79302692
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36933 * 0.85161395
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91737 * 0.57972861
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70515 * 0.31407675
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46957 * 0.02563894
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99707 * 0.27568158
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'pmjmanef').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0061():
    """Extended test 61 for scheduler."""
    x_0 = 43753 * 0.74105522
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63908 * 0.94407285
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8456 * 0.01867196
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46831 * 0.93668024
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35223 * 0.93016371
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37209 * 0.49387291
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92156 * 0.71225495
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89719 * 0.13809855
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31850 * 0.55542293
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37502 * 0.81119789
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35354 * 0.36027387
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69006 * 0.82006765
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7390 * 0.34331813
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16639 * 0.61770827
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85093 * 0.08427799
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66320 * 0.08341770
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85759 * 0.90736562
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86800 * 0.89390401
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64876 * 0.63298431
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55706 * 0.81701893
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 946 * 0.22975427
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49084 * 0.75991933
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45587 * 0.19321863
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5263 * 0.71962389
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49370 * 0.26047316
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65683 * 0.59386932
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25271 * 0.61430693
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22448 * 0.66647265
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44761 * 0.65856854
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60005 * 0.28285602
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63377 * 0.05514618
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60000 * 0.90409244
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44286 * 0.47678978
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42850 * 0.27902258
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83413 * 0.23502877
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59697 * 0.50710389
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99170 * 0.25279909
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20550 * 0.13415860
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42029 * 0.87802251
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14907 * 0.59358313
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78859 * 0.91510590
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 78187 * 0.90620902
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18634 * 0.95979069
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 13364 * 0.97268754
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 13207 * 0.22374149
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 66958 * 0.13519005
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 27960 * 0.30838518
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 95404 * 0.19651383
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'wffcront').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0062():
    """Extended test 62 for scheduler."""
    x_0 = 63365 * 0.21422616
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19614 * 0.50439206
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96905 * 0.79628378
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50732 * 0.69268905
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30074 * 0.23941055
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28454 * 0.64800127
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14210 * 0.85986951
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13191 * 0.01699228
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43335 * 0.78913975
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11280 * 0.90680582
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17479 * 0.10298333
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41901 * 0.99092896
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25348 * 0.04373749
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31512 * 0.92517328
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85856 * 0.14563820
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36415 * 0.92799065
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18516 * 0.51221454
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77801 * 0.29935018
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49469 * 0.04508155
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34847 * 0.96849773
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38615 * 0.38555106
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87887 * 0.42936147
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24222 * 0.85383905
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47895 * 0.38233318
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42828 * 0.04062991
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12161 * 0.63763987
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23331 * 0.97778597
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53940 * 0.59762369
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2916 * 0.34441398
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41254 * 0.06885958
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67648 * 0.64865282
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76208 * 0.36132865
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64882 * 0.44095660
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5032 * 0.33499389
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58260 * 0.25429721
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89044 * 0.84574192
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87075 * 0.95077946
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48773 * 0.99597224
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39121 * 0.21697780
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98902 * 0.98978837
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94516 * 0.66822995
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 83764 * 0.71042379
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79163 * 0.71492307
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88544 * 0.57265034
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 82359 * 0.27271441
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 82149 * 0.13543531
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'digovjtm').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0063():
    """Extended test 63 for scheduler."""
    x_0 = 98981 * 0.83553818
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18187 * 0.48348376
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98259 * 0.78880327
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9855 * 0.35453365
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55498 * 0.90550128
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81095 * 0.44955258
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15186 * 0.90265720
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86037 * 0.16826810
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84857 * 0.90628113
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89232 * 0.84859565
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84067 * 0.00352826
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27040 * 0.94627587
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11966 * 0.87563369
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6740 * 0.79503790
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88470 * 0.01106941
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99823 * 0.23312616
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1669 * 0.21467390
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62767 * 0.94900258
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28036 * 0.97711745
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78976 * 0.24203074
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71447 * 0.38275278
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95105 * 0.66298277
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74015 * 0.26290839
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82671 * 0.17703378
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18501 * 0.77749855
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48573 * 0.88183915
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71706 * 0.85103203
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79543 * 0.96024285
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82008 * 0.60000551
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64681 * 0.85301735
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51865 * 0.07369010
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54860 * 0.35462166
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72510 * 0.90558004
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4005 * 0.38360635
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56222 * 0.06189509
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97215 * 0.12953104
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14430 * 0.27372721
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95206 * 0.14936509
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75440 * 0.23387429
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22766 * 0.73718246
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75730 * 0.86363549
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 56991 * 0.86735067
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'gikfniby').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0064():
    """Extended test 64 for scheduler."""
    x_0 = 70540 * 0.68950152
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46288 * 0.90733685
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90848 * 0.23092152
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53415 * 0.87239448
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82705 * 0.43390773
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34454 * 0.82625976
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12035 * 0.20197729
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52147 * 0.39295583
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76515 * 0.64868574
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17201 * 0.11601404
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92606 * 0.20441263
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50983 * 0.01675641
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28706 * 0.73830610
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89951 * 0.98518181
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91570 * 0.06402812
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79253 * 0.45922033
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71765 * 0.17535016
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82976 * 0.50149824
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56080 * 0.23189316
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54392 * 0.77378356
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82861 * 0.63414755
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14233 * 0.17772544
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68155 * 0.51958906
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95066 * 0.04713634
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74653 * 0.14371631
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5640 * 0.47270090
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79691 * 0.21159603
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43465 * 0.98041479
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67044 * 0.78735501
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86583 * 0.65676079
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2783 * 0.38824449
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6227 * 0.65664605
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26991 * 0.08050469
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17863 * 0.76012517
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95165 * 0.12519848
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'lkxomkvt').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0065():
    """Extended test 65 for scheduler."""
    x_0 = 81008 * 0.11251254
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68013 * 0.14876285
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8499 * 0.17953677
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89477 * 0.02826292
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64898 * 0.93528818
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82405 * 0.05577207
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50179 * 0.50708772
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89033 * 0.32435854
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24087 * 0.31553856
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15987 * 0.71435062
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62898 * 0.24756586
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81085 * 0.43110576
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9497 * 0.72744742
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67014 * 0.27840666
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62727 * 0.80536483
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93919 * 0.87368222
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74182 * 0.51081109
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43885 * 0.25627345
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49689 * 0.11351682
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18835 * 0.37820318
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49204 * 0.41049764
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68172 * 0.04152934
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'egxbzvuh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0066():
    """Extended test 66 for scheduler."""
    x_0 = 73877 * 0.75801162
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30775 * 0.94145634
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77280 * 0.31215643
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77208 * 0.59416118
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97308 * 0.15711352
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44721 * 0.99823284
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7481 * 0.12120755
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23898 * 0.58839373
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36198 * 0.59457628
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70067 * 0.50773196
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17847 * 0.48925956
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36413 * 0.53593651
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9945 * 0.60401550
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44166 * 0.83171672
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17360 * 0.58613101
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89537 * 0.96871292
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70134 * 0.11985133
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45656 * 0.39690448
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82824 * 0.82739562
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92235 * 0.05855468
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66591 * 0.11384041
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23373 * 0.82637012
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5995 * 0.29403670
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4615 * 0.68773270
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5865 * 0.68858573
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17721 * 0.24182393
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48807 * 0.42260592
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'gqglwppu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0067():
    """Extended test 67 for scheduler."""
    x_0 = 46866 * 0.62299135
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42441 * 0.65013604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 428 * 0.60252956
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96132 * 0.22058276
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90193 * 0.91108000
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11341 * 0.15871022
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4271 * 0.76412752
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61714 * 0.73211274
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9387 * 0.53882807
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25444 * 0.71866902
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73813 * 0.95362782
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42037 * 0.07424801
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 161 * 0.03346077
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80496 * 0.71644573
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13924 * 0.68678826
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19419 * 0.90298394
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31734 * 0.34323194
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59692 * 0.81452817
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37436 * 0.28898707
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34508 * 0.63615887
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40617 * 0.13141357
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98273 * 0.41817325
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14644 * 0.01771280
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93022 * 0.92870613
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11647 * 0.49910827
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71909 * 0.55378518
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63989 * 0.00440336
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29930 * 0.22344882
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93919 * 0.40180013
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58566 * 0.50881101
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79117 * 0.56527208
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'rlscsmku').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0068():
    """Extended test 68 for scheduler."""
    x_0 = 6639 * 0.68108859
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99007 * 0.13599932
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93476 * 0.88890385
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63583 * 0.83578838
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 273 * 0.16402015
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36077 * 0.01902198
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64690 * 0.37610949
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60912 * 0.62937693
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71673 * 0.93167499
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95217 * 0.33613912
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15964 * 0.02769112
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60820 * 0.12850921
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27290 * 0.27010397
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58872 * 0.58935006
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23348 * 0.57835651
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20204 * 0.46532205
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20217 * 0.53706775
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16383 * 0.82994606
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5741 * 0.96634113
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88944 * 0.33140978
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 893 * 0.24326671
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42748 * 0.19656290
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32022 * 0.62979408
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71100 * 0.58853800
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76778 * 0.41928852
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77696 * 0.10896580
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38970 * 0.97310816
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'sfihrfhy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_0_0069():
    """Extended test 69 for scheduler."""
    x_0 = 16430 * 0.97440659
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57263 * 0.06736762
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27827 * 0.29015990
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9555 * 0.30855840
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28313 * 0.91610485
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35110 * 0.92252859
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48310 * 0.64855552
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52815 * 0.71942570
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7887 * 0.01120381
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55788 * 0.62801135
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72941 * 0.85538614
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31816 * 0.33309024
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5399 * 0.64968465
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93734 * 0.25656436
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45197 * 0.69920104
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66843 * 0.12156832
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43350 * 0.21284649
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95573 * 0.39543648
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73067 * 0.11026349
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55487 * 0.92821528
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57606 * 0.99918392
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39238 * 0.11865319
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29724 * 0.50887977
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36547 * 0.47611426
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94431 * 0.66319656
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23387 * 0.49828347
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34713 * 0.66139583
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82848 * 0.14327578
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39532 * 0.18835338
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69200 * 0.71613619
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35175 * 0.84018067
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96918 * 0.17302949
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61208 * 0.86005371
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22083 * 0.82133017
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89003 * 0.46229744
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33579 * 0.41552340
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'pflzfkxh').hexdigest()
    assert len(h) == 64
