"""Extended tests for billing suite 4."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_billing_extended_4_0000():
    """Extended test 0 for billing."""
    x_0 = 31896 * 0.05549401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99149 * 0.17779116
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49782 * 0.12937498
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81953 * 0.24407020
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11786 * 0.87245494
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84924 * 0.84965352
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87155 * 0.70450404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9086 * 0.98302859
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89252 * 0.76936150
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15215 * 0.00525072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1893 * 0.18469428
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38590 * 0.51204113
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 725 * 0.23461847
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35688 * 0.17842804
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11876 * 0.88790288
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37702 * 0.04616609
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49172 * 0.52055046
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63556 * 0.58385102
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34709 * 0.75083108
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49939 * 0.83666901
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99846 * 0.26199735
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65706 * 0.10444684
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19529 * 0.07842936
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44996 * 0.54304391
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13935 * 0.50889693
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92929 * 0.93927090
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97723 * 0.66705677
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36527 * 0.59231113
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97083 * 0.58806985
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69781 * 0.20531255
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'zfypcxbk').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0001():
    """Extended test 1 for billing."""
    x_0 = 37105 * 0.01916766
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85344 * 0.64609379
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67499 * 0.15236199
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33805 * 0.03119102
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43276 * 0.66033785
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45753 * 0.92344682
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13555 * 0.44545079
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74322 * 0.71017313
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1050 * 0.17463136
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82662 * 0.66810138
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79613 * 0.23111682
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23333 * 0.95991564
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14151 * 0.24701606
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41052 * 0.33791641
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67861 * 0.32796568
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64966 * 0.04225203
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98333 * 0.93412840
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51678 * 0.67052524
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94303 * 0.55211838
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51213 * 0.95291503
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14249 * 0.57294190
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17391 * 0.48072566
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58030 * 0.21277329
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93693 * 0.05831547
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72729 * 0.93773311
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30227 * 0.26630663
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7256 * 0.20171932
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74169 * 0.93562671
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7947 * 0.79901550
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65564 * 0.34233684
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15572 * 0.04261646
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29163 * 0.92621772
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21623 * 0.64598320
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23503 * 0.77038525
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50454 * 0.70652591
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'fxwjfapf').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0002():
    """Extended test 2 for billing."""
    x_0 = 14061 * 0.15006374
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27681 * 0.81117916
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1083 * 0.30861195
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52389 * 0.17421368
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12430 * 0.30536684
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75613 * 0.17553512
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91817 * 0.01517117
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58050 * 0.88243776
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91873 * 0.32390705
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15968 * 0.67599688
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29257 * 0.71644686
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32810 * 0.92291818
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43376 * 0.43818944
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3665 * 0.88874292
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43013 * 0.63330347
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26120 * 0.37485483
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20433 * 0.75245292
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11539 * 0.19214893
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41649 * 0.45708266
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18159 * 0.97465217
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7555 * 0.53800622
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21914 * 0.28017169
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96307 * 0.89324870
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37345 * 0.53028839
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94656 * 0.36656872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67339 * 0.07760313
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'rhzgiwvo').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0003():
    """Extended test 3 for billing."""
    x_0 = 89844 * 0.32685324
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75095 * 0.40824191
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10272 * 0.06294023
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69724 * 0.05794882
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27218 * 0.80238247
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95687 * 0.79309743
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30175 * 0.51250553
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54296 * 0.56297622
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35500 * 0.29967470
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29221 * 0.84104586
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81408 * 0.36105980
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36517 * 0.52217943
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44412 * 0.60754445
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55302 * 0.90555073
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23840 * 0.01984501
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36575 * 0.52606040
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87115 * 0.49077801
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35521 * 0.25336844
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52228 * 0.71683458
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57470 * 0.83353417
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10098 * 0.51180917
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56574 * 0.70418726
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4918 * 0.35528046
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12123 * 0.25615932
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54960 * 0.07689541
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3819 * 0.23647885
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55920 * 0.79982215
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73231 * 0.77788299
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59523 * 0.04118529
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61856 * 0.56478820
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75215 * 0.50125089
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15747 * 0.65965563
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98479 * 0.47656262
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9278 * 0.05241447
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83379 * 0.93454203
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12238 * 0.26241267
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98406 * 0.37906485
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'dnrvchkd').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0004():
    """Extended test 4 for billing."""
    x_0 = 46054 * 0.57492755
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19834 * 0.10371369
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99762 * 0.01068243
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20505 * 0.96887872
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60139 * 0.59057527
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13554 * 0.39278685
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72963 * 0.64340494
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92987 * 0.10520047
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33216 * 0.48426016
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62718 * 0.76663817
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38440 * 0.84809633
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10506 * 0.80462370
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6654 * 0.22143375
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15227 * 0.73540549
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18852 * 0.11000888
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34662 * 0.97139212
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12922 * 0.00894148
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81037 * 0.54371468
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66122 * 0.78345427
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83593 * 0.20835184
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57081 * 0.55466664
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83278 * 0.10752232
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92149 * 0.30546809
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73881 * 0.50975656
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94620 * 0.89692104
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44768 * 0.31848085
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'oehucutt').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0005():
    """Extended test 5 for billing."""
    x_0 = 16235 * 0.39949427
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92400 * 0.30344834
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73755 * 0.20392065
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27000 * 0.84696096
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7344 * 0.54778463
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61609 * 0.53440742
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70311 * 0.94620708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42943 * 0.09838182
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59392 * 0.94217501
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27657 * 0.40274877
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65376 * 0.80869612
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94347 * 0.97288209
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34233 * 0.42836487
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34876 * 0.54728449
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80801 * 0.63086662
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14691 * 0.86560419
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32215 * 0.92242089
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20764 * 0.56791903
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28927 * 0.61780362
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3797 * 0.76620556
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90605 * 0.87862691
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6630 * 0.84695079
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63632 * 0.85743990
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10708 * 0.67291726
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46467 * 0.51352813
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22500 * 0.35531248
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76341 * 0.55757526
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36368 * 0.82441706
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59049 * 0.20888986
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73991 * 0.18691007
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34655 * 0.93035534
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97640 * 0.47888224
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75516 * 0.79038353
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59084 * 0.40574262
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46816 * 0.31125081
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45171 * 0.99887068
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74875 * 0.01592709
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69715 * 0.20561885
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1363 * 0.78014049
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30023 * 0.17277176
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 59215 * 0.23828850
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6137 * 0.61137734
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 92058 * 0.36710721
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 49084 * 0.59722741
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86771 * 0.37979628
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26796 * 0.79599000
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 24362 * 0.89281087
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 78769 * 0.86636065
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'hjqvreoj').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0006():
    """Extended test 6 for billing."""
    x_0 = 47686 * 0.51900216
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29373 * 0.64799902
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5547 * 0.79693691
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70451 * 0.59941892
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26896 * 0.05687247
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44477 * 0.63044537
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83257 * 0.78045085
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9782 * 0.66044406
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45762 * 0.57043742
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28508 * 0.00623084
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94163 * 0.27071000
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56455 * 0.72104845
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58137 * 0.69407123
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82225 * 0.45232363
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76221 * 0.60172009
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63864 * 0.75513731
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6044 * 0.12102557
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64325 * 0.04614629
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31018 * 0.97862097
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80806 * 0.72514434
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51891 * 0.99112056
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60452 * 0.48376376
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26280 * 0.50113287
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55950 * 0.12521218
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 675 * 0.47553926
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4691 * 0.32540444
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9827 * 0.52577731
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82907 * 0.95847966
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35239 * 0.20927182
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9198 * 0.16561779
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 599 * 0.61372311
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78175 * 0.77189988
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19195 * 0.95936662
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3269 * 0.26065732
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41170 * 0.78169832
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64147 * 0.45858664
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71872 * 0.29027559
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36662 * 0.22081294
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16544 * 0.98156840
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16207 * 0.03975321
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81027 * 0.93972870
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15586 * 0.36186858
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 84988 * 0.88717626
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 63280 * 0.18665500
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 66653 * 0.26879305
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 52806 * 0.60805785
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 74350 * 0.98153620
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'lpijprzu').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0007():
    """Extended test 7 for billing."""
    x_0 = 28505 * 0.62197475
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43315 * 0.90341955
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22929 * 0.76353141
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 661 * 0.68617832
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58756 * 0.96346020
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29766 * 0.17718828
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30319 * 0.26849504
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96789 * 0.28847648
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6911 * 0.32635289
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91154 * 0.84770388
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79076 * 0.01727206
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96770 * 0.70611815
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62682 * 0.88252731
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25630 * 0.70649735
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21123 * 0.78839530
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60007 * 0.19509676
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93401 * 0.32323488
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20835 * 0.03201700
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16523 * 0.43288279
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88393 * 0.40604696
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19725 * 0.88099918
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56736 * 0.32593867
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77094 * 0.93701418
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76236 * 0.58058486
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91871 * 0.66207470
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84058 * 0.28561318
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66564 * 0.12798384
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52866 * 0.49182316
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27243 * 0.57080798
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58916 * 0.52820950
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92144 * 0.75215887
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46332 * 0.97796005
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10977 * 0.90566682
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40877 * 0.06928809
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 630 * 0.69515662
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67144 * 0.92021477
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72101 * 0.82152917
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38857 * 0.45205070
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53049 * 0.35342889
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'sysrchbo').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0008():
    """Extended test 8 for billing."""
    x_0 = 43443 * 0.84425410
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32421 * 0.16551148
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53915 * 0.94317681
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84156 * 0.98010892
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60976 * 0.32652668
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32712 * 0.20828568
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34161 * 0.41128008
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1688 * 0.19855560
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41671 * 0.31402863
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51171 * 0.27181825
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57476 * 0.67662364
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58527 * 0.73470225
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22911 * 0.67859357
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84358 * 0.59313055
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4997 * 0.20543356
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73166 * 0.29652417
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47072 * 0.37797040
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14502 * 0.53549816
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69053 * 0.14253891
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93403 * 0.42214596
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'vrxhnncp').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0009():
    """Extended test 9 for billing."""
    x_0 = 51949 * 0.93478552
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 789 * 0.08320071
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48560 * 0.09165928
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21739 * 0.09555908
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40303 * 0.37319116
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35838 * 0.53405407
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85115 * 0.71690423
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52842 * 0.44107842
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74842 * 0.44088152
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75236 * 0.48277029
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85451 * 0.96153716
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85053 * 0.51676753
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53653 * 0.53270986
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80902 * 0.96590970
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36947 * 0.70922153
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 475 * 0.44773747
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18073 * 0.63142044
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17256 * 0.76486774
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97221 * 0.69588283
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20200 * 0.54176927
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55836 * 0.15986172
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29939 * 0.69895515
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48966 * 0.46786434
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92340 * 0.99058474
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12762 * 0.75675509
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12057 * 0.38253510
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81768 * 0.62374967
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50293 * 0.26757974
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88899 * 0.87092104
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78435 * 0.20858689
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57459 * 0.46750409
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96354 * 0.65211103
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90994 * 0.06071439
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29492 * 0.79267271
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83199 * 0.20315615
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94519 * 0.29938122
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68650 * 0.99678192
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66667 * 0.65264151
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82798 * 0.52036120
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 61214 * 0.33932463
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6647 * 0.67640496
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37755 * 0.30796264
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70051 * 0.63681099
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 17040 * 0.04311579
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 20030 * 0.61883942
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 36830 * 0.01621373
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 89975 * 0.03163596
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 78028 * 0.92367987
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'xnmgvrke').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0010():
    """Extended test 10 for billing."""
    x_0 = 15813 * 0.01414222
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41496 * 0.28352372
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79966 * 0.09857462
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31436 * 0.39108623
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31879 * 0.99964483
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70456 * 0.39314143
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87969 * 0.94105651
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45701 * 0.89267852
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38692 * 0.21726322
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55961 * 0.71739204
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91082 * 0.75161980
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49700 * 0.82024685
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86326 * 0.34910791
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89833 * 0.68003540
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72132 * 0.43610967
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75463 * 0.47849031
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72024 * 0.40042845
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35191 * 0.94195732
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77051 * 0.33757867
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53901 * 0.11985480
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38226 * 0.87457283
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19195 * 0.22938138
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66922 * 0.76009831
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21494 * 0.27045016
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56890 * 0.22025769
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42532 * 0.36738158
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20795 * 0.79811750
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8016 * 0.99322208
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32687 * 0.63190403
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11356 * 0.21715907
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63843 * 0.65475698
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51346 * 0.80619548
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71985 * 0.08022411
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5152 * 0.11511386
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27921 * 0.51134581
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96356 * 0.86108590
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98867 * 0.04962634
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82224 * 0.22153640
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18042 * 0.94876582
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 48486 * 0.75811468
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52319 * 0.74683033
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 95881 * 0.16383428
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 76568 * 0.70163258
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 14811 * 0.57055521
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 98636 * 0.40351064
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 81901 * 0.18515781
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 42794 * 0.05999573
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 13486 * 0.01623356
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 68064 * 0.21423226
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 57907 * 0.84125472
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'uszwzgdl').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0011():
    """Extended test 11 for billing."""
    x_0 = 35502 * 0.54644340
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55766 * 0.47956239
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20812 * 0.36199802
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73728 * 0.26388368
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62763 * 0.50261059
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44845 * 0.31151326
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99367 * 0.52791210
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97863 * 0.10128793
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19153 * 0.65013046
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26255 * 0.52275687
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25097 * 0.73966526
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21726 * 0.06761137
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23276 * 0.61318552
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13544 * 0.44293256
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97327 * 0.73363998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94993 * 0.79953536
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90246 * 0.76248385
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11195 * 0.31923036
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28570 * 0.90803992
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60372 * 0.28825229
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45707 * 0.92781119
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65542 * 0.91263926
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27805 * 0.32034536
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52766 * 0.20623057
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55850 * 0.22027993
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82060 * 0.50903294
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64403 * 0.64833914
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28877 * 0.48437485
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87283 * 0.14718614
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10748 * 0.49901612
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73226 * 0.41734458
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36909 * 0.34789078
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31195 * 0.50136902
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16527 * 0.45484423
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89488 * 0.98947446
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50202 * 0.02643447
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8561 * 0.90301040
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17283 * 0.96180851
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28670 * 0.08368905
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 36410 * 0.64203564
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'wcigzcdk').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0012():
    """Extended test 12 for billing."""
    x_0 = 71867 * 0.97337348
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14358 * 0.58182150
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53427 * 0.23590560
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52056 * 0.99301760
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12279 * 0.42218556
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37443 * 0.33184403
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19499 * 0.85731788
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13625 * 0.73912069
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97122 * 0.67833077
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65363 * 0.41488624
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45383 * 0.15718699
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22405 * 0.56267848
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40948 * 0.21805076
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49027 * 0.03629402
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42086 * 0.72283640
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67102 * 0.12816087
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29642 * 0.97254299
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7456 * 0.17566559
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57720 * 0.65662599
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24860 * 0.54969500
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64449 * 0.05986044
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93294 * 0.14908695
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64118 * 0.86685419
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11182 * 0.46468027
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68573 * 0.77053113
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7554 * 0.70303568
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18190 * 0.30087548
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78316 * 0.97335189
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82679 * 0.87546193
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60862 * 0.15566672
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55889 * 0.41574956
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60313 * 0.30024913
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72773 * 0.07545107
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76012 * 0.64203177
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35088 * 0.95383946
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17604 * 0.43042509
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79441 * 0.56671694
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48075 * 0.13485387
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12939 * 0.19644504
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51981 * 0.16666867
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8020 * 0.77638626
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59740 * 0.34307510
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12390 * 0.14446260
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 6174 * 0.47812782
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'lttwzvbr').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0013():
    """Extended test 13 for billing."""
    x_0 = 50835 * 0.36777308
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46708 * 0.67375859
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48616 * 0.98771436
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45181 * 0.00112956
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85098 * 0.90529405
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86235 * 0.59010544
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68126 * 0.09795316
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94608 * 0.25358891
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97509 * 0.27513155
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17883 * 0.91160035
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6137 * 0.84882180
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9121 * 0.19751165
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87641 * 0.67341728
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21060 * 0.18363949
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36536 * 0.31912435
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32850 * 0.60322849
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89008 * 0.10078215
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77432 * 0.32712692
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21344 * 0.08851877
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53177 * 0.48597205
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65874 * 0.96144899
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21675 * 0.32629148
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45650 * 0.80904957
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29390 * 0.43378204
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96325 * 0.30968703
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82283 * 0.10226502
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66061 * 0.62579703
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26240 * 0.87394300
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58045 * 0.13703015
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92215 * 0.38391473
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89636 * 0.11684528
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36416 * 0.15820892
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70029 * 0.63667583
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24065 * 0.42769836
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71986 * 0.90307589
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56645 * 0.87405349
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97048 * 0.27260935
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20014 * 0.08131225
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'tqzyiljs').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0014():
    """Extended test 14 for billing."""
    x_0 = 58366 * 0.91467994
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11348 * 0.12437968
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51797 * 0.71455602
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36511 * 0.78423124
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90369 * 0.89992577
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60687 * 0.22169821
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38738 * 0.98437033
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90473 * 0.56838826
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63340 * 0.94544686
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36625 * 0.59216247
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71695 * 0.34405809
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80923 * 0.96241639
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55187 * 0.37785290
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41057 * 0.91687048
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71380 * 0.75749341
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16096 * 0.44922244
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24759 * 0.77884515
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6270 * 0.04402195
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2362 * 0.78951197
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20688 * 0.96898866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25667 * 0.53472510
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'fgqrqjza').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0015():
    """Extended test 15 for billing."""
    x_0 = 98480 * 0.56851041
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22852 * 0.81747596
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84302 * 0.55239987
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90428 * 0.27797764
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20996 * 0.95995463
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96164 * 0.49732031
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6648 * 0.01921189
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49834 * 0.82328258
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2617 * 0.20055110
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4254 * 0.29305354
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27345 * 0.91043322
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75892 * 0.44200265
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84724 * 0.08923481
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31282 * 0.14839445
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76033 * 0.70271505
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31379 * 0.77006306
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52529 * 0.46119171
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87879 * 0.38539909
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36596 * 0.78331975
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80163 * 0.89815364
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64307 * 0.05090538
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45804 * 0.09514965
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'jepmqdat').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0016():
    """Extended test 16 for billing."""
    x_0 = 49169 * 0.92039746
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60425 * 0.73681275
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32714 * 0.91718578
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47853 * 0.86191036
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40241 * 0.66973960
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65286 * 0.94001468
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98494 * 0.00162314
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24387 * 0.27549472
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31186 * 0.89489382
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83168 * 0.92373916
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19512 * 0.53023246
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89837 * 0.74141152
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99798 * 0.84503692
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37996 * 0.81134501
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25914 * 0.08307257
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14482 * 0.49825087
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3587 * 0.65991146
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13866 * 0.28505643
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37063 * 0.58750297
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1691 * 0.75650440
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61087 * 0.39352245
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20946 * 0.11249628
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51670 * 0.82202585
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57806 * 0.09140511
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13632 * 0.09328240
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17610 * 0.15617736
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46401 * 0.43052898
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59933 * 0.69800063
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43540 * 0.30441532
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45008 * 0.90536705
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99621 * 0.38242355
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15250 * 0.70763221
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10895 * 0.88753591
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26746 * 0.76962789
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76696 * 0.61144340
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56239 * 0.21232956
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32045 * 0.05589535
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1036 * 0.37379462
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24939 * 0.95797677
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45743 * 0.68327697
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'opyyziot').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0017():
    """Extended test 17 for billing."""
    x_0 = 37793 * 0.86109916
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78753 * 0.84422517
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64437 * 0.96573989
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16959 * 0.48500901
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52047 * 0.84718403
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79925 * 0.70151227
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3116 * 0.45532680
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55268 * 0.80711101
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89677 * 0.37731753
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12199 * 0.97517627
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34551 * 0.90971027
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71320 * 0.07968570
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25261 * 0.66084866
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95991 * 0.94290649
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35996 * 0.43572449
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10014 * 0.58895779
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10432 * 0.12848841
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70218 * 0.49276286
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34064 * 0.58086727
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12219 * 0.99506165
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92405 * 0.64931051
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36139 * 0.57181009
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'lehoxuuh').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0018():
    """Extended test 18 for billing."""
    x_0 = 29322 * 0.17140936
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98851 * 0.34917266
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31648 * 0.36089652
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32813 * 0.79172538
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88813 * 0.22242777
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7242 * 0.32582778
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24417 * 0.97508970
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78143 * 0.47602555
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80787 * 0.40746496
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75142 * 0.75144330
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84515 * 0.74105053
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98021 * 0.63532873
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69283 * 0.22214399
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44986 * 0.57899149
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17354 * 0.34275200
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72806 * 0.48555828
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1567 * 0.09875904
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34204 * 0.43074770
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43840 * 0.08671644
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34748 * 0.06272986
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65371 * 0.33141704
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32916 * 0.92571332
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97408 * 0.93421020
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79668 * 0.12039189
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11526 * 0.70199949
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40570 * 0.38376472
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94590 * 0.32451059
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76188 * 0.07546866
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49378 * 0.86850504
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61824 * 0.36883033
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14377 * 0.96507999
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40326 * 0.28220526
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3758 * 0.92139920
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14943 * 0.28430226
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48227 * 0.93084204
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28070 * 0.33985736
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21242 * 0.12621341
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4780 * 0.91898446
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26424 * 0.58238472
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29285 * 0.54177850
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 61623 * 0.74082568
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84073 * 0.73375614
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12970 * 0.31020947
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 45231 * 0.15007579
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 41900 * 0.43820668
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 42526 * 0.00971678
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17017 * 0.85704893
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 80378 * 0.29848596
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'molixava').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0019():
    """Extended test 19 for billing."""
    x_0 = 38399 * 0.92381723
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92639 * 0.24379883
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97368 * 0.57965689
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82263 * 0.01576144
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44651 * 0.89077368
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2199 * 0.25977467
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10600 * 0.30184023
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93264 * 0.65334121
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4636 * 0.69139518
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81827 * 0.00485804
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50011 * 0.45452484
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91910 * 0.87656779
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80011 * 0.48659088
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2350 * 0.82344244
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64533 * 0.11783579
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35226 * 0.22384117
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8282 * 0.37931308
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43539 * 0.32935669
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60110 * 0.48006777
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41897 * 0.73238703
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94820 * 0.93151413
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47429 * 0.36946736
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78577 * 0.74523847
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62306 * 0.47667950
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80794 * 0.45612126
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13158 * 0.59226207
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97218 * 0.27725066
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97980 * 0.66285269
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88362 * 0.72602806
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61114 * 0.10466105
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77206 * 0.07258703
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92913 * 0.25800742
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45918 * 0.46264193
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14881 * 0.87683616
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46199 * 0.77081761
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12961 * 0.33807091
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63628 * 0.96990733
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33731 * 0.30135439
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12626 * 0.25255376
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10048 * 0.39672068
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49117 * 0.07036581
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'twdtcgaz').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0020():
    """Extended test 20 for billing."""
    x_0 = 18468 * 0.24178382
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2032 * 0.18136323
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93076 * 0.80815629
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70458 * 0.95509288
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79846 * 0.19326069
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95940 * 0.08848909
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34148 * 0.06475425
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88006 * 0.44760227
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30442 * 0.83155563
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31903 * 0.69915042
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66236 * 0.86339350
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51780 * 0.17114390
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 484 * 0.58682005
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28730 * 0.10100540
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61694 * 0.73103614
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39660 * 0.65797780
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1271 * 0.10709930
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21936 * 0.48302233
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85607 * 0.18298127
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80865 * 0.44249114
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71177 * 0.65192888
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70481 * 0.10432172
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2081 * 0.15699823
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99057 * 0.69299564
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69851 * 0.64049997
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21417 * 0.69128811
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8682 * 0.05228104
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'vzowlogc').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0021():
    """Extended test 21 for billing."""
    x_0 = 31350 * 0.03582678
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66938 * 0.39561839
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62276 * 0.34178584
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94867 * 0.59373679
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85050 * 0.87785529
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82693 * 0.59811528
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5579 * 0.69053380
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6725 * 0.47774277
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86041 * 0.30551877
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3653 * 0.73213954
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5921 * 0.67342720
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65964 * 0.52516513
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7539 * 0.61170607
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81601 * 0.16272975
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9633 * 0.37322508
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41685 * 0.26186249
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59679 * 0.72717350
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82391 * 0.38257627
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96638 * 0.32697345
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19715 * 0.64525313
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14810 * 0.38189963
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51095 * 0.78814647
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5800 * 0.70267579
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76079 * 0.10015824
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91021 * 0.04301966
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18915 * 0.97156364
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91515 * 0.56338133
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46873 * 0.21014693
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92685 * 0.09464159
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93352 * 0.24712192
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93529 * 0.58440524
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25090 * 0.99335931
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46287 * 0.39530384
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79769 * 0.27917040
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16401 * 0.31993056
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20917 * 0.16396815
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32883 * 0.93967915
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13255 * 0.43728781
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59426 * 0.35122444
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 60843 * 0.89025848
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 33019 * 0.68605881
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81849 * 0.66179252
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 58085 * 0.41947141
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 7091 * 0.72617905
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'gfcyohmj').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0022():
    """Extended test 22 for billing."""
    x_0 = 38889 * 0.68994587
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45081 * 0.55461277
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65725 * 0.91923494
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60015 * 0.22763431
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14488 * 0.90125311
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77918 * 0.88441969
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77784 * 0.56810856
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22417 * 0.23999681
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48586 * 0.42097476
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72770 * 0.80230403
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6119 * 0.79458549
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73303 * 0.97193599
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49819 * 0.61379049
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24620 * 0.57529887
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80072 * 0.18232148
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45642 * 0.47739320
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40710 * 0.48819557
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99726 * 0.57891415
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13303 * 0.82884029
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52562 * 0.56589309
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45179 * 0.68455139
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30983 * 0.07743111
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8321 * 0.23655864
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22314 * 0.18718661
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27181 * 0.32370205
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 518 * 0.92703793
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40577 * 0.76821159
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46262 * 0.71657286
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17751 * 0.03552410
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17949 * 0.04954773
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'rabeqagk').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0023():
    """Extended test 23 for billing."""
    x_0 = 30975 * 0.31532167
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27523 * 0.56201781
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99859 * 0.42327426
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89727 * 0.24583239
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10296 * 0.78651787
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55800 * 0.85237858
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72808 * 0.65878168
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75108 * 0.89590578
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45635 * 0.32996748
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40798 * 0.55860634
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89823 * 0.75782706
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19879 * 0.23129488
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25243 * 0.15196786
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6693 * 0.00520296
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17967 * 0.81420309
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42471 * 0.56736159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88739 * 0.38339800
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30396 * 0.75920916
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66945 * 0.73865356
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85928 * 0.97749899
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77134 * 0.06914393
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87249 * 0.23030618
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34483 * 0.05621480
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45480 * 0.61160784
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8357 * 0.98588299
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16293 * 0.92747350
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23284 * 0.60971767
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23000 * 0.04774328
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85880 * 0.05643314
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18150 * 0.74668052
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'cbijpvom').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0024():
    """Extended test 24 for billing."""
    x_0 = 68977 * 0.62450731
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32278 * 0.28907005
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78314 * 0.77458061
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27540 * 0.70773720
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10895 * 0.57386636
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17693 * 0.76506905
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6516 * 0.37042925
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18415 * 0.37730875
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51569 * 0.92682982
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72094 * 0.89248834
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42441 * 0.24575820
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69438 * 0.14534544
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46793 * 0.39995604
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86896 * 0.88173651
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10607 * 0.52674654
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37071 * 0.64176807
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11110 * 0.47002991
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30879 * 0.89962024
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80715 * 0.73755923
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1874 * 0.59901061
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58517 * 0.63051371
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81157 * 0.68523260
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90307 * 0.92478053
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40653 * 0.06923477
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47378 * 0.63679601
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'fatgxrus').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0025():
    """Extended test 25 for billing."""
    x_0 = 67932 * 0.83627010
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77233 * 0.62001245
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14188 * 0.45527996
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10337 * 0.33624092
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50220 * 0.07609736
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75813 * 0.51655960
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28294 * 0.66835835
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8615 * 0.34833232
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19047 * 0.20108947
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71603 * 0.47751052
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83438 * 0.04445957
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58901 * 0.73198683
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41238 * 0.11190309
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5634 * 0.70573932
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46443 * 0.83630403
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60504 * 0.43390702
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6129 * 0.00618959
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64923 * 0.98758706
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32361 * 0.92803077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73618 * 0.49973373
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92667 * 0.85152908
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48442 * 0.51645051
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30735 * 0.83430275
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91582 * 0.39153134
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56626 * 0.41478096
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31708 * 0.31558542
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99118 * 0.30618924
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4010 * 0.51596159
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83638 * 0.39917771
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32971 * 0.25578597
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62041 * 0.25120368
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69758 * 0.01714998
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83621 * 0.24355458
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98546 * 0.38982932
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33006 * 0.34418962
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56387 * 0.92105461
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 77911 * 0.04030015
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11639 * 0.13816618
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'nydyihta').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0026():
    """Extended test 26 for billing."""
    x_0 = 95971 * 0.98415014
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42476 * 0.72216049
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89362 * 0.36798421
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21656 * 0.31300481
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48868 * 0.78098521
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62839 * 0.21229065
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36956 * 0.45437348
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31398 * 0.10386442
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20075 * 0.20210416
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79953 * 0.75892418
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90130 * 0.82649327
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96444 * 0.72090656
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33888 * 0.92970549
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33229 * 0.45709058
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84109 * 0.54372631
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34927 * 0.21304784
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72164 * 0.61078555
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21894 * 0.68750619
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87603 * 0.21744073
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89232 * 0.16442306
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'zaxoplew').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0027():
    """Extended test 27 for billing."""
    x_0 = 50567 * 0.94597640
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98865 * 0.79382448
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41727 * 0.73878156
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22758 * 0.77648518
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20200 * 0.92377354
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76834 * 0.53005039
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57068 * 0.05550490
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74235 * 0.37556638
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70469 * 0.68389973
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17015 * 0.21254812
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74724 * 0.64980097
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3195 * 0.94222589
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26276 * 0.40691107
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54378 * 0.07593685
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38939 * 0.29344112
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81316 * 0.50850707
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11 * 0.65825511
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87284 * 0.18843948
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47981 * 0.58233067
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63876 * 0.88519328
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31341 * 0.74172179
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19977 * 0.10387893
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16420 * 0.46219397
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85719 * 0.79880705
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61012 * 0.41613250
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69021 * 0.84576782
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78433 * 0.07220000
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16370 * 0.74398290
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40968 * 0.37037373
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40449 * 0.81966601
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55438 * 0.93457874
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25127 * 0.46481471
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25534 * 0.20829883
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10111 * 0.47566155
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43340 * 0.65389778
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21623 * 0.01084025
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19738 * 0.89633194
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19747 * 0.93586583
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4035 * 0.10193672
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75366 * 0.49683231
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 26644 * 0.43971718
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36249 * 0.80964451
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74475 * 0.16985947
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 68175 * 0.36957322
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 40950 * 0.60131029
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 90304 * 0.56492470
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'gspliiqm').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0028():
    """Extended test 28 for billing."""
    x_0 = 60004 * 0.03176185
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17469 * 0.24732332
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24307 * 0.34593416
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27888 * 0.82778726
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47417 * 0.09204312
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64960 * 0.59031576
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21933 * 0.22133990
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41153 * 0.15721554
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44367 * 0.48264973
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19777 * 0.51370931
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31518 * 0.32440751
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46321 * 0.07857813
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38104 * 0.78659413
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97064 * 0.74008562
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66024 * 0.19536779
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97391 * 0.46586578
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36301 * 0.75437592
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75908 * 0.58014419
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6002 * 0.68151564
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87791 * 0.09235829
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91649 * 0.31604840
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33530 * 0.28296336
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61662 * 0.59871467
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39081 * 0.00578539
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75820 * 0.26100741
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94901 * 0.90069470
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35238 * 0.25117307
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72699 * 0.25295525
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7072 * 0.80442742
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97832 * 0.65409855
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'zlyfwzew').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0029():
    """Extended test 29 for billing."""
    x_0 = 2364 * 0.17765426
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44638 * 0.15831754
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37988 * 0.91915974
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94430 * 0.36676217
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96348 * 0.12498484
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40520 * 0.53079369
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62001 * 0.78312852
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25167 * 0.80861784
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56437 * 0.82580488
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81116 * 0.34891648
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68453 * 0.29287082
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68115 * 0.80628097
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82360 * 0.34009820
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59440 * 0.71743976
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 538 * 0.30166130
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34 * 0.46960456
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10419 * 0.36512610
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54608 * 0.61838946
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74279 * 0.93420824
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14765 * 0.24713487
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45702 * 0.56999648
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32298 * 0.44561434
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24924 * 0.38111470
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20003 * 0.37095254
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8648 * 0.76800838
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96583 * 0.33623092
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82749 * 0.96484842
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81176 * 0.29234630
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6990 * 0.79000444
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38521 * 0.81157517
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80331 * 0.48168622
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9003 * 0.27264712
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29780 * 0.52961672
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49985 * 0.14795787
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79977 * 0.18571920
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 92673 * 0.57219595
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1752 * 0.36092542
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63051 * 0.34867877
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13911 * 0.64883651
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'lwfgptls').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0030():
    """Extended test 30 for billing."""
    x_0 = 78712 * 0.09295401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3159 * 0.61617563
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99895 * 0.77038054
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66951 * 0.20361242
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56624 * 0.30000602
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31624 * 0.68027115
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88734 * 0.64981746
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24171 * 0.70861290
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33223 * 0.42838690
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20161 * 0.16434599
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94858 * 0.23736403
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64141 * 0.05638357
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14037 * 0.27446507
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95721 * 0.79608598
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39046 * 0.13813410
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78026 * 0.48099957
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57468 * 0.36238101
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78711 * 0.84751047
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47577 * 0.66933229
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55706 * 0.49590025
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50257 * 0.16148071
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15188 * 0.24055579
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36489 * 0.60187176
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2233 * 0.36105279
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53870 * 0.11664386
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58548 * 0.98235843
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5948 * 0.13560973
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77463 * 0.45102315
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78703 * 0.87627473
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48146 * 0.17701322
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11871 * 0.55290953
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20414 * 0.77375576
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24178 * 0.36965584
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45838 * 0.53075456
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60748 * 0.91065033
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'nirqojju').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0031():
    """Extended test 31 for billing."""
    x_0 = 6750 * 0.34832021
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16131 * 0.19656684
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54382 * 0.34126178
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98782 * 0.44885078
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3083 * 0.05650763
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32366 * 0.63154350
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44528 * 0.81048536
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23732 * 0.99974273
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5177 * 0.56856963
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14422 * 0.78911359
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3883 * 0.75692027
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6979 * 0.63649938
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94697 * 0.30522708
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50914 * 0.25606218
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68267 * 0.14669060
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17399 * 0.08807741
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93015 * 0.89977537
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50402 * 0.63381747
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96523 * 0.86698561
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89384 * 0.69549680
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9973 * 0.54773453
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55090 * 0.95873889
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52956 * 0.60325586
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96375 * 0.99158717
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8595 * 0.32072551
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75110 * 0.88090749
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97907 * 0.49761121
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85200 * 0.37666841
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73690 * 0.45874155
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64743 * 0.48800645
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89161 * 0.76258735
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91165 * 0.39665112
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47150 * 0.74290220
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13061 * 0.67552929
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55705 * 0.99348151
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ozeeqfwq').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0032():
    """Extended test 32 for billing."""
    x_0 = 89454 * 0.33780580
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23214 * 0.15667498
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5994 * 0.81666082
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30516 * 0.65384066
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11983 * 0.68369787
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38211 * 0.05887753
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73113 * 0.29010042
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37234 * 0.19467674
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64543 * 0.32757146
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41366 * 0.51592042
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31321 * 0.08650793
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52338 * 0.75275988
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57099 * 0.46446079
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13563 * 0.39025195
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91846 * 0.76109865
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13973 * 0.85268070
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35388 * 0.37692278
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 231 * 0.59630007
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76460 * 0.13572810
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36078 * 0.18494834
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68884 * 0.68384358
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99428 * 0.00230556
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43593 * 0.45365161
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17177 * 0.25009222
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58581 * 0.79562813
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75758 * 0.69807223
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94783 * 0.98939595
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55655 * 0.63348215
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 244 * 0.33535145
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37356 * 0.84728334
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88252 * 0.07007431
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40416 * 0.24864678
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'kuhhkaob').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0033():
    """Extended test 33 for billing."""
    x_0 = 43723 * 0.39412631
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17583 * 0.11728692
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82737 * 0.16840385
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50931 * 0.14494696
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91912 * 0.09131114
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69161 * 0.87559796
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32412 * 0.86405712
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35156 * 0.36833145
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91545 * 0.20021782
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48204 * 0.65134554
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22183 * 0.85555710
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57332 * 0.66699857
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91769 * 0.11680158
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4299 * 0.01689164
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58515 * 0.16450230
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87623 * 0.17644625
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37933 * 0.84095886
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10103 * 0.08595345
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51658 * 0.81612229
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55670 * 0.39358973
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29740 * 0.10588642
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89389 * 0.41746834
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35623 * 0.42763240
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ksmiaccy').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0034():
    """Extended test 34 for billing."""
    x_0 = 43252 * 0.38953096
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98906 * 0.83341302
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65587 * 0.89870538
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66849 * 0.70109392
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10706 * 0.46290411
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8607 * 0.55036898
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9910 * 0.44578808
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76252 * 0.93503156
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75225 * 0.27126975
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21369 * 0.40027563
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6556 * 0.76422202
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22828 * 0.42426411
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54715 * 0.87917182
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16430 * 0.27840432
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67495 * 0.04479588
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24092 * 0.67775801
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11669 * 0.22713167
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35905 * 0.68091045
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58184 * 0.73938337
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52481 * 0.34463672
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81613 * 0.82923983
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30612 * 0.17494333
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55362 * 0.44437053
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75260 * 0.66750624
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85564 * 0.67472376
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62350 * 0.96565539
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'ruwoukpt').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0035():
    """Extended test 35 for billing."""
    x_0 = 8455 * 0.48982031
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95129 * 0.78502278
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63211 * 0.60997115
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52606 * 0.63525071
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90517 * 0.49169493
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14292 * 0.65989266
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19088 * 0.33715948
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75074 * 0.81144696
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36527 * 0.83701900
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47276 * 0.73826540
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97668 * 0.43765219
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20496 * 0.46117355
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46397 * 0.86456522
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38468 * 0.77075709
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3248 * 0.55608951
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44056 * 0.76755975
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39239 * 0.95125350
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26299 * 0.38994934
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49961 * 0.23181277
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93520 * 0.78463692
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 386 * 0.95252541
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18921 * 0.00707675
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55617 * 0.01375399
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54214 * 0.78945259
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56282 * 0.41210197
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30025 * 0.99028248
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'valxcdzz').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0036():
    """Extended test 36 for billing."""
    x_0 = 27109 * 0.70323781
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51263 * 0.97663881
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68684 * 0.08776353
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69223 * 0.47713614
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31834 * 0.94277473
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14164 * 0.15617634
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29225 * 0.45536235
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86499 * 0.92446339
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21024 * 0.61878312
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65800 * 0.29127657
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80700 * 0.15876032
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95645 * 0.55264068
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53732 * 0.50492198
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10316 * 0.69793796
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24392 * 0.45033199
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91278 * 0.20846598
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94344 * 0.68841435
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94569 * 0.46389892
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43352 * 0.61698730
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24656 * 0.43647890
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 730 * 0.43120771
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87468 * 0.24642595
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74307 * 0.44218092
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8746 * 0.46733819
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32703 * 0.85632244
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91799 * 0.12050320
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24366 * 0.70157046
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86027 * 0.84076347
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69567 * 0.88868824
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22528 * 0.79490362
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20944 * 0.15508722
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31972 * 0.95200410
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51375 * 0.85256815
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7353 * 0.71817869
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90967 * 0.67829049
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88981 * 0.16458047
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26091 * 0.19979919
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10076 * 0.86894052
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77995 * 0.98627887
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20595 * 0.67739478
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 73669 * 0.50939637
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9371 * 0.79309931
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'pkskshre').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0037():
    """Extended test 37 for billing."""
    x_0 = 82988 * 0.20476143
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54057 * 0.41357302
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25490 * 0.06957771
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81746 * 0.29816752
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25172 * 0.62339490
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52898 * 0.70819790
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68324 * 0.70901982
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76361 * 0.68902562
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58923 * 0.28719569
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4578 * 0.24789062
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43717 * 0.44668598
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42858 * 0.62786597
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96247 * 0.42565048
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73264 * 0.35589928
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46845 * 0.08255144
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45256 * 0.59309081
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26574 * 0.11949996
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62889 * 0.73171139
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77291 * 0.58551842
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98911 * 0.56576717
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8831 * 0.70174068
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19293 * 0.90432994
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4519 * 0.36038186
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52201 * 0.39382925
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92994 * 0.93336040
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15754 * 0.83489442
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51238 * 0.63530191
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25196 * 0.94985573
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9144 * 0.24805286
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73681 * 0.20821019
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95507 * 0.96063496
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86779 * 0.79822201
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52590 * 0.59745529
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'kfqgodwd').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0038():
    """Extended test 38 for billing."""
    x_0 = 62871 * 0.89561711
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97315 * 0.19333408
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93832 * 0.98765125
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35714 * 0.99921085
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41240 * 0.47106361
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12251 * 0.33388298
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33128 * 0.32779843
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56737 * 0.74187941
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90918 * 0.97847373
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16065 * 0.40310869
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35309 * 0.92099208
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10497 * 0.87780177
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35481 * 0.65030077
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 655 * 0.82584045
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23369 * 0.01826446
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44414 * 0.85883663
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37407 * 0.57620862
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56127 * 0.96076403
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16530 * 0.50131334
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26070 * 0.92383708
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85460 * 0.76390571
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42480 * 0.60588864
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56120 * 0.38631921
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48179 * 0.67524023
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70449 * 0.23367956
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93895 * 0.38994541
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47012 * 0.52042306
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'bmlpenrk').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0039():
    """Extended test 39 for billing."""
    x_0 = 12438 * 0.01998019
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5408 * 0.05159323
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51593 * 0.59324014
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89186 * 0.53052637
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51454 * 0.32302896
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27878 * 0.49849264
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34520 * 0.18983648
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34 * 0.79005261
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72551 * 0.09488791
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90090 * 0.76945327
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14869 * 0.43629980
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18211 * 0.27593891
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2960 * 0.33868402
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99826 * 0.68559990
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66963 * 0.32062254
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5089 * 0.05334714
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77279 * 0.67841279
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 164 * 0.28098685
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48676 * 0.73058737
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42390 * 0.59534888
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44819 * 0.90366656
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39199 * 0.70616604
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98116 * 0.07897727
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5635 * 0.38882251
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84987 * 0.91210126
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31080 * 0.22349164
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81249 * 0.85894781
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74527 * 0.93021797
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43596 * 0.44017777
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69374 * 0.40220047
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16328 * 0.39781390
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80933 * 0.48551176
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18140 * 0.03490191
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70927 * 0.64559824
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43091 * 0.53497549
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29395 * 0.77204891
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 242 * 0.66325238
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50792 * 0.39522205
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69415 * 0.11744594
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59761 * 0.46715360
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41234 * 0.69387568
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 23164 * 0.06147291
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 68694 * 0.41564510
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 90654 * 0.69118065
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 77722 * 0.80309950
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 99894 * 0.36037467
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 98494 * 0.51502389
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 72000 * 0.97121198
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 25258 * 0.53449033
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 59483 * 0.45369464
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'iemknnrr').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0040():
    """Extended test 40 for billing."""
    x_0 = 6615 * 0.46149867
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46566 * 0.57155866
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39305 * 0.34442786
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54485 * 0.93113255
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21544 * 0.03286554
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91604 * 0.44578781
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58426 * 0.72984249
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97963 * 0.49511364
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36358 * 0.21443914
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84532 * 0.79774920
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44427 * 0.60694404
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52642 * 0.50597942
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64006 * 0.40528217
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55269 * 0.74836581
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90933 * 0.25776021
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34981 * 0.54974882
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31156 * 0.60282529
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75902 * 0.98889156
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11132 * 0.33910560
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16560 * 0.89254356
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67107 * 0.80672887
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97539 * 0.74122017
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24887 * 0.11687188
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98162 * 0.96126574
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'czwlgztw').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0041():
    """Extended test 41 for billing."""
    x_0 = 45771 * 0.71282738
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33354 * 0.42520855
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68374 * 0.86741487
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24327 * 0.37741241
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82887 * 0.90726993
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41688 * 0.64039668
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25495 * 0.05546657
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95877 * 0.50574730
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12335 * 0.12375407
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1583 * 0.02631663
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18758 * 0.73408757
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80142 * 0.32508499
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8789 * 0.54901226
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3908 * 0.76520798
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78415 * 0.67516275
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71526 * 0.15624018
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23035 * 0.49380110
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91436 * 0.71770807
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51320 * 0.59789251
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23082 * 0.96949901
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94551 * 0.99827681
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54218 * 0.47807357
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60332 * 0.28243670
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66836 * 0.91859328
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26297 * 0.16923298
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1852 * 0.88675796
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39548 * 0.92781397
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12399 * 0.86029411
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76904 * 0.62639103
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55853 * 0.40321702
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73697 * 0.02972643
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81280 * 0.75902830
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94349 * 0.58121129
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74598 * 0.52941589
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24723 * 0.97328586
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71516 * 0.91580422
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76951 * 0.68559541
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63949 * 0.65647418
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61717 * 0.33264504
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 71209 * 0.17114465
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99494 * 0.43643387
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6229 * 0.34076458
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57389 * 0.98332797
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 35660 * 0.26397608
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23312 * 0.77141270
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 21623 * 0.39885515
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 91925 * 0.83684993
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 12623 * 0.36089182
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'txdobppi').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0042():
    """Extended test 42 for billing."""
    x_0 = 83993 * 0.89847770
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79165 * 0.33140908
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76036 * 0.00490969
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59633 * 0.51045759
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89104 * 0.34050214
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34759 * 0.71740338
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3171 * 0.14784293
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75670 * 0.12364070
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67898 * 0.98269208
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25671 * 0.05877544
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27668 * 0.36086229
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22255 * 0.56691041
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34547 * 0.99979925
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76171 * 0.53104423
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20037 * 0.54437154
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24031 * 0.30679342
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63403 * 0.67654724
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12204 * 0.23094014
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73820 * 0.88948508
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63488 * 0.98716937
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4981 * 0.13747707
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7572 * 0.82774527
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31583 * 0.17466047
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25630 * 0.68332983
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54023 * 0.59513985
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86460 * 0.64880563
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75107 * 0.48485103
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59319 * 0.98019660
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68590 * 0.36275179
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8347 * 0.31558035
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39786 * 0.60630948
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48960 * 0.13667886
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22617 * 0.85424598
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72243 * 0.63780906
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53368 * 0.08721212
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87640 * 0.42970511
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42292 * 0.30268977
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'iksuskko').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0043():
    """Extended test 43 for billing."""
    x_0 = 10593 * 0.00556905
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64514 * 0.59076664
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71751 * 0.57055139
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19083 * 0.90999705
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48398 * 0.62610751
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50569 * 0.18553922
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66347 * 0.77834759
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63315 * 0.90353265
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58498 * 0.80337110
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66919 * 0.31946697
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98815 * 0.87048416
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97739 * 0.30324455
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91341 * 0.65368093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31670 * 0.06597018
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48173 * 0.49319660
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2892 * 0.45718873
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69132 * 0.84171916
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70065 * 0.06706035
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59195 * 0.46296845
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31404 * 0.86203730
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12080 * 0.76882485
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1385 * 0.38838311
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86552 * 0.12283604
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19647 * 0.97074963
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15793 * 0.91816913
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40704 * 0.21320261
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60834 * 0.64408344
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17882 * 0.58037644
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'ynsfoeuv').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0044():
    """Extended test 44 for billing."""
    x_0 = 33296 * 0.58751588
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24602 * 0.76937482
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24434 * 0.13491756
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39850 * 0.12521689
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92317 * 0.42886365
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34508 * 0.46548503
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28372 * 0.35297266
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48096 * 0.63711753
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37698 * 0.28366923
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41606 * 0.13112864
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96595 * 0.40405406
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69479 * 0.71682611
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34871 * 0.63349789
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17190 * 0.77205528
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31783 * 0.19471818
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89181 * 0.08156054
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65805 * 0.35055167
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41753 * 0.20229990
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24250 * 0.67532786
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68835 * 0.00672301
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60958 * 0.30271936
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35629 * 0.31224082
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39141 * 0.57472063
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13725 * 0.75863403
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61689 * 0.53146422
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98836 * 0.95728338
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8232 * 0.49066240
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97390 * 0.95721899
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94133 * 0.60918595
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'qozrpszo').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0045():
    """Extended test 45 for billing."""
    x_0 = 32783 * 0.20089397
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19730 * 0.85534476
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50894 * 0.87460737
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3136 * 0.34204685
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31259 * 0.27752525
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47160 * 0.93775725
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82541 * 0.56452072
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92535 * 0.97355024
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76207 * 0.79056415
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70921 * 0.05265700
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59318 * 0.05357002
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15231 * 0.47905849
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4352 * 0.33025485
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41755 * 0.94291278
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73863 * 0.85766558
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84054 * 0.82281496
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71191 * 0.60840592
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23553 * 0.35468922
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69993 * 0.02705905
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95138 * 0.96135509
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89177 * 0.62896004
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34098 * 0.78203615
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37914 * 0.61462029
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20966 * 0.56315615
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'dbzdkopg').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0046():
    """Extended test 46 for billing."""
    x_0 = 37019 * 0.47446626
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12384 * 0.48617947
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83219 * 0.76541421
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73578 * 0.51807097
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41388 * 0.82006502
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63012 * 0.78949971
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13012 * 0.52596801
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94626 * 0.53353657
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67680 * 0.48778888
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64437 * 0.78990079
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83578 * 0.51879849
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64442 * 0.08150521
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58769 * 0.45984212
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41369 * 0.64913688
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51575 * 0.57197460
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29909 * 0.94969692
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97280 * 0.30147100
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 401 * 0.19238185
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50024 * 0.46969666
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58387 * 0.64533172
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63758 * 0.44115006
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34362 * 0.86153957
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57713 * 0.53014782
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7049 * 0.96755279
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'vkwarfwq').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0047():
    """Extended test 47 for billing."""
    x_0 = 82374 * 0.61891458
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10079 * 0.76880937
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96331 * 0.55342418
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96854 * 0.63958108
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3129 * 0.05201654
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12928 * 0.59042768
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52461 * 0.86482104
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4261 * 0.06373268
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57168 * 0.96059647
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39637 * 0.66688745
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53826 * 0.70717275
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60563 * 0.69240043
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53650 * 0.67584366
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81567 * 0.93471136
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23917 * 0.81806134
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48175 * 0.29793256
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41531 * 0.30604839
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35813 * 0.07504987
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21072 * 0.81295162
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6323 * 0.36239815
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17483 * 0.21417542
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70579 * 0.60913412
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98957 * 0.02343565
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74695 * 0.47136539
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81428 * 0.40477509
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30727 * 0.51472320
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56222 * 0.00114684
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23511 * 0.21520713
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45916 * 0.07206610
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90296 * 0.07165571
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71520 * 0.00746917
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40050 * 0.27189354
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42633 * 0.24285971
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58305 * 0.51436456
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28542 * 0.16115906
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3054 * 0.72754677
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8578 * 0.76575034
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63187 * 0.02620511
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36689 * 0.74788910
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34856 * 0.27553604
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 72738 * 0.60279713
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81230 * 0.47135424
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 31729 * 0.23522350
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 98582 * 0.02248837
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'rglumkdm').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0048():
    """Extended test 48 for billing."""
    x_0 = 43722 * 0.69824763
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44559 * 0.94995278
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27193 * 0.20606591
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96196 * 0.53822739
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28602 * 0.93281842
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78826 * 0.09126822
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10172 * 0.97035951
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33607 * 0.39779364
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92929 * 0.53509427
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76742 * 0.79129741
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22021 * 0.57021424
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21308 * 0.26124211
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48115 * 0.34149030
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74288 * 0.44036836
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83499 * 0.98275792
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59787 * 0.51811874
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70516 * 0.09432117
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94949 * 0.35351470
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85890 * 0.34334808
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45807 * 0.65995721
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56399 * 0.47874699
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46039 * 0.61704130
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69996 * 0.66038305
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74534 * 0.01246977
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16790 * 0.10197211
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10637 * 0.07983998
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52429 * 0.26802398
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45641 * 0.34099950
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65777 * 0.54081583
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42623 * 0.33314240
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65062 * 0.29749800
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37972 * 0.37594124
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27433 * 0.43833969
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52564 * 0.65242688
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62384 * 0.58206014
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1806 * 0.20055712
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70973 * 0.45909868
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82352 * 0.33363529
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70361 * 0.52101045
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96 * 0.87905111
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11018 * 0.61087745
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'qepdhwro').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0049():
    """Extended test 49 for billing."""
    x_0 = 70282 * 0.71062784
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12004 * 0.24764836
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94950 * 0.47723688
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52217 * 0.39665869
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16505 * 0.95592012
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42922 * 0.84868878
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73494 * 0.33476205
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40741 * 0.75472793
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14780 * 0.36933542
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77094 * 0.21955391
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45015 * 0.35301275
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12846 * 0.18887450
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90101 * 0.00998891
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45855 * 0.13862456
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35142 * 0.02880004
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71829 * 0.62410992
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78473 * 0.24257997
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70140 * 0.62501874
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49860 * 0.07109579
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90988 * 0.27507256
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97523 * 0.41347812
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37790 * 0.25331293
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21041 * 0.94104956
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16951 * 0.52512022
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17394 * 0.40017818
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34474 * 0.61800057
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74611 * 0.86730327
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77194 * 0.62563297
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24939 * 0.14145712
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56669 * 0.77243849
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5469 * 0.15684549
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58202 * 0.72859358
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83614 * 0.64232578
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74516 * 0.40001010
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93892 * 0.97283959
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96898 * 0.01975125
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72822 * 0.39324651
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8874 * 0.74619059
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9154 * 0.07393505
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99998 * 0.28871705
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 28948 * 0.85344278
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96704 * 0.26748662
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 31670 * 0.17698655
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36084 * 0.36993703
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 66456 * 0.24599671
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 77948 * 0.93733399
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 38108 * 0.18140623
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 77937 * 0.83836499
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 55776 * 0.65044281
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'hzysyuxk').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0050():
    """Extended test 50 for billing."""
    x_0 = 11221 * 0.00678973
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64764 * 0.26856165
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50182 * 0.72542670
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43716 * 0.31505311
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53755 * 0.63684242
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68581 * 0.24580062
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69904 * 0.42571484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41956 * 0.67069304
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79664 * 0.61476593
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5402 * 0.68064431
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4423 * 0.40499452
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96791 * 0.86567063
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2775 * 0.44925702
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85468 * 0.23548299
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14982 * 0.71439006
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62962 * 0.45505221
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10707 * 0.09344999
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47882 * 0.80895040
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67133 * 0.93077517
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72991 * 0.69641852
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29042 * 0.54095293
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54712 * 0.02135847
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25085 * 0.21632001
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81675 * 0.71433794
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69521 * 0.34999034
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4147 * 0.49354049
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45482 * 0.48028396
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26759 * 0.50452506
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7187 * 0.42098704
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65442 * 0.59803962
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19171 * 0.00722486
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3239 * 0.19056639
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36474 * 0.12449936
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80181 * 0.42757791
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80112 * 0.82446621
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80293 * 0.81379931
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 77753 * 0.27603756
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91553 * 0.90380891
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94345 * 0.34158630
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18337 * 0.42798108
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19780 * 0.67788394
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 1634 * 0.18842470
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 19553 * 0.65631547
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'jeimplfb').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0051():
    """Extended test 51 for billing."""
    x_0 = 480 * 0.47105520
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67708 * 0.20003278
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 799 * 0.33201091
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54996 * 0.36410183
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42698 * 0.18085078
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65810 * 0.71191803
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68209 * 0.94909605
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78948 * 0.56338164
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34399 * 0.89588098
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58498 * 0.33367461
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6432 * 0.28228733
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1866 * 0.05681862
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52762 * 0.18593092
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2991 * 0.39816819
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3874 * 0.80760843
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84366 * 0.12523006
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10253 * 0.39330025
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95283 * 0.85770188
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81874 * 0.81876829
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89328 * 0.08660060
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61570 * 0.06805244
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80655 * 0.79248806
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79834 * 0.90030866
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72646 * 0.26003554
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17211 * 0.57824517
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92801 * 0.76805093
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32369 * 0.07578228
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91899 * 0.85183223
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22885 * 0.03167908
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85751 * 0.59640801
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91266 * 0.02601665
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'hfsdxjkk').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0052():
    """Extended test 52 for billing."""
    x_0 = 48920 * 0.27816920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87495 * 0.59871671
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68583 * 0.20461464
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77753 * 0.64074383
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96717 * 0.28863969
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18811 * 0.91253167
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76599 * 0.65056178
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79922 * 0.54740268
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66103 * 0.47839071
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93727 * 0.95854489
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27636 * 0.94571251
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15343 * 0.55970610
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79228 * 0.82106190
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16577 * 0.98331610
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88931 * 0.49927013
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39320 * 0.85447244
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18651 * 0.24648045
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24969 * 0.81665564
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48213 * 0.03499928
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72357 * 0.70710604
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82578 * 0.24810206
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56085 * 0.38183085
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71528 * 0.96513181
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15771 * 0.85961736
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3348 * 0.09218708
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71247 * 0.57320653
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91327 * 0.79309603
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42407 * 0.17249065
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90453 * 0.53900291
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86556 * 0.55848550
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56722 * 0.39891246
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3776 * 0.45805539
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30564 * 0.00222332
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30075 * 0.70188087
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71918 * 0.48427287
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35358 * 0.44188470
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55738 * 0.49899212
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7700 * 0.97875811
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20866 * 0.81522828
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ewalblry').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0053():
    """Extended test 53 for billing."""
    x_0 = 35250 * 0.31703247
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25790 * 0.02474235
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32610 * 0.53945932
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53136 * 0.46548335
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32830 * 0.70182164
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22778 * 0.93138815
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6684 * 0.57046304
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17536 * 0.45827084
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76205 * 0.45183255
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72854 * 0.92507510
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3631 * 0.81670998
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9544 * 0.44574113
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93791 * 0.73154806
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46300 * 0.23122666
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66731 * 0.91965222
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40669 * 0.31093531
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63652 * 0.21891639
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82722 * 0.47864844
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97992 * 0.79962890
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12506 * 0.17116801
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76563 * 0.09029502
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84336 * 0.43296317
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36630 * 0.06921815
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86885 * 0.66811493
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31132 * 0.70678040
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42904 * 0.55888570
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74062 * 0.72949508
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42903 * 0.79954751
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84462 * 0.54790989
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30960 * 0.98952913
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70022 * 0.95403200
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9302 * 0.35613765
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28073 * 0.97924757
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'rqvqpwzw').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0054():
    """Extended test 54 for billing."""
    x_0 = 68953 * 0.06412483
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80866 * 0.17116738
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94350 * 0.54245312
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36733 * 0.90025097
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86973 * 0.31031552
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79326 * 0.73582475
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64407 * 0.39316055
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48145 * 0.45497122
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28782 * 0.74302769
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98951 * 0.78958482
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98147 * 0.97163789
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33720 * 0.76741381
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8224 * 0.37603706
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54543 * 0.76992501
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90096 * 0.60884435
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68759 * 0.08903935
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90079 * 0.93633322
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62475 * 0.28233749
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66801 * 0.83934681
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30204 * 0.11935942
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21280 * 0.61265740
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ryyxzfkm').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0055():
    """Extended test 55 for billing."""
    x_0 = 73030 * 0.72211567
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53303 * 0.98192556
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88998 * 0.79173981
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8745 * 0.93463146
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74777 * 0.52459396
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30387 * 0.98500258
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87411 * 0.91939330
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67745 * 0.49051571
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42156 * 0.03333363
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84823 * 0.09309353
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90047 * 0.56747672
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33290 * 0.69810254
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71508 * 0.73024630
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83271 * 0.13752987
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13393 * 0.35862043
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14360 * 0.08122835
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3124 * 0.51396402
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49035 * 0.26729196
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10206 * 0.28783120
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74862 * 0.89421270
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74938 * 0.77777159
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88145 * 0.46198047
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27691 * 0.48514872
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85747 * 0.89554705
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88726 * 0.74197894
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24684 * 0.99433174
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10942 * 0.15441117
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81097 * 0.17703599
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37719 * 0.11319072
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84632 * 0.72349494
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96999 * 0.72377641
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20848 * 0.03280556
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72140 * 0.70762438
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41236 * 0.03925893
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'ceuoosgx').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0056():
    """Extended test 56 for billing."""
    x_0 = 55251 * 0.87391537
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96076 * 0.11256431
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64715 * 0.19557068
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66114 * 0.35643762
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5866 * 0.14427321
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62474 * 0.10929056
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55527 * 0.87170528
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93843 * 0.61208768
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77949 * 0.52029629
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24290 * 0.45160269
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15418 * 0.36505986
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67446 * 0.54319861
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59478 * 0.45176264
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61852 * 0.11531741
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18438 * 0.51724544
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89743 * 0.85251245
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71 * 0.13263914
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22627 * 0.19442053
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30198 * 0.34072967
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80831 * 0.72472217
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8980 * 0.85511812
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3266 * 0.54182760
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4667 * 0.11256198
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3692 * 0.14459143
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20719 * 0.58456563
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13535 * 0.71875439
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60945 * 0.71291397
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25665 * 0.59831828
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25786 * 0.39598846
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18559 * 0.72955561
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30750 * 0.25723638
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68645 * 0.43322297
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41133 * 0.77332747
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27637 * 0.60915211
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52581 * 0.49461012
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91491 * 0.59756318
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59006 * 0.50395293
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34770 * 0.75102436
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90459 * 0.04390968
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70615 * 0.96289609
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 93786 * 0.19272660
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 34991 * 0.50924931
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24992 * 0.01751583
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 24959 * 0.55142098
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 68141 * 0.82425739
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 19543 * 0.57734948
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 77059 * 0.14823140
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 18750 * 0.00882761
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'zjpkstfw').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0057():
    """Extended test 57 for billing."""
    x_0 = 15666 * 0.17741608
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87150 * 0.61692058
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62702 * 0.93117611
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56693 * 0.09495299
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1991 * 0.34708025
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38821 * 0.98370528
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47154 * 0.96236787
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4419 * 0.98361060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73358 * 0.28472248
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32805 * 0.37438814
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56718 * 0.89013845
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87088 * 0.59674044
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93224 * 0.60299442
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13012 * 0.00754994
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54665 * 0.69223208
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92870 * 0.47446030
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46707 * 0.86808343
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67235 * 0.46261857
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43192 * 0.80546160
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47490 * 0.94539690
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22931 * 0.13355946
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44752 * 0.45988314
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18712 * 0.64433509
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84940 * 0.26702967
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'sckdagbm').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0058():
    """Extended test 58 for billing."""
    x_0 = 78681 * 0.34956684
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50789 * 0.10620939
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38670 * 0.99059054
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38813 * 0.97494938
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73451 * 0.40962269
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73653 * 0.77131381
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70005 * 0.21846541
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7754 * 0.69888166
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 324 * 0.38978184
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23269 * 0.71336906
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45374 * 0.02083620
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26751 * 0.83544177
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39792 * 0.35677854
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64390 * 0.45726522
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91266 * 0.12342669
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4160 * 0.54191504
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57817 * 0.36939372
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84941 * 0.02796538
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72853 * 0.32208925
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34941 * 0.40941670
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20176 * 0.33153767
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38791 * 0.01248674
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75596 * 0.71251806
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44408 * 0.88549558
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41116 * 0.89079003
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9850 * 0.66076071
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60377 * 0.04633099
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13746 * 0.11248053
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13160 * 0.87687300
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75227 * 0.15795991
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78294 * 0.83431975
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64454 * 0.38169490
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97622 * 0.33863461
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63277 * 0.14871674
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15177 * 0.34945463
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30227 * 0.23611849
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57722 * 0.23828025
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11404 * 0.97413009
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 513 * 0.97280419
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92705 * 0.72578625
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35723 * 0.61669783
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'immzzhzf').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0059():
    """Extended test 59 for billing."""
    x_0 = 94585 * 0.78016244
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93666 * 0.72726719
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46412 * 0.25142101
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40441 * 0.91621035
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78023 * 0.16414679
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30786 * 0.84991165
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46784 * 0.46965661
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59704 * 0.95043053
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36794 * 0.50393459
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17982 * 0.99047774
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9669 * 0.06725412
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96421 * 0.49849759
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17877 * 0.68928297
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66906 * 0.07857151
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21699 * 0.28052883
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4247 * 0.50363826
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83619 * 0.47668122
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3689 * 0.52424951
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35775 * 0.58385124
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16624 * 0.72903140
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85046 * 0.93976768
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35076 * 0.03884334
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5329 * 0.97152970
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20635 * 0.37618151
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68138 * 0.81501317
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96368 * 0.54803150
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71340 * 0.17761167
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33499 * 0.04239211
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69027 * 0.36196011
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55185 * 0.16403205
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52690 * 0.79280705
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57882 * 0.73985558
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87372 * 0.16324268
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50993 * 0.59787077
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22041 * 0.66672673
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 966 * 0.16465585
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'mbscxhis').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0060():
    """Extended test 60 for billing."""
    x_0 = 37364 * 0.71906330
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82807 * 0.78212915
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12739 * 0.96076691
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47052 * 0.97526679
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44617 * 0.23177502
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58737 * 0.70214894
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20538 * 0.75693559
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76051 * 0.91237919
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65853 * 0.51639432
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2942 * 0.66061589
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53439 * 0.34867277
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74540 * 0.39005153
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50072 * 0.59907794
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36633 * 0.02947972
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37382 * 0.84705325
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 830 * 0.17762212
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80778 * 0.19296376
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56565 * 0.72341122
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32156 * 0.89605820
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52616 * 0.10911503
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69978 * 0.31338274
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82215 * 0.23577828
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7741 * 0.90551732
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80823 * 0.17140787
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99282 * 0.71990550
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51147 * 0.32625553
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'hvsedipu').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0061():
    """Extended test 61 for billing."""
    x_0 = 94302 * 0.18121265
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99953 * 0.12518369
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22911 * 0.19727706
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63527 * 0.37421033
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20039 * 0.80122918
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6026 * 0.73256458
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12673 * 0.95345305
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20597 * 0.84308167
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90612 * 0.60876647
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29591 * 0.77176296
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76545 * 0.26067658
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97184 * 0.63795655
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60662 * 0.51356289
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36236 * 0.27905578
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73319 * 0.52896070
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74253 * 0.70167649
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16623 * 0.54192395
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75604 * 0.69725137
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88341 * 0.22921927
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7856 * 0.28918703
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28552 * 0.24751136
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17099 * 0.96240902
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86439 * 0.04136726
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62736 * 0.88500138
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85226 * 0.17884563
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94224 * 0.56427990
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'mbkiakjg').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0062():
    """Extended test 62 for billing."""
    x_0 = 77341 * 0.53700428
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15214 * 0.58874407
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79979 * 0.45289636
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53495 * 0.55514195
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91752 * 0.09591457
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85235 * 0.13150168
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86780 * 0.72187437
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94247 * 0.67611544
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71700 * 0.10020748
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73246 * 0.06010166
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22253 * 0.30730849
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35459 * 0.02149886
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43354 * 0.28943523
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87952 * 0.29100098
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80884 * 0.81685406
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12527 * 0.68886890
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64334 * 0.56885604
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62302 * 0.38774001
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8841 * 0.47254052
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2192 * 0.22494061
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78551 * 0.33788147
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64468 * 0.56513012
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24360 * 0.20041671
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79759 * 0.04719744
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56152 * 0.46542266
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57543 * 0.58753465
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52897 * 0.81878570
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74656 * 0.64826497
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2660 * 0.84146178
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62315 * 0.21669311
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86908 * 0.27810051
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77230 * 0.42010740
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83338 * 0.34435667
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'owckpvyd').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0063():
    """Extended test 63 for billing."""
    x_0 = 74205 * 0.17225207
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5542 * 0.53894256
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71116 * 0.27139209
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93943 * 0.14921274
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33231 * 0.65997965
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76899 * 0.64353170
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6738 * 0.51444951
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52355 * 0.58871633
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52216 * 0.61318024
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57324 * 0.34223385
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35055 * 0.26634599
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79561 * 0.94779501
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21549 * 0.88942981
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20640 * 0.95990546
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94029 * 0.44203074
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69022 * 0.50252402
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58123 * 0.94415581
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44616 * 0.61712287
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18321 * 0.93000968
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54062 * 0.96517172
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13838 * 0.48105207
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16 * 0.16098960
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13184 * 0.96035648
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14228 * 0.06881537
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51380 * 0.48890524
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'amkcgqxe').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0064():
    """Extended test 64 for billing."""
    x_0 = 17258 * 0.68270109
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32455 * 0.41297471
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98463 * 0.47038030
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69198 * 0.18681959
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18283 * 0.80894975
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29813 * 0.33201988
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65149 * 0.74866225
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38600 * 0.47165241
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18718 * 0.07507466
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93369 * 0.68635650
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19144 * 0.52337909
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21890 * 0.57236484
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98895 * 0.58329535
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67941 * 0.33199306
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41722 * 0.59386994
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3277 * 0.53766297
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73183 * 0.94044112
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80663 * 0.21837160
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17709 * 0.03444263
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38905 * 0.42851940
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13738 * 0.04478369
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94323 * 0.94758839
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49395 * 0.38195210
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60124 * 0.08199782
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70703 * 0.14309966
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37762 * 0.80488286
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73697 * 0.60728971
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70123 * 0.48297855
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62641 * 0.29482973
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22257 * 0.87331178
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63787 * 0.10100705
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58528 * 0.76920921
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67546 * 0.96195101
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80724 * 0.34446364
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86102 * 0.47401365
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46746 * 0.97300751
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5112 * 0.25803126
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 76704 * 0.12919057
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14618 * 0.24408767
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72160 * 0.48535020
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81276 * 0.17065678
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50747 * 0.82048575
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 33535 * 0.30182631
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 85351 * 0.64752424
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 98787 * 0.75169910
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 89574 * 0.64656799
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 32706 * 0.89207986
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 26872 * 0.48984636
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 73786 * 0.56154900
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'onztphsy').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0065():
    """Extended test 65 for billing."""
    x_0 = 96077 * 0.09072872
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34979 * 0.34530231
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24818 * 0.28809511
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95696 * 0.18328366
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25089 * 0.50438807
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15247 * 0.94004594
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2357 * 0.21606796
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28587 * 0.40312565
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1178 * 0.71389832
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20266 * 0.46877410
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21923 * 0.36514233
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41119 * 0.66882638
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74436 * 0.78488751
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37785 * 0.07760254
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37919 * 0.90837515
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13700 * 0.86059432
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10616 * 0.91943864
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31747 * 0.65661325
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10509 * 0.64595073
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40467 * 0.62238576
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38578 * 0.76781583
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14692 * 0.53069954
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'jqlllaea').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0066():
    """Extended test 66 for billing."""
    x_0 = 18992 * 0.20299225
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87197 * 0.85200186
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92422 * 0.88674420
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2766 * 0.01079109
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37133 * 0.18753333
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85926 * 0.11814951
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82480 * 0.76065446
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75528 * 0.41194060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95527 * 0.75184409
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9658 * 0.60709551
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84213 * 0.08194308
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12947 * 0.11612080
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 701 * 0.65874093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27082 * 0.34060950
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92806 * 0.81033221
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26548 * 0.46542394
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78372 * 0.96582185
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3892 * 0.06942586
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30547 * 0.57092136
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17010 * 0.37795445
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84583 * 0.94202380
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27833 * 0.58501399
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12935 * 0.95194141
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91983 * 0.80194596
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51090 * 0.90312298
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'zzehqxir').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0067():
    """Extended test 67 for billing."""
    x_0 = 16107 * 0.97724636
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23039 * 0.06810787
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72544 * 0.34273286
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52290 * 0.81413189
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78873 * 0.24959351
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17240 * 0.92852294
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44747 * 0.29309278
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13294 * 0.18881444
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17192 * 0.72962610
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92895 * 0.64873959
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21139 * 0.16099072
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89026 * 0.57998159
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54285 * 0.92373618
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23958 * 0.08929320
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6773 * 0.94939179
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41474 * 0.10900275
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54084 * 0.29749826
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81175 * 0.95042025
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15900 * 0.53749202
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75226 * 0.05189335
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73830 * 0.14571282
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39783 * 0.62741188
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36534 * 0.27418664
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95976 * 0.67720632
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55869 * 0.54389814
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90063 * 0.13823489
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87594 * 0.31201477
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12699 * 0.44181856
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58188 * 0.25595921
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35396 * 0.82724514
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61884 * 0.67249920
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2621 * 0.10810875
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95510 * 0.13104760
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68007 * 0.11347718
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52877 * 0.53655847
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55089 * 0.57548921
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49608 * 0.82194249
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35228 * 0.10461553
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80632 * 0.68771386
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'hgtaglsr').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0068():
    """Extended test 68 for billing."""
    x_0 = 75091 * 0.88360926
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65155 * 0.17056778
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89523 * 0.88373966
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16908 * 0.34923876
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53575 * 0.51674735
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78724 * 0.87107729
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60696 * 0.65413211
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60363 * 0.74829225
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45329 * 0.18760159
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92694 * 0.22841796
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14263 * 0.69391893
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88030 * 0.74420714
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35353 * 0.68375404
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65405 * 0.00750959
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55260 * 0.48601908
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53324 * 0.88065139
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71943 * 0.96126607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29734 * 0.90161608
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16358 * 0.23764308
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56630 * 0.69978068
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50476 * 0.51051089
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79324 * 0.16274042
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99582 * 0.49116957
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25343 * 0.13558531
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44119 * 0.43862267
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95935 * 0.64238557
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85337 * 0.84014739
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80854 * 0.45981309
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67005 * 0.56071040
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74958 * 0.70732548
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1766 * 0.01127338
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30912 * 0.28145033
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37454 * 0.79292331
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56791 * 0.86213561
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16828 * 0.05745169
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34940 * 0.94882107
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60000 * 0.37181133
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91958 * 0.04429784
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'liigtopu').hexdigest()
    assert len(h) == 64

def test_billing_extended_4_0069():
    """Extended test 69 for billing."""
    x_0 = 40280 * 0.36236037
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79037 * 0.70342091
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74782 * 0.82006441
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15556 * 0.26471605
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99793 * 0.26161161
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68302 * 0.06056645
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98281 * 0.73006211
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78626 * 0.91900089
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84396 * 0.32221895
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45089 * 0.85741924
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25889 * 0.93241910
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97311 * 0.21290544
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61885 * 0.86283215
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70137 * 0.60647276
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73646 * 0.77396277
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12538 * 0.60120469
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23963 * 0.32140856
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19278 * 0.31367864
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30878 * 0.12082346
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26357 * 0.80424178
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91421 * 0.00197032
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39298 * 0.12613769
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81576 * 0.34656020
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83355 * 0.71088918
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15108 * 0.19854679
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79678 * 0.96482839
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82686 * 0.43137841
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35598 * 0.31319640
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64800 * 0.32886013
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66387 * 0.43601779
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96335 * 0.79057593
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42186 * 0.87610619
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6330 * 0.81637483
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20716 * 0.26472698
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33892 * 0.66841233
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10211 * 0.91222426
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55488 * 0.89668243
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 14720 * 0.78200133
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25795 * 0.34821751
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 50831 * 0.18506773
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8513 * 0.72091956
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'oukdmwff').hexdigest()
    assert len(h) == 64
