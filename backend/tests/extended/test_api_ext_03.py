"""Extended tests for api suite 3."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_api_extended_3_0000():
    """Extended test 0 for api."""
    x_0 = 99716 * 0.16288017
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84130 * 0.07023298
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80268 * 0.13125777
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41082 * 0.42688767
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44497 * 0.30033502
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44532 * 0.44264554
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1405 * 0.48146901
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17005 * 0.81537691
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31494 * 0.44266679
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90614 * 0.11850649
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36515 * 0.57989945
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94090 * 0.14730782
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37009 * 0.97325258
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23159 * 0.62974005
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25972 * 0.51253946
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6844 * 0.96726233
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20722 * 0.78597290
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51524 * 0.57184949
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21225 * 0.48926161
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66251 * 0.30527923
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90188 * 0.02779344
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55335 * 0.26019607
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7784 * 0.02577260
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82121 * 0.36937085
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55003 * 0.14849208
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54767 * 0.09797876
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67981 * 0.45094107
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39759 * 0.95075231
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1104 * 0.37647411
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57109 * 0.30875400
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88618 * 0.95664802
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43730 * 0.76476118
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52225 * 0.01553043
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61838 * 0.67574459
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93051 * 0.80607217
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87089 * 0.20836226
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76811 * 0.05750338
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42225 * 0.54162589
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4787 * 0.80287326
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84726 * 0.34693437
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78796 * 0.50332475
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 90409 * 0.48767476
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'plroczmj').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0001():
    """Extended test 1 for api."""
    x_0 = 1079 * 0.24134731
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46309 * 0.27921999
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58087 * 0.60037553
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41835 * 0.48957195
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32353 * 0.28343729
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88102 * 0.99140012
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93535 * 0.60781309
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77181 * 0.21865060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60607 * 0.55030510
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7032 * 0.58989562
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98472 * 0.51038630
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98589 * 0.46542903
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 512 * 0.44679179
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66952 * 0.98798958
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26856 * 0.88699344
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5586 * 0.79481774
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25543 * 0.55981311
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72094 * 0.49832475
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90523 * 0.50332748
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21340 * 0.46642174
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91155 * 0.64454129
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46206 * 0.07964361
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44826 * 0.62852886
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21492 * 0.81866057
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87973 * 0.44985053
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42402 * 0.52066769
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84341 * 0.77419283
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50176 * 0.96054684
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48970 * 0.58259614
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58318 * 0.21686869
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5541 * 0.52730930
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19851 * 0.16327666
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23194 * 0.57604379
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73810 * 0.96984895
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24194 * 0.54369192
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26185 * 0.76323011
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14868 * 0.10139387
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52600 * 0.30506959
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56779 * 0.89081914
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9196 * 0.01424574
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 16999 * 0.80486580
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93752 * 0.34034957
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 49553 * 0.96905709
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 54900 * 0.12667012
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 42479 * 0.31044218
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 93245 * 0.85610487
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 79412 * 0.57967701
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 61649 * 0.60274031
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ehhkipbn').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0002():
    """Extended test 2 for api."""
    x_0 = 22680 * 0.99819385
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75886 * 0.42022768
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29965 * 0.19904327
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72102 * 0.26827136
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10114 * 0.78796139
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93152 * 0.04450042
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19932 * 0.88845017
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92844 * 0.05878457
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78340 * 0.33449794
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76582 * 0.00170141
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90012 * 0.92409236
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81249 * 0.34001224
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1101 * 0.53795066
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39579 * 0.17395385
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10335 * 0.64764255
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33737 * 0.53123283
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87937 * 0.94590362
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24451 * 0.48686480
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29599 * 0.70190894
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36038 * 0.31744358
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46643 * 0.09757646
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82958 * 0.90723751
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36944 * 0.21776745
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86415 * 0.01949168
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46065 * 0.56469947
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11583 * 0.06771298
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35086 * 0.72361799
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17926 * 0.65164633
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9183 * 0.15015020
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74442 * 0.03883652
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75111 * 0.76016750
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48408 * 0.38588422
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53442 * 0.42084513
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68045 * 0.86283364
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96051 * 0.68965986
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85886 * 0.59790722
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36297 * 0.86247452
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15355 * 0.34634754
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56192 * 0.48919935
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22237 * 0.87906087
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13479 * 0.73203008
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 86511 * 0.15957356
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 37565 * 0.72403689
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'glpjmdrn').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0003():
    """Extended test 3 for api."""
    x_0 = 39651 * 0.98804712
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27541 * 0.72807514
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14266 * 0.14726704
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52230 * 0.22667613
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6247 * 0.68055627
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72215 * 0.08022715
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15034 * 0.96350842
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70677 * 0.29768639
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31309 * 0.35213021
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26594 * 0.24048967
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69332 * 0.00134455
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70646 * 0.41500712
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14894 * 0.53607008
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96917 * 0.62215585
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23757 * 0.05808463
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25 * 0.66538710
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74988 * 0.06618770
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 400 * 0.54527538
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49155 * 0.81596317
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1841 * 0.99337639
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21061 * 0.27977579
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35551 * 0.78082961
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6777 * 0.33387764
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98595 * 0.18989019
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87391 * 0.40551782
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90919 * 0.83113910
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33521 * 0.36793178
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42079 * 0.64929227
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18047 * 0.20005000
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62468 * 0.02336021
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61825 * 0.99855970
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52598 * 0.91567823
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84134 * 0.66257886
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36303 * 0.88381067
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52574 * 0.60541139
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75361 * 0.27344642
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29252 * 0.70358449
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58921 * 0.68670349
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'rtkdfwif').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0004():
    """Extended test 4 for api."""
    x_0 = 89771 * 0.21777976
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2094 * 0.78782796
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28784 * 0.35753778
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47311 * 0.24748519
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98260 * 0.03887011
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98345 * 0.53598747
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61363 * 0.40145544
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61971 * 0.83180710
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62053 * 0.68327684
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79371 * 0.90395153
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24319 * 0.94251784
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67804 * 0.72157713
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83646 * 0.02753953
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96337 * 0.38505933
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24246 * 0.76865281
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52432 * 0.22649027
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53990 * 0.53851415
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73180 * 0.51340999
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2983 * 0.14601770
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64503 * 0.79660617
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'fhoxnemo').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0005():
    """Extended test 5 for api."""
    x_0 = 72084 * 0.08272798
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31375 * 0.24036951
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71659 * 0.20420998
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84731 * 0.46176751
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40790 * 0.35023240
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8124 * 0.19809345
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36627 * 0.47523483
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47880 * 0.61977896
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91076 * 0.18151752
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94084 * 0.17712423
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40000 * 0.32598826
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28958 * 0.70771660
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52741 * 0.74675665
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42247 * 0.20357198
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 281 * 0.01243738
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84521 * 0.60825306
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63812 * 0.61698769
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14309 * 0.96756135
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17504 * 0.25685931
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12812 * 0.28978134
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51807 * 0.17619857
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58203 * 0.73122789
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15020 * 0.37621563
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84742 * 0.22621929
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86329 * 0.89017729
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76599 * 0.64763433
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80791 * 0.61925079
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65532 * 0.47456563
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19304 * 0.21849547
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30050 * 0.54618636
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5164 * 0.34194688
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25703 * 0.35165345
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8192 * 0.74763900
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89846 * 0.43652493
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 491 * 0.27991162
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7815 * 0.39748380
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5599 * 0.37556908
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66790 * 0.50963672
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13741 * 0.75541315
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81785 * 0.64770463
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91405 * 0.74173959
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38217 * 0.08071281
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42978 * 0.89297536
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 29636 * 0.07047940
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71672 * 0.48824841
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 50986 * 0.31562173
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 79092 * 0.60019419
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 30699 * 0.40346570
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 4080 * 0.46517905
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 74397 * 0.51366014
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'kighvynl').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0006():
    """Extended test 6 for api."""
    x_0 = 7817 * 0.77125920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34588 * 0.68334271
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29121 * 0.47670258
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29137 * 0.83485431
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86163 * 0.72612713
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75609 * 0.79897225
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52757 * 0.41689385
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4790 * 0.69156354
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91532 * 0.22655217
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33675 * 0.95972182
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30238 * 0.98525667
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64103 * 0.43915149
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64635 * 0.85368549
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9545 * 0.78921486
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46283 * 0.30834544
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6394 * 0.24201392
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20499 * 0.73183922
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59846 * 0.41996747
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66897 * 0.88537192
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40222 * 0.02057676
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58554 * 0.30474788
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44952 * 0.23073326
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56162 * 0.67607088
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94190 * 0.84648180
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98714 * 0.56183492
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29724 * 0.04309149
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'fngbdfyt').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0007():
    """Extended test 7 for api."""
    x_0 = 68951 * 0.52881258
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91733 * 0.47799608
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70346 * 0.93964688
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67634 * 0.90613968
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29019 * 0.37729771
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49050 * 0.05168795
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58210 * 0.51868528
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5809 * 0.86881830
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44434 * 0.10338937
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27031 * 0.82048111
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34356 * 0.50245521
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 742 * 0.64877062
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45291 * 0.44295870
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94182 * 0.82936962
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76858 * 0.94499704
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69174 * 0.33348481
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3198 * 0.83651371
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53457 * 0.47955077
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12224 * 0.35820114
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48013 * 0.64478873
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29385 * 0.75447507
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53229 * 0.62572280
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60709 * 0.58995051
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88646 * 0.73650001
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39313 * 0.72938585
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88963 * 0.62521634
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51414 * 0.76232816
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17983 * 0.62519121
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97697 * 0.51969225
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8899 * 0.37326318
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47042 * 0.71704179
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3791 * 0.82319502
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'awvoemsx').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0008():
    """Extended test 8 for api."""
    x_0 = 78918 * 0.58440793
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81821 * 0.57505565
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78163 * 0.24011765
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61817 * 0.88783806
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30543 * 0.96533510
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12494 * 0.23285536
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81988 * 0.83634832
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91203 * 0.93994769
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88918 * 0.79107681
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16600 * 0.69442281
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20639 * 0.84984483
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43743 * 0.25961369
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12573 * 0.78308901
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28713 * 0.31717128
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85022 * 0.94211464
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23315 * 0.73199055
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44938 * 0.64789620
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97368 * 0.20705887
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43456 * 0.35244395
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14155 * 0.20186227
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46352 * 0.33173785
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11150 * 0.65716853
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69656 * 0.13463365
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17903 * 0.42938523
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9187 * 0.87687580
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95048 * 0.99944051
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87383 * 0.93603666
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79295 * 0.58408105
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37840 * 0.22876854
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77193 * 0.68954717
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67324 * 0.50714084
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46712 * 0.90219780
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38139 * 0.20450190
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16100 * 0.32145220
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'qshxgqjj').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0009():
    """Extended test 9 for api."""
    x_0 = 401 * 0.02382647
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70902 * 0.38107585
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51795 * 0.27252072
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93721 * 0.96192312
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58642 * 0.84442219
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27947 * 0.62533471
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3284 * 0.77140165
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50184 * 0.74467342
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35304 * 0.50550522
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56986 * 0.10174219
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38373 * 0.78332643
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83784 * 0.15264899
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78981 * 0.83767970
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47401 * 0.26385269
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29766 * 0.94070177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53613 * 0.27015093
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35367 * 0.21026874
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95297 * 0.83981946
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19523 * 0.04422686
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29123 * 0.72938099
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95266 * 0.70049470
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10876 * 0.73998155
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95981 * 0.37266275
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43134 * 0.64690976
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62724 * 0.30050708
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44346 * 0.42562654
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25055 * 0.04692020
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20098 * 0.72143394
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66385 * 0.21805483
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86667 * 0.07347497
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70897 * 0.43154155
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36084 * 0.50483289
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43462 * 0.70120716
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42661 * 0.52097925
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88223 * 0.66104216
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98359 * 0.55504602
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95089 * 0.48089621
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5665 * 0.07987690
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56538 * 0.74832571
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31194 * 0.21614085
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 25253 * 0.77389978
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13534 * 0.03187543
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12822 * 0.93462016
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22820 * 0.16049369
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 88046 * 0.27981032
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 8581 * 0.08633381
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 37507 * 0.32540697
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'mlsjfdgb').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0010():
    """Extended test 10 for api."""
    x_0 = 65387 * 0.64637825
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64142 * 0.19215414
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63067 * 0.95935600
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1540 * 0.93854155
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88694 * 0.43664819
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95219 * 0.80826818
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36476 * 0.37784956
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48589 * 0.82926445
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7027 * 0.32561908
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38338 * 0.91097512
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94516 * 0.85305540
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14862 * 0.25281270
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63006 * 0.77811569
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51933 * 0.33711561
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43478 * 0.16315352
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56599 * 0.13629563
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94573 * 0.85192915
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76218 * 0.24884415
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94496 * 0.86064714
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50131 * 0.21392721
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45605 * 0.71152832
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48269 * 0.80446833
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15465 * 0.20607278
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13780 * 0.64922388
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17020 * 0.59624102
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17194 * 0.89735224
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35003 * 0.63786043
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36181 * 0.40067331
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66755 * 0.68876296
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26728 * 0.99741269
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60867 * 0.48111071
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62727 * 0.72450161
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76380 * 0.73787408
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54112 * 0.05539295
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'jaonesbz').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0011():
    """Extended test 11 for api."""
    x_0 = 6502 * 0.29962754
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30114 * 0.09503710
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58543 * 0.00272307
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43808 * 0.48012857
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76591 * 0.26358871
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75204 * 0.20805177
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44139 * 0.23339271
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48836 * 0.61702118
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14126 * 0.64354557
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74648 * 0.99496784
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29683 * 0.89515309
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16224 * 0.47089325
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1372 * 0.38265520
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49025 * 0.91242161
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79687 * 0.51889664
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5252 * 0.77763796
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44385 * 0.80540363
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33010 * 0.70970957
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10471 * 0.47249847
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97465 * 0.00223022
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62655 * 0.43058292
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49883 * 0.33675649
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'dhzkhrig').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0012():
    """Extended test 12 for api."""
    x_0 = 23157 * 0.20540001
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72688 * 0.01332732
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97431 * 0.40244974
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24979 * 0.01097893
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14375 * 0.74201681
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96071 * 0.99730442
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18133 * 0.78021156
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97565 * 0.92368576
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90202 * 0.38339615
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82806 * 0.29644630
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27303 * 0.03716678
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47097 * 0.52885544
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20497 * 0.85388400
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94940 * 0.68642652
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88572 * 0.47446011
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67120 * 0.45884172
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77618 * 0.90046371
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72676 * 0.52650231
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20851 * 0.50515693
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30146 * 0.60187847
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87889 * 0.63014352
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79219 * 0.68252035
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85777 * 0.61323392
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60264 * 0.40902315
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8217 * 0.25205396
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66075 * 0.61952708
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 561 * 0.31732575
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16587 * 0.30721018
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49791 * 0.00943211
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91300 * 0.51677421
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13709 * 0.70921923
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19777 * 0.22781017
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 755 * 0.05611491
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60397 * 0.65983739
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19714 * 0.60586193
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36142 * 0.26304559
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42952 * 0.07217270
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87520 * 0.83572859
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93980 * 0.53883565
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30849 * 0.26352836
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1782 * 0.14614799
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66372 * 0.52475869
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9605 * 0.32440092
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75899 * 0.47380418
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35927 * 0.49682359
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 21785 * 0.01451672
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 26491 * 0.32527976
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 50282 * 0.03544734
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 86776 * 0.19928773
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 86281 * 0.65614943
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'eyetogfw').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0013():
    """Extended test 13 for api."""
    x_0 = 69455 * 0.34254881
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66721 * 0.05122447
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50348 * 0.14620603
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29927 * 0.55213135
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86042 * 0.45614183
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11596 * 0.96104965
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15056 * 0.93978261
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76179 * 0.08085665
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74815 * 0.79842962
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83635 * 0.46009390
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22421 * 0.67246209
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55067 * 0.28254231
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9641 * 0.21859077
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52583 * 0.76809456
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22034 * 0.59846841
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66496 * 0.99261524
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43055 * 0.80177054
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43623 * 0.51035079
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47602 * 0.69530345
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79578 * 0.28643776
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2928 * 0.61363814
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31443 * 0.42897616
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13510 * 0.73142201
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62773 * 0.85430279
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79364 * 0.88190357
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23835 * 0.12800857
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29514 * 0.49594365
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63508 * 0.37057039
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29580 * 0.54425311
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15806 * 0.60609990
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10376 * 0.45487902
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68887 * 0.35866525
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14001 * 0.14448759
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56285 * 0.92167975
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60142 * 0.82400745
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18956 * 0.12594638
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41323 * 0.88239052
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93719 * 0.13032389
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87286 * 0.46389573
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'tzblpylj').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0014():
    """Extended test 14 for api."""
    x_0 = 46304 * 0.99317831
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38332 * 0.51539721
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91613 * 0.69666672
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2640 * 0.06983350
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45539 * 0.27585277
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77283 * 0.66936706
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52115 * 0.97590668
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55605 * 0.53015225
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96804 * 0.13048117
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72685 * 0.91922187
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17600 * 0.65285358
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70877 * 0.82241207
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31442 * 0.09274667
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83297 * 0.05322829
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31740 * 0.96942570
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51620 * 0.26475165
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41859 * 0.49520355
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73596 * 0.67811349
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97433 * 0.96798903
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 171 * 0.06993492
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35977 * 0.62424096
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27695 * 0.26647446
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8348 * 0.28978075
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4641 * 0.72274098
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60279 * 0.67418795
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'xerftfes').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0015():
    """Extended test 15 for api."""
    x_0 = 45179 * 0.46290520
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72499 * 0.83674989
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31972 * 0.99547990
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60910 * 0.75590591
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89959 * 0.80762330
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95218 * 0.01550190
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70157 * 0.06306775
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76839 * 0.87554247
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68476 * 0.80906236
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6081 * 0.57986403
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65194 * 0.16096280
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44414 * 0.95489207
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25719 * 0.60948054
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68673 * 0.07852296
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70101 * 0.76047007
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20252 * 0.15031401
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51071 * 0.32248054
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62966 * 0.67844380
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86764 * 0.37738491
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35383 * 0.27268449
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2075 * 0.47668720
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 284 * 0.87377855
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82625 * 0.74925706
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89131 * 0.39784435
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69453 * 0.57456301
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47551 * 0.84816834
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53007 * 0.65710731
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73502 * 0.06489642
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84585 * 0.19822929
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78522 * 0.25904487
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1278 * 0.47508749
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66236 * 0.40152816
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89350 * 0.71912205
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87555 * 0.19115188
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44867 * 0.70766159
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91091 * 0.85639478
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96086 * 0.04172305
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'ohwmpktp').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0016():
    """Extended test 16 for api."""
    x_0 = 38362 * 0.21942258
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40675 * 0.81140319
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19791 * 0.46877213
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72791 * 0.00190535
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53415 * 0.72038058
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98557 * 0.99835272
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65827 * 0.83066282
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41824 * 0.82847571
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10864 * 0.17481139
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4229 * 0.24510837
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35900 * 0.44633814
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79398 * 0.79034772
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83652 * 0.85127335
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46514 * 0.91607665
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80211 * 0.42256943
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15948 * 0.92788485
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19121 * 0.99820472
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14741 * 0.70188838
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46825 * 0.48931730
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28691 * 0.95403437
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11137 * 0.25520824
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29468 * 0.92139936
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46993 * 0.61405814
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88352 * 0.45764068
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69489 * 0.81300682
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63326 * 0.72058090
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1462 * 0.69189619
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45415 * 0.41794478
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99636 * 0.29613457
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60122 * 0.21543404
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38989 * 0.47027336
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74773 * 0.76656761
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93496 * 0.05946558
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22946 * 0.26767056
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85263 * 0.69830950
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 72700 * 0.68169669
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56969 * 0.99509072
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'gznjnngx').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0017():
    """Extended test 17 for api."""
    x_0 = 56499 * 0.80954912
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89593 * 0.87445316
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82208 * 0.17270671
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53416 * 0.11427063
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97400 * 0.36351190
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21922 * 0.32883816
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15106 * 0.29878306
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22941 * 0.28854433
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16250 * 0.55754480
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34310 * 0.31188728
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64746 * 0.69346739
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86740 * 0.03369566
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17977 * 0.32989591
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59071 * 0.96417832
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99928 * 0.48514724
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16256 * 0.15766971
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3245 * 0.23894671
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39188 * 0.53932441
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7997 * 0.14177338
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67465 * 0.88452864
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12192 * 0.75927441
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33965 * 0.67028683
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79822 * 0.20762046
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91072 * 0.66142919
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50267 * 0.68776233
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86164 * 0.81626027
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48871 * 0.16345661
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26999 * 0.95401302
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65548 * 0.96066369
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'znulwebv').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0018():
    """Extended test 18 for api."""
    x_0 = 87197 * 0.00617443
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64852 * 0.72957114
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45823 * 0.66365007
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38580 * 0.89260178
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94132 * 0.76685108
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13480 * 0.65968695
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99678 * 0.78524258
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61344 * 0.93777800
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76755 * 0.95177829
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29078 * 0.24177433
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58031 * 0.74317288
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59028 * 0.14830768
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4175 * 0.61013359
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94688 * 0.20113761
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25189 * 0.85328813
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79922 * 0.78502893
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10063 * 0.80285028
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39247 * 0.01671421
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12510 * 0.09480381
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72867 * 0.29571957
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28942 * 0.60863647
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8391 * 0.93279796
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11778 * 0.46676399
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50675 * 0.83688022
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4083 * 0.41951639
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2333 * 0.18953064
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11301 * 0.42131625
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94440 * 0.17054448
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75971 * 0.36470230
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90222 * 0.63248913
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86241 * 0.22610177
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93064 * 0.97132933
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'sidwsjol').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0019():
    """Extended test 19 for api."""
    x_0 = 39693 * 0.06660527
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97095 * 0.49292026
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37923 * 0.66127709
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81932 * 0.23896905
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86970 * 0.62935593
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76930 * 0.59675594
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69673 * 0.38302361
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88836 * 0.35642289
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38579 * 0.56861952
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85598 * 0.23691122
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73032 * 0.82604447
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73072 * 0.58429729
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61169 * 0.59272214
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45334 * 0.14771632
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56189 * 0.31599368
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48129 * 0.68699210
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53561 * 0.79863130
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76887 * 0.41589180
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79092 * 0.07977875
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42499 * 0.91203939
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33255 * 0.34510908
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36809 * 0.17443065
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66929 * 0.09384251
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92301 * 0.83642290
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92784 * 0.66275239
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71412 * 0.04271161
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95933 * 0.27384032
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'icksgsnj').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0020():
    """Extended test 20 for api."""
    x_0 = 40579 * 0.79621586
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85471 * 0.48108805
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65097 * 0.32661527
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37779 * 0.18656604
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2111 * 0.49739635
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74446 * 0.27527734
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49706 * 0.25535682
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63995 * 0.74934180
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77880 * 0.04586818
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48960 * 0.95491517
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92796 * 0.57095177
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21421 * 0.62354914
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56403 * 0.24166706
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40304 * 0.16111293
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68716 * 0.22469053
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9494 * 0.77987028
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92800 * 0.39257068
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68799 * 0.36285170
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61419 * 0.27671483
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87926 * 0.72234167
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46813 * 0.96405873
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95395 * 0.20038252
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41752 * 0.26034796
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35150 * 0.24447066
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'gtylumsv').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0021():
    """Extended test 21 for api."""
    x_0 = 13980 * 0.76407525
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93685 * 0.68649142
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51716 * 0.17533009
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95721 * 0.77403343
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87620 * 0.60395021
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41410 * 0.80287213
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83994 * 0.29818713
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79221 * 0.10190979
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44936 * 0.52127038
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35321 * 0.54407169
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69374 * 0.34333166
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68877 * 0.71244451
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87426 * 0.65279926
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13636 * 0.63966956
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42797 * 0.21492852
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24157 * 0.54688727
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9226 * 0.10581600
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58694 * 0.56154693
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14230 * 0.22050162
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89718 * 0.72786124
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18617 * 0.60284372
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78179 * 0.96160234
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45665 * 0.79472468
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91871 * 0.56011520
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69847 * 0.04890700
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65676 * 0.29874794
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4725 * 0.17854629
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47755 * 0.69025472
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27729 * 0.67420236
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59939 * 0.39030390
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57530 * 0.08825929
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17145 * 0.06587411
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35696 * 0.63197965
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6855 * 0.21877569
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40499 * 0.09064707
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60841 * 0.56679450
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49564 * 0.53293140
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64776 * 0.62944124
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18580 * 0.87653915
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ptvbkacy').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0022():
    """Extended test 22 for api."""
    x_0 = 19642 * 0.71527609
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54171 * 0.34009304
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17127 * 0.71784790
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61611 * 0.69614323
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17734 * 0.17850226
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88041 * 0.61676061
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95574 * 0.30207956
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33863 * 0.82221080
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32849 * 0.60350066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53231 * 0.52867506
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66723 * 0.61551400
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75440 * 0.41025175
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30327 * 0.88139074
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92385 * 0.06803625
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86250 * 0.18463001
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83642 * 0.16400692
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71234 * 0.94769018
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31767 * 0.12372287
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82268 * 0.42930122
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20701 * 0.85847800
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35345 * 0.65572139
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79565 * 0.85188249
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95017 * 0.03384451
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77365 * 0.11935063
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89689 * 0.41143111
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6919 * 0.97310912
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73118 * 0.10784184
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43512 * 0.91830424
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16806 * 0.25391069
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1673 * 0.49554464
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86493 * 0.22879344
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48527 * 0.19651771
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79008 * 0.95739042
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31989 * 0.34474154
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54072 * 0.05819328
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62696 * 0.51086515
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70063 * 0.94387679
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38513 * 0.30312669
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39303 * 0.74260743
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22410 * 0.85787864
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84856 * 0.58097815
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14304 * 0.76832417
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 67078 * 0.56470228
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 37547 * 0.02779316
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 7256 * 0.90366102
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 99694 * 0.08016815
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 87572 * 0.60861891
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 47964 * 0.87190607
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 34769 * 0.47885523
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 49067 * 0.06994847
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'wjyflqgl').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0023():
    """Extended test 23 for api."""
    x_0 = 39920 * 0.49826122
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99178 * 0.31245157
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32027 * 0.34800438
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3758 * 0.11813271
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54680 * 0.78390104
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11598 * 0.14231102
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62727 * 0.79573398
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33343 * 0.81338370
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9672 * 0.77947501
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99185 * 0.59734806
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44552 * 0.33280758
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95665 * 0.83083268
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39517 * 0.80470772
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18041 * 0.03904121
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94665 * 0.90854126
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29566 * 0.24448421
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94866 * 0.67872775
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88745 * 0.95114794
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25098 * 0.14371286
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84585 * 0.45776041
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61770 * 0.82299296
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24082 * 0.61394961
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23195 * 0.98279342
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'wwsotcdp').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0024():
    """Extended test 24 for api."""
    x_0 = 22775 * 0.11461129
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72314 * 0.51493526
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91234 * 0.61013523
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79474 * 0.16209492
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39443 * 0.84163183
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64285 * 0.72072374
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95352 * 0.09112137
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25583 * 0.49258112
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72562 * 0.60849455
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84628 * 0.59300290
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13542 * 0.03631575
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52595 * 0.33778672
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7502 * 0.65385516
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37935 * 0.39727158
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3318 * 0.29077142
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13086 * 0.95796220
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12308 * 0.87125735
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70614 * 0.71996496
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59808 * 0.14360246
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69731 * 0.06629496
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62650 * 0.62517837
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'gkusvjfu').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0025():
    """Extended test 25 for api."""
    x_0 = 62676 * 0.19143062
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26035 * 0.97223771
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86820 * 0.51904137
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25217 * 0.57740113
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55816 * 0.89820901
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50716 * 0.27396004
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22844 * 0.40235546
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57828 * 0.40499627
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76761 * 0.82829262
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21075 * 0.59031670
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46011 * 0.99306401
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63035 * 0.25763241
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83751 * 0.48814995
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71134 * 0.12025401
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27759 * 0.16093241
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29809 * 0.49385006
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47826 * 0.14251567
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19408 * 0.36437651
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37006 * 0.71666711
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62815 * 0.92561789
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7848 * 0.22378871
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96996 * 0.46364026
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88087 * 0.48206522
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92648 * 0.80599357
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30436 * 0.31124341
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73021 * 0.94915234
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24295 * 0.69460315
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 338 * 0.86748280
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6446 * 0.31884746
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52066 * 0.18783880
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52665 * 0.10522564
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71530 * 0.41247066
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95018 * 0.83288548
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32974 * 0.09705649
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96290 * 0.87136316
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67328 * 0.87482240
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44605 * 0.23872901
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 14160 * 0.43746751
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53715 * 0.65362122
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 58052 * 0.72510702
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32837 * 0.60877401
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81733 * 0.41916843
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 39342 * 0.68785037
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'gvqhrfjc').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0026():
    """Extended test 26 for api."""
    x_0 = 25220 * 0.99635721
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34137 * 0.10946560
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75609 * 0.52479764
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95492 * 0.51802519
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33888 * 0.54775906
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74139 * 0.28156536
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71746 * 0.49059679
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61545 * 0.78099591
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46619 * 0.82248366
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59866 * 0.94320606
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32103 * 0.06234590
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99885 * 0.33821082
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56147 * 0.71453323
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65637 * 0.47282809
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36977 * 0.05458939
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70494 * 0.78140098
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47601 * 0.42764788
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72631 * 0.50785515
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71341 * 0.45710317
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76277 * 0.06481590
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62566 * 0.84337752
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52552 * 0.48419134
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12360 * 0.30239530
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80173 * 0.70759405
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4485 * 0.69738955
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66383 * 0.12861470
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69280 * 0.26972198
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72592 * 0.04170210
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26198 * 0.81807073
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18395 * 0.44322999
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99373 * 0.40011956
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26212 * 0.89064525
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18315 * 0.36504656
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ceikqohm').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0027():
    """Extended test 27 for api."""
    x_0 = 39809 * 0.12011422
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60413 * 0.73255753
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16474 * 0.83916190
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52431 * 0.10599292
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61203 * 0.96576793
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78800 * 0.99916361
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86682 * 0.09618763
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20552 * 0.70720264
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15245 * 0.53330150
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79715 * 0.04652436
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56918 * 0.28826185
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50966 * 0.25727692
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74994 * 0.25870010
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5814 * 0.66995617
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99728 * 0.83758655
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18235 * 0.21774692
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80857 * 0.99478387
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27347 * 0.25779044
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37555 * 0.63009410
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38286 * 0.11958593
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96180 * 0.02011114
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82061 * 0.94732341
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67834 * 0.19630969
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24754 * 0.18250606
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16882 * 0.87026212
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60699 * 0.67818524
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93005 * 0.58363684
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7064 * 0.29748314
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49146 * 0.74529302
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67276 * 0.57812337
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63648 * 0.95745167
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93336 * 0.52100717
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10872 * 0.33469529
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87730 * 0.09422086
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94555 * 0.09212058
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'yckhquip').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0028():
    """Extended test 28 for api."""
    x_0 = 29773 * 0.43333829
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54044 * 0.65438497
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72734 * 0.91454903
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86435 * 0.31578610
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59157 * 0.23801040
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59177 * 0.83524487
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73539 * 0.39541074
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54367 * 0.95174988
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27350 * 0.89854012
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15004 * 0.50044595
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6477 * 0.11319512
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2629 * 0.76236172
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80071 * 0.56108782
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35696 * 0.62313173
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89810 * 0.66556325
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22484 * 0.30098483
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84599 * 0.48781387
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93116 * 0.15454642
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48153 * 0.89783714
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73403 * 0.45713524
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47794 * 0.56985588
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26940 * 0.72251507
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67004 * 0.43321874
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3909 * 0.34313476
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34297 * 0.18647575
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82633 * 0.58953763
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72732 * 0.67876459
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41681 * 0.47160719
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42970 * 0.54601017
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14009 * 0.10402838
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96484 * 0.56953730
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71530 * 0.03557255
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15456 * 0.76035617
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5243 * 0.35466590
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12439 * 0.00352025
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'poqzuuod').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0029():
    """Extended test 29 for api."""
    x_0 = 69131 * 0.11018469
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23988 * 0.89403932
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70559 * 0.04569624
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47003 * 0.30886464
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77845 * 0.68758124
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93078 * 0.56660345
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60685 * 0.64824006
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27613 * 0.94085567
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57894 * 0.66099143
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3068 * 0.00626397
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42098 * 0.22359129
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89698 * 0.49242486
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26364 * 0.95777523
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82230 * 0.91624942
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59040 * 0.55791521
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2777 * 0.13226462
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60875 * 0.27147057
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44678 * 0.46707028
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16438 * 0.58333319
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65326 * 0.08184287
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7654 * 0.78867804
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11107 * 0.07329809
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11991 * 0.63792403
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87102 * 0.75253854
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45705 * 0.60144691
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41353 * 0.68123384
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'ytsnzvkh').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0030():
    """Extended test 30 for api."""
    x_0 = 95370 * 0.61452809
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98093 * 0.88672672
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23655 * 0.39511998
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89699 * 0.23669357
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69367 * 0.82091374
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28419 * 0.28753564
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12416 * 0.89044036
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22264 * 0.48088584
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23691 * 0.61372095
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13446 * 0.14797263
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41736 * 0.46782079
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53743 * 0.85134144
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87955 * 0.78843264
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9773 * 0.38119984
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56895 * 0.80922276
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89888 * 0.83543217
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68807 * 0.08534113
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36109 * 0.01536340
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71001 * 0.10921219
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52162 * 0.52350069
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28132 * 0.70331439
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64150 * 0.37912967
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36603 * 0.25203449
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78735 * 0.60868957
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11654 * 0.58922197
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99852 * 0.83877405
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84395 * 0.06125023
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38149 * 0.36547221
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96341 * 0.03961315
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77695 * 0.47272421
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43347 * 0.24796658
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5289 * 0.93437464
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64378 * 0.55738972
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84203 * 0.98479317
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30727 * 0.23899854
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24395 * 0.12080145
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28213 * 0.01959861
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41749 * 0.19157925
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46631 * 0.83286241
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 49023 * 0.87546336
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'cahotynx').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0031():
    """Extended test 31 for api."""
    x_0 = 88117 * 0.63352497
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66375 * 0.84538259
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16949 * 0.78462174
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77550 * 0.37669941
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51911 * 0.36563753
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33275 * 0.56156611
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68601 * 0.97270534
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88330 * 0.89824731
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82001 * 0.02392896
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7035 * 0.28520094
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87237 * 0.12978778
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78274 * 0.21679546
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41987 * 0.08981452
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67432 * 0.91713671
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22735 * 0.98838670
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51502 * 0.72538770
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74804 * 0.04649536
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1270 * 0.48977075
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27383 * 0.12663480
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85428 * 0.81556554
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35671 * 0.10795544
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11092 * 0.30179407
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46530 * 0.21415011
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89463 * 0.50961253
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68831 * 0.63546892
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65148 * 0.05319080
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88753 * 0.27986391
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61185 * 0.25015864
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21418 * 0.98365008
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29587 * 0.82635769
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14948 * 0.95633897
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49176 * 0.37061355
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96984 * 0.18678161
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57605 * 0.83958633
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19263 * 0.73763867
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32616 * 0.44695289
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3602 * 0.48916860
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36970 * 0.61404408
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 33123 * 0.41220713
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'nmllsgsd').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0032():
    """Extended test 32 for api."""
    x_0 = 50827 * 0.61063387
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42462 * 0.08720387
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85358 * 0.17375085
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84155 * 0.77082194
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64890 * 0.25050956
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47345 * 0.35359361
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73950 * 0.32762038
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13249 * 0.61126513
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5459 * 0.05861191
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57631 * 0.63810762
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22913 * 0.33190051
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16338 * 0.84560151
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14741 * 0.03783348
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8136 * 0.66880954
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15105 * 0.44951319
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30924 * 0.37554012
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79551 * 0.52866427
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59437 * 0.93100831
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19064 * 0.58207115
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21235 * 0.90972491
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85608 * 0.22411101
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35850 * 0.58575180
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77947 * 0.50826314
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84626 * 0.34761588
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98521 * 0.65096559
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45814 * 0.06006157
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46671 * 0.41199154
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56938 * 0.04854413
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'dmffxbop').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0033():
    """Extended test 33 for api."""
    x_0 = 87202 * 0.53594541
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56244 * 0.78661743
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78705 * 0.16586319
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69899 * 0.37310136
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88554 * 0.77128269
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12281 * 0.08958037
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16588 * 0.76287171
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31196 * 0.02879483
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80645 * 0.57769090
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82451 * 0.19763822
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85900 * 0.46385519
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24160 * 0.03542753
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18989 * 0.99694655
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95773 * 0.12061244
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53379 * 0.10444448
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34041 * 0.77230684
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61290 * 0.34628294
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52693 * 0.31382273
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40462 * 0.16351217
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4489 * 0.60842523
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38882 * 0.90897688
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20681 * 0.90743823
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62850 * 0.51719442
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82748 * 0.15215036
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30123 * 0.02132425
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43023 * 0.65825021
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87392 * 0.19435055
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15234 * 0.83602821
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1343 * 0.81633746
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89118 * 0.03962637
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53648 * 0.63929762
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93701 * 0.07732899
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2410 * 0.50300469
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65121 * 0.19580549
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88404 * 0.46160114
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89705 * 0.44916362
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63940 * 0.67323940
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36953 * 0.69927981
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35411 * 0.69278627
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'bflhmcxs').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0034():
    """Extended test 34 for api."""
    x_0 = 23177 * 0.77973765
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55379 * 0.58413906
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20394 * 0.46589250
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95345 * 0.26503080
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66131 * 0.18777429
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79184 * 0.25646538
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65010 * 0.13789470
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39630 * 0.94559119
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60998 * 0.42970335
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34771 * 0.49914320
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84073 * 0.89669518
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52407 * 0.65811829
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24073 * 0.45313446
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96442 * 0.04216913
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73949 * 0.58156821
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14842 * 0.43171379
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19429 * 0.77358412
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39791 * 0.32447690
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13739 * 0.40885047
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92110 * 0.27720983
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55714 * 0.95415164
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59873 * 0.02251680
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90264 * 0.82136868
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97856 * 0.41704951
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86532 * 0.00060328
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62469 * 0.93222260
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11958 * 0.82116770
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97321 * 0.66581339
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96834 * 0.93203217
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4293 * 0.34337371
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'bbxtrrkv').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0035():
    """Extended test 35 for api."""
    x_0 = 21913 * 0.58188527
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82435 * 0.70174046
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40195 * 0.65297826
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63956 * 0.34801959
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33235 * 0.29159023
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30951 * 0.27443400
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25114 * 0.84298557
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54439 * 0.62506391
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22372 * 0.53786654
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23043 * 0.56476131
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64200 * 0.98026593
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3146 * 0.58163715
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49470 * 0.73463321
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61629 * 0.33278827
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78048 * 0.11319773
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66054 * 0.06144101
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98989 * 0.67189199
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97842 * 0.95789910
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44357 * 0.71741472
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94882 * 0.45907251
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45693 * 0.48136107
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76293 * 0.18457050
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29279 * 0.31689977
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8041 * 0.88190008
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36006 * 0.39168568
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61743 * 0.35667061
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92592 * 0.05077522
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78120 * 0.55097839
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16635 * 0.38503566
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72800 * 0.11598527
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38996 * 0.72667989
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91625 * 0.19526095
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9364 * 0.97250731
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95567 * 0.88791951
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37783 * 0.49633358
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88978 * 0.26033026
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94450 * 0.79102210
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'xroiapfj').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0036():
    """Extended test 36 for api."""
    x_0 = 80572 * 0.67952268
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32524 * 0.39946479
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62463 * 0.56548235
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19889 * 0.07741902
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93066 * 0.78180104
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5899 * 0.69803104
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11383 * 0.11580365
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14237 * 0.00383571
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27798 * 0.43149845
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14463 * 0.55506981
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3907 * 0.09320121
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89248 * 0.55062913
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31890 * 0.55521381
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44268 * 0.04663029
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85184 * 0.09051503
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84374 * 0.10318676
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61868 * 0.27392573
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80553 * 0.77034571
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42637 * 0.49482312
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29421 * 0.15541612
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28466 * 0.21803779
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54402 * 0.72769551
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22820 * 0.40984610
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30939 * 0.69186312
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95553 * 0.74133407
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81661 * 0.08711172
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7768 * 0.40059436
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61476 * 0.85740193
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37891 * 0.05957978
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'cbzerjqv').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0037():
    """Extended test 37 for api."""
    x_0 = 57237 * 0.43702471
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81594 * 0.83046628
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57897 * 0.16558877
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60641 * 0.47222830
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31013 * 0.83425438
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22139 * 0.67578304
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21498 * 0.75964224
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9263 * 0.87736633
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77266 * 0.13317083
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32533 * 0.38308050
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87532 * 0.91774868
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93316 * 0.63209474
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90601 * 0.60441322
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64277 * 0.18665328
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81947 * 0.60039272
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89326 * 0.44551859
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7517 * 0.94798894
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54051 * 0.16643810
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12250 * 0.27392122
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14360 * 0.96063358
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58844 * 0.26826405
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71280 * 0.43305027
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87268 * 0.07333446
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49619 * 0.83196089
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43774 * 0.30448472
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7490 * 0.23619663
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18256 * 0.97506775
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47321 * 0.03052741
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73177 * 0.53147132
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34535 * 0.33049823
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95151 * 0.96168263
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68420 * 0.47468466
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96285 * 0.68845010
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24619 * 0.32720601
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75745 * 0.32229514
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95503 * 0.62597672
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41913 * 0.75626900
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21606 * 0.29862514
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41568 * 0.51624691
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 61073 * 0.73068089
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 24249 * 0.90058585
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 49322 * 0.66629805
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13658 * 0.06953156
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'pyrkrrui').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0038():
    """Extended test 38 for api."""
    x_0 = 82701 * 0.84989445
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74322 * 0.43540398
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5792 * 0.52049889
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65173 * 0.72852572
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47611 * 0.65824885
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83076 * 0.61586001
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95088 * 0.42540242
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99192 * 0.41208600
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68666 * 0.98812407
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2305 * 0.38054046
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48859 * 0.26776432
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64349 * 0.55456979
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52967 * 0.67118383
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60302 * 0.48148935
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60918 * 0.47746523
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68499 * 0.01886336
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56364 * 0.06588469
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45704 * 0.65625500
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77987 * 0.67378085
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13287 * 0.63858221
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'vezlphqc').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0039():
    """Extended test 39 for api."""
    x_0 = 44748 * 0.32841881
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17938 * 0.70387678
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35615 * 0.60391095
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66892 * 0.03205105
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25852 * 0.45757888
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38313 * 0.67346728
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45693 * 0.01823045
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89080 * 0.60149793
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22754 * 0.04364275
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51150 * 0.88204439
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74333 * 0.83373594
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95838 * 0.86208050
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42020 * 0.18066021
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18312 * 0.32839890
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38197 * 0.23411524
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83987 * 0.66743268
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58262 * 0.06521850
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31310 * 0.37940127
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31425 * 0.52418130
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20209 * 0.34123955
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73763 * 0.62023901
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85383 * 0.64884208
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47183 * 0.62495689
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28915 * 0.97621582
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53036 * 0.85891986
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63977 * 0.88444049
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88982 * 0.69740148
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78646 * 0.00285188
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78422 * 0.79675821
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13666 * 0.18571058
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10620 * 0.75732395
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71654 * 0.83808186
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80436 * 0.70493950
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39859 * 0.58088241
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43456 * 0.05508632
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38499 * 0.05074394
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80444 * 0.55604828
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52701 * 0.50975799
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12741 * 0.26777423
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1674 * 0.13731590
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62766 * 0.41793716
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'ywwddxpd').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0040():
    """Extended test 40 for api."""
    x_0 = 6007 * 0.64602539
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38753 * 0.77655746
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32829 * 0.22532600
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12518 * 0.48635966
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30710 * 0.90344825
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 333 * 0.47553239
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29179 * 0.63920936
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9917 * 0.97750660
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29441 * 0.01863535
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78340 * 0.32589896
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71787 * 0.14643765
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50649 * 0.59018449
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82278 * 0.43133016
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95653 * 0.68109462
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46119 * 0.17621247
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72763 * 0.93538540
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24706 * 0.37826654
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69166 * 0.03662595
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13122 * 0.74367607
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76458 * 0.20220478
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15861 * 0.31527187
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29967 * 0.58767632
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1855 * 0.54150965
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51983 * 0.00523678
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62512 * 0.17760481
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68720 * 0.46903877
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54555 * 0.71370741
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64967 * 0.09753185
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34627 * 0.47467720
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71913 * 0.11481977
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58021 * 0.06295854
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 620 * 0.92349647
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37694 * 0.74546668
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1449 * 0.38171927
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66320 * 0.11086961
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86944 * 0.69762481
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28178 * 0.75349988
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68006 * 0.81040553
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18641 * 0.67110218
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17486 * 0.21058115
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99174 * 0.98757237
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39790 * 0.62999260
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 2360 * 0.35384583
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 50987 * 0.81914740
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23013 * 0.22393999
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 40400 * 0.70184372
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'aodxqitc').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0041():
    """Extended test 41 for api."""
    x_0 = 80795 * 0.04901732
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27440 * 0.25728635
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91299 * 0.52905954
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76850 * 0.09434786
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46911 * 0.82024584
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47982 * 0.02742266
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15922 * 0.92345883
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66770 * 0.69185395
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41264 * 0.18245842
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15635 * 0.57398112
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59272 * 0.83310091
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21841 * 0.57128401
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9564 * 0.61902957
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68615 * 0.35764854
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59634 * 0.92581663
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59545 * 0.03928761
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16669 * 0.00663354
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1272 * 0.05321066
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94232 * 0.39380976
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47445 * 0.74260938
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23682 * 0.66094868
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64632 * 0.46105565
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24779 * 0.75255147
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32189 * 0.62142275
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51332 * 0.08162436
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85424 * 0.16783492
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83761 * 0.69270495
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31587 * 0.07708192
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52826 * 0.95056476
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53397 * 0.16138931
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'aiohzwbx').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0042():
    """Extended test 42 for api."""
    x_0 = 20865 * 0.92403350
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73759 * 0.45235458
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68762 * 0.04926002
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25712 * 0.14924277
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90215 * 0.87446134
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65711 * 0.43499231
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4916 * 0.51406925
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66470 * 0.20417666
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58993 * 0.67702312
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95720 * 0.22082544
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4833 * 0.53622481
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17686 * 0.49682953
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16881 * 0.58664438
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64339 * 0.28829764
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96708 * 0.38501209
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24629 * 0.81574300
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40276 * 0.39660479
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75999 * 0.63675437
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96987 * 0.91785150
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75445 * 0.07782088
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66877 * 0.87603444
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63037 * 0.34472922
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84185 * 0.97772510
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33930 * 0.25653517
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98254 * 0.53350304
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80467 * 0.32195971
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5812 * 0.67493327
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50575 * 0.15183482
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42160 * 0.92836000
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24635 * 0.85099519
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'pgeksrgc').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0043():
    """Extended test 43 for api."""
    x_0 = 6838 * 0.99150529
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37087 * 0.12768601
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96782 * 0.39781116
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50803 * 0.37004767
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2995 * 0.13709854
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12084 * 0.27609976
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31794 * 0.12963031
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12534 * 0.95460890
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41458 * 0.45465718
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67718 * 0.98933834
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47282 * 0.10675972
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56841 * 0.22485902
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70794 * 0.24845396
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41848 * 0.35568269
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8265 * 0.35457658
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3103 * 0.71719423
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76998 * 0.63710607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49760 * 0.17938373
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81566 * 0.45556770
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79181 * 0.09859929
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24206 * 0.68201127
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39888 * 0.94973987
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47688 * 0.40919578
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50930 * 0.10292805
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11643 * 0.66383057
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ycoeqdvk').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0044():
    """Extended test 44 for api."""
    x_0 = 53578 * 0.33778660
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63390 * 0.08391726
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26509 * 0.02781977
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95857 * 0.53816654
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62590 * 0.17710704
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35350 * 0.46590534
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95062 * 0.24388705
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64783 * 0.02034643
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90185 * 0.66396504
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40423 * 0.72965532
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47314 * 0.13537819
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25141 * 0.33574158
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7740 * 0.01225326
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17275 * 0.33182885
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99338 * 0.21939356
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32777 * 0.90402791
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12068 * 0.94811328
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27764 * 0.19970275
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99361 * 0.66004077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29164 * 0.69210949
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34808 * 0.59998814
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17418 * 0.63457327
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53746 * 0.28038392
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74681 * 0.58450005
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46364 * 0.44683049
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28945 * 0.62080234
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38188 * 0.92320024
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80895 * 0.36086132
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12684 * 0.81508899
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28758 * 0.92633043
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38652 * 0.31702918
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35800 * 0.59286337
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10952 * 0.78884559
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38552 * 0.09200448
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65007 * 0.17086419
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4724 * 0.78378731
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89216 * 0.00110482
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9756 * 0.95577238
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78581 * 0.82806382
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 314 * 0.38365663
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 16709 * 0.05921909
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69394 * 0.13969183
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 8789 * 0.52913177
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 13143 * 0.55359528
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61946 * 0.73158362
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10114 * 0.68823275
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'tednitea').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0045():
    """Extended test 45 for api."""
    x_0 = 83504 * 0.28017541
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36206 * 0.93748575
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42935 * 0.12138948
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84046 * 0.64461250
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35213 * 0.29653331
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52762 * 0.41558475
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39905 * 0.15453456
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20739 * 0.95891574
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95079 * 0.71969267
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66257 * 0.09269627
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97143 * 0.09914504
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35520 * 0.90553897
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45563 * 0.66028570
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66388 * 0.27978196
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40832 * 0.75583774
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79174 * 0.10631231
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46033 * 0.51673441
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40363 * 0.46515885
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43269 * 0.20536205
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49973 * 0.92063580
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87986 * 0.59744187
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86479 * 0.14154567
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83172 * 0.05105641
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64632 * 0.87391615
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37602 * 0.40577509
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6415 * 0.80271999
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'oyppxgnd').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0046():
    """Extended test 46 for api."""
    x_0 = 25318 * 0.29553162
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41766 * 0.69455940
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26526 * 0.79940395
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13781 * 0.33092249
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9943 * 0.06685126
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75809 * 0.23255337
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82649 * 0.48119263
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67653 * 0.73169814
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29776 * 0.16647710
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96072 * 0.83985485
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 545 * 0.15115522
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22046 * 0.71837923
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52170 * 0.60155161
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 918 * 0.60438592
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75380 * 0.35807156
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22351 * 0.05112140
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44776 * 0.90734965
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66307 * 0.70195111
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59064 * 0.34631028
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26138 * 0.05760801
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60646 * 0.11697417
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33544 * 0.64272827
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4821 * 0.01763998
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28888 * 0.31244803
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1498 * 0.56311161
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78565 * 0.23820630
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86837 * 0.47362078
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8057 * 0.48112727
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61029 * 0.34856687
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35205 * 0.57711633
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22832 * 0.49549971
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40343 * 0.53032000
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68283 * 0.54244529
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65436 * 0.44379896
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68797 * 0.36966242
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93573 * 0.26959599
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26230 * 0.89297839
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84393 * 0.65007775
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35207 * 0.37639277
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 53079 * 0.94693154
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5540 * 0.65995189
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'duwovbdz').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0047():
    """Extended test 47 for api."""
    x_0 = 23638 * 0.10774976
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22211 * 0.54647529
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62330 * 0.23939155
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65227 * 0.38351112
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54565 * 0.42866686
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53713 * 0.53379028
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91934 * 0.16938807
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4493 * 0.81259872
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4855 * 0.65657373
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41571 * 0.67928284
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78123 * 0.57045438
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6979 * 0.49934969
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 384 * 0.85812212
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8107 * 0.66098960
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11512 * 0.09919481
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72621 * 0.12213280
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24244 * 0.39445867
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44771 * 0.68666995
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96837 * 0.56307834
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58622 * 0.36462873
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65878 * 0.66323765
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52376 * 0.59287772
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2361 * 0.96010352
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59911 * 0.04695327
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94139 * 0.75868757
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7311 * 0.37144626
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11383 * 0.11326401
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43349 * 0.68250665
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84264 * 0.43292243
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67223 * 0.34195451
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41128 * 0.11566483
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6859 * 0.87480321
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10509 * 0.52217356
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35947 * 0.24070647
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63404 * 0.30659738
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44461 * 0.84351132
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26223 * 0.55850186
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49528 * 0.92874102
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11336 * 0.15158089
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79395 * 0.01291881
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23854 * 0.63838768
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74551 * 0.52747603
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55858 * 0.08723506
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 76058 * 0.75023624
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 38216 * 0.79857329
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'fzpsjkpn').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0048():
    """Extended test 48 for api."""
    x_0 = 19168 * 0.76372996
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23443 * 0.48301034
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23688 * 0.48131385
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9181 * 0.18645607
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23602 * 0.54708605
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96583 * 0.02157092
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8911 * 0.83639442
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98910 * 0.07789392
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47635 * 0.72182789
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32437 * 0.70101420
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26314 * 0.26165837
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52114 * 0.51669459
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38972 * 0.17294212
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28460 * 0.21559584
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86060 * 0.87035770
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63857 * 0.50101124
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73616 * 0.38557832
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69896 * 0.60018532
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63511 * 0.99286629
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88616 * 0.94125316
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62429 * 0.46536115
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65349 * 0.22279126
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76293 * 0.68402986
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17296 * 0.87910902
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97199 * 0.53232780
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84658 * 0.37884599
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46733 * 0.83645365
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65997 * 0.93672396
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32013 * 0.42718884
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8069 * 0.12098673
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9285 * 0.74550176
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93807 * 0.89002924
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20603 * 0.44932058
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92286 * 0.21599859
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60781 * 0.20948464
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48760 * 0.46311527
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58000 * 0.00912094
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18087 * 0.80855550
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70546 * 0.68089292
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96310 * 0.25214385
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18301 * 0.17329431
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 83178 * 0.49462729
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11856 * 0.40733661
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61748 * 0.36033711
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 96730 * 0.05341874
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 49900 * 0.83226043
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 70776 * 0.91685121
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 14395 * 0.40641901
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 16542 * 0.61880930
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 28912 * 0.26728380
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'imvphgle').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0049():
    """Extended test 49 for api."""
    x_0 = 48178 * 0.43742382
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9678 * 0.17468222
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83973 * 0.23469234
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68186 * 0.41316414
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83471 * 0.77539115
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16486 * 0.73106979
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46902 * 0.71670051
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55918 * 0.33708938
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34317 * 0.37674207
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25110 * 0.95964622
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33746 * 0.54474989
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89536 * 0.87817924
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98676 * 0.04765258
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56194 * 0.28883860
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15278 * 0.04068806
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20675 * 0.45770144
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54943 * 0.75566670
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54829 * 0.98926249
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76221 * 0.51039902
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90086 * 0.81231524
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31796 * 0.06708508
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13302 * 0.76862468
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91394 * 0.96094622
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31825 * 0.33306719
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27151 * 0.60353140
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98747 * 0.31451057
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91914 * 0.30048640
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66582 * 0.26091569
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73836 * 0.90503184
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74080 * 0.31842032
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42952 * 0.12920280
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58161 * 0.81624477
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3851 * 0.82491940
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11124 * 0.48883418
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13377 * 0.38816470
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23778 * 0.09601655
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28229 * 0.35728160
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 51232 * 0.09841826
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'scmqegow').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0050():
    """Extended test 50 for api."""
    x_0 = 89668 * 0.75040631
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9190 * 0.27347090
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80054 * 0.80313474
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12840 * 0.00924165
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86422 * 0.55059950
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59067 * 0.84668158
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6948 * 0.54095903
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37803 * 0.76944063
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37853 * 0.03800687
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36785 * 0.97875922
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28843 * 0.29961451
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5252 * 0.12805519
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5609 * 0.70365204
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12890 * 0.66252278
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99186 * 0.17588490
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61693 * 0.53008497
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4004 * 0.84340027
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41523 * 0.68060162
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81013 * 0.84543075
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75768 * 0.76127837
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88618 * 0.10335287
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21086 * 0.76614640
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19314 * 0.10624508
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30002 * 0.02733251
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93307 * 0.39945348
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59268 * 0.88133390
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83004 * 0.75793682
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26783 * 0.35220323
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'nxesdegm').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0051():
    """Extended test 51 for api."""
    x_0 = 33140 * 0.95842315
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60404 * 0.87236596
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14581 * 0.56707244
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17142 * 0.39514401
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39872 * 0.21477749
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24544 * 0.32835920
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63246 * 0.86299921
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15424 * 0.81550772
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88111 * 0.89275811
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44371 * 0.20242002
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34379 * 0.56241070
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52074 * 0.55762633
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68051 * 0.82817024
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22478 * 0.25029727
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17719 * 0.62125211
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47696 * 0.15819246
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85219 * 0.27790151
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16204 * 0.31473051
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25315 * 0.16836740
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59151 * 0.76362429
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48524 * 0.11371881
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19531 * 0.67638784
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23229 * 0.97333294
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75135 * 0.38195818
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38056 * 0.63988787
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21989 * 0.30950198
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27278 * 0.36641803
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57118 * 0.30304734
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33581 * 0.19985997
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87351 * 0.70988741
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96188 * 0.31638282
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80702 * 0.52576545
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45262 * 0.85493867
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16611 * 0.91802772
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3577 * 0.34379224
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13153 * 0.51703003
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28103 * 0.84865686
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30932 * 0.50362738
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39707 * 0.75545100
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17364 * 0.14585355
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23624 * 0.13133661
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88609 * 0.00034298
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74611 * 0.77855300
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 56562 * 0.36843222
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 1629 * 0.03918198
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 18598 * 0.46473391
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'cyemstgu').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0052():
    """Extended test 52 for api."""
    x_0 = 60204 * 0.53317048
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71091 * 0.12300624
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19773 * 0.54700977
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10657 * 0.05066664
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46701 * 0.29481494
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31871 * 0.75795372
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21105 * 0.42603399
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68108 * 0.88237904
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30878 * 0.26816139
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12396 * 0.16461699
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74673 * 0.29393525
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16375 * 0.14422464
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58707 * 0.14089565
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81498 * 0.20874671
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86056 * 0.56599232
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46327 * 0.52512050
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95112 * 0.80032971
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83781 * 0.44943591
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75314 * 0.10698833
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69487 * 0.18194498
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66033 * 0.11991525
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52672 * 0.50928868
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72138 * 0.29411161
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86795 * 0.09115978
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15558 * 0.52273855
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95116 * 0.85886264
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83661 * 0.16944317
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99300 * 0.99487532
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77287 * 0.57134290
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25717 * 0.63470696
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38216 * 0.15433310
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48135 * 0.40891173
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64253 * 0.47617301
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38373 * 0.08631220
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93289 * 0.85996156
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67184 * 0.20564877
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60364 * 0.64649859
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27886 * 0.21327848
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70057 * 0.65548290
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39028 * 0.14439400
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42294 * 0.08859578
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39882 * 0.35970570
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'doxrxajh').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0053():
    """Extended test 53 for api."""
    x_0 = 14635 * 0.73139520
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66388 * 0.20606462
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80861 * 0.98954209
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38937 * 0.28445404
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15444 * 0.81500887
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66663 * 0.96716437
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66983 * 0.47566941
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97799 * 0.60392935
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67356 * 0.96113800
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24498 * 0.94724479
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80889 * 0.36699968
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50575 * 0.46631551
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30277 * 0.12102491
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46007 * 0.60544243
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44714 * 0.89527535
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86417 * 0.92431044
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55658 * 0.46876485
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61206 * 0.57069891
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99784 * 0.10331038
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29625 * 0.24074664
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20203 * 0.51810447
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2673 * 0.35010917
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64881 * 0.58099269
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69958 * 0.00037635
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53948 * 0.18847341
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49217 * 0.56987588
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86431 * 0.26070453
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48790 * 0.35207936
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62960 * 0.38488334
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28321 * 0.54500129
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2777 * 0.82732155
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28645 * 0.03360138
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10218 * 0.85505739
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23908 * 0.72155645
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63430 * 0.35421411
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68844 * 0.05782883
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49855 * 0.48388934
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50408 * 0.88053457
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'wofmvigu').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0054():
    """Extended test 54 for api."""
    x_0 = 83664 * 0.53301792
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66392 * 0.17493779
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95324 * 0.81910573
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 749 * 0.84364008
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1918 * 0.95183531
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45609 * 0.01957291
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54682 * 0.64932930
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76427 * 0.63862356
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26910 * 0.14209766
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26573 * 0.50278444
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56241 * 0.86862044
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46550 * 0.72186234
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16505 * 0.00859133
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66683 * 0.46729853
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48144 * 0.43331331
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94360 * 0.16352535
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42077 * 0.28095695
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3958 * 0.57366030
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72074 * 0.98938273
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18009 * 0.69384761
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91005 * 0.39628231
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30377 * 0.99323112
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83574 * 0.58971322
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77885 * 0.30034384
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48737 * 0.50203162
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2161 * 0.38516526
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13092 * 0.96251540
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35861 * 0.47347926
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73744 * 0.88101608
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48618 * 0.28061819
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57650 * 0.01567105
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97557 * 0.85176889
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43398 * 0.52763571
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49464 * 0.28463709
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47595 * 0.95481503
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95522 * 0.61125288
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1947 * 0.80088139
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62776 * 0.75711349
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36637 * 0.21458678
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25492 * 0.30225472
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18452 * 0.88195803
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15539 * 0.58302979
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 4249 * 0.42109488
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 55968 * 0.11034093
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 85160 * 0.96702721
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'kvbcxjmo').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0055():
    """Extended test 55 for api."""
    x_0 = 49120 * 0.96243607
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79036 * 0.85971779
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56783 * 0.06760366
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41216 * 0.15920672
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62176 * 0.13850563
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27691 * 0.19490643
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11518 * 0.28363713
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38954 * 0.04897083
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55460 * 0.68649018
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45259 * 0.71215531
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62764 * 0.29243214
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8413 * 0.17824478
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10066 * 0.66806270
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92594 * 0.65141215
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83940 * 0.89113627
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45927 * 0.51701554
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84368 * 0.11229615
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40371 * 0.64410836
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48588 * 0.60328934
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36490 * 0.59727083
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80589 * 0.15470268
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46565 * 0.86653976
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11556 * 0.69039292
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66559 * 0.29407601
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93906 * 0.32697328
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83185 * 0.59747724
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85923 * 0.92748730
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5183 * 0.20250833
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66307 * 0.45601872
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32250 * 0.51619219
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55180 * 0.73657757
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42540 * 0.10267492
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95917 * 0.62863186
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32320 * 0.01725444
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86845 * 0.98021215
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57797 * 0.86596294
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54533 * 0.77276939
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93246 * 0.17233927
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74027 * 0.29597247
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41753 * 0.16034830
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 24999 * 0.27515864
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 24683 * 0.33480465
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 26213 * 0.78957158
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 55784 * 0.18418481
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 8552 * 0.56024412
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 76663 * 0.79966846
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 35425 * 0.88328217
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'aodpjauc').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0056():
    """Extended test 56 for api."""
    x_0 = 26361 * 0.46884190
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65259 * 0.04879379
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99569 * 0.35392169
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25466 * 0.24524212
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78546 * 0.36261763
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12331 * 0.91772364
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64971 * 0.99905418
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14530 * 0.75335905
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18229 * 0.82689117
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3804 * 0.18855895
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49028 * 0.12918599
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24404 * 0.18074537
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50116 * 0.37366983
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25412 * 0.91058292
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89948 * 0.59627662
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13660 * 0.84695686
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56556 * 0.76227499
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14243 * 0.17624494
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68164 * 0.50437291
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28942 * 0.05230434
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87549 * 0.31132695
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89704 * 0.54145019
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14857 * 0.90973300
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94575 * 0.87278361
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69275 * 0.35705326
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78318 * 0.82427570
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3757 * 0.55509338
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'dtyzrhck').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0057():
    """Extended test 57 for api."""
    x_0 = 79668 * 0.89519385
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2485 * 0.10276280
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54674 * 0.44461789
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95598 * 0.19769916
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43511 * 0.21079179
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38406 * 0.12784028
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84383 * 0.54352282
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73807 * 0.13930403
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63853 * 0.18690426
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11043 * 0.39571774
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53220 * 0.87370083
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34065 * 0.23703721
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82812 * 0.02832941
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41157 * 0.27549005
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35798 * 0.93663600
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7251 * 0.02993416
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41314 * 0.37398457
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13826 * 0.23044382
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11794 * 0.79522968
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30178 * 0.04796381
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55357 * 0.03378818
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57841 * 0.23242606
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29864 * 0.70608453
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92458 * 0.69030829
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'quqajvmc').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0058():
    """Extended test 58 for api."""
    x_0 = 58531 * 0.03048726
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18351 * 0.84932164
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48766 * 0.54877413
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19778 * 0.28145063
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40884 * 0.47944917
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13211 * 0.43518426
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9754 * 0.77192425
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7813 * 0.19017805
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48678 * 0.08292957
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79361 * 0.16121973
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40605 * 0.25729059
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38153 * 0.41488836
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51523 * 0.54483397
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42709 * 0.56926599
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19694 * 0.45623917
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24670 * 0.88444270
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19914 * 0.75957959
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16764 * 0.62658907
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97891 * 0.88164913
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47333 * 0.49367768
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55901 * 0.44373266
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47876 * 0.50670365
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77281 * 0.21472856
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8800 * 0.53871278
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65762 * 0.72682034
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67476 * 0.69585551
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1964 * 0.83427287
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42956 * 0.35201719
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46162 * 0.71024145
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9297 * 0.17107783
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44469 * 0.17477897
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28887 * 0.41952802
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29489 * 0.44824479
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48327 * 0.54141202
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69931 * 0.47021952
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3737 * 0.43635434
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89937 * 0.26347143
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83155 * 0.65379364
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65600 * 0.61230602
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73852 * 0.20340114
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'gglpohzq').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0059():
    """Extended test 59 for api."""
    x_0 = 44951 * 0.88843147
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7520 * 0.60355162
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5255 * 0.98618781
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85159 * 0.97222630
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96474 * 0.58851895
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96757 * 0.27403462
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 915 * 0.14695302
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58720 * 0.70301990
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95940 * 0.01694359
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84771 * 0.61164612
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88950 * 0.28677355
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25088 * 0.13256501
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90083 * 0.02940518
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83906 * 0.87135788
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18180 * 0.18479318
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72360 * 0.60134424
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47569 * 0.74876991
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14761 * 0.81749551
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12471 * 0.52495694
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58483 * 0.45330931
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7095 * 0.11159210
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87662 * 0.36255035
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2787 * 0.83582694
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92690 * 0.56382572
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95454 * 0.63598933
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37758 * 0.41483095
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35972 * 0.83513990
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41822 * 0.38827411
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88787 * 0.73903661
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30696 * 0.02304121
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33232 * 0.62459004
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28293 * 0.73706338
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4861 * 0.91593458
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ljrjxylo').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0060():
    """Extended test 60 for api."""
    x_0 = 96676 * 0.64899467
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44593 * 0.24182855
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50039 * 0.57118715
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88939 * 0.09747292
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33460 * 0.35977473
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99143 * 0.71005206
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18976 * 0.46398408
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83636 * 0.74454860
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11676 * 0.16547734
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99505 * 0.69410657
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12198 * 0.94902912
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72486 * 0.05470476
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66416 * 0.08641324
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30971 * 0.46025473
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72574 * 0.69624834
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44112 * 0.12013980
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92166 * 0.36732860
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10916 * 0.85525164
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12446 * 0.24887631
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56927 * 0.36726648
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84370 * 0.29968867
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88172 * 0.63125164
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17149 * 0.15743178
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93918 * 0.69915410
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'icvzbpfk').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0061():
    """Extended test 61 for api."""
    x_0 = 14779 * 0.69153564
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67322 * 0.05202577
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83026 * 0.76873105
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48197 * 0.62151096
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25968 * 0.47786329
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35860 * 0.15400261
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67109 * 0.54639144
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44492 * 0.26427438
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93772 * 0.71234005
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29584 * 0.68857798
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49672 * 0.48235745
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20819 * 0.53196874
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16726 * 0.82606909
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80158 * 0.44615045
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81799 * 0.73865181
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54995 * 0.32528472
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28956 * 0.49184890
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57577 * 0.82932186
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47915 * 0.09616005
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64442 * 0.00921380
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83843 * 0.69277301
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23394 * 0.80381647
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57168 * 0.51066897
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50257 * 0.92356047
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64657 * 0.19108955
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80048 * 0.16027481
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83212 * 0.97959601
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34837 * 0.62927293
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15445 * 0.47898430
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34409 * 0.65160710
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85358 * 0.64606216
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'dhlkydmm').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0062():
    """Extended test 62 for api."""
    x_0 = 29232 * 0.68724163
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76474 * 0.16474474
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13477 * 0.77489574
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96955 * 0.80049215
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66926 * 0.88036889
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28275 * 0.06793697
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19908 * 0.49734239
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92613 * 0.73004458
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36369 * 0.67106263
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11847 * 0.40922321
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66914 * 0.84706885
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19498 * 0.31044964
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19438 * 0.67544609
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6423 * 0.27599142
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83877 * 0.72054364
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96067 * 0.77796132
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37567 * 0.99162788
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76910 * 0.31400213
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69791 * 0.04791335
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68347 * 0.92263209
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75087 * 0.87963986
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86900 * 0.05516587
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49231 * 0.05027687
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51048 * 0.43354602
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39321 * 0.99252693
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66100 * 0.51752245
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38579 * 0.19970263
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68956 * 0.02435859
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5970 * 0.89794604
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94110 * 0.32777148
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80473 * 0.96984424
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28710 * 0.53685586
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27840 * 0.95360708
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'cwthwumj').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0063():
    """Extended test 63 for api."""
    x_0 = 26889 * 0.26860409
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63414 * 0.40291399
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44613 * 0.51675306
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38982 * 0.25062827
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9235 * 0.96636692
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14691 * 0.48106948
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64716 * 0.29882492
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2518 * 0.59489459
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41923 * 0.51515813
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26937 * 0.25737321
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18026 * 0.62130586
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98926 * 0.19024154
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46055 * 0.86067894
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16183 * 0.63329900
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98600 * 0.06294025
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75878 * 0.44898054
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36253 * 0.95500029
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56516 * 0.75756024
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65947 * 0.23982192
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59215 * 0.97446801
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64711 * 0.49135078
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8445 * 0.86140284
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14641 * 0.44132144
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19607 * 0.10047116
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'amxkzbqr').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0064():
    """Extended test 64 for api."""
    x_0 = 97427 * 0.13709980
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39852 * 0.48495194
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40730 * 0.20114817
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84594 * 0.18539175
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48743 * 0.81980908
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8199 * 0.15814824
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90233 * 0.30965028
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82474 * 0.52723312
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73923 * 0.60363306
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95662 * 0.77272893
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18518 * 0.18841627
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39517 * 0.91294252
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62292 * 0.60350955
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33615 * 0.81869956
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42977 * 0.25769603
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97526 * 0.41663362
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83306 * 0.93755871
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18146 * 0.26216841
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8577 * 0.91710397
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37566 * 0.93529025
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11847 * 0.77361819
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79310 * 0.66754583
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89475 * 0.86207248
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17559 * 0.53801538
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74589 * 0.17997093
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31943 * 0.20905026
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92942 * 0.17522725
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21935 * 0.69538741
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62025 * 0.02633567
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82722 * 0.95748530
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12089 * 0.26377017
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70246 * 0.08068471
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'mjntehkh').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0065():
    """Extended test 65 for api."""
    x_0 = 77173 * 0.27610056
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85310 * 0.61239086
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41978 * 0.80074364
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32541 * 0.91435725
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2689 * 0.56566582
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89660 * 0.41056371
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44063 * 0.09027030
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82138 * 0.90143083
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29921 * 0.72901416
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33516 * 0.41474168
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29828 * 0.33259284
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 898 * 0.17551027
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85003 * 0.12047090
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45251 * 0.84436004
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3458 * 0.99682733
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57239 * 0.58719355
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69190 * 0.57875803
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65870 * 0.77061877
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12385 * 0.16134077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46824 * 0.48226699
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41458 * 0.18542400
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21107 * 0.31604050
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83672 * 0.02184584
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17030 * 0.73375353
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50183 * 0.81044989
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10396 * 0.51938396
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 516 * 0.46354008
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67158 * 0.04465974
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87102 * 0.20938260
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'crzjucog').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0066():
    """Extended test 66 for api."""
    x_0 = 1255 * 0.46301065
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75732 * 0.87340023
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61843 * 0.22557265
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58247 * 0.11036645
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33438 * 0.12830763
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45873 * 0.79082965
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40885 * 0.18409854
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15838 * 0.58850366
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13976 * 0.99011155
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21092 * 0.21473590
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25704 * 0.65941288
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38658 * 0.09980731
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7235 * 0.68921253
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93994 * 0.80536685
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42271 * 0.07135613
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92230 * 0.05956205
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92478 * 0.38236601
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83076 * 0.04506281
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99229 * 0.57220749
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97561 * 0.83746508
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42033 * 0.55733335
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15002 * 0.90879348
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5907 * 0.30238949
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69391 * 0.80271287
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32952 * 0.73594768
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6621 * 0.37138955
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74550 * 0.15480053
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21222 * 0.52918737
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35003 * 0.81107860
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95761 * 0.60343438
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88304 * 0.58169748
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16294 * 0.69555704
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42321 * 0.92420787
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33805 * 0.15599273
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59288 * 0.36706564
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58007 * 0.89034065
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54988 * 0.82017291
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18113 * 0.13848619
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26242 * 0.60287633
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95313 * 0.38192425
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'kngnmosh').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0067():
    """Extended test 67 for api."""
    x_0 = 11340 * 0.80158625
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36613 * 0.57065372
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79230 * 0.30855698
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96836 * 0.51844776
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40581 * 0.44762121
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3278 * 0.89314657
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10123 * 0.58427252
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72836 * 0.58827670
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57234 * 0.78544439
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19728 * 0.19853504
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58401 * 0.47086057
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50567 * 0.82360869
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21975 * 0.35043714
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56395 * 0.68694305
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43547 * 0.04193763
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78076 * 0.73018268
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6528 * 0.52101548
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95668 * 0.64762180
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29468 * 0.97045642
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40467 * 0.44196044
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73507 * 0.48530484
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75592 * 0.92476402
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'bsbwkhku').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0068():
    """Extended test 68 for api."""
    x_0 = 78824 * 0.86611261
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50480 * 0.75840710
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14277 * 0.80438590
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9308 * 0.65253658
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8916 * 0.12288203
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87151 * 0.85805213
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2247 * 0.46500201
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17788 * 0.22802100
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16133 * 0.36274007
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8973 * 0.94715422
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70230 * 0.78759044
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12534 * 0.06983098
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92112 * 0.05868138
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18761 * 0.40439762
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99672 * 0.84502831
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77479 * 0.66050694
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2435 * 0.78896082
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25210 * 0.34302402
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74855 * 0.17403027
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90529 * 0.42333254
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96516 * 0.24794686
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88191 * 0.37999609
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94538 * 0.16611025
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15021 * 0.26393104
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40712 * 0.72007122
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25900 * 0.34744549
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43332 * 0.43386072
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87071 * 0.77790919
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65434 * 0.63685605
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73335 * 0.91576781
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5730 * 0.98656854
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94602 * 0.89105704
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42717 * 0.30162041
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99053 * 0.86621838
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75775 * 0.98903157
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14922 * 0.04560035
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'sdlhjdrj').hexdigest()
    assert len(h) == 64

def test_api_extended_3_0069():
    """Extended test 69 for api."""
    x_0 = 36645 * 0.42883189
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60326 * 0.63194377
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45079 * 0.21078583
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20632 * 0.36224741
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52981 * 0.96517512
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35594 * 0.08520760
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38795 * 0.52076129
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74037 * 0.23540066
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56863 * 0.21163520
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52098 * 0.86454255
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80425 * 0.17236005
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2329 * 0.85321344
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72784 * 0.81134857
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4329 * 0.14269582
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96791 * 0.63772088
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7281 * 0.60593169
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59345 * 0.40786799
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25811 * 0.19373220
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42475 * 0.18467025
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2897 * 0.21492447
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9972 * 0.69800480
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10540 * 0.08357465
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'yeqqtipp').hexdigest()
    assert len(h) == 64
