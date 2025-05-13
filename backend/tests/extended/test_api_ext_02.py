"""Extended tests for api suite 2."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_api_extended_2_0000():
    """Extended test 0 for api."""
    x_0 = 39480 * 0.26741627
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82532 * 0.62883205
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20976 * 0.55619336
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54005 * 0.51147078
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39940 * 0.78789711
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6320 * 0.98538127
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54007 * 0.67670686
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10372 * 0.38087998
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 675 * 0.77893955
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20837 * 0.14972282
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92209 * 0.18334995
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74008 * 0.40180937
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44772 * 0.35305802
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83199 * 0.72272614
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95668 * 0.33293698
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77280 * 0.71197662
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21450 * 0.16081145
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99488 * 0.43189567
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69204 * 0.74058501
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48125 * 0.34818645
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6567 * 0.83397615
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84641 * 0.72022306
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99081 * 0.98291698
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33192 * 0.78735762
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41674 * 0.17397770
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3719 * 0.55015260
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54426 * 0.37578961
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50329 * 0.75040955
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24480 * 0.44592150
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50462 * 0.82279941
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'enjlgerl').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0001():
    """Extended test 1 for api."""
    x_0 = 83737 * 0.92402158
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39047 * 0.87805784
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73957 * 0.39356484
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31497 * 0.06206826
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7926 * 0.34175486
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53301 * 0.63395127
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10967 * 0.49611477
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53147 * 0.31899160
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63981 * 0.61955796
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74621 * 0.69259519
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37516 * 0.40137431
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72404 * 0.42422642
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89594 * 0.76219763
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26365 * 0.26912382
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28042 * 0.30542374
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32081 * 0.03899384
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62612 * 0.77026601
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82867 * 0.33022192
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75545 * 0.06206287
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31147 * 0.92719802
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61672 * 0.15845833
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90346 * 0.73347403
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33471 * 0.90394727
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35888 * 0.13616073
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94934 * 0.86373304
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51859 * 0.39446930
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60002 * 0.69157890
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92716 * 0.53598791
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98497 * 0.37770281
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23957 * 0.93809925
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39561 * 0.90020476
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60410 * 0.98770565
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40836 * 0.44551708
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2924 * 0.19345080
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23897 * 0.65956274
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'yqojypdg').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0002():
    """Extended test 2 for api."""
    x_0 = 25069 * 0.85982175
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74483 * 0.02337421
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78361 * 0.16868285
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10205 * 0.94851087
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40543 * 0.92025800
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91970 * 0.17107679
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49480 * 0.56932747
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79344 * 0.93581856
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11091 * 0.18222261
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4229 * 0.86275938
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76040 * 0.09259540
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61500 * 0.13408096
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79616 * 0.25331399
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92869 * 0.22338588
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60005 * 0.90447194
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32286 * 0.69548382
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84367 * 0.36834865
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12402 * 0.84313113
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87705 * 0.14702798
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6204 * 0.36748240
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85833 * 0.15369620
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88241 * 0.48660828
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84463 * 0.90082247
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86414 * 0.61761697
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82403 * 0.74855691
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58668 * 0.99910809
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37173 * 0.93448848
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5409 * 0.03850520
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15260 * 0.72701306
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43623 * 0.46617098
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54145 * 0.80308726
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88722 * 0.13245094
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3577 * 0.07425820
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95670 * 0.01892026
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4374 * 0.38300120
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15788 * 0.47608972
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13625 * 0.95688396
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68538 * 0.05376867
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47805 * 0.71069251
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82660 * 0.21791944
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42992 * 0.29549504
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 23929 * 0.77494682
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 45032 * 0.09670751
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 65884 * 0.64074635
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 75369 * 0.51941860
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 27855 * 0.56236291
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 78539 * 0.82913062
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 11753 * 0.65283634
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'gqyxtmvq').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0003():
    """Extended test 3 for api."""
    x_0 = 84028 * 0.19271681
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59942 * 0.28864646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87135 * 0.97370963
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85979 * 0.99153225
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23547 * 0.91753933
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95459 * 0.58867705
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97473 * 0.85421576
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50222 * 0.81056723
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29713 * 0.63651782
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72687 * 0.07623604
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63260 * 0.43549953
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61533 * 0.94136622
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96282 * 0.92601283
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20468 * 0.50139581
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96157 * 0.52005212
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54520 * 0.69672931
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45688 * 0.61277947
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97 * 0.03325504
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54586 * 0.02568443
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11613 * 0.61814543
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70761 * 0.23401262
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4634 * 0.73476796
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55247 * 0.91630523
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10198 * 0.20339586
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53003 * 0.97731065
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3173 * 0.96502481
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9662 * 0.79514701
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80154 * 0.87623488
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65731 * 0.29140350
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16108 * 0.05685956
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18231 * 0.17342253
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28413 * 0.67657717
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'gudilpfq').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0004():
    """Extended test 4 for api."""
    x_0 = 24902 * 0.15350453
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97309 * 0.78216942
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40354 * 0.39343958
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48289 * 0.68585376
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38523 * 0.26580915
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54600 * 0.62434302
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44725 * 0.42659187
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79157 * 0.28420722
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99071 * 0.87721669
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18966 * 0.82802507
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27242 * 0.03920656
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12757 * 0.95452982
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3602 * 0.07362018
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75370 * 0.24016834
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42891 * 0.66714425
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62604 * 0.71561949
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59081 * 0.67901292
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25259 * 0.98170607
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56464 * 0.52257660
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50951 * 0.57598396
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8751 * 0.78988595
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80498 * 0.01807843
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55032 * 0.13446959
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83999 * 0.16114708
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96739 * 0.87193219
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'wkflwfei').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0005():
    """Extended test 5 for api."""
    x_0 = 43567 * 0.13430884
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90372 * 0.68421803
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83707 * 0.73501132
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16453 * 0.83466662
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25631 * 0.44570201
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27886 * 0.55233477
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6785 * 0.91825525
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62331 * 0.42773712
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50908 * 0.63274640
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68292 * 0.32108259
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83179 * 0.94898207
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10989 * 0.06386626
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11938 * 0.96367072
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60487 * 0.14031482
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41343 * 0.27750120
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25331 * 0.90999269
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60598 * 0.64272741
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92487 * 0.82628204
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30075 * 0.23309903
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74070 * 0.81936219
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72329 * 0.41524275
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64905 * 0.95050060
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78542 * 0.60126944
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83588 * 0.93249204
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6126 * 0.01161862
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63084 * 0.87344184
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19865 * 0.20882476
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17644 * 0.96471145
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28619 * 0.02481960
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97871 * 0.24576309
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4382 * 0.81194005
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90337 * 0.22229620
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 643 * 0.72343801
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49143 * 0.83439898
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87080 * 0.85374160
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89716 * 0.12228251
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28024 * 0.33984162
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96943 * 0.27212118
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55686 * 0.94924084
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 12759 * 0.22743428
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 97524 * 0.12874062
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35019 * 0.38681830
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46983 * 0.47635165
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69964 * 0.81307403
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'mhakvymm').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0006():
    """Extended test 6 for api."""
    x_0 = 73819 * 0.44831287
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27926 * 0.46438073
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27558 * 0.74047574
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23560 * 0.49031856
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6870 * 0.59884002
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61928 * 0.17831539
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50610 * 0.90580239
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3566 * 0.36185969
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42922 * 0.64724395
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69504 * 0.92389761
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83629 * 0.81285908
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68143 * 0.08707805
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58431 * 0.62059734
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49647 * 0.85959427
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17871 * 0.48846913
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4109 * 0.07298325
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21479 * 0.31721618
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94309 * 0.81881020
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91447 * 0.12429946
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70187 * 0.01453413
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82229 * 0.41649117
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33668 * 0.88594083
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2221 * 0.94725105
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52781 * 0.01983578
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 789 * 0.76347046
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17716 * 0.64818019
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86020 * 0.41788690
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6578 * 0.34909406
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61100 * 0.05415186
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54678 * 0.72137892
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86469 * 0.48149923
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64382 * 0.17487307
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89082 * 0.46697232
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67619 * 0.68676727
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12031 * 0.18741153
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78815 * 0.08925532
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24523 * 0.33348289
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4415 * 0.18198623
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26403 * 0.41144087
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 78964 * 0.82856398
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43268 * 0.98099466
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71274 * 0.64186616
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75041 * 0.56957315
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97709 * 0.09717106
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 40743 * 0.93058098
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 565 * 0.54871150
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 55267 * 0.79725646
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 88267 * 0.14059253
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'vnoccumf').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0007():
    """Extended test 7 for api."""
    x_0 = 9906 * 0.32385168
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27629 * 0.41106261
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58837 * 0.03851804
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79128 * 0.98183667
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64503 * 0.03265810
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38348 * 0.91674354
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20291 * 0.44842451
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24213 * 0.79826091
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47198 * 0.57404212
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94840 * 0.22461985
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57994 * 0.60870584
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65904 * 0.93066433
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49250 * 0.78601678
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57867 * 0.65814143
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13882 * 0.93934914
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69679 * 0.52794499
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29161 * 0.79557989
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54664 * 0.23428758
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10727 * 0.96735316
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27271 * 0.25355920
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67187 * 0.27531864
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34767 * 0.64975942
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68439 * 0.92704569
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69213 * 0.87927531
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'tpmfbwcm').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0008():
    """Extended test 8 for api."""
    x_0 = 98944 * 0.76895832
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8189 * 0.16333632
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19638 * 0.19952831
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26595 * 0.09657683
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56232 * 0.12779074
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20420 * 0.83658478
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3085 * 0.39855070
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23821 * 0.84399000
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53267 * 0.50651191
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72629 * 0.32214769
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14437 * 0.11202636
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12391 * 0.39792422
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7096 * 0.40489700
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56633 * 0.67104243
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14112 * 0.05268342
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1122 * 0.08743822
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91453 * 0.77314048
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92806 * 0.66757718
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36572 * 0.91266265
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48846 * 0.65040874
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58876 * 0.92331645
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79845 * 0.70280453
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43128 * 0.84796251
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12540 * 0.17501682
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29384 * 0.86005464
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59198 * 0.21798041
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32243 * 0.73368280
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96112 * 0.00424539
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86580 * 0.16581773
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51571 * 0.10978171
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34435 * 0.56635315
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21359 * 0.79211373
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82914 * 0.26102045
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26187 * 0.92020444
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9508 * 0.55355468
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14907 * 0.48153280
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1430 * 0.92980374
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95319 * 0.93743998
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61550 * 0.25949524
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43644 * 0.79578012
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52442 * 0.34745446
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69798 * 0.00709621
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81119 * 0.72186994
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75419 * 0.46707316
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'zyssbvxh').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0009():
    """Extended test 9 for api."""
    x_0 = 88070 * 0.43961436
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92182 * 0.63543229
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8226 * 0.91765740
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8571 * 0.91338808
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24212 * 0.88562507
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78251 * 0.98903811
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84571 * 0.93564817
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96744 * 0.32678766
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31380 * 0.57084866
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23755 * 0.04568507
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28263 * 0.27928410
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77310 * 0.04295375
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12787 * 0.67036310
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54220 * 0.54387894
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85199 * 0.95954682
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14989 * 0.02199484
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99804 * 0.63227858
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71300 * 0.14926277
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7678 * 0.41377914
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84113 * 0.37170912
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34792 * 0.03048965
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17417 * 0.34215629
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14329 * 0.43285602
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84502 * 0.12393530
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85506 * 0.41781602
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86364 * 0.86169984
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21457 * 0.37743476
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47212 * 0.75980330
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76912 * 0.46084976
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31592 * 0.62339315
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90115 * 0.94677241
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40683 * 0.04904686
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66888 * 0.13594212
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55389 * 0.95850384
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32974 * 0.33122204
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91713 * 0.49850489
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43454 * 0.94579340
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90173 * 0.77485852
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67421 * 0.67564938
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15520 * 0.64401101
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23230 * 0.58768921
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 7203 * 0.84112041
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96555 * 0.90192887
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47274 * 0.11810011
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 47686 * 0.44078783
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 11199 * 0.46109720
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 88250 * 0.64554622
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 29253 * 0.31316583
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ioliwjfb').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0010():
    """Extended test 10 for api."""
    x_0 = 86591 * 0.05145035
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25030 * 0.89716313
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98976 * 0.68747637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94543 * 0.23717567
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89039 * 0.60832499
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35126 * 0.56315207
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8831 * 0.20925684
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 130 * 0.31934577
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25675 * 0.28956322
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75002 * 0.85016494
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6838 * 0.56258710
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27721 * 0.64596315
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20915 * 0.16093911
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1311 * 0.53882551
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8102 * 0.30238076
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85943 * 0.09004829
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69625 * 0.06926337
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87353 * 0.60948892
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82955 * 0.21540356
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31520 * 0.14497496
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55961 * 0.31262290
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11485 * 0.89933387
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76242 * 0.79480489
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30658 * 0.99249253
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22329 * 0.89684994
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1939 * 0.86103379
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34631 * 0.32202720
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41644 * 0.21020651
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31961 * 0.82806386
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'stgixkfn').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0011():
    """Extended test 11 for api."""
    x_0 = 88177 * 0.03617040
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96762 * 0.33425508
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29619 * 0.54943059
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99677 * 0.31502174
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9222 * 0.79228027
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91533 * 0.05654819
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18054 * 0.14931243
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7155 * 0.53241903
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82621 * 0.26813988
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16550 * 0.07450579
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87932 * 0.37154940
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47336 * 0.83482491
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7149 * 0.29930362
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40116 * 0.81799008
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6072 * 0.25836624
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88192 * 0.81527838
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64606 * 0.87806816
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85841 * 0.86463687
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23677 * 0.51971382
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52190 * 0.46789297
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52195 * 0.11766607
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55491 * 0.00651121
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7679 * 0.86520718
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85339 * 0.56140009
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14337 * 0.79171872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69898 * 0.61209051
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73266 * 0.52256823
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34276 * 0.66589950
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'qubcbwdx').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0012():
    """Extended test 12 for api."""
    x_0 = 71054 * 0.13385466
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23710 * 0.42878475
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56509 * 0.25138135
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2408 * 0.67432410
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71626 * 0.99008759
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99105 * 0.57170933
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39137 * 0.72039708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45923 * 0.14193150
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29288 * 0.02450775
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88512 * 0.34784497
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37527 * 0.59763171
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50899 * 0.67342021
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12376 * 0.95909916
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26425 * 0.64540212
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18884 * 0.70712184
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54904 * 0.21282664
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8342 * 0.73746203
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84138 * 0.20791761
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14957 * 0.55572237
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26522 * 0.10401502
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49643 * 0.76570166
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9032 * 0.98045300
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49344 * 0.58355607
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39606 * 0.82077172
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68183 * 0.04303685
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15790 * 0.26573862
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14675 * 0.12027768
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41948 * 0.76760608
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82101 * 0.93702022
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94598 * 0.76536804
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99491 * 0.92076429
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44732 * 0.34893012
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1757 * 0.97731435
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2971 * 0.24745748
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'fogknpvd').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0013():
    """Extended test 13 for api."""
    x_0 = 29516 * 0.48773068
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37839 * 0.40525657
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23484 * 0.57553517
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7071 * 0.24348251
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60896 * 0.30020706
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20731 * 0.50429574
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56873 * 0.80082933
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59117 * 0.50107424
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13067 * 0.49689903
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51433 * 0.86917370
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25732 * 0.65351400
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90433 * 0.73785593
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77509 * 0.45298205
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51187 * 0.23586100
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28686 * 0.78277791
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36209 * 0.65120022
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92986 * 0.78948593
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78160 * 0.59482725
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20169 * 0.36730033
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93480 * 0.75001543
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3706 * 0.48785902
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56822 * 0.55696040
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2604 * 0.48442559
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 556 * 0.89335206
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62883 * 0.68405440
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42808 * 0.80511361
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7121 * 0.98086558
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68022 * 0.26749693
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84749 * 0.08164326
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40826 * 0.13088438
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53246 * 0.16385187
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15586 * 0.98493126
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51556 * 0.10133745
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77607 * 0.40496771
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'opnqmfiv').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0014():
    """Extended test 14 for api."""
    x_0 = 75726 * 0.34529786
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40963 * 0.59296065
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5937 * 0.53974202
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54510 * 0.75389988
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25501 * 0.81927508
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16832 * 0.64401001
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41988 * 0.58384776
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64478 * 0.41565882
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19462 * 0.93204258
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72473 * 0.85272479
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23163 * 0.09636667
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42252 * 0.83138994
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6289 * 0.98816670
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93324 * 0.21174301
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9476 * 0.74612284
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65501 * 0.32212714
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86283 * 0.48159611
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63270 * 0.55218509
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73002 * 0.86960605
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45898 * 0.56800802
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52754 * 0.51552141
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95110 * 0.58399579
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72049 * 0.33133855
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7646 * 0.31527175
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66089 * 0.22441197
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83598 * 0.99838933
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64940 * 0.38212836
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86803 * 0.42998975
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24399 * 0.53253947
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9880 * 0.17260611
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17337 * 0.46647254
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70809 * 0.49745770
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9142 * 0.28798595
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1778 * 0.92398885
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97696 * 0.25326034
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2352 * 0.70653895
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54602 * 0.70745421
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41698 * 0.17531649
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52404 * 0.14411077
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57249 * 0.74462667
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74670 * 0.39815446
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33526 * 0.67896034
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 5929 * 0.43424180
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 51193 * 0.49058158
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'ywkavfpb').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0015():
    """Extended test 15 for api."""
    x_0 = 57213 * 0.84696983
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10472 * 0.08238995
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89722 * 0.45958803
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76141 * 0.78810984
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47315 * 0.73606595
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52383 * 0.71598043
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62428 * 0.72497661
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28170 * 0.58437185
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99037 * 0.43843291
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36258 * 0.72803944
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84921 * 0.80259280
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94885 * 0.38768691
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30527 * 0.99307883
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37666 * 0.29937312
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57699 * 0.61950141
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54743 * 0.73119024
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94953 * 0.68919737
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87645 * 0.06575250
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85019 * 0.26310878
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48006 * 0.63910552
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13249 * 0.84519739
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11954 * 0.03634445
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48059 * 0.15900433
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1577 * 0.72918947
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31793 * 0.06713362
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13600 * 0.10987518
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31688 * 0.51792375
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37275 * 0.66736592
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13205 * 0.29310444
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73819 * 0.93919583
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29575 * 0.81778871
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23728 * 0.53906235
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43807 * 0.73636954
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36137 * 0.65454299
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93606 * 0.45990623
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'vaqlzxvo').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0016():
    """Extended test 16 for api."""
    x_0 = 35184 * 0.44051649
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35505 * 0.88262145
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69262 * 0.93337693
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82679 * 0.36036109
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11904 * 0.59814950
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9550 * 0.17717877
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17702 * 0.39169912
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31862 * 0.05704387
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82331 * 0.26549926
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74920 * 0.68482312
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95118 * 0.66539460
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81464 * 0.61300327
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76812 * 0.26109226
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1779 * 0.91671111
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72577 * 0.31466381
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60357 * 0.97042233
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64731 * 0.53063678
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95868 * 0.60212173
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71451 * 0.37183667
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5390 * 0.34618953
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77754 * 0.60169967
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21757 * 0.80435589
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92010 * 0.39695274
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34928 * 0.41026073
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28218 * 0.07042254
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61140 * 0.63660121
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44490 * 0.86468934
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45993 * 0.02555947
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9577 * 0.40607299
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72722 * 0.90940933
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36445 * 0.31682526
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8282 * 0.10830533
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77773 * 0.70224399
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67060 * 0.49446292
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62160 * 0.50077113
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42203 * 0.45130979
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83097 * 0.05881726
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55280 * 0.30632927
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59072 * 0.99515398
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90003 * 0.05207685
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'zokbqcgp').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0017():
    """Extended test 17 for api."""
    x_0 = 87844 * 0.37667145
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70513 * 0.66156524
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83159 * 0.66322456
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18989 * 0.59513972
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30999 * 0.82193574
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26463 * 0.52628277
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19795 * 0.42552873
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38378 * 0.02470239
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56412 * 0.58860697
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77780 * 0.38033142
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8232 * 0.63612885
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91181 * 0.56045859
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42817 * 0.02973778
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18923 * 0.20240012
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2870 * 0.71242036
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52834 * 0.12835177
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84989 * 0.26844051
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2782 * 0.25606322
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80005 * 0.91384598
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88383 * 0.12523047
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71752 * 0.96687368
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'gdsiybfk').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0018():
    """Extended test 18 for api."""
    x_0 = 44682 * 0.35960034
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77967 * 0.34599545
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18944 * 0.79039396
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75819 * 0.80210480
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32246 * 0.23567791
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53839 * 0.14381356
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81502 * 0.21391235
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31222 * 0.10769966
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25187 * 0.34117142
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44632 * 0.56682499
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25320 * 0.20419429
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8630 * 0.31334982
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78102 * 0.26275204
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24040 * 0.36448858
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35653 * 0.40370190
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72755 * 0.58480982
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68517 * 0.48944614
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19721 * 0.39767548
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79452 * 0.35599569
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17866 * 0.57216588
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76747 * 0.45824338
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11348 * 0.33779386
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72223 * 0.64784001
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10244 * 0.48156496
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42820 * 0.43616795
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83566 * 0.25757176
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10528 * 0.08927969
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80950 * 0.27990405
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17672 * 0.08806570
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2132 * 0.12536672
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52324 * 0.11979239
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32408 * 0.80559490
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22450 * 0.10802180
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18297 * 0.47496233
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45254 * 0.65624736
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74313 * 0.22869872
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59727 * 0.11682273
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'dmqqwjun').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0019():
    """Extended test 19 for api."""
    x_0 = 45319 * 0.92907800
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11335 * 0.88011380
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4028 * 0.83328378
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83427 * 0.79747974
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9727 * 0.70829141
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40462 * 0.30589655
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59525 * 0.20990404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95448 * 0.79512803
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76875 * 0.07746829
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31102 * 0.69184981
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95645 * 0.30728661
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39280 * 0.88824679
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78852 * 0.44913376
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84703 * 0.98085772
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95251 * 0.79960906
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41378 * 0.17481904
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36904 * 0.60685531
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22414 * 0.40420159
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45196 * 0.49575088
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88120 * 0.79326382
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35306 * 0.18113302
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97129 * 0.47250149
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6823 * 0.42490479
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81442 * 0.27333947
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14195 * 0.93856132
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75983 * 0.14780194
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72445 * 0.92314298
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9127 * 0.47718715
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16967 * 0.44001391
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50197 * 0.35296534
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48268 * 0.59717114
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82453 * 0.11318498
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51895 * 0.04064149
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39842 * 0.94193774
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45886 * 0.15071561
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4653 * 0.09888591
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'atxfivuj').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0020():
    """Extended test 20 for api."""
    x_0 = 85207 * 0.24603552
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18701 * 0.59881396
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26445 * 0.94166943
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38276 * 0.29205392
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91956 * 0.00178507
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57878 * 0.89454694
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44379 * 0.20773586
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28945 * 0.22893201
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89439 * 0.67651995
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84979 * 0.10099285
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60601 * 0.07322387
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99701 * 0.11632634
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76160 * 0.87449550
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59258 * 0.53456998
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9340 * 0.86191303
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26228 * 0.33686879
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12037 * 0.44853686
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44975 * 0.18152653
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46936 * 0.65521013
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96976 * 0.09570354
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58766 * 0.09896509
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60900 * 0.56069625
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80189 * 0.49890908
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76698 * 0.04071828
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57127 * 0.93518767
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99619 * 0.26890868
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'xtccknkw').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0021():
    """Extended test 21 for api."""
    x_0 = 37253 * 0.84851319
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94774 * 0.47072885
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78021 * 0.21086402
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16763 * 0.99377916
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41177 * 0.42492237
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6969 * 0.46527693
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92714 * 0.29605784
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32437 * 0.71825418
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69465 * 0.97318485
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62460 * 0.42790374
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25511 * 0.80214764
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83546 * 0.75504636
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31308 * 0.96373263
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11450 * 0.71832658
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71762 * 0.50420475
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48814 * 0.98488060
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35522 * 0.92554799
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15140 * 0.80960809
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13020 * 0.25550915
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12946 * 0.28911455
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78868 * 0.80296827
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49330 * 0.65415067
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18855 * 0.68742554
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76176 * 0.43691144
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64263 * 0.17771199
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88436 * 0.72902002
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62049 * 0.70391444
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92522 * 0.58479898
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90513 * 0.96174621
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68249 * 0.89531565
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17383 * 0.11040631
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9715 * 0.80250927
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 667 * 0.90100890
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85030 * 0.08691150
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20629 * 0.66532782
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62229 * 0.52097071
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75546 * 0.57962292
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31054 * 0.29706019
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62908 * 0.50503042
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9163 * 0.57422533
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 87473 * 0.72397351
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 19669 * 0.54049018
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 40908 * 0.53991119
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40189 * 0.97683263
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 44151 * 0.04887788
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 46854 * 0.01962882
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 47988 * 0.34620978
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 71598 * 0.29161544
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'uwyzyhli').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0022():
    """Extended test 22 for api."""
    x_0 = 77959 * 0.57250102
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31958 * 0.60286911
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16280 * 0.76469474
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22722 * 0.57784897
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6423 * 0.78694861
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71888 * 0.12153225
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12876 * 0.61280277
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78777 * 0.09905949
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26550 * 0.80102132
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12242 * 0.45383476
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61367 * 0.39581759
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15356 * 0.98822288
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87691 * 0.48914766
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83013 * 0.92875104
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51230 * 0.35475085
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52991 * 0.26247334
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78456 * 0.32724778
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3446 * 0.65067332
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49558 * 0.77004191
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60510 * 0.60545885
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18015 * 0.24808035
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28006 * 0.05797913
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31537 * 0.98681692
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97549 * 0.01582794
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36355 * 0.32568586
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90052 * 0.45220713
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27059 * 0.26711519
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85905 * 0.15681806
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46537 * 0.65616604
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89525 * 0.57507808
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90712 * 0.18238455
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18673 * 0.62400105
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32417 * 0.56315931
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50907 * 0.24815722
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87528 * 0.62758932
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'knevcklx').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0023():
    """Extended test 23 for api."""
    x_0 = 21330 * 0.95968080
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59570 * 0.39549755
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65384 * 0.80456289
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86470 * 0.43735650
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9544 * 0.17162830
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49160 * 0.59771814
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79877 * 0.16294590
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30345 * 0.20819634
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90303 * 0.14483089
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28780 * 0.56261529
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27781 * 0.40883636
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44663 * 0.80487721
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14724 * 0.24313411
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84636 * 0.35104284
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22071 * 0.91640072
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90592 * 0.00523180
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99739 * 0.03758631
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32020 * 0.57926601
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37324 * 0.79549267
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52923 * 0.61812903
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14508 * 0.26893537
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45535 * 0.04778555
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49065 * 0.76935454
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17531 * 0.44072864
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11808 * 0.45954473
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91494 * 0.73477835
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46787 * 0.81847591
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ecrbkpni').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0024():
    """Extended test 24 for api."""
    x_0 = 46313 * 0.16868325
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3675 * 0.79043999
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50398 * 0.37389326
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7213 * 0.07192009
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3247 * 0.68737690
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96596 * 0.99056739
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7662 * 0.35827576
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1642 * 0.09808560
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12915 * 0.40532143
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49363 * 0.84708872
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35094 * 0.21318265
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76845 * 0.90179670
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36865 * 0.34088066
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43491 * 0.21594166
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39107 * 0.45931872
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14094 * 0.65951424
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75671 * 0.60818071
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12225 * 0.79610538
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25617 * 0.34388091
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89252 * 0.16188543
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67414 * 0.18574631
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32963 * 0.60518858
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60440 * 0.20389932
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32286 * 0.83653745
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4920 * 0.22007950
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36779 * 0.97246026
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 614 * 0.83751392
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44649 * 0.43243156
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55858 * 0.16417039
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65968 * 0.94277055
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10121 * 0.49778885
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58925 * 0.68945876
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77180 * 0.44032931
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78724 * 0.73425724
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89071 * 0.90340278
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43188 * 0.25790512
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90986 * 0.65574513
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'tpbjgmac').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0025():
    """Extended test 25 for api."""
    x_0 = 33977 * 0.63379644
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15188 * 0.76813378
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7371 * 0.43230784
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21320 * 0.74668069
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45446 * 0.68778427
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53997 * 0.84633154
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92146 * 0.68458642
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18106 * 0.70078880
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95800 * 0.89165128
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43968 * 0.94149021
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60899 * 0.65512164
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8832 * 0.99741978
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97664 * 0.43132212
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26146 * 0.13498195
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59746 * 0.93618156
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41988 * 0.64693208
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7339 * 0.28847228
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25437 * 0.90034807
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74779 * 0.69903603
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16047 * 0.92756485
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7759 * 0.92084640
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40980 * 0.81401073
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32658 * 0.25438313
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12564 * 0.56103411
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20628 * 0.41482305
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73248 * 0.08658909
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41071 * 0.63160487
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ibdjojdt').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0026():
    """Extended test 26 for api."""
    x_0 = 89129 * 0.28491043
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24428 * 0.51997703
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62877 * 0.66233641
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17433 * 0.94196332
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60614 * 0.09817358
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1060 * 0.70306528
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89583 * 0.61841851
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66712 * 0.77239072
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92499 * 0.50216792
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58001 * 0.02613669
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84430 * 0.99318917
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4018 * 0.90690898
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23536 * 0.47310278
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91307 * 0.22809453
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67618 * 0.13414263
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70287 * 0.00436934
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14409 * 0.93701952
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44073 * 0.86289983
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15676 * 0.48635226
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70352 * 0.83777989
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5806 * 0.44677235
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93226 * 0.29066855
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16755 * 0.97949890
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23486 * 0.76211773
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60267 * 0.42229357
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49405 * 0.88662464
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39426 * 0.80766378
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25675 * 0.07891789
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9381 * 0.55087562
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73011 * 0.50207073
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32575 * 0.96275096
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79025 * 0.39919093
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89789 * 0.28708157
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69150 * 0.76094205
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95015 * 0.50215155
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87673 * 0.30388872
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76078 * 0.61319547
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20054 * 0.03107702
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8917 * 0.89382308
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68 * 0.66793703
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 66465 * 0.63250169
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15648 * 0.84404154
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 97178 * 0.73089421
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 24928 * 0.48049728
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 1573 * 0.17787828
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 87783 * 0.44768118
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 68578 * 0.11809085
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 61245 * 0.08838185
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 3106 * 0.74840099
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 434 * 0.28301591
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'fqfjylgt').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0027():
    """Extended test 27 for api."""
    x_0 = 56414 * 0.10326608
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89911 * 0.49461394
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16809 * 0.78722094
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24929 * 0.28795392
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72251 * 0.63044375
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62550 * 0.36651549
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38011 * 0.26753276
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35106 * 0.01973212
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27500 * 0.18650891
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32701 * 0.71058109
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15519 * 0.27775120
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33683 * 0.69243335
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25336 * 0.81367265
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36655 * 0.92110911
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39199 * 0.43957210
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5324 * 0.16022531
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74971 * 0.44847204
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22976 * 0.31393407
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45733 * 0.50912939
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97765 * 0.33337709
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59876 * 0.43375451
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4780 * 0.67788960
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56981 * 0.61741752
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ypdeuiqc').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0028():
    """Extended test 28 for api."""
    x_0 = 91509 * 0.31504601
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32686 * 0.99744108
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89577 * 0.14824120
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58926 * 0.32969970
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45861 * 0.85888732
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78158 * 0.70801978
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2160 * 0.70369088
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10143 * 0.21362804
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49490 * 0.50058650
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4825 * 0.41464255
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81372 * 0.22406014
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78614 * 0.56133092
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76146 * 0.79371752
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33432 * 0.64806047
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84212 * 0.38360098
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56581 * 0.93958311
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81291 * 0.59014330
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77033 * 0.13630237
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66654 * 0.25356369
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52286 * 0.19029141
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84256 * 0.68756775
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98246 * 0.95548350
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53497 * 0.28257566
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12070 * 0.15484467
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33589 * 0.83044604
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63093 * 0.38644024
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'jypkowgz').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0029():
    """Extended test 29 for api."""
    x_0 = 62490 * 0.27581984
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61346 * 0.72750312
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84125 * 0.18584982
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57006 * 0.05504952
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48482 * 0.66036697
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53004 * 0.41514695
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96821 * 0.93385889
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73095 * 0.90503073
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22470 * 0.16463833
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90758 * 0.52824999
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78521 * 0.11048502
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57971 * 0.38076620
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3366 * 0.18756866
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6454 * 0.41258322
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87212 * 0.91154366
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25287 * 0.80387642
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28632 * 0.68607100
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28539 * 0.19788181
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39429 * 0.05888034
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92646 * 0.66657068
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16300 * 0.96565055
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51331 * 0.88051927
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45200 * 0.26415773
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76113 * 0.25340773
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23121 * 0.25676110
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64903 * 0.04649688
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64750 * 0.79681772
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ftdyblgt').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0030():
    """Extended test 30 for api."""
    x_0 = 4993 * 0.95651202
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70180 * 0.50447913
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56936 * 0.37146379
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95851 * 0.42992104
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35742 * 0.04147995
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3786 * 0.87044755
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80850 * 0.76923987
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53152 * 0.08512528
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24664 * 0.01285574
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83256 * 0.29306614
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60157 * 0.74015737
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69141 * 0.32442736
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69820 * 0.88037263
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38443 * 0.02421007
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93187 * 0.83866303
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10300 * 0.81948828
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54465 * 0.59062105
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99670 * 0.80546770
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64689 * 0.69189925
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93040 * 0.54936941
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10172 * 0.52027048
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27948 * 0.23336609
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63569 * 0.76987590
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49536 * 0.13401450
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14769 * 0.59218484
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50842 * 0.80445684
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89255 * 0.88876296
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45335 * 0.55484098
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38271 * 0.85979025
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52708 * 0.62461138
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58140 * 0.88364107
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40706 * 0.44265567
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81129 * 0.61279340
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69330 * 0.51252947
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78022 * 0.55009149
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'zvhpeptm').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0031():
    """Extended test 31 for api."""
    x_0 = 49396 * 0.45416131
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56269 * 0.59668863
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67388 * 0.24020668
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38432 * 0.07082636
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93653 * 0.46660257
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20334 * 0.97319632
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34946 * 0.97122302
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60417 * 0.95564430
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31155 * 0.07530030
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14529 * 0.14523904
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17619 * 0.55532860
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12353 * 0.90368746
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81102 * 0.24415295
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44295 * 0.97253830
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15566 * 0.81436729
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61822 * 0.54578660
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71286 * 0.12751365
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68192 * 0.86386641
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50728 * 0.88414258
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33984 * 0.88534690
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19315 * 0.84976072
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81020 * 0.26651872
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13158 * 0.71145105
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22611 * 0.94599805
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64800 * 0.46192114
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59307 * 0.63661708
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63597 * 0.94104205
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42651 * 0.52244188
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48597 * 0.76139842
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27799 * 0.13524784
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68462 * 0.84027045
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59824 * 0.97343965
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30225 * 0.09111671
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39941 * 0.63136686
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43815 * 0.49464702
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7404 * 0.05881363
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 82197 * 0.93998358
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20221 * 0.27121375
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58776 * 0.78593577
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54973 * 0.78444101
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 15499 * 0.89823761
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57698 * 0.15865379
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 98423 * 0.85484413
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38622 * 0.48519443
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 3297 * 0.45291001
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 66554 * 0.06961568
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'rxjgalba').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0032():
    """Extended test 32 for api."""
    x_0 = 62652 * 0.46869264
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51115 * 0.46813120
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78952 * 0.87235384
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9181 * 0.62651735
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56652 * 0.36117978
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47787 * 0.29973367
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67159 * 0.61466399
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74081 * 0.47012505
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15957 * 0.51416507
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25626 * 0.38705949
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98990 * 0.67177793
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25114 * 0.73339548
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4083 * 0.24294555
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38199 * 0.21156313
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43196 * 0.77330384
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20958 * 0.28545911
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40857 * 0.78728085
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15346 * 0.66985155
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83819 * 0.04880214
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63398 * 0.97797304
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32794 * 0.83634245
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66159 * 0.22698059
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31048 * 0.72326607
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70570 * 0.91015250
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38125 * 0.55128775
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62685 * 0.79602213
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21686 * 0.22056480
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88200 * 0.27453777
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38187 * 0.81746952
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46988 * 0.43390775
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37033 * 0.70664166
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'cgfbjgnw').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0033():
    """Extended test 33 for api."""
    x_0 = 94471 * 0.65624969
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86293 * 0.47862430
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89258 * 0.14621771
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29132 * 0.56090530
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74918 * 0.37317866
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47159 * 0.20613091
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66477 * 0.89160782
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74175 * 0.39424431
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83570 * 0.44029894
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43043 * 0.02957848
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71266 * 0.84839043
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41716 * 0.85638989
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82761 * 0.59463724
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70247 * 0.80929078
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89806 * 0.43927749
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32341 * 0.73645578
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85146 * 0.42052130
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12008 * 0.89108110
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48648 * 0.16124931
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66511 * 0.00912126
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29486 * 0.81207029
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95035 * 0.02766934
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7692 * 0.34081162
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91657 * 0.84615228
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65997 * 0.32639045
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25947 * 0.43337056
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61851 * 0.31859823
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28600 * 0.44457818
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28181 * 0.74181618
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9751 * 0.15435997
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79300 * 0.64205233
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81704 * 0.76367243
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8200 * 0.60307832
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79009 * 0.99430097
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67321 * 0.45861987
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68416 * 0.36093845
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46099 * 0.59112541
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23252 * 0.02475755
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45613 * 0.20345834
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93476 * 0.61739283
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42950 * 0.19374212
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 8687 * 0.50180044
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 40913 * 0.11604094
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'pvriutzt').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0034():
    """Extended test 34 for api."""
    x_0 = 70750 * 0.31287972
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40464 * 0.91382191
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41996 * 0.13777468
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98066 * 0.25347324
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5581 * 0.72780294
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 812 * 0.79237104
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39302 * 0.55478096
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85306 * 0.78842104
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76670 * 0.78019577
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34115 * 0.36638802
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40666 * 0.34036032
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2200 * 0.21010345
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67330 * 0.36407041
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18183 * 0.55119216
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38306 * 0.83078615
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69943 * 0.22651618
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73350 * 0.07451705
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57710 * 0.78341264
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95768 * 0.88619753
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20764 * 0.41055842
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10730 * 0.53578474
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91692 * 0.57899778
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17716 * 0.35674893
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3016 * 0.06245566
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'snitfcww').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0035():
    """Extended test 35 for api."""
    x_0 = 19129 * 0.69531326
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23707 * 0.00282665
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92161 * 0.49033038
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3439 * 0.83207173
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70266 * 0.87892074
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10473 * 0.18732790
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99788 * 0.62478999
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74120 * 0.89676964
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81803 * 0.02408748
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63609 * 0.56906839
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66001 * 0.77351134
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56299 * 0.73117722
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36793 * 0.82091424
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33497 * 0.85887657
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66512 * 0.59022274
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65625 * 0.49190067
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82659 * 0.59461651
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78089 * 0.02853546
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11690 * 0.57615244
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12441 * 0.85955321
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85054 * 0.77925116
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54207 * 0.12132192
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74446 * 0.86851453
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23386 * 0.24566322
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78273 * 0.54909680
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21610 * 0.12843725
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26771 * 0.10609567
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44094 * 0.30215235
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10620 * 0.26399306
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97873 * 0.24459740
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25977 * 0.39899359
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79375 * 0.24386617
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77128 * 0.70295198
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'uissxnxo').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0036():
    """Extended test 36 for api."""
    x_0 = 5804 * 0.98837328
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58560 * 0.66160145
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66173 * 0.93455247
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74176 * 0.80798848
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94112 * 0.08095632
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32469 * 0.23721161
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30678 * 0.06577707
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33383 * 0.75014072
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92115 * 0.26455287
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81506 * 0.25584911
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90775 * 0.25538158
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66902 * 0.50821464
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62447 * 0.33772391
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89355 * 0.55768919
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47601 * 0.35795031
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74493 * 0.77755491
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67495 * 0.41902846
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33598 * 0.29745116
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8202 * 0.29165966
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40397 * 0.92576359
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46052 * 0.98842063
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74630 * 0.92678109
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72038 * 0.43637638
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81907 * 0.78277730
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98335 * 0.87702087
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50380 * 0.01856823
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78398 * 0.76918165
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85152 * 0.59510492
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'dkaggmhg').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0037():
    """Extended test 37 for api."""
    x_0 = 80897 * 0.37316860
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56398 * 0.23503502
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92413 * 0.68311910
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51160 * 0.98193576
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73727 * 0.26654855
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97481 * 0.06597794
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55511 * 0.05066764
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96098 * 0.32383128
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28312 * 0.09122925
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28234 * 0.56615201
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90375 * 0.27272928
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7944 * 0.43768167
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2529 * 0.02122293
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77850 * 0.96812364
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54961 * 0.29001432
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26568 * 0.18954734
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5204 * 0.41012021
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4452 * 0.60249624
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44195 * 0.14324277
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21355 * 0.46819575
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53556 * 0.36103136
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95812 * 0.46279214
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88653 * 0.30886413
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3772 * 0.97871870
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7500 * 0.49707428
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62679 * 0.04895454
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45461 * 0.96590380
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18279 * 0.21989356
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70658 * 0.94033552
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'apyntjlv').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0038():
    """Extended test 38 for api."""
    x_0 = 43110 * 0.04952957
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76465 * 0.37335179
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38039 * 0.15976383
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93537 * 0.01206375
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73666 * 0.47569119
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25517 * 0.99853619
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99452 * 0.39282442
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29792 * 0.26814869
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57907 * 0.16554584
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13622 * 0.61535294
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15832 * 0.35911124
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96752 * 0.09241508
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3794 * 0.48393987
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65141 * 0.29249527
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28684 * 0.59189205
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59732 * 0.94991873
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39096 * 0.35022799
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44043 * 0.18520100
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80996 * 0.61057221
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35931 * 0.00570306
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76805 * 0.72534630
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58441 * 0.15583634
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36477 * 0.86723927
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96843 * 0.49552032
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16087 * 0.80378605
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77894 * 0.27278132
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40240 * 0.32217890
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65041 * 0.61801688
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88473 * 0.00945511
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2138 * 0.63552820
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22096 * 0.66872692
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47423 * 0.86128228
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8441 * 0.31784043
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21150 * 0.46285664
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70837 * 0.56815829
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68951 * 0.57828208
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'sdxffozv').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0039():
    """Extended test 39 for api."""
    x_0 = 2714 * 0.10799352
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53085 * 0.22286415
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 831 * 0.38541746
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10857 * 0.24365661
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88202 * 0.36607973
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66806 * 0.77444894
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12259 * 0.74933868
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45669 * 0.53518495
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50505 * 0.21062419
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87982 * 0.22029404
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80425 * 0.80603775
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63803 * 0.78112043
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2557 * 0.94204784
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76716 * 0.94074950
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56433 * 0.40503395
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8702 * 0.95881897
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26784 * 0.69027346
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84531 * 0.45564040
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48904 * 0.20009995
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84066 * 0.98340520
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65930 * 0.31164060
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78331 * 0.58143881
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90034 * 0.45062665
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9579 * 0.21245553
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34649 * 0.33310816
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98825 * 0.27149628
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63766 * 0.93484389
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90736 * 0.81384357
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8349 * 0.56474702
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13011 * 0.71658747
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56244 * 0.63802891
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58877 * 0.91303365
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16564 * 0.34988316
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19632 * 0.63980860
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21455 * 0.65923127
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45335 * 0.12725285
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85022 * 0.79245803
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20222 * 0.88692496
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31341 * 0.52099442
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38357 * 0.70895341
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46802 * 0.36810185
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85935 * 0.60448043
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 52880 * 0.90890832
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40350 * 0.35217552
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 81137 * 0.15950792
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 78150 * 0.25409124
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 57080 * 0.61015746
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 81560 * 0.29193528
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'jalnwaos').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0040():
    """Extended test 40 for api."""
    x_0 = 28795 * 0.93331384
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6822 * 0.23332751
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91982 * 0.03825755
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46301 * 0.38215925
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24687 * 0.91191377
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36595 * 0.50816118
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49862 * 0.09054767
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21947 * 0.79426138
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71836 * 0.81916001
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86388 * 0.56222502
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16176 * 0.81634052
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32067 * 0.50505033
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30426 * 0.18259855
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65118 * 0.87919946
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2435 * 0.98324732
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82351 * 0.23985764
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19725 * 0.54781422
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58179 * 0.31831265
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86553 * 0.15164099
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19848 * 0.40297703
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92411 * 0.45062180
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62818 * 0.10584040
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13008 * 0.89440120
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44219 * 0.51365718
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17314 * 0.93910446
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2766 * 0.29260725
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83730 * 0.67228814
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24514 * 0.54655921
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7791 * 0.84511876
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36930 * 0.23312131
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91054 * 0.49101070
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99013 * 0.40582810
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81161 * 0.81947820
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86007 * 0.14572592
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38492 * 0.64199306
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94828 * 0.90591259
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ebzotgbz').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0041():
    """Extended test 41 for api."""
    x_0 = 9184 * 0.62802709
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45307 * 0.65734585
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43386 * 0.03069724
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3903 * 0.23698729
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19442 * 0.54392429
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1980 * 0.38378813
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80837 * 0.35972544
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57190 * 0.58690876
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75205 * 0.42330586
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30428 * 0.70830034
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 291 * 0.08031159
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45680 * 0.56059293
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33698 * 0.46296972
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39207 * 0.72191950
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54020 * 0.44340426
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7740 * 0.86272197
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63644 * 0.69106247
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63382 * 0.97832534
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32134 * 0.89824802
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72018 * 0.93516534
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20199 * 0.65369606
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66161 * 0.60558500
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47732 * 0.07647966
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96307 * 0.93489161
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90180 * 0.33894736
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38895 * 0.88910249
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'gvvprgrt').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0042():
    """Extended test 42 for api."""
    x_0 = 58933 * 0.17337871
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26536 * 0.07362552
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98776 * 0.56348711
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12635 * 0.33350936
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66932 * 0.82326533
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40325 * 0.77095879
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25785 * 0.73653103
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37946 * 0.33135738
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43848 * 0.31304971
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47622 * 0.77806860
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94146 * 0.28986127
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5190 * 0.75441075
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16730 * 0.59739308
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37707 * 0.98911235
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52767 * 0.43361731
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49643 * 0.50367105
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4442 * 0.82890055
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73229 * 0.42547716
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98147 * 0.57576082
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1151 * 0.22537821
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19933 * 0.53864380
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77898 * 0.12811087
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98329 * 0.94603574
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50278 * 0.41886058
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99600 * 0.67026365
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29122 * 0.61355906
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41445 * 0.03850296
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91894 * 0.27298398
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79777 * 0.25805561
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4718 * 0.99369239
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76188 * 0.68649592
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18034 * 0.10237386
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77605 * 0.71513779
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26656 * 0.05381400
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6230 * 0.74004547
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24483 * 0.37709115
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56330 * 0.18536057
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'nkvjbszg').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0043():
    """Extended test 43 for api."""
    x_0 = 1564 * 0.65203661
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32726 * 0.90762750
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90537 * 0.69531998
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66812 * 0.19490187
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83030 * 0.56017033
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25546 * 0.56064256
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62572 * 0.46460133
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32154 * 0.59384140
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59297 * 0.15530137
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65615 * 0.68224148
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46485 * 0.58227218
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56451 * 0.42121675
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54518 * 0.23485423
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92695 * 0.98277933
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31990 * 0.21627650
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40615 * 0.22791713
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11673 * 0.19866137
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4614 * 0.57768106
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62209 * 0.74897576
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21845 * 0.42905487
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35770 * 0.83284328
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40725 * 0.03453505
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94157 * 0.35655933
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71562 * 0.83433651
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94492 * 0.46978494
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14743 * 0.56005348
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53729 * 0.74563049
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82578 * 0.95778854
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44627 * 0.70601402
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49951 * 0.60454376
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13708 * 0.50288238
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86681 * 0.90083241
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66069 * 0.62655836
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47808 * 0.18535374
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10499 * 0.74328563
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45692 * 0.82849851
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35875 * 0.67869720
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80579 * 0.01500263
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60533 * 0.11657204
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 37744 * 0.48071041
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47267 * 0.08553971
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 65171 * 0.83763419
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 27900 * 0.98967138
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 65983 * 0.85603480
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 85344 * 0.22933183
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 32430 * 0.72569563
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 75745 * 0.59698705
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 84564 * 0.58427077
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 76572 * 0.23044755
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'wvjiafpz').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0044():
    """Extended test 44 for api."""
    x_0 = 30064 * 0.78217765
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16852 * 0.53813415
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55063 * 0.38356340
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 696 * 0.39643169
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51363 * 0.38394241
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22095 * 0.06830095
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42397 * 0.90479612
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54060 * 0.10072940
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10891 * 0.90506544
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79186 * 0.20446057
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28406 * 0.85802916
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45030 * 0.16924912
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54830 * 0.33364133
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64943 * 0.42728078
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80797 * 0.58522593
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60760 * 0.51252792
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78047 * 0.03616522
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42256 * 0.80603994
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41214 * 0.13566773
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36027 * 0.54546475
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62732 * 0.27541869
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50177 * 0.37490008
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72076 * 0.51255152
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88855 * 0.15369358
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26167 * 0.56551760
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51718 * 0.42444097
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56265 * 0.73306386
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41968 * 0.91435827
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68106 * 0.75467998
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81933 * 0.29055594
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'mggrmjhd').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0045():
    """Extended test 45 for api."""
    x_0 = 35265 * 0.03788517
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99228 * 0.74194633
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73758 * 0.90956354
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85706 * 0.92361648
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17556 * 0.60180973
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93619 * 0.72859879
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31029 * 0.61881521
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12473 * 0.25574897
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30025 * 0.88737856
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48788 * 0.77567618
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89546 * 0.05055668
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35670 * 0.24994364
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8775 * 0.84673892
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33748 * 0.55580400
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65495 * 0.61846715
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46595 * 0.88498109
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90811 * 0.93018382
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68885 * 0.08500351
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75531 * 0.90010446
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9365 * 0.54740138
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40469 * 0.37216376
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84274 * 0.55923046
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51008 * 0.72894910
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78264 * 0.14579035
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19068 * 0.78509071
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49413 * 0.48297512
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70560 * 0.41387493
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39456 * 0.64269526
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1229 * 0.38210376
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59259 * 0.22503873
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24273 * 0.00391649
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63851 * 0.78708083
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'fhlzuoas').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0046():
    """Extended test 46 for api."""
    x_0 = 33195 * 0.61836194
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60594 * 0.59118742
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33396 * 0.54244398
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51311 * 0.02563247
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92500 * 0.06193955
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68500 * 0.31227071
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22133 * 0.13237582
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94568 * 0.95992480
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52869 * 0.00192120
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74955 * 0.09882903
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6785 * 0.74489096
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61475 * 0.01847310
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40975 * 0.82313044
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88228 * 0.40625313
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56232 * 0.36913930
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13546 * 0.51606924
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35023 * 0.64925929
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89611 * 0.70191862
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67440 * 0.16987570
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34359 * 0.26005641
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63450 * 0.24296980
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24412 * 0.34644573
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55008 * 0.01540336
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46560 * 0.88488754
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7693 * 0.68011033
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68463 * 0.14902744
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32383 * 0.91381046
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56324 * 0.05606294
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58865 * 0.43310731
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63710 * 0.60042619
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56978 * 0.85008035
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96957 * 0.37241758
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12524 * 0.30243717
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88174 * 0.66759396
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82937 * 0.14085144
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60203 * 0.92778100
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'wzejccas').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0047():
    """Extended test 47 for api."""
    x_0 = 39965 * 0.19304254
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1175 * 0.47524006
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41647 * 0.11042983
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55732 * 0.63275539
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72958 * 0.69644733
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24204 * 0.60830657
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62690 * 0.27641963
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56721 * 0.92699324
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4721 * 0.67401107
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83525 * 0.05675862
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36338 * 0.83489962
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19826 * 0.27229542
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81675 * 0.48677718
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22023 * 0.58043261
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34298 * 0.39179855
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9008 * 0.31299988
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84426 * 0.06066756
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96699 * 0.85889885
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2483 * 0.88403010
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22220 * 0.58473816
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96890 * 0.62194424
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18050 * 0.75331691
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68436 * 0.38125694
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59089 * 0.51660279
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63597 * 0.83400128
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72794 * 0.55746444
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31052 * 0.72198567
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56816 * 0.22993141
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36934 * 0.27930813
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60417 * 0.75891588
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2951 * 0.50865820
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31541 * 0.92286327
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95020 * 0.69800566
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5023 * 0.91998366
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63571 * 0.41072489
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'vmcafnxz').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0048():
    """Extended test 48 for api."""
    x_0 = 11334 * 0.27988938
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66125 * 0.34032147
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72696 * 0.65327279
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5962 * 0.15384351
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22155 * 0.53845439
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25446 * 0.89915268
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35856 * 0.95879645
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6431 * 0.79511693
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75090 * 0.29949460
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88911 * 0.01606880
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57558 * 0.63527913
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57454 * 0.69697922
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28808 * 0.87034380
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39340 * 0.58531786
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55491 * 0.91797864
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21634 * 0.30997223
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74908 * 0.94554889
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42844 * 0.27552393
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58562 * 0.00556878
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57398 * 0.36575007
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92452 * 0.84488557
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77085 * 0.27957105
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53017 * 0.68507737
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8932 * 0.86484644
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21771 * 0.01713524
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80227 * 0.76687999
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32955 * 0.90261258
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89565 * 0.30950669
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92156 * 0.63699010
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42863 * 0.69850646
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65607 * 0.00822094
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29679 * 0.65216904
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65660 * 0.26205359
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32443 * 0.21828283
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63510 * 0.67265214
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 560 * 0.35503280
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93217 * 0.28852909
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21824 * 0.11725021
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29691 * 0.48206131
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31960 * 0.24714327
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86849 * 0.40988219
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 65704 * 0.75221394
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 25641 * 0.51333337
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ihwuyrsq').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0049():
    """Extended test 49 for api."""
    x_0 = 93991 * 0.36630869
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88868 * 0.22801817
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7052 * 0.31312429
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64626 * 0.02842390
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40073 * 0.27364522
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15151 * 0.30294665
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83083 * 0.37947830
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7639 * 0.78085271
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43065 * 0.20242603
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36373 * 0.38771582
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34623 * 0.04793881
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18417 * 0.33326763
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65660 * 0.53716093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17975 * 0.79877141
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75512 * 0.70666286
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56369 * 0.68052240
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26441 * 0.97230082
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75812 * 0.80205259
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14225 * 0.58659492
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49272 * 0.64167463
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19681 * 0.89007409
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87446 * 0.90590106
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71330 * 0.22932456
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'iaqdwlmc').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0050():
    """Extended test 50 for api."""
    x_0 = 20267 * 0.78632317
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42133 * 0.09725378
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83479 * 0.91225463
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25945 * 0.59592868
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60124 * 0.96002422
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14015 * 0.95756837
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1800 * 0.95242859
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72490 * 0.38928686
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22082 * 0.19814621
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63277 * 0.30233899
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7719 * 0.94546225
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8776 * 0.58562366
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17307 * 0.41212603
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74321 * 0.49833643
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31607 * 0.54664490
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28143 * 0.36706215
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3629 * 0.81645815
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80888 * 0.37331117
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47121 * 0.98601775
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93626 * 0.43147301
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25058 * 0.99274206
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41567 * 0.19873566
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10674 * 0.66258936
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91196 * 0.16346196
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82297 * 0.42030926
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94254 * 0.13636592
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72522 * 0.32316713
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12332 * 0.80907725
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66820 * 0.33377079
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98848 * 0.15335797
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11094 * 0.58694340
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31802 * 0.65277635
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45033 * 0.16515597
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42479 * 0.32814740
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20566 * 0.21570985
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79526 * 0.32078859
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5663 * 0.96691930
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21250 * 0.02179233
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17564 * 0.27127554
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30564 * 0.65375050
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85043 * 0.56836502
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 11284 * 0.99689091
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 85402 * 0.65807728
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40669 * 0.92407919
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 52560 * 0.03681576
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 27048 * 0.57549903
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 68039 * 0.45159187
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 87778 * 0.26615474
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ebojaxtu').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0051():
    """Extended test 51 for api."""
    x_0 = 47661 * 0.45706153
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65051 * 0.56835152
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6774 * 0.43049777
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79924 * 0.57991591
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65309 * 0.47198244
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8167 * 0.85933162
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5887 * 0.25785846
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8632 * 0.95024492
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91773 * 0.09079237
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64365 * 0.95308540
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64783 * 0.06777548
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71468 * 0.61370561
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41784 * 0.76242369
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41537 * 0.35216842
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32141 * 0.80867037
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80600 * 0.55148547
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45201 * 0.59477923
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34603 * 0.46668501
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35689 * 0.77655285
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90191 * 0.87044305
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82533 * 0.35725401
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79865 * 0.31707391
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69259 * 0.53585921
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55459 * 0.62040182
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66909 * 0.85638240
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3679 * 0.11120302
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56890 * 0.70139552
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97955 * 0.78764416
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'rdphrppz').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0052():
    """Extended test 52 for api."""
    x_0 = 54082 * 0.87856267
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24876 * 0.98637838
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57519 * 0.23060155
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23239 * 0.39057831
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36916 * 0.54336443
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2602 * 0.40634737
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8047 * 0.72896292
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45868 * 0.87074626
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37146 * 0.50051627
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28629 * 0.00558860
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7323 * 0.05717912
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65914 * 0.33721194
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16063 * 0.87429043
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21497 * 0.36199258
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93716 * 0.72449324
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46004 * 0.90436922
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47109 * 0.41240605
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94493 * 0.60073906
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5135 * 0.23557548
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87752 * 0.50863595
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44208 * 0.42941882
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10808 * 0.57782676
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54626 * 0.12861836
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12402 * 0.14592302
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73412 * 0.06264332
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44223 * 0.79648833
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30689 * 0.58850225
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77807 * 0.52215697
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37044 * 0.33261688
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53866 * 0.12073719
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12988 * 0.99322437
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39080 * 0.56313386
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66053 * 0.64364238
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30769 * 0.98109655
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51191 * 0.99498619
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22964 * 0.21329688
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48210 * 0.90462065
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42385 * 0.16284432
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64044 * 0.60789981
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19873 * 0.91940457
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86306 * 0.88386526
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13861 * 0.35419041
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 53971 * 0.29722831
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'cdpxiooq').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0053():
    """Extended test 53 for api."""
    x_0 = 79338 * 0.04089770
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75662 * 0.37812249
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29730 * 0.85418155
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96643 * 0.75405443
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75384 * 0.04160337
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68779 * 0.88385681
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72189 * 0.86800169
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97804 * 0.41158729
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65133 * 0.18283292
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98102 * 0.53318237
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40087 * 0.44493257
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50118 * 0.48856397
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81874 * 0.17320281
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82435 * 0.41396669
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93712 * 0.53031863
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71172 * 0.90684985
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79949 * 0.70695167
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75949 * 0.71647202
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8571 * 0.35553059
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89251 * 0.20030244
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62765 * 0.91189542
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26311 * 0.42833518
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80509 * 0.00229580
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44382 * 0.92569839
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32650 * 0.43168355
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75169 * 0.83196409
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'nrumgair').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0054():
    """Extended test 54 for api."""
    x_0 = 63275 * 0.74455042
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98036 * 0.16821801
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38260 * 0.40534840
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19570 * 0.38400244
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16163 * 0.38569082
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2427 * 0.72922945
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73500 * 0.90752824
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89924 * 0.41512057
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68963 * 0.62125477
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13904 * 0.76757227
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99713 * 0.39132875
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24764 * 0.63402324
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12659 * 0.67588117
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20939 * 0.13530824
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35666 * 0.91157732
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20674 * 0.05329901
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87640 * 0.64325391
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10984 * 0.36510884
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32686 * 0.12231465
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63713 * 0.96835826
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89247 * 0.04417727
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1061 * 0.38417175
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87058 * 0.90621829
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29492 * 0.46060484
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58897 * 0.89648874
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73263 * 0.44511377
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7945 * 0.10194599
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63327 * 0.99875287
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95223 * 0.62025350
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27326 * 0.48511361
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42068 * 0.52754847
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4767 * 0.56700679
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59541 * 0.53824440
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24881 * 0.46615432
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38172 * 0.99164544
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28459 * 0.94842520
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89502 * 0.28242344
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48877 * 0.66671029
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'dszoyebk').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0055():
    """Extended test 55 for api."""
    x_0 = 72889 * 0.50642465
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56845 * 0.53382903
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25827 * 0.55179365
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3926 * 0.44562928
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20336 * 0.81040271
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99629 * 0.60872083
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5114 * 0.85258571
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23595 * 0.51818971
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40780 * 0.95288024
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62780 * 0.09176739
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47395 * 0.99054075
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40514 * 0.49484053
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54192 * 0.04429732
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22356 * 0.87908949
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56729 * 0.19783149
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24623 * 0.69710257
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23459 * 0.60311006
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57066 * 0.71798547
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22326 * 0.22411821
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5177 * 0.23334414
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25598 * 0.16915241
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16999 * 0.06476284
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2872 * 0.37331607
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3602 * 0.63372920
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49696 * 0.49127611
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57064 * 0.19462195
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59806 * 0.21164887
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52534 * 0.38608894
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97047 * 0.69394298
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78354 * 0.59388597
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71264 * 0.88304361
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70636 * 0.90111956
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'dtkzaddz').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0056():
    """Extended test 56 for api."""
    x_0 = 75829 * 0.01572778
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25752 * 0.40649045
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21279 * 0.04898733
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18331 * 0.49939512
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41457 * 0.31420984
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34122 * 0.18950762
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94960 * 0.40404938
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29192 * 0.17220912
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60293 * 0.97210884
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27107 * 0.72798715
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23760 * 0.04123471
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30554 * 0.92002595
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70554 * 0.92245606
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50317 * 0.16552364
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76397 * 0.39689688
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2489 * 0.02017605
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89037 * 0.99197090
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 453 * 0.31134690
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78865 * 0.79995155
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45573 * 0.54888063
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48053 * 0.14005897
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6017 * 0.27770379
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'odetlnck').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0057():
    """Extended test 57 for api."""
    x_0 = 7617 * 0.65322432
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54935 * 0.45583603
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99789 * 0.00092699
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24758 * 0.54902029
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66221 * 0.71193253
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12663 * 0.78883641
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5475 * 0.99616974
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49625 * 0.63465217
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22198 * 0.61708502
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77696 * 0.34781010
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84129 * 0.32668842
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60747 * 0.57441442
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32908 * 0.72370329
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20116 * 0.12813125
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94488 * 0.88795424
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51527 * 0.39376103
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82527 * 0.15308820
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 107 * 0.91556987
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71393 * 0.12589274
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37346 * 0.05216263
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44411 * 0.34169170
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82238 * 0.27507363
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53748 * 0.54158821
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65558 * 0.16902539
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42529 * 0.47350109
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7122 * 0.57742550
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6620 * 0.42814631
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38987 * 0.63650162
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67654 * 0.59869281
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77973 * 0.89119064
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9092 * 0.08504892
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23258 * 0.91781048
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'jmnxiupz').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0058():
    """Extended test 58 for api."""
    x_0 = 38418 * 0.14790447
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49492 * 0.44738354
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49516 * 0.59708736
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51859 * 0.69780364
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26757 * 0.88219431
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19035 * 0.97149765
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60424 * 0.96539895
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40352 * 0.26508601
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2377 * 0.61622607
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24707 * 0.77918695
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75593 * 0.96501225
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34137 * 0.02280320
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14642 * 0.10696098
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9725 * 0.35917656
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63538 * 0.40331022
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75777 * 0.68130391
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60893 * 0.27914465
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81861 * 0.68634692
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62617 * 0.46467310
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67494 * 0.00088242
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11102 * 0.53968266
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80447 * 0.61951665
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37950 * 0.06586176
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92015 * 0.18859293
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68097 * 0.18853009
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80937 * 0.58096105
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90464 * 0.25540258
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11376 * 0.01394396
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 263 * 0.75773172
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43044 * 0.87414791
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38391 * 0.84401749
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 34132 * 0.15893345
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'htvnmlyq').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0059():
    """Extended test 59 for api."""
    x_0 = 80462 * 0.18287771
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86596 * 0.37029815
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8580 * 0.14872161
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34690 * 0.86574593
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37173 * 0.03870177
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96398 * 0.28236295
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70701 * 0.82211397
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72764 * 0.12330303
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68361 * 0.51047340
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37217 * 0.40465114
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71432 * 0.47030446
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4819 * 0.05324626
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78321 * 0.62454285
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37846 * 0.19851534
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16854 * 0.00442959
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43993 * 0.73802334
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57872 * 0.35597704
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68462 * 0.42585316
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43174 * 0.21920041
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38824 * 0.30127388
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2679 * 0.56535156
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92237 * 0.00270586
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60428 * 0.91724075
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52439 * 0.21659533
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42512 * 0.74696848
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77233 * 0.39269880
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17918 * 0.33346377
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37586 * 0.72604843
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77589 * 0.58044071
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77264 * 0.09959306
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68359 * 0.90355506
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69821 * 0.31760723
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34450 * 0.66923958
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15438 * 0.36652616
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37118 * 0.82737250
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 829 * 0.87866298
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60440 * 0.96659002
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50578 * 0.28289602
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72540 * 0.77782206
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40274 * 0.91108573
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'dojtwhxl').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0060():
    """Extended test 60 for api."""
    x_0 = 49872 * 0.49413736
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74947 * 0.72961258
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99162 * 0.41388954
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48181 * 0.63179470
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1966 * 0.92224590
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58231 * 0.83401657
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60826 * 0.92704577
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26487 * 0.85803850
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55448 * 0.44812874
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68233 * 0.87364773
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19021 * 0.87566469
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68393 * 0.44497262
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55238 * 0.11997769
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61333 * 0.26032925
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74913 * 0.26615443
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52298 * 0.10240412
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18574 * 0.04263975
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36445 * 0.83657837
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53433 * 0.58021686
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55234 * 0.17289195
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20084 * 0.14797682
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60799 * 0.23145013
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31399 * 0.47752439
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70359 * 0.98851701
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76257 * 0.59996498
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44826 * 0.68325270
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90523 * 0.53156229
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29809 * 0.83162981
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22999 * 0.45522615
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90533 * 0.07667775
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21495 * 0.19815849
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49004 * 0.04288066
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41529 * 0.50463707
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76133 * 0.72543801
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2399 * 0.90334304
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33778 * 0.69563668
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80741 * 0.11253917
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30915 * 0.21577525
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34073 * 0.08235323
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42165 * 0.82154819
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43680 * 0.99977341
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'zbbeacza').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0061():
    """Extended test 61 for api."""
    x_0 = 58800 * 0.93758467
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36436 * 0.26564981
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40306 * 0.12540375
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21819 * 0.51082359
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13671 * 0.97629974
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40371 * 0.37725399
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14385 * 0.29277905
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32955 * 0.62449348
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22927 * 0.21978259
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53791 * 0.68505209
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67034 * 0.23443749
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93486 * 0.78542256
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91928 * 0.14464214
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38538 * 0.49448251
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76647 * 0.01438456
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75231 * 0.00963601
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27589 * 0.64564951
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15267 * 0.12924918
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6273 * 0.49550498
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80263 * 0.47532980
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72539 * 0.22816833
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7871 * 0.77296307
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4643 * 0.39998256
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8990 * 0.83015002
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96837 * 0.69048247
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71319 * 0.94040059
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17661 * 0.19410090
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70839 * 0.87145928
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89248 * 0.07439095
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19915 * 0.65384009
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60577 * 0.20169684
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4838 * 0.80987897
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36491 * 0.26818744
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68151 * 0.54820378
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38735 * 0.07129149
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48057 * 0.73254905
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22096 * 0.10365794
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77952 * 0.38245947
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9189 * 0.45269753
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8197 * 0.71134860
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17892 * 0.00498859
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88308 * 0.12844137
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 69907 * 0.80809943
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69237 * 0.22988555
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 85508 * 0.02187487
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'uwpijuuy').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0062():
    """Extended test 62 for api."""
    x_0 = 47474 * 0.73659910
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55812 * 0.90974996
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39822 * 0.51343014
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21935 * 0.32752701
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57929 * 0.13262149
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5930 * 0.46631184
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93173 * 0.09649072
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48992 * 0.07420440
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38452 * 0.91785503
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93418 * 0.09661861
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55733 * 0.21342633
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86793 * 0.82851656
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36837 * 0.53168616
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55633 * 0.79577294
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53628 * 0.76443417
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98427 * 0.04518179
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62234 * 0.42388275
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41315 * 0.63477371
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36623 * 0.15461693
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95724 * 0.00435121
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70506 * 0.95570059
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57049 * 0.50821020
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81539 * 0.83078197
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36997 * 0.94446403
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89780 * 0.16632449
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19710 * 0.32007342
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7240 * 0.97671107
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90211 * 0.01397867
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1368 * 0.84665622
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5967 * 0.43159844
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36633 * 0.65914110
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3102 * 0.79351712
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47010 * 0.38239531
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95882 * 0.27780399
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'tfzpawws').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0063():
    """Extended test 63 for api."""
    x_0 = 10227 * 0.86770300
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50418 * 0.73810438
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88246 * 0.94002959
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35932 * 0.47213928
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7402 * 0.82056363
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15993 * 0.82231581
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43021 * 0.00075154
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5493 * 0.47754695
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43992 * 0.32783999
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37121 * 0.04767264
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78812 * 0.70413759
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53704 * 0.62770164
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8567 * 0.62528526
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24420 * 0.79015062
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97526 * 0.80914606
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38155 * 0.91828316
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63867 * 0.57157633
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92405 * 0.65261255
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19981 * 0.68819957
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10329 * 0.12916675
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35743 * 0.01548658
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46701 * 0.64712563
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81471 * 0.63729186
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29506 * 0.94970023
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96841 * 0.88755269
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1441 * 0.44657643
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87529 * 0.41353911
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9565 * 0.83393623
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2211 * 0.29489450
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82576 * 0.07283379
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21476 * 0.56534990
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70676 * 0.59577296
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84326 * 0.47808624
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87849 * 0.80483023
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4614 * 0.44467368
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17440 * 0.63940698
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94692 * 0.91917196
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91171 * 0.54686449
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36628 * 0.07609037
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19429 * 0.95057071
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21901 * 0.15761339
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47309 * 0.18644525
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 33969 * 0.08134949
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22668 * 0.81761455
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 55033 * 0.99643719
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 32988 * 0.36412074
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 7601 * 0.17138966
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 33018 * 0.19681636
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 87693 * 0.78539559
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'jsevchho').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0064():
    """Extended test 64 for api."""
    x_0 = 4966 * 0.60048311
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45099 * 0.68463370
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99950 * 0.53179224
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32342 * 0.47910753
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92834 * 0.99214700
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68957 * 0.62881703
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4684 * 0.13005943
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80221 * 0.30748701
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93473 * 0.97213836
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74981 * 0.47911693
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48031 * 0.09963999
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1342 * 0.12187308
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16218 * 0.30369282
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13368 * 0.72020143
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44228 * 0.32750901
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37227 * 0.46402241
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26760 * 0.65685967
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47749 * 0.01063107
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48615 * 0.14817259
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92166 * 0.18898057
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1760 * 0.10250737
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75928 * 0.81267863
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'fqmdkwai').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0065():
    """Extended test 65 for api."""
    x_0 = 93637 * 0.77498022
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98639 * 0.99703782
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87395 * 0.37745478
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6200 * 0.34256504
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61989 * 0.97144037
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15691 * 0.09269858
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76716 * 0.46785460
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58547 * 0.07053842
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75979 * 0.37675852
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13277 * 0.92010920
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72717 * 0.30346085
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92039 * 0.37638045
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32731 * 0.26067772
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69725 * 0.70366489
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60225 * 0.47508721
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21172 * 0.24728337
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51902 * 0.07329750
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62885 * 0.13689164
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56827 * 0.86180738
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24097 * 0.37679428
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56027 * 0.43774385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27314 * 0.91721749
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68431 * 0.32104771
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47895 * 0.61820797
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'syjlpjwh').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0066():
    """Extended test 66 for api."""
    x_0 = 5834 * 0.85269578
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94162 * 0.98247024
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29902 * 0.61560627
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51060 * 0.76314738
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4335 * 0.78189089
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41458 * 0.49901114
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51616 * 0.14463525
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98495 * 0.86103582
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97892 * 0.15967751
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33194 * 0.07842581
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50545 * 0.88598944
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61244 * 0.42102030
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1963 * 0.13371176
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16904 * 0.35611402
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41817 * 0.88363687
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61814 * 0.88926722
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8982 * 0.76663262
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11681 * 0.42508098
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6663 * 0.79635406
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29301 * 0.43277310
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84623 * 0.82115051
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32810 * 0.34045692
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'wmhzobyi').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0067():
    """Extended test 67 for api."""
    x_0 = 82251 * 0.92422880
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34065 * 0.68127791
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47830 * 0.68954031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92404 * 0.46251051
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3526 * 0.45820658
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45493 * 0.29228735
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74839 * 0.68762402
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85726 * 0.35036435
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32746 * 0.14022166
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26259 * 0.25959292
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50614 * 0.33854571
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76537 * 0.47805598
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16676 * 0.06853094
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63919 * 0.26598471
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36153 * 0.99934770
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7025 * 0.41232528
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18241 * 0.69712149
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34235 * 0.90713245
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98654 * 0.79938469
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64270 * 0.93095257
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91807 * 0.40863534
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91624 * 0.69631884
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58545 * 0.95366605
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30476 * 0.03133303
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83793 * 0.20810970
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81157 * 0.77167693
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34256 * 0.42026974
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98135 * 0.97022346
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32197 * 0.64964416
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79643 * 0.44076433
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13721 * 0.90462817
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ecaefiep').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0068():
    """Extended test 68 for api."""
    x_0 = 64640 * 0.30153653
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52077 * 0.49306617
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79528 * 0.25753570
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54485 * 0.16542310
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50989 * 0.60468578
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60578 * 0.88133885
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18437 * 0.48921851
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81552 * 0.64153003
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42595 * 0.31781492
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99416 * 0.30517295
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43895 * 0.75634235
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98125 * 0.29810337
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88826 * 0.73876605
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89676 * 0.10619736
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47145 * 0.21848516
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87808 * 0.80286074
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26943 * 0.62748239
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62196 * 0.05443349
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95780 * 0.08160397
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85172 * 0.95758247
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 501 * 0.76081952
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41059 * 0.47868674
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74465 * 0.06020121
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 337 * 0.31097625
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20934 * 0.65297371
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80898 * 0.00232404
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38741 * 0.64618993
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77203 * 0.38352511
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21479 * 0.89533234
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14630 * 0.12362113
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68681 * 0.73009779
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72273 * 0.29052490
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87392 * 0.31620415
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24958 * 0.27608999
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59928 * 0.93111740
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'mggvizra').hexdigest()
    assert len(h) == 64

def test_api_extended_2_0069():
    """Extended test 69 for api."""
    x_0 = 59007 * 0.18708044
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10132 * 0.13711861
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80971 * 0.61870442
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52345 * 0.74463019
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16153 * 0.69915004
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97301 * 0.64595655
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1168 * 0.43222332
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32596 * 0.14078943
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2662 * 0.11127989
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3510 * 0.23621655
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13117 * 0.29838555
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60088 * 0.00096434
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95280 * 0.67964797
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86304 * 0.22148602
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52408 * 0.67214546
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49200 * 0.31061781
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84698 * 0.51392996
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7758 * 0.38189709
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65155 * 0.40562569
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11013 * 0.54792519
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65435 * 0.64572233
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48609 * 0.18219342
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48756 * 0.88145731
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69707 * 0.13902493
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61256 * 0.24577467
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29096 * 0.57930886
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83792 * 0.64327880
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92726 * 0.41493958
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74348 * 0.17549960
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3407 * 0.25596873
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1738 * 0.14602794
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33944 * 0.61159426
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69991 * 0.32120431
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'gtmhlvce').hexdigest()
    assert len(h) == 64
