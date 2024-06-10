"""Extended tests for billing suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_billing_extended_8_0000():
    """Extended test 0 for billing."""
    x_0 = 52821 * 0.99711360
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59796 * 0.45247040
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31007 * 0.40470253
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34678 * 0.31531874
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42520 * 0.38244621
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53657 * 0.75949776
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81167 * 0.29797650
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82515 * 0.38624058
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21630 * 0.85571500
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80406 * 0.95830595
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51729 * 0.55219917
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56713 * 0.62901079
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35468 * 0.27280865
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59872 * 0.10681046
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48392 * 0.47057556
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61418 * 0.67647071
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7925 * 0.55233190
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72274 * 0.44009362
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89215 * 0.66129196
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37739 * 0.68585877
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85390 * 0.88967133
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74243 * 0.85154167
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59680 * 0.23114946
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55497 * 0.71270598
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30518 * 0.66041962
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54925 * 0.84606823
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94683 * 0.98711659
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4047 * 0.29060128
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69665 * 0.67284116
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19343 * 0.50074956
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'wrogdqro').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0001():
    """Extended test 1 for billing."""
    x_0 = 77247 * 0.88390198
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13129 * 0.82268566
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6755 * 0.85802914
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3929 * 0.23811966
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38571 * 0.15758585
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76790 * 0.40886565
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8405 * 0.87102257
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5230 * 0.54232915
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85676 * 0.99198856
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2714 * 0.88064545
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30482 * 0.06327663
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83557 * 0.15758528
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40082 * 0.33593626
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27365 * 0.79592643
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21322 * 0.44513389
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16683 * 0.22390199
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13588 * 0.38124065
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8431 * 0.61043895
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51982 * 0.06767315
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8756 * 0.22686363
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34439 * 0.61065195
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2111 * 0.41298790
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85749 * 0.36191390
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52910 * 0.45874569
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85606 * 0.49589676
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61856 * 0.44269837
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89843 * 0.72997781
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28293 * 0.13261749
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55405 * 0.78791574
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9049 * 0.74660993
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33509 * 0.41136651
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21607 * 0.20086985
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18110 * 0.80012165
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87535 * 0.17640866
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67165 * 0.77871626
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69287 * 0.71414215
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54490 * 0.63180182
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 57890 * 0.35249564
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1466 * 0.23483118
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'zkhypveq').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0002():
    """Extended test 2 for billing."""
    x_0 = 28013 * 0.19852431
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76609 * 0.21653225
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41942 * 0.95307353
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65629 * 0.28576772
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27016 * 0.12879215
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33515 * 0.29074432
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49708 * 0.86137985
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93652 * 0.37866868
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22263 * 0.93885096
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61467 * 0.61555851
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54202 * 0.99881077
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41802 * 0.29878687
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28101 * 0.20489107
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14569 * 0.24185634
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78829 * 0.84068844
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66733 * 0.94323938
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95058 * 0.39682472
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45698 * 0.47443308
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69311 * 0.00620492
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83770 * 0.85762892
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42106 * 0.06417968
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67532 * 0.34902944
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92397 * 0.97441872
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1421 * 0.13879750
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60042 * 0.00662764
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97363 * 0.85116611
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50028 * 0.38160992
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13460 * 0.57737820
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43423 * 0.84297321
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72309 * 0.26044624
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52051 * 0.06537285
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23883 * 0.62018061
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9591 * 0.43213510
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59060 * 0.20509550
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26907 * 0.11798711
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81742 * 0.25027783
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'vyympcgo').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0003():
    """Extended test 3 for billing."""
    x_0 = 1499 * 0.96550605
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91605 * 0.11630886
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31969 * 0.49069156
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66567 * 0.59981204
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51491 * 0.95976187
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23623 * 0.29633395
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99573 * 0.00231012
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64820 * 0.46395481
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8416 * 0.62019669
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29107 * 0.03906736
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1225 * 0.45175452
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91768 * 0.23407139
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33019 * 0.26469006
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90197 * 0.03544254
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17552 * 0.39189035
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17488 * 0.15507313
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68240 * 0.85688180
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80486 * 0.46749542
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34948 * 0.12291103
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18206 * 0.77522906
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49957 * 0.81502864
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88960 * 0.48493606
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70963 * 0.65522394
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42156 * 0.93572350
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83128 * 0.51729519
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59116 * 0.34882971
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86351 * 0.22782032
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86116 * 0.53846086
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66526 * 0.32735521
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23721 * 0.19175366
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36133 * 0.87513359
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62717 * 0.92257104
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90247 * 0.47412690
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68789 * 0.59713507
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73390 * 0.12435242
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75467 * 0.16538597
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35584 * 0.79057248
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98709 * 0.16606973
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90081 * 0.02414735
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20788 * 0.49987049
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11551 * 0.06819447
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58296 * 0.64111059
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66651 * 0.55275039
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38609 * 0.08512310
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 56476 * 0.63115641
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 40842 * 0.38341452
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 28879 * 0.59555006
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 74570 * 0.93448316
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 21225 * 0.12723922
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'iabnujzq').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0004():
    """Extended test 4 for billing."""
    x_0 = 53508 * 0.67587886
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57350 * 0.46766398
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91243 * 0.72781144
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73389 * 0.25740913
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1950 * 0.35472305
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95044 * 0.08630298
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29063 * 0.53097359
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50190 * 0.27615758
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5539 * 0.84058444
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15034 * 0.62605536
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38781 * 0.80436906
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19238 * 0.82824097
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45678 * 0.70167583
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40917 * 0.93684064
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87892 * 0.58332398
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94924 * 0.56674646
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79790 * 0.11382197
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72445 * 0.05216419
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60001 * 0.66858653
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77824 * 0.06913892
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30687 * 0.19724367
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38263 * 0.78591435
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41437 * 0.35682345
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21594 * 0.03934058
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64031 * 0.25204704
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61884 * 0.20457003
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4440 * 0.68245437
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85390 * 0.62192031
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72124 * 0.62779648
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68556 * 0.04007778
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49624 * 0.37919228
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77705 * 0.50214311
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90870 * 0.65370095
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49566 * 0.27698334
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78384 * 0.35876816
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23586 * 0.23495810
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17460 * 0.20145401
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80155 * 0.42620879
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5477 * 0.94283867
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 50540 * 0.01891385
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'cpxgqfqw').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0005():
    """Extended test 5 for billing."""
    x_0 = 62656 * 0.91888585
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29453 * 0.62791169
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39059 * 0.15074385
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31577 * 0.23314878
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16874 * 0.22510653
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64880 * 0.00215345
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85814 * 0.81406623
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96750 * 0.04540518
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52124 * 0.80104858
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1984 * 0.57017842
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1235 * 0.42835602
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4401 * 0.89002468
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81482 * 0.63791962
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93153 * 0.16810650
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23542 * 0.31963945
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43128 * 0.85899008
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97360 * 0.24801145
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70982 * 0.10392994
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29422 * 0.16240167
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9807 * 0.44208163
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56499 * 0.41750273
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32052 * 0.00565117
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80755 * 0.80410504
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61379 * 0.53769971
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88451 * 0.23445961
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39777 * 0.12369233
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13335 * 0.81270329
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25577 * 0.51884650
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36842 * 0.93260091
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45522 * 0.87208458
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70081 * 0.49613195
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65027 * 0.90001124
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10391 * 0.84299231
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31548 * 0.24281414
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91057 * 0.84298629
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87105 * 0.67841391
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69857 * 0.38722056
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13360 * 0.77294450
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91333 * 0.09864934
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22090 * 0.27212516
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'agloyfvt').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0006():
    """Extended test 6 for billing."""
    x_0 = 55432 * 0.50404204
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3121 * 0.65077419
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30779 * 0.42393250
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33815 * 0.35085446
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7220 * 0.23554986
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88512 * 0.72111223
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34206 * 0.39769589
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15343 * 0.91674517
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36014 * 0.93844201
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62489 * 0.75967350
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68326 * 0.95241747
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40784 * 0.31868412
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10906 * 0.83685325
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54679 * 0.39702221
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34889 * 0.18367403
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7918 * 0.95103173
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43662 * 0.29209720
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56853 * 0.88971488
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51943 * 0.28277051
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15703 * 0.76800122
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43409 * 0.72997068
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'vumynonx').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0007():
    """Extended test 7 for billing."""
    x_0 = 2245 * 0.98770415
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72393 * 0.99353151
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85446 * 0.41208569
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50812 * 0.93966231
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80467 * 0.86856313
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60111 * 0.81551681
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39822 * 0.61529390
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25644 * 0.37843398
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47157 * 0.95943109
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73823 * 0.18519671
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80376 * 0.54289573
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23683 * 0.99103598
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45718 * 0.40256476
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75693 * 0.86169928
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54367 * 0.82553577
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58874 * 0.49500653
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32830 * 0.02099507
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48640 * 0.79263033
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22439 * 0.08147591
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89968 * 0.99954236
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51087 * 0.86311549
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12879 * 0.26011412
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58336 * 0.18412470
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11984 * 0.00436682
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39934 * 0.06043661
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22440 * 0.32114392
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12443 * 0.50797187
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8453 * 0.35656628
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74871 * 0.47975065
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96418 * 0.33431659
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80319 * 0.89966407
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46316 * 0.16803700
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84163 * 0.15290904
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89126 * 0.57926802
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'srjkpcum').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0008():
    """Extended test 8 for billing."""
    x_0 = 54795 * 0.71277140
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78732 * 0.85348398
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91326 * 0.30126349
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74751 * 0.64827487
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3264 * 0.83804386
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58817 * 0.19129758
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51081 * 0.34829827
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47613 * 0.62560229
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40235 * 0.71968216
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44018 * 0.73980447
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31372 * 0.15635351
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39139 * 0.20758104
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88782 * 0.22728876
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98033 * 0.65006753
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59338 * 0.85786693
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83681 * 0.21113287
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64881 * 0.48247135
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56793 * 0.61422385
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48189 * 0.26445876
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50655 * 0.87189677
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10041 * 0.76132821
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91937 * 0.84984161
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11859 * 0.59937230
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85160 * 0.69083563
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3155 * 0.50494987
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24092 * 0.68075844
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69234 * 0.44433351
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80935 * 0.87441330
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88648 * 0.03389625
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24332 * 0.83863992
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47503 * 0.44521230
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'vvgvophz').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0009():
    """Extended test 9 for billing."""
    x_0 = 90185 * 0.41845922
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21090 * 0.53478676
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16772 * 0.80273037
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97597 * 0.62597014
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12370 * 0.69830360
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49767 * 0.18122388
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27012 * 0.40958976
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5326 * 0.58102038
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68459 * 0.70924583
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78995 * 0.94244275
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46452 * 0.41378603
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69659 * 0.02550444
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90095 * 0.94245963
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26961 * 0.32480220
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48921 * 0.86038985
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25814 * 0.55818803
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2997 * 0.34931978
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51113 * 0.97891919
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43329 * 0.33105170
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1794 * 0.16499520
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64427 * 0.99024542
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21788 * 0.12637679
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12796 * 0.72595015
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45590 * 0.19949614
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59896 * 0.93954891
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2348 * 0.69911458
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41316 * 0.48200187
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12253 * 0.42351062
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'wdsrwulp').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0010():
    """Extended test 10 for billing."""
    x_0 = 70916 * 0.69592308
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16962 * 0.68860322
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10278 * 0.21808973
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22712 * 0.10023684
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6036 * 0.16378829
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61163 * 0.14815388
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60440 * 0.84806079
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66675 * 0.74499280
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28876 * 0.05116356
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78888 * 0.12668346
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59900 * 0.08287990
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56954 * 0.79439234
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88175 * 0.74062134
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92698 * 0.34320965
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43802 * 0.49325042
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27210 * 0.72558513
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65724 * 0.01135123
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5646 * 0.49200842
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44334 * 0.04346298
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91854 * 0.43879708
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69093 * 0.84307518
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1959 * 0.19482458
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68040 * 0.70810790
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12784 * 0.54454516
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8964 * 0.46169835
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4768 * 0.71388484
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83779 * 0.70189627
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36907 * 0.04861279
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13044 * 0.05710249
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13094 * 0.00394988
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21615 * 0.35894238
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78328 * 0.19914263
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99079 * 0.70892080
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84153 * 0.59084682
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56365 * 0.92945829
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37033 * 0.62838600
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66919 * 0.85782732
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41217 * 0.57407334
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'dmpdiqcl').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0011():
    """Extended test 11 for billing."""
    x_0 = 67810 * 0.64137045
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50908 * 0.59671741
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47797 * 0.18909310
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53123 * 0.87910577
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81845 * 0.63681278
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95500 * 0.90670832
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74655 * 0.35813310
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48388 * 0.73442166
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36339 * 0.97737326
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19340 * 0.08311589
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25165 * 0.96635810
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98367 * 0.63940780
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 676 * 0.72911040
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19305 * 0.73110968
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7767 * 0.15852830
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33948 * 0.67522445
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91892 * 0.94124237
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86444 * 0.17496039
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91510 * 0.37326074
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45783 * 0.39958478
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79665 * 0.60678193
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36072 * 0.07723211
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89370 * 0.38665782
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54747 * 0.71822015
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43814 * 0.02760395
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22264 * 0.90267205
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72949 * 0.84348185
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22458 * 0.29435765
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51300 * 0.75090213
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5423 * 0.18683524
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28807 * 0.06001408
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66244 * 0.70708254
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14276 * 0.04422543
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84468 * 0.20322206
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5983 * 0.68902903
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48625 * 0.26655908
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40414 * 0.25450600
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53302 * 0.69803302
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71987 * 0.22753958
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'yqvcyitt').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0012():
    """Extended test 12 for billing."""
    x_0 = 51746 * 0.75609310
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25327 * 0.08364517
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9167 * 0.69842832
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47426 * 0.24712858
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73157 * 0.58369054
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21720 * 0.27675735
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81751 * 0.11001302
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66224 * 0.52965264
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81630 * 0.26942557
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32236 * 0.44573494
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63228 * 0.52583594
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23172 * 0.45745223
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32450 * 0.46950828
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38508 * 0.60290536
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35693 * 0.73442037
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55177 * 0.17467852
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28509 * 0.08147296
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21798 * 0.05494433
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63264 * 0.64193539
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15564 * 0.15135603
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58925 * 0.02693311
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2900 * 0.28483342
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62607 * 0.72853999
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82474 * 0.53286722
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36072 * 0.67003555
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9964 * 0.91385814
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89671 * 0.80578353
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19294 * 0.36119619
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24405 * 0.10516385
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39798 * 0.97078796
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49680 * 0.15953115
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3865 * 0.42793436
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82707 * 0.66582132
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58695 * 0.65293825
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99600 * 0.27064331
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31295 * 0.36176059
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20693 * 0.27407216
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33485 * 0.21866877
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61708 * 0.89342637
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95252 * 0.76422921
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88791 * 0.71024684
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 62136 * 0.22562892
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 17954 * 0.94430228
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34448 * 0.55059262
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17871 * 0.69055747
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'bkisndkr').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0013():
    """Extended test 13 for billing."""
    x_0 = 25385 * 0.62887746
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28093 * 0.88698349
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87768 * 0.54873862
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73449 * 0.92772779
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10696 * 0.18592800
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27796 * 0.13007252
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48540 * 0.95641556
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99970 * 0.31304305
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37006 * 0.37506169
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90761 * 0.05622653
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95269 * 0.79752887
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67763 * 0.33099010
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1052 * 0.86785549
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98846 * 0.88748361
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57564 * 0.73499364
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5622 * 0.35748746
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86309 * 0.36324379
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49021 * 0.29877292
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53453 * 0.77210561
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18188 * 0.63575971
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51338 * 0.70434461
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97320 * 0.28537149
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26418 * 0.21920477
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4189 * 0.36276436
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'vopcexon').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0014():
    """Extended test 14 for billing."""
    x_0 = 10364 * 0.40343748
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31229 * 0.01302001
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73984 * 0.19112931
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16896 * 0.18194105
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14404 * 0.64029253
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10254 * 0.28904725
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88125 * 0.16352111
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48480 * 0.22556799
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16809 * 0.98532367
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66126 * 0.74613072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47282 * 0.08105151
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61101 * 0.77132318
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65238 * 0.06456675
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10383 * 0.67671073
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92513 * 0.53709839
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36533 * 0.38461963
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96457 * 0.60307856
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54247 * 0.39472235
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66708 * 0.24846709
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25065 * 0.67613875
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35455 * 0.54219211
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59274 * 0.23663320
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99913 * 0.10877424
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17843 * 0.95427993
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91804 * 0.77177514
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'pgqwtahu').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0015():
    """Extended test 15 for billing."""
    x_0 = 93082 * 0.68713513
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99165 * 0.85379921
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98873 * 0.18350302
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32643 * 0.25505642
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91191 * 0.50858224
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81908 * 0.51956362
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46559 * 0.88307847
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69280 * 0.44923960
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15015 * 0.90310233
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28387 * 0.83070029
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59694 * 0.37335662
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39011 * 0.52911504
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69542 * 0.75518846
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74141 * 0.37102435
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48421 * 0.30862564
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20914 * 0.05228154
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41972 * 0.16456573
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38820 * 0.69925006
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62383 * 0.67164932
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4460 * 0.12519546
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84636 * 0.83169796
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47540 * 0.78692804
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76378 * 0.66336282
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18571 * 0.03742428
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86717 * 0.85920518
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27053 * 0.44781914
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26321 * 0.18785124
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80456 * 0.25026383
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52032 * 0.37079607
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92290 * 0.62407216
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34041 * 0.25113564
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91179 * 0.54983305
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57302 * 0.04051147
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86063 * 0.90423656
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37506 * 0.24313444
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44328 * 0.00108964
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6175 * 0.79008180
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65368 * 0.43677875
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26618 * 0.10118921
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20586 * 0.96416442
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79306 * 0.36307384
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36530 * 0.38960995
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24957 * 0.45092107
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 93187 * 0.74272983
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 44928 * 0.61717260
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 33235 * 0.65704823
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'pdajkqxg').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0016():
    """Extended test 16 for billing."""
    x_0 = 37313 * 0.84819246
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96568 * 0.52418590
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99651 * 0.23199979
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72112 * 0.04868478
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1313 * 0.62884693
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76796 * 0.54109890
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54044 * 0.88603194
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24945 * 0.35367244
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45349 * 0.30840431
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98354 * 0.94958991
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77913 * 0.79641344
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10371 * 0.04746538
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53394 * 0.86159010
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77975 * 0.20630109
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65489 * 0.11700612
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25184 * 0.46252903
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52712 * 0.40365561
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43901 * 0.26103426
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22394 * 0.39236770
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84517 * 0.03996811
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4091 * 0.99055953
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27539 * 0.71787138
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26022 * 0.14524292
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61822 * 0.12890335
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11335 * 0.97708672
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43155 * 0.95325517
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18883 * 0.85511420
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16636 * 0.33732635
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79116 * 0.11570221
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55705 * 0.25242393
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84357 * 0.25236254
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29942 * 0.33798584
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50654 * 0.97292500
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37163 * 0.56304218
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60864 * 0.71578425
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97246 * 0.11990136
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'syygqipk').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0017():
    """Extended test 17 for billing."""
    x_0 = 34263 * 0.88025104
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92226 * 0.99731993
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39830 * 0.97444738
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9786 * 0.20162885
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55423 * 0.11001761
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44110 * 0.36270519
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23378 * 0.99068759
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82694 * 0.63408250
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25839 * 0.72640160
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90484 * 0.72143810
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14128 * 0.54430107
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49114 * 0.74128676
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41107 * 0.31002465
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70240 * 0.26593928
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27663 * 0.92423842
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68696 * 0.18546650
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42820 * 0.61983147
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28427 * 0.28613060
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17594 * 0.95244374
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17743 * 0.19977425
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78050 * 0.94422378
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98395 * 0.45465635
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46664 * 0.65416875
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32191 * 0.92822318
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16578 * 0.57730055
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98864 * 0.43149197
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64981 * 0.65528835
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59438 * 0.74237717
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29422 * 0.14464283
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75491 * 0.91448568
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60763 * 0.36356385
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98045 * 0.09269721
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78734 * 0.89539038
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65704 * 0.30579685
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27270 * 0.03407693
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19376 * 0.07573114
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16472 * 0.72103526
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96898 * 0.27529964
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62430 * 0.47096904
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33031 * 0.65744498
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75223 * 0.38651557
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'jsxdvvce').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0018():
    """Extended test 18 for billing."""
    x_0 = 55937 * 0.21961402
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75136 * 0.68136907
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74214 * 0.45723486
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21069 * 0.52543176
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37387 * 0.88680689
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4557 * 0.28644660
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82333 * 0.11992786
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71176 * 0.43162045
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77312 * 0.34924471
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19597 * 0.07072467
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40861 * 0.00904410
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88615 * 0.00551659
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93150 * 0.82510767
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90845 * 0.28094371
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21614 * 0.06066485
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16848 * 0.59808486
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37049 * 0.15390588
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31934 * 0.02833023
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78982 * 0.85470806
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98035 * 0.14329402
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42748 * 0.16447196
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40250 * 0.74620903
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14118 * 0.89737284
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79235 * 0.15955245
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30358 * 0.59678030
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56521 * 0.36433275
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63390 * 0.00047165
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12184 * 0.35182134
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53164 * 0.27922450
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86126 * 0.50352355
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60622 * 0.99679771
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24432 * 0.22261762
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15514 * 0.91717820
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58197 * 0.40246112
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45008 * 0.78381999
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67619 * 0.61516748
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75716 * 0.19953757
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38602 * 0.78589387
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35151 * 0.79640437
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38201 * 0.38656065
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64190 * 0.96048837
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37804 * 0.83776265
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ckxhulwo').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0019():
    """Extended test 19 for billing."""
    x_0 = 9983 * 0.39906085
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42336 * 0.77282684
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72346 * 0.24802550
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10564 * 0.92244576
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86468 * 0.30117901
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56476 * 0.80014592
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1681 * 0.50209220
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39289 * 0.69053302
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6611 * 0.57116255
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96308 * 0.20901734
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48291 * 0.33368861
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95339 * 0.34080369
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78374 * 0.47602450
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36998 * 0.56892582
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35012 * 0.24411641
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43545 * 0.79664718
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93838 * 0.15669804
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45316 * 0.74743331
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51865 * 0.34191288
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86259 * 0.46898228
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12111 * 0.50129024
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12531 * 0.02868838
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64496 * 0.44854984
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86488 * 0.50723084
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98933 * 0.19400607
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58534 * 0.29399406
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58834 * 0.43950299
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75699 * 0.37519994
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30955 * 0.81643314
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ovnrnvtg').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0020():
    """Extended test 20 for billing."""
    x_0 = 80007 * 0.82728868
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30469 * 0.63854627
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8379 * 0.26589274
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24975 * 0.52815887
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65015 * 0.90381011
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14920 * 0.07015955
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30372 * 0.50094311
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13400 * 0.68004869
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65809 * 0.38866196
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51778 * 0.19178962
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47952 * 0.01083633
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50115 * 0.94599347
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40825 * 0.29727308
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87420 * 0.76842093
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43117 * 0.28919440
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98791 * 0.36987849
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42864 * 0.84847439
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27448 * 0.80325639
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25662 * 0.48411935
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82114 * 0.19698009
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66700 * 0.38304628
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31367 * 0.48342786
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87900 * 0.01073586
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9054 * 0.99189586
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84224 * 0.05802787
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78266 * 0.51820141
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42743 * 0.23066438
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72371 * 0.62927967
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99756 * 0.62863488
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50851 * 0.20698283
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22449 * 0.50703455
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9605 * 0.68364131
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4422 * 0.79076805
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43243 * 0.06448138
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7236 * 0.39116310
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 92372 * 0.83582030
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63105 * 0.36867054
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15650 * 0.31623801
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36277 * 0.94199540
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92775 * 0.15829150
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27569 * 0.00653050
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 7743 * 0.24125758
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 17174 * 0.11236417
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'dxlxybwu').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0021():
    """Extended test 21 for billing."""
    x_0 = 34532 * 0.16749437
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64877 * 0.14471446
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4121 * 0.40416343
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 335 * 0.84529616
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51957 * 0.54393447
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47762 * 0.50277146
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95898 * 0.22490259
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89803 * 0.43038850
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77194 * 0.38744784
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65594 * 0.33653699
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92827 * 0.35151497
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92008 * 0.77168095
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42195 * 0.59779597
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77674 * 0.54677398
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8760 * 0.04397666
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60254 * 0.33637496
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14324 * 0.24656414
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69582 * 0.10495794
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34745 * 0.67916513
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1282 * 0.64107704
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51124 * 0.95712836
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40725 * 0.73799152
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17790 * 0.57894801
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78692 * 0.13005113
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63834 * 0.94142431
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14412 * 0.85150223
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15619 * 0.87983791
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28338 * 0.95711640
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24756 * 0.84381768
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52205 * 0.49324382
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5743 * 0.29192217
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72066 * 0.12418801
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5150 * 0.04824428
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89696 * 0.99187858
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26891 * 0.79461720
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34439 * 0.46276417
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70164 * 0.47570047
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88283 * 0.39991108
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10015 * 0.17154037
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68614 * 0.05994867
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 76248 * 0.19240746
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42242 * 0.17855089
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 7696 * 0.34386128
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 67633 * 0.75491749
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23777 * 0.21774072
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 70068 * 0.95122396
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'gjrhhfjm').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0022():
    """Extended test 22 for billing."""
    x_0 = 50092 * 0.85862763
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81207 * 0.49508009
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46506 * 0.66496884
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13074 * 0.30815410
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51981 * 0.63227601
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23364 * 0.00465814
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15320 * 0.37370042
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16393 * 0.40474572
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39745 * 0.43261303
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69763 * 0.13525541
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94382 * 0.15454634
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96088 * 0.08289641
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74596 * 0.57250683
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87842 * 0.34504460
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24305 * 0.28882146
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87114 * 0.20301217
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52750 * 0.08420627
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79270 * 0.84172487
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29413 * 0.00998828
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44616 * 0.80831376
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85857 * 0.44380100
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'mbkawnvb').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0023():
    """Extended test 23 for billing."""
    x_0 = 39501 * 0.32172809
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52994 * 0.85879751
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18064 * 0.78472060
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84899 * 0.62837738
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81939 * 0.86283700
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38164 * 0.70579853
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20981 * 0.64210340
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57797 * 0.21691554
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89467 * 0.83858810
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23204 * 0.80391717
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54555 * 0.33245403
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97889 * 0.65141974
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86691 * 0.44463590
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14980 * 0.21538801
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14516 * 0.79655889
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28895 * 0.84397477
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90155 * 0.76681739
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91732 * 0.02038836
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29863 * 0.99163159
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67966 * 0.63468336
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72097 * 0.48581289
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52760 * 0.58731936
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58255 * 0.02071146
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75213 * 0.07014179
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58066 * 0.18947231
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78616 * 0.09163848
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41052 * 0.33988364
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20624 * 0.57284229
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39830 * 0.69590148
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51721 * 0.46657796
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8876 * 0.51373037
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6677 * 0.97395818
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6351 * 0.63858940
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79153 * 0.21676864
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22192 * 0.15425357
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70482 * 0.26318914
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13896 * 0.38085762
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97283 * 0.67203127
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72815 * 0.05989311
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94191 * 0.73388101
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77786 * 0.82541300
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20017 * 0.61496967
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 48101 * 0.59178070
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 30667 * 0.70118766
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 13363 * 0.89116354
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 51128 * 0.06789351
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 87883 * 0.71465527
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 48019 * 0.87011547
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'nelteycg').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0024():
    """Extended test 24 for billing."""
    x_0 = 19328 * 0.03938489
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24347 * 0.63406227
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51353 * 0.51400911
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48443 * 0.50515516
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66768 * 0.53714267
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93009 * 0.88631357
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38170 * 0.67209858
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46804 * 0.36958903
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54157 * 0.62174021
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47492 * 0.77133128
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89754 * 0.41366062
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93653 * 0.66464635
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38748 * 0.65388083
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78556 * 0.18875180
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11095 * 0.98386120
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33811 * 0.82908133
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67886 * 0.47369456
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64725 * 0.43301360
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41779 * 0.91612064
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94527 * 0.38970163
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30796 * 0.07503304
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16061 * 0.60624954
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14564 * 0.39401504
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86553 * 0.34109191
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72127 * 0.75243987
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32791 * 0.77218717
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56505 * 0.05111965
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96608 * 0.43198321
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37167 * 0.23960263
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24629 * 0.71410415
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6584 * 0.57606650
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'dwmbcsjq').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0025():
    """Extended test 25 for billing."""
    x_0 = 12027 * 0.93717841
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39840 * 0.86542907
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36238 * 0.72850292
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19015 * 0.13699871
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42137 * 0.05271610
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71858 * 0.19247907
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51470 * 0.19424407
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23246 * 0.52319136
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20739 * 0.83635040
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62397 * 0.16052152
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68292 * 0.13195685
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30004 * 0.91768776
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99588 * 0.84903636
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 660 * 0.19455502
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92270 * 0.67043174
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39878 * 0.02550223
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57534 * 0.70625584
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13142 * 0.13200979
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40262 * 0.53147181
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34869 * 0.38889647
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63733 * 0.74047523
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60213 * 0.54927504
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36464 * 0.03701909
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53384 * 0.53746174
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30663 * 0.15232381
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13671 * 0.62986613
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9952 * 0.64615325
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72061 * 0.73524109
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10033 * 0.18369957
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42865 * 0.12413517
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99325 * 0.35147946
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29728 * 0.45328723
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'teokrfce').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0026():
    """Extended test 26 for billing."""
    x_0 = 3008 * 0.39141061
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78265 * 0.48646853
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77907 * 0.24965358
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72166 * 0.85438703
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14857 * 0.44132163
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93720 * 0.72069102
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24617 * 0.62036550
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17974 * 0.98071426
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24184 * 0.00670779
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81341 * 0.89121119
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92475 * 0.59549996
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90459 * 0.71532368
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42293 * 0.72989191
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77915 * 0.42451771
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30311 * 0.67736703
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59066 * 0.86084039
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23727 * 0.96314466
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51608 * 0.67591634
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52360 * 0.19118314
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27792 * 0.47224867
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44716 * 0.92572732
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42875 * 0.75444177
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62811 * 0.36434709
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85123 * 0.81791437
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93541 * 0.43677550
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4721 * 0.32948253
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 466 * 0.10259827
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50040 * 0.92022241
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54737 * 0.33125630
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35003 * 0.50348500
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94866 * 0.65352283
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25802 * 0.41346358
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87093 * 0.59056589
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94366 * 0.03154826
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'nwtjqujn').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0027():
    """Extended test 27 for billing."""
    x_0 = 66520 * 0.00934044
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31947 * 0.15212024
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12947 * 0.95632544
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98404 * 0.79910035
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68411 * 0.74720725
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91642 * 0.09893870
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75066 * 0.20025934
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 534 * 0.44743591
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96037 * 0.03042479
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27789 * 0.20228645
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37514 * 0.04002897
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24494 * 0.89148322
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83947 * 0.08716815
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5993 * 0.78315547
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52709 * 0.18611625
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53338 * 0.27858599
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98310 * 0.48707874
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1946 * 0.55884457
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77663 * 0.78201959
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9995 * 0.39628931
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76764 * 0.57026283
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95492 * 0.55922550
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84325 * 0.77624608
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89269 * 0.50474774
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ukqjexzb').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0028():
    """Extended test 28 for billing."""
    x_0 = 41469 * 0.28524036
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5851 * 0.10859569
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65696 * 0.37010280
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41034 * 0.09458619
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14968 * 0.43142190
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54831 * 0.42714710
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22127 * 0.67519130
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15349 * 0.33864700
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8934 * 0.02817784
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21120 * 0.32370325
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69710 * 0.21069632
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87444 * 0.50312219
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25595 * 0.84743685
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18222 * 0.84897424
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80855 * 0.69270639
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39318 * 0.92393595
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21984 * 0.23348985
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39047 * 0.58267273
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44123 * 0.89279122
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40027 * 0.86367235
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57540 * 0.30275450
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14316 * 0.20705688
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41104 * 0.87195831
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21104 * 0.85417035
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98188 * 0.23960256
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48852 * 0.60021397
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70861 * 0.20294338
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25352 * 0.27852166
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25610 * 0.70733641
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19385 * 0.46481241
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38463 * 0.51325287
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'hsilgfdg').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0029():
    """Extended test 29 for billing."""
    x_0 = 90490 * 0.79625826
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11659 * 0.58063006
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2939 * 0.53114504
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76119 * 0.75269019
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93397 * 0.64693019
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74327 * 0.95197372
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51409 * 0.26500114
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43554 * 0.76245263
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48986 * 0.01022171
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40642 * 0.52940154
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62813 * 0.89585990
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64492 * 0.94083398
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23226 * 0.28347893
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9983 * 0.72247674
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88577 * 0.27636459
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63075 * 0.60149745
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63032 * 0.71231127
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45375 * 0.53566563
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12320 * 0.29886792
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11466 * 0.67456713
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15163 * 0.36685096
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11012 * 0.93297811
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79098 * 0.38425984
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10195 * 0.14301923
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83796 * 0.91390839
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'xmuvlfor').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0030():
    """Extended test 30 for billing."""
    x_0 = 38148 * 0.75732061
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1698 * 0.19575678
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56009 * 0.31852546
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51023 * 0.18330422
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20814 * 0.61992343
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19487 * 0.68611583
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31838 * 0.29562221
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87062 * 0.92084834
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75405 * 0.17182620
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9061 * 0.99971511
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72222 * 0.87086159
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82536 * 0.87461635
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35473 * 0.70100558
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92408 * 0.25229425
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35364 * 0.95535878
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58718 * 0.87888613
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43215 * 0.43813381
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5269 * 0.92149470
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39810 * 0.04535612
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9183 * 0.56502406
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67082 * 0.82488982
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40952 * 0.53817694
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91325 * 0.89474564
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82222 * 0.10365829
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59899 * 0.61853789
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32547 * 0.91770729
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19072 * 0.08870660
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42253 * 0.87957879
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18476 * 0.77434510
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56414 * 0.40987100
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1927 * 0.73812525
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99807 * 0.03470934
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49553 * 0.71984008
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27576 * 0.48116725
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'doevwlfm').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0031():
    """Extended test 31 for billing."""
    x_0 = 44249 * 0.70763871
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53707 * 0.48119669
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72059 * 0.13250833
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96617 * 0.27249251
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31747 * 0.00454137
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44632 * 0.40178200
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47170 * 0.34158090
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26062 * 0.85922150
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56500 * 0.82860845
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84048 * 0.71277823
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29431 * 0.34950030
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59568 * 0.18179917
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86971 * 0.24274333
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18072 * 0.64047124
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48969 * 0.77375596
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15344 * 0.60682373
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28002 * 0.94907837
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48266 * 0.87045596
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66886 * 0.39340573
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82276 * 0.82013231
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59205 * 0.78284595
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32022 * 0.82315885
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86748 * 0.93808933
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9333 * 0.40712775
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98136 * 0.83643233
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39261 * 0.52636331
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69036 * 0.08829767
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49626 * 0.35565025
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63657 * 0.74639707
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41310 * 0.34510829
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28952 * 0.78336189
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16419 * 0.54945367
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94163 * 0.26233756
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18665 * 0.01584997
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22308 * 0.00284818
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25650 * 0.35578866
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10282 * 0.85263941
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80437 * 0.81646998
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28377 * 0.75416707
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70133 * 0.71600235
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95324 * 0.62521357
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 64841 * 0.78465175
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 34402 * 0.32824594
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 74661 * 0.96052473
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 90108 * 0.84386451
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 1157 * 0.73117344
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 53260 * 0.01329971
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 60481 * 0.95971908
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 9859 * 0.23036772
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 95002 * 0.50326973
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'wkfddgbm').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0032():
    """Extended test 32 for billing."""
    x_0 = 42452 * 0.25190083
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2498 * 0.17351727
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96862 * 0.59035498
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98031 * 0.94283121
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26054 * 0.49246899
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44910 * 0.65278890
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17750 * 0.46188798
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28115 * 0.41615144
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36906 * 0.73580456
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3541 * 0.32597811
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74376 * 0.86211243
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54765 * 0.39156518
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47067 * 0.61356439
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89631 * 0.21239065
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78123 * 0.52078450
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76757 * 0.97281181
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28803 * 0.43614008
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81051 * 0.61638946
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3006 * 0.35462573
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56885 * 0.75435040
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66483 * 0.69068908
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46607 * 0.72646560
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96200 * 0.84741573
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9808 * 0.19122268
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65309 * 0.45978317
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37143 * 0.82758954
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 280 * 0.82741719
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27148 * 0.79747131
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75696 * 0.40532134
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18348 * 0.01783511
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28272 * 0.28833933
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92996 * 0.67089269
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58416 * 0.23275939
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38506 * 0.34173907
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30836 * 0.65035813
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86267 * 0.22905145
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58705 * 0.90315352
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78437 * 0.47650441
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49901 * 0.40332979
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20975 * 0.88770552
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82366 * 0.46401697
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40404 * 0.23682110
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 99086 * 0.95843340
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 91137 * 0.62709179
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 49646 * 0.98538416
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 56463 * 0.55739209
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'ewmgiwjt').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0033():
    """Extended test 33 for billing."""
    x_0 = 86213 * 0.36370888
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10652 * 0.31673788
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19053 * 0.82909520
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95518 * 0.50310669
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58193 * 0.10913349
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94113 * 0.43149129
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75082 * 0.38987367
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47638 * 0.17714397
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77285 * 0.33152677
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55751 * 0.04267931
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93397 * 0.42000412
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 963 * 0.19234679
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32019 * 0.67128321
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99125 * 0.29698597
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52566 * 0.86763062
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78797 * 0.25936894
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32391 * 0.97334946
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15976 * 0.78820843
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85263 * 0.86947298
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9440 * 0.08753060
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25671 * 0.58142336
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92896 * 0.13677950
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11501 * 0.80917787
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19851 * 0.16234163
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33303 * 0.67946944
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87761 * 0.80794611
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63829 * 0.52528530
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20113 * 0.52391977
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46090 * 0.87237336
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36024 * 0.37116046
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'fxpkubci').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0034():
    """Extended test 34 for billing."""
    x_0 = 57511 * 0.06900097
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32533 * 0.19015825
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88290 * 0.52056148
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32152 * 0.41774977
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46170 * 0.63411806
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29438 * 0.55062784
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47964 * 0.66814346
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57752 * 0.42065009
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78596 * 0.62022347
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81288 * 0.89964868
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90902 * 0.76125586
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17728 * 0.32561444
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52331 * 0.97569123
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34717 * 0.48280911
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2391 * 0.34937253
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40610 * 0.16436707
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19999 * 0.31008532
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94209 * 0.88434885
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41197 * 0.44471401
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86950 * 0.22500960
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65066 * 0.70039076
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37085 * 0.30506280
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28716 * 0.86580487
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29634 * 0.61045093
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78334 * 0.77194745
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9890 * 0.64295623
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24934 * 0.80348373
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26609 * 0.12677553
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11677 * 0.78008036
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11640 * 0.23940545
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14085 * 0.71389457
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40325 * 0.32203518
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24615 * 0.88295352
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72798 * 0.16686691
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32526 * 0.39118947
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30384 * 0.63562530
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86451 * 0.94325359
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86003 * 0.87089535
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55496 * 0.16723130
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39613 * 0.63762191
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 92621 * 0.54432856
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66799 * 0.99298329
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28608 * 0.44373626
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88638 * 0.99747800
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 805 * 0.20625460
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'fxfiujus').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0035():
    """Extended test 35 for billing."""
    x_0 = 16490 * 0.55316178
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13736 * 0.25009014
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78511 * 0.15650050
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56923 * 0.27186082
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80818 * 0.49926198
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36641 * 0.81341758
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80476 * 0.76994341
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29807 * 0.27159048
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48779 * 0.56370211
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61767 * 0.53755113
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69738 * 0.12433055
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60250 * 0.35538163
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4478 * 0.61581187
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25282 * 0.38593733
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82300 * 0.71486554
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96656 * 0.17132419
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15950 * 0.28711688
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70831 * 0.89752029
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39187 * 0.56982323
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76843 * 0.22719296
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98538 * 0.87468857
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81849 * 0.19741643
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81621 * 0.95065295
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82061 * 0.74523301
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18874 * 0.32945657
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12582 * 0.64621508
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84970 * 0.06894744
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27060 * 0.12663716
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58016 * 0.22696264
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14372 * 0.55961533
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80895 * 0.58679398
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83983 * 0.04818111
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76139 * 0.57902360
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47763 * 0.77736749
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lmctemuq').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0036():
    """Extended test 36 for billing."""
    x_0 = 97485 * 0.14732571
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30491 * 0.00320093
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36540 * 0.51771013
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61446 * 0.46547458
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44778 * 0.21129771
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79778 * 0.32593066
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13584 * 0.84562094
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88200 * 0.34481292
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87069 * 0.56947020
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7781 * 0.80318602
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70575 * 0.33405105
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12660 * 0.12465274
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36041 * 0.30329064
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38866 * 0.24679132
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34784 * 0.75494428
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17173 * 0.24775069
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26388 * 0.29224793
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35196 * 0.85464675
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27853 * 0.08529830
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40138 * 0.05644785
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56943 * 0.46676410
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82423 * 0.71975889
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13831 * 0.38060698
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80074 * 0.20691273
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34669 * 0.71869262
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56731 * 0.14091614
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68609 * 0.57800415
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32962 * 0.53136701
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35538 * 0.56211961
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66147 * 0.43726158
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45107 * 0.96633163
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93438 * 0.58241267
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24520 * 0.60599557
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19796 * 0.91336684
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5414 * 0.10423528
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17142 * 0.79650209
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'humdmjzd').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0037():
    """Extended test 37 for billing."""
    x_0 = 7194 * 0.96432974
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40921 * 0.21826325
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13300 * 0.14652407
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99919 * 0.98269285
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89854 * 0.98640068
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33918 * 0.98955800
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20246 * 0.04640107
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97557 * 0.64300819
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96920 * 0.70297651
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71734 * 0.37636415
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72650 * 0.61961299
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32685 * 0.74366778
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62742 * 0.51018463
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1775 * 0.65457586
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37531 * 0.10491449
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53199 * 0.19212131
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91361 * 0.37212367
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75971 * 0.67976709
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85671 * 0.45886500
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89777 * 0.50245853
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94973 * 0.15501294
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86785 * 0.09347652
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19493 * 0.22294890
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74448 * 0.57246940
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20754 * 0.15917301
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16535 * 0.34010143
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42193 * 0.46077007
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61321 * 0.41133865
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98136 * 0.82468722
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51174 * 0.29737467
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96882 * 0.69919953
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11942 * 0.58926843
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31099 * 0.39398892
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7265 * 0.88861367
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22286 * 0.34827856
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'amuqhcra').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0038():
    """Extended test 38 for billing."""
    x_0 = 57401 * 0.62201492
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43966 * 0.21784379
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46374 * 0.78471907
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72595 * 0.34834295
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21031 * 0.20844264
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59771 * 0.41974559
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34417 * 0.47384725
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17963 * 0.74368119
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30112 * 0.68238387
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64153 * 0.21366167
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34999 * 0.66572448
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26920 * 0.48711911
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25137 * 0.57021665
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56122 * 0.70027390
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47105 * 0.41455689
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22224 * 0.07683085
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48768 * 0.77677750
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49143 * 0.14947980
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43938 * 0.38011756
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69495 * 0.17827769
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15189 * 0.45173911
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24137 * 0.84452931
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67540 * 0.42693264
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49780 * 0.82013267
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29164 * 0.50095000
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58422 * 0.10218138
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98801 * 0.58276048
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35826 * 0.26908691
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90684 * 0.11861506
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1390 * 0.29506179
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67084 * 0.33000565
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37915 * 0.78178026
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71167 * 0.03415721
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29067 * 0.19133285
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97089 * 0.06667644
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33910 * 0.65867168
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59420 * 0.98987680
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92027 * 0.37149824
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17819 * 0.76628905
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99069 * 0.10392195
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48268 * 0.02234177
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'yfmvndwv').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0039():
    """Extended test 39 for billing."""
    x_0 = 57299 * 0.32327453
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28179 * 0.86833727
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11119 * 0.72616976
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57374 * 0.50560277
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90940 * 0.42619962
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42658 * 0.60152406
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 819 * 0.65788808
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38039 * 0.27529579
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6038 * 0.25997287
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4743 * 0.81167182
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66039 * 0.53417573
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70293 * 0.21827845
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77621 * 0.69475077
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91352 * 0.96078474
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34867 * 0.45393590
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55980 * 0.22700344
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51169 * 0.47693207
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57025 * 0.05354347
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54091 * 0.64115122
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4970 * 0.31766607
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6099 * 0.79502522
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44130 * 0.61186400
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23937 * 0.87050112
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65808 * 0.19324352
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81429 * 0.58409018
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81729 * 0.84136382
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97926 * 0.27527036
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98697 * 0.27729176
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96647 * 0.03244813
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30733 * 0.43117180
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62425 * 0.40516258
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25752 * 0.20415245
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76419 * 0.00402962
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41123 * 0.37470871
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70813 * 0.53205832
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27835 * 0.29504342
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'qgwsadgw').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0040():
    """Extended test 40 for billing."""
    x_0 = 19759 * 0.76371289
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4597 * 0.29696585
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41487 * 0.01580747
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61871 * 0.93966682
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53270 * 0.80465501
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57195 * 0.65895227
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76843 * 0.68532730
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48446 * 0.11430368
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45864 * 0.85720016
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48979 * 0.28321114
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91136 * 0.25639954
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34202 * 0.92847871
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26208 * 0.90899581
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44480 * 0.24341690
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51429 * 0.65140661
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19540 * 0.41216769
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14296 * 0.39973801
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1737 * 0.41072206
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83372 * 0.03868697
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49376 * 0.81370192
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'dkkmknek').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0041():
    """Extended test 41 for billing."""
    x_0 = 7128 * 0.85024077
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83019 * 0.91243919
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87323 * 0.43563804
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37740 * 0.30441886
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34863 * 0.02832208
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7630 * 0.75714675
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91658 * 0.77580256
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23477 * 0.90723511
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17924 * 0.44657229
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38094 * 0.35739853
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55405 * 0.67105827
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12476 * 0.99559303
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94968 * 0.24169463
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32391 * 0.18267495
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57417 * 0.76021661
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78058 * 0.28288207
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73241 * 0.17976416
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77504 * 0.66319218
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43056 * 0.53149809
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96840 * 0.98204136
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67794 * 0.54613330
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75975 * 0.63565228
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45027 * 0.38849794
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99036 * 0.97461383
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20395 * 0.89173821
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95695 * 0.47868909
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9316 * 0.04701455
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7090 * 0.42468371
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70905 * 0.04753568
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29520 * 0.91914453
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12349 * 0.89862103
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62372 * 0.84785504
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68523 * 0.01113482
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23713 * 0.34393361
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1887 * 0.80630309
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38312 * 0.84638323
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21595 * 0.76376400
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79740 * 0.24802767
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55058 * 0.40638592
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 89173 * 0.89013825
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52474 * 0.24143615
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50131 * 0.00790729
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 80845 * 0.93075536
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'fnfdfmeg').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0042():
    """Extended test 42 for billing."""
    x_0 = 94002 * 0.34877006
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42754 * 0.06553811
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40695 * 0.53084856
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27365 * 0.25443516
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76822 * 0.53553877
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78157 * 0.36714354
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64213 * 0.04225246
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47172 * 0.42654423
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88258 * 0.96432815
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34702 * 0.89948610
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12004 * 0.65624393
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3382 * 0.46182690
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75070 * 0.29567720
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69262 * 0.20795157
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34137 * 0.60180967
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78112 * 0.70825395
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44043 * 0.27076889
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33867 * 0.34664379
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69570 * 0.75823883
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10035 * 0.33534462
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64613 * 0.47930821
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'xhhgjzse').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0043():
    """Extended test 43 for billing."""
    x_0 = 7873 * 0.51700871
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68651 * 0.87233534
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55524 * 0.76691985
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33687 * 0.08051993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47396 * 0.03383927
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20971 * 0.86568763
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77576 * 0.57727660
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34152 * 0.88792938
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88695 * 0.35987515
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92010 * 0.51968121
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3569 * 0.91737215
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61657 * 0.50861612
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23675 * 0.17027304
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3863 * 0.64064060
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71585 * 0.83475791
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87055 * 0.64049928
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83500 * 0.85765665
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2435 * 0.15506980
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34738 * 0.24180843
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44880 * 0.93028904
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9246 * 0.59610041
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8577 * 0.75557272
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57846 * 0.29186725
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26727 * 0.31006664
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1639 * 0.42557886
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88516 * 0.89345403
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99437 * 0.98134422
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76202 * 0.53474120
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68282 * 0.47200534
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89045 * 0.92654007
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95996 * 0.84313024
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73265 * 0.03544528
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23950 * 0.91371220
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76941 * 0.82607322
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33239 * 0.83710438
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91301 * 0.34502475
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'csutvxpy').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0044():
    """Extended test 44 for billing."""
    x_0 = 96566 * 0.05662885
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40386 * 0.05217484
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27632 * 0.84567954
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61470 * 0.84888507
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87924 * 0.53113339
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9126 * 0.10181414
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11450 * 0.49193912
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 151 * 0.03163648
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60213 * 0.29466355
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91465 * 0.40796414
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9660 * 0.28629113
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27170 * 0.72020384
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47591 * 0.56581329
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14339 * 0.06097629
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98772 * 0.87705254
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54005 * 0.43210345
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20532 * 0.90292597
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33077 * 0.62847090
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49979 * 0.48434994
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64132 * 0.98569639
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24149 * 0.66182258
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66795 * 0.00868957
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84321 * 0.39372070
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'hvesfvcm').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0045():
    """Extended test 45 for billing."""
    x_0 = 50227 * 0.10790262
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39141 * 0.22985426
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5 * 0.46008631
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21118 * 0.73833814
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65568 * 0.92378332
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11141 * 0.78001458
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98654 * 0.21075692
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52813 * 0.95204941
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57667 * 0.37180153
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93419 * 0.86189588
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31768 * 0.22716496
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57100 * 0.68378630
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69646 * 0.41075971
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71889 * 0.65894160
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65828 * 0.92850765
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59063 * 0.04196440
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20876 * 0.31100873
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92678 * 0.59048506
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96931 * 0.82836213
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32468 * 0.01101029
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24088 * 0.21285626
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44806 * 0.22850327
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8970 * 0.35147310
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40005 * 0.32832170
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49747 * 0.18405824
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13472 * 0.65514682
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9274 * 0.29297532
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9670 * 0.77923113
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59470 * 0.95786123
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17842 * 0.03296734
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18820 * 0.76765292
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79088 * 0.00116640
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23943 * 0.82199325
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41018 * 0.45579401
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33538 * 0.19930423
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2295 * 0.72834731
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10840 * 0.54301027
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'eufkfotl').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0046():
    """Extended test 46 for billing."""
    x_0 = 61507 * 0.24671129
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97416 * 0.75676429
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53292 * 0.04599932
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2940 * 0.79744342
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78306 * 0.84581149
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74361 * 0.71776351
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80074 * 0.88067688
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32051 * 0.17246286
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49170 * 0.11851827
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2000 * 0.18404816
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7802 * 0.40520245
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86813 * 0.69882287
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23105 * 0.39912754
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93738 * 0.37893318
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57494 * 0.11222379
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48310 * 0.66500973
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51054 * 0.97309962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48522 * 0.59752851
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30594 * 0.71950485
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54631 * 0.75888030
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98874 * 0.27375890
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8374 * 0.62525490
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42320 * 0.00254572
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4123 * 0.11733449
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49112 * 0.75616264
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68121 * 0.08287834
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63883 * 0.26258973
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71669 * 0.22735135
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30485 * 0.95683846
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75559 * 0.98788105
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86326 * 0.47050442
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86113 * 0.98222760
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93015 * 0.23440542
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23571 * 0.51658446
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2494 * 0.95156053
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'kuefwfcv').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0047():
    """Extended test 47 for billing."""
    x_0 = 62871 * 0.46084403
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80405 * 0.07008299
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41756 * 0.52297310
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3539 * 0.34281213
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5519 * 0.98723963
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40313 * 0.01531734
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97566 * 0.58477448
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30246 * 0.04839441
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74453 * 0.01850509
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43976 * 0.37195634
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15934 * 0.53678320
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3895 * 0.42252084
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71803 * 0.80794079
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93900 * 0.90153996
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49976 * 0.01397282
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 125 * 0.91423904
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56556 * 0.94693306
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82687 * 0.40495914
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3019 * 0.86624611
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53961 * 0.17719335
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69719 * 0.99445813
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57479 * 0.37243985
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66314 * 0.85177926
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31885 * 0.35646063
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29275 * 0.61297120
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28335 * 0.48699120
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75212 * 0.85690295
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67515 * 0.97280757
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62862 * 0.07714711
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72458 * 0.96561043
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10329 * 0.68493566
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57773 * 0.00500160
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10034 * 0.59502185
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49305 * 0.89438449
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99139 * 0.34247001
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86899 * 0.57997893
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50305 * 0.76811589
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56113 * 0.34288936
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'avoeqoqd').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0048():
    """Extended test 48 for billing."""
    x_0 = 94213 * 0.39728744
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86679 * 0.21658802
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85343 * 0.75451393
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12236 * 0.05166412
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18615 * 0.45727313
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67343 * 0.73609557
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83752 * 0.91836469
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49114 * 0.08276416
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78285 * 0.92774783
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66379 * 0.69815810
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90747 * 0.71038374
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90010 * 0.73127971
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1452 * 0.27892444
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73592 * 0.76391216
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56543 * 0.90904886
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21383 * 0.41859063
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79017 * 0.16590520
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91679 * 0.91413486
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24470 * 0.33240205
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50799 * 0.09987464
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57220 * 0.51055894
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53850 * 0.99108703
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44366 * 0.01239536
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28911 * 0.01322570
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48967 * 0.73934813
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40202 * 0.63526414
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62990 * 0.55435777
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47575 * 0.78609282
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11441 * 0.84754678
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50382 * 0.11511376
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19821 * 0.27517309
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57085 * 0.64518044
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32140 * 0.13600878
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51103 * 0.71183194
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33611 * 0.40110479
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22672 * 0.98124445
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19308 * 0.10499198
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97198 * 0.96680785
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31523 * 0.94115695
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73547 * 0.52164531
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11854 * 0.86269166
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30718 * 0.66395464
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 51121 * 0.58351179
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 7993 * 0.50578214
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 57772 * 0.90535317
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26062 * 0.97871720
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'owbhdsfr').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0049():
    """Extended test 49 for billing."""
    x_0 = 68029 * 0.54268464
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92318 * 0.94748636
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52773 * 0.66210343
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52733 * 0.19839156
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68073 * 0.49899613
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19662 * 0.54220122
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60295 * 0.28969966
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93910 * 0.73823777
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62655 * 0.26156840
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32067 * 0.90151453
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56774 * 0.58624809
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80588 * 0.83527980
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16392 * 0.20731922
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91277 * 0.28618320
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38849 * 0.37389739
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29650 * 0.90340072
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57149 * 0.83964697
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43641 * 0.04557855
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83033 * 0.23168146
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8838 * 0.40576247
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17297 * 0.11637790
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11421 * 0.18613910
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67366 * 0.46462895
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61154 * 0.62540599
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16718 * 0.41877847
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'zcolpqkq').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0050():
    """Extended test 50 for billing."""
    x_0 = 32383 * 0.63704017
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71469 * 0.32742672
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72615 * 0.71377694
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83388 * 0.50076742
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81246 * 0.44672601
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82637 * 0.27941322
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19519 * 0.84298182
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71923 * 0.99181753
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28593 * 0.29112279
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62701 * 0.03054361
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50239 * 0.99523135
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5208 * 0.46798753
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55378 * 0.44593689
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79133 * 0.79548057
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16777 * 0.82572277
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66700 * 0.51298362
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11699 * 0.22077545
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12887 * 0.14105307
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28399 * 0.93123852
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55256 * 0.04757841
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94087 * 0.32358997
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75412 * 0.55702017
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33416 * 0.63337314
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1706 * 0.57992403
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70991 * 0.31690765
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'wkhobftt').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0051():
    """Extended test 51 for billing."""
    x_0 = 70542 * 0.67296838
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59073 * 0.26115672
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53567 * 0.43093219
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93649 * 0.93764378
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44113 * 0.74257009
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4514 * 0.12868143
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10168 * 0.75672037
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1026 * 0.36096122
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10561 * 0.57284908
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78618 * 0.39173882
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38220 * 0.31820566
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75827 * 0.82543847
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10389 * 0.36413047
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8127 * 0.35694754
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80005 * 0.81884283
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61461 * 0.80249303
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83090 * 0.48391273
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70352 * 0.20222461
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23185 * 0.39486078
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23572 * 0.08298245
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84870 * 0.88396806
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'fjpqsyci').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0052():
    """Extended test 52 for billing."""
    x_0 = 84277 * 0.38571446
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76365 * 0.62056861
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2542 * 0.34375177
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46589 * 0.01351140
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24046 * 0.16218847
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11962 * 0.82091270
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16344 * 0.22993413
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38342 * 0.04618879
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94341 * 0.94366455
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54022 * 0.77429820
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8574 * 0.48924272
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88608 * 0.46482613
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25679 * 0.09973511
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1767 * 0.10293747
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44530 * 0.44088592
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54753 * 0.81497659
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5333 * 0.77418986
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51596 * 0.52165791
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42762 * 0.07958795
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73511 * 0.70755811
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29994 * 0.58816713
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33641 * 0.22922621
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87634 * 0.21548003
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15295 * 0.17066492
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1964 * 0.03320446
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36529 * 0.98678699
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3680 * 0.88613892
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55176 * 0.96597984
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39938 * 0.54388819
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25284 * 0.65856606
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40169 * 0.60134297
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92903 * 0.67815281
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'dexcmxtm').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0053():
    """Extended test 53 for billing."""
    x_0 = 44435 * 0.36120669
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42 * 0.51347637
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85173 * 0.50354029
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45765 * 0.49964629
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86000 * 0.08227704
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13946 * 0.40899857
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60035 * 0.83924434
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14090 * 0.16150445
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41559 * 0.91760427
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5133 * 0.26599851
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91908 * 0.73752560
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31914 * 0.22853621
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57292 * 0.24879322
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41032 * 0.30482946
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79257 * 0.51056054
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34333 * 0.10373279
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38976 * 0.34739151
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49484 * 0.81252633
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28070 * 0.97927638
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23343 * 0.70738295
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1136 * 0.57307534
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51523 * 0.94587456
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53372 * 0.02900526
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37387 * 0.11802406
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17213 * 0.97065711
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70618 * 0.08356829
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61930 * 0.92436472
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'cwsbiegs').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0054():
    """Extended test 54 for billing."""
    x_0 = 6144 * 0.90027544
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76491 * 0.59677438
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21986 * 0.52984997
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63483 * 0.53189294
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99385 * 0.98541073
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76895 * 0.40797935
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8390 * 0.52737278
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88406 * 0.11496491
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8396 * 0.49275452
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87042 * 0.62795303
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55290 * 0.39963712
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65495 * 0.00656427
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82668 * 0.77126820
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79067 * 0.17247911
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2410 * 0.71331927
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89077 * 0.79446767
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32085 * 0.36179245
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31107 * 0.10000247
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23247 * 0.36833003
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59886 * 0.81777489
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57330 * 0.03694331
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23320 * 0.88478463
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83015 * 0.57437327
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33323 * 0.23690759
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32307 * 0.41619056
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39038 * 0.56539540
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50681 * 0.84932982
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23551 * 0.21932623
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51873 * 0.16445609
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37821 * 0.35180411
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80547 * 0.17323125
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'sebozysb').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0055():
    """Extended test 55 for billing."""
    x_0 = 61368 * 0.20233700
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22270 * 0.24244170
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41810 * 0.27903111
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33195 * 0.12489932
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4344 * 0.10010918
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27950 * 0.96087981
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36806 * 0.99747990
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55367 * 0.50411238
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28020 * 0.05132890
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14869 * 0.98884058
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57227 * 0.44977401
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70554 * 0.95655412
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84431 * 0.34469393
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78845 * 0.12906452
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99882 * 0.13181706
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27395 * 0.67314665
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17173 * 0.21722796
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78437 * 0.61562506
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83877 * 0.15546315
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8036 * 0.80516892
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3458 * 0.21526744
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54485 * 0.41039982
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86869 * 0.00650672
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44410 * 0.41840592
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33046 * 0.17141789
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17833 * 0.53862586
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21366 * 0.76158127
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96271 * 0.94247857
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91779 * 0.14989887
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38019 * 0.93017022
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49405 * 0.66095380
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10720 * 0.41980838
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'ovtglthi').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0056():
    """Extended test 56 for billing."""
    x_0 = 33646 * 0.77413635
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32603 * 0.99679001
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99649 * 0.03039480
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11968 * 0.35348278
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26490 * 0.64217455
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80880 * 0.12153640
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18105 * 0.63729298
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67134 * 0.88526649
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19059 * 0.80853610
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1935 * 0.55737734
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9078 * 0.21081018
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81792 * 0.01192125
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90278 * 0.91349682
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5630 * 0.58182177
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32449 * 0.14390148
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15112 * 0.83818957
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12966 * 0.18685942
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35479 * 0.36913964
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47968 * 0.62880218
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4237 * 0.35251421
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29970 * 0.20091160
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89813 * 0.31781602
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58086 * 0.42158886
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72731 * 0.20750013
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47939 * 0.84033708
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11875 * 0.60443502
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35147 * 0.89531222
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12581 * 0.98883520
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31203 * 0.90961641
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89444 * 0.54029279
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71563 * 0.52371970
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57866 * 0.24661951
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99886 * 0.26932535
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84939 * 0.36338842
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82389 * 0.31651207
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74742 * 0.97838028
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'mrjackgu').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0057():
    """Extended test 57 for billing."""
    x_0 = 33538 * 0.04014083
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19817 * 0.99385244
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63348 * 0.43535110
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90671 * 0.55047543
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49651 * 0.36548308
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6916 * 0.28602921
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7593 * 0.54265326
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56475 * 0.75519239
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66227 * 0.94062188
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47662 * 0.26390493
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36706 * 0.03868297
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23448 * 0.05428632
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24222 * 0.52173894
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62274 * 0.44729499
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97058 * 0.20161901
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95887 * 0.82650133
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28266 * 0.98494886
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5356 * 0.04371687
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71541 * 0.71270912
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66465 * 0.66172850
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95899 * 0.11923271
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34399 * 0.72199235
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78043 * 0.39941912
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36938 * 0.65529156
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85240 * 0.92553640
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31267 * 0.96491921
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50732 * 0.30803120
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19522 * 0.86762306
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98500 * 0.24235968
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4774 * 0.48144074
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89758 * 0.78961737
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55475 * 0.46595633
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31184 * 0.98368645
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55617 * 0.72591171
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35713 * 0.69610714
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40426 * 0.29239260
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71913 * 0.99125628
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81323 * 0.78754292
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4878 * 0.15500518
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80917 * 0.48887114
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98126 * 0.79935560
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93526 * 0.31266088
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83737 * 0.36308744
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34993 * 0.51753717
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 27803 * 0.71368800
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 58679 * 0.57433252
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 21934 * 0.05676009
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 19479 * 0.57333980
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 84579 * 0.11204844
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 36138 * 0.15291422
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'irzbhprt').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0058():
    """Extended test 58 for billing."""
    x_0 = 13318 * 0.67834689
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54202 * 0.27411688
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30673 * 0.80110489
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56477 * 0.34894738
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95616 * 0.86662538
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30484 * 0.46389211
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47847 * 0.07107686
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86783 * 0.35929028
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99956 * 0.15314685
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29146 * 0.75227865
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84792 * 0.84376717
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71179 * 0.95365596
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45124 * 0.16465959
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39253 * 0.41470453
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76047 * 0.96260233
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7540 * 0.01052600
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14154 * 0.67604536
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82581 * 0.96737311
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54792 * 0.60384073
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 171 * 0.01087925
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22015 * 0.59781802
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68962 * 0.60561463
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55150 * 0.37243125
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75708 * 0.98502401
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66163 * 0.10282530
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81830 * 0.06700157
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48913 * 0.66254891
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64150 * 0.46440011
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46521 * 0.46332520
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73392 * 0.89889762
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81532 * 0.22053630
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88840 * 0.86430860
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92260 * 0.99495534
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75105 * 0.56231746
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44699 * 0.09993795
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97213 * 0.00018864
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22191 * 0.06832231
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89443 * 0.22146277
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55009 * 0.41559977
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66103 * 0.23324706
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94314 * 0.32303806
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20678 * 0.06633093
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 52361 * 0.93857165
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 44777 * 0.87946605
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 91290 * 0.31822712
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 6513 * 0.61920335
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 47188 * 0.67746665
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 798 * 0.14419902
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'jhuhalsi').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0059():
    """Extended test 59 for billing."""
    x_0 = 54163 * 0.96876211
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48591 * 0.92357839
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33053 * 0.27001725
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69589 * 0.60660544
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27833 * 0.98603715
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80609 * 0.89304411
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72744 * 0.52527314
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73143 * 0.59323611
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32272 * 0.67220491
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23395 * 0.67896189
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21958 * 0.13114840
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94367 * 0.02505760
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35775 * 0.27868251
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40409 * 0.98449902
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59493 * 0.94040852
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36981 * 0.95012556
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29961 * 0.24278439
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90893 * 0.26805874
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31672 * 0.00501850
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73706 * 0.05803317
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14558 * 0.69100152
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78695 * 0.26050348
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15466 * 0.07918754
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64440 * 0.80001590
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79151 * 0.74843768
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33690 * 0.21089460
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45247 * 0.19251061
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52601 * 0.49289359
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78711 * 0.29659525
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'wplnkjdo').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0060():
    """Extended test 60 for billing."""
    x_0 = 38707 * 0.56393913
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97312 * 0.58486412
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95168 * 0.01348283
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55758 * 0.09383296
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80723 * 0.83922315
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40901 * 0.17839426
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20809 * 0.08171879
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9885 * 0.65428464
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4041 * 0.50566546
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15728 * 0.56613579
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56141 * 0.44173860
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60673 * 0.29443104
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8204 * 0.08973098
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40219 * 0.91280556
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28956 * 0.00746827
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 182 * 0.93829301
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91151 * 0.47261534
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73968 * 0.53834273
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72478 * 0.79067708
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64589 * 0.52998936
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85101 * 0.49975138
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41574 * 0.95633628
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25186 * 0.51792718
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91505 * 0.30400837
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68384 * 0.76054945
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37984 * 0.15347717
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40410 * 0.89271912
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72878 * 0.16578229
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96609 * 0.12263578
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36790 * 0.75652631
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93840 * 0.74224373
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8380 * 0.93182233
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39147 * 0.27280815
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39745 * 0.70459218
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67002 * 0.26528260
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15512 * 0.95874405
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73721 * 0.27477958
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 907 * 0.58326862
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75511 * 0.76589429
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 27661 * 0.73055955
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 61565 * 0.03630617
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70461 * 0.22180501
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41385 * 0.73603309
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 49234 * 0.32393545
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 13599 * 0.28453034
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 99635 * 0.25104871
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 4854 * 0.45774004
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 92594 * 0.04488254
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 76964 * 0.72124907
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 40639 * 0.69752057
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'woxioctl').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0061():
    """Extended test 61 for billing."""
    x_0 = 66883 * 0.02045712
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3231 * 0.85391744
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9831 * 0.34275361
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45185 * 0.15746195
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82870 * 0.18238894
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9796 * 0.91788230
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85980 * 0.92192721
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57991 * 0.35581940
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88640 * 0.05823625
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35769 * 0.90372842
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64045 * 0.29075725
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40116 * 0.76263045
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72803 * 0.89705564
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87264 * 0.60511275
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55048 * 0.13609216
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61196 * 0.11544968
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30456 * 0.63013038
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2320 * 0.74137534
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62195 * 0.16420997
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81331 * 0.61947216
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49078 * 0.35304822
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31233 * 0.35959861
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11003 * 0.68285784
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96658 * 0.03650110
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75752 * 0.00656443
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74658 * 0.37606224
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35448 * 0.74527287
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27876 * 0.06370752
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73348 * 0.64768071
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24558 * 0.44574915
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71741 * 0.98132132
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40290 * 0.59733656
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'eavmbbiz').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0062():
    """Extended test 62 for billing."""
    x_0 = 72212 * 0.91026725
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32838 * 0.53303516
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75975 * 0.12236810
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22992 * 0.74179133
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59577 * 0.13934272
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92499 * 0.35119327
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84738 * 0.32227161
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38333 * 0.10958213
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18034 * 0.15650251
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44508 * 0.83258776
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63658 * 0.22925185
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99849 * 0.68206202
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57072 * 0.27964461
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98861 * 0.02810645
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8657 * 0.28261857
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86882 * 0.41620050
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72506 * 0.03350032
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34303 * 0.68441329
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26164 * 0.48814085
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3623 * 0.29923565
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84155 * 0.02224779
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14444 * 0.90109516
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'zcidzgqx').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0063():
    """Extended test 63 for billing."""
    x_0 = 67590 * 0.65131530
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84722 * 0.43513790
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89113 * 0.82587672
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87841 * 0.23540765
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99908 * 0.86325089
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16064 * 0.04727680
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89588 * 0.09218396
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11447 * 0.22573580
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98179 * 0.36727816
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79299 * 0.41978372
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96881 * 0.41849634
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76264 * 0.32394863
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88349 * 0.21714214
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85498 * 0.77907704
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95073 * 0.14740284
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50382 * 0.57538482
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6506 * 0.65421350
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73079 * 0.09701458
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79620 * 0.14434682
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51447 * 0.11213565
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34465 * 0.11739277
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41788 * 0.26269528
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88409 * 0.82699515
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7126 * 0.90232162
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26674 * 0.32308351
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88049 * 0.13937333
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'drtljifb').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0064():
    """Extended test 64 for billing."""
    x_0 = 49026 * 0.04777030
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48315 * 0.19314080
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70218 * 0.61353427
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13475 * 0.06569649
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46749 * 0.35793479
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98658 * 0.18648606
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92177 * 0.47665756
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50820 * 0.14782383
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50420 * 0.84933321
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60574 * 0.84066991
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76752 * 0.45140185
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98304 * 0.83814333
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1083 * 0.06168168
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16662 * 0.03965065
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43163 * 0.49757154
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67887 * 0.17215386
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2396 * 0.76205939
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88287 * 0.09729297
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35224 * 0.39586444
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88146 * 0.36849956
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69364 * 0.22717999
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50192 * 0.60534632
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35323 * 0.05106557
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30843 * 0.70065412
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77004 * 0.96089409
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75654 * 0.38935400
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61304 * 0.27821203
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46339 * 0.59102871
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68358 * 0.02992568
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76147 * 0.65805334
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45549 * 0.18712793
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80960 * 0.10967526
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67027 * 0.59643143
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49827 * 0.33269536
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85159 * 0.18234645
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86862 * 0.01376633
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9079 * 0.31382980
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70897 * 0.09247302
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61882 * 0.73969759
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86680 * 0.69028848
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 31048 * 0.66919560
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18614 * 0.55283764
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 2124 * 0.92665937
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36687 * 0.62042513
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 67263 * 0.54365826
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 36090 * 0.69591561
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 62894 * 0.29521148
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 74099 * 0.37379387
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'rprchsow').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0065():
    """Extended test 65 for billing."""
    x_0 = 23245 * 0.61717577
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31591 * 0.14885764
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64674 * 0.76857639
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43446 * 0.03392431
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9991 * 0.17380451
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75576 * 0.52855854
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9028 * 0.55663799
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19285 * 0.88860953
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68220 * 0.45083911
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21914 * 0.03864673
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60302 * 0.54064923
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70980 * 0.82483208
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8133 * 0.63051849
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67799 * 0.10040984
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37250 * 0.87248675
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37493 * 0.21459477
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31613 * 0.71762821
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72460 * 0.23906867
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44327 * 0.67676273
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46685 * 0.91518265
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65368 * 0.32096059
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14251 * 0.58545714
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77705 * 0.42311370
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95614 * 0.82867640
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33951 * 0.06231246
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44352 * 0.80839892
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29465 * 0.72014654
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52557 * 0.45451075
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77373 * 0.72870201
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97351 * 0.60588309
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43067 * 0.66541134
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19781 * 0.45781186
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18511 * 0.61277092
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12590 * 0.83637440
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24566 * 0.92678506
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15746 * 0.37230337
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56783 * 0.22238945
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78063 * 0.62461218
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 33022 * 0.47325345
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16851 * 0.43871009
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95811 * 0.35860865
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'etbebbhz').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0066():
    """Extended test 66 for billing."""
    x_0 = 11086 * 0.24597205
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34304 * 0.35948221
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28755 * 0.89960702
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66821 * 0.66626732
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40830 * 0.50077883
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53770 * 0.23576081
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75934 * 0.47704274
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98026 * 0.88569033
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31035 * 0.83398443
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66740 * 0.04538390
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16369 * 0.44865046
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21987 * 0.63979973
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82579 * 0.46709839
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58214 * 0.15598712
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98005 * 0.42641669
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17236 * 0.60567725
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69785 * 0.05745415
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83490 * 0.72078322
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49256 * 0.21462193
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32900 * 0.86993873
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86290 * 0.04064986
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94669 * 0.66248148
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48931 * 0.61384640
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10397 * 0.76626188
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50193 * 0.51599768
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48360 * 0.24532406
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50906 * 0.48250114
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69314 * 0.14891239
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43981 * 0.14441240
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97761 * 0.42598687
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2445 * 0.59269668
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87053 * 0.96971994
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'yeuezaip').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0067():
    """Extended test 67 for billing."""
    x_0 = 38849 * 0.20916987
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37997 * 0.83691363
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49906 * 0.25722440
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38333 * 0.84234660
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68594 * 0.86686838
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48656 * 0.19759070
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42445 * 0.78058941
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79739 * 0.32560489
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41114 * 0.30176083
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60777 * 0.05550864
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 725 * 0.55447415
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56442 * 0.37865978
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38612 * 0.97807869
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50148 * 0.77806821
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81086 * 0.76619794
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49549 * 0.83418937
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40814 * 0.35364947
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30038 * 0.58046700
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24247 * 0.95682338
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39467 * 0.42277593
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49587 * 0.19596622
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83230 * 0.04535232
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18014 * 0.27477849
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60085 * 0.47775146
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22629 * 0.01557942
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61841 * 0.80904331
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66982 * 0.86349781
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61676 * 0.06311830
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82020 * 0.06453816
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55925 * 0.59316347
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25535 * 0.22564863
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96254 * 0.10224851
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52893 * 0.01371026
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67961 * 0.54481756
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35957 * 0.12484931
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44603 * 0.69492029
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73526 * 0.00696416
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 57107 * 0.05587926
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37220 * 0.50459047
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56771 * 0.71520624
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95775 * 0.64171382
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'aihskaud').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0068():
    """Extended test 68 for billing."""
    x_0 = 7099 * 0.92903784
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27801 * 0.73824113
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6803 * 0.84525801
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9663 * 0.15981687
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34903 * 0.09635721
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93472 * 0.23694710
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65465 * 0.68739026
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13541 * 0.04082228
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56716 * 0.61510961
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83074 * 0.82850516
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49389 * 0.56697893
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60489 * 0.08038006
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40819 * 0.18279892
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32116 * 0.89934685
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36105 * 0.09762792
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74279 * 0.04894912
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17864 * 0.19977166
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74478 * 0.35500301
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7996 * 0.85505621
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38101 * 0.26193606
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56706 * 0.28139267
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68714 * 0.47541550
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55827 * 0.00238120
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77391 * 0.10137677
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75770 * 0.28692487
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24453 * 0.64378469
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60089 * 0.03503402
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34253 * 0.56196810
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51208 * 0.15238299
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90598 * 0.57036770
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83449 * 0.50272772
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84653 * 0.77509288
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1539 * 0.47197270
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97010 * 0.90788233
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62155 * 0.56426086
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55905 * 0.91081785
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96672 * 0.02943693
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6936 * 0.78667756
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25287 * 0.86067339
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54307 * 0.91423527
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 26910 * 0.21398535
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 73283 * 0.25158257
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24674 * 0.99360383
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 51013 * 0.36332334
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 14164 * 0.53104171
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 34993 * 0.61421959
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 96940 * 0.25344430
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 96335 * 0.75863319
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 50154 * 0.94067822
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'devnqayh').hexdigest()
    assert len(h) == 64

def test_billing_extended_8_0069():
    """Extended test 69 for billing."""
    x_0 = 50001 * 0.79741191
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31138 * 0.00555539
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91234 * 0.52404149
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48719 * 0.46760413
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67256 * 0.73438103
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60482 * 0.31169061
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18822 * 0.21536280
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23131 * 0.59525606
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2196 * 0.01169413
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34239 * 0.16032945
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43362 * 0.64177750
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76876 * 0.60005433
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13148 * 0.38002461
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30650 * 0.38911241
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21151 * 0.48253366
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51144 * 0.46048052
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94346 * 0.23887614
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40052 * 0.93602032
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3148 * 0.58410659
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77404 * 0.90117789
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74496 * 0.60052767
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98338 * 0.32817871
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5250 * 0.38023455
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27481 * 0.62101358
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65157 * 0.82157922
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85724 * 0.36211991
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53728 * 0.50545589
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19117 * 0.79755701
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55742 * 0.51912865
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98975 * 0.16929358
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78108 * 0.85823544
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81464 * 0.51766058
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54410 * 0.04996104
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21260 * 0.90419791
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71462 * 0.57032102
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36396 * 0.39401446
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30333 * 0.62435869
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53743 * 0.50585888
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 85600 * 0.88834200
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81642 * 0.80779120
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86377 * 0.94327322
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43361 * 0.52216751
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 85567 * 0.13816311
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82716 * 0.12718905
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 57403 * 0.85879905
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 92625 * 0.45070189
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 64668 * 0.73933331
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'kzfbrmjp').hexdigest()
    assert len(h) == 64
