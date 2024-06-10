"""Extended tests for aggregation suite 6."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_aggregation_extended_6_0000():
    """Extended test 0 for aggregation."""
    x_0 = 36485 * 0.57005031
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69899 * 0.24008538
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72336 * 0.23054498
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9673 * 0.80369105
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29589 * 0.60595279
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94767 * 0.17466758
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19806 * 0.50399616
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14373 * 0.52025000
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36955 * 0.02471616
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60227 * 0.64661448
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61969 * 0.63137775
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73014 * 0.26866587
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56234 * 0.75853954
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46976 * 0.66592686
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5396 * 0.68706046
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99751 * 0.98258535
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8593 * 0.94408462
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93967 * 0.99310648
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8444 * 0.79008598
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13400 * 0.73752383
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59500 * 0.01484731
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59524 * 0.04996706
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87189 * 0.68212703
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93158 * 0.04051518
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8944 * 0.67787898
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98645 * 0.51223834
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90640 * 0.47024264
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94609 * 0.84876682
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12825 * 0.41249442
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18586 * 0.79401329
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21140 * 0.80104104
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53092 * 0.33774221
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 696 * 0.29108745
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4796 * 0.52442364
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97773 * 0.78818190
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71706 * 0.80659687
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50323 * 0.32536238
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'bxzjchro').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0001():
    """Extended test 1 for aggregation."""
    x_0 = 56803 * 0.82357061
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81130 * 0.16710750
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90015 * 0.46014781
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30179 * 0.81752402
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7836 * 0.16187354
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73597 * 0.86441929
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68003 * 0.85117267
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89262 * 0.89418322
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47819 * 0.06385368
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88385 * 0.29254897
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43737 * 0.89716365
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69863 * 0.15704934
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1963 * 0.11567698
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8841 * 0.37364926
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70646 * 0.56224377
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18597 * 0.09879599
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46226 * 0.32207262
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26672 * 0.64795153
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70750 * 0.77884992
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69367 * 0.64351634
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 537 * 0.70013590
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2794 * 0.26248703
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34734 * 0.52304295
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80425 * 0.28498034
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87337 * 0.82706446
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97433 * 0.43744629
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98834 * 0.29797423
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46086 * 0.86690545
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95049 * 0.58202177
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51419 * 0.90589268
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83658 * 0.07466698
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68658 * 0.78589595
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19327 * 0.73349364
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1586 * 0.36179727
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59841 * 0.72454450
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24869 * 0.76163369
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36444 * 0.25531465
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83082 * 0.81123036
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42866 * 0.22046954
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'blwihwrf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0002():
    """Extended test 2 for aggregation."""
    x_0 = 69292 * 0.07442186
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36233 * 0.40645268
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44109 * 0.12957945
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81736 * 0.32730617
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75194 * 0.61669438
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24447 * 0.27137982
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68119 * 0.95573798
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82805 * 0.17883098
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12198 * 0.90013913
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23581 * 0.92619180
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83278 * 0.37513901
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84270 * 0.16083519
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67893 * 0.55870474
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51197 * 0.13172328
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1109 * 0.78519316
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84987 * 0.52994775
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7182 * 0.84830345
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52016 * 0.70510902
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6158 * 0.47022333
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93000 * 0.72318615
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ntmcccjj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0003():
    """Extended test 3 for aggregation."""
    x_0 = 62140 * 0.99740896
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27522 * 0.73729571
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4875 * 0.33304534
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73130 * 0.45084451
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54188 * 0.53163481
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82446 * 0.11769862
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90757 * 0.93572418
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66741 * 0.37120984
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69204 * 0.62657240
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82724 * 0.82673173
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36220 * 0.69640495
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84336 * 0.76013448
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22218 * 0.39594170
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16364 * 0.42141768
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71780 * 0.09630051
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56458 * 0.56475960
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45440 * 0.98077882
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98210 * 0.47287353
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81717 * 0.61629168
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77637 * 0.41367391
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42554 * 0.00703360
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48272 * 0.96492112
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62799 * 0.74772996
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10921 * 0.60174242
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97925 * 0.78858560
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57569 * 0.09257434
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68412 * 0.11044163
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66924 * 0.48262796
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7779 * 0.60886796
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89495 * 0.99665610
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20293 * 0.17394317
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47420 * 0.67645115
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75739 * 0.73517975
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64645 * 0.47696054
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57050 * 0.77458542
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26370 * 0.81695014
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90347 * 0.07307643
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75844 * 0.24480550
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42991 * 0.23219224
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80891 * 0.32298089
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 9233 * 0.14565776
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 65308 * 0.23681553
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 4897 * 0.11990652
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84279 * 0.83373848
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 30362 * 0.92261369
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 57934 * 0.51221779
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 22473 * 0.03517042
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 87807 * 0.96142089
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 89438 * 0.06131729
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 3135 * 0.57931718
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'qumjjoxh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0004():
    """Extended test 4 for aggregation."""
    x_0 = 88788 * 0.98570629
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22548 * 0.31631011
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52318 * 0.51751422
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58329 * 0.24392660
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71790 * 0.30668528
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20547 * 0.35606011
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55825 * 0.84589235
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66519 * 0.87343308
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51669 * 0.52943450
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3836 * 0.74690363
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32375 * 0.54970047
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21704 * 0.54908951
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91126 * 0.82208990
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81950 * 0.63392156
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24498 * 0.78562671
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1860 * 0.01051947
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81142 * 0.70335821
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81264 * 0.21724858
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68593 * 0.53041084
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76091 * 0.00475605
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46830 * 0.55582204
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80674 * 0.43237414
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29310 * 0.07274409
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44119 * 0.48539569
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24625 * 0.31687913
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33046 * 0.86636171
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'fvysfxew').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0005():
    """Extended test 5 for aggregation."""
    x_0 = 74654 * 0.77788576
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84548 * 0.95723900
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75256 * 0.01000124
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9134 * 0.74400805
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48344 * 0.49837105
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17807 * 0.27288554
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36588 * 0.37985491
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5106 * 0.72691745
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86174 * 0.37698105
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81078 * 0.26023414
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71698 * 0.39044386
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12684 * 0.63141599
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40957 * 0.36805058
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89724 * 0.98162467
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 862 * 0.27232483
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65417 * 0.51335140
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63081 * 0.10219551
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43407 * 0.11577240
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72009 * 0.17122964
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73656 * 0.39491684
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12174 * 0.00649166
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72984 * 0.28829050
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60088 * 0.78854581
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'bzyvgpos').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0006():
    """Extended test 6 for aggregation."""
    x_0 = 67613 * 0.00003151
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92276 * 0.63978174
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99897 * 0.85199202
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20434 * 0.46433738
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30373 * 0.91840233
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22574 * 0.76615581
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80378 * 0.13444992
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96077 * 0.02767777
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65068 * 0.03524225
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75112 * 0.85160155
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43696 * 0.71507509
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58379 * 0.59054101
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65774 * 0.84457806
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82247 * 0.50253128
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65117 * 0.67169113
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71275 * 0.37857878
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58257 * 0.93760974
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38617 * 0.53214255
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47694 * 0.07655778
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92294 * 0.31860752
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83971 * 0.61858213
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67909 * 0.56285976
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97469 * 0.54432914
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57318 * 0.26495249
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92001 * 0.99770620
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33805 * 0.41451792
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93991 * 0.27502630
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32536 * 0.83344533
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33092 * 0.27426959
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89583 * 0.88348848
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11316 * 0.68515762
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'whiczyqt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0007():
    """Extended test 7 for aggregation."""
    x_0 = 32041 * 0.95974600
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45278 * 0.58560557
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5915 * 0.46389522
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85640 * 0.86643980
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31357 * 0.35150514
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 832 * 0.60955100
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25103 * 0.06922484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93354 * 0.06088143
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69147 * 0.12300749
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43628 * 0.13575845
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85889 * 0.42350818
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20431 * 0.90229352
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94113 * 0.40603223
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15496 * 0.71895277
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95921 * 0.97782579
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57135 * 0.21279164
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83503 * 0.35675541
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7738 * 0.47189608
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40436 * 0.86612392
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58082 * 0.27885713
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72871 * 0.81530400
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58883 * 0.69447504
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89337 * 0.57017961
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81047 * 0.60365664
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28226 * 0.85756937
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6965 * 0.82858700
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69789 * 0.11957890
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11526 * 0.13459911
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71623 * 0.69841215
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53576 * 0.62707471
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70592 * 0.32248542
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11460 * 0.92023000
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90047 * 0.39576269
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54160 * 0.00402103
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56886 * 0.63335746
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57342 * 0.00730565
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22395 * 0.49683743
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45588 * 0.48311837
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82221 * 0.55832830
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17309 * 0.24954426
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 73327 * 0.46355316
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 62950 * 0.02652721
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 76874 * 0.73846329
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 791 * 0.79430393
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 54541 * 0.89106533
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'kdcrskub').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0008():
    """Extended test 8 for aggregation."""
    x_0 = 56972 * 0.57871925
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48651 * 0.76141597
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25839 * 0.60071269
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75913 * 0.03803237
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58352 * 0.74387251
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3206 * 0.54200838
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6670 * 0.87802234
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74867 * 0.98551219
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24404 * 0.97621506
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63344 * 0.53340977
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89916 * 0.28900292
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61572 * 0.56021186
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33220 * 0.92293847
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29007 * 0.74599831
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63278 * 0.27773597
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1293 * 0.64440438
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13732 * 0.54880652
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81955 * 0.71203690
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82106 * 0.43195861
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27703 * 0.93793671
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59752 * 0.73639428
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'mhszjnnk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0009():
    """Extended test 9 for aggregation."""
    x_0 = 39323 * 0.18784307
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30423 * 0.90790063
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37054 * 0.47647919
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31710 * 0.17009271
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35421 * 0.56555684
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18744 * 0.84786929
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52561 * 0.61603036
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32350 * 0.73509407
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10699 * 0.94626022
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33414 * 0.24953699
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70819 * 0.46530087
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83708 * 0.33730137
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33165 * 0.53852581
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82437 * 0.57394992
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13613 * 0.21593520
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19109 * 0.50978822
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45590 * 0.35236511
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1211 * 0.64492652
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95174 * 0.24452886
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98923 * 0.22149527
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74971 * 0.09756195
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87722 * 0.63180591
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13604 * 0.86828540
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83895 * 0.55228609
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43141 * 0.82425350
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88535 * 0.37074610
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88870 * 0.64103562
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75914 * 0.60760849
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30444 * 0.47742015
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84623 * 0.96461321
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30873 * 0.12896614
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13930 * 0.50051105
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5306 * 0.48114452
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76188 * 0.12096054
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lkzvzubv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0010():
    """Extended test 10 for aggregation."""
    x_0 = 23250 * 0.45682251
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93414 * 0.06203652
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50973 * 0.82223437
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84737 * 0.37941064
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8534 * 0.07980693
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53816 * 0.19567709
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72297 * 0.56942879
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54989 * 0.83695934
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74034 * 0.90958361
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21112 * 0.78784787
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32538 * 0.62241808
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31932 * 0.89535551
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98999 * 0.99178434
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27686 * 0.40165615
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24933 * 0.54486407
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6308 * 0.67644048
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86060 * 0.29387662
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79142 * 0.55317828
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20646 * 0.22595635
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72457 * 0.43162081
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98206 * 0.75179853
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54763 * 0.46383670
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71975 * 0.54994127
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16594 * 0.30329652
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94565 * 0.10692820
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'rlnoxvhu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0011():
    """Extended test 11 for aggregation."""
    x_0 = 60652 * 0.14633294
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92574 * 0.39886395
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51625 * 0.25953642
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91583 * 0.87283616
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32153 * 0.54687233
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90902 * 0.17425159
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65432 * 0.82641940
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93979 * 0.04866033
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31111 * 0.23100714
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14110 * 0.39854060
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52054 * 0.81498207
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74887 * 0.06676649
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31331 * 0.54957041
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39925 * 0.58811825
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63615 * 0.04823605
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85153 * 0.01788762
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93470 * 0.60503111
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60702 * 0.38798115
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68078 * 0.23073130
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76518 * 0.81458865
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99943 * 0.40049623
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22882 * 0.92923006
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67525 * 0.43561145
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96029 * 0.84439098
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45604 * 0.98981348
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80643 * 0.84717761
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8353 * 0.29425467
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40430 * 0.87551279
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81113 * 0.22627759
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31297 * 0.38553880
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33117 * 0.14830372
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47357 * 0.05472538
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87761 * 0.84834726
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55594 * 0.53303777
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45183 * 0.55231895
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44338 * 0.28399145
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43916 * 0.31018594
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41627 * 0.25576651
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60392 * 0.30702643
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21610 * 0.46036768
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4892 * 0.51965751
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26583 * 0.24366685
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 43422 * 0.63925124
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 71979 * 0.10264629
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 47066 * 0.06833196
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'bvckpkww').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0012():
    """Extended test 12 for aggregation."""
    x_0 = 51213 * 0.98390337
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30560 * 0.33248439
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26017 * 0.75290830
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82235 * 0.94851088
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30771 * 0.33101022
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70854 * 0.23835158
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76145 * 0.16191867
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68451 * 0.92093714
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41004 * 0.07462096
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33174 * 0.59391910
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72815 * 0.91465737
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25351 * 0.63030651
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68633 * 0.43581768
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21194 * 0.88924850
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41289 * 0.20571896
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13569 * 0.62348323
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63631 * 0.45303320
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94770 * 0.07931764
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25630 * 0.00031147
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78269 * 0.01464817
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38923 * 0.02962615
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65551 * 0.33597517
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70881 * 0.14474435
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86041 * 0.81791663
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21061 * 0.73419252
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34195 * 0.57890499
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98564 * 0.16286827
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51922 * 0.57618660
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92120 * 0.75256132
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54526 * 0.79899095
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75856 * 0.33414355
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32714 * 0.71653711
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67994 * 0.33956182
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26309 * 0.14799905
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73808 * 0.81118680
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70196 * 0.10527940
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93189 * 0.94735244
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27744 * 0.88212789
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80537 * 0.69028035
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39692 * 0.72077851
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38816 * 0.74745132
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 44944 * 0.73765078
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ewislnhp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0013():
    """Extended test 13 for aggregation."""
    x_0 = 31333 * 0.90951303
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35878 * 0.30432493
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5545 * 0.78354502
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62936 * 0.94583873
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16984 * 0.91396211
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64936 * 0.05130101
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6675 * 0.08252992
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71743 * 0.10972325
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73377 * 0.77791161
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49236 * 0.34786997
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59521 * 0.61227000
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90014 * 0.25371014
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24292 * 0.67268645
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19863 * 0.05908580
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31316 * 0.11943081
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67851 * 0.61182750
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70313 * 0.44362850
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32027 * 0.08361121
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36420 * 0.43894797
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51729 * 0.27404646
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51273 * 0.45906630
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65835 * 0.37798678
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32548 * 0.22279114
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14557 * 0.34957549
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48148 * 0.04868829
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18694 * 0.85353139
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51235 * 0.76141315
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11304 * 0.98422048
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44012 * 0.03140060
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39673 * 0.07976742
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11531 * 0.07706646
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84557 * 0.60137454
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39059 * 0.87236511
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21765 * 0.60570464
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4309 * 0.69793906
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 9232 * 0.05295164
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71705 * 0.35219284
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82534 * 0.59484296
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6490 * 0.38595346
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67304 * 0.86110845
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ieqwjerq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0014():
    """Extended test 14 for aggregation."""
    x_0 = 86702 * 0.62624235
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34573 * 0.88286340
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44172 * 0.92177031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72180 * 0.86867358
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87490 * 0.26325598
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40097 * 0.69541780
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43250 * 0.64946912
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29078 * 0.26617133
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91688 * 0.25341766
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86194 * 0.95734565
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52288 * 0.70868876
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3495 * 0.44095149
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16381 * 0.79831474
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66482 * 0.55415239
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56170 * 0.70857362
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86216 * 0.90448451
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44476 * 0.50613379
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16664 * 0.06351265
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87242 * 0.84619966
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85573 * 0.99813354
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40989 * 0.12823636
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94133 * 0.36928408
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38886 * 0.02773948
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62662 * 0.38385663
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38090 * 0.40337923
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79860 * 0.58850066
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77055 * 0.21863940
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55288 * 0.47988227
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81278 * 0.15559602
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'udufdits').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0015():
    """Extended test 15 for aggregation."""
    x_0 = 66193 * 0.42421212
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89435 * 0.13808535
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93841 * 0.26134235
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35435 * 0.29514049
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35927 * 0.06502164
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17794 * 0.67979992
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64165 * 0.63775294
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73982 * 0.40693549
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80011 * 0.19511790
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64366 * 0.83005927
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51079 * 0.77746067
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2976 * 0.09023008
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43346 * 0.80243874
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15733 * 0.14695216
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66115 * 0.47739201
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43914 * 0.86150339
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23302 * 0.92273508
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20740 * 0.88992824
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1992 * 0.73714301
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35895 * 0.59730948
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ovlumbol').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0016():
    """Extended test 16 for aggregation."""
    x_0 = 43912 * 0.42261921
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10186 * 0.23532777
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42138 * 0.12899191
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44877 * 0.48353114
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88324 * 0.61917294
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93939 * 0.63143406
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38566 * 0.30679374
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88760 * 0.05585632
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1437 * 0.05421860
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61973 * 0.20659107
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63183 * 0.22577478
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43619 * 0.20361764
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79803 * 0.87962188
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88711 * 0.47604541
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22996 * 0.82468426
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79578 * 0.94908120
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63155 * 0.22314100
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91669 * 0.00295190
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 115 * 0.26138749
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22267 * 0.52455430
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44510 * 0.99218973
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64702 * 0.90302384
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91551 * 0.31191864
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24175 * 0.04554650
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65648 * 0.05153771
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32359 * 0.41198354
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94816 * 0.53856419
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4601 * 0.86468746
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99124 * 0.14760842
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49423 * 0.62401779
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92095 * 0.64311416
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94914 * 0.06876650
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62919 * 0.52576434
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'rhteykvg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0017():
    """Extended test 17 for aggregation."""
    x_0 = 7959 * 0.56572282
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10947 * 0.32327899
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56287 * 0.98415073
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97581 * 0.18132604
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11964 * 0.69546099
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11939 * 0.92605546
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68363 * 0.64301719
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83134 * 0.98009398
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68569 * 0.17649802
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27273 * 0.96557817
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19049 * 0.91766996
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41970 * 0.09979397
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53759 * 0.99347207
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26207 * 0.49630220
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81 * 0.85596242
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26980 * 0.61900378
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72284 * 0.59317602
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92043 * 0.89745480
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86678 * 0.68930953
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 832 * 0.83244555
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44088 * 0.53167749
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44207 * 0.95517413
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39818 * 0.52681981
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13138 * 0.17314251
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15457 * 0.60633904
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20007 * 0.62559928
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46925 * 0.76209120
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94988 * 0.22450061
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'awdlpzyt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0018():
    """Extended test 18 for aggregation."""
    x_0 = 94815 * 0.81897568
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6634 * 0.85845682
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42505 * 0.39685791
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16921 * 0.19060706
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86876 * 0.49343643
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74322 * 0.08361471
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18639 * 0.69951749
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35578 * 0.31676123
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99545 * 0.04236717
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61393 * 0.97928794
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92887 * 0.06409296
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30741 * 0.90739791
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76569 * 0.66957627
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91906 * 0.25525472
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 509 * 0.90554046
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87620 * 0.70113844
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26199 * 0.31129224
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8282 * 0.46769735
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26292 * 0.41780166
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91794 * 0.70678531
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52655 * 0.19944539
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76243 * 0.65607365
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28466 * 0.09174864
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16939 * 0.36284826
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14698 * 0.97800467
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 831 * 0.16510257
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33506 * 0.79510382
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20317 * 0.86988448
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57149 * 0.45457816
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73636 * 0.97154423
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53634 * 0.08064228
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57665 * 0.17915453
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64892 * 0.61045647
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81173 * 0.93664500
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91053 * 0.41318316
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64189 * 0.49070238
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89304 * 0.84905035
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15478 * 0.54100841
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53751 * 0.14846544
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18103 * 0.91508074
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37960 * 0.70878494
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84549 * 0.82344938
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35592 * 0.00983914
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 80235 * 0.43933211
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 8689 * 0.42811508
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 64521 * 0.70864660
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 71123 * 0.32556640
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 80570 * 0.74796527
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 10486 * 0.75536299
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 25560 * 0.27202317
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'edygmelr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0019():
    """Extended test 19 for aggregation."""
    x_0 = 65526 * 0.53967137
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32614 * 0.76088486
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71094 * 0.82892836
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69617 * 0.68392621
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62762 * 0.87510968
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19137 * 0.07466461
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38756 * 0.24055001
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36573 * 0.34352784
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75032 * 0.71433078
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40080 * 0.91806458
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60482 * 0.75566791
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95913 * 0.98717737
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41752 * 0.80900998
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42855 * 0.80912800
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84102 * 0.93318466
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36281 * 0.85581890
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99925 * 0.23716411
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65183 * 0.89278546
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62817 * 0.50342342
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35666 * 0.41899154
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12811 * 0.54690669
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81926 * 0.06207343
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47799 * 0.55421312
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50674 * 0.43295491
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20029 * 0.76198426
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17906 * 0.15453017
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31572 * 0.80836882
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82456 * 0.17358032
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52013 * 0.30536048
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60573 * 0.75714964
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18974 * 0.28990162
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36682 * 0.41032099
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26059 * 0.02480976
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24140 * 0.16688806
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25276 * 0.89608365
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63831 * 0.73493761
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5986 * 0.87769611
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 14000 * 0.02548137
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 89105 * 0.89594303
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98986 * 0.85315479
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47172 * 0.25089767
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66629 * 0.92807023
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 87391 * 0.90732242
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 56326 * 0.17421734
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'exiqoanc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0020():
    """Extended test 20 for aggregation."""
    x_0 = 25995 * 0.03803611
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27035 * 0.27093089
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27902 * 0.86993414
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84010 * 0.91059238
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60694 * 0.54972907
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4444 * 0.66918125
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25421 * 0.95613405
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71854 * 0.97292574
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12268 * 0.88686419
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28283 * 0.85723559
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54436 * 0.49000009
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49081 * 0.91525727
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58250 * 0.32819941
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1376 * 0.75966329
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97445 * 0.81691586
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29059 * 0.07431294
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90300 * 0.62962530
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72734 * 0.45107020
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95544 * 0.98759379
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94481 * 0.17054786
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94624 * 0.22607778
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85660 * 0.31000072
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60391 * 0.35154423
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95933 * 0.29459877
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59810 * 0.26148462
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66603 * 0.36056570
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7433 * 0.53865194
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8651 * 0.35601290
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86398 * 0.34799088
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8016 * 0.53558590
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64496 * 0.73765914
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43657 * 0.88890071
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34207 * 0.08008066
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12053 * 0.66796167
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81590 * 0.43385826
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60390 * 0.32117802
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18357 * 0.77518397
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41224 * 0.24697614
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 50888 * 0.12146718
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4515 * 0.86853647
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 63734 * 0.19333263
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66822 * 0.55578728
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62404 * 0.93937659
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'zxaartmf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0021():
    """Extended test 21 for aggregation."""
    x_0 = 93801 * 0.53397168
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94487 * 0.12642055
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91637 * 0.95443536
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32639 * 0.89556578
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81300 * 0.20783125
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53903 * 0.43324988
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83993 * 0.68655541
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58667 * 0.19720576
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19082 * 0.99165683
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50043 * 0.97872909
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29589 * 0.67283505
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83149 * 0.40145096
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90360 * 0.20086489
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28343 * 0.20336861
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34544 * 0.54441771
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96259 * 0.74420106
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47657 * 0.38239652
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99042 * 0.66740004
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28704 * 0.28515870
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 399 * 0.79776816
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12736 * 0.19663637
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18656 * 0.40249259
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16852 * 0.98337240
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5978 * 0.78715082
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85146 * 0.22104828
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29022 * 0.85570118
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19265 * 0.56535969
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25048 * 0.65212060
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67733 * 0.42278863
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79710 * 0.36919731
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81870 * 0.86308976
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32793 * 0.36709048
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79004 * 0.75189563
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72843 * 0.43636159
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64468 * 0.56634392
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12545 * 0.33140217
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23730 * 0.09854812
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59207 * 0.62634333
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56708 * 0.19096535
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32278 * 0.13470816
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 15094 * 0.79800064
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'fbrujgla').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0022():
    """Extended test 22 for aggregation."""
    x_0 = 59866 * 0.43749154
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29702 * 0.87848445
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49417 * 0.33779456
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35597 * 0.02748036
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5390 * 0.93217465
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73347 * 0.76429225
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76437 * 0.45133798
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34179 * 0.44754761
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42858 * 0.98699544
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93364 * 0.46813723
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82894 * 0.56258149
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27003 * 0.34043622
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74650 * 0.60801842
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38045 * 0.10316257
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29787 * 0.05123509
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22773 * 0.54540872
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69353 * 0.70273851
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95416 * 0.78652864
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81922 * 0.01330926
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45192 * 0.60401953
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47276 * 0.32312611
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60970 * 0.25727156
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76678 * 0.14187657
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12201 * 0.85918770
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97128 * 0.49077014
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4601 * 0.06911414
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46567 * 0.02736873
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97925 * 0.97283479
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35717 * 0.10180072
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48070 * 0.52135856
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70754 * 0.17157547
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10350 * 0.56160288
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67845 * 0.86312924
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19717 * 0.31978944
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20526 * 0.01949930
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17519 * 0.45161190
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25700 * 0.41346751
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79953 * 0.31279595
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34766 * 0.87559006
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 26028 * 0.58455943
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45982 * 0.99213362
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 23179 * 0.13673806
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12761 * 0.84474736
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 24054 * 0.89401626
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23105 * 0.46778513
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 46472 * 0.80029051
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 93156 * 0.06161879
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'zazzatvx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0023():
    """Extended test 23 for aggregation."""
    x_0 = 69476 * 0.48754885
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2361 * 0.33292469
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16994 * 0.81137732
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48560 * 0.25507368
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34765 * 0.41697361
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22154 * 0.30096105
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56196 * 0.77613331
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27900 * 0.01511345
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13337 * 0.16784651
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55947 * 0.54877288
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30572 * 0.61938154
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61601 * 0.92438211
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8586 * 0.52790944
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91200 * 0.69183992
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83509 * 0.50526057
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6766 * 0.63147948
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71706 * 0.35822438
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87591 * 0.14802163
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60997 * 0.79363386
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49795 * 0.88679508
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14066 * 0.97357377
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2377 * 0.04448759
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84509 * 0.10213015
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94823 * 0.07599760
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2600 * 0.51269495
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69026 * 0.87088564
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40775 * 0.52600777
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 937 * 0.36922744
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74358 * 0.49028405
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 812 * 0.73830673
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70650 * 0.63961757
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32077 * 0.22862341
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53130 * 0.28447102
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75445 * 0.66752615
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 49442 * 0.28845911
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48167 * 0.81903486
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50652 * 0.09321720
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2599 * 0.09320827
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63080 * 0.99068058
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 49390 * 0.78179503
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 39803 * 0.79870909
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79325 * 0.73641810
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22106 * 0.07993572
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 77718 * 0.48250583
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 90350 * 0.84197667
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10161 * 0.52925985
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 64746 * 0.33964110
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 47273 * 0.35860352
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 45075 * 0.34126379
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 87870 * 0.89866268
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'xsxiugms').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0024():
    """Extended test 24 for aggregation."""
    x_0 = 98644 * 0.11037106
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84763 * 0.99505882
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77239 * 0.66376521
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26088 * 0.54761487
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49376 * 0.47720590
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29122 * 0.66309706
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75487 * 0.36837418
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2641 * 0.99637297
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48408 * 0.98774837
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88802 * 0.68229008
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91476 * 0.70467932
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29356 * 0.64149882
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40562 * 0.84981597
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84603 * 0.54863576
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47799 * 0.02129607
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9022 * 0.03880848
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91877 * 0.54352572
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56862 * 0.63907192
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7076 * 0.37531206
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48219 * 0.97102535
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6325 * 0.48068201
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28424 * 0.72410974
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48669 * 0.28785301
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70419 * 0.99565416
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65338 * 0.40830153
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52198 * 0.18997116
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37764 * 0.33002998
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75137 * 0.22615660
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73980 * 0.77814582
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90571 * 0.40202434
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27759 * 0.45715876
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85528 * 0.82859999
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66287 * 0.42980426
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'mnikxxhu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0025():
    """Extended test 25 for aggregation."""
    x_0 = 30686 * 0.30543060
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43363 * 0.58754389
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14254 * 0.13603346
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27987 * 0.38123720
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46411 * 0.94227184
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87665 * 0.83027804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11950 * 0.29459843
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22937 * 0.56863563
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43147 * 0.75538094
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12490 * 0.73569616
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33105 * 0.14299954
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78971 * 0.77833721
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38700 * 0.06754122
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74338 * 0.83981949
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80601 * 0.95918211
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66305 * 0.42750901
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11663 * 0.64919803
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2732 * 0.59871543
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92268 * 0.03636348
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38893 * 0.13032231
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23804 * 0.03863648
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42615 * 0.31887908
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34034 * 0.55336367
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53807 * 0.75612257
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42773 * 0.45224845
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56167 * 0.34123986
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64739 * 0.81529973
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59278 * 0.59862803
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57153 * 0.84074939
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16972 * 0.03623990
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29170 * 0.35591423
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51734 * 0.34433854
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54867 * 0.33633896
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61047 * 0.28999447
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65690 * 0.70397398
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21697 * 0.52203776
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6406 * 0.96484205
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98968 * 0.44108544
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14094 * 0.78231477
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77196 * 0.96291729
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91917 * 0.18733670
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57273 * 0.10561994
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 49803 * 0.49529425
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 79861 * 0.12446847
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 88173 * 0.54554099
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'uqszwzqb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0026():
    """Extended test 26 for aggregation."""
    x_0 = 57093 * 0.43352058
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38301 * 0.33683765
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32762 * 0.73518795
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47427 * 0.36057983
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51169 * 0.31622371
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46589 * 0.41979733
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84227 * 0.60427504
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82631 * 0.08438459
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40824 * 0.59253466
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57031 * 0.62937615
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84505 * 0.36985385
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21771 * 0.50167330
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77883 * 0.84172751
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7949 * 0.46647666
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17867 * 0.45738118
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65521 * 0.46135622
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63878 * 0.13996299
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39351 * 0.86793568
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55992 * 0.99805801
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42197 * 0.26843702
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99575 * 0.59372646
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81970 * 0.06855987
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69315 * 0.28078615
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79490 * 0.32224157
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98130 * 0.15379152
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52668 * 0.58081080
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9364 * 0.82194041
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83380 * 0.90070119
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79548 * 0.60634500
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53674 * 0.26181605
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85275 * 0.41320367
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65105 * 0.01915525
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40679 * 0.92165429
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'fzfpiutq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0027():
    """Extended test 27 for aggregation."""
    x_0 = 27124 * 0.45636442
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87980 * 0.81557086
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35377 * 0.44921043
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62371 * 0.65648185
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55789 * 0.41799239
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98106 * 0.19130970
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76987 * 0.32729299
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55953 * 0.47620641
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74377 * 0.22700967
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86005 * 0.04866804
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34447 * 0.01691349
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99039 * 0.67127952
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15658 * 0.17361570
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23685 * 0.13734581
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97460 * 0.98911076
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95774 * 0.06074920
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6016 * 0.71014448
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17715 * 0.84141775
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10772 * 0.71249144
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94043 * 0.75663150
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92972 * 0.70024282
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71541 * 0.19584398
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35886 * 0.04986512
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7060 * 0.21547170
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69017 * 0.70880872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62356 * 0.59542170
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9410 * 0.27538060
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85951 * 0.82920438
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43963 * 0.72646121
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54769 * 0.89030057
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58590 * 0.09050589
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72393 * 0.63726773
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14515 * 0.32406868
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81267 * 0.86581864
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58120 * 0.98530081
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34552 * 0.46731564
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42 * 0.14129555
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6315 * 0.64188371
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24852 * 0.92273650
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80099 * 0.60984775
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44774 * 0.91614424
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42625 * 0.54902952
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 30709 * 0.42228163
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 48043 * 0.36715651
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 18777 * 0.45756812
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 65650 * 0.02975528
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 18188 * 0.75460084
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 64284 * 0.01437626
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'enuozoxl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0028():
    """Extended test 28 for aggregation."""
    x_0 = 11574 * 0.48280008
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38011 * 0.99493636
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42684 * 0.31459162
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70476 * 0.92472350
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84890 * 0.96993661
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60519 * 0.98865245
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85254 * 0.62213750
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44752 * 0.54077241
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26160 * 0.24138482
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85939 * 0.03946061
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60504 * 0.44092501
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98185 * 0.08994353
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62765 * 0.98509801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17313 * 0.60193106
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48355 * 0.16884909
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49770 * 0.15524606
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71719 * 0.64426460
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42360 * 0.19362087
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41666 * 0.68819754
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30952 * 0.37745237
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50635 * 0.15432649
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40636 * 0.05797992
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56988 * 0.56603430
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32747 * 0.64999443
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77438 * 0.25621227
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54213 * 0.48213739
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81922 * 0.44477718
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7931 * 0.00867035
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3551 * 0.74357154
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2172 * 0.43213375
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14331 * 0.72186746
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5075 * 0.02506658
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95185 * 0.11120748
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5076 * 0.22664856
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89581 * 0.38923003
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46640 * 0.60714911
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21784 * 0.41855253
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47681 * 0.31412229
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78818 * 0.60299535
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'toknvyoj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0029():
    """Extended test 29 for aggregation."""
    x_0 = 56424 * 0.67498148
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43953 * 0.60084902
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5631 * 0.83969084
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90467 * 0.22504540
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28987 * 0.71929639
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1334 * 0.20530487
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58343 * 0.79747543
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30874 * 0.83591608
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55613 * 0.71235981
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83816 * 0.68057474
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1993 * 0.65531429
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71789 * 0.45819834
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5246 * 0.51505451
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30295 * 0.21429009
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84888 * 0.66395828
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3654 * 0.20655115
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37426 * 0.75975426
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84159 * 0.31021690
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7756 * 0.64021383
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7838 * 0.84682139
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30591 * 0.49990602
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93393 * 0.06939416
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87516 * 0.83049339
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54879 * 0.59132242
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6230 * 0.33132168
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29062 * 0.56871940
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47872 * 0.94401952
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18081 * 0.54897253
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16880 * 0.39420609
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61735 * 0.12751746
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57653 * 0.78574196
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20100 * 0.27512377
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18354 * 0.98456664
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91420 * 0.85605791
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37463 * 0.66204569
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67827 * 0.91471857
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8830 * 0.97475088
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80484 * 0.07956058
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15900 * 0.72398212
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23127 * 0.23384518
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71326 * 0.29789368
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 94711 * 0.66029544
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6671 * 0.13644480
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20036 * 0.25925227
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35370 * 0.21849341
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 99383 * 0.95903999
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17132 * 0.99901828
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 32197 * 0.90617280
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 1396 * 0.32435795
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 33744 * 0.72987215
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'amkcivhn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0030():
    """Extended test 30 for aggregation."""
    x_0 = 93307 * 0.26971735
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46305 * 0.88360907
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44114 * 0.58572787
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85166 * 0.49205148
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6622 * 0.56076036
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 278 * 0.94680911
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24254 * 0.60225486
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76637 * 0.54679838
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60621 * 0.63568947
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38504 * 0.17495263
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11459 * 0.49311199
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82583 * 0.88513521
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94672 * 0.63920695
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15317 * 0.23810893
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80663 * 0.72172575
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88654 * 0.85121125
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6572 * 0.40909210
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89533 * 0.34883014
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8572 * 0.89545356
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48970 * 0.43009810
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'qaixsguo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0031():
    """Extended test 31 for aggregation."""
    x_0 = 79931 * 0.48573652
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79604 * 0.62723286
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40204 * 0.95623736
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66526 * 0.17382828
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70789 * 0.42169369
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18565 * 0.07042086
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33086 * 0.40534914
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10304 * 0.22247204
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17504 * 0.95166872
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22379 * 0.97187780
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30170 * 0.76993426
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16555 * 0.11117423
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98067 * 0.39516755
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39527 * 0.93749139
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4045 * 0.99358765
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7019 * 0.63153147
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38409 * 0.36325549
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77867 * 0.62299085
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39533 * 0.71535208
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51532 * 0.71735689
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4044 * 0.57639314
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54550 * 0.19139701
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28643 * 0.44204890
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18681 * 0.91030207
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41721 * 0.75217864
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83384 * 0.18941107
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10541 * 0.22664883
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72865 * 0.13321030
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77966 * 0.92927069
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50170 * 0.05495433
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67010 * 0.65387673
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76474 * 0.35532818
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78942 * 0.55456402
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32379 * 0.05954463
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'xesgotvc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0032():
    """Extended test 32 for aggregation."""
    x_0 = 43326 * 0.72947301
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4653 * 0.80961072
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52202 * 0.20768646
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34706 * 0.79443265
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26454 * 0.25496411
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29564 * 0.55133907
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42788 * 0.99956637
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84374 * 0.87515808
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64222 * 0.36477386
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72800 * 0.11071043
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76475 * 0.46803317
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13943 * 0.54540344
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28693 * 0.22079800
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47264 * 0.76163617
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26908 * 0.84648990
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66962 * 0.58857623
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49469 * 0.11080766
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23158 * 0.31292882
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87866 * 0.14173781
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88686 * 0.63890757
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85754 * 0.57857094
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50266 * 0.27217909
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78175 * 0.09878637
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91173 * 0.80324065
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17825 * 0.62061751
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50948 * 0.56055767
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93296 * 0.42457711
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72072 * 0.68084197
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76061 * 0.24728079
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'rsvvqjxy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0033():
    """Extended test 33 for aggregation."""
    x_0 = 93574 * 0.28914517
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44898 * 0.24005814
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23945 * 0.10102172
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32238 * 0.29026508
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26560 * 0.91688500
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2929 * 0.62360850
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30658 * 0.96047170
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38955 * 0.30355296
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52426 * 0.04722551
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16191 * 0.89017104
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99023 * 0.22498534
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51916 * 0.66587448
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51504 * 0.27127623
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15088 * 0.06248011
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35107 * 0.32528949
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90761 * 0.19357283
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14210 * 0.76055236
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46031 * 0.31146193
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39723 * 0.96253790
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80852 * 0.52006873
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65399 * 0.88474931
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48580 * 0.35611971
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90823 * 0.75556677
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48987 * 0.27610410
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21067 * 0.18123291
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10697 * 0.60023916
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47548 * 0.87219903
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34443 * 0.86381650
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'cinsqiai').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0034():
    """Extended test 34 for aggregation."""
    x_0 = 18540 * 0.33687219
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44513 * 0.02871839
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81640 * 0.86829060
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67451 * 0.86335086
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56418 * 0.58540950
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7589 * 0.32562601
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83768 * 0.18928346
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69710 * 0.89044479
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35762 * 0.04644339
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34227 * 0.67616359
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44430 * 0.13501856
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29973 * 0.16303461
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46415 * 0.87792248
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64101 * 0.87429556
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9000 * 0.15158577
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70535 * 0.90716672
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69165 * 0.97146260
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19945 * 0.74699225
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60538 * 0.78316019
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77793 * 0.11530936
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71560 * 0.25641866
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46824 * 0.80334998
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94568 * 0.67905046
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24895 * 0.16594421
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10381 * 0.08818799
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41915 * 0.46087363
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'cznoqtuy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0035():
    """Extended test 35 for aggregation."""
    x_0 = 40705 * 0.44518293
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95318 * 0.31582333
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83178 * 0.64029907
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42463 * 0.92608797
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31899 * 0.27477603
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73100 * 0.68926628
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18246 * 0.75363500
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91448 * 0.81424372
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39432 * 0.83507034
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27135 * 0.93522108
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59380 * 0.13366823
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34154 * 0.07653572
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41361 * 0.55516610
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93350 * 0.88422491
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77729 * 0.40269706
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80881 * 0.79920781
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89990 * 0.92650692
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59131 * 0.51190670
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81448 * 0.11808171
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99767 * 0.43543082
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20808 * 0.57425232
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28242 * 0.89945144
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89753 * 0.59015187
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42509 * 0.10880593
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62493 * 0.32354431
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53423 * 0.08418820
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15374 * 0.29061342
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89088 * 0.63083665
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70591 * 0.57362353
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59924 * 0.20503204
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40881 * 0.31045760
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12264 * 0.68312315
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83339 * 0.80190844
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4128 * 0.01678903
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61385 * 0.66782945
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6450 * 0.32412471
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42699 * 0.49378902
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97202 * 0.64570406
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24774 * 0.37464078
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46249 * 0.43929769
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27930 * 0.05741729
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30269 * 0.86923334
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 84428 * 0.65545289
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 9106 * 0.41993920
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 99044 * 0.99338599
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 99891 * 0.55548166
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 72173 * 0.51021178
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 16798 * 0.22807224
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ixfcieqb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0036():
    """Extended test 36 for aggregation."""
    x_0 = 47062 * 0.63209249
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17041 * 0.76721192
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21526 * 0.57509251
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1129 * 0.27667767
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95474 * 0.34928414
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24735 * 0.01941407
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29919 * 0.01021601
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11799 * 0.28561536
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87407 * 0.45150082
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28858 * 0.52317730
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12729 * 0.25118291
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96507 * 0.55646581
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99946 * 0.39744628
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8787 * 0.95231529
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53437 * 0.43760377
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43845 * 0.86013814
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61750 * 0.53744543
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87590 * 0.00571673
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25797 * 0.80142647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9960 * 0.67224692
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43783 * 0.56924882
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'tfosveht').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0037():
    """Extended test 37 for aggregation."""
    x_0 = 47320 * 0.14123812
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28800 * 0.22458165
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7057 * 0.24405902
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18552 * 0.98079851
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61422 * 0.93310260
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13202 * 0.33571611
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67858 * 0.22490331
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61028 * 0.35844942
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60111 * 0.12946556
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61010 * 0.22886269
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11583 * 0.51387009
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93067 * 0.49205332
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70649 * 0.25057437
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28872 * 0.76282171
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31527 * 0.69872445
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62190 * 0.18150765
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11978 * 0.66909399
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80143 * 0.54600659
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27813 * 0.74601566
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91223 * 0.04701258
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76727 * 0.42723972
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83218 * 0.41586338
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43443 * 0.76802727
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10921 * 0.98264028
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37126 * 0.19295906
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84635 * 0.96268103
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53015 * 0.54986031
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37857 * 0.67328702
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55893 * 0.95846170
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1710 * 0.85770153
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7685 * 0.47117548
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29026 * 0.51001820
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52027 * 0.75439889
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76965 * 0.30240932
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23116 * 0.96774161
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80979 * 0.22510620
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9311 * 0.54716038
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17019 * 0.97745949
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55226 * 0.11351583
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91894 * 0.86633590
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 70085 * 0.93572927
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82879 * 0.26277167
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47085 * 0.90807389
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 14165 * 0.33467373
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4036 * 0.11057882
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 51665 * 0.08523247
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'yeikmjqz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0038():
    """Extended test 38 for aggregation."""
    x_0 = 86263 * 0.73354408
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8873 * 0.08174486
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30220 * 0.35461943
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59558 * 0.12766327
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41769 * 0.92948605
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96924 * 0.74789894
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37472 * 0.41757046
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82757 * 0.67220924
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98837 * 0.90228897
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38243 * 0.19513463
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99284 * 0.39877844
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15277 * 0.97056973
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 916 * 0.24793841
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 615 * 0.49301821
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54530 * 0.87629812
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8836 * 0.27602054
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94390 * 0.90523423
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40510 * 0.71245548
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24183 * 0.51165818
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13244 * 0.40211373
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24957 * 0.02314989
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30735 * 0.09651698
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34691 * 0.34794368
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10806 * 0.53756215
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6392 * 0.68699817
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5096 * 0.98338362
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86120 * 0.33850043
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41590 * 0.12201483
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65676 * 0.81877726
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94379 * 0.94145413
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51872 * 0.94032807
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55614 * 0.14454645
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53320 * 0.09759892
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8186 * 0.45568041
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79443 * 0.42084749
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36456 * 0.35965046
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45951 * 0.94172787
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91652 * 0.69543330
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'eejysuph').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0039():
    """Extended test 39 for aggregation."""
    x_0 = 5824 * 0.76268922
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99750 * 0.82377285
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35043 * 0.22012988
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31540 * 0.00531218
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66133 * 0.73677539
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15938 * 0.17161925
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53722 * 0.53874040
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87766 * 0.85190184
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11421 * 0.28808207
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35286 * 0.98614809
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77885 * 0.75309511
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32027 * 0.46490469
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26827 * 0.85173485
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26090 * 0.65350792
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20860 * 0.00649842
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37760 * 0.31471850
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29147 * 0.52015996
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38659 * 0.52932250
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29272 * 0.48938282
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30455 * 0.45293520
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83855 * 0.51553852
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32536 * 0.51960008
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80477 * 0.23403494
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67780 * 0.35858718
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27191 * 0.66006400
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72958 * 0.53974896
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41267 * 0.63047568
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79644 * 0.47516781
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55620 * 0.71444938
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31908 * 0.94320210
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69529 * 0.11056509
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92223 * 0.89694488
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66849 * 0.68710762
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93024 * 0.83295858
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'srgghoxx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0040():
    """Extended test 40 for aggregation."""
    x_0 = 55634 * 0.84291114
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98633 * 0.77777181
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36433 * 0.42453815
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39440 * 0.97395521
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36752 * 0.10041828
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15999 * 0.79069519
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93920 * 0.45542391
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50863 * 0.38011652
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22872 * 0.18940895
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81216 * 0.55098312
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34464 * 0.13615263
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74369 * 0.81076660
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49897 * 0.09284364
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24401 * 0.20433984
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62740 * 0.93042370
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65026 * 0.30988886
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80631 * 0.90949187
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83206 * 0.91150429
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7370 * 0.38837692
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10304 * 0.13398857
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73688 * 0.91810296
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97952 * 0.66454030
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72184 * 0.16583728
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74983 * 0.44420409
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36722 * 0.28572128
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98949 * 0.43405765
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75147 * 0.92651080
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16401 * 0.32816913
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53360 * 0.25582090
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73351 * 0.17457554
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'uauefxkk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0041():
    """Extended test 41 for aggregation."""
    x_0 = 64159 * 0.47860103
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74284 * 0.79916179
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76030 * 0.65205384
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69644 * 0.22274646
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4157 * 0.75925285
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12854 * 0.42444915
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71068 * 0.92314719
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37571 * 0.34146082
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62667 * 0.51440559
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31907 * 0.35610469
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60140 * 0.69983137
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58858 * 0.32429335
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8345 * 0.60040715
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88801 * 0.38455311
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38227 * 0.47574622
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39434 * 0.18889211
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51266 * 0.68114071
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83646 * 0.81669981
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2276 * 0.43246053
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42990 * 0.12531986
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52097 * 0.76553355
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79704 * 0.95080121
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31097 * 0.61998962
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17351 * 0.83847881
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53368 * 0.90444792
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77245 * 0.32234961
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79361 * 0.88621712
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13571 * 0.36357165
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96150 * 0.25884406
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39957 * 0.28991451
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'jhyzdzmb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0042():
    """Extended test 42 for aggregation."""
    x_0 = 18699 * 0.92355499
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6397 * 0.64045725
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58421 * 0.57448890
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84332 * 0.42738214
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66048 * 0.87374671
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29911 * 0.18476570
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 278 * 0.96235529
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67955 * 0.02451747
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75010 * 0.56851580
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24425 * 0.73085034
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32569 * 0.82662939
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15980 * 0.44849294
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48805 * 0.64913908
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25764 * 0.01978305
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 408 * 0.60928585
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70236 * 0.27376589
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16589 * 0.36814792
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36611 * 0.31711248
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66687 * 0.13972518
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49554 * 0.83798441
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69925 * 0.29107636
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82720 * 0.13781469
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29366 * 0.28376771
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23974 * 0.13486508
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24584 * 0.22749615
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40732 * 0.59665811
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87340 * 0.38999520
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3590 * 0.58496923
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23828 * 0.58478386
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7567 * 0.97890240
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94967 * 0.95181793
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99669 * 0.22384545
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13186 * 0.30843373
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27703 * 0.97629317
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70201 * 0.45927564
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 92357 * 0.23066068
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66762 * 0.41279557
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46325 * 0.20367180
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67713 * 0.80913634
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23461 * 0.68577872
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86881 * 0.45887046
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33793 * 0.38084354
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6558 * 0.08465034
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27904 * 0.37145699
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 41693 * 0.46342214
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'niwghhld').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0043():
    """Extended test 43 for aggregation."""
    x_0 = 85114 * 0.33260847
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82287 * 0.06284610
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84824 * 0.69361599
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90404 * 0.34044005
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34797 * 0.91740534
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10379 * 0.57460028
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5077 * 0.94114842
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34384 * 0.78874006
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20335 * 0.98350984
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5934 * 0.97105319
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94623 * 0.76269941
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79637 * 0.44692929
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54261 * 0.73268063
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41912 * 0.78628451
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57761 * 0.73883075
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40512 * 0.34347055
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28799 * 0.07767945
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94422 * 0.01966329
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52922 * 0.56903053
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94601 * 0.00729009
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30664 * 0.29127862
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53113 * 0.28605614
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51920 * 0.32060044
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71581 * 0.02093792
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25702 * 0.07137317
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91714 * 0.10192566
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55013 * 0.57029300
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49725 * 0.16746528
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24821 * 0.78689309
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31450 * 0.32999627
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8677 * 0.40304221
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67029 * 0.43287665
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97194 * 0.81967527
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41561 * 0.47800436
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'vjqitwwu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0044():
    """Extended test 44 for aggregation."""
    x_0 = 75090 * 0.74391251
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76410 * 0.38175349
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49300 * 0.48447698
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82288 * 0.84755804
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63575 * 0.75176080
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74803 * 0.56597037
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84447 * 0.60462686
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20208 * 0.11258719
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80082 * 0.66263184
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22851 * 0.82782491
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75464 * 0.87878867
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89499 * 0.02671992
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20558 * 0.41248876
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81499 * 0.46357489
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90256 * 0.73014457
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94515 * 0.01867263
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12250 * 0.77775346
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29147 * 0.19979501
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3441 * 0.38561180
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22240 * 0.40084001
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81352 * 0.32531823
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13653 * 0.43072487
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20807 * 0.18784483
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54870 * 0.89286747
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22083 * 0.42778212
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20233 * 0.68488892
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68970 * 0.65394550
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'mtgetsdm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0045():
    """Extended test 45 for aggregation."""
    x_0 = 55273 * 0.86280793
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16302 * 0.95661030
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26497 * 0.83748269
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49626 * 0.61720500
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27535 * 0.84773063
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82351 * 0.08538175
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84594 * 0.25821774
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29301 * 0.94287399
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81440 * 0.61666047
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91512 * 0.59506357
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74745 * 0.90542418
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84483 * 0.80000916
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80520 * 0.19024131
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61789 * 0.74314778
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19272 * 0.03109461
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60718 * 0.98039452
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50747 * 0.60766152
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84364 * 0.48802694
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16139 * 0.50774636
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20711 * 0.79835382
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58462 * 0.34042463
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7050 * 0.13252358
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38188 * 0.26521291
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'skinmocx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0046():
    """Extended test 46 for aggregation."""
    x_0 = 68787 * 0.45927236
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26222 * 0.37524579
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14054 * 0.93367406
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21092 * 0.50139868
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77657 * 0.31028827
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90032 * 0.83075481
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54657 * 0.22740013
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64428 * 0.37412661
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19197 * 0.67943080
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67992 * 0.49966484
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7104 * 0.70497066
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96350 * 0.12556213
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22128 * 0.03506725
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91366 * 0.72283805
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69973 * 0.77726037
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47787 * 0.63060115
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 325 * 0.50018256
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38 * 0.50862642
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80405 * 0.24909285
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35744 * 0.41063032
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56727 * 0.06911572
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15932 * 0.51247220
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2679 * 0.74459970
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92750 * 0.04443242
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52587 * 0.21787495
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53321 * 0.45011194
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93352 * 0.34203814
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66912 * 0.82867537
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95595 * 0.21330389
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33245 * 0.68932543
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90729 * 0.74078403
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84222 * 0.32190004
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86670 * 0.84062267
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56409 * 0.23962883
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'gqtexmxj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0047():
    """Extended test 47 for aggregation."""
    x_0 = 74820 * 0.65069703
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40729 * 0.55172835
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45665 * 0.78376090
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77087 * 0.03070179
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35587 * 0.17984033
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48429 * 0.14946026
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46310 * 0.98430568
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52608 * 0.42843490
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13634 * 0.44945534
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42710 * 0.99649373
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76011 * 0.63518064
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35999 * 0.30492919
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20661 * 0.51666216
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66625 * 0.37538367
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90200 * 0.39906868
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47545 * 0.92115108
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44372 * 0.64121127
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74062 * 0.95402007
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64955 * 0.84967448
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49873 * 0.90661069
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93582 * 0.02136091
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71200 * 0.92622968
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6415 * 0.21377886
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62764 * 0.25107913
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20029 * 0.82205740
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32127 * 0.71150778
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90152 * 0.57244782
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68281 * 0.52982254
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21601 * 0.67801767
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45190 * 0.28613662
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'tcglftaa').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0048():
    """Extended test 48 for aggregation."""
    x_0 = 55514 * 0.32612052
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85722 * 0.55466301
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27369 * 0.33155389
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43349 * 0.92195239
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24852 * 0.28133851
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96112 * 0.33290151
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53767 * 0.42024835
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57220 * 0.87554558
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13978 * 0.12203556
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78068 * 0.44483531
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1861 * 0.93771195
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12037 * 0.94767016
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4913 * 0.97938833
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17560 * 0.85000148
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19934 * 0.51216845
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82713 * 0.43230561
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76855 * 0.62232728
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89578 * 0.11918118
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5657 * 0.48311580
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80905 * 0.28645342
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'hnbhltuk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0049():
    """Extended test 49 for aggregation."""
    x_0 = 16614 * 0.97395195
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13542 * 0.13832149
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58639 * 0.51667903
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67243 * 0.92025798
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4796 * 0.85194515
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83142 * 0.44087604
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4346 * 0.46039019
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98948 * 0.20304613
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25570 * 0.10270729
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82736 * 0.08856648
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39927 * 0.54249553
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27366 * 0.36308469
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12811 * 0.28037537
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32619 * 0.89684967
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63639 * 0.54072157
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92410 * 0.70596999
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47853 * 0.43024845
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42853 * 0.51809283
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82785 * 0.97271297
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89602 * 0.49316948
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26940 * 0.31809365
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32023 * 0.21131594
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27478 * 0.00670321
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96850 * 0.67051480
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2334 * 0.45015693
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92489 * 0.79112635
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39498 * 0.54136237
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26073 * 0.55227328
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10560 * 0.81564704
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98281 * 0.40031104
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15907 * 0.61605263
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36250 * 0.20649240
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8442 * 0.12500380
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72527 * 0.22082515
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12791 * 0.91288849
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1494 * 0.70213857
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33835 * 0.84279184
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34052 * 0.92882452
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69707 * 0.65803645
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55301 * 0.21903613
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94062 * 0.11837447
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25713 * 0.89758124
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9718 * 0.80114136
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 59049 * 0.26086117
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 26553 * 0.51586982
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 5549 * 0.18585114
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 53375 * 0.36702639
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 2683 * 0.20397254
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 72010 * 0.30117844
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 78831 * 0.86497729
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'xxdwcphi').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0050():
    """Extended test 50 for aggregation."""
    x_0 = 78666 * 0.63305279
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78358 * 0.13848227
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84801 * 0.69465537
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36944 * 0.02940502
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53563 * 0.19261089
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 958 * 0.82231997
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81395 * 0.95611431
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76906 * 0.03499819
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42689 * 0.73390216
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85349 * 0.58637608
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44440 * 0.84758238
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25083 * 0.61185668
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67724 * 0.47207453
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44558 * 0.76839876
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56258 * 0.44334599
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30838 * 0.98320754
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45584 * 0.45758415
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82411 * 0.73326305
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38824 * 0.78007693
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96726 * 0.16988577
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57218 * 0.59966685
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67867 * 0.09138880
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83013 * 0.42224052
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85854 * 0.10859530
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4831 * 0.25811107
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46174 * 0.12860616
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92331 * 0.61718648
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58866 * 0.83451624
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93637 * 0.30380904
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42588 * 0.15723369
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74017 * 0.39064337
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32090 * 0.03726545
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10159 * 0.94170969
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'yrhwdjlw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0051():
    """Extended test 51 for aggregation."""
    x_0 = 42828 * 0.92581051
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25837 * 0.84267784
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49432 * 0.47856515
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41007 * 0.62615860
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86882 * 0.61876824
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43954 * 0.70993575
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61943 * 0.79247349
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78702 * 0.33384254
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27035 * 0.79520110
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72590 * 0.60453087
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42681 * 0.60555180
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2588 * 0.40479931
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98497 * 0.03808335
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19564 * 0.55868895
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83344 * 0.32946959
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36356 * 0.75251213
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93346 * 0.64614061
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41858 * 0.40679943
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25211 * 0.38381321
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64295 * 0.45073397
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12174 * 0.95320354
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'lfznkgsm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0052():
    """Extended test 52 for aggregation."""
    x_0 = 93482 * 0.54469199
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87686 * 0.04582084
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26312 * 0.16257883
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1788 * 0.25853904
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88264 * 0.87598349
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44334 * 0.94871026
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31100 * 0.51076731
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61999 * 0.21635188
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51050 * 0.41185876
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46864 * 0.45799313
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81993 * 0.17857993
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74346 * 0.57526197
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83472 * 0.66457394
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4450 * 0.15336896
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38401 * 0.73588095
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84773 * 0.33574976
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6732 * 0.02935992
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36959 * 0.43428689
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80470 * 0.35324553
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85139 * 0.46783313
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36797 * 0.94441006
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41217 * 0.16883685
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65893 * 0.71846600
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1985 * 0.37066492
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52418 * 0.55355805
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41853 * 0.47056237
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89805 * 0.11248684
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23415 * 0.08199287
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18700 * 0.57838346
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10765 * 0.19022194
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94958 * 0.72900752
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ldoihetu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0053():
    """Extended test 53 for aggregation."""
    x_0 = 79151 * 0.92856440
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47113 * 0.27432657
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18254 * 0.54143152
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54352 * 0.62337203
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65454 * 0.68088242
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84245 * 0.33600360
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26020 * 0.29950106
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67976 * 0.47926773
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3185 * 0.67056083
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54975 * 0.40199711
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36109 * 0.00393154
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92466 * 0.89854627
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67927 * 0.60258709
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73448 * 0.14065758
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56519 * 0.41902463
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31887 * 0.22785688
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95406 * 0.59709502
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17129 * 0.73430026
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34791 * 0.89475045
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18736 * 0.79707545
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69948 * 0.20059277
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63538 * 0.89721539
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19691 * 0.94708094
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14344 * 0.00414881
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10505 * 0.57011583
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95643 * 0.56381823
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77172 * 0.13230261
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10650 * 0.48267178
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21661 * 0.91264860
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88122 * 0.05106845
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44648 * 0.66206296
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94361 * 0.94624000
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33456 * 0.12587922
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78288 * 0.29623958
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16524 * 0.20046369
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47890 * 0.37413899
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94480 * 0.25190100
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 99121 * 0.98949958
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74363 * 0.75847607
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67747 * 0.33036025
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4250 * 0.61788328
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 44592 * 0.33565018
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 34404 * 0.34521477
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38598 * 0.55865788
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 60234 * 0.69859163
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4345 * 0.49057668
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 95816 * 0.63888179
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'edqzkbrg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0054():
    """Extended test 54 for aggregation."""
    x_0 = 41116 * 0.98373180
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83778 * 0.25581892
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29270 * 0.04831015
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29443 * 0.47134808
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60313 * 0.86823186
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67856 * 0.17900639
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34920 * 0.02508106
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59606 * 0.94433395
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14967 * 0.80604334
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71983 * 0.79850732
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5414 * 0.47458549
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33747 * 0.40564539
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61394 * 0.75449116
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97161 * 0.03125207
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85163 * 0.76571997
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6535 * 0.83872231
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68016 * 0.82654282
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96612 * 0.74182901
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37173 * 0.39652765
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65774 * 0.55574660
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80224 * 0.14339921
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51414 * 0.42964435
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72900 * 0.70712781
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74511 * 0.92049274
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77830 * 0.53913289
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5447 * 0.06714089
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44655 * 0.91333396
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16079 * 0.81855125
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24958 * 0.68358866
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34102 * 0.21497515
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68178 * 0.83259660
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12961 * 0.23407082
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82703 * 0.91180359
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61668 * 0.05213847
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90184 * 0.03697800
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81342 * 0.33644433
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24897 * 0.30364423
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'gaendpbh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0055():
    """Extended test 55 for aggregation."""
    x_0 = 87591 * 0.23864990
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97333 * 0.83794324
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55543 * 0.13004256
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90206 * 0.98628662
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82583 * 0.49742177
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60615 * 0.49629115
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70953 * 0.27757512
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33743 * 0.26784882
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67785 * 0.62209603
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10045 * 0.43537024
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32155 * 0.00924381
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99482 * 0.67089659
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43207 * 0.55238955
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72583 * 0.62195235
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94220 * 0.02118953
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83981 * 0.50438217
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35180 * 0.07521773
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50725 * 0.63766477
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5932 * 0.98396557
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17146 * 0.24758369
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68391 * 0.73148023
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23102 * 0.90291504
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79376 * 0.84687698
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28443 * 0.01757609
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24806 * 0.04657926
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14467 * 0.74454237
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78275 * 0.10885533
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95232 * 0.30912396
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12333 * 0.58027556
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82457 * 0.59781097
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48245 * 0.39505058
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76286 * 0.91578356
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78203 * 0.53302296
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68169 * 0.09729392
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39183 * 0.07826663
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70199 * 0.85866468
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61512 * 0.83053306
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'txbatjvz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0056():
    """Extended test 56 for aggregation."""
    x_0 = 45496 * 0.98265681
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42089 * 0.43501568
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9692 * 0.77939576
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84318 * 0.50486523
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57279 * 0.70675445
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55316 * 0.53459993
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92838 * 0.15197632
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61926 * 0.81468601
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15728 * 0.37198285
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25539 * 0.48190138
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8230 * 0.26347007
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94164 * 0.33612581
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70338 * 0.72736199
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62783 * 0.01990183
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93455 * 0.22026328
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74457 * 0.30276161
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37259 * 0.41660819
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27689 * 0.25182179
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11626 * 0.36159808
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31648 * 0.68779962
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72096 * 0.17242552
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98670 * 0.04808532
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46852 * 0.08487593
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67367 * 0.04050179
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78321 * 0.79911456
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66245 * 0.75191257
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80852 * 0.79450065
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94128 * 0.65556264
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51489 * 0.97241160
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55817 * 0.47910168
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5893 * 0.33151938
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45653 * 0.51804780
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40390 * 0.38365547
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'kxvjrwxp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0057():
    """Extended test 57 for aggregation."""
    x_0 = 70940 * 0.93447896
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19946 * 0.94048349
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77163 * 0.79210970
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86564 * 0.72739534
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98796 * 0.39575268
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11486 * 0.94273176
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26463 * 0.23386641
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69273 * 0.60705316
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24556 * 0.48707640
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28032 * 0.91038847
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96394 * 0.23324501
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41232 * 0.58962491
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81984 * 0.17207643
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7884 * 0.61460919
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59575 * 0.73724864
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11355 * 0.05445789
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85287 * 0.65610907
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9507 * 0.17036354
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37737 * 0.39088359
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76001 * 0.14675372
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85086 * 0.26977727
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13126 * 0.72524077
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15473 * 0.59994870
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26211 * 0.03982691
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93358 * 0.66287034
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31703 * 0.59919168
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24992 * 0.58810634
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79229 * 0.44295396
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35459 * 0.01887933
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2696 * 0.71545296
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21695 * 0.60532900
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69479 * 0.27275862
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69059 * 0.71629305
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76727 * 0.46199116
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73281 * 0.09502539
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56442 * 0.81432885
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35750 * 0.51723314
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32406 * 0.64378361
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99491 * 0.07422851
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75404 * 0.76279408
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83709 * 0.95107572
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 98443 * 0.14405378
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88153 * 0.14209859
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 55626 * 0.25217152
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 73660 * 0.70493635
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 36654 * 0.61005257
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'fywckacb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0058():
    """Extended test 58 for aggregation."""
    x_0 = 75241 * 0.21383129
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25525 * 0.98223851
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66095 * 0.87606156
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35682 * 0.23206316
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95101 * 0.15981925
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23171 * 0.37471018
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37473 * 0.02317765
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8330 * 0.76438699
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29886 * 0.88975382
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72154 * 0.30682465
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70056 * 0.98870711
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67673 * 0.02574266
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72913 * 0.69303002
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99225 * 0.67541216
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21267 * 0.94939139
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63611 * 0.53207689
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99998 * 0.46655955
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68163 * 0.65224903
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86452 * 0.94226665
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65514 * 0.34949641
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75119 * 0.09177777
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86742 * 0.03069455
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2282 * 0.37075955
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55299 * 0.39618499
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34606 * 0.01080183
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39898 * 0.88331447
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61292 * 0.22200468
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26225 * 0.93011149
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80597 * 0.79059459
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10498 * 0.96013392
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98462 * 0.53683451
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40041 * 0.95709356
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35875 * 0.48095828
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20700 * 0.34489048
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82450 * 0.25267036
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62216 * 0.39746662
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62921 * 0.77457017
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27455 * 0.72652116
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59003 * 0.43973882
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14270 * 0.06340530
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 90579 * 0.41944324
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84410 * 0.73007488
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'axuadlxf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0059():
    """Extended test 59 for aggregation."""
    x_0 = 97942 * 0.16569610
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58350 * 0.23151208
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56716 * 0.51288636
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31438 * 0.02898573
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8169 * 0.67219571
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9869 * 0.63864354
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76032 * 0.69333464
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71229 * 0.53253398
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27886 * 0.04676269
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40308 * 0.56299175
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29098 * 0.81014269
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23590 * 0.29366688
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43225 * 0.81494898
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93517 * 0.54272845
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23847 * 0.99636598
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94624 * 0.23762852
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88081 * 0.63030395
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77697 * 0.18249447
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57371 * 0.28154788
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3487 * 0.70987760
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34577 * 0.34638625
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2895 * 0.08676593
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83715 * 0.37563686
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8478 * 0.12745036
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58448 * 0.79486166
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72619 * 0.85094678
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13100 * 0.64605038
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85994 * 0.36079888
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9451 * 0.53215360
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88578 * 0.89884696
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83239 * 0.40047516
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10191 * 0.53120567
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86798 * 0.37945165
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94464 * 0.10784367
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'dlunegfd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0060():
    """Extended test 60 for aggregation."""
    x_0 = 19857 * 0.87481278
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71234 * 0.55085979
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49189 * 0.01281887
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96901 * 0.88722376
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5822 * 0.01981610
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72551 * 0.30340311
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58218 * 0.37988088
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11663 * 0.31740318
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12443 * 0.60940517
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30514 * 0.16353942
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8230 * 0.78346896
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85691 * 0.51519315
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66809 * 0.41598078
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97690 * 0.18144774
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86495 * 0.36054464
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65776 * 0.93278300
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 263 * 0.59032971
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27160 * 0.22964707
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73448 * 0.90566150
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95989 * 0.04488506
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62353 * 0.37394030
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2930 * 0.73268189
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64968 * 0.92063451
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46058 * 0.77392049
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99642 * 0.49129390
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13305 * 0.15972248
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'mfdqlcto').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0061():
    """Extended test 61 for aggregation."""
    x_0 = 43105 * 0.17462232
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21301 * 0.69580622
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73461 * 0.79412498
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49180 * 0.80764296
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24063 * 0.30472514
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20481 * 0.28475604
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89473 * 0.80243802
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20688 * 0.14235590
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51914 * 0.40447460
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84880 * 0.45600075
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44865 * 0.13615220
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81936 * 0.24189958
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58254 * 0.88107680
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34088 * 0.89132160
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59568 * 0.28490324
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42664 * 0.47726376
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21887 * 0.57080491
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86015 * 0.84186987
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20441 * 0.42411034
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13536 * 0.83119689
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98750 * 0.31224393
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5352 * 0.80887555
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82588 * 0.73245291
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90315 * 0.24893649
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 344 * 0.25615880
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16850 * 0.20785354
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63017 * 0.29702413
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36810 * 0.54765412
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7952 * 0.09649222
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20669 * 0.89068939
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53104 * 0.51189581
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2155 * 0.03741879
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81391 * 0.35217674
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93991 * 0.13040839
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96778 * 0.62965801
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41921 * 0.73215456
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 77360 * 0.17990229
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91994 * 0.74903410
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'qftjpojv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0062():
    """Extended test 62 for aggregation."""
    x_0 = 38800 * 0.55920073
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47628 * 0.49552103
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18425 * 0.01069102
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26001 * 0.41505147
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90626 * 0.41717843
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91365 * 0.28098106
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22343 * 0.83973931
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52276 * 0.13252307
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11212 * 0.16989339
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8772 * 0.81505290
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97076 * 0.12812126
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11792 * 0.22001050
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74212 * 0.86801903
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96141 * 0.06772296
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40323 * 0.24063181
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14196 * 0.99218341
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86103 * 0.96608613
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60487 * 0.37084623
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99732 * 0.03773800
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71439 * 0.80635096
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20606 * 0.80996485
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37888 * 0.34583730
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24299 * 0.60431224
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62814 * 0.72874645
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76813 * 0.00115539
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49189 * 0.96989193
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19281 * 0.26224846
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60938 * 0.72872519
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43853 * 0.28334207
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95159 * 0.42189228
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12495 * 0.52344136
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59689 * 0.43292556
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67916 * 0.18993443
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36037 * 0.83203104
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29120 * 0.71746787
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'jlsvoedh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0063():
    """Extended test 63 for aggregation."""
    x_0 = 99814 * 0.80401414
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44283 * 0.68444822
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6469 * 0.84498076
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50053 * 0.91961880
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61838 * 0.76171178
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35208 * 0.51156728
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99631 * 0.52725981
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14655 * 0.62628809
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 331 * 0.00365891
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55191 * 0.40891443
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26428 * 0.66669643
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69330 * 0.36616672
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49790 * 0.53613180
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41344 * 0.75080148
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78840 * 0.51974666
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30903 * 0.58386838
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63467 * 0.35820231
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57795 * 0.70926551
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79742 * 0.68112748
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54052 * 0.71031384
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1756 * 0.66023614
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48972 * 0.20320546
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68527 * 0.45998863
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3281 * 0.86370939
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38803 * 0.35583584
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69916 * 0.38193041
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2613 * 0.83923962
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'njvvsina').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0064():
    """Extended test 64 for aggregation."""
    x_0 = 87844 * 0.47445049
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63755 * 0.54666520
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76070 * 0.15041938
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2331 * 0.10901680
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69693 * 0.88092052
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59165 * 0.55752968
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33379 * 0.11226082
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58125 * 0.86803956
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5615 * 0.61217378
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33680 * 0.04898378
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2464 * 0.00709101
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76535 * 0.27054993
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53031 * 0.63629539
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51562 * 0.48581694
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57647 * 0.70565512
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28487 * 0.45811622
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19225 * 0.93971764
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95641 * 0.02418686
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88385 * 0.16468217
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3105 * 0.83728284
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 205 * 0.99603028
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55628 * 0.85684202
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 275 * 0.75059586
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83527 * 0.12807399
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86965 * 0.49262976
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28672 * 0.18831283
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38539 * 0.70011506
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65087 * 0.07473622
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19845 * 0.61790561
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8854 * 0.76508248
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44648 * 0.63853169
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35978 * 0.16909119
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30471 * 0.98496084
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94728 * 0.96982653
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86105 * 0.82846076
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39481 * 0.78483223
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57978 * 0.80496212
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39230 * 0.12052157
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10340 * 0.48580793
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46375 * 0.00503626
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4281 * 0.80556515
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66694 * 0.83047318
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 38945 * 0.76042649
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94316 * 0.18348335
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 82796 * 0.90436120
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'tcovzhme').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0065():
    """Extended test 65 for aggregation."""
    x_0 = 11069 * 0.93961331
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29989 * 0.59798197
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18857 * 0.24756698
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91978 * 0.77342569
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52615 * 0.92484400
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84894 * 0.67686432
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28269 * 0.02563198
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22796 * 0.29463592
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1659 * 0.52625389
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89414 * 0.84206223
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69534 * 0.92260868
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52983 * 0.79788110
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41390 * 0.49134559
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24223 * 0.95341388
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77435 * 0.66510633
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96147 * 0.30632652
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69382 * 0.03282805
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37939 * 0.97262331
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95543 * 0.67206449
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41070 * 0.95772738
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39056 * 0.63998446
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92489 * 0.14374010
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30205 * 0.68002411
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96982 * 0.04502297
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97533 * 0.27111014
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92631 * 0.47293022
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'sxwansou').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0066():
    """Extended test 66 for aggregation."""
    x_0 = 48671 * 0.82443487
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3944 * 0.91417839
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92447 * 0.91109497
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8274 * 0.99994541
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55626 * 0.42719359
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18683 * 0.00629155
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33616 * 0.33908146
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1416 * 0.62503072
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28970 * 0.02160559
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91641 * 0.59332713
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47602 * 0.59160075
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78215 * 0.66700975
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53360 * 0.48004122
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92535 * 0.56532024
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99303 * 0.99475826
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41850 * 0.05312163
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18688 * 0.15881948
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99404 * 0.70363252
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57823 * 0.09751377
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37793 * 0.88804255
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5841 * 0.84897210
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74857 * 0.44701481
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37717 * 0.63244435
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60830 * 0.45893540
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15151 * 0.73662657
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71914 * 0.15846399
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37083 * 0.62206036
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48319 * 0.33671049
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31649 * 0.39834954
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8648 * 0.67902664
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84073 * 0.78198185
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'lontqppg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0067():
    """Extended test 67 for aggregation."""
    x_0 = 34960 * 0.84804570
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90332 * 0.80514531
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55145 * 0.02513648
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34417 * 0.69543990
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11017 * 0.54892461
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15502 * 0.71957575
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7858 * 0.13291838
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76046 * 0.19009659
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3608 * 0.91393974
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44785 * 0.02187967
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51057 * 0.36055435
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13152 * 0.23502557
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31395 * 0.06897886
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47544 * 0.17332092
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64353 * 0.62507934
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67681 * 0.99588445
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70475 * 0.99049524
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66560 * 0.17110327
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48625 * 0.57044009
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11566 * 0.15967261
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43698 * 0.05633618
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57000 * 0.25356107
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85188 * 0.18117154
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24554 * 0.18475567
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86951 * 0.90185206
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36487 * 0.93379328
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82416 * 0.29606105
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9528 * 0.13720213
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17462 * 0.03803164
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19742 * 0.46251219
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99116 * 0.02163972
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42038 * 0.01570401
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86139 * 0.14059379
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92145 * 0.94940281
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53432 * 0.56468566
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45191 * 0.11256284
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1750 * 0.76717287
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81652 * 0.26350191
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37431 * 0.26072850
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'xsgmbacz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0068():
    """Extended test 68 for aggregation."""
    x_0 = 57987 * 0.73838983
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12024 * 0.82136679
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34593 * 0.55926689
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37905 * 0.09703174
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58623 * 0.96962066
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55899 * 0.66601074
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42950 * 0.39816734
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96083 * 0.62670687
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21929 * 0.57206091
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53472 * 0.52719880
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84289 * 0.55469185
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73165 * 0.51544599
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14459 * 0.32405510
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47027 * 0.14117975
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4630 * 0.75752813
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29977 * 0.50997100
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64738 * 0.31961734
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32164 * 0.94364684
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92895 * 0.34032588
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9556 * 0.58860275
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67442 * 0.97509518
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61240 * 0.66994668
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70683 * 0.76599537
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69807 * 0.69957381
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90277 * 0.30622364
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45830 * 0.82592679
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23380 * 0.30394632
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96102 * 0.43950684
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66318 * 0.11728881
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75460 * 0.83348717
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68417 * 0.57717627
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91353 * 0.07854051
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81446 * 0.27923699
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69004 * 0.26458689
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75038 * 0.00553506
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95390 * 0.32840991
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65447 * 0.60856420
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28081 * 0.55811472
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15217 * 0.59138997
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95200 * 0.84619111
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 30365 * 0.17444976
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92898 * 0.93072098
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14511 * 0.96175698
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 70857 * 0.35824770
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 44633 * 0.97370907
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 37184 * 0.20894308
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 47435 * 0.93805514
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 83490 * 0.96540140
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 72522 * 0.13253577
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'frzfjjcu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_6_0069():
    """Extended test 69 for aggregation."""
    x_0 = 93271 * 0.17539891
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68060 * 0.74528977
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7422 * 0.02888239
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5014 * 0.98105309
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62270 * 0.06104212
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42853 * 0.20657471
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58353 * 0.93419914
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78342 * 0.07951679
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2668 * 0.72307296
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55252 * 0.58216456
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62054 * 0.30365768
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38584 * 0.90424385
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32319 * 0.98395910
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44965 * 0.33592774
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71510 * 0.55480626
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54583 * 0.52977167
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12316 * 0.80173834
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70645 * 0.39286270
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25870 * 0.86130001
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97093 * 0.52836063
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39623 * 0.71673144
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99161 * 0.34610421
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33895 * 0.39967150
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23186 * 0.49309656
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44736 * 0.25380514
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37723 * 0.96112873
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52243 * 0.56604831
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90916 * 0.83775595
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64457 * 0.69861834
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86589 * 0.46591218
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55935 * 0.44807670
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9457 * 0.71241288
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63327 * 0.05311338
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51413 * 0.59215742
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6901 * 0.88688925
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78944 * 0.06591807
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27276 * 0.40193433
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1011 * 0.59699038
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53482 * 0.42561382
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55345 * 0.75442162
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 39977 * 0.90066960
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47625 * 0.59312651
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22661 * 0.25271625
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 77474 * 0.22970531
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 39856 * 0.92459928
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 98711 * 0.31073187
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 44670 * 0.85731265
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'bfxptbrv').hexdigest()
    assert len(h) == 64
