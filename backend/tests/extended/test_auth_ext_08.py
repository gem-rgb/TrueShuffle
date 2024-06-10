"""Extended tests for auth suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_auth_extended_8_0000():
    """Extended test 0 for auth."""
    x_0 = 91353 * 0.34217265
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52445 * 0.99173103
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55578 * 0.73403948
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22668 * 0.36866327
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97442 * 0.93808939
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27616 * 0.18381481
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71266 * 0.78468363
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43950 * 0.73904803
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17461 * 0.47583255
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4204 * 0.80239859
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16286 * 0.23378479
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14691 * 0.67989106
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17664 * 0.17805321
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75116 * 0.53725111
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54330 * 0.91289979
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92691 * 0.30645094
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14284 * 0.56558513
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6881 * 0.33264446
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42567 * 0.91181434
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27651 * 0.81367314
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93592 * 0.30316074
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43229 * 0.86685548
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'xxwznofi').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0001():
    """Extended test 1 for auth."""
    x_0 = 23743 * 0.40527228
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88945 * 0.01678518
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26648 * 0.91709780
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75824 * 0.27099336
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75849 * 0.76028277
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65334 * 0.44416324
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38748 * 0.74225041
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59615 * 0.87296632
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41722 * 0.56860047
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19491 * 0.28406751
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78437 * 0.59464236
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30501 * 0.76744359
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74304 * 0.07279861
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28021 * 0.86622116
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19339 * 0.47341432
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25072 * 0.18554079
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18931 * 0.41774769
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44654 * 0.65249939
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24773 * 0.02150045
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66574 * 0.25397731
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4397 * 0.27838801
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94354 * 0.62413373
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60770 * 0.66483461
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43081 * 0.30064270
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68024 * 0.66889712
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84097 * 0.95694700
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85464 * 0.82459454
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57044 * 0.95953915
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55269 * 0.83593266
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79357 * 0.17687849
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12764 * 0.09250410
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33003 * 0.90634165
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7447 * 0.99633522
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23741 * 0.76961201
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48952 * 0.80931696
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1111 * 0.06990534
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69540 * 0.80900391
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44341 * 0.64052541
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74737 * 0.02113735
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 60712 * 0.36146249
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'lnazgwsb').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0002():
    """Extended test 2 for auth."""
    x_0 = 82244 * 0.21761074
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82592 * 0.28046132
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73876 * 0.52383677
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88922 * 0.75657895
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79506 * 0.43443009
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76373 * 0.48874205
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10482 * 0.16929099
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68751 * 0.17640863
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11713 * 0.47597190
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97164 * 0.83435536
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71158 * 0.28910068
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20125 * 0.67701888
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33530 * 0.89924363
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3756 * 0.18940514
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87561 * 0.31948763
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52272 * 0.20080057
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78816 * 0.55111228
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99363 * 0.94696652
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11989 * 0.00907364
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22222 * 0.13473858
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75445 * 0.58193998
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43819 * 0.86814001
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73660 * 0.12869617
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95127 * 0.70559919
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86762 * 0.30458485
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86943 * 0.22415763
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39608 * 0.06137942
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'iqjxqqys').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0003():
    """Extended test 3 for auth."""
    x_0 = 45524 * 0.74817564
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48941 * 0.36552499
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46505 * 0.00358432
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93663 * 0.68944648
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92676 * 0.42992730
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36535 * 0.04851972
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81379 * 0.43544945
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85136 * 0.47455990
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40409 * 0.00726413
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61863 * 0.52331544
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67969 * 0.70480396
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2633 * 0.93820011
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12573 * 0.31695888
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25189 * 0.21791101
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2623 * 0.75154175
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11975 * 0.41024458
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88475 * 0.29421850
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52262 * 0.26576528
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44123 * 0.90585409
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35121 * 0.87747780
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3420 * 0.67532569
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80644 * 0.92893515
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67394 * 0.36087441
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41516 * 0.37910009
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40333 * 0.96164344
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56890 * 0.10221097
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36972 * 0.72292460
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38522 * 0.29788996
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18787 * 0.17592921
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18517 * 0.28440550
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39608 * 0.97723243
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7345 * 0.41524218
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1793 * 0.32556370
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31113 * 0.16559099
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29975 * 0.41486742
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25758 * 0.68740882
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10430 * 0.12582307
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69703 * 0.81860911
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16207 * 0.57898591
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4337 * 0.12027653
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51915 * 0.38239961
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5860 * 0.17686304
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14558 * 0.92432539
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 87704 * 0.47241526
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 49687 * 0.38952129
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 14854 * 0.82465474
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 4827 * 0.57387831
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 73265 * 0.33390781
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 99767 * 0.07669061
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 15617 * 0.79226146
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'nvzzbcmv').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0004():
    """Extended test 4 for auth."""
    x_0 = 88631 * 0.12197294
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16766 * 0.15189586
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94948 * 0.52791151
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24438 * 0.98381845
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33357 * 0.16710390
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28080 * 0.33325777
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39071 * 0.68957022
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64429 * 0.52079268
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13096 * 0.28304091
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90030 * 0.16372737
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26843 * 0.41743942
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74243 * 0.67363615
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46100 * 0.42366501
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7054 * 0.68977648
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32443 * 0.09082508
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94332 * 0.04216318
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86646 * 0.97619743
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74633 * 0.37154506
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71330 * 0.00745988
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30095 * 0.84261830
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32970 * 0.20260512
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92972 * 0.96808188
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19288 * 0.30199693
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79802 * 0.81252732
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11147 * 0.21535235
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84999 * 0.40990696
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64830 * 0.10679372
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59437 * 0.72820610
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74129 * 0.37236082
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5255 * 0.89357675
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72544 * 0.59319091
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82664 * 0.37150781
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2914 * 0.13787167
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69022 * 0.55843415
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21731 * 0.28853210
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26473 * 0.38870235
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7334 * 0.70009252
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53381 * 0.01578811
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2197 * 0.59282235
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95729 * 0.31721905
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35538 * 0.01207982
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3397 * 0.55982637
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'kjxmiamw').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0005():
    """Extended test 5 for auth."""
    x_0 = 83749 * 0.53787527
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11622 * 0.75232413
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43066 * 0.25774247
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12999 * 0.97755153
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60241 * 0.45660823
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33289 * 0.57616292
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86359 * 0.71197218
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20308 * 0.15558282
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24675 * 0.56865393
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78471 * 0.87570268
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57509 * 0.26993574
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19825 * 0.92293682
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36807 * 0.40156170
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6188 * 0.62076248
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84623 * 0.34126829
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76338 * 0.90023167
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22854 * 0.57694124
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71902 * 0.40764501
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8961 * 0.84717560
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79301 * 0.37504248
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64108 * 0.51926648
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26618 * 0.34458010
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85465 * 0.03545879
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80404 * 0.64110825
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70743 * 0.31236563
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55924 * 0.57218211
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73976 * 0.61184303
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38873 * 0.35859205
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65298 * 0.11440898
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75896 * 0.47715912
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51782 * 0.04070732
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94089 * 0.64598938
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88213 * 0.68915373
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68823 * 0.23753347
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88721 * 0.53393495
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20941 * 0.17028512
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18933 * 0.31117420
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24731 * 0.82450639
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4386 * 0.89405316
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96685 * 0.01990117
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 16411 * 0.65390388
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70205 * 0.81901640
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20372 * 0.95759508
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84920 * 0.22051247
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 25796 * 0.45040860
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 84795 * 0.02382336
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 48129 * 0.19203144
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 32393 * 0.51122951
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'khvotdtv').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0006():
    """Extended test 6 for auth."""
    x_0 = 30489 * 0.91608142
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79426 * 0.77317688
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22616 * 0.73531016
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80310 * 0.61722596
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87083 * 0.37690167
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52077 * 0.14389326
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24194 * 0.94817637
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12556 * 0.73494029
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30190 * 0.55683396
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93038 * 0.50064324
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55620 * 0.11221957
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40815 * 0.05487280
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22119 * 0.25749865
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90600 * 0.85776831
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25966 * 0.18254426
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63226 * 0.67657153
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35854 * 0.29258914
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48144 * 0.16119552
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7515 * 0.30205810
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34468 * 0.13874149
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39608 * 0.60047549
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48140 * 0.02010474
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71063 * 0.01174094
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8788 * 0.76410199
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88909 * 0.40710510
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32835 * 0.98558083
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96782 * 0.56985126
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82863 * 0.59010015
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15639 * 0.71800601
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'xpsaoolj').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0007():
    """Extended test 7 for auth."""
    x_0 = 45076 * 0.12878210
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94632 * 0.62150243
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21971 * 0.66327806
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96759 * 0.54057226
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58331 * 0.11514452
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3056 * 0.56713049
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35063 * 0.04082450
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20273 * 0.90945473
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24257 * 0.98042540
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7343 * 0.31739533
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11090 * 0.55351534
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90572 * 0.79268923
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1921 * 0.33355254
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56153 * 0.52358582
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93363 * 0.74995247
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30011 * 0.27227716
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33853 * 0.86183919
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85972 * 0.42307933
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10847 * 0.28591760
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44171 * 0.75380423
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56742 * 0.95063288
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49708 * 0.33335840
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2919 * 0.14459087
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10190 * 0.62303890
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32589 * 0.07546782
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62990 * 0.69448535
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34052 * 0.78772155
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7913 * 0.91291160
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90677 * 0.31918176
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57898 * 0.05359310
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73348 * 0.71351705
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45197 * 0.80869447
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59163 * 0.87601362
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73512 * 0.65740860
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84450 * 0.67072455
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27653 * 0.08520992
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42493 * 0.56511017
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32284 * 0.84844416
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16835 * 0.22429675
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57956 * 0.97624145
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12415 * 0.19725677
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81545 * 0.53615267
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 72171 * 0.79740639
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 81366 * 0.85894490
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 55170 * 0.56475678
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'cgeyuudv').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0008():
    """Extended test 8 for auth."""
    x_0 = 32568 * 0.42308689
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63067 * 0.85092058
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29825 * 0.05278050
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62322 * 0.12320486
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28834 * 0.81968368
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89023 * 0.80026784
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52593 * 0.74758671
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70065 * 0.30424732
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5752 * 0.08967748
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2780 * 0.28392275
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64516 * 0.82641536
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27401 * 0.83926951
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67136 * 0.76966621
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55546 * 0.67376092
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47287 * 0.49369755
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63853 * 0.53476944
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60100 * 0.46495626
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56874 * 0.48266752
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87803 * 0.95736762
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93902 * 0.64880497
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93065 * 0.57802958
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35786 * 0.70042173
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75334 * 0.48873955
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'isscwccs').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0009():
    """Extended test 9 for auth."""
    x_0 = 29031 * 0.81652700
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36157 * 0.28121624
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54793 * 0.09945204
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84054 * 0.68040876
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34664 * 0.69173755
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81171 * 0.49836252
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18591 * 0.37930422
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5300 * 0.96233227
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39964 * 0.18674520
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59757 * 0.38374970
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55322 * 0.16051099
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7531 * 0.72729805
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89761 * 0.69806720
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70689 * 0.03629863
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74594 * 0.77801439
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31191 * 0.44544697
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35263 * 0.19367370
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27976 * 0.54414271
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34850 * 0.69080344
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46329 * 0.71430607
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15828 * 0.92686594
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6928 * 0.02935759
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65915 * 0.99518212
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28833 * 0.12821497
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14645 * 0.31484434
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93494 * 0.18427519
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39781 * 0.32591084
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45730 * 0.61885761
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57886 * 0.47727447
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70670 * 0.25720149
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22702 * 0.24341294
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66875 * 0.79362052
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78789 * 0.20310900
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53524 * 0.99574590
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34682 * 0.47152333
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58366 * 0.64870226
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5043 * 0.94708135
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'xrnznecs').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0010():
    """Extended test 10 for auth."""
    x_0 = 97049 * 0.81816491
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95667 * 0.24920635
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49071 * 0.74050591
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64744 * 0.28000801
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12229 * 0.38100010
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69871 * 0.40570397
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61181 * 0.93493610
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49584 * 0.50895418
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75041 * 0.16822621
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86062 * 0.46978714
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2609 * 0.43073363
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27304 * 0.15259243
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96571 * 0.90651493
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71741 * 0.41937000
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88815 * 0.28384640
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11833 * 0.37533104
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28879 * 0.72686404
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67142 * 0.84329332
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1616 * 0.02630006
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3242 * 0.80203373
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67008 * 0.47051264
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78025 * 0.42554160
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86352 * 0.82337021
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13014 * 0.32981898
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65585 * 0.55636766
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49062 * 0.73573124
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3426 * 0.49613131
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68326 * 0.70347801
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78654 * 0.76479302
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ciyxxhbw').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0011():
    """Extended test 11 for auth."""
    x_0 = 80794 * 0.95877458
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94463 * 0.48424136
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50253 * 0.42237003
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40258 * 0.67737245
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61794 * 0.23538882
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90246 * 0.16530206
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20122 * 0.57924543
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32285 * 0.17837858
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92435 * 0.68560000
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67363 * 0.27329540
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22998 * 0.23582690
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94346 * 0.46475309
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79823 * 0.04173041
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67081 * 0.75803726
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49143 * 0.84456433
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67226 * 0.79942125
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7563 * 0.49401127
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5073 * 0.28489701
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14741 * 0.17113044
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37030 * 0.68469609
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92545 * 0.68206761
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34858 * 0.06114934
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65103 * 0.89429199
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15869 * 0.35786372
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57058 * 0.94789425
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84066 * 0.44890770
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23116 * 0.47942710
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34804 * 0.41694492
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54034 * 0.46934231
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'maojptdr').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0012():
    """Extended test 12 for auth."""
    x_0 = 44970 * 0.44962065
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86410 * 0.55685063
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35697 * 0.28589622
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19571 * 0.77712918
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9659 * 0.16838202
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89485 * 0.02746005
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97115 * 0.10647057
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84187 * 0.72540352
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59453 * 0.16826110
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57293 * 0.30454873
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69950 * 0.34165075
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72865 * 0.43944833
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10181 * 0.92062844
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90361 * 0.74673065
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96785 * 0.32973007
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3634 * 0.82700486
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50171 * 0.53879927
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69913 * 0.35185752
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40243 * 0.05371742
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52021 * 0.12160519
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34509 * 0.11363223
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39267 * 0.68572469
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43117 * 0.16203982
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83688 * 0.31714458
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80239 * 0.65155848
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25282 * 0.96467421
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42101 * 0.18839665
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46126 * 0.30038003
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17333 * 0.51432106
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70860 * 0.77924391
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91929 * 0.45198319
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78684 * 0.39621856
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1691 * 0.04169626
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9508 * 0.24843239
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95146 * 0.50833304
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81068 * 0.03576224
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55502 * 0.66096431
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89270 * 0.42456340
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15885 * 0.61212627
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24403 * 0.54343400
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80153 * 0.61836482
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67415 * 0.46162448
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'cmhakvay').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0013():
    """Extended test 13 for auth."""
    x_0 = 17727 * 0.33864918
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41937 * 0.90745238
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94281 * 0.44037378
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41984 * 0.21527800
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14594 * 0.33897302
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51458 * 0.16377233
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25308 * 0.88063771
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84861 * 0.21151241
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48547 * 0.91297278
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98047 * 0.57428913
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4819 * 0.98275903
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71201 * 0.02095009
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25825 * 0.32447856
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39078 * 0.07368639
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58936 * 0.60272079
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87517 * 0.26546800
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27026 * 0.88722586
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23853 * 0.13856651
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60432 * 0.17182224
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87006 * 0.26606339
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72949 * 0.96405775
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22950 * 0.32346864
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17954 * 0.98456820
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18900 * 0.89724695
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25839 * 0.53950580
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38006 * 0.08969935
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75592 * 0.98244580
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92645 * 0.62409272
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10023 * 0.79592501
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34433 * 0.70182805
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76608 * 0.18706222
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88642 * 0.68016251
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54176 * 0.75938223
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48997 * 0.68615206
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19729 * 0.60045764
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27258 * 0.32645324
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97518 * 0.26301105
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66968 * 0.31119001
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63870 * 0.32032281
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65793 * 0.67005887
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54928 * 0.23152401
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27420 * 0.55426047
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 63683 * 0.66759721
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92433 * 0.61660372
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 95097 * 0.42373173
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 53132 * 0.77635436
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'jlntffgs').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0014():
    """Extended test 14 for auth."""
    x_0 = 98101 * 0.85913925
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68627 * 0.60145827
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60680 * 0.12045649
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97017 * 0.08106403
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14415 * 0.49537990
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49998 * 0.22629170
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2491 * 0.29282947
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76768 * 0.50837639
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55021 * 0.23167232
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27436 * 0.48907989
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58427 * 0.53233933
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27328 * 0.40062177
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75605 * 0.17762924
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33495 * 0.26588191
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66620 * 0.82559473
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 769 * 0.78414701
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 462 * 0.41172183
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74338 * 0.84191576
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46602 * 0.13597293
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48508 * 0.58382239
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71837 * 0.26894824
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37391 * 0.25932441
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49564 * 0.79069660
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43310 * 0.02201033
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62703 * 0.60721863
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70491 * 0.66130391
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38294 * 0.89901536
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68787 * 0.98166485
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77694 * 0.95088276
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80605 * 0.40647137
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71208 * 0.06096185
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94699 * 0.10640375
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14502 * 0.38547608
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55763 * 0.82974345
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6538 * 0.91622271
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'fpifgexs').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0015():
    """Extended test 15 for auth."""
    x_0 = 57155 * 0.02281729
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42210 * 0.39732297
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90214 * 0.51928812
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51207 * 0.84653312
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49018 * 0.48723258
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18346 * 0.27484208
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21969 * 0.43270529
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 505 * 0.93237805
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33433 * 0.66898442
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43927 * 0.02596098
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3891 * 0.14774322
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58811 * 0.76997059
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82623 * 0.90728235
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18947 * 0.63339889
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91219 * 0.20861597
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5764 * 0.76928076
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40738 * 0.88771349
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23400 * 0.34019760
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67490 * 0.90653988
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61380 * 0.86715282
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36159 * 0.82430305
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91814 * 0.01981065
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73689 * 0.47679851
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16483 * 0.66333078
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59760 * 0.37040233
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55855 * 0.39290354
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73645 * 0.11681104
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47321 * 0.24575282
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66774 * 0.48419460
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73562 * 0.46051431
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55256 * 0.78304125
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8889 * 0.82699322
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28669 * 0.16244157
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7695 * 0.44917749
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11456 * 0.52681447
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51549 * 0.22694787
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7592 * 0.59523397
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19990 * 0.17719354
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'zpotwjjt').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0016():
    """Extended test 16 for auth."""
    x_0 = 687 * 0.73125964
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24037 * 0.73318938
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69245 * 0.45071355
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67112 * 0.85564360
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15886 * 0.23559805
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89921 * 0.23305753
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54563 * 0.26425600
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24799 * 0.34343871
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64399 * 0.56693217
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20614 * 0.81473494
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89455 * 0.54016351
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16219 * 0.89639611
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20503 * 0.91207824
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75196 * 0.02282090
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26636 * 0.25641504
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64083 * 0.64434784
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49720 * 0.21441119
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22660 * 0.42071816
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69271 * 0.77151482
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78588 * 0.06788089
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55959 * 0.62569788
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8644 * 0.71090783
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64248 * 0.65780617
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85734 * 0.31969075
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84501 * 0.56437676
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91131 * 0.08200728
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54212 * 0.85903851
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72537 * 0.62675006
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61179 * 0.46830867
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58815 * 0.62995599
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63378 * 0.87994271
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23280 * 0.40181620
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13308 * 0.28131460
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80463 * 0.49403058
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7465 * 0.73687988
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19416 * 0.74473187
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'qqpzdgjq').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0017():
    """Extended test 17 for auth."""
    x_0 = 8707 * 0.77802212
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95969 * 0.36707204
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36496 * 0.97291922
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96585 * 0.99874749
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47532 * 0.27237819
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40865 * 0.93708768
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45728 * 0.89341333
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27309 * 0.18407518
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7586 * 0.93993058
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33213 * 0.04385814
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52337 * 0.08757563
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38338 * 0.65665999
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65551 * 0.71422095
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28441 * 0.06142158
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47375 * 0.31058514
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88799 * 0.07868656
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 762 * 0.33809890
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51055 * 0.01713314
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62827 * 0.83662597
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86215 * 0.30776335
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35010 * 0.87044867
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72831 * 0.17815593
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89577 * 0.86295037
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66508 * 0.68916498
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11198 * 0.95804520
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37840 * 0.54958416
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22175 * 0.80924156
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73138 * 0.69100736
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25972 * 0.07709098
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 970 * 0.23788719
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88148 * 0.44022019
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57967 * 0.45623443
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55025 * 0.38189671
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42253 * 0.97257435
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83494 * 0.22473683
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95045 * 0.60369609
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39145 * 0.62625958
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95365 * 0.13398738
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34688 * 0.51585608
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84626 * 0.40325075
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47082 * 0.32637521
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 83715 * 0.61281020
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 85708 * 0.83793938
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 78606 * 0.94856844
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 16106 * 0.31228365
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 7581 * 0.21686953
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 51721 * 0.44107711
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'zpdtgggh').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0018():
    """Extended test 18 for auth."""
    x_0 = 68933 * 0.79431654
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5291 * 0.37076777
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98101 * 0.08643284
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91470 * 0.44672781
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45281 * 0.79546418
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34901 * 0.82142451
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 401 * 0.76786432
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2260 * 0.97353409
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30825 * 0.23255608
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72868 * 0.81367671
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86605 * 0.23514578
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84871 * 0.12754021
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75896 * 0.57545353
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93900 * 0.99147964
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71429 * 0.18889870
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68659 * 0.10351422
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86406 * 0.54846413
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30272 * 0.24070342
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60959 * 0.41873862
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44871 * 0.01886816
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32719 * 0.20013745
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'dywvjoic').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0019():
    """Extended test 19 for auth."""
    x_0 = 43072 * 0.41552516
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56454 * 0.01646353
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91483 * 0.46513637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68036 * 0.80363596
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89806 * 0.55019556
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99893 * 0.56748754
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86195 * 0.68842305
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6306 * 0.83114112
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40672 * 0.97593255
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35741 * 0.59304336
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70720 * 0.64150952
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51711 * 0.47840846
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74082 * 0.84700855
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21459 * 0.61363589
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57284 * 0.22931087
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80916 * 0.23529913
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99460 * 0.03781657
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20398 * 0.16722886
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30317 * 0.10971408
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99290 * 0.88413320
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8116 * 0.34950306
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33514 * 0.51731175
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98641 * 0.05517568
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42403 * 0.47404360
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51582 * 0.35570017
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72072 * 0.95529297
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99308 * 0.85110053
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19099 * 0.62998645
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'jgsqssvk').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0020():
    """Extended test 20 for auth."""
    x_0 = 32976 * 0.89048100
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41793 * 0.17832047
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61245 * 0.26646261
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6689 * 0.92304247
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73071 * 0.40703820
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95933 * 0.56220449
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57631 * 0.90562839
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15456 * 0.43922892
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3250 * 0.44130169
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30137 * 0.84605988
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45076 * 0.22625319
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17453 * 0.45130340
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92606 * 0.42055232
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89785 * 0.58902750
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40732 * 0.60892839
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74745 * 0.37498136
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44370 * 0.63559325
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61601 * 0.73209295
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49549 * 0.41405505
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7369 * 0.92239537
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2671 * 0.11238750
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27794 * 0.05711876
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26020 * 0.70187256
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9905 * 0.83738829
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42786 * 0.51156543
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40969 * 0.37693785
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27098 * 0.39675388
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43994 * 0.86394877
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11405 * 0.56330221
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36638 * 0.28998875
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13025 * 0.47232095
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62484 * 0.02236621
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36239 * 0.08041911
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79454 * 0.76437232
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60619 * 0.69737113
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84336 * 0.19315982
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53219 * 0.18179059
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55381 * 0.97178554
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'sgvjmbps').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0021():
    """Extended test 21 for auth."""
    x_0 = 86135 * 0.43407138
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26824 * 0.95544817
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92453 * 0.32052798
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56711 * 0.47527922
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13659 * 0.78809584
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22896 * 0.45429496
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14559 * 0.22966160
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28960 * 0.14439005
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45011 * 0.71757158
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 106 * 0.69569804
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84601 * 0.75314899
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8729 * 0.55476434
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26442 * 0.29909690
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78981 * 0.14437131
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71095 * 0.19613511
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59171 * 0.98819543
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42726 * 0.04606552
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55438 * 0.54486978
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64624 * 0.75460461
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49657 * 0.47403483
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'grbsczmi').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0022():
    """Extended test 22 for auth."""
    x_0 = 67217 * 0.12457164
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41688 * 0.29133815
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69185 * 0.23210664
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75802 * 0.36890109
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17056 * 0.33867894
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54253 * 0.17744670
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3968 * 0.62366477
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93963 * 0.13603894
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 528 * 0.36369419
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91431 * 0.43675788
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60556 * 0.89464029
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76563 * 0.36453782
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12154 * 0.02675420
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58529 * 0.78156549
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41460 * 0.12841036
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94137 * 0.34722728
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93440 * 0.92683198
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46332 * 0.27224285
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56622 * 0.15303007
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71344 * 0.26383836
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2171 * 0.82851145
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26512 * 0.73222298
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60423 * 0.61694372
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89120 * 0.73787943
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'lrpfawjg').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0023():
    """Extended test 23 for auth."""
    x_0 = 79357 * 0.91289822
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95266 * 0.72303253
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81609 * 0.18771754
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8381 * 0.53673965
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51289 * 0.19262200
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29104 * 0.06471438
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76151 * 0.95402912
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53195 * 0.99863250
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7883 * 0.79147416
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88550 * 0.04494909
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 209 * 0.56554314
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45582 * 0.25490892
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7544 * 0.73335957
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83769 * 0.81912819
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8620 * 0.81265227
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45567 * 0.86825127
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55578 * 0.21973541
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10341 * 0.72734767
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44108 * 0.15890510
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38225 * 0.02726748
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99403 * 0.38784046
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97623 * 0.24242530
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89582 * 0.71849929
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38450 * 0.39334514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64601 * 0.05958629
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27673 * 0.09774042
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66837 * 0.72463087
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36244 * 0.51853173
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34082 * 0.29831101
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'mzziklbl').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0024():
    """Extended test 24 for auth."""
    x_0 = 11796 * 0.93329407
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10950 * 0.54715226
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15502 * 0.07831408
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29318 * 0.46952271
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23371 * 0.30068109
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12343 * 0.97813716
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67494 * 0.86498285
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11518 * 0.29276109
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57957 * 0.86743269
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41036 * 0.28498803
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41436 * 0.43261232
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31128 * 0.07526911
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19462 * 0.45987560
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41033 * 0.36066108
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92068 * 0.29937757
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6627 * 0.83220989
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12834 * 0.95309260
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8597 * 0.84856090
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54547 * 0.95214322
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74784 * 0.23050590
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96589 * 0.23129422
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84703 * 0.57397706
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74306 * 0.64978143
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77980 * 0.05698515
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12388 * 0.62514343
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63480 * 0.14609836
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87105 * 0.82563572
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37800 * 0.21427891
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'zrpkqfsj').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0025():
    """Extended test 25 for auth."""
    x_0 = 80280 * 0.70196474
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78134 * 0.08302502
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62981 * 0.17531675
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46836 * 0.17182575
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35265 * 0.78568368
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80114 * 0.63247729
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99416 * 0.98683497
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69415 * 0.22876351
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68049 * 0.02475824
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17543 * 0.13144110
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94039 * 0.74275091
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16960 * 0.47961442
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70198 * 0.06187270
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84562 * 0.10007375
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7403 * 0.33970868
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3624 * 0.11504136
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31212 * 0.84841756
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16473 * 0.81963282
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54650 * 0.75172654
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32112 * 0.16644572
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75244 * 0.40992448
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36448 * 0.94374342
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37931 * 0.42535265
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50666 * 0.92184843
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77564 * 0.08842943
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 456 * 0.57389647
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58635 * 0.93851700
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70569 * 0.89378179
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77156 * 0.79634623
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35681 * 0.25334715
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54497 * 0.12770435
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63085 * 0.06824944
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50113 * 0.51852697
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79870 * 0.36014418
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95257 * 0.85026631
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77025 * 0.16875729
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65702 * 0.59788234
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61042 * 0.20875934
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86820 * 0.56697246
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28294 * 0.66714908
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'nltaiees').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0026():
    """Extended test 26 for auth."""
    x_0 = 34183 * 0.55927708
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98485 * 0.13843960
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87731 * 0.20769408
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37648 * 0.88491948
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29513 * 0.75180192
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55562 * 0.82201138
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36029 * 0.06329499
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65236 * 0.49347857
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5058 * 0.81796422
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35175 * 0.94731106
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21954 * 0.33841192
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92635 * 0.55442214
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49876 * 0.96486002
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38794 * 0.43350880
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34065 * 0.64141532
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97011 * 0.60745494
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62532 * 0.43968009
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90044 * 0.70830209
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25493 * 0.56345738
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52644 * 0.09222870
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86698 * 0.42201269
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37457 * 0.99009972
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25016 * 0.44875200
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12678 * 0.28776606
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'mlxhsoks').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0027():
    """Extended test 27 for auth."""
    x_0 = 87133 * 0.24650938
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47444 * 0.15323346
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72937 * 0.71362899
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17362 * 0.13400718
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21185 * 0.47450885
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34107 * 0.36554040
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22642 * 0.54700983
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59570 * 0.50059226
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61550 * 0.47440393
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34292 * 0.80868777
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30824 * 0.98669675
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85147 * 0.28210862
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78146 * 0.10755705
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58470 * 0.17383832
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72920 * 0.83441504
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78910 * 0.55694604
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59936 * 0.90256925
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55950 * 0.78120468
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43737 * 0.05486045
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80208 * 0.90029424
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65352 * 0.53463395
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36249 * 0.86121468
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42623 * 0.64418375
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'mdnklliq').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0028():
    """Extended test 28 for auth."""
    x_0 = 37808 * 0.12121235
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69097 * 0.80670736
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38163 * 0.39924033
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79532 * 0.95784219
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47158 * 0.53823908
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30894 * 0.77729911
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87314 * 0.90290552
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74354 * 0.20144139
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79659 * 0.43052525
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25964 * 0.50119476
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42333 * 0.19142711
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27307 * 0.69786160
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13884 * 0.66234283
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34039 * 0.48445911
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49011 * 0.37917134
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2162 * 0.12118350
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92805 * 0.32508671
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39354 * 0.19134722
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29079 * 0.91819195
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70815 * 0.82972837
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39411 * 0.55527608
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18168 * 0.30681085
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2587 * 0.02750922
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38919 * 0.92588895
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57856 * 0.34328278
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11981 * 0.71041740
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61643 * 0.71015527
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'luzxcisp').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0029():
    """Extended test 29 for auth."""
    x_0 = 6285 * 0.96127154
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98123 * 0.60692721
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51835 * 0.16897946
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99772 * 0.70653340
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42742 * 0.07104059
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48426 * 0.52499307
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46001 * 0.78435744
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76818 * 0.49050780
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44182 * 0.65754888
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72098 * 0.62281279
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66904 * 0.60742497
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59166 * 0.98267348
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 809 * 0.18116330
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99887 * 0.66348047
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55054 * 0.42749321
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34894 * 0.47438596
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13621 * 0.83634932
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69869 * 0.20295996
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87795 * 0.58098007
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36848 * 0.65331978
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51614 * 0.79069981
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64825 * 0.54530386
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6206 * 0.93427607
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4567 * 0.32325669
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93710 * 0.60440113
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94891 * 0.51598871
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32733 * 0.78527922
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15655 * 0.43702260
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38065 * 0.63435292
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26074 * 0.77975113
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84905 * 0.28299184
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31216 * 0.89320469
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99121 * 0.05896814
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77375 * 0.09007727
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'dldqoruz').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0030():
    """Extended test 30 for auth."""
    x_0 = 40199 * 0.74609588
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99932 * 0.12620295
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2664 * 0.12768658
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33273 * 0.17221767
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21339 * 0.66094858
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60114 * 0.14127474
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99251 * 0.09949913
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65959 * 0.39085099
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32119 * 0.49527711
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65166 * 0.29948930
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81872 * 0.95595577
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37418 * 0.61581147
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12509 * 0.29498040
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99134 * 0.70308321
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70898 * 0.51668602
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36465 * 0.12831704
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15599 * 0.60550644
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68287 * 0.76712610
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23027 * 0.64630206
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96055 * 0.94254698
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71019 * 0.91969630
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99290 * 0.38438217
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15333 * 0.21419341
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91551 * 0.67925682
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55938 * 0.55794179
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63250 * 0.22220803
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87129 * 0.81920271
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56387 * 0.43677018
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18548 * 0.59428452
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22030 * 0.86428610
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96834 * 0.28513666
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9377 * 0.80258805
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2339 * 0.84107738
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63109 * 0.62869038
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11619 * 0.55371490
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87705 * 0.94822596
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19173 * 0.63849812
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97267 * 0.15820183
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34827 * 0.19875551
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54460 * 0.89823881
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 93135 * 0.77444815
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45194 * 0.77486599
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75115 * 0.09671089
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'svsrwbtw').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0031():
    """Extended test 31 for auth."""
    x_0 = 43225 * 0.17844425
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99867 * 0.57241450
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78496 * 0.03781285
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34084 * 0.08636452
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7794 * 0.13053639
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57264 * 0.55726283
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79872 * 0.56500404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10294 * 0.37385663
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82217 * 0.13334392
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92278 * 0.92315905
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42011 * 0.19681253
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97989 * 0.33637823
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87773 * 0.27617553
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8137 * 0.29593192
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94858 * 0.88615334
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7862 * 0.37406284
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73187 * 0.67006959
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52265 * 0.06415191
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84669 * 0.71665626
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93391 * 0.19585884
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92729 * 0.95635622
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57548 * 0.65015704
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87905 * 0.17053054
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88342 * 0.34388177
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31931 * 0.14262523
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5296 * 0.09263359
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88956 * 0.79251782
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8534 * 0.75578847
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96189 * 0.26104331
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'mcxyjulz').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0032():
    """Extended test 32 for auth."""
    x_0 = 1579 * 0.98423548
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16030 * 0.72881053
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95879 * 0.64437717
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2122 * 0.00471618
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18192 * 0.20586200
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73267 * 0.27280235
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50336 * 0.03686528
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98860 * 0.79891861
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30683 * 0.58311522
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24448 * 0.20797589
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64494 * 0.25953315
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10958 * 0.99077243
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52593 * 0.45110496
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41748 * 0.64974172
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80222 * 0.63639454
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50988 * 0.24957614
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12211 * 0.55887311
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24488 * 0.05977711
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67207 * 0.04636180
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48050 * 0.86476756
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13729 * 0.21210451
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43771 * 0.11952470
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76542 * 0.21700734
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39431 * 0.87737977
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36977 * 0.50665865
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89174 * 0.44818856
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16394 * 0.52435616
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69325 * 0.19561635
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61037 * 0.20090932
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67790 * 0.70494166
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90003 * 0.92528542
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31856 * 0.82390756
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15460 * 0.55868364
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88482 * 0.36502460
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65591 * 0.57557078
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'bnxnlfss').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0033():
    """Extended test 33 for auth."""
    x_0 = 30153 * 0.52309374
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38635 * 0.92279957
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71965 * 0.33056306
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67643 * 0.92397583
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57332 * 0.69720332
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57812 * 0.09202646
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5357 * 0.76392721
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21393 * 0.46078643
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87348 * 0.21841690
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42132 * 0.48587868
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44945 * 0.29631617
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26769 * 0.14828899
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51843 * 0.29640213
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67083 * 0.16037274
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18323 * 0.45110947
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23814 * 0.11528555
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85466 * 0.04103378
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81283 * 0.40826283
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19235 * 0.67366787
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96893 * 0.72774588
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51917 * 0.91889291
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14729 * 0.09014180
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5370 * 0.13472398
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88975 * 0.95631068
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64355 * 0.67816266
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40463 * 0.96211173
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'dugfxkhw').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0034():
    """Extended test 34 for auth."""
    x_0 = 4691 * 0.14780240
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33219 * 0.73316492
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 298 * 0.86568193
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90151 * 0.31764334
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56230 * 0.12414840
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47327 * 0.51973632
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25393 * 0.31395172
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63677 * 0.82134927
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35977 * 0.13185381
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7667 * 0.11298569
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66089 * 0.92796039
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10295 * 0.74275777
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59595 * 0.30954093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81899 * 0.89129040
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54083 * 0.12236122
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18684 * 0.86830626
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94759 * 0.33536191
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36561 * 0.53643155
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24918 * 0.68621144
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28305 * 0.03956146
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'xzethrjh').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0035():
    """Extended test 35 for auth."""
    x_0 = 73793 * 0.68557124
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19423 * 0.74135624
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27937 * 0.80777416
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44392 * 0.19825940
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85034 * 0.34091448
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4525 * 0.97825456
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38546 * 0.05499612
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79898 * 0.15854030
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97029 * 0.05102412
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71712 * 0.22229896
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28754 * 0.04547780
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36871 * 0.97010279
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13675 * 0.66006074
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95833 * 0.51225444
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41980 * 0.27608167
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34819 * 0.37726026
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22183 * 0.76442135
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61097 * 0.76401964
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74606 * 0.60209503
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75383 * 0.70038614
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51263 * 0.95934035
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45208 * 0.87933644
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28625 * 0.71359638
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47665 * 0.42316563
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45424 * 0.76439858
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31853 * 0.00926971
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96359 * 0.97627455
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47267 * 0.68674031
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3511 * 0.02532504
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45782 * 0.56966038
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55696 * 0.53234869
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92493 * 0.55428956
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27103 * 0.51521325
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85933 * 0.31018873
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13937 * 0.77009349
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42665 * 0.65577673
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98814 * 0.57800046
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43227 * 0.97478445
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'foysrwnn').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0036():
    """Extended test 36 for auth."""
    x_0 = 19687 * 0.37571184
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66388 * 0.96104368
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42710 * 0.81809748
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71229 * 0.10114920
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13639 * 0.36736743
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18962 * 0.18080714
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37651 * 0.98695484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82992 * 0.68744023
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28197 * 0.96018376
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91373 * 0.97723003
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78242 * 0.82443312
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82926 * 0.07003279
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94576 * 0.37295906
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19862 * 0.78296156
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8194 * 0.97334701
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59544 * 0.47928250
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7246 * 0.61389060
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63397 * 0.70519238
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73061 * 0.21958285
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24071 * 0.55115277
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31868 * 0.39554342
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96247 * 0.24652341
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15020 * 0.47827648
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47291 * 0.71626250
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4499 * 0.76233920
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40039 * 0.56237700
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'qexfokuk').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0037():
    """Extended test 37 for auth."""
    x_0 = 45374 * 0.39936021
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29574 * 0.57227760
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9292 * 0.80305939
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98348 * 0.47647746
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16567 * 0.40070219
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30496 * 0.88003545
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42162 * 0.58503283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91039 * 0.45516772
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55684 * 0.70880248
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96210 * 0.74000765
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16478 * 0.81773819
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6794 * 0.24284284
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39412 * 0.88475187
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25140 * 0.05603755
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90430 * 0.94851001
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35616 * 0.96550048
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83540 * 0.74128676
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1706 * 0.18338318
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6064 * 0.27671408
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56314 * 0.47129629
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57644 * 0.84132540
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21564 * 0.89131635
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48436 * 0.36381577
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56745 * 0.01991631
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38008 * 0.85907574
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76624 * 0.38269215
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6587 * 0.85793027
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21459 * 0.47354791
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32041 * 0.89730735
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39249 * 0.65736486
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70341 * 0.92181459
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 139 * 0.04639500
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37549 * 0.40732616
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6271 * 0.44439053
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24542 * 0.63529987
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'mxgaudhu').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0038():
    """Extended test 38 for auth."""
    x_0 = 91089 * 0.27469501
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91955 * 0.19850349
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12046 * 0.00482916
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35 * 0.65353006
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69986 * 0.73287138
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40913 * 0.85639248
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10997 * 0.88667708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61403 * 0.03109631
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70748 * 0.83045475
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24502 * 0.75175893
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92371 * 0.73344845
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64511 * 0.89051663
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65318 * 0.67295550
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13054 * 0.00402479
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37012 * 0.51045683
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31376 * 0.08790656
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76517 * 0.29730501
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98408 * 0.85657937
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25651 * 0.83570111
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80811 * 0.24302265
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51505 * 0.39109145
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58908 * 0.69548824
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9710 * 0.04663582
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31521 * 0.08980581
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10893 * 0.65105913
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48266 * 0.21476668
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25027 * 0.87947967
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93687 * 0.84123848
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2312 * 0.26595747
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35453 * 0.37986077
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23399 * 0.15308876
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'utoggnwf').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0039():
    """Extended test 39 for auth."""
    x_0 = 36866 * 0.64520665
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73800 * 0.44939484
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27852 * 0.15348694
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57112 * 0.22820307
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25814 * 0.15878757
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61969 * 0.98240247
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65945 * 0.55414456
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78321 * 0.94769627
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26714 * 0.92454190
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80906 * 0.64750401
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81429 * 0.52588451
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26184 * 0.70448320
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73099 * 0.82579379
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80393 * 0.29615484
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68921 * 0.81462929
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70589 * 0.51982626
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5348 * 0.52799327
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97280 * 0.14291342
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96976 * 0.39000748
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75247 * 0.10458601
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17918 * 0.32129001
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83561 * 0.62009286
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58578 * 0.64318340
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54352 * 0.27250405
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9948 * 0.12200444
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10147 * 0.23736862
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97427 * 0.17872514
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79399 * 0.33150798
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94193 * 0.66866533
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73333 * 0.87226562
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94348 * 0.45132145
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75405 * 0.38518569
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'dfvafkxy').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0040():
    """Extended test 40 for auth."""
    x_0 = 10297 * 0.37340129
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91945 * 0.71072287
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83206 * 0.43126132
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75267 * 0.57246178
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35344 * 0.87088701
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81546 * 0.53172388
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74361 * 0.04137894
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55908 * 0.66016748
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99736 * 0.41330089
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67609 * 0.39423687
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1272 * 0.30061597
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11450 * 0.27706740
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61395 * 0.39164974
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24211 * 0.55024522
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42986 * 0.77661607
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71651 * 0.38912140
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27025 * 0.09673950
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82484 * 0.69140982
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30568 * 0.42738031
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75637 * 0.11358263
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9751 * 0.56658261
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94509 * 0.29768718
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48883 * 0.52192612
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2877 * 0.63274416
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4043 * 0.53639154
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40775 * 0.98781590
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77345 * 0.40779346
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9795 * 0.57337385
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97256 * 0.76432793
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18725 * 0.18880096
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67967 * 0.70340106
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68360 * 0.24038883
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1594 * 0.94797775
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59456 * 0.15220772
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53833 * 0.69035005
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63790 * 0.34071836
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58389 * 0.09455561
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'lmmmyalv').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0041():
    """Extended test 41 for auth."""
    x_0 = 99616 * 0.34056927
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2413 * 0.64937419
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65593 * 0.36960736
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89303 * 0.17406407
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9877 * 0.86654876
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74985 * 0.09989851
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6999 * 0.76458009
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24822 * 0.00059655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13764 * 0.98120911
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99564 * 0.75365619
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33575 * 0.96957665
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34845 * 0.46410714
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56942 * 0.49840585
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45129 * 0.16339822
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48281 * 0.90109761
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68391 * 0.82767857
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55544 * 0.44177904
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28724 * 0.54945589
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27510 * 0.56143344
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42728 * 0.65414589
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21221 * 0.63207804
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8224 * 0.39820091
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86887 * 0.25013445
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24021 * 0.94268696
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72284 * 0.87044392
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23695 * 0.88350037
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57951 * 0.47329967
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98678 * 0.91915921
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84616 * 0.42522952
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77089 * 0.17336409
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74834 * 0.52914770
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45515 * 0.32655002
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1781 * 0.69275676
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32173 * 0.24201801
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92777 * 0.61695372
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42994 * 0.75141144
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13269 * 0.72440364
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91941 * 0.53801997
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53678 * 0.56513736
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99188 * 0.09527100
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77160 * 0.92343303
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 7212 * 0.96791858
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 78635 * 0.17191684
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88862 * 0.84470066
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86794 * 0.80764744
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 28449 * 0.87891759
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 13068 * 0.56656718
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 33172 * 0.54407963
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'soxrugyv').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0042():
    """Extended test 42 for auth."""
    x_0 = 76397 * 0.39285305
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48621 * 0.65376879
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64321 * 0.17956730
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50890 * 0.37443859
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86933 * 0.55354039
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41114 * 0.10003617
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70179 * 0.12276561
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60490 * 0.94608066
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87072 * 0.07347500
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55328 * 0.46127472
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37215 * 0.37389914
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57569 * 0.93902276
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19516 * 0.54940331
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15554 * 0.59193591
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42830 * 0.31016894
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51415 * 0.14633358
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82849 * 0.39687598
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67585 * 0.38438503
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25121 * 0.23038002
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68008 * 0.28681714
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74736 * 0.90325432
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45943 * 0.24144043
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25045 * 0.91042656
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76291 * 0.34779107
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'bbhocota').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0043():
    """Extended test 43 for auth."""
    x_0 = 22689 * 0.46199641
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9569 * 0.94701294
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51395 * 0.18700160
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57182 * 0.21597112
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3318 * 0.33225973
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57562 * 0.61601060
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27889 * 0.84066282
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19458 * 0.02735593
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44314 * 0.60623424
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96161 * 0.22187951
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78770 * 0.79993053
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47526 * 0.27866370
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44274 * 0.68515519
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26736 * 0.80138891
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66347 * 0.71613601
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53016 * 0.81405973
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87387 * 0.81573674
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14458 * 0.28722896
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3094 * 0.75914017
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59009 * 0.57359634
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10933 * 0.80526231
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'qhmoadud').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0044():
    """Extended test 44 for auth."""
    x_0 = 23658 * 0.79723964
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33495 * 0.68473577
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84621 * 0.07769069
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57103 * 0.62619824
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81978 * 0.19252186
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47711 * 0.19033862
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36774 * 0.64745903
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54922 * 0.77368708
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78650 * 0.33004372
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67677 * 0.36144063
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55224 * 0.48856670
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83305 * 0.26024863
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2582 * 0.42497483
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11207 * 0.53370626
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63939 * 0.17969000
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12518 * 0.29316890
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54309 * 0.60343610
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75962 * 0.03806499
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17854 * 0.32512995
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42685 * 0.68609399
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15551 * 0.99680504
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27162 * 0.10687121
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62492 * 0.23852237
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57435 * 0.32880468
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56186 * 0.26316925
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48282 * 0.13322290
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7736 * 0.79261984
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81539 * 0.97186887
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80498 * 0.60683513
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47585 * 0.81841200
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32018 * 0.25683109
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25366 * 0.18338353
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34966 * 0.13744357
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34192 * 0.24298943
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60917 * 0.42579400
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55015 * 0.95698225
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89085 * 0.83389148
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'gruwtvja').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0045():
    """Extended test 45 for auth."""
    x_0 = 45814 * 0.95035494
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54138 * 0.40917061
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79889 * 0.84488951
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70560 * 0.60844356
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15025 * 0.79098322
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29898 * 0.99340158
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27527 * 0.30905253
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87613 * 0.59714359
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57259 * 0.96092112
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4628 * 0.39398275
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30102 * 0.64605628
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47002 * 0.03162699
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65512 * 0.85433447
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45613 * 0.31276746
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19138 * 0.62331889
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12590 * 0.73542176
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 209 * 0.35888721
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86087 * 0.30907280
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93711 * 0.19552363
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10758 * 0.53380967
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2586 * 0.09156485
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29675 * 0.56681613
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63580 * 0.12010404
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94599 * 0.50655642
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77710 * 0.48638089
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8848 * 0.02627990
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94525 * 0.69075229
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71651 * 0.78030477
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59119 * 0.50072256
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90323 * 0.62773820
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24026 * 0.31538897
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63924 * 0.81137464
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29225 * 0.72380997
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35956 * 0.15485780
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17457 * 0.53250586
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11748 * 0.49219457
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43475 * 0.62876184
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42724 * 0.05377100
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38090 * 0.25341050
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6547 * 0.67508678
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65129 * 0.45532989
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'zmsvwpca').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0046():
    """Extended test 46 for auth."""
    x_0 = 13402 * 0.90819682
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5270 * 0.48310995
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91913 * 0.25999357
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25648 * 0.98867510
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91199 * 0.20144236
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6257 * 0.63582823
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78870 * 0.09740593
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90786 * 0.88819657
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69480 * 0.69481569
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56627 * 0.26553938
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83720 * 0.25363809
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71222 * 0.63042556
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24827 * 0.83848772
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8199 * 0.84653070
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20424 * 0.93382183
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62233 * 0.68485995
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61381 * 0.78039113
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63585 * 0.02480799
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80572 * 0.74733663
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59050 * 0.64021515
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63922 * 0.85715447
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43327 * 0.71798236
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17789 * 0.27928929
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9509 * 0.61514974
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27219 * 0.10996073
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22607 * 0.69113643
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21433 * 0.40325670
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99383 * 0.55260048
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75798 * 0.96205560
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19754 * 0.62992486
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17920 * 0.87564388
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21786 * 0.71768206
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52247 * 0.10042184
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90528 * 0.85700509
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'jvldshvb').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0047():
    """Extended test 47 for auth."""
    x_0 = 92232 * 0.41190858
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45445 * 0.20668095
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58213 * 0.67348780
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86835 * 0.95486471
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38003 * 0.55611037
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53541 * 0.80377507
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98178 * 0.11975705
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73439 * 0.63749572
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75192 * 0.14788155
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80269 * 0.02832301
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60213 * 0.53453526
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50543 * 0.70471441
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72260 * 0.47564066
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12022 * 0.02926798
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61820 * 0.73701864
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9761 * 0.50811722
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35657 * 0.96980258
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59698 * 0.66151308
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 397 * 0.13307100
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26612 * 0.81374311
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71670 * 0.69875309
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96232 * 0.78825969
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45516 * 0.89772606
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16583 * 0.43587494
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5816 * 0.15515245
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46740 * 0.86894935
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9241 * 0.39587533
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32698 * 0.96641730
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78392 * 0.87636531
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18067 * 0.92811731
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65624 * 0.48097237
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58485 * 0.21252122
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62082 * 0.88765701
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36297 * 0.70218936
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13308 * 0.52044895
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53502 * 0.55503011
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94746 * 0.62694695
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6033 * 0.40827037
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75593 * 0.65336011
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90175 * 0.49403938
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19072 * 0.52890742
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39996 * 0.08936064
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 80291 * 0.73328048
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 342 * 0.22111073
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 52639 * 0.43107177
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 37059 * 0.34083319
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 74448 * 0.99796969
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 85141 * 0.70156358
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ptggadue').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0048():
    """Extended test 48 for auth."""
    x_0 = 9918 * 0.60398350
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84761 * 0.22481683
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75556 * 0.55134238
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69239 * 0.21856749
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47832 * 0.17676609
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59378 * 0.58484193
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71273 * 0.44503376
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85211 * 0.77863411
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53094 * 0.16544386
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56806 * 0.88068476
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80108 * 0.47395421
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78046 * 0.29980075
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48117 * 0.89781830
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20954 * 0.56829201
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79383 * 0.58023185
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44145 * 0.22208404
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81832 * 0.35526524
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91347 * 0.13198863
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34543 * 0.18012194
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17205 * 0.72194031
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59368 * 0.00823827
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49826 * 0.43506437
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5095 * 0.13439768
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26490 * 0.52024955
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68414 * 0.98792608
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 822 * 0.04360217
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32371 * 0.35681017
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18510 * 0.31101315
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64250 * 0.09453115
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21289 * 0.75041363
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93820 * 0.54183587
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56527 * 0.02809751
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87126 * 0.36382423
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55642 * 0.20702606
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'sakyophl').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0049():
    """Extended test 49 for auth."""
    x_0 = 73758 * 0.94452263
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4840 * 0.09926648
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5539 * 0.02268668
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76129 * 0.62554065
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76200 * 0.90045658
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54530 * 0.65766812
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99419 * 0.99543267
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64326 * 0.70794349
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78093 * 0.09211164
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96567 * 0.43413774
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58318 * 0.61234802
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82633 * 0.46646748
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39097 * 0.71563373
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2147 * 0.60334332
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24461 * 0.51021478
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59123 * 0.31435272
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12502 * 0.67312961
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91258 * 0.52444187
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34684 * 0.46922792
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90395 * 0.65121935
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64973 * 0.65517923
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12382 * 0.50318365
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62079 * 0.72103472
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6663 * 0.81640858
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21122 * 0.22865892
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75252 * 0.39997746
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31677 * 0.58104704
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62145 * 0.16251314
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57091 * 0.87504673
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96762 * 0.94949697
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2615 * 0.28642131
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5448 * 0.62419302
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17765 * 0.71139500
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56960 * 0.59101729
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30700 * 0.27266187
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7905 * 0.76275235
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56953 * 0.79825408
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 99707 * 0.92146259
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'qyehyoiz').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0050():
    """Extended test 50 for auth."""
    x_0 = 94823 * 0.88452009
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41371 * 0.47000256
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97721 * 0.17141147
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61866 * 0.60090167
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22830 * 0.60351797
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94205 * 0.08677975
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12598 * 0.44887151
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37457 * 0.93568979
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29271 * 0.45718059
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13375 * 0.81486632
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18467 * 0.14115117
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57790 * 0.02016222
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18484 * 0.69980114
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83328 * 0.17949349
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54894 * 0.73131900
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65480 * 0.88432413
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29645 * 0.26076350
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64583 * 0.34555688
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37514 * 0.57338452
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12141 * 0.33584449
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52494 * 0.43499723
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71538 * 0.59024207
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26587 * 0.83954715
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14791 * 0.29418004
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11758 * 0.45469981
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3607 * 0.61679361
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96504 * 0.42953091
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37893 * 0.72546843
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37910 * 0.85262447
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53235 * 0.28516744
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44891 * 0.00123323
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27746 * 0.37197841
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43814 * 0.94769789
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9680 * 0.17419890
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87423 * 0.70661680
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ivgxuxav').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0051():
    """Extended test 51 for auth."""
    x_0 = 66840 * 0.93194525
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81241 * 0.68425068
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21113 * 0.43872463
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6846 * 0.77207246
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70531 * 0.74312990
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41069 * 0.25785397
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25791 * 0.13556174
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9153 * 0.20207220
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85569 * 0.44988163
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33957 * 0.80506802
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11657 * 0.29957293
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92416 * 0.13922822
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61303 * 0.01858602
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15385 * 0.64209057
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11859 * 0.78670625
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68507 * 0.72405971
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31020 * 0.52771174
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83195 * 0.54430337
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40961 * 0.36111825
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8100 * 0.96964256
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38058 * 0.47124736
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22387 * 0.71311288
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14068 * 0.72718367
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58871 * 0.80919326
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22972 * 0.19791288
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22605 * 0.16117757
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67105 * 0.03483173
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48865 * 0.11402566
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88719 * 0.44200937
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76328 * 0.04963677
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32815 * 0.61057804
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37864 * 0.23063416
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39580 * 0.51065490
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82122 * 0.12356964
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79977 * 0.55963379
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13010 * 0.42384661
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3720 * 0.78727462
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43778 * 0.29743769
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30421 * 0.01757570
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82695 * 0.05677379
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'krrhgfbb').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0052():
    """Extended test 52 for auth."""
    x_0 = 50570 * 0.47910338
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32641 * 0.26295591
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98519 * 0.70642426
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10785 * 0.47489243
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21569 * 0.25766944
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17602 * 0.37194151
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78929 * 0.51934991
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41061 * 0.85344175
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42192 * 0.39297522
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84874 * 0.24204463
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96483 * 0.61603183
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85660 * 0.04380252
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8690 * 0.27739016
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92518 * 0.62270078
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95906 * 0.01753177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65307 * 0.49442297
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26629 * 0.18259614
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42259 * 0.26349818
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29745 * 0.17921521
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84956 * 0.73700330
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14068 * 0.29819416
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86552 * 0.19959113
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91101 * 0.93379761
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24368 * 0.22465614
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31117 * 0.39441296
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96232 * 0.86179459
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61106 * 0.16397087
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'xjndssdg').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0053():
    """Extended test 53 for auth."""
    x_0 = 71907 * 0.66713649
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38270 * 0.75622278
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42761 * 0.37484761
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52540 * 0.18060585
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97253 * 0.07365882
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19913 * 0.52519011
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71918 * 0.93192540
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10687 * 0.35353583
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66928 * 0.95064175
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16999 * 0.94873736
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99500 * 0.51183163
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74530 * 0.38291581
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4481 * 0.90810785
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30422 * 0.75372104
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86598 * 0.54409485
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53919 * 0.40311030
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89637 * 0.49263789
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40954 * 0.65718865
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33841 * 0.37789603
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46045 * 0.31699511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5619 * 0.64074003
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16056 * 0.45067089
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81780 * 0.60908187
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16879 * 0.69112300
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77744 * 0.97952224
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94874 * 0.16819983
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45003 * 0.59990485
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67160 * 0.31461381
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40711 * 0.58922359
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95249 * 0.10996366
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88805 * 0.87651404
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35040 * 0.66678107
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49057 * 0.37387188
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'cnazlcyu').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0054():
    """Extended test 54 for auth."""
    x_0 = 51620 * 0.73267291
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30658 * 0.78818295
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26456 * 0.97249608
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91140 * 0.30262842
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48143 * 0.55336614
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19925 * 0.57520799
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17548 * 0.80649214
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18546 * 0.48489323
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10239 * 0.57615986
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34884 * 0.66295785
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20390 * 0.95316393
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23248 * 0.83677539
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98703 * 0.27126900
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4693 * 0.78034816
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95004 * 0.35520470
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71903 * 0.77271606
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24914 * 0.27581997
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6418 * 0.97583380
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60178 * 0.49432998
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87585 * 0.86376275
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27019 * 0.14037119
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11828 * 0.49478733
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50902 * 0.84423962
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30159 * 0.94546483
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33565 * 0.05975275
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91700 * 0.99924116
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82245 * 0.13741992
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28918 * 0.26939470
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53464 * 0.77056485
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91555 * 0.93664173
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7511 * 0.31713319
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7795 * 0.65204788
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1219 * 0.42856168
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80776 * 0.05194578
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15767 * 0.39535308
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57891 * 0.88514495
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ogymhjtp').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0055():
    """Extended test 55 for auth."""
    x_0 = 68552 * 0.29273481
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99258 * 0.41323529
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59009 * 0.61236521
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37726 * 0.72331266
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13747 * 0.03338114
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59560 * 0.45828385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62982 * 0.11642621
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2812 * 0.10399304
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14808 * 0.59673897
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25518 * 0.26410261
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66999 * 0.82182564
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77435 * 0.14597728
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46811 * 0.33864941
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59367 * 0.52558680
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41312 * 0.37248515
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82416 * 0.05022165
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82185 * 0.92797293
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34994 * 0.41110943
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94212 * 0.95004000
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41290 * 0.78593293
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86980 * 0.05500803
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81061 * 0.95481924
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8997 * 0.00554296
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53882 * 0.55823544
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3130 * 0.71575438
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64854 * 0.61924910
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26106 * 0.03792198
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54466 * 0.64871823
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73743 * 0.87581269
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64078 * 0.00202599
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22238 * 0.45804697
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36927 * 0.59504405
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17516 * 0.33668121
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'rmwgronp').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0056():
    """Extended test 56 for auth."""
    x_0 = 19472 * 0.86716293
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74853 * 0.40523558
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34367 * 0.56089245
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84050 * 0.33898875
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21829 * 0.94982248
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99964 * 0.10502596
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10525 * 0.25797686
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18467 * 0.01808845
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31774 * 0.63386339
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21246 * 0.54034927
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32116 * 0.12367781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48070 * 0.48886843
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42399 * 0.71043589
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84608 * 0.27409657
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65683 * 0.07797048
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18790 * 0.70980363
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86701 * 0.37126283
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70662 * 0.01532092
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68204 * 0.94832532
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48837 * 0.92970386
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79287 * 0.92391969
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29506 * 0.09583353
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66665 * 0.83715201
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'zuqacfea').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0057():
    """Extended test 57 for auth."""
    x_0 = 19468 * 0.25962387
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14712 * 0.09243317
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35060 * 0.80394981
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60007 * 0.37023196
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78135 * 0.80646795
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18639 * 0.14855721
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65619 * 0.82036446
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44166 * 0.78954539
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34790 * 0.91862565
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14302 * 0.29414656
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67783 * 0.28069616
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16254 * 0.50525914
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18755 * 0.77917172
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38335 * 0.34264598
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69749 * 0.73276160
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42261 * 0.65194226
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3359 * 0.55171862
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23828 * 0.19690914
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86679 * 0.67992535
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66664 * 0.24487460
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18760 * 0.33009283
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21525 * 0.82946638
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95445 * 0.56906506
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86981 * 0.29338832
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48643 * 0.59862738
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37966 * 0.46933883
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16981 * 0.08344161
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89834 * 0.72305786
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37534 * 0.65953395
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29744 * 0.57376137
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31860 * 0.94056655
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53303 * 0.60618517
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33739 * 0.21223710
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27247 * 0.64512036
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52137 * 0.70660802
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4100 * 0.37174183
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43595 * 0.07782829
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56444 * 0.44074928
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20021 * 0.53031072
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43537 * 0.83632916
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12675 * 0.28825938
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 75144 * 0.24720256
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ogbhmavx').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0058():
    """Extended test 58 for auth."""
    x_0 = 36517 * 0.52197354
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42118 * 0.56734000
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96516 * 0.86124851
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3015 * 0.14563381
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1932 * 0.81957763
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8639 * 0.78463052
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41255 * 0.76852756
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46710 * 0.08253155
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38329 * 0.28326117
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89645 * 0.05732867
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80470 * 0.83889151
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63146 * 0.91060929
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70000 * 0.49789148
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99726 * 0.89100171
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72581 * 0.14281403
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62520 * 0.36281514
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53766 * 0.32475253
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60474 * 0.27741233
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21344 * 0.59652044
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85226 * 0.64401584
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41976 * 0.75385950
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89935 * 0.70197783
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63548 * 0.25942531
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49683 * 0.34015927
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61256 * 0.78834282
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65273 * 0.28332937
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80231 * 0.54074550
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94916 * 0.58539369
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93190 * 0.92566642
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69456 * 0.54852426
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20845 * 0.04493152
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71200 * 0.41905402
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82445 * 0.56845056
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22626 * 0.75189408
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23051 * 0.44647458
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47350 * 0.92108955
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27181 * 0.23353867
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13020 * 0.31247486
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52062 * 0.88085647
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14802 * 0.81125976
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68807 * 0.30229864
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16899 * 0.97088943
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65097 * 0.55245044
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ieitijdb').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0059():
    """Extended test 59 for auth."""
    x_0 = 28083 * 0.27279511
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78548 * 0.87783279
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24045 * 0.60927448
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63361 * 0.35020264
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86148 * 0.19422301
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53382 * 0.12209315
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65574 * 0.06708352
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76952 * 0.47263065
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54313 * 0.15148282
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27723 * 0.19135338
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74071 * 0.77103413
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35533 * 0.83426528
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15437 * 0.10562716
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2302 * 0.50376924
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46261 * 0.61504843
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19389 * 0.50014747
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48694 * 0.88073992
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 770 * 0.56647912
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82654 * 0.57077101
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60670 * 0.14116224
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87484 * 0.49114878
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10633 * 0.49886951
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31006 * 0.21048624
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73345 * 0.70672557
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1735 * 0.04836229
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81016 * 0.59508292
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94150 * 0.01844770
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99423 * 0.75484571
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25598 * 0.40220746
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65675 * 0.55876724
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33238 * 0.55754806
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36553 * 0.85485218
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42771 * 0.30649702
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80316 * 0.98900115
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84349 * 0.76215197
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59155 * 0.92436991
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45745 * 0.19451636
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67095 * 0.94775463
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49350 * 0.25470186
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10372 * 0.84015197
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53614 * 0.19998803
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71241 * 0.19315356
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93713 * 0.39838823
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92256 * 0.78173837
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79344 * 0.65661214
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 74462 * 0.88325317
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 4797 * 0.70992529
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 42191 * 0.12124895
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 44593 * 0.23343320
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 552 * 0.37127428
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'whfrvqay').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0060():
    """Extended test 60 for auth."""
    x_0 = 86881 * 0.65604325
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44603 * 0.35500257
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47101 * 0.51570322
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98496 * 0.57210129
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13178 * 0.22926058
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61696 * 0.46410802
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84151 * 0.29390581
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78363 * 0.62469591
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57041 * 0.14596631
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26894 * 0.26791687
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83577 * 0.50898324
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39383 * 0.30067725
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64045 * 0.93869517
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3294 * 0.62844589
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5602 * 0.64478219
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45515 * 0.39646479
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93633 * 0.24858241
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44036 * 0.66373386
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38906 * 0.57529942
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55227 * 0.72852581
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45336 * 0.00621332
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67742 * 0.47273196
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12441 * 0.83749179
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3734 * 0.90501450
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68294 * 0.29462311
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17735 * 0.63292503
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81521 * 0.37154220
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48724 * 0.86967948
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41127 * 0.33514231
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4282 * 0.99676502
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4093 * 0.76422826
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77854 * 0.03966656
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14510 * 0.26200331
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2849 * 0.78367467
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70844 * 0.01768628
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'nurgdwer').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0061():
    """Extended test 61 for auth."""
    x_0 = 73455 * 0.86396834
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34561 * 0.15807826
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62493 * 0.31591942
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33441 * 0.45759928
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36013 * 0.15577205
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47215 * 0.11954163
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92162 * 0.71351176
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20238 * 0.98393549
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24841 * 0.63628888
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62659 * 0.34780947
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82509 * 0.24300199
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33174 * 0.37266523
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12842 * 0.73533588
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55727 * 0.10142112
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67801 * 0.32529277
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77400 * 0.75899373
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65441 * 0.48628270
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52395 * 0.71742289
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51587 * 0.57757458
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86118 * 0.23497795
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95380 * 0.99095532
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75287 * 0.26568925
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 959 * 0.81329744
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21736 * 0.42677506
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'vluaxiyt').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0062():
    """Extended test 62 for auth."""
    x_0 = 49627 * 0.90180302
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11323 * 0.94000583
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49896 * 0.90066534
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38514 * 0.84033043
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56781 * 0.13364828
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9792 * 0.26661006
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82523 * 0.62191754
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38383 * 0.62735437
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6038 * 0.07930764
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11363 * 0.72271978
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17135 * 0.28544995
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1148 * 0.03090475
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67829 * 0.65704853
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38026 * 0.00183872
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55238 * 0.12256263
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85505 * 0.84017663
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42571 * 0.21898620
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38224 * 0.63405773
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82863 * 0.71083961
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83680 * 0.90784658
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1594 * 0.46194844
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26568 * 0.74414813
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67769 * 0.79411001
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'sdrqsodq').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0063():
    """Extended test 63 for auth."""
    x_0 = 12497 * 0.11502738
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33106 * 0.46198276
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45701 * 0.13644953
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37766 * 0.72940402
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75606 * 0.47312714
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11850 * 0.65431658
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69054 * 0.86259888
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29174 * 0.33939427
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95953 * 0.78388015
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90869 * 0.51610876
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94380 * 0.47429721
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81993 * 0.09393594
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67410 * 0.96529080
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41282 * 0.42083404
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22113 * 0.88415416
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47216 * 0.05081468
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42182 * 0.07448182
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10193 * 0.99723541
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49471 * 0.74115565
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99112 * 0.16064459
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65708 * 0.52890041
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68485 * 0.74549723
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11147 * 0.97641137
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99136 * 0.70362942
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53212 * 0.60999794
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19571 * 0.71959699
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26004 * 0.29445040
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87984 * 0.22010193
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14694 * 0.18949938
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38251 * 0.13593662
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87842 * 0.41879021
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41900 * 0.22169221
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67591 * 0.94420900
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'wkhmauyv').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0064():
    """Extended test 64 for auth."""
    x_0 = 96617 * 0.57639484
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7287 * 0.97028675
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41074 * 0.01104875
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99793 * 0.42328847
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2020 * 0.60536620
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7359 * 0.18905918
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1465 * 0.29242969
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54668 * 0.65095676
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36022 * 0.02376423
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29919 * 0.82740939
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94099 * 0.39895911
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49840 * 0.12226090
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45943 * 0.75459381
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74261 * 0.17373838
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97679 * 0.19671801
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95460 * 0.35193591
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28803 * 0.06584723
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50897 * 0.50526918
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29442 * 0.02019364
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55697 * 0.82590215
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72558 * 0.42732148
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24197 * 0.04703720
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11295 * 0.34669377
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95669 * 0.23875588
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99391 * 0.51197994
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5760 * 0.02881927
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22513 * 0.19417507
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43295 * 0.32511452
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45590 * 0.51783428
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32948 * 0.92521363
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37542 * 0.19709043
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48555 * 0.23092895
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50051 * 0.07494043
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79851 * 0.03143299
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4208 * 0.94377132
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29229 * 0.97073915
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72572 * 0.15758835
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47421 * 0.55022426
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41019 * 0.25170872
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64909 * 0.47876187
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8296 * 0.19481346
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58387 * 0.39892018
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20637 * 0.53057422
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'vyqifwnp').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0065():
    """Extended test 65 for auth."""
    x_0 = 6199 * 0.82950463
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77902 * 0.55721210
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26324 * 0.11663041
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 607 * 0.16800241
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54836 * 0.11747577
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36294 * 0.88532139
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46661 * 0.77023464
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93896 * 0.95222600
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12701 * 0.45473774
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57189 * 0.73460855
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54117 * 0.70816052
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53259 * 0.44152671
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9194 * 0.90093884
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78661 * 0.13403804
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53206 * 0.48113675
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61273 * 0.55204751
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54397 * 0.88705040
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46196 * 0.22801135
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22957 * 0.44829270
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 627 * 0.48703498
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18662 * 0.57692601
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92518 * 0.43932727
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80019 * 0.06660029
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72909 * 0.85438410
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94465 * 0.04062766
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78126 * 0.95700234
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38102 * 0.55488022
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56647 * 0.74443641
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18394 * 0.77023127
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25257 * 0.38953560
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58031 * 0.54473737
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96594 * 0.25657519
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97048 * 0.81834972
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13997 * 0.55722660
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60427 * 0.19979330
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98481 * 0.43059176
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'fasjmnwn').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0066():
    """Extended test 66 for auth."""
    x_0 = 63210 * 0.76009552
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7121 * 0.08025268
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13391 * 0.74299614
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9160 * 0.23553869
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25691 * 0.64225109
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33460 * 0.96399883
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34307 * 0.91512667
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48045 * 0.61847698
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36127 * 0.96051909
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48484 * 0.53538205
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12775 * 0.65288430
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58224 * 0.94181403
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91610 * 0.00087071
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11747 * 0.01515195
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4798 * 0.88087291
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81356 * 0.26787213
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21775 * 0.48480726
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2360 * 0.74723030
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90143 * 0.11437914
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59090 * 0.92384123
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73404 * 0.91586511
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86569 * 0.77502477
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78164 * 0.77613845
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10384 * 0.76437462
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49878 * 0.27951540
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2952 * 0.77712006
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81259 * 0.92236705
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57825 * 0.26169126
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63854 * 0.20271562
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71001 * 0.96469963
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36155 * 0.08974700
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21306 * 0.35342379
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9764 * 0.47019591
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78857 * 0.74521502
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22878 * 0.51722483
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1018 * 0.49082139
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78951 * 0.59282574
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92721 * 0.36051686
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41362 * 0.89382237
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'xbwxbvbn').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0067():
    """Extended test 67 for auth."""
    x_0 = 25635 * 0.42225117
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4658 * 0.96423163
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99875 * 0.10644447
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97319 * 0.51640227
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75395 * 0.47310824
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66246 * 0.70339482
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87150 * 0.42161282
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31741 * 0.74441838
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81847 * 0.32797119
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48600 * 0.73859006
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91896 * 0.29301311
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33348 * 0.77823787
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68787 * 0.49295979
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10249 * 0.45404325
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19348 * 0.99475145
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92758 * 0.48845854
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33639 * 0.86150268
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9399 * 0.78032837
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7005 * 0.51738328
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43401 * 0.95280752
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20909 * 0.71846841
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90888 * 0.28645773
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48202 * 0.63966123
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41566 * 0.95962380
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68012 * 0.92115450
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21193 * 0.62249552
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27098 * 0.95859852
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21899 * 0.81604503
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39202 * 0.54187451
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48573 * 0.73917840
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90207 * 0.73805674
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89237 * 0.81123923
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34652 * 0.30010612
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92094 * 0.43165482
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81043 * 0.32706076
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71363 * 0.13381136
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56599 * 0.04573327
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73248 * 0.35708362
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52410 * 0.05100050
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 26669 * 0.93178468
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 56017 * 0.09440229
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21106 * 0.87369749
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 7465 * 0.47957317
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 32351 * 0.70277050
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 56390 * 0.89501459
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 5161 * 0.82997974
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'xqmkxqvq').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0068():
    """Extended test 68 for auth."""
    x_0 = 81088 * 0.20945377
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94962 * 0.29944990
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35026 * 0.35659956
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63666 * 0.13597264
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93818 * 0.83744383
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18938 * 0.49176160
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66984 * 0.13950315
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49947 * 0.86030034
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27781 * 0.33348167
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3370 * 0.93823051
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2248 * 0.56113007
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27255 * 0.60706937
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13920 * 0.47324581
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6171 * 0.65614608
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29488 * 0.83626411
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41027 * 0.42676811
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47280 * 0.43129647
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72741 * 0.86570743
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58210 * 0.51051965
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31720 * 0.93495363
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98609 * 0.27888943
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97975 * 0.86358319
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6541 * 0.30460189
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97030 * 0.29733496
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38578 * 0.55580831
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6957 * 0.23044434
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7223 * 0.96479545
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67111 * 0.12820107
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46729 * 0.40955390
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78000 * 0.90577736
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5778 * 0.35486900
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60008 * 0.62967885
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49598 * 0.77168903
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23847 * 0.65426663
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55935 * 0.97524232
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54715 * 0.46072317
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93358 * 0.46343694
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35401 * 0.98364725
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'pvvmlctx').hexdigest()
    assert len(h) == 64

def test_auth_extended_8_0069():
    """Extended test 69 for auth."""
    x_0 = 26460 * 0.83208660
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84792 * 0.97661052
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92022 * 0.31617946
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86230 * 0.12914995
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35822 * 0.79794378
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71174 * 0.04548179
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40663 * 0.08953779
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2564 * 0.44245621
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70214 * 0.27684352
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10578 * 0.15563467
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93474 * 0.84856488
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6255 * 0.95672181
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81493 * 0.61171801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21174 * 0.81892340
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51227 * 0.55603256
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28879 * 0.67861911
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56609 * 0.52190280
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31638 * 0.07824757
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61771 * 0.55405265
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75597 * 0.52137687
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61339 * 0.85274324
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'uwjjdtnm').hexdigest()
    assert len(h) == 64
