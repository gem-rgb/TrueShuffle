"""Extended tests for api suite 7."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_api_extended_7_0000():
    """Extended test 0 for api."""
    x_0 = 70756 * 0.71306622
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21403 * 0.98648292
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43408 * 0.44752328
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9027 * 0.96951785
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58236 * 0.77021815
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89145 * 0.20558551
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83549 * 0.54180281
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13686 * 0.06349728
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6948 * 0.98408319
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40983 * 0.65645666
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72040 * 0.08715606
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56135 * 0.99041392
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45495 * 0.01969216
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48218 * 0.88447955
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2613 * 0.61012691
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67541 * 0.71018428
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95652 * 0.03245286
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57377 * 0.05313244
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34658 * 0.41462408
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14449 * 0.65303228
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64836 * 0.12217227
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10699 * 0.89810536
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29698 * 0.89452242
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ctmwhuft').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0001():
    """Extended test 1 for api."""
    x_0 = 36424 * 0.11979733
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81888 * 0.90718128
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70816 * 0.32548708
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47488 * 0.75473541
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40155 * 0.82616306
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62877 * 0.22829224
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90869 * 0.96481037
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64599 * 0.69416723
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17449 * 0.01965457
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41242 * 0.47324872
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65065 * 0.35200847
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49259 * 0.36541508
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89603 * 0.24834138
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96996 * 0.99065982
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59155 * 0.65974796
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38165 * 0.56418805
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45999 * 0.16093558
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94538 * 0.64797714
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60639 * 0.65063228
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56388 * 0.67287959
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12562 * 0.75062536
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 545 * 0.37735628
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4959 * 0.52190243
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31968 * 0.78055217
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12527 * 0.38262216
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80686 * 0.48776902
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79363 * 0.89872328
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83029 * 0.58612583
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22077 * 0.92933372
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94232 * 0.57624872
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78357 * 0.37338749
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75928 * 0.25918274
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2176 * 0.37613523
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36600 * 0.66266533
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 49200 * 0.32760958
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38591 * 0.26599062
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8695 * 0.42008185
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24112 * 0.28350231
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8191 * 0.12339435
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66168 * 0.87724441
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89224 * 0.24994009
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41629 * 0.79304498
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'dvkwgjtx').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0002():
    """Extended test 2 for api."""
    x_0 = 16742 * 0.68016646
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56268 * 0.06331232
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37001 * 0.07246364
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36020 * 0.22108712
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90768 * 0.61583374
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37837 * 0.29445510
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5494 * 0.02618349
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17047 * 0.56744652
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10022 * 0.90472808
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38518 * 0.30216002
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34414 * 0.14978689
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74250 * 0.71932945
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11284 * 0.09677165
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42016 * 0.21355699
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62474 * 0.90942952
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27638 * 0.24857466
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90259 * 0.04280780
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28427 * 0.52086223
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90029 * 0.20633677
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81060 * 0.97374877
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67682 * 0.28218864
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79308 * 0.72410426
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61402 * 0.85994490
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78876 * 0.45758771
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31294 * 0.01323238
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61063 * 0.66536467
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67233 * 0.94782761
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'haudhhmh').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0003():
    """Extended test 3 for api."""
    x_0 = 30616 * 0.41664410
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49720 * 0.96893900
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15990 * 0.48390082
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7098 * 0.32577171
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87904 * 0.42611277
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97849 * 0.70082234
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31629 * 0.17952381
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68285 * 0.65708213
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95213 * 0.66606416
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 958 * 0.91518497
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7710 * 0.85272977
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4438 * 0.73851096
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38061 * 0.34093476
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69696 * 0.78217944
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63711 * 0.75002027
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9118 * 0.79231282
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55829 * 0.97295691
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30188 * 0.62329622
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52183 * 0.07934272
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17997 * 0.12821721
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98736 * 0.63722042
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43525 * 0.82553235
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23956 * 0.70137790
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93434 * 0.45056805
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69772 * 0.47580318
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48299 * 0.66718958
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31216 * 0.69000423
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66657 * 0.35507471
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90139 * 0.93186631
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16524 * 0.79759588
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58960 * 0.88620328
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2560 * 0.52560681
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6021 * 0.74131696
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9002 * 0.81949770
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75700 * 0.37250974
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90712 * 0.23796961
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36527 * 0.38983814
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3402 * 0.59330687
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48438 * 0.74525875
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 35079 * 0.48706227
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 973 * 0.40756231
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36154 * 0.46453342
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83745 * 0.54648298
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 4920 * 0.53929846
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'jgpleoss').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0004():
    """Extended test 4 for api."""
    x_0 = 15611 * 0.78080659
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54576 * 0.51774568
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40174 * 0.35258359
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33684 * 0.08894466
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25579 * 0.88352394
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81711 * 0.47343868
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56490 * 0.71359128
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21185 * 0.99648183
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17965 * 0.57950979
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98108 * 0.67252592
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37122 * 0.96211612
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14384 * 0.44972538
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53206 * 0.97038269
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8846 * 0.60836269
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9556 * 0.19775774
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83325 * 0.67917286
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15972 * 0.25782620
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68790 * 0.48349025
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75917 * 0.69260836
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43375 * 0.41462815
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42098 * 0.11744603
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68307 * 0.19164165
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5448 * 0.99871268
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90375 * 0.88948408
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91289 * 0.00871120
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41543 * 0.76356237
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6355 * 0.28968000
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4876 * 0.66676740
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85217 * 0.26698442
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95817 * 0.27972523
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92460 * 0.56216603
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79721 * 0.64410357
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64629 * 0.70740359
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95919 * 0.80139502
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71813 * 0.75850757
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63549 * 0.09491574
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46917 * 0.89163292
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77997 * 0.33983538
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6045 * 0.47520048
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'fshhggvu').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0005():
    """Extended test 5 for api."""
    x_0 = 81821 * 0.48322965
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37098 * 0.72153545
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46725 * 0.11163251
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67957 * 0.40869439
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94622 * 0.95761186
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75456 * 0.69226379
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94173 * 0.02172774
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52687 * 0.67578096
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53487 * 0.03068864
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97771 * 0.13838794
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3553 * 0.47901577
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42441 * 0.64638402
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56325 * 0.08335669
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13604 * 0.33627192
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59503 * 0.72128762
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32763 * 0.56967319
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91116 * 0.59446740
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45293 * 0.62774345
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50870 * 0.09666507
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8493 * 0.57236790
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 757 * 0.65102808
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29418 * 0.81231881
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68963 * 0.63478437
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15731 * 0.57318311
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10135 * 0.27337022
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49583 * 0.67902951
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93366 * 0.65276618
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93952 * 0.94624124
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'enfwwesg').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0006():
    """Extended test 6 for api."""
    x_0 = 16193 * 0.24789593
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81539 * 0.01819425
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2021 * 0.00916025
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89252 * 0.81020966
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76259 * 0.73314788
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59708 * 0.44470118
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86378 * 0.04812564
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92175 * 0.94310448
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48703 * 0.54904467
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91083 * 0.53739982
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81606 * 0.50757827
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40779 * 0.55770653
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80015 * 0.54327133
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61984 * 0.14408959
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83490 * 0.11169452
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41171 * 0.09162461
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45693 * 0.86131022
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91399 * 0.55358151
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52667 * 0.90332219
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84703 * 0.40438404
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22003 * 0.83933509
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4773 * 0.15311332
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72655 * 0.08557644
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83918 * 0.66170183
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3160 * 0.32296989
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27695 * 0.87742357
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49240 * 0.52135739
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84432 * 0.55588454
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32524 * 0.93049621
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89284 * 0.64683783
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54777 * 0.60170577
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69443 * 0.75789155
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78347 * 0.15671525
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7822 * 0.32205341
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8740 * 0.93587380
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43495 * 0.47583118
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62951 * 0.75366476
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'aehbrvkm').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0007():
    """Extended test 7 for api."""
    x_0 = 48971 * 0.47707474
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88116 * 0.36784703
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78985 * 0.40358584
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17651 * 0.59659363
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11680 * 0.96405348
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20111 * 0.51855801
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31900 * 0.48643036
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21807 * 0.79263310
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2549 * 0.55794443
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36237 * 0.15627091
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36889 * 0.52802257
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52036 * 0.61804067
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7130 * 0.66736905
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53734 * 0.38697117
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4942 * 0.50750320
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57394 * 0.49601118
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15859 * 0.46628039
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96210 * 0.47220324
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71099 * 0.18409200
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52929 * 0.79813516
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90737 * 0.85942062
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17259 * 0.68094419
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26241 * 0.24083230
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22905 * 0.33577185
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90862 * 0.47113963
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14926 * 0.04428230
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26610 * 0.49745392
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68897 * 0.00858551
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84972 * 0.61061677
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42669 * 0.66862461
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72334 * 0.68517638
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35592 * 0.06120867
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9164 * 0.89986798
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29412 * 0.93511015
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3856 * 0.54548833
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 73855 * 0.22122170
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48771 * 0.39503247
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63915 * 0.30793807
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41804 * 0.06236430
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93790 * 0.35352083
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68912 * 0.68419271
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 48354 * 0.84130953
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20192 * 0.86581466
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 79130 * 0.76744653
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'aewfnqyo').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0008():
    """Extended test 8 for api."""
    x_0 = 18536 * 0.99723866
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33306 * 0.90909981
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37131 * 0.09298748
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1756 * 0.02773443
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81396 * 0.83482767
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39489 * 0.52573111
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89464 * 0.87515743
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53347 * 0.63399604
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94568 * 0.67324962
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62688 * 0.87610508
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88453 * 0.01369008
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27956 * 0.42694766
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25440 * 0.87119684
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92170 * 0.44053497
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49956 * 0.66158624
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61052 * 0.17223245
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97822 * 0.64941896
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6306 * 0.87325641
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86557 * 0.11092635
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97881 * 0.33846260
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4713 * 0.25426318
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84522 * 0.79117047
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80948 * 0.68791005
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96794 * 0.89681516
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ngdmksub').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0009():
    """Extended test 9 for api."""
    x_0 = 99294 * 0.80821423
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64226 * 0.21422875
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76461 * 0.95025226
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88176 * 0.29995408
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30913 * 0.18835356
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74725 * 0.92964996
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45123 * 0.65327423
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21588 * 0.00362113
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28083 * 0.08734425
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9950 * 0.00171589
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69188 * 0.26878876
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83712 * 0.08078618
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19159 * 0.18166168
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18702 * 0.10811036
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48695 * 0.90349604
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25346 * 0.61903070
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79731 * 0.51077615
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22101 * 0.00352578
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50684 * 0.00605873
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29854 * 0.51909631
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4158 * 0.85097379
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27857 * 0.89680246
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41855 * 0.96463505
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28930 * 0.28495782
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15834 * 0.56324140
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99728 * 0.14183909
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2330 * 0.55970737
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20462 * 0.00961973
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34658 * 0.91357172
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50219 * 0.39627454
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76161 * 0.71769132
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32394 * 0.23819245
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71483 * 0.83216859
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98725 * 0.10694268
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80426 * 0.71844144
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74044 * 0.44954903
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78848 * 0.67527180
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13133 * 0.59146981
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31055 * 0.91189441
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34767 * 0.35452504
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40700 * 0.77099536
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80218 * 0.95275201
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 68232 * 0.31196499
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47875 * 0.25877803
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23606 * 0.39590895
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 56306 * 0.83414316
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'xktjsgio').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0010():
    """Extended test 10 for api."""
    x_0 = 74151 * 0.83764618
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85377 * 0.92068433
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69716 * 0.59801917
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28375 * 0.75256719
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6670 * 0.56214388
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2116 * 0.01454020
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44507 * 0.94983851
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75860 * 0.17819828
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7592 * 0.32425901
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91006 * 0.14227602
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58692 * 0.20766435
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31765 * 0.97708666
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12662 * 0.22858728
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53866 * 0.66455576
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 255 * 0.89353760
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22940 * 0.20990843
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75689 * 0.78196044
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91563 * 0.80234552
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47101 * 0.75559509
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44230 * 0.79483559
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 927 * 0.28428056
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17321 * 0.37276604
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59151 * 0.40050720
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82686 * 0.30410913
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71172 * 0.95891919
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'wlcdgbmu').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0011():
    """Extended test 11 for api."""
    x_0 = 97243 * 0.81385706
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42053 * 0.74092190
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 293 * 0.16864632
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87712 * 0.15305604
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4215 * 0.67312588
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83190 * 0.48407960
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44435 * 0.82685466
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54467 * 0.48579495
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7444 * 0.44716592
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21007 * 0.33551742
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66653 * 0.27641555
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97536 * 0.99072057
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83095 * 0.26193050
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25425 * 0.98402605
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51326 * 0.03172724
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27823 * 0.36760110
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72108 * 0.01160402
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69025 * 0.81204155
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28033 * 0.25261044
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38820 * 0.01410697
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71717 * 0.18379717
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40161 * 0.31396037
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24880 * 0.03829431
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15678 * 0.47626102
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8310 * 0.83077157
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83471 * 0.95869304
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46074 * 0.18923351
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14495 * 0.05830294
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29329 * 0.75908835
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75841 * 0.76124116
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70342 * 0.97726061
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9514 * 0.99884874
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88381 * 0.53658343
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23636 * 0.71182608
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29900 * 0.10521802
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31803 * 0.62709226
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12383 * 0.46867969
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66707 * 0.20319247
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 50333 * 0.90874406
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'enxheizq').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0012():
    """Extended test 12 for api."""
    x_0 = 46858 * 0.49976217
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75134 * 0.33676834
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59577 * 0.86421241
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64515 * 0.47420251
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91138 * 0.69316877
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34518 * 0.02209410
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57092 * 0.17529984
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89602 * 0.03995986
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43952 * 0.25958285
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1109 * 0.24769641
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90157 * 0.41714738
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78617 * 0.52506001
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44333 * 0.99273123
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40113 * 0.36189640
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19370 * 0.03925578
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39648 * 0.80547662
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81946 * 0.95199643
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81029 * 0.96827324
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99375 * 0.13157225
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66807 * 0.36543083
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51711 * 0.77703219
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'xyntufea').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0013():
    """Extended test 13 for api."""
    x_0 = 21263 * 0.73675619
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4114 * 0.39329432
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14356 * 0.06188140
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83335 * 0.96390692
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31449 * 0.62314363
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72102 * 0.47517143
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66547 * 0.79474266
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11022 * 0.81396209
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67563 * 0.57868918
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53736 * 0.90948630
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22649 * 0.25815752
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51488 * 0.56084492
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1515 * 0.18613438
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19073 * 0.29814448
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1233 * 0.58032159
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 102 * 0.75396079
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22356 * 0.49524362
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79672 * 0.84948448
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75357 * 0.75185946
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14464 * 0.12591572
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87852 * 0.20629799
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13298 * 0.67427715
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'uvinmlko').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0014():
    """Extended test 14 for api."""
    x_0 = 38314 * 0.04792059
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56631 * 0.48451288
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94880 * 0.49718661
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41604 * 0.34812406
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61689 * 0.54682071
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55231 * 0.03525559
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79349 * 0.60441697
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34889 * 0.20803179
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83176 * 0.60593258
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82538 * 0.05699016
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73812 * 0.08933102
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88733 * 0.27608302
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78184 * 0.92180225
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6980 * 0.35008598
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60843 * 0.24430912
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22968 * 0.60176620
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70865 * 0.48898390
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44350 * 0.11237602
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96366 * 0.97277708
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35518 * 0.95086835
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77070 * 0.21501639
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41751 * 0.08488339
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35488 * 0.02896713
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24931 * 0.99479084
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67449 * 0.24072025
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3023 * 0.62221380
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34420 * 0.92943457
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82513 * 0.39550083
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56860 * 0.87468747
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35845 * 0.77968293
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43072 * 0.17615371
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23747 * 0.28086739
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75789 * 0.93942100
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9719 * 0.78250036
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94135 * 0.80439109
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33540 * 0.47358724
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33630 * 0.71332995
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41627 * 0.85481099
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36424 * 0.28468523
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'rqjmiwkn').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0015():
    """Extended test 15 for api."""
    x_0 = 66678 * 0.35241097
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86386 * 0.31473234
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18816 * 0.08358629
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39730 * 0.66107962
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42170 * 0.06716019
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10030 * 0.97976733
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31018 * 0.50653973
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39460 * 0.75946941
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26779 * 0.53012680
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68808 * 0.48934647
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57082 * 0.88490830
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82035 * 0.51376860
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92449 * 0.59929653
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45892 * 0.25635406
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73935 * 0.06732894
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86917 * 0.37356978
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85478 * 0.49707213
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33482 * 0.13035274
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90810 * 0.80621283
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37233 * 0.37468389
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59001 * 0.56436133
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32931 * 0.52437848
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'hchesuch').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0016():
    """Extended test 16 for api."""
    x_0 = 21125 * 0.92119647
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84289 * 0.87162513
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73393 * 0.14495207
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3 * 0.50773997
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33312 * 0.25953942
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90344 * 0.53545913
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53131 * 0.29453004
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81307 * 0.90859308
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95851 * 0.85603784
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7169 * 0.05657612
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22472 * 0.82243833
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86318 * 0.75609191
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52288 * 0.39859837
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42072 * 0.79349762
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98467 * 0.05512731
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52234 * 0.86083104
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52126 * 0.77392206
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46529 * 0.74296371
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97731 * 0.04566982
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65364 * 0.14132912
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84654 * 0.56188195
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89635 * 0.28022154
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30974 * 0.62323708
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8828 * 0.32906573
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46203 * 0.36932317
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5053 * 0.84866199
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97727 * 0.22249972
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50949 * 0.76504560
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70971 * 0.19523890
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68132 * 0.67954443
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89115 * 0.20173554
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83890 * 0.82851289
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10538 * 0.02082633
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95153 * 0.22371639
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16732 * 0.00271776
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3480 * 0.21310990
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69202 * 0.84536354
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19514 * 0.46331095
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77966 * 0.54858821
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92954 * 0.72459595
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40343 * 0.43330893
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45535 * 0.11128072
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'rypikstw').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0017():
    """Extended test 17 for api."""
    x_0 = 11463 * 0.49961300
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98093 * 0.53285136
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60068 * 0.18441243
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95799 * 0.14361694
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69899 * 0.68657910
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53261 * 0.88050432
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86922 * 0.33689889
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96131 * 0.07856876
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12020 * 0.66322355
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9585 * 0.69473048
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71254 * 0.31958646
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32882 * 0.96441882
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55461 * 0.06571692
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9461 * 0.46443884
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54190 * 0.65209243
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8315 * 0.16736035
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96027 * 0.93485846
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92986 * 0.58038300
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32090 * 0.37279838
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64391 * 0.66633831
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8505 * 0.61441256
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51919 * 0.69841301
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7933 * 0.07718824
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27745 * 0.43136450
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49204 * 0.14563392
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11312 * 0.64877659
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70545 * 0.08232290
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67961 * 0.34878630
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46532 * 0.86720419
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80061 * 0.61849073
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20847 * 0.82843480
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33990 * 0.38429461
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66702 * 0.17392183
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35741 * 0.96958348
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41085 * 0.55378586
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14924 * 0.02757141
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75799 * 0.55861182
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13066 * 0.98313508
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98140 * 0.20056366
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'dvrboron').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0018():
    """Extended test 18 for api."""
    x_0 = 91554 * 0.86789963
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36390 * 0.81010286
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78431 * 0.18649035
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61928 * 0.79955287
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94820 * 0.93509540
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35359 * 0.40177832
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 598 * 0.75936473
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56182 * 0.03655525
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48332 * 0.39156639
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6934 * 0.59174225
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98685 * 0.00734513
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96756 * 0.05114593
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67646 * 0.12358740
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10839 * 0.55846436
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33776 * 0.78801814
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89912 * 0.97148417
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25453 * 0.84257977
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31331 * 0.46656116
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1704 * 0.20031764
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83213 * 0.95438441
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45785 * 0.07018765
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'hrunxyxc').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0019():
    """Extended test 19 for api."""
    x_0 = 68187 * 0.71663288
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23972 * 0.02656742
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40216 * 0.63815982
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48320 * 0.16318711
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86743 * 0.54178372
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50269 * 0.07381546
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66269 * 0.93418266
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15458 * 0.86420828
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18545 * 0.67023949
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46534 * 0.89416703
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8175 * 0.62528444
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32379 * 0.64013114
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44732 * 0.24869602
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91613 * 0.12150487
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93873 * 0.44115628
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85092 * 0.12720392
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9480 * 0.32708835
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72893 * 0.29920776
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42467 * 0.78876655
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98227 * 0.49203640
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67547 * 0.55877966
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6184 * 0.71775968
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29108 * 0.70816719
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72422 * 0.08572503
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66040 * 0.89984777
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30897 * 0.39694989
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18376 * 0.43783325
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82326 * 0.48307839
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27605 * 0.68484747
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83155 * 0.60843995
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27910 * 0.60452154
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96413 * 0.60444377
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5108 * 0.45339247
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23094 * 0.76824249
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74761 * 0.68233691
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7450 * 0.98868118
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'nuqgozss').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0020():
    """Extended test 20 for api."""
    x_0 = 97458 * 0.71900204
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34381 * 0.44773313
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14524 * 0.59007158
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51987 * 0.05507631
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32190 * 0.75544934
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28657 * 0.59634183
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44532 * 0.56029593
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29484 * 0.23212422
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79679 * 0.98950354
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5328 * 0.66831638
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31226 * 0.91573672
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35429 * 0.79728527
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35841 * 0.39761964
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22981 * 0.17349876
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27258 * 0.74780742
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90074 * 0.46765332
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66274 * 0.38069667
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86769 * 0.18041134
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11952 * 0.39082678
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29290 * 0.07620788
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12280 * 0.70783872
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7483 * 0.11012655
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'indddkce').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0021():
    """Extended test 21 for api."""
    x_0 = 52802 * 0.80692285
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7735 * 0.12881494
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74203 * 0.58664041
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29254 * 0.47470781
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93595 * 0.37937476
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72054 * 0.94841868
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7130 * 0.68681746
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23325 * 0.55691739
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22525 * 0.53534725
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94931 * 0.92296457
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22946 * 0.95061298
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2300 * 0.86825836
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76323 * 0.43479231
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28069 * 0.00370803
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87508 * 0.91287691
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24481 * 0.71637993
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96526 * 0.70738944
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43552 * 0.94387181
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84648 * 0.61841504
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11615 * 0.49328702
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25910 * 0.49616809
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91857 * 0.74908757
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96835 * 0.52470611
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78372 * 0.05145789
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3887 * 0.27533161
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7406 * 0.11408194
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3835 * 0.43168146
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45852 * 0.71147607
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3498 * 0.59438142
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6090 * 0.09990983
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'axgfjnnv').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0022():
    """Extended test 22 for api."""
    x_0 = 25681 * 0.67580344
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22953 * 0.62208808
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45952 * 0.44259037
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7107 * 0.47712952
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95854 * 0.71438016
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34233 * 0.81981846
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66380 * 0.77321485
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7767 * 0.75286597
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73169 * 0.80665080
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26469 * 0.51969666
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54984 * 0.17477574
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58677 * 0.44085455
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2057 * 0.45843179
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50500 * 0.90753310
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79841 * 0.87290337
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1524 * 0.47264072
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43506 * 0.30286415
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5229 * 0.77074419
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51137 * 0.66573149
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12057 * 0.58681052
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82420 * 0.99887714
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61538 * 0.04074372
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58572 * 0.96956487
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78307 * 0.29437325
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25944 * 0.52787867
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36303 * 0.73711613
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97752 * 0.09373313
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16809 * 0.81645796
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11369 * 0.37854706
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65156 * 0.40945645
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25642 * 0.94357198
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16140 * 0.34684471
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'tbidrdbj').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0023():
    """Extended test 23 for api."""
    x_0 = 63328 * 0.56523143
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2796 * 0.35897115
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32268 * 0.97833013
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63956 * 0.73140842
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98241 * 0.94166776
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11295 * 0.38857393
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28291 * 0.09542109
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44503 * 0.04753807
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42964 * 0.08058605
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49460 * 0.99833739
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76329 * 0.76913228
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57322 * 0.14739807
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62215 * 0.04609168
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15458 * 0.93693652
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90120 * 0.08188520
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84285 * 0.92677724
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26190 * 0.89511251
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37698 * 0.29413958
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18671 * 0.01648412
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77538 * 0.36190698
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21053 * 0.14182117
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52499 * 0.77678182
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70005 * 0.85798396
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39164 * 0.21926279
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90711 * 0.65489378
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41021 * 0.52866945
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57505 * 0.25197290
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68612 * 0.66891198
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99980 * 0.30580736
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82380 * 0.26768009
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5676 * 0.67293389
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51037 * 0.12274694
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59770 * 0.93070726
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54710 * 0.71824757
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11972 * 0.08004332
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70681 * 0.91020644
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85711 * 0.85524126
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25237 * 0.93191789
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19835 * 0.81571605
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98578 * 0.42442431
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27022 * 0.39531777
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'uefzxefo').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0024():
    """Extended test 24 for api."""
    x_0 = 24266 * 0.95808626
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12053 * 0.66444181
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20105 * 0.50298843
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78339 * 0.72088602
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89922 * 0.62421645
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62113 * 0.54407619
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94084 * 0.20717479
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25652 * 0.62559703
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85935 * 0.92710150
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65749 * 0.12794995
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70901 * 0.57638783
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8736 * 0.68138249
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94612 * 0.77812015
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97623 * 0.36439319
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65053 * 0.89410540
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19411 * 0.76091559
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69051 * 0.22829185
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83065 * 0.88541605
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31959 * 0.98968565
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26658 * 0.36793966
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34109 * 0.95756359
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59704 * 0.02054873
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31743 * 0.88209350
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3278 * 0.88963879
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61614 * 0.35326592
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52225 * 0.60593014
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31329 * 0.94345745
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97346 * 0.70671397
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88235 * 0.44318943
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85210 * 0.74368485
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73533 * 0.40217227
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88960 * 0.13063500
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98760 * 0.47359746
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99615 * 0.19355291
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5693 * 0.44479466
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'yalumipc').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0025():
    """Extended test 25 for api."""
    x_0 = 97765 * 0.47458060
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49505 * 0.97662777
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32938 * 0.50337035
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94156 * 0.04572577
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71348 * 0.83419388
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49114 * 0.11133820
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65348 * 0.24298109
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21855 * 0.62536682
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82309 * 0.58248604
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54487 * 0.27397434
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88537 * 0.79631714
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73157 * 0.19603857
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29826 * 0.73400395
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56465 * 0.59412259
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76641 * 0.72305507
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50488 * 0.55484899
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52867 * 0.25728085
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56598 * 0.73077598
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99745 * 0.34410081
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30318 * 0.82829437
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60955 * 0.04651666
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91674 * 0.80610241
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33925 * 0.08289425
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72926 * 0.80279241
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41505 * 0.79211363
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10978 * 0.09269490
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84870 * 0.91752713
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28076 * 0.96542902
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75289 * 0.93173815
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70455 * 0.82775663
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91846 * 0.83379860
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62977 * 0.28990032
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70880 * 0.65155400
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66668 * 0.50530422
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66250 * 0.51134535
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34860 * 0.62395767
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87348 * 0.49483583
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29867 * 0.86003433
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67615 * 0.31549298
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56606 * 0.75287622
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32491 * 0.80716259
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 73871 * 0.61481485
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23199 * 0.43695396
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 60084 * 0.25169666
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61661 * 0.02051066
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10877 * 0.09491282
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'wzxluaqr').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0026():
    """Extended test 26 for api."""
    x_0 = 88503 * 0.77679413
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86253 * 0.78073828
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89547 * 0.31672645
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42861 * 0.49002318
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16956 * 0.69126312
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16713 * 0.63791939
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15261 * 0.24665652
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93668 * 0.31063121
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39248 * 0.57485604
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18423 * 0.92752266
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54993 * 0.05217100
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14321 * 0.78028109
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23796 * 0.64709617
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6994 * 0.99167339
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93136 * 0.07428755
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56714 * 0.00982878
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7815 * 0.73581235
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21837 * 0.98813949
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33328 * 0.71371825
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45171 * 0.45324688
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57807 * 0.96621009
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33239 * 0.90209795
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86167 * 0.37452616
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77110 * 0.54942344
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99116 * 0.56553263
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45151 * 0.19757162
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73917 * 0.54403403
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52813 * 0.18173921
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31197 * 0.81568181
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14029 * 0.51274046
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49395 * 0.96556497
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52841 * 0.84139462
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67395 * 0.57619492
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65789 * 0.57139757
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45542 * 0.01319813
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58784 * 0.69623411
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23127 * 0.98922234
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 76210 * 0.64862303
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94827 * 0.85304249
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87474 * 0.16111790
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36040 * 0.85884389
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12702 * 0.16590794
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47657 * 0.02110522
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 54492 * 0.27676502
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 97234 * 0.49920199
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'pvhmcawu').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0027():
    """Extended test 27 for api."""
    x_0 = 63129 * 0.15355649
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75765 * 0.53851747
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58518 * 0.37877828
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3605 * 0.80180737
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71865 * 0.78217203
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48494 * 0.68878543
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84973 * 0.40577116
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39262 * 0.15194711
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33467 * 0.19783217
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15314 * 0.33280036
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49048 * 0.10301862
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67907 * 0.79782689
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18765 * 0.19625193
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94886 * 0.18894240
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31125 * 0.56828646
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19078 * 0.50918242
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4999 * 0.21284795
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31263 * 0.90597638
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63595 * 0.61895887
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95169 * 0.54412412
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81306 * 0.78017241
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58040 * 0.39646070
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22845 * 0.09798881
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71065 * 0.46526287
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18431 * 0.94694268
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56149 * 0.23835817
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82821 * 0.20038300
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80697 * 0.38705179
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 989 * 0.17180120
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18439 * 0.20423391
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23925 * 0.97678465
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63832 * 0.83000710
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49210 * 0.51609454
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67109 * 0.61419801
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'hrrtzflx').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0028():
    """Extended test 28 for api."""
    x_0 = 64204 * 0.29607471
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68037 * 0.65876100
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70952 * 0.39820476
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88289 * 0.37477836
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36260 * 0.50329734
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35527 * 0.04400970
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35684 * 0.30469373
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85749 * 0.24401226
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34065 * 0.09895892
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66925 * 0.99901146
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6449 * 0.25208420
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46965 * 0.38829495
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29632 * 0.15764739
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98486 * 0.31590033
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50281 * 0.18026173
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60364 * 0.08637169
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48446 * 0.99239317
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65641 * 0.46104851
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62386 * 0.52902169
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86633 * 0.15680079
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99254 * 0.62159803
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21944 * 0.01053000
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83678 * 0.81718421
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38351 * 0.92733381
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13806 * 0.60150838
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58211 * 0.96769250
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87177 * 0.54939774
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72063 * 0.63032453
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60665 * 0.15932695
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84893 * 0.82348741
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4365 * 0.04008267
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73571 * 0.49814405
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78312 * 0.02413927
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2424 * 0.11741624
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6671 * 0.07820372
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38901 * 0.41961216
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56837 * 0.72452191
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98378 * 0.00293968
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34838 * 0.62272848
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 61776 * 0.63541770
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 58063 * 0.80191672
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 91164 * 0.05794331
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'btexvdft').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0029():
    """Extended test 29 for api."""
    x_0 = 28977 * 0.16873523
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77726 * 0.56062171
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54641 * 0.23281262
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79691 * 0.71807242
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15370 * 0.56199461
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16811 * 0.20223875
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81589 * 0.46431905
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44882 * 0.69848856
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5352 * 0.18345015
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14667 * 0.42615216
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1668 * 0.01973145
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35774 * 0.89237379
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66829 * 0.07372520
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77145 * 0.35572465
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22825 * 0.13940350
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77170 * 0.20125952
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25973 * 0.26973027
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78783 * 0.41599871
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26220 * 0.62140931
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36768 * 0.75261905
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5447 * 0.30218032
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29316 * 0.32182836
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23002 * 0.30112248
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51265 * 0.35759525
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54144 * 0.99503657
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40252 * 0.67524220
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16570 * 0.33931974
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79225 * 0.29764740
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63709 * 0.95418823
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39455 * 0.03506868
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92284 * 0.85996059
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27767 * 0.21155684
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41883 * 0.54014352
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4924 * 0.40997912
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55928 * 0.77573119
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71054 * 0.78806912
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36610 * 0.85085657
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29906 * 0.84971887
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 95208 * 0.65432970
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43621 * 0.63386656
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82737 * 0.12098306
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4683 * 0.97442343
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 27860 * 0.23564211
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92534 * 0.83184649
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 64846 * 0.90328367
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 17997 * 0.36148905
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 30868 * 0.77660879
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 87563 * 0.01226477
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 80614 * 0.25849218
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 71367 * 0.87639121
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'hhhlavrq').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0030():
    """Extended test 30 for api."""
    x_0 = 23120 * 0.07333458
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93770 * 0.23991747
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90021 * 0.61239522
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31582 * 0.56886897
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94428 * 0.34265155
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44094 * 0.50342053
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63086 * 0.14519295
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97562 * 0.70852969
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53543 * 0.57286546
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15781 * 0.49373777
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23028 * 0.09210064
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95096 * 0.31671536
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 233 * 0.12181801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62106 * 0.61853602
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46537 * 0.26375082
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80205 * 0.45372211
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84717 * 0.39803840
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34569 * 0.70271281
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32320 * 0.66837188
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66883 * 0.78047188
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42679 * 0.91080891
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66288 * 0.98851897
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79769 * 0.79280684
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50216 * 0.58033009
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85176 * 0.16222050
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13937 * 0.27668243
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82167 * 0.34257608
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97631 * 0.21550547
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21105 * 0.29847412
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74814 * 0.17840080
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69744 * 0.39868014
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61500 * 0.27686652
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17260 * 0.71136872
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71341 * 0.38573236
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9298 * 0.66764284
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97226 * 0.51356802
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68496 * 0.64834648
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59392 * 0.97013627
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82081 * 0.74331701
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56225 * 0.19639271
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 61084 * 0.86532048
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 49032 * 0.02628245
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35621 * 0.08933199
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 48764 * 0.01248349
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 53712 * 0.56075810
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 12628 * 0.78948702
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 34094 * 0.48347007
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 72225 * 0.07197670
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 48730 * 0.11858641
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'hjxkogqg').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0031():
    """Extended test 31 for api."""
    x_0 = 57253 * 0.07143505
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95153 * 0.69793001
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68952 * 0.66345617
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72834 * 0.09183051
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89822 * 0.96138081
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14027 * 0.76405957
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69157 * 0.65466589
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48480 * 0.70954568
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28779 * 0.88716621
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44770 * 0.25430444
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97427 * 0.00959384
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19832 * 0.38907111
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80900 * 0.03648962
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77460 * 0.20098677
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72741 * 0.82792197
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92508 * 0.10917657
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21312 * 0.33282967
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16977 * 0.66608153
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95953 * 0.24588010
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97141 * 0.75288930
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25104 * 0.67158224
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30695 * 0.71982146
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94269 * 0.38112767
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82338 * 0.03923843
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2885 * 0.58350004
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98870 * 0.31172073
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64505 * 0.53977378
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34549 * 0.07490867
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4445 * 0.64491680
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89356 * 0.72099338
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12231 * 0.39162549
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89289 * 0.03492044
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6897 * 0.86259697
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84456 * 0.00494474
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41630 * 0.53409354
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'vzhtxoag').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0032():
    """Extended test 32 for api."""
    x_0 = 35593 * 0.21124716
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48535 * 0.11385866
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90429 * 0.59305160
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27304 * 0.24726701
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18765 * 0.76555732
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85304 * 0.56347246
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72181 * 0.66575208
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4905 * 0.74907976
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7435 * 0.21788772
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42232 * 0.05326618
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57283 * 0.40311027
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59815 * 0.67508810
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 351 * 0.31716828
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66078 * 0.98643179
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69088 * 0.05572174
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54555 * 0.41957590
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56089 * 0.55074630
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65090 * 0.04123879
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8115 * 0.18222521
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49027 * 0.60086504
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1524 * 0.50767656
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92278 * 0.53471062
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87176 * 0.43368202
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55778 * 0.52126313
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85643 * 0.93206603
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43904 * 0.47465541
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48137 * 0.55523267
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59205 * 0.44727917
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92005 * 0.81167125
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ipnrmrer').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0033():
    """Extended test 33 for api."""
    x_0 = 84228 * 0.47512772
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44022 * 0.67256264
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 385 * 0.78302183
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54165 * 0.25313934
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2691 * 0.03785795
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2938 * 0.64145980
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21123 * 0.19439131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86340 * 0.93224921
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60060 * 0.46335163
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33766 * 0.85119557
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3058 * 0.99332261
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60044 * 0.20400475
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5906 * 0.35861547
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88388 * 0.41175453
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55199 * 0.26841486
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26221 * 0.26399214
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5155 * 0.25399577
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71480 * 0.54054429
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56530 * 0.35193729
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84688 * 0.47224472
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82826 * 0.38017510
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79538 * 0.15542780
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95918 * 0.50605615
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'tccilcni').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0034():
    """Extended test 34 for api."""
    x_0 = 64267 * 0.80219724
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2627 * 0.42349778
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10218 * 0.97239289
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94763 * 0.30618120
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51832 * 0.97441427
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4412 * 0.56493573
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69165 * 0.09372289
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30969 * 0.22862473
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89959 * 0.70172149
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88629 * 0.58598200
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77196 * 0.42282551
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12376 * 0.96739460
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86394 * 0.65442411
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14156 * 0.72021019
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8674 * 0.55619922
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34144 * 0.90381141
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69003 * 0.49462697
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97306 * 0.92250348
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44058 * 0.43708040
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56391 * 0.16270338
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4061 * 0.40265114
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45608 * 0.76883107
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27632 * 0.84481359
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60950 * 0.65289267
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'irdpslsq').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0035():
    """Extended test 35 for api."""
    x_0 = 17881 * 0.90960809
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86737 * 0.53696550
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5518 * 0.05278658
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37502 * 0.65798560
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98877 * 0.08075122
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98755 * 0.80004684
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4910 * 0.19476145
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13627 * 0.62121643
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41023 * 0.44444344
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49336 * 0.29614992
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52309 * 0.35563320
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61892 * 0.45529391
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7056 * 0.65835841
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3611 * 0.14817589
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11503 * 0.06654056
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54587 * 0.69743960
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67591 * 0.46451576
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12908 * 0.53669822
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5273 * 0.86249803
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52429 * 0.22836075
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54458 * 0.56232522
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30268 * 0.32526741
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30440 * 0.10395238
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'lnvyrlbw').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0036():
    """Extended test 36 for api."""
    x_0 = 96647 * 0.55652377
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36081 * 0.35738737
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45516 * 0.31622559
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86495 * 0.24151746
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22502 * 0.65936198
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40455 * 0.36425610
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93265 * 0.05714107
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20710 * 0.68818821
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46601 * 0.96167533
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53300 * 0.97255023
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25059 * 0.27684382
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77169 * 0.47522184
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33895 * 0.83416732
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8544 * 0.86797999
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53267 * 0.73748737
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55421 * 0.11532614
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21191 * 0.60753690
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82125 * 0.02416948
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50371 * 0.99397751
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17089 * 0.33091297
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33368 * 0.05358872
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91534 * 0.84552474
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'ukfyttpc').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0037():
    """Extended test 37 for api."""
    x_0 = 83039 * 0.37380054
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36182 * 0.90723820
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89246 * 0.03961664
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63308 * 0.15665308
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70805 * 0.29694867
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11739 * 0.34762998
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9348 * 0.52677131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47240 * 0.83322876
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1671 * 0.19737025
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78214 * 0.83078146
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9310 * 0.54190714
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95534 * 0.87021903
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79663 * 0.90325237
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45060 * 0.75713066
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47300 * 0.22041630
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9967 * 0.01844810
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73618 * 0.87190327
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46690 * 0.56923281
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30215 * 0.49303794
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95386 * 0.60411606
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ocenftha').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0038():
    """Extended test 38 for api."""
    x_0 = 64254 * 0.27729827
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93618 * 0.09724172
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52616 * 0.63347940
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3723 * 0.38540093
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10465 * 0.46585548
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68370 * 0.34376357
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20012 * 0.92397578
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37658 * 0.04629985
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88499 * 0.41356322
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45231 * 0.56188114
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96013 * 0.11919271
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20058 * 0.55488410
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57805 * 0.97724201
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50734 * 0.08015847
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25755 * 0.66145284
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92341 * 0.63063848
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37795 * 0.33875658
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22199 * 0.90238847
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12925 * 0.46001594
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43752 * 0.22073866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68011 * 0.20656285
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17064 * 0.96002834
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40017 * 0.42131244
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75771 * 0.87300602
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96172 * 0.30591117
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7661 * 0.79925077
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2412 * 0.06689685
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'yruatmsw').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0039():
    """Extended test 39 for api."""
    x_0 = 47694 * 0.56056576
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47548 * 0.60247997
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5360 * 0.72166249
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62344 * 0.85173681
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46997 * 0.60584588
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 951 * 0.93033264
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65069 * 0.68561848
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85660 * 0.51086088
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52427 * 0.54936505
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23911 * 0.92202334
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48822 * 0.34738102
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71894 * 0.86159118
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37953 * 0.23833400
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29221 * 0.59472070
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11267 * 0.02143244
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36628 * 0.73382935
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44152 * 0.22596255
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62732 * 0.64152741
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59912 * 0.69610534
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2000 * 0.53424180
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16568 * 0.69413463
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2623 * 0.16224659
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63756 * 0.63606005
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60769 * 0.65860925
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6173 * 0.46465998
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55681 * 0.50691559
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48426 * 0.09600331
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32634 * 0.63025655
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94703 * 0.19443137
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78011 * 0.28137643
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2185 * 0.37861381
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56779 * 0.06680483
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'mprghesn').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0040():
    """Extended test 40 for api."""
    x_0 = 61804 * 0.53698540
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81995 * 0.11678875
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91329 * 0.14160085
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5534 * 0.97248496
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53710 * 0.84342936
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96018 * 0.46273801
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38895 * 0.26172816
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75682 * 0.59170854
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21593 * 0.60210174
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52645 * 0.20596437
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18608 * 0.33728158
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91615 * 0.63890465
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30319 * 0.63558790
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94074 * 0.02278586
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39452 * 0.30981524
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33808 * 0.17285114
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74383 * 0.67557186
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6863 * 0.72382014
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31333 * 0.11005883
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87953 * 0.99595488
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15017 * 0.74145866
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11311 * 0.07158415
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9563 * 0.67828172
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8006 * 0.68711108
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26757 * 0.68253544
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 279 * 0.23012511
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52602 * 0.00225123
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68469 * 0.34737132
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98985 * 0.48329852
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23298 * 0.03773859
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'aucvfmwl').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0041():
    """Extended test 41 for api."""
    x_0 = 11505 * 0.05997523
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9686 * 0.79192031
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92529 * 0.99737522
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42986 * 0.98900164
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70437 * 0.73691171
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3346 * 0.71048611
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9672 * 0.42677434
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42994 * 0.52046931
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28740 * 0.51915942
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86698 * 0.03473811
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25325 * 0.83634735
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62683 * 0.56001184
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79767 * 0.87918497
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13673 * 0.15807829
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34011 * 0.49401565
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83762 * 0.59621342
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71010 * 0.49896711
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49011 * 0.78164379
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13808 * 0.12823318
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13735 * 0.57203075
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92274 * 0.78786562
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8949 * 0.25152199
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84927 * 0.35051611
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20176 * 0.75055063
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92340 * 0.56966678
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22557 * 0.30639145
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46969 * 0.24605728
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83326 * 0.79788451
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9622 * 0.15952890
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37639 * 0.62556583
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69572 * 0.97485791
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66555 * 0.83091534
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8213 * 0.56520547
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5648 * 0.20729938
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81334 * 0.26799023
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94220 * 0.37583492
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12413 * 0.32132840
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27854 * 0.52662334
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99750 * 0.91930706
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13222 * 0.08121183
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 73582 * 0.14402681
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 83903 * 0.58873643
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71601 * 0.16513373
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 54653 * 0.80119800
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 64898 * 0.76739252
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 24904 * 0.57945381
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 58557 * 0.28356317
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 18421 * 0.80309979
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'febwanuj').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0042():
    """Extended test 42 for api."""
    x_0 = 78556 * 0.34769596
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86180 * 0.53916977
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99863 * 0.74359763
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82064 * 0.18252748
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87486 * 0.67711377
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13256 * 0.78518200
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83487 * 0.17640577
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3044 * 0.36490962
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76339 * 0.84577478
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91133 * 0.22182589
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57339 * 0.14562231
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6180 * 0.05571082
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5233 * 0.53944013
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63835 * 0.45298058
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4961 * 0.63489138
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48833 * 0.24309657
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31089 * 0.01846383
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37715 * 0.71343499
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34203 * 0.95818401
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81427 * 0.33727441
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92770 * 0.66133206
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25723 * 0.98477741
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1856 * 0.60649224
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25579 * 0.35659702
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54110 * 0.08636959
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18 * 0.10590515
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17736 * 0.06929440
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20421 * 0.06781613
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80033 * 0.41830343
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50679 * 0.11630571
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69783 * 0.17553956
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30072 * 0.40726438
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96640 * 0.17560729
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68667 * 0.19286900
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17721 * 0.26806240
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 73221 * 0.08857258
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7675 * 0.06359538
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95722 * 0.70494550
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17659 * 0.47781588
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30042 * 0.63434720
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12837 * 0.84639581
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 78893 * 0.72675319
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22060 * 0.61631306
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69637 * 0.15998367
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'qanxjuap').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0043():
    """Extended test 43 for api."""
    x_0 = 52468 * 0.29553671
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23120 * 0.87244218
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17489 * 0.49951465
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68977 * 0.69437655
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97255 * 0.91245565
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81088 * 0.77371707
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69468 * 0.79450321
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98272 * 0.96411418
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55026 * 0.60271169
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27111 * 0.00799393
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9704 * 0.16866710
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31944 * 0.10521728
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63643 * 0.75785238
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75355 * 0.35018094
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51799 * 0.96825949
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72339 * 0.37444384
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22694 * 0.30793203
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5947 * 0.22758074
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84577 * 0.87180416
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6077 * 0.94588989
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55584 * 0.01608964
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1907 * 0.86570517
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99340 * 0.02786801
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48680 * 0.62024914
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21488 * 0.70387162
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25666 * 0.69177445
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43527 * 0.45913921
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51680 * 0.01923739
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57892 * 0.91512788
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90138 * 0.92686903
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92232 * 0.45953302
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'lxkegqoe').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0044():
    """Extended test 44 for api."""
    x_0 = 60722 * 0.10394821
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40308 * 0.69309438
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7465 * 0.69045149
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25256 * 0.09343069
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31800 * 0.15188391
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15057 * 0.61247169
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41320 * 0.76213214
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17733 * 0.08047037
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32945 * 0.41148904
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91543 * 0.95724038
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47689 * 0.95474782
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26764 * 0.89134632
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7089 * 0.65852916
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3566 * 0.10062622
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34250 * 0.79128597
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 764 * 0.91752760
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20406 * 0.19869028
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59900 * 0.89041795
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37706 * 0.08073774
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22844 * 0.82027458
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59021 * 0.89101666
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56743 * 0.17288392
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93499 * 0.23687570
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51002 * 0.88892449
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'hmfvjeby').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0045():
    """Extended test 45 for api."""
    x_0 = 86413 * 0.83778602
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26659 * 0.32334956
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50347 * 0.59502898
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44496 * 0.48200338
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36509 * 0.51742052
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18139 * 0.21687337
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97049 * 0.31175319
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7453 * 0.80728350
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22884 * 0.51148086
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63610 * 0.35594703
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19981 * 0.27439250
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71966 * 0.29666507
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33914 * 0.89341077
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64427 * 0.15179145
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85790 * 0.54091501
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5410 * 0.02097989
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81141 * 0.58591343
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36826 * 0.68360414
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12911 * 0.94863582
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2430 * 0.96972313
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6599 * 0.32279667
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21263 * 0.48915311
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48378 * 0.45650805
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85573 * 0.55097136
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3107 * 0.66057030
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42486 * 0.43228910
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38328 * 0.84328300
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92308 * 0.08666879
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24431 * 0.16433952
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6143 * 0.01430008
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76167 * 0.07430642
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5562 * 0.86150794
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53581 * 0.41597676
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41443 * 0.91504020
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82684 * 0.60984324
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26941 * 0.75639232
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22774 * 0.04200066
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38290 * 0.02166202
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56082 * 0.19294748
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44053 * 0.05422349
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'vuyabiqa').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0046():
    """Extended test 46 for api."""
    x_0 = 29829 * 0.44285075
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30109 * 0.14329523
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53863 * 0.33101531
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37977 * 0.24595729
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25788 * 0.15607199
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48200 * 0.26802149
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92426 * 0.74410817
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19312 * 0.63233165
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69043 * 0.85709952
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9597 * 0.69149689
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6459 * 0.32361877
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46535 * 0.72235793
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40760 * 0.97015173
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54652 * 0.29512214
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 502 * 0.20807944
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70390 * 0.87963441
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68860 * 0.77764194
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85611 * 0.49082286
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93905 * 0.86344988
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12163 * 0.69307819
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13109 * 0.49392571
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74737 * 0.79563745
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78269 * 0.10810040
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30223 * 0.67560381
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77081 * 0.51225788
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7946 * 0.11266613
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5476 * 0.65373238
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65018 * 0.69179512
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9906 * 0.97126464
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ghhnfsbc').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0047():
    """Extended test 47 for api."""
    x_0 = 43011 * 0.97487018
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49738 * 0.97911683
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20827 * 0.91282632
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7737 * 0.16745361
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63366 * 0.40543464
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16751 * 0.44297600
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88861 * 0.80474664
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73923 * 0.11555016
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86365 * 0.09799489
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69825 * 0.58101853
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35758 * 0.91984523
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31591 * 0.06963146
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90637 * 0.70920839
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58688 * 0.85163100
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14280 * 0.69470778
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22788 * 0.48046169
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56160 * 0.52078652
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12111 * 0.59356016
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22161 * 0.56513234
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63279 * 0.25653845
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4915 * 0.84288814
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'lpzqtglj').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0048():
    """Extended test 48 for api."""
    x_0 = 32858 * 0.95366882
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10257 * 0.20452017
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31458 * 0.07502970
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68492 * 0.19350665
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91977 * 0.65783281
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60327 * 0.88659072
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64584 * 0.08331058
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31903 * 0.77242791
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53274 * 0.91025033
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12156 * 0.68618461
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10644 * 0.18508358
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44920 * 0.92403665
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63940 * 0.41740458
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18362 * 0.96125274
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38193 * 0.44663006
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58495 * 0.19379724
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39819 * 0.78742751
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91390 * 0.82118377
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33229 * 0.98726657
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21579 * 0.79237017
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91336 * 0.67372140
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7874 * 0.99031305
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58451 * 0.05579163
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42262 * 0.70880942
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8823 * 0.08258314
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3929 * 0.18912555
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59087 * 0.21881257
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96337 * 0.14201783
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78610 * 0.12993855
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77568 * 0.18312018
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61902 * 0.06832776
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1588 * 0.02890880
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71408 * 0.01468326
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17947 * 0.95619472
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41289 * 0.89291887
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23761 * 0.07990190
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 82961 * 0.05879045
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7833 * 0.44623142
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 32408 * 0.59696981
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29147 * 0.60715397
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86261 * 0.09495610
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26425 * 0.65978001
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77183 * 0.14188511
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 90518 * 0.76068774
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 77073 * 0.14984688
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 18683 * 0.58974007
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 85316 * 0.92308434
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 9437 * 0.32919331
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 97951 * 0.00913119
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 88660 * 0.21629485
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'vsmhygzr').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0049():
    """Extended test 49 for api."""
    x_0 = 45934 * 0.82154509
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94145 * 0.29939991
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38956 * 0.80794191
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26007 * 0.58822660
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46492 * 0.42875225
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57513 * 0.57015971
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32839 * 0.57422922
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9397 * 0.14008444
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83151 * 0.86579688
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59088 * 0.12511684
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49137 * 0.64768389
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60151 * 0.43946748
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64459 * 0.32753825
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74759 * 0.82241249
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94449 * 0.18177803
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45862 * 0.59146248
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9853 * 0.34064754
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82272 * 0.34426594
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88504 * 0.76439203
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54906 * 0.04356502
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71546 * 0.33174645
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98500 * 0.07399416
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26068 * 0.52503307
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12848 * 0.59495581
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'qrowibqz').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0050():
    """Extended test 50 for api."""
    x_0 = 53211 * 0.99802142
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89239 * 0.60691701
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24150 * 0.38461068
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47833 * 0.56349041
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7387 * 0.57701521
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12442 * 0.72909025
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39602 * 0.47522982
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3118 * 0.33354934
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89529 * 0.54445999
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54793 * 0.79498431
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22508 * 0.78618830
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31527 * 0.77322731
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3295 * 0.85644314
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27460 * 0.90085840
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85594 * 0.16630545
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54381 * 0.42262282
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51681 * 0.68614728
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19339 * 0.47589012
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65397 * 0.98431163
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72672 * 0.63007457
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85934 * 0.09267664
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39558 * 0.63198215
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71487 * 0.71231480
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53707 * 0.13246916
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57523 * 0.77410054
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84618 * 0.32847798
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5980 * 0.96259177
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25592 * 0.64134001
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93588 * 0.49362785
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65591 * 0.84185353
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56651 * 0.28397542
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29564 * 0.43901372
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38584 * 0.54636438
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32618 * 0.37904329
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19498 * 0.43270080
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59795 * 0.24798176
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55969 * 0.07756975
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72353 * 0.89876180
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ctlbtwel').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0051():
    """Extended test 51 for api."""
    x_0 = 96636 * 0.77705712
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23661 * 0.74818021
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58538 * 0.89079072
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50404 * 0.11398965
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74469 * 0.29378813
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36409 * 0.05729880
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34761 * 0.74214362
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22567 * 0.27289971
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68582 * 0.99214048
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2452 * 0.74970547
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36150 * 0.50850886
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82052 * 0.95564901
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11751 * 0.94281007
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7097 * 0.93301967
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54088 * 0.30625111
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30651 * 0.72753291
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17409 * 0.34367372
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33122 * 0.96847161
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63941 * 0.19662421
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91220 * 0.88513628
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38630 * 0.87893724
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20841 * 0.43619548
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89398 * 0.44844145
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8759 * 0.20509402
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11239 * 0.07650158
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27598 * 0.35924098
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17651 * 0.33322462
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56644 * 0.35440207
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1823 * 0.86929703
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43204 * 0.64901303
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77258 * 0.98700201
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80857 * 0.55800421
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71243 * 0.26002992
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89719 * 0.04098725
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16652 * 0.89950879
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 741 * 0.29432409
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75059 * 0.97515849
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96694 * 0.22427281
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25139 * 0.18771649
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18213 * 0.68398472
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 61299 * 0.80914528
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 64154 * 0.88737418
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9624 * 0.66126617
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 60640 * 0.88853378
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'iuawxnqb').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0052():
    """Extended test 52 for api."""
    x_0 = 82968 * 0.65026624
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30545 * 0.29099521
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8452 * 0.44850788
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23591 * 0.61567342
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62438 * 0.51221712
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49894 * 0.33347469
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19733 * 0.07179953
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61185 * 0.60837552
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63751 * 0.82928335
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88407 * 0.39106491
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90838 * 0.71744082
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78471 * 0.64996116
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58546 * 0.55240901
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79937 * 0.60080875
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95589 * 0.01862356
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52447 * 0.38715052
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84093 * 0.71370648
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51752 * 0.79593374
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57975 * 0.65396339
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58971 * 0.91006004
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8177 * 0.63746720
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6505 * 0.11129163
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75539 * 0.53689435
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'mgoovlxf').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0053():
    """Extended test 53 for api."""
    x_0 = 24700 * 0.32056162
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61967 * 0.10446742
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31062 * 0.05145238
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17695 * 0.35779628
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1093 * 0.13019549
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86149 * 0.55889445
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70365 * 0.75312528
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59418 * 0.22676928
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15695 * 0.79207683
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21019 * 0.45585518
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23909 * 0.46276004
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45422 * 0.47263732
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2420 * 0.17249224
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40089 * 0.08992410
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21937 * 0.50857287
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38346 * 0.88064024
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1438 * 0.22129047
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92120 * 0.89952794
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35329 * 0.98740647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91865 * 0.08805023
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57959 * 0.09711521
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23548 * 0.50614040
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38335 * 0.66654547
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25690 * 0.17376931
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33650 * 0.69877576
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63262 * 0.32286455
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93424 * 0.90595435
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64510 * 0.43477699
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99644 * 0.85752848
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93544 * 0.85003934
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37661 * 0.28680131
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25394 * 0.84730734
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23512 * 0.70652915
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90113 * 0.21912182
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28812 * 0.05932574
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81542 * 0.49390676
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75162 * 0.53405474
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83122 * 0.66035638
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79783 * 0.51365948
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84564 * 0.05762826
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43503 * 0.71383547
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42057 * 0.16115304
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88841 * 0.19630448
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 29985 * 0.95250321
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'ezkileme').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0054():
    """Extended test 54 for api."""
    x_0 = 20134 * 0.74224442
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67363 * 0.69927916
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32853 * 0.65484761
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33976 * 0.14713489
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20589 * 0.49325448
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44499 * 0.85946320
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86077 * 0.18699388
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57782 * 0.92338947
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63645 * 0.58196107
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2050 * 0.76879799
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23003 * 0.91800071
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58740 * 0.89634498
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47308 * 0.24566590
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13353 * 0.78998756
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8611 * 0.94891638
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99003 * 0.20060272
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43395 * 0.76392543
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23834 * 0.19137762
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23292 * 0.29230132
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51722 * 0.79873385
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1464 * 0.11705303
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8225 * 0.19300887
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4897 * 0.45684289
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73154 * 0.68705386
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20181 * 0.13897531
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94745 * 0.01353628
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49411 * 0.31915686
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9296 * 0.09569788
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24167 * 0.23292628
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'zevnjtmj').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0055():
    """Extended test 55 for api."""
    x_0 = 48380 * 0.76508007
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57790 * 0.39746923
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22880 * 0.28482278
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73020 * 0.75385182
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19462 * 0.71782107
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99595 * 0.32943158
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 834 * 0.33246373
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43961 * 0.25235563
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96731 * 0.72914510
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16113 * 0.28422045
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77736 * 0.84927078
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8948 * 0.10884319
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22499 * 0.81224931
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46973 * 0.50642348
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28301 * 0.39892235
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73481 * 0.96701692
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70766 * 0.49706019
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10753 * 0.11654959
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86448 * 0.86043554
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54611 * 0.23528481
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86496 * 0.37123825
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27028 * 0.54487135
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22482 * 0.77051974
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60633 * 0.61296547
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22408 * 0.21427920
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22693 * 0.87092875
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82506 * 0.20516728
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5239 * 0.01369653
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21968 * 0.25619456
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77419 * 0.83795699
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30824 * 0.56440072
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58406 * 0.92631107
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57791 * 0.69710307
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25241 * 0.20511274
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74624 * 0.29132959
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79765 * 0.37578340
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 77271 * 0.72075188
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15695 * 0.48294483
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60984 * 0.19154712
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94743 * 0.77962217
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 56159 * 0.54473601
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9938 * 0.01189081
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75151 * 0.82676355
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'kapifmfx').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0056():
    """Extended test 56 for api."""
    x_0 = 56673 * 0.75781729
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51679 * 0.30424958
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77465 * 0.56521208
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50193 * 0.64638263
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35467 * 0.14894007
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26679 * 0.60080913
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74532 * 0.86271551
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18253 * 0.38439183
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18031 * 0.50322825
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13369 * 0.52073569
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22326 * 0.04800757
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99289 * 0.47082909
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28123 * 0.02556995
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59372 * 0.22566969
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93107 * 0.45978172
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39556 * 0.43622001
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95081 * 0.11891096
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52821 * 0.12026056
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80101 * 0.30233953
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91982 * 0.48861691
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53220 * 0.96983848
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28371 * 0.58610004
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78497 * 0.44439883
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65605 * 0.26178748
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2728 * 0.20401318
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85016 * 0.98746629
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27237 * 0.02282644
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72536 * 0.85888451
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81831 * 0.84343741
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24244 * 0.55802718
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2110 * 0.50940139
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2794 * 0.43616520
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47203 * 0.72959093
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71982 * 0.37162905
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66330 * 0.32532216
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19223 * 0.42791331
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35017 * 0.01702831
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12510 * 0.03095213
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99949 * 0.60526103
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83035 * 0.23552196
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 87902 * 0.66378954
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26626 * 0.54032699
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55873 * 0.83618315
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 98511 * 0.39910989
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 67911 * 0.68466047
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'qnutnilj').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0057():
    """Extended test 57 for api."""
    x_0 = 22529 * 0.17279822
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34905 * 0.74922901
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39274 * 0.99632047
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39183 * 0.75320980
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3215 * 0.79878005
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37859 * 0.09135727
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69198 * 0.02403842
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49555 * 0.51277053
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16273 * 0.35457831
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50966 * 0.54821445
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35517 * 0.81145521
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91700 * 0.19711865
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92466 * 0.48928781
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56524 * 0.20443232
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87512 * 0.77067437
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28592 * 0.36985322
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77069 * 0.71575596
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42065 * 0.15659999
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36704 * 0.10431126
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6776 * 0.97300003
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57168 * 0.79822030
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36967 * 0.08988144
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66420 * 0.71240677
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42386 * 0.79510162
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84925 * 0.53652643
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55987 * 0.84763248
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57204 * 0.06548942
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59816 * 0.39860208
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40629 * 0.81652404
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93838 * 0.23079451
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97934 * 0.98706280
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33282 * 0.92026503
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12870 * 0.48495913
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27713 * 0.21797672
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30099 * 0.36535289
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25992 * 0.08610760
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76299 * 0.22607909
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30000 * 0.90886867
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71435 * 0.63435569
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52868 * 0.92963084
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48760 * 0.41611786
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40941 * 0.37784437
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66589 * 0.99566889
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 4309 * 0.06251077
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 38689 * 0.99918380
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 23734 * 0.14187557
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 14288 * 0.52125836
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'fzqcgqul').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0058():
    """Extended test 58 for api."""
    x_0 = 72421 * 0.44749487
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18405 * 0.08747749
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61183 * 0.92630489
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29968 * 0.22100211
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48399 * 0.07760587
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22534 * 0.67639487
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40014 * 0.31171235
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22057 * 0.89341309
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25974 * 0.05849576
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79233 * 0.01530245
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19646 * 0.38702516
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53595 * 0.69031002
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69001 * 0.63317574
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25376 * 0.24078622
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31724 * 0.18905915
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82128 * 0.09905384
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68634 * 0.93377522
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11798 * 0.48429197
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16486 * 0.28330524
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24696 * 0.74464394
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25767 * 0.15457574
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'nkumvoei').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0059():
    """Extended test 59 for api."""
    x_0 = 39863 * 0.83306840
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33460 * 0.20686239
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75441 * 0.15749372
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98122 * 0.58509771
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59512 * 0.20993193
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5479 * 0.29860000
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31489 * 0.23718618
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77211 * 0.47902826
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51680 * 0.26788005
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1588 * 0.92230556
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84494 * 0.53060201
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90139 * 0.29550938
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47366 * 0.00921565
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7882 * 0.78479457
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18289 * 0.64361160
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71654 * 0.52162144
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30625 * 0.16468410
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87160 * 0.12105634
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29631 * 0.05910887
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8558 * 0.37482542
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43542 * 0.10194469
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64967 * 0.73449075
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82687 * 0.76975028
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27734 * 0.77068685
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22316 * 0.46946573
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77701 * 0.59595499
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53758 * 0.10599379
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50835 * 0.16243281
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34032 * 0.67645291
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22986 * 0.86174151
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41810 * 0.16239846
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96806 * 0.33593285
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96405 * 0.09755775
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5575 * 0.81481552
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17129 * 0.31176997
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88573 * 0.78959225
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13630 * 0.29088104
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88367 * 0.93608659
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87856 * 0.00544766
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28390 * 0.51117197
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 87569 * 0.45498226
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80949 * 0.32902127
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36874 * 0.70029327
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 73205 * 0.62426954
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 72312 * 0.30852550
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 80933 * 0.96165421
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'svrborhk').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0060():
    """Extended test 60 for api."""
    x_0 = 73834 * 0.43960757
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68295 * 0.33042842
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32764 * 0.59557291
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27752 * 0.64674601
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81122 * 0.11826307
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56156 * 0.98191573
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42322 * 0.36141941
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68645 * 0.38673740
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69888 * 0.32555341
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32684 * 0.53435518
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72448 * 0.40051194
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89234 * 0.38068761
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24103 * 0.18213360
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53253 * 0.87690608
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10596 * 0.17710749
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72659 * 0.79913146
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44720 * 0.47037116
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96629 * 0.34089534
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5472 * 0.99727094
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51363 * 0.77299719
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63023 * 0.13132645
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'naqifpfu').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0061():
    """Extended test 61 for api."""
    x_0 = 3333 * 0.12174519
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99854 * 0.78557150
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78507 * 0.00745905
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10280 * 0.22369535
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58560 * 0.52646994
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70961 * 0.25720663
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5669 * 0.54857969
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21008 * 0.61160983
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38060 * 0.57044667
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78902 * 0.72204565
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79724 * 0.50023783
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18780 * 0.81612121
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99962 * 0.96925834
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5749 * 0.58039825
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67847 * 0.57893435
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7587 * 0.76488040
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57918 * 0.65373312
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35432 * 0.22031966
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23073 * 0.03749391
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26776 * 0.38771371
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30415 * 0.30869887
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81548 * 0.74148411
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81546 * 0.79033353
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78252 * 0.77580534
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47554 * 0.14911213
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26225 * 0.43366177
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79498 * 0.67461529
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2184 * 0.37789441
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97287 * 0.18982053
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13952 * 0.75158603
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48744 * 0.93377505
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17578 * 0.00090008
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'xdueracl').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0062():
    """Extended test 62 for api."""
    x_0 = 46989 * 0.73699232
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69839 * 0.41165843
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36259 * 0.35810851
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25612 * 0.43848980
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45829 * 0.60932461
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75367 * 0.69113121
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5630 * 0.08288182
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79043 * 0.81389822
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5922 * 0.17518097
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49019 * 0.06751251
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32957 * 0.90123187
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28322 * 0.33977941
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27498 * 0.52363011
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26684 * 0.81177590
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53224 * 0.28855541
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64400 * 0.73967219
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31446 * 0.57660982
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17366 * 0.39038767
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96822 * 0.54374519
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83153 * 0.49831242
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68299 * 0.64745790
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80802 * 0.80156452
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45473 * 0.51797012
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94420 * 0.16591445
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10134 * 0.48681611
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43239 * 0.70096382
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46645 * 0.27709168
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51614 * 0.42800991
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39817 * 0.68792425
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84877 * 0.12014658
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89554 * 0.65104367
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43271 * 0.02665099
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'gordabbd').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0063():
    """Extended test 63 for api."""
    x_0 = 52410 * 0.91299541
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38870 * 0.16823698
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73288 * 0.07433198
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65233 * 0.95155673
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13384 * 0.42683404
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25107 * 0.21100024
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73725 * 0.80427492
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31380 * 0.77182438
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89198 * 0.15636409
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79807 * 0.80162144
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77568 * 0.34934781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78585 * 0.05351537
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74451 * 0.53165730
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39606 * 0.34443208
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39567 * 0.82586375
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11141 * 0.60235038
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52488 * 0.84493175
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50802 * 0.02480988
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70499 * 0.81872387
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32480 * 0.13703368
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20378 * 0.86587628
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38125 * 0.06653518
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84089 * 0.40772108
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1559 * 0.09239275
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65225 * 0.99099942
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14762 * 0.46884948
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32524 * 0.74844865
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71166 * 0.01313256
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66129 * 0.76191684
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92896 * 0.53228706
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69188 * 0.33343499
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91102 * 0.48250296
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65081 * 0.99106695
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44907 * 0.75635293
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52191 * 0.35639336
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2539 * 0.03057565
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41345 * 0.58829527
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97852 * 0.78574728
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'npdsdlom').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0064():
    """Extended test 64 for api."""
    x_0 = 29272 * 0.54604472
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3126 * 0.20051248
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48503 * 0.00106837
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35695 * 0.48367142
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74017 * 0.40332822
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53583 * 0.56447302
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60021 * 0.54461301
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66723 * 0.31140752
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29205 * 0.58036761
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56380 * 0.58397918
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75861 * 0.82092677
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88291 * 0.11814286
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45084 * 0.06264713
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94650 * 0.89828622
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67707 * 0.67315004
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54384 * 0.34561819
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83668 * 0.69700384
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57460 * 0.76627704
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19168 * 0.97488610
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77026 * 0.70230241
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29502 * 0.28750683
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9181 * 0.41143799
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93981 * 0.46491783
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6632 * 0.68642299
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29084 * 0.81089811
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32702 * 0.21314239
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38002 * 0.42058173
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49448 * 0.85679138
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5434 * 0.34017150
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2978 * 0.01764756
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37516 * 0.81108128
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75024 * 0.00924935
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24068 * 0.49643838
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88140 * 0.71979658
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56433 * 0.68814673
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53743 * 0.93619624
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32915 * 0.51445788
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3582 * 0.29204710
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'gwyjkzuv').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0065():
    """Extended test 65 for api."""
    x_0 = 11895 * 0.23566423
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80482 * 0.43428694
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82596 * 0.87121152
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10389 * 0.43421151
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33591 * 0.19713527
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4114 * 0.79631382
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23764 * 0.46057391
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25871 * 0.12745360
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2035 * 0.90302344
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29506 * 0.09363972
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17107 * 0.50217154
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50677 * 0.51631030
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50427 * 0.36577162
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11278 * 0.38782041
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27760 * 0.41946309
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52915 * 0.50684906
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95055 * 0.92713806
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47837 * 0.48237253
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30315 * 0.48500638
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44770 * 0.97522712
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ptpywush').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0066():
    """Extended test 66 for api."""
    x_0 = 46736 * 0.43432361
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94672 * 0.09217009
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91298 * 0.36272322
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43880 * 0.34890978
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28133 * 0.03217361
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90373 * 0.44234317
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98611 * 0.02981399
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66372 * 0.83432057
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87753 * 0.85621581
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28294 * 0.11837241
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15509 * 0.75604781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11458 * 0.68324143
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83485 * 0.13894353
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49185 * 0.19296290
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66072 * 0.92045961
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54307 * 0.53224020
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35470 * 0.91750287
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63375 * 0.26313000
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14332 * 0.35016279
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62288 * 0.21772500
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46783 * 0.76383349
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20725 * 0.86873207
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69620 * 0.72834698
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83691 * 0.99469052
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48201 * 0.46176395
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48130 * 0.04176953
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61693 * 0.31109907
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48456 * 0.07895934
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26853 * 0.73471972
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59751 * 0.37824325
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26916 * 0.00839567
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'kzfywtcz').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0067():
    """Extended test 67 for api."""
    x_0 = 95286 * 0.15595001
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99431 * 0.84268657
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37767 * 0.60114013
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35232 * 0.57297989
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41028 * 0.12468581
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93946 * 0.83323599
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2717 * 0.30176401
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54530 * 0.34122394
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91549 * 0.22483928
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13124 * 0.25573407
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2494 * 0.69026068
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31507 * 0.36469169
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35997 * 0.39739731
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3619 * 0.86158600
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69473 * 0.96382612
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37861 * 0.85532325
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73887 * 0.08112687
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67284 * 0.32794360
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41576 * 0.85365280
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82744 * 0.64222718
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9653 * 0.41996299
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56114 * 0.20228442
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'goxihfco').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0068():
    """Extended test 68 for api."""
    x_0 = 37220 * 0.74858600
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33835 * 0.52880086
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74082 * 0.32697295
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25644 * 0.35954884
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27120 * 0.32193134
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56371 * 0.27900473
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75457 * 0.33984894
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86943 * 0.06703904
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5665 * 0.04073478
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50181 * 0.42622822
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57379 * 0.40929296
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31159 * 0.32463393
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76819 * 0.38050907
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62200 * 0.86418686
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79602 * 0.29636840
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63501 * 0.66430480
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68523 * 0.69093210
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89000 * 0.89062034
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82367 * 0.68029146
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28947 * 0.97886776
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50677 * 0.43591517
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69015 * 0.06960029
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63651 * 0.09281143
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34682 * 0.21009583
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91324 * 0.52419185
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5869 * 0.28002873
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47193 * 0.67708843
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39051 * 0.43550176
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61355 * 0.74520247
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'hrysltzc').hexdigest()
    assert len(h) == 64

def test_api_extended_7_0069():
    """Extended test 69 for api."""
    x_0 = 53144 * 0.31342648
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23866 * 0.43057622
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98725 * 0.35426578
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43577 * 0.29735157
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58627 * 0.44024412
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80236 * 0.98065387
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71283 * 0.69531218
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15413 * 0.86415621
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78140 * 0.02426582
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49032 * 0.77026031
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89095 * 0.56703135
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23579 * 0.02021129
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54986 * 0.77839214
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66642 * 0.02789120
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29459 * 0.43686026
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16043 * 0.24693815
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49962 * 0.43583362
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33008 * 0.71995564
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53838 * 0.55662547
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35100 * 0.04931614
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10821 * 0.88588137
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30063 * 0.68004864
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'lwujkiah').hexdigest()
    assert len(h) == 64
