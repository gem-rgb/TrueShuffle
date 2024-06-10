"""Extended tests for import suite 3."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_import_extended_3_0000():
    """Extended test 0 for import."""
    x_0 = 96836 * 0.33537003
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67133 * 0.01771412
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21526 * 0.63706572
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5698 * 0.65337238
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47743 * 0.92996091
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24196 * 0.51009425
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56421 * 0.10696418
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46168 * 0.56712363
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54808 * 0.29112539
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33589 * 0.99834230
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82904 * 0.64454459
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11929 * 0.46963232
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48706 * 0.98640877
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61387 * 0.97141708
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98249 * 0.79303718
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22401 * 0.33575469
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5608 * 0.20120775
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95872 * 0.16890217
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5333 * 0.62230455
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39210 * 0.22337496
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97785 * 0.41372475
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68676 * 0.22073290
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'rmbnyaop').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0001():
    """Extended test 1 for import."""
    x_0 = 92890 * 0.15738593
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30510 * 0.43427134
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60244 * 0.87821101
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 613 * 0.43139817
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25274 * 0.32581445
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9701 * 0.48997655
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87357 * 0.25329399
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24526 * 0.30244647
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9388 * 0.52320461
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29668 * 0.16829530
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97804 * 0.89907851
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62811 * 0.18631580
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13418 * 0.57618640
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81075 * 0.97294476
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40253 * 0.31028331
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72403 * 0.68148962
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76029 * 0.11032575
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95468 * 0.77433342
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58100 * 0.94008994
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47798 * 0.37451549
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8205 * 0.46779457
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89850 * 0.76101212
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37678 * 0.19366389
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54343 * 0.07576511
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 535 * 0.08779826
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41149 * 0.89324364
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54410 * 0.49637692
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66741 * 0.58954415
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98306 * 0.93486482
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67405 * 0.93938863
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77827 * 0.37261057
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26453 * 0.97653521
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78134 * 0.78352136
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6002 * 0.45225331
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55793 * 0.16330642
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15879 * 0.93965704
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99336 * 0.66156410
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90264 * 0.84468548
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 68228 * 0.91295686
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16650 * 0.35725916
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 76496 * 0.91197211
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6608 * 0.67787613
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15112 * 0.05681953
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11363 * 0.03322633
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35059 * 0.47324974
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 77493 * 0.32482174
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 92466 * 0.56329005
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 2664 * 0.98892860
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 64600 * 0.17737531
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'wphrqyzh').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0002():
    """Extended test 2 for import."""
    x_0 = 79221 * 0.07956540
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11861 * 0.32450571
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39725 * 0.20755062
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7135 * 0.24317103
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64288 * 0.76081729
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45502 * 0.17825539
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48971 * 0.37831786
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94655 * 0.24833521
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22274 * 0.39389793
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83627 * 0.44551325
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25046 * 0.40342517
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78067 * 0.57669876
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72693 * 0.29935348
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94639 * 0.77425595
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4015 * 0.42755714
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8391 * 0.72233595
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82434 * 0.79143182
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39878 * 0.18125848
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46619 * 0.43392648
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71396 * 0.63602982
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82809 * 0.55140722
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32216 * 0.40609298
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71253 * 0.23186338
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52275 * 0.74453343
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26355 * 0.40360750
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59803 * 0.31991402
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94067 * 0.04249290
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76211 * 0.60722428
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'byxiitsm').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0003():
    """Extended test 3 for import."""
    x_0 = 14550 * 0.41025228
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4223 * 0.54952006
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39341 * 0.04570428
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43205 * 0.85050241
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48771 * 0.46449236
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41154 * 0.41183780
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45546 * 0.97734617
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48769 * 0.25455290
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67117 * 0.32338652
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77353 * 0.70218830
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14801 * 0.97007940
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19575 * 0.06577265
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62475 * 0.82629836
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41584 * 0.91375280
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95369 * 0.69910721
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18490 * 0.62484285
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1752 * 0.06563761
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91722 * 0.05586799
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53175 * 0.24888157
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50801 * 0.80225000
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49446 * 0.21506421
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85930 * 0.25733026
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85327 * 0.87457436
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96016 * 0.92808231
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49140 * 0.59527086
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19550 * 0.82958821
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33061 * 0.03386972
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5517 * 0.77310756
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7520 * 0.17778333
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73791 * 0.66339755
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28849 * 0.56806226
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4034 * 0.17299300
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60640 * 0.67554565
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10148 * 0.20967471
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3573 * 0.10212326
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15853 * 0.39944431
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36303 * 0.84326410
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27543 * 0.50757949
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 33044 * 0.73443044
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7651 * 0.31400523
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12049 * 0.54988179
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 48419 * 0.38855160
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23535 * 0.72384187
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 49212 * 0.92411896
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'fnkawlol').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0004():
    """Extended test 4 for import."""
    x_0 = 24550 * 0.82471703
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46326 * 0.02124601
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55413 * 0.71087496
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42426 * 0.01339010
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95909 * 0.29134133
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81831 * 0.08359355
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28457 * 0.90288190
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9258 * 0.13388354
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84446 * 0.51998841
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95616 * 0.84532253
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37058 * 0.33989580
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76212 * 0.92802310
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35359 * 0.99529953
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33871 * 0.01163069
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97839 * 0.31745399
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39886 * 0.84209865
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57122 * 0.38848285
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53092 * 0.89340092
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43448 * 0.96891800
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49665 * 0.28400519
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81478 * 0.10352190
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1392 * 0.89992771
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2209 * 0.30043852
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81986 * 0.15638827
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28414 * 0.58177132
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'wfyguoui').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0005():
    """Extended test 5 for import."""
    x_0 = 90318 * 0.92174581
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4508 * 0.22909151
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70992 * 0.78177506
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94594 * 0.08009097
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19214 * 0.37524986
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70247 * 0.47096229
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78094 * 0.88285273
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95449 * 0.63669058
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8017 * 0.60689244
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64500 * 0.71326702
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69608 * 0.04481723
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16984 * 0.85719166
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36303 * 0.88956196
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53499 * 0.20956862
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60811 * 0.78818436
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56578 * 0.45001164
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 108 * 0.53149614
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44819 * 0.03064449
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40427 * 0.09114101
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82258 * 0.97823051
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77581 * 0.48860313
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28286 * 0.11007451
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'gseljwvu').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0006():
    """Extended test 6 for import."""
    x_0 = 94247 * 0.37461167
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55679 * 0.50253509
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18686 * 0.56239328
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52921 * 0.65610702
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80714 * 0.05248039
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23188 * 0.04426669
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11687 * 0.44697978
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51918 * 0.12230405
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12247 * 0.95495757
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14873 * 0.56994821
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39736 * 0.80629497
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1137 * 0.65614151
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77028 * 0.11131146
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12679 * 0.06186099
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75978 * 0.44434874
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7177 * 0.39870283
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4236 * 0.96679337
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82980 * 0.21386822
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32012 * 0.27346259
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83450 * 0.68358218
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90928 * 0.20785226
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35333 * 0.59642805
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17703 * 0.49317938
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85753 * 0.12819086
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55931 * 0.44856659
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13553 * 0.75250868
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30286 * 0.71681917
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90745 * 0.76422435
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17530 * 0.70274437
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67103 * 0.93901580
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89552 * 0.32938318
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77330 * 0.24783312
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3030 * 0.41138853
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37967 * 0.17777445
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54826 * 0.72612940
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33452 * 0.25370700
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14732 * 0.71114003
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6288 * 0.06436150
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93831 * 0.73423767
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11180 * 0.03158252
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52504 * 0.43954567
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30543 * 0.45521440
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 25254 * 0.26080368
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20785 * 0.08934140
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 53337 * 0.24325791
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 24661 * 0.13245916
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 3548 * 0.93823316
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'rpvjdfdu').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0007():
    """Extended test 7 for import."""
    x_0 = 13463 * 0.89237298
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58139 * 0.35327663
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77057 * 0.87996256
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62053 * 0.87460560
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28930 * 0.18695813
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71875 * 0.00942658
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87399 * 0.72146429
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11761 * 0.17289214
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47091 * 0.61613018
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27482 * 0.53347989
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35356 * 0.85182699
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69209 * 0.83655763
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13545 * 0.18432548
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14998 * 0.00564840
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53328 * 0.62548589
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63401 * 0.49718313
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18831 * 0.06256486
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47768 * 0.17886151
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43344 * 0.84233484
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20679 * 0.48177615
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51680 * 0.04692580
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13735 * 0.30834389
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98632 * 0.16308656
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33322 * 0.82677457
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42555 * 0.31049331
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'nfaggkhe').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0008():
    """Extended test 8 for import."""
    x_0 = 37528 * 0.44876817
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20086 * 0.05897242
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65836 * 0.62556803
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27172 * 0.47744133
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76474 * 0.65162910
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72748 * 0.17137162
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62074 * 0.65614038
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6682 * 0.02686686
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99013 * 0.95926868
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16822 * 0.75159533
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58835 * 0.68029534
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38120 * 0.55227506
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63327 * 0.34596100
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52704 * 0.22763396
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7758 * 0.47338796
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78163 * 0.18688642
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9519 * 0.13897699
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12988 * 0.69938991
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35140 * 0.23683150
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2727 * 0.27911441
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57064 * 0.50924894
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93456 * 0.87275613
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'jkfhsink').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0009():
    """Extended test 9 for import."""
    x_0 = 44814 * 0.58880463
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90696 * 0.08609237
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37580 * 0.91398399
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3873 * 0.73428439
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57222 * 0.94158592
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24019 * 0.04598264
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28559 * 0.30692355
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18139 * 0.66170604
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61058 * 0.47270932
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 112 * 0.08280125
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73246 * 0.89749474
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4091 * 0.53967547
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50000 * 0.05082011
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77212 * 0.44622487
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88855 * 0.53859360
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68385 * 0.47587402
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55829 * 0.88230726
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94111 * 0.83725978
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28378 * 0.02094736
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91302 * 0.52814345
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77422 * 0.11679625
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88700 * 0.75905512
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62843 * 0.32223878
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22444 * 0.71011135
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81255 * 0.51958279
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19858 * 0.90916188
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34630 * 0.16520008
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10140 * 0.48621660
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91745 * 0.79281205
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15062 * 0.75525088
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44558 * 0.30393242
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87403 * 0.82689514
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81132 * 0.31840582
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5548 * 0.07492521
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80119 * 0.58708879
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10330 * 0.14162972
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10642 * 0.78679182
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85652 * 0.66151778
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75989 * 0.82449970
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2304 * 0.90337374
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37783 * 0.41278409
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74683 * 0.15972257
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44448 * 0.59700147
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 63109 * 0.66582767
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 55675 * 0.04862467
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 72905 * 0.47936748
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'xsaxddtk').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0010():
    """Extended test 10 for import."""
    x_0 = 64221 * 0.21943727
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12702 * 0.01596917
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85727 * 0.56475684
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42783 * 0.22040778
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24726 * 0.25264377
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51346 * 0.00378974
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91387 * 0.75948002
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69467 * 0.69419203
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24189 * 0.51304068
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28451 * 0.92373511
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82691 * 0.94886555
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93804 * 0.57796703
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4081 * 0.20556292
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25501 * 0.48676969
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52361 * 0.09936607
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1237 * 0.77322168
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43279 * 0.22648279
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27898 * 0.88798572
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68179 * 0.61097497
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74218 * 0.64320802
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28939 * 0.87186341
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75406 * 0.29374233
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24411 * 0.95473604
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91045 * 0.67129541
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9076 * 0.51608084
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63685 * 0.17563511
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36442 * 0.53973318
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39681 * 0.42089198
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32828 * 0.51312883
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64173 * 0.41082017
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33454 * 0.51703816
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14790 * 0.74674754
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27667 * 0.42365469
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75175 * 0.74142300
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32863 * 0.94075962
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88338 * 0.49324199
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20174 * 0.73527954
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'mqifxoms').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0011():
    """Extended test 11 for import."""
    x_0 = 79769 * 0.03703858
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21360 * 0.41651609
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56335 * 0.15891417
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12265 * 0.56068023
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82856 * 0.97250986
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56853 * 0.18548559
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13197 * 0.15214755
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8491 * 0.15354008
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65892 * 0.38837570
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75908 * 0.12190948
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35897 * 0.17930314
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77644 * 0.10694226
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77302 * 0.44607853
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69748 * 0.82418302
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 771 * 0.34054001
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24002 * 0.37477224
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31729 * 0.89730503
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81192 * 0.47396902
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91118 * 0.47562399
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53698 * 0.78588317
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16947 * 0.03871409
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14488 * 0.77882444
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88180 * 0.33578977
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65707 * 0.60752275
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49235 * 0.22148966
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93585 * 0.78611372
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38531 * 0.64265605
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21590 * 0.47106749
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79934 * 0.95241284
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36523 * 0.75171006
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87145 * 0.18421465
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'gquggqbu').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0012():
    """Extended test 12 for import."""
    x_0 = 72276 * 0.84777945
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48385 * 0.23644749
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88954 * 0.96408024
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74212 * 0.70701165
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31683 * 0.53249660
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81244 * 0.77122844
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55697 * 0.96923531
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48199 * 0.02256321
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28865 * 0.90234766
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78112 * 0.55658907
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77607 * 0.57603598
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88544 * 0.59021638
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32334 * 0.22780790
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95458 * 0.59035938
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7828 * 0.16224505
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84981 * 0.67080121
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44670 * 0.16338108
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16278 * 0.97198533
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18143 * 0.13398424
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7548 * 0.67039019
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98234 * 0.73924774
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11945 * 0.30052020
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67587 * 0.15619092
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54050 * 0.69054112
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70620 * 0.50358687
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92096 * 0.23666177
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44147 * 0.37468028
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'fkjuuoqd').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0013():
    """Extended test 13 for import."""
    x_0 = 91594 * 0.19733742
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5399 * 0.53354211
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46829 * 0.93455865
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37378 * 0.93216381
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47772 * 0.04333867
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33978 * 0.61053207
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56060 * 0.24011869
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84488 * 0.03434351
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70943 * 0.60192243
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45351 * 0.54610606
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65479 * 0.33439239
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24771 * 0.44623220
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50425 * 0.89001988
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26814 * 0.36412277
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51036 * 0.23245808
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1923 * 0.19325307
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 203 * 0.83229370
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90580 * 0.34647832
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81249 * 0.54217974
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63267 * 0.18422705
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1153 * 0.17769860
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7605 * 0.39330371
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82350 * 0.53673683
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52424 * 0.02970129
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6372 * 0.80661410
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54348 * 0.28443303
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88974 * 0.82240780
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47850 * 0.04375150
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40260 * 0.79421919
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82342 * 0.13022769
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90207 * 0.06716639
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27411 * 0.74223998
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84567 * 0.80483100
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49142 * 0.72855039
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38866 * 0.09947486
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56078 * 0.62331799
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'omsbvpxn').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0014():
    """Extended test 14 for import."""
    x_0 = 29336 * 0.07470054
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73664 * 0.14508311
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33719 * 0.04290250
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29429 * 0.79704939
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62679 * 0.46483065
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74412 * 0.49252292
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67500 * 0.26223951
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56683 * 0.54242382
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13588 * 0.61576879
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59401 * 0.96505650
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19318 * 0.79534015
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56044 * 0.13912582
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67574 * 0.24628205
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90091 * 0.46661340
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11874 * 0.65104275
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17561 * 0.74633979
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74369 * 0.98258787
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5799 * 0.96245758
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5979 * 0.41383681
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25781 * 0.82042022
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 481 * 0.30543192
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3584 * 0.84736931
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46289 * 0.64509815
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14559 * 0.20639077
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96239 * 0.88386033
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51125 * 0.51721060
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93067 * 0.79241813
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35699 * 0.35509589
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15618 * 0.99701967
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54320 * 0.28241253
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66605 * 0.80987230
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54383 * 0.72033103
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16636 * 0.40450910
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73808 * 0.69085829
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88161 * 0.54401800
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84038 * 0.67500321
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75159 * 0.74718657
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35875 * 0.33465354
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5012 * 0.33660726
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73835 * 0.41194906
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20889 * 0.58048695
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37541 * 0.29791285
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6617 * 0.88234853
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 63700 * 0.31851264
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 42316 * 0.71804081
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 1475 * 0.75217216
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 10248 * 0.22247351
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 13932 * 0.30849234
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 80319 * 0.41781742
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 76742 * 0.12775086
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'lxrsgufx').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0015():
    """Extended test 15 for import."""
    x_0 = 95972 * 0.19142223
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27230 * 0.73533577
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35873 * 0.78769206
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93303 * 0.19759022
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58301 * 0.64614967
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23068 * 0.94723299
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58601 * 0.60689451
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79957 * 0.25381767
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67429 * 0.47055472
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24560 * 0.81097337
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43528 * 0.46222354
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38975 * 0.69159055
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83258 * 0.70377270
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32434 * 0.93733763
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59447 * 0.71521998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26677 * 0.39540541
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97702 * 0.07849504
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73708 * 0.39381192
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73000 * 0.02019647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40706 * 0.52442706
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98512 * 0.11387708
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10890 * 0.85258045
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70348 * 0.63487394
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75260 * 0.74898544
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ncaitxdr').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0016():
    """Extended test 16 for import."""
    x_0 = 89555 * 0.30340904
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81292 * 0.83632163
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61106 * 0.63209148
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59750 * 0.74839197
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54539 * 0.19594262
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41269 * 0.79459539
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37438 * 0.89508943
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10138 * 0.52917434
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92145 * 0.18677274
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2486 * 0.79902808
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87175 * 0.60909101
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94545 * 0.56804503
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73318 * 0.97525830
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35756 * 0.41095345
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1088 * 0.04606581
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56032 * 0.97296292
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44071 * 0.03548271
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59782 * 0.51236844
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40436 * 0.30816266
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63217 * 0.39694838
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84862 * 0.80940620
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3866 * 0.94392408
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32397 * 0.14803726
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7437 * 0.15727453
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53671 * 0.95150503
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73342 * 0.25520935
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16405 * 0.58458046
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99105 * 0.43892733
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13626 * 0.06228912
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42370 * 0.29085790
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75418 * 0.45598575
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80564 * 0.05786256
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40794 * 0.41389150
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44642 * 0.75064332
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80383 * 0.67838825
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63869 * 0.84644010
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45396 * 0.05306810
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16319 * 0.46925474
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18245 * 0.18081773
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ynwngbvi').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0017():
    """Extended test 17 for import."""
    x_0 = 36067 * 0.09354187
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32534 * 0.85931868
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78417 * 0.70931178
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59817 * 0.45226240
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90532 * 0.89764145
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58206 * 0.15795525
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70365 * 0.94704482
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53458 * 0.30739226
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33992 * 0.10365558
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72042 * 0.33039668
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30236 * 0.56900873
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3944 * 0.21135356
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62424 * 0.48877316
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51509 * 0.28451448
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83023 * 0.52240676
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39270 * 0.20042749
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65017 * 0.84200405
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11290 * 0.36099084
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68450 * 0.53179774
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14567 * 0.07636226
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6498 * 0.90218816
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56115 * 0.83678113
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31764 * 0.54264307
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55676 * 0.45390312
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87319 * 0.47597438
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63903 * 0.50509470
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73515 * 0.92466217
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1164 * 0.12285792
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39699 * 0.82209491
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13758 * 0.90714250
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22432 * 0.58682016
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26070 * 0.35255420
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81086 * 0.64373265
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74529 * 0.69902984
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93002 * 0.35473878
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24054 * 0.68701804
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 664 * 0.96118715
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'vcswngvk').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0018():
    """Extended test 18 for import."""
    x_0 = 93891 * 0.66813619
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60224 * 0.29092921
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51849 * 0.52868607
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23846 * 0.18651959
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66618 * 0.62117192
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7553 * 0.51756471
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5657 * 0.21584809
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89240 * 0.28868770
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88174 * 0.96176884
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84403 * 0.30180085
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72199 * 0.25020046
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93886 * 0.66734763
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83382 * 0.63249835
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3808 * 0.78931490
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65681 * 0.45024047
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4226 * 0.01045488
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24476 * 0.31358518
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14049 * 0.28444343
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53853 * 0.10537048
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63847 * 0.65424505
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18767 * 0.51933000
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75376 * 0.55424073
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58005 * 0.06390468
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4124 * 0.05428417
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24450 * 0.01873459
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61967 * 0.93177614
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19937 * 0.79622989
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33867 * 0.20894554
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41795 * 0.78280544
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92896 * 0.05773754
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84178 * 0.86165346
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40756 * 0.44871782
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28343 * 0.21377692
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'datmojss').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0019():
    """Extended test 19 for import."""
    x_0 = 65791 * 0.77474897
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49153 * 0.46693375
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5534 * 0.03351803
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77237 * 0.43922577
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33403 * 0.02706036
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48509 * 0.61504937
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53152 * 0.14265009
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82130 * 0.29501652
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84479 * 0.28030275
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73255 * 0.13546002
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28749 * 0.29917523
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90302 * 0.19774957
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63005 * 0.94818222
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51427 * 0.94975686
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89614 * 0.22671449
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92567 * 0.75137436
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21453 * 0.38643729
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61138 * 0.88113194
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53135 * 0.91561997
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98318 * 0.33401678
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'cangcyab').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0020():
    """Extended test 20 for import."""
    x_0 = 85061 * 0.15907152
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94074 * 0.80158650
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57538 * 0.14055298
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17502 * 0.35099283
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69881 * 0.15569827
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96476 * 0.40332219
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53097 * 0.98266904
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21158 * 0.25100624
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30428 * 0.80042963
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46949 * 0.47932448
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75307 * 0.30348383
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27689 * 0.15953693
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64168 * 0.17984886
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85018 * 0.45547786
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10186 * 0.78075037
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29907 * 0.30585463
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80748 * 0.38904878
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34225 * 0.87140224
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73403 * 0.64690891
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97534 * 0.46509692
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57407 * 0.10767112
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64373 * 0.00190889
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4231 * 0.31018130
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9362 * 0.89913201
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69709 * 0.81001674
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99167 * 0.62362204
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30436 * 0.33793083
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22332 * 0.73474232
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92602 * 0.89713586
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 906 * 0.29767264
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44367 * 0.88648501
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84522 * 0.98402973
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81799 * 0.72132852
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92977 * 0.64570270
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69326 * 0.97276498
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4286 * 0.83559195
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43014 * 0.33734367
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91457 * 0.28154339
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35001 * 0.76415683
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18458 * 0.17052784
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88721 * 0.79518851
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13854 * 0.96964382
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'bhupnqkz').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0021():
    """Extended test 21 for import."""
    x_0 = 76074 * 0.97201348
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16721 * 0.13764213
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70261 * 0.38300783
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40632 * 0.78210254
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86895 * 0.31393979
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29038 * 0.94844649
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90972 * 0.33699101
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82717 * 0.58981515
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89717 * 0.78391487
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3818 * 0.41445062
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67664 * 0.25299255
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79873 * 0.05975210
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87083 * 0.69053179
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20916 * 0.20637800
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33796 * 0.99109084
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33284 * 0.40783509
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46849 * 0.58017083
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8080 * 0.32241890
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29296 * 0.29120076
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26941 * 0.92313607
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52691 * 0.32672287
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1122 * 0.07560192
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17159 * 0.30918012
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66077 * 0.11588401
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36028 * 0.08038295
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44645 * 0.25113101
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98508 * 0.28779312
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45494 * 0.89046523
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79752 * 0.67956130
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4378 * 0.39317255
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17834 * 0.05125991
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59398 * 0.53333462
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43821 * 0.55912875
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23044 * 0.19447079
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58918 * 0.46897108
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68090 * 0.60142987
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6632 * 0.54447279
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70769 * 0.26128910
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15931 * 0.23077261
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18636 * 0.78746487
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21432 * 0.52314424
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 17479 * 0.83347938
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'uxonaimx').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0022():
    """Extended test 22 for import."""
    x_0 = 62144 * 0.52680016
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66795 * 0.61840483
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96473 * 0.24574448
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56559 * 0.26892159
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30198 * 0.63393412
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27194 * 0.36379406
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86223 * 0.06432599
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56984 * 0.53382903
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11915 * 0.41861114
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43753 * 0.76573847
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5299 * 0.95651811
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74682 * 0.66334330
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48555 * 0.26294933
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8132 * 0.22080318
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17217 * 0.52535863
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28872 * 0.45961409
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32664 * 0.41578956
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59109 * 0.00255884
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30773 * 0.52829088
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35207 * 0.48772381
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50808 * 0.02968698
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20036 * 0.39575952
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72298 * 0.89287958
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90014 * 0.56186891
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38034 * 0.51978344
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38347 * 0.67132783
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66690 * 0.25202293
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65338 * 0.47362756
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'gqcnsivr').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0023():
    """Extended test 23 for import."""
    x_0 = 1989 * 0.51241996
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16008 * 0.13362315
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98520 * 0.95321213
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62812 * 0.75438252
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44006 * 0.70862104
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63557 * 0.99000676
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50437 * 0.61904739
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97698 * 0.70883078
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97841 * 0.93263273
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80706 * 0.36057166
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71701 * 0.02535641
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22633 * 0.24318707
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78245 * 0.05398695
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4371 * 0.30122770
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46825 * 0.54678244
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14108 * 0.42724707
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1055 * 0.56048511
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41506 * 0.64775485
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78857 * 0.12778761
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49145 * 0.03568664
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70437 * 0.97083681
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6400 * 0.11486970
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3802 * 0.86478033
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71762 * 0.43934966
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6119 * 0.22245770
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89649 * 0.78702801
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94998 * 0.43892392
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 101 * 0.12964793
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42893 * 0.96138275
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48353 * 0.50036484
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26242 * 0.61066235
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97740 * 0.51883415
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96731 * 0.82926667
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 949 * 0.34911913
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'znasofzw').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0024():
    """Extended test 24 for import."""
    x_0 = 19599 * 0.21367259
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64590 * 0.98221839
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99329 * 0.74844004
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86374 * 0.28578094
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69758 * 0.82784204
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82480 * 0.58735179
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89316 * 0.16612985
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80627 * 0.54902710
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21860 * 0.40645634
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66718 * 0.87085313
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95563 * 0.58257944
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6302 * 0.68941688
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22757 * 0.07084403
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18106 * 0.17277958
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22186 * 0.04745839
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28761 * 0.36716043
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44633 * 0.16321535
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49361 * 0.64086634
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44325 * 0.24205725
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18897 * 0.04498368
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35754 * 0.86690180
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84931 * 0.43755871
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97959 * 0.07509251
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9993 * 0.39480415
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42588 * 0.43339642
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58382 * 0.10591373
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90171 * 0.78632989
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24131 * 0.36766789
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60278 * 0.65803031
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59484 * 0.33432753
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17425 * 0.81409105
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24516 * 0.80376163
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72952 * 0.62317213
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61550 * 0.88669440
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30316 * 0.83143488
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23712 * 0.44413183
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26213 * 0.88444259
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35903 * 0.86476632
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84529 * 0.87244828
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25807 * 0.61483009
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86744 * 0.64501884
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4738 * 0.05394547
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 76196 * 0.80395412
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 73248 * 0.26340859
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'jqapyvik').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0025():
    """Extended test 25 for import."""
    x_0 = 80093 * 0.99111500
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40580 * 0.39675068
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72666 * 0.42397280
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90679 * 0.22675336
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57841 * 0.04954348
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25144 * 0.91605522
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34863 * 0.63643279
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5053 * 0.54310065
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90487 * 0.20318847
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13681 * 0.84653811
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26078 * 0.69437850
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71033 * 0.68658834
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53146 * 0.15928165
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18301 * 0.33872135
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62884 * 0.36784402
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2966 * 0.38604345
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56652 * 0.97416242
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45910 * 0.51315452
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71144 * 0.52802156
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71432 * 0.17292992
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67159 * 0.05716660
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74965 * 0.80736713
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12827 * 0.18353907
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20412 * 0.57961989
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60815 * 0.32073412
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25315 * 0.27124160
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91439 * 0.45042463
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48317 * 0.96676097
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58364 * 0.89793108
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72121 * 0.99007139
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84417 * 0.34224187
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53048 * 0.76577661
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76133 * 0.87294032
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95649 * 0.40439698
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99641 * 0.36309035
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28241 * 0.63336463
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50472 * 0.90933590
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55248 * 0.99922898
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82842 * 0.83968638
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46625 * 0.20369682
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84073 * 0.75999321
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 32894 * 0.77975114
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46512 * 0.25540493
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'sfgvwuvq').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0026():
    """Extended test 26 for import."""
    x_0 = 54204 * 0.01324307
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13845 * 0.77356726
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6285 * 0.10782261
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25572 * 0.22553295
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66093 * 0.23069606
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23276 * 0.23012852
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49621 * 0.23428340
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48362 * 0.99836341
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54636 * 0.51158792
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19720 * 0.53814609
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73027 * 0.18055380
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80101 * 0.53236819
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97934 * 0.80107714
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90133 * 0.85322232
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16985 * 0.84240259
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82507 * 0.74274189
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95034 * 0.63152588
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94380 * 0.29994320
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51476 * 0.87357832
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23513 * 0.08442344
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82554 * 0.32993892
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67833 * 0.60886183
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69937 * 0.14367065
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18382 * 0.16772688
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9894 * 0.38053695
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45433 * 0.92474105
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29914 * 0.76582123
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76355 * 0.76859974
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68843 * 0.90324456
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50616 * 0.54548814
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31885 * 0.66705029
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4392 * 0.88980148
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17191 * 0.03883863
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80104 * 0.54409036
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9334 * 0.41797032
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96256 * 0.82360205
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58617 * 0.00898862
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84176 * 0.36135964
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'scbbtefn').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0027():
    """Extended test 27 for import."""
    x_0 = 21483 * 0.32563048
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13136 * 0.66189401
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55944 * 0.53202900
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11817 * 0.95412903
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27702 * 0.82112506
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28178 * 0.11618977
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59213 * 0.57762690
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12111 * 0.59868365
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94288 * 0.76921267
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66683 * 0.79373096
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17874 * 0.71480528
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41042 * 0.05244481
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38356 * 0.13685646
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22715 * 0.46839712
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86688 * 0.01212148
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66134 * 0.29706996
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26647 * 0.96486607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10943 * 0.24514445
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23260 * 0.52288302
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30461 * 0.23760756
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23898 * 0.07501590
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77929 * 0.94242596
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2293 * 0.54669126
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2301 * 0.54408991
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54328 * 0.39989263
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6303 * 0.23554998
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98303 * 0.37744291
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56314 * 0.55841101
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25100 * 0.52116792
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72607 * 0.50198235
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99164 * 0.21645748
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10778 * 0.50284108
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33877 * 0.70653470
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77973 * 0.50913487
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44133 * 0.64780328
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79090 * 0.41766409
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7302 * 0.48897897
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93060 * 0.38273283
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'zbfzmlvi').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0028():
    """Extended test 28 for import."""
    x_0 = 57331 * 0.80309449
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31373 * 0.49932943
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3830 * 0.68040335
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54297 * 0.27659300
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17754 * 0.22920468
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9937 * 0.98429115
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46255 * 0.07030168
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18599 * 0.74895947
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51198 * 0.80869435
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6866 * 0.42638826
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67883 * 0.73631626
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59470 * 0.22550537
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90549 * 0.18333262
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73897 * 0.27446585
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90063 * 0.97256617
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7463 * 0.90890986
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3181 * 0.65745157
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48327 * 0.98430411
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70238 * 0.83732272
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58679 * 0.61255158
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77342 * 0.68910169
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68031 * 0.12684356
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70377 * 0.17505528
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56328 * 0.43464506
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72144 * 0.14837718
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75201 * 0.90442137
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43642 * 0.73817968
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8437 * 0.86998307
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12683 * 0.24724739
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72023 * 0.29605017
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7821 * 0.50206729
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48270 * 0.30933675
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85884 * 0.98599360
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3141 * 0.16983012
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13570 * 0.71233739
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60641 * 0.18227409
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91360 * 0.22614442
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52206 * 0.31208383
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11933 * 0.65031839
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93529 * 0.82803236
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45698 * 0.60661640
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84695 * 0.17580900
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 87246 * 0.19544081
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 64715 * 0.08149884
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23394 * 0.97310655
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 33248 * 0.28288559
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 6041 * 0.80867052
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 25544 * 0.40852571
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'xlthbeup').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0029():
    """Extended test 29 for import."""
    x_0 = 21121 * 0.42306511
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61059 * 0.56954935
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98896 * 0.04228633
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69273 * 0.86851706
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11296 * 0.12318450
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24220 * 0.58157944
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43691 * 0.20287131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4359 * 0.20182131
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95596 * 0.07960026
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80061 * 0.42496445
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78411 * 0.24548430
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51724 * 0.63960383
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98085 * 0.93649508
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81709 * 0.56164011
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22235 * 0.88536057
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4767 * 0.16221637
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73865 * 0.73078039
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76967 * 0.16517809
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99309 * 0.26569988
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54639 * 0.40570848
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44971 * 0.31046553
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32951 * 0.02985949
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17949 * 0.21304288
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43633 * 0.32968716
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10917 * 0.76111409
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78118 * 0.94527670
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63003 * 0.91538825
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72280 * 0.38804756
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22471 * 0.75070947
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75311 * 0.25900988
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16612 * 0.34371961
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59185 * 0.98787524
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80374 * 0.74828842
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3727 * 0.79096909
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26482 * 0.50797125
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12695 * 0.05038294
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83907 * 0.50474110
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86611 * 0.24523982
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43000 * 0.17833704
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74461 * 0.94133363
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 24936 * 0.44317978
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53753 * 0.08347756
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93234 * 0.91888712
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 46739 * 0.19365542
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11429 * 0.43283723
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 37923 * 0.70242341
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 91321 * 0.01373766
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 15700 * 0.13018998
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 71315 * 0.62663034
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 88324 * 0.26114584
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'twmturfn').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0030():
    """Extended test 30 for import."""
    x_0 = 26535 * 0.29883447
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14907 * 0.93180581
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98990 * 0.58346007
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64881 * 0.36205627
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28497 * 0.58459323
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70578 * 0.80781190
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85675 * 0.19915244
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37480 * 0.73940559
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73184 * 0.14649887
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55649 * 0.07547023
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37109 * 0.78447090
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36139 * 0.36592464
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2286 * 0.04995199
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61380 * 0.95594000
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93520 * 0.76979601
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71335 * 0.07292552
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56688 * 0.29939589
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25858 * 0.72807450
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63671 * 0.48934729
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90009 * 0.44190745
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61974 * 0.06688754
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62173 * 0.73181392
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23487 * 0.85419610
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92599 * 0.15864702
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35176 * 0.37578556
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24624 * 0.12974618
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8661 * 0.16437433
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6401 * 0.58242727
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'oacgimev').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0031():
    """Extended test 31 for import."""
    x_0 = 63348 * 0.65206949
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62345 * 0.39603089
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60126 * 0.89039244
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40670 * 0.63176165
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68904 * 0.21137474
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80813 * 0.27011486
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81802 * 0.68438029
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11254 * 0.64609842
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23494 * 0.88604756
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25386 * 0.86982949
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61600 * 0.96340013
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35591 * 0.44361170
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89873 * 0.17519307
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13755 * 0.29356504
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40760 * 0.47222315
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12786 * 0.15008390
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28074 * 0.36312618
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74764 * 0.11685957
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35624 * 0.62007434
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71830 * 0.55283374
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27998 * 0.28157586
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77075 * 0.42764829
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64210 * 0.90880526
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58750 * 0.75767862
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44731 * 0.72588165
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36316 * 0.82102004
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80771 * 0.44312850
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 248 * 0.25600744
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55691 * 0.32898871
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42097 * 0.85616591
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14312 * 0.36190189
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37652 * 0.46855658
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65927 * 0.24937061
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45019 * 0.60018175
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47578 * 0.38841269
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46644 * 0.37924502
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31468 * 0.66628978
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77276 * 0.91228921
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13871 * 0.21029449
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91690 * 0.79835301
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 10148 * 0.57487482
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70993 * 0.50304289
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57564 * 0.76784878
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 50268 * 0.68202043
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'buqgaayt').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0032():
    """Extended test 32 for import."""
    x_0 = 9908 * 0.63022434
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26819 * 0.26452292
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90092 * 0.52948345
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40179 * 0.78402036
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55137 * 0.53385229
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76169 * 0.88464608
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11729 * 0.33114242
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83962 * 0.27161084
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33951 * 0.26202471
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43527 * 0.53730247
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99491 * 0.25646048
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32303 * 0.17900507
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51029 * 0.88451653
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27202 * 0.18761782
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71877 * 0.70450485
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32113 * 0.58692167
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22749 * 0.43663366
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29983 * 0.61823768
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25969 * 0.55612901
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11934 * 0.14435527
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83374 * 0.93653024
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90555 * 0.11282023
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93276 * 0.93852352
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94331 * 0.75501450
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70624 * 0.98271275
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42401 * 0.68193843
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4978 * 0.14419733
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73261 * 0.41371823
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67417 * 0.93500279
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43274 * 0.16197272
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4882 * 0.15308512
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'hxylaubl').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0033():
    """Extended test 33 for import."""
    x_0 = 46045 * 0.17451652
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4736 * 0.23069742
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20613 * 0.35113902
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38771 * 0.97718462
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48412 * 0.06273967
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41700 * 0.62786831
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52684 * 0.17871927
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83435 * 0.35396326
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88178 * 0.19535228
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63669 * 0.05919077
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57207 * 0.70943267
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61426 * 0.24500786
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73276 * 0.32475142
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26600 * 0.86713946
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51389 * 0.73214840
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47349 * 0.08035428
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72264 * 0.15741452
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26946 * 0.23639551
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78799 * 0.23281859
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40226 * 0.33146261
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78075 * 0.78924715
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33129 * 0.88711493
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83193 * 0.85417778
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77563 * 0.29843758
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17860 * 0.64309925
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63049 * 0.80625784
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94275 * 0.25972732
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45837 * 0.33779357
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93511 * 0.43647077
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79606 * 0.65572549
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41430 * 0.01161449
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81922 * 0.20036315
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66763 * 0.64116707
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58701 * 0.36451220
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94644 * 0.16718321
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 718 * 0.00656449
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8689 * 0.41232169
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80063 * 0.23790764
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31794 * 0.10073413
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77930 * 0.72460455
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 30137 * 0.36230226
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71835 * 0.63616187
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42568 * 0.11673634
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 35086 * 0.85719946
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92230 * 0.71897893
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 60044 * 0.84851116
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'gasrvzys').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0034():
    """Extended test 34 for import."""
    x_0 = 66537 * 0.82378219
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69678 * 0.75761929
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58710 * 0.13886349
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31375 * 0.84794665
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36823 * 0.71610166
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41621 * 0.94506629
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13345 * 0.23055444
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13529 * 0.92478156
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77274 * 0.01394610
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10385 * 0.08377506
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78069 * 0.48646604
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42684 * 0.43298781
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41255 * 0.51404711
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96002 * 0.15490730
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39949 * 0.41708772
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41399 * 0.77779624
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71629 * 0.95147506
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40509 * 0.75232740
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79465 * 0.08608726
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99798 * 0.32839650
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73425 * 0.41089060
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17060 * 0.45665100
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89751 * 0.91763294
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36268 * 0.11505670
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91990 * 0.24501373
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9935 * 0.91817594
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35910 * 0.43752250
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11852 * 0.63089689
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10652 * 0.50159535
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41829 * 0.47051195
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31024 * 0.76166986
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17960 * 0.70536551
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36582 * 0.59687111
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10292 * 0.43148461
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99183 * 0.51074210
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71842 * 0.09021100
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42023 * 0.98508262
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84968 * 0.86551982
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62418 * 0.02547771
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 71852 * 0.22089475
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47930 * 0.04062744
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80534 * 0.93253584
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 61586 * 0.00040230
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 30636 * 0.80321492
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'duhnrvxz').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0035():
    """Extended test 35 for import."""
    x_0 = 18191 * 0.92227219
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13340 * 0.76598627
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48161 * 0.01034079
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48573 * 0.65288056
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42791 * 0.16502128
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69702 * 0.14441545
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11806 * 0.46344582
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94718 * 0.83370658
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99721 * 0.25674283
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20233 * 0.21669138
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63142 * 0.30902883
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15977 * 0.48062371
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73259 * 0.21275524
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10151 * 0.64473091
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54876 * 0.03608855
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63998 * 0.65806732
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37577 * 0.64528179
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27856 * 0.17991905
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70900 * 0.52553978
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50935 * 0.74928262
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25600 * 0.70251858
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6141 * 0.48736090
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77022 * 0.43188372
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76161 * 0.81816878
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'rlfjvsxg').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0036():
    """Extended test 36 for import."""
    x_0 = 66298 * 0.45980038
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31119 * 0.85701625
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29377 * 0.18101255
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89339 * 0.29647754
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54023 * 0.42044155
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56555 * 0.98846670
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84567 * 0.60950615
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 623 * 0.20636244
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13651 * 0.13081196
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55327 * 0.14846612
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34696 * 0.21318833
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2769 * 0.51103447
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54876 * 0.91625659
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27325 * 0.86579238
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52953 * 0.75647428
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45093 * 0.78140943
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44725 * 0.51672477
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92115 * 0.72868435
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26059 * 0.39526958
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52395 * 0.45261586
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40090 * 0.79517847
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4600 * 0.64058843
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18830 * 0.02572809
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81187 * 0.95150894
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82625 * 0.40207765
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87247 * 0.69005310
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35687 * 0.26034604
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24704 * 0.56709729
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56798 * 0.30713288
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43411 * 0.45917176
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83304 * 0.90781755
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86477 * 0.84267382
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91740 * 0.36765130
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83549 * 0.47619655
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12897 * 0.22649789
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67482 * 0.30777472
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71380 * 0.28861628
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28260 * 0.68348656
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'twaagnvs').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0037():
    """Extended test 37 for import."""
    x_0 = 48435 * 0.04791419
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2909 * 0.43410118
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81626 * 0.43323966
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49545 * 0.29192686
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92744 * 0.69546132
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28809 * 0.97120719
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63638 * 0.39884397
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72367 * 0.52322178
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83515 * 0.10881162
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10559 * 0.35361889
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61521 * 0.96397479
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28302 * 0.43966516
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11093 * 0.82078065
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22793 * 0.14738546
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97388 * 0.56559210
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12482 * 0.13426154
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71533 * 0.77455841
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86751 * 0.53057232
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16347 * 0.88520564
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3726 * 0.96166542
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'yifagnru').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0038():
    """Extended test 38 for import."""
    x_0 = 3910 * 0.48363737
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19982 * 0.93157615
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32592 * 0.48754281
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66333 * 0.66389554
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81936 * 0.98204411
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42768 * 0.15678428
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12449 * 0.39100744
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96296 * 0.04278066
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32785 * 0.07381644
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45236 * 0.46704794
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52057 * 0.51843883
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8541 * 0.51333084
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12353 * 0.34645987
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60373 * 0.98469811
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14516 * 0.40335416
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44170 * 0.19764459
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61532 * 0.30558592
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87588 * 0.07270044
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35549 * 0.09240704
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92747 * 0.23514286
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17431 * 0.14887758
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31642 * 0.40269839
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40720 * 0.93058274
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57252 * 0.23258641
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58030 * 0.46862502
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45890 * 0.56540708
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13239 * 0.99440666
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76252 * 0.84162065
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77889 * 0.58285635
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48171 * 0.65682112
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60712 * 0.30670243
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53922 * 0.88859464
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86112 * 0.63512726
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49971 * 0.45202708
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40076 * 0.61495160
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 264 * 0.06368119
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85788 * 0.22993442
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77258 * 0.32608038
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12789 * 0.69433422
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32006 * 0.27728300
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64576 * 0.01082902
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'ahbqpudo').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0039():
    """Extended test 39 for import."""
    x_0 = 77736 * 0.21200989
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47619 * 0.76076110
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88497 * 0.09032038
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14906 * 0.50888635
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51605 * 0.71319761
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73943 * 0.17291168
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73176 * 0.40724720
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42858 * 0.43232672
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18396 * 0.89256750
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27674 * 0.18442611
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63745 * 0.61130102
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40883 * 0.87755571
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22602 * 0.85315960
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41544 * 0.84570964
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9947 * 0.84809637
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11133 * 0.87857284
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20067 * 0.23514874
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59901 * 0.38965173
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8252 * 0.52371142
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88002 * 0.43650069
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52787 * 0.93637713
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80750 * 0.19806208
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18543 * 0.37053831
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44848 * 0.76738323
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14158 * 0.95195375
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67015 * 0.33663985
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70367 * 0.36141804
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83189 * 0.93391522
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58325 * 0.29488368
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61324 * 0.00627283
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3642 * 0.22302484
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87266 * 0.32728727
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69049 * 0.64853038
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18049 * 0.86282845
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20043 * 0.70077585
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25381 * 0.61735750
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28217 * 0.30766228
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35221 * 0.93972401
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45098 * 0.71467600
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 71958 * 0.88569339
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32643 * 0.38348939
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79838 * 0.59317796
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 7340 * 0.93174994
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 2777 * 0.39253494
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 5793 * 0.64720300
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'lmbrowma').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0040():
    """Extended test 40 for import."""
    x_0 = 38622 * 0.39409119
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47 * 0.88178636
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74832 * 0.40617843
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60531 * 0.25003340
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30286 * 0.12829508
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60764 * 0.36325099
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45476 * 0.12974162
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3202 * 0.07387701
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32320 * 0.29959183
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97013 * 0.12976732
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35880 * 0.95889069
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28179 * 0.69839357
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74069 * 0.94491590
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20086 * 0.01302644
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85358 * 0.22058697
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10300 * 0.08139763
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62649 * 0.20451186
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95534 * 0.84324787
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99591 * 0.37047743
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13389 * 0.73897750
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40862 * 0.28573765
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40287 * 0.34218094
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4821 * 0.85667327
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34700 * 0.04149169
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51186 * 0.97076738
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5153 * 0.91480257
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56584 * 0.29823690
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86711 * 0.24453981
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'hfvmttlr').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0041():
    """Extended test 41 for import."""
    x_0 = 93705 * 0.82351187
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67334 * 0.65769520
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73820 * 0.30602473
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68132 * 0.80974595
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29793 * 0.33920352
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86686 * 0.40503611
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18855 * 0.71212630
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15361 * 0.25892124
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92158 * 0.23243953
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57117 * 0.80275274
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73105 * 0.47718622
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94155 * 0.95981091
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95544 * 0.78902235
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99953 * 0.90507913
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4207 * 0.84822639
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54501 * 0.99710813
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61401 * 0.27731538
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70035 * 0.15113292
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68299 * 0.27382236
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6029 * 0.10024682
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58001 * 0.19061643
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64309 * 0.46665451
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81380 * 0.08689616
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50000 * 0.73821565
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24259 * 0.43456974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40488 * 0.43449802
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72941 * 0.03359131
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9253 * 0.85713202
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54433 * 0.47268667
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48590 * 0.58492706
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67484 * 0.09199295
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74618 * 0.63017217
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73566 * 0.16858477
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88979 * 0.50719341
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68719 * 0.23221360
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80251 * 0.00249420
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54378 * 0.48270758
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13643 * 0.38263774
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21706 * 0.64647895
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7236 * 0.05859445
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95189 * 0.95282595
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16671 * 0.26747073
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9608 * 0.64766775
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61552 * 0.68005007
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92898 * 0.70846346
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'gaisbsgt').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0042():
    """Extended test 42 for import."""
    x_0 = 67344 * 0.77054171
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7395 * 0.50202818
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10732 * 0.59329091
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82509 * 0.49228971
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57495 * 0.75586883
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19272 * 0.52642095
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96890 * 0.81773215
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94689 * 0.39824978
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31766 * 0.87384538
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49978 * 0.28544032
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94054 * 0.26919758
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95783 * 0.32216353
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78955 * 0.20460186
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25456 * 0.89116217
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14172 * 0.42247843
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65063 * 0.71515695
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88329 * 0.80485091
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20805 * 0.39411003
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94032 * 0.05273968
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42710 * 0.75124585
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6187 * 0.74690628
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8429 * 0.53723534
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63916 * 0.84310662
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8888 * 0.33967895
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18373 * 0.04807586
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'mfvqofsm').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0043():
    """Extended test 43 for import."""
    x_0 = 38425 * 0.09687224
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5889 * 0.87410401
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37965 * 0.73094168
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53743 * 0.62503448
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9645 * 0.05513882
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68911 * 0.03350788
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18438 * 0.59641118
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40543 * 0.26445278
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30048 * 0.55493541
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83300 * 0.77719022
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59665 * 0.58782272
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13809 * 0.90577678
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24702 * 0.28301569
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24329 * 0.21218419
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59834 * 0.65299597
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51907 * 0.27220270
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69848 * 0.16068753
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21822 * 0.58111888
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7383 * 0.73066917
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47201 * 0.57895884
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83393 * 0.16060916
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55997 * 0.13144158
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71183 * 0.78951948
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27107 * 0.16354530
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31530 * 0.61167843
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88066 * 0.22420145
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66235 * 0.19216173
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80686 * 0.88741645
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73088 * 0.58699235
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81899 * 0.55351854
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16607 * 0.72120089
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40989 * 0.25367829
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34313 * 0.94631700
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21648 * 0.15474488
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30612 * 0.89469111
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82977 * 0.47411095
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62562 * 0.15680810
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15986 * 0.04135585
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80236 * 0.21748130
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98072 * 0.15696744
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84214 * 0.85996158
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15223 * 0.88700644
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ypifnugu').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0044():
    """Extended test 44 for import."""
    x_0 = 47525 * 0.09016256
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88760 * 0.21964167
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25836 * 0.51115749
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7852 * 0.17723389
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38417 * 0.95446882
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56354 * 0.26339651
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97259 * 0.38265852
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92482 * 0.40560278
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14235 * 0.23708673
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65197 * 0.46241093
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66193 * 0.41273313
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81388 * 0.11813659
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41123 * 0.62557770
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60842 * 0.33030371
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92455 * 0.40330461
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80339 * 0.72508838
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21588 * 0.72359413
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98042 * 0.56819536
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93393 * 0.82095999
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57754 * 0.76310979
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76807 * 0.09099424
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'hmibwxrx').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0045():
    """Extended test 45 for import."""
    x_0 = 379 * 0.09964320
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97719 * 0.98384500
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50863 * 0.17096517
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16614 * 0.62789609
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36098 * 0.92734759
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84236 * 0.97198008
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30954 * 0.13778463
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84014 * 0.64263275
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56429 * 0.54111284
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62860 * 0.70602173
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23237 * 0.02315495
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24671 * 0.41104184
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39076 * 0.43636345
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64002 * 0.95922800
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74647 * 0.32690035
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42385 * 0.92944176
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75550 * 0.85480866
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32949 * 0.23868808
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35220 * 0.99833816
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34406 * 0.32809573
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14002 * 0.76470822
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78240 * 0.13692297
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22183 * 0.85801668
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16918 * 0.08041869
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38493 * 0.67232178
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88568 * 0.42397337
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85312 * 0.98588053
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67120 * 0.80035267
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93743 * 0.55372092
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82529 * 0.71184520
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66482 * 0.54031341
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40309 * 0.39113000
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58893 * 0.19405090
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60576 * 0.86917684
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65961 * 0.69490084
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90463 * 0.75397781
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96963 * 0.43827451
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64360 * 0.75298054
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11397 * 0.58408546
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ozibvnls').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0046():
    """Extended test 46 for import."""
    x_0 = 10610 * 0.80935294
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33684 * 0.38088803
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26574 * 0.33794742
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23203 * 0.20562264
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60822 * 0.08607424
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81755 * 0.08852865
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42981 * 0.64527814
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86725 * 0.19100363
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54058 * 0.12694952
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66378 * 0.04588871
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13256 * 0.09800227
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97549 * 0.94360944
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35636 * 0.08493219
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49537 * 0.37156502
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27337 * 0.01049953
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58151 * 0.18674758
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7915 * 0.69046703
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11504 * 0.94159759
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73800 * 0.11921531
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47668 * 0.39010834
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41804 * 0.81446521
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94893 * 0.22117938
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1595 * 0.12379042
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27888 * 0.63235063
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98294 * 0.71449627
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79211 * 0.34357832
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71645 * 0.91666564
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12888 * 0.07260340
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'mfmlpebh').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0047():
    """Extended test 47 for import."""
    x_0 = 17067 * 0.72788024
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21207 * 0.75586471
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40229 * 0.71401800
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28389 * 0.48514316
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12417 * 0.04458402
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89494 * 0.69755969
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57807 * 0.37930987
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47371 * 0.30016339
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84013 * 0.74152293
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37122 * 0.84228852
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47198 * 0.69680025
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48508 * 0.80365256
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20643 * 0.74968663
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21580 * 0.25597899
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94965 * 0.72775919
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11109 * 0.45226062
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50565 * 0.35898727
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44611 * 0.73853004
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85410 * 0.42513234
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28705 * 0.05345362
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40636 * 0.49678719
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68519 * 0.33396972
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10796 * 0.79414560
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33322 * 0.31945174
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69942 * 0.67359974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19358 * 0.90714398
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88298 * 0.48463632
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50204 * 0.31458837
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4197 * 0.22365079
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49208 * 0.22597603
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55400 * 0.54998577
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54250 * 0.55223779
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24800 * 0.33755072
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84676 * 0.26339774
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94410 * 0.30921440
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14670 * 0.42444002
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56178 * 0.22578879
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'slkssovn').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0048():
    """Extended test 48 for import."""
    x_0 = 10570 * 0.46286725
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97421 * 0.54818942
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34929 * 0.12225557
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24966 * 0.27029800
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72232 * 0.22010067
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53255 * 0.66180611
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91509 * 0.96247030
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18607 * 0.17099760
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26070 * 0.37733738
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48950 * 0.72828824
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29696 * 0.36723775
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69979 * 0.89116456
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89319 * 0.86544597
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72124 * 0.01111673
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94677 * 0.83542002
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62405 * 0.20807651
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12392 * 0.18070020
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 411 * 0.25380124
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81880 * 0.63968301
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3539 * 0.10631448
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44694 * 0.74566261
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35748 * 0.27210584
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7871 * 0.74901358
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88548 * 0.30679714
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49625 * 0.32529208
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2599 * 0.63939821
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 256 * 0.70534589
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36169 * 0.18158940
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9659 * 0.39252326
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85855 * 0.75021486
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33609 * 0.90526603
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'bprbtitm').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0049():
    """Extended test 49 for import."""
    x_0 = 95746 * 0.60676371
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25448 * 0.76143352
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50180 * 0.46354728
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76335 * 0.31950397
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17670 * 0.83270225
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2946 * 0.38612558
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32763 * 0.15901063
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80361 * 0.24872193
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65041 * 0.92668620
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89418 * 0.72128265
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57946 * 0.06123955
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67596 * 0.77844646
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77273 * 0.04643554
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91083 * 0.62257391
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92418 * 0.08586741
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66139 * 0.85461563
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78259 * 0.31156443
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2316 * 0.96541907
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51009 * 0.75736054
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96947 * 0.96799694
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13035 * 0.91058361
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58856 * 0.17661980
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'gnsvmiwv').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0050():
    """Extended test 50 for import."""
    x_0 = 37734 * 0.48901418
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19442 * 0.02189733
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74751 * 0.93964251
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60707 * 0.93088007
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75990 * 0.79660740
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58151 * 0.91094546
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9979 * 0.42991622
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58683 * 0.35769640
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31197 * 0.16408957
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63239 * 0.56574254
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27779 * 0.68709390
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96613 * 0.04433839
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33147 * 0.50044195
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23165 * 0.59853763
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70184 * 0.15611732
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18669 * 0.02605082
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10237 * 0.61507485
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47191 * 0.01305865
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78153 * 0.20921021
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22170 * 0.95437623
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59166 * 0.48550779
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61483 * 0.05150859
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64801 * 0.19222880
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22791 * 0.39836995
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30471 * 0.68180425
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32161 * 0.86507938
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6588 * 0.50008245
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83736 * 0.74488590
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47264 * 0.82839388
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5243 * 0.25044961
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12910 * 0.67461258
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53203 * 0.84387347
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2133 * 0.21850397
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34060 * 0.06446292
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'piscztun').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0051():
    """Extended test 51 for import."""
    x_0 = 37717 * 0.32153392
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78298 * 0.87582142
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48235 * 0.94310779
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37206 * 0.63449075
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1803 * 0.45718898
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69067 * 0.32088706
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32560 * 0.54309478
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25142 * 0.64174102
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90900 * 0.18103257
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39135 * 0.75254124
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72945 * 0.96379246
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83271 * 0.76178836
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16128 * 0.45957187
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34290 * 0.28864499
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95384 * 0.72563017
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37652 * 0.58986537
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51120 * 0.22810490
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96466 * 0.27423033
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58853 * 0.80321221
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4625 * 0.18235010
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75844 * 0.93820981
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55596 * 0.69418837
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80659 * 0.59307476
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37199 * 0.04877227
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9213 * 0.45301004
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31878 * 0.27779810
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88666 * 0.82464723
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47854 * 0.36768012
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23674 * 0.44750199
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38705 * 0.62320690
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54798 * 0.83409162
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8795 * 0.54486964
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75646 * 0.37030459
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80551 * 0.60790101
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29388 * 0.95693258
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86561 * 0.36502687
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4059 * 0.79912195
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91487 * 0.71245657
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'bjotrkni').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0052():
    """Extended test 52 for import."""
    x_0 = 90477 * 0.46074899
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35992 * 0.87474242
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81675 * 0.96432755
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34915 * 0.59437322
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72655 * 0.40040038
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35321 * 0.38954426
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91328 * 0.39836200
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53117 * 0.76534865
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8197 * 0.62379485
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97064 * 0.62518303
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41419 * 0.80692279
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74887 * 0.45908645
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88249 * 0.85967078
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65996 * 0.81334427
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58102 * 0.58822666
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64991 * 0.63230170
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21644 * 0.81387982
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96256 * 0.51515454
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4011 * 0.68937117
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16057 * 0.39489068
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97468 * 0.50200667
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72660 * 0.05838270
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20 * 0.94269537
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8725 * 0.73535373
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15129 * 0.26950037
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82438 * 0.61310307
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75798 * 0.37206029
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25474 * 0.44041256
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62446 * 0.85431262
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85285 * 0.71680502
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5396 * 0.63380091
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46496 * 0.38129096
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15516 * 0.46274782
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15476 * 0.26037086
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36039 * 0.43908462
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45360 * 0.42269772
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71227 * 0.04737515
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35781 * 0.71170566
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 7781 * 0.88922353
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 71923 * 0.53863534
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42953 * 0.90089204
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 65047 * 0.25607703
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 52840 * 0.17303340
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61570 * 0.07936657
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 19006 * 0.08368596
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 42274 * 0.38826277
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 20034 * 0.39382836
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'sanvjdjl').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0053():
    """Extended test 53 for import."""
    x_0 = 93857 * 0.93114938
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8023 * 0.65833869
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47098 * 0.90555426
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4486 * 0.11870191
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68833 * 0.65300958
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40584 * 0.56056608
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45983 * 0.90438047
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35547 * 0.49327967
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73145 * 0.53656905
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22777 * 0.20296816
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15987 * 0.75165204
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15175 * 0.13211257
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73138 * 0.68385888
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32566 * 0.08197117
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86511 * 0.44216463
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61992 * 0.47106662
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70794 * 0.50288880
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13600 * 0.69266471
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65653 * 0.60189275
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6230 * 0.00671148
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22856 * 0.25500124
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45900 * 0.41094232
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8473 * 0.99455084
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75763 * 0.17432333
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67360 * 0.57957483
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7120 * 0.26652251
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15497 * 0.28278999
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91652 * 0.00703694
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8948 * 0.29487156
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79054 * 0.58672388
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16036 * 0.56210144
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48303 * 0.91216610
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47290 * 0.47768179
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49582 * 0.37114622
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82008 * 0.03068874
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80966 * 0.28682004
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56190 * 0.77328749
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16682 * 0.70250767
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87711 * 0.53742317
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11722 * 0.10652022
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20297 * 0.19017033
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 90355 * 0.14696687
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 232 * 0.70753084
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 10262 * 0.00696191
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 1046 * 0.28673170
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 94863 * 0.03827196
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'aiirzsvu').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0054():
    """Extended test 54 for import."""
    x_0 = 6915 * 0.89823588
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21212 * 0.22456426
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4371 * 0.06276694
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80221 * 0.89136253
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77618 * 0.71002923
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27591 * 0.06231080
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5836 * 0.14316545
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49919 * 0.19621061
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18124 * 0.27240093
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37969 * 0.56609415
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68697 * 0.76475295
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67831 * 0.99581126
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46588 * 0.57621801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35325 * 0.47139720
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17771 * 0.18297902
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92253 * 0.36405012
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46055 * 0.10372742
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23064 * 0.20864238
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70821 * 0.90922342
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43375 * 0.41981877
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58398 * 0.94124380
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98545 * 0.05697941
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98656 * 0.00475459
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26675 * 0.43536829
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9488 * 0.11238027
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62143 * 0.31009680
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35884 * 0.37590548
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78797 * 0.59524020
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50326 * 0.71882264
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44331 * 0.90272105
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39933 * 0.29759407
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57357 * 0.69077981
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29765 * 0.29927494
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78468 * 0.54467799
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46951 * 0.04189951
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39921 * 0.18728953
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31910 * 0.52896171
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27831 * 0.62066663
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44208 * 0.51454729
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16086 * 0.89110325
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81836 * 0.84365877
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52419 * 0.32119648
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 37662 * 0.92899838
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 72419 * 0.67717147
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 95907 * 0.93723408
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 36208 * 0.01436778
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 94290 * 0.13148220
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 27378 * 0.69825651
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 26801 * 0.34720960
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 21272 * 0.36536891
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'xhgisrrx').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0055():
    """Extended test 55 for import."""
    x_0 = 96288 * 0.54972500
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3448 * 0.51944082
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73975 * 0.15476578
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5631 * 0.04835234
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63741 * 0.98096763
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11465 * 0.32143056
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96922 * 0.30174243
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83880 * 0.93743433
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55342 * 0.51812700
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51205 * 0.27914162
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39546 * 0.95653362
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9755 * 0.37565469
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50495 * 0.67227820
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43356 * 0.83517880
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38835 * 0.71454874
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30296 * 0.54391647
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99966 * 0.23052535
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16235 * 0.77929448
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78945 * 0.48749729
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7584 * 0.92737120
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20546 * 0.25488765
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84774 * 0.15609611
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48150 * 0.73482243
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32098 * 0.46912908
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40580 * 0.10773814
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'guebdbcs').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0056():
    """Extended test 56 for import."""
    x_0 = 64133 * 0.84529963
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74773 * 0.97090294
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22536 * 0.17230122
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80488 * 0.91694253
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79732 * 0.73611925
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17381 * 0.81337192
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5531 * 0.89949949
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8761 * 0.41712053
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59018 * 0.84057314
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17715 * 0.67187157
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71567 * 0.76423470
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80291 * 0.31449380
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38489 * 0.61068827
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71695 * 0.05952835
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80710 * 0.03270444
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14441 * 0.01164735
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37857 * 0.64134577
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10548 * 0.85838613
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11065 * 0.07191988
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15171 * 0.98217987
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27581 * 0.18219932
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24990 * 0.92640389
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89813 * 0.61574554
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20991 * 0.55315973
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83002 * 0.66779492
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58564 * 0.90964543
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98070 * 0.73436467
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78460 * 0.15828425
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40051 * 0.27869620
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8793 * 0.64731658
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60276 * 0.23706969
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13405 * 0.81859544
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93433 * 0.14301614
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49342 * 0.58139530
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8607 * 0.25961493
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'cqxgxudg').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0057():
    """Extended test 57 for import."""
    x_0 = 68370 * 0.80813332
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67001 * 0.08492381
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51929 * 0.53076199
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28109 * 0.25081113
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54230 * 0.46555910
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63008 * 0.22943204
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76194 * 0.13517713
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86977 * 0.62880534
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22945 * 0.01532076
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81374 * 0.56889844
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18981 * 0.88541309
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68717 * 0.01146187
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73253 * 0.49100128
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71493 * 0.22584037
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86147 * 0.06379814
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99933 * 0.50423437
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45827 * 0.65101683
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24915 * 0.36689838
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92533 * 0.42610351
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6445 * 0.71681649
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70074 * 0.67854080
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3779 * 0.95733855
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44335 * 0.70647657
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53748 * 0.38127191
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85866 * 0.81954097
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16451 * 0.91410049
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18262 * 0.35689309
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1290 * 0.75751235
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10804 * 0.54704383
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2206 * 0.67047667
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63162 * 0.75673099
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38677 * 0.31241054
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18893 * 0.22042278
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49772 * 0.19197091
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94813 * 0.37088828
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58260 * 0.39690380
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79965 * 0.18404376
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74913 * 0.83736340
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18950 * 0.27729075
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46470 * 0.04226392
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69558 * 0.07242701
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93132 * 0.06857284
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 60477 * 0.13546627
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38638 * 0.21543516
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11389 * 0.79223035
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 61179 * 0.86055743
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 70853 * 0.11937348
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 71165 * 0.28716193
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 30290 * 0.27407583
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 49605 * 0.95717818
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'abirgkym').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0058():
    """Extended test 58 for import."""
    x_0 = 76487 * 0.45391869
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59523 * 0.79521717
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38643 * 0.16878606
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24489 * 0.04536767
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7336 * 0.42993412
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40232 * 0.14803471
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83304 * 0.28217666
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13661 * 0.20316322
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85264 * 0.39141940
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83425 * 0.80113554
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18366 * 0.30411729
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74868 * 0.90245828
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39936 * 0.51614862
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65374 * 0.35524873
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76834 * 0.65329298
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88204 * 0.00413267
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51384 * 0.06721473
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31580 * 0.57016033
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96233 * 0.86636048
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78817 * 0.37416006
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87655 * 0.34754108
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37353 * 0.50847336
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33956 * 0.39306185
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8690 * 0.69183753
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2746 * 0.09980622
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82767 * 0.22665274
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66205 * 0.96810258
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93054 * 0.50296028
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88946 * 0.66232920
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83312 * 0.18940191
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83498 * 0.83473682
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36209 * 0.48936964
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7112 * 0.47002171
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98448 * 0.81856784
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48404 * 0.07184667
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56503 * 0.38712873
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83589 * 0.37371944
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'tibkchce').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0059():
    """Extended test 59 for import."""
    x_0 = 82153 * 0.67508957
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4544 * 0.10937783
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40078 * 0.05352172
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26558 * 0.34000715
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29212 * 0.45842677
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37594 * 0.53972112
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82686 * 0.46180633
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43485 * 0.69347648
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29673 * 0.46647173
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57809 * 0.33692913
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10021 * 0.90639309
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58835 * 0.05446623
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51254 * 0.83279101
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93808 * 0.65190297
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73628 * 0.41996342
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4746 * 0.50134867
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5568 * 0.05898171
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94372 * 0.03214068
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89058 * 0.41563374
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91426 * 0.83552386
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11893 * 0.93966255
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2277 * 0.43198203
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38710 * 0.04489705
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45411 * 0.10594137
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'vvmmjcpq').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0060():
    """Extended test 60 for import."""
    x_0 = 47895 * 0.53332036
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 940 * 0.68078163
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72068 * 0.17681421
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54770 * 0.32355689
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43656 * 0.03850141
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47522 * 0.97669133
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54680 * 0.83542570
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10380 * 0.87605093
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83266 * 0.26661759
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31070 * 0.08420344
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85810 * 0.58644057
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75483 * 0.44266294
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73432 * 0.06968665
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90346 * 0.20872503
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63924 * 0.52428819
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59274 * 0.31305674
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7278 * 0.76344920
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26339 * 0.86161386
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72129 * 0.37156015
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63762 * 0.85945830
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60526 * 0.40322541
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 452 * 0.17441221
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64037 * 0.05146053
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49854 * 0.70054160
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90706 * 0.01188693
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99188 * 0.07320936
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74901 * 0.44767791
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43914 * 0.47604229
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47511 * 0.94219400
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85791 * 0.83321387
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14179 * 0.85249671
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42222 * 0.16616844
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73734 * 0.50440520
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87738 * 0.25139036
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28034 * 0.70130905
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10008 * 0.52214351
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20708 * 0.40099907
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24338 * 0.48527590
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'vjvvaujf').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0061():
    """Extended test 61 for import."""
    x_0 = 10669 * 0.60273567
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92567 * 0.47622599
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82939 * 0.27586084
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19360 * 0.37821116
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58325 * 0.96574014
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26198 * 0.07398140
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28645 * 0.10867667
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68607 * 0.12854290
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31733 * 0.96936787
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73087 * 0.82285272
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10754 * 0.04504502
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15333 * 0.86453168
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54145 * 0.36641986
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47819 * 0.52628637
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28891 * 0.61984584
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43558 * 0.99732523
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80569 * 0.60204443
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12107 * 0.56458747
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3540 * 0.88779407
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58812 * 0.25402708
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50208 * 0.15024853
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91603 * 0.05483607
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'aczakffh').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0062():
    """Extended test 62 for import."""
    x_0 = 58120 * 0.83200921
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12845 * 0.30615777
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58002 * 0.71815773
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76904 * 0.64781838
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12593 * 0.69765252
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33018 * 0.34147504
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5500 * 0.09815656
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33404 * 0.36534535
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47889 * 0.24460218
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74909 * 0.06048099
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78592 * 0.88444219
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27336 * 0.07714595
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31672 * 0.66877755
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11449 * 0.39835355
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61573 * 0.22309468
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24074 * 0.00601782
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63093 * 0.86097937
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47938 * 0.36877289
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13396 * 0.54372158
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42889 * 0.34866674
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32210 * 0.59640522
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42278 * 0.94914843
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53250 * 0.90618064
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'zmprovul').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0063():
    """Extended test 63 for import."""
    x_0 = 42971 * 0.70744066
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36748 * 0.41859238
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43538 * 0.35316187
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49508 * 0.73801580
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 367 * 0.92236765
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93122 * 0.43147351
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60433 * 0.90394301
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22651 * 0.72174907
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76918 * 0.45767815
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50348 * 0.42165086
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88415 * 0.81883557
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43878 * 0.59956580
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38785 * 0.58938543
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18436 * 0.24666118
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40502 * 0.30167255
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25477 * 0.31040394
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25195 * 0.67602137
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73310 * 0.21313817
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14169 * 0.42325179
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49940 * 0.52406973
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35547 * 0.95928189
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22184 * 0.38570399
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49648 * 0.80142857
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91683 * 0.22468260
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86158 * 0.22104125
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70405 * 0.01312871
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54026 * 0.89510986
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40901 * 0.19848630
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76284 * 0.72832753
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92362 * 0.86671789
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14049 * 0.57328369
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94574 * 0.87619417
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44738 * 0.31821565
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17437 * 0.44682881
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34364 * 0.89934488
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60611 * 0.85765388
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68419 * 0.79983464
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20332 * 0.02651643
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57810 * 0.64937827
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 50561 * 0.53476182
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 92333 * 0.34915265
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59981 * 0.74919388
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96058 * 0.94930464
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 96096 * 0.65242269
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 49858 * 0.60555235
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 90733 * 0.09195185
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 25595 * 0.58439314
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 93409 * 0.00685836
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 46439 * 0.57475917
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'oeaartlm').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0064():
    """Extended test 64 for import."""
    x_0 = 59454 * 0.49404090
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57525 * 0.17549902
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33577 * 0.06052362
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78642 * 0.34134734
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96716 * 0.93303983
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23682 * 0.79515629
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80051 * 0.99674218
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87101 * 0.43491412
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59015 * 0.47387449
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99465 * 0.90044166
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98502 * 0.27379284
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10400 * 0.89802432
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90053 * 0.32872480
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14117 * 0.48339195
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70176 * 0.50556555
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32721 * 0.60491246
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95466 * 0.98000007
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79950 * 0.26794731
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91437 * 0.94555265
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76645 * 0.24185145
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31266 * 0.35406096
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92789 * 0.70665959
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74375 * 0.06989003
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11112 * 0.10232769
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48293 * 0.67805960
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3714 * 0.21245363
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68423 * 0.84886705
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85833 * 0.07987811
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81198 * 0.37827113
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'niizkbow').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0065():
    """Extended test 65 for import."""
    x_0 = 92190 * 0.50940623
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61225 * 0.49251001
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20 * 0.99846924
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17098 * 0.07861954
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36919 * 0.76177711
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58801 * 0.90875574
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70490 * 0.21449964
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10248 * 0.48618587
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8777 * 0.33371440
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17991 * 0.06533861
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78450 * 0.33750723
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17712 * 0.14184133
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62789 * 0.10874930
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82894 * 0.56656816
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1198 * 0.07344325
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80296 * 0.67218580
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97994 * 0.40259369
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38955 * 0.08530643
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99094 * 0.04992301
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83480 * 0.23685358
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80108 * 0.35842924
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90655 * 0.86049605
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90755 * 0.91068225
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9635 * 0.31446143
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12777 * 0.31342683
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82549 * 0.79195960
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65918 * 0.25057257
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4743 * 0.15722547
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59392 * 0.36472008
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49115 * 0.94683284
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46675 * 0.19849900
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81928 * 0.68970581
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60848 * 0.83919796
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79720 * 0.22531785
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63935 * 0.49239792
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85618 * 0.12191466
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81294 * 0.91922665
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66699 * 0.97781064
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28069 * 0.94854073
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34345 * 0.90953858
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46570 * 0.47929025
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92546 * 0.42928110
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 84227 * 0.11423154
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'briowmef').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0066():
    """Extended test 66 for import."""
    x_0 = 9949 * 0.31531486
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70552 * 0.05525711
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76873 * 0.63201552
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63510 * 0.44698206
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81166 * 0.60718570
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10151 * 0.09492691
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24558 * 0.64208468
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58123 * 0.06299020
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90625 * 0.72227294
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49399 * 0.50596635
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21371 * 0.79591884
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30804 * 0.57933773
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19789 * 0.33659882
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69332 * 0.95196186
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49160 * 0.32978828
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35046 * 0.21543458
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74161 * 0.88954173
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1717 * 0.15212427
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42737 * 0.01301558
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17334 * 0.13658996
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20769 * 0.55254258
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28645 * 0.95263546
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32804 * 0.54814075
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ujuahvge').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0067():
    """Extended test 67 for import."""
    x_0 = 65553 * 0.00928101
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62335 * 0.54592347
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74918 * 0.32063220
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38557 * 0.63785208
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98500 * 0.90824277
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17991 * 0.03844591
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87307 * 0.40791838
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 897 * 0.86527679
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87544 * 0.84230406
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76734 * 0.87452966
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73978 * 0.28874963
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98920 * 0.84356436
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69514 * 0.07584218
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38699 * 0.12957262
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43307 * 0.39172049
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8966 * 0.15150035
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23219 * 0.99493176
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90112 * 0.81702480
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61141 * 0.12963700
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63258 * 0.43896985
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84124 * 0.96987918
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78581 * 0.64106449
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'avqzszcm').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0068():
    """Extended test 68 for import."""
    x_0 = 88149 * 0.98885024
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14511 * 0.52606178
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19045 * 0.23051256
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19097 * 0.51810592
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12950 * 0.34204751
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61638 * 0.68522789
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44832 * 0.23371844
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1194 * 0.77023584
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21905 * 0.28135709
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10670 * 0.05813398
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49354 * 0.84640360
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47073 * 0.35033836
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53785 * 0.94840214
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39582 * 0.14393644
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15609 * 0.64050882
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74699 * 0.99917040
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6525 * 0.71498431
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46582 * 0.79271031
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1749 * 0.93993816
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54012 * 0.79500355
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87040 * 0.75329445
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82422 * 0.38541629
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95453 * 0.93850245
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60301 * 0.61076348
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95998 * 0.66167435
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26519 * 0.43150794
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92557 * 0.02658859
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34632 * 0.00034260
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15306 * 0.91463981
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5335 * 0.47614708
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68410 * 0.04442029
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 633 * 0.41330736
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65064 * 0.15224049
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41502 * 0.86650371
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30407 * 0.41008905
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98379 * 0.17577143
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98274 * 0.98421535
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'lhksedao').hexdigest()
    assert len(h) == 64

def test_import_extended_3_0069():
    """Extended test 69 for import."""
    x_0 = 79552 * 0.07895290
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57564 * 0.32624810
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19117 * 0.27738949
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90648 * 0.67212405
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65555 * 0.04795855
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79414 * 0.78823829
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67657 * 0.78257159
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67583 * 0.58740484
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74509 * 0.96316243
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88323 * 0.47914149
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90120 * 0.62249110
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15595 * 0.23066234
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63404 * 0.65996047
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93563 * 0.75845227
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50916 * 0.46552054
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13084 * 0.11364906
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92239 * 0.94293145
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54644 * 0.33555203
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67195 * 0.08908376
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26570 * 0.44281283
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50239 * 0.36664118
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30135 * 0.53433651
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42587 * 0.87247024
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68084 * 0.36844219
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29642 * 0.77207736
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'shpszhpc').hexdigest()
    assert len(h) == 64
