"""Extended tests for aggregation suite 0."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_aggregation_extended_0_0000():
    """Extended test 0 for aggregation."""
    x_0 = 24689 * 0.38979587
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31171 * 0.20049712
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26032 * 0.54768893
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95559 * 0.79575482
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76205 * 0.81099553
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9135 * 0.36557636
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51757 * 0.35606410
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6232 * 0.40925733
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58511 * 0.67133684
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78485 * 0.84099513
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34699 * 0.30465296
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93244 * 0.50910621
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39162 * 0.54072182
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99994 * 0.68790266
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17995 * 0.35517506
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12035 * 0.86563802
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72603 * 0.88322452
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14562 * 0.11756335
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74398 * 0.69570984
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83696 * 0.84669246
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95635 * 0.79207238
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51519 * 0.93426489
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62728 * 0.37673930
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51696 * 0.34723629
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44641 * 0.16926080
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57907 * 0.92753273
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35746 * 0.47688509
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27854 * 0.38085548
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71764 * 0.91684584
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61065 * 0.76607990
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40594 * 0.63717914
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86342 * 0.60600352
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72167 * 0.47848357
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46226 * 0.39443271
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44574 * 0.35528276
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79458 * 0.73286606
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28031 * 0.49804869
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16286 * 0.08542630
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46799 * 0.14444212
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22519 * 0.12072321
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17689 * 0.88360047
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 99365 * 0.76944536
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75046 * 0.78274982
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'pulfpdip').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0001():
    """Extended test 1 for aggregation."""
    x_0 = 10830 * 0.56629496
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57552 * 0.81172637
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33034 * 0.15875153
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12139 * 0.62306240
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54217 * 0.02541522
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28778 * 0.97843930
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7745 * 0.74259670
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74186 * 0.73264908
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22051 * 0.54650241
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5929 * 0.00980207
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25070 * 0.70985357
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89459 * 0.49913720
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80202 * 0.99619686
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78564 * 0.70427282
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42946 * 0.45493835
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89575 * 0.62430563
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20072 * 0.84261312
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54588 * 0.32386433
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94049 * 0.12365289
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54157 * 0.08137680
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14979 * 0.96217467
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37087 * 0.08079108
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13679 * 0.53302887
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7279 * 0.77110012
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83736 * 0.99558642
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52418 * 0.04686025
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83977 * 0.50318660
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93938 * 0.88745947
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95326 * 0.79523892
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42494 * 0.09737600
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79668 * 0.80645546
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75289 * 0.79625464
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86159 * 0.46307282
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10176 * 0.58967321
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76482 * 0.54325312
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43826 * 0.77367253
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72928 * 0.69005399
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68600 * 0.93045867
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76774 * 0.21409210
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42216 * 0.13298261
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27785 * 0.32833458
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 48831 * 0.53145446
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16277 * 0.43566516
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 73019 * 0.78777479
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 5239 * 0.43084529
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 27634 * 0.35150755
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'wryjvsvw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0002():
    """Extended test 2 for aggregation."""
    x_0 = 1738 * 0.36483664
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96936 * 0.75517363
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45861 * 0.26562700
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81518 * 0.90045854
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20356 * 0.45808503
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36913 * 0.41946032
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12664 * 0.91928777
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27368 * 0.47234418
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87485 * 0.43730453
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56221 * 0.15480878
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82405 * 0.45617165
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17336 * 0.49568675
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71567 * 0.26856750
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47769 * 0.58756127
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85527 * 0.54381014
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50229 * 0.34873021
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21835 * 0.35710431
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62836 * 0.38224254
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79647 * 0.65472081
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17877 * 0.70489517
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78411 * 0.44472724
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95320 * 0.46746875
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27558 * 0.83430804
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92592 * 0.62714535
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'rdruzbqt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0003():
    """Extended test 3 for aggregation."""
    x_0 = 72559 * 0.21895449
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34179 * 0.13392444
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23539 * 0.78951715
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97899 * 0.91337824
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1999 * 0.37598436
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30906 * 0.12218443
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8826 * 0.11438129
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1853 * 0.12800866
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95085 * 0.60795627
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67070 * 0.26740049
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68540 * 0.21120806
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72691 * 0.95324127
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97042 * 0.77089406
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82471 * 0.96017532
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75658 * 0.09824267
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29479 * 0.61700644
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76464 * 0.61016363
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41823 * 0.76267827
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34740 * 0.07027048
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74381 * 0.52163919
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84902 * 0.12552824
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58944 * 0.61176695
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'iunxadrd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0004():
    """Extended test 4 for aggregation."""
    x_0 = 25049 * 0.28361222
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23828 * 0.59712413
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57630 * 0.84268489
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31863 * 0.51571802
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27088 * 0.55547912
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27576 * 0.78401597
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56206 * 0.39641100
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49731 * 0.85103097
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54576 * 0.82578677
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87992 * 0.17800387
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11617 * 0.74281900
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90411 * 0.92792506
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17001 * 0.55064664
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84693 * 0.07953414
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62420 * 0.28857249
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14875 * 0.39431771
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13761 * 0.15727447
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78471 * 0.28923509
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8693 * 0.09236807
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64245 * 0.29860807
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77570 * 0.09144816
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77604 * 0.34008474
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10275 * 0.29028812
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14906 * 0.94123109
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3776 * 0.54339042
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10493 * 0.19493039
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98927 * 0.26955379
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24984 * 0.26523627
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31489 * 0.48359347
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26156 * 0.91133981
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21555 * 0.79336664
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90437 * 0.19002422
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19801 * 0.73932985
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'occycgap').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0005():
    """Extended test 5 for aggregation."""
    x_0 = 80876 * 0.03383954
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88734 * 0.29316824
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79610 * 0.63816423
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93487 * 0.56834074
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82361 * 0.78387114
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72645 * 0.21379113
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89754 * 0.27491845
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 380 * 0.36048394
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48784 * 0.67747584
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4403 * 0.84238921
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40431 * 0.03879820
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30795 * 0.12908668
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66540 * 0.30952226
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38065 * 0.90602718
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22021 * 0.95035646
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77053 * 0.21696247
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76249 * 0.09513579
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76622 * 0.60444044
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91730 * 0.70584593
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68062 * 0.32757015
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30670 * 0.35026769
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86335 * 0.40283106
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63335 * 0.79121125
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95444 * 0.54423594
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20934 * 0.85905427
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77894 * 0.14403363
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62385 * 0.61706267
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 379 * 0.88561709
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35003 * 0.96553719
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50348 * 0.36336736
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77651 * 0.61560305
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14845 * 0.85505134
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35746 * 0.27335656
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12934 * 0.92892764
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78154 * 0.32004512
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22136 * 0.30936671
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 77816 * 0.43490863
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88467 * 0.96628374
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99612 * 0.86217519
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2539 * 0.39568919
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47513 * 0.50122751
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'eakxpkto').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0006():
    """Extended test 6 for aggregation."""
    x_0 = 79561 * 0.04054702
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23671 * 0.97635218
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76630 * 0.74676959
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46910 * 0.40155758
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49457 * 0.70289476
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44820 * 0.04465310
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68275 * 0.15843222
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50747 * 0.09799162
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90799 * 0.64866129
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61083 * 0.22467287
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17564 * 0.81305877
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35374 * 0.25174068
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31703 * 0.98633391
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62293 * 0.98112119
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55853 * 0.35370456
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92784 * 0.67607054
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26511 * 0.66473153
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2817 * 0.49474534
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54508 * 0.49456490
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4979 * 0.70824355
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97319 * 0.56963647
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5820 * 0.01640658
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22349 * 0.68900202
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55572 * 0.84173757
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3259 * 0.12883531
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39152 * 0.98359326
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89148 * 0.44476808
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51964 * 0.21308286
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'lvgsobwz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0007():
    """Extended test 7 for aggregation."""
    x_0 = 25798 * 0.59292308
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84914 * 0.52544646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25837 * 0.82043397
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72156 * 0.34353632
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86979 * 0.59081107
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16091 * 0.57980391
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30265 * 0.39410672
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63074 * 0.87539309
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55285 * 0.98307960
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12679 * 0.08688618
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11962 * 0.02293295
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47139 * 0.64717389
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87127 * 0.03836276
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33846 * 0.32222882
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24576 * 0.97492899
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6548 * 0.26053339
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65838 * 0.92677199
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35451 * 0.53045333
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29457 * 0.18455777
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50877 * 0.74699826
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27417 * 0.12988263
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83175 * 0.79449403
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29971 * 0.15804470
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49228 * 0.66116499
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70817 * 0.37920041
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52011 * 0.64254805
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13967 * 0.32793271
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7870 * 0.83665643
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63917 * 0.49061399
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30600 * 0.50762676
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70455 * 0.64217856
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'gfqqvgcy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0008():
    """Extended test 8 for aggregation."""
    x_0 = 28874 * 0.83952358
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87583 * 0.59383940
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90531 * 0.53697899
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78479 * 0.87951849
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56455 * 0.65101245
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69684 * 0.55939140
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31379 * 0.14819360
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52141 * 0.37958003
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42719 * 0.87079194
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62694 * 0.34151937
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 933 * 0.53837411
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75052 * 0.77056839
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56609 * 0.31128136
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26951 * 0.84855242
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51716 * 0.62342100
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30968 * 0.19379525
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45729 * 0.52186383
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94295 * 0.71814877
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59301 * 0.26168401
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58138 * 0.65181659
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95171 * 0.83310448
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74385 * 0.17071848
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17693 * 0.63184317
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80337 * 0.79176519
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56813 * 0.51349042
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14124 * 0.60716182
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42478 * 0.55816508
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75260 * 0.08596789
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45478 * 0.04092618
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81692 * 0.19201321
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37525 * 0.05502622
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40877 * 0.78911264
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52432 * 0.59477521
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10549 * 0.16066750
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31822 * 0.21836815
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84123 * 0.13522237
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92603 * 0.67003569
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31323 * 0.95553306
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 50962 * 0.04300865
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 12141 * 0.29587895
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'sdbhjxsz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0009():
    """Extended test 9 for aggregation."""
    x_0 = 80533 * 0.94166668
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77988 * 0.65562046
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44976 * 0.14515259
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62114 * 0.27542664
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40776 * 0.72645297
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89230 * 0.88740197
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77401 * 0.77822264
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80413 * 0.90946309
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95676 * 0.27460141
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48386 * 0.52237603
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34438 * 0.13471670
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92060 * 0.92235348
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44974 * 0.16997386
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27485 * 0.22612331
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93948 * 0.38746888
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42424 * 0.15127833
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43083 * 0.29151194
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98499 * 0.40597141
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54882 * 0.05861344
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9432 * 0.06418355
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54985 * 0.65875162
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'qaahdhow').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0010():
    """Extended test 10 for aggregation."""
    x_0 = 53407 * 0.21975322
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 989 * 0.78066653
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68005 * 0.05654328
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9665 * 0.72826137
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78939 * 0.55210213
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1954 * 0.87683578
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85380 * 0.99085913
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95878 * 0.21990858
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48634 * 0.77909828
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96570 * 0.02545664
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19630 * 0.02875040
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20483 * 0.45832433
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23473 * 0.54149579
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47457 * 0.72404738
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98747 * 0.72170477
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51266 * 0.06502666
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44862 * 0.12619892
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70919 * 0.30519326
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84896 * 0.34047602
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30427 * 0.97040796
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1449 * 0.43826785
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38886 * 0.90653823
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8668 * 0.63790750
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33705 * 0.51854799
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1515 * 0.08810550
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32810 * 0.55192211
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5474 * 0.74650537
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72789 * 0.34739753
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44182 * 0.14229815
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21593 * 0.97278262
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31621 * 0.29892414
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33435 * 0.20269628
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'kspqlcgf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0011():
    """Extended test 11 for aggregation."""
    x_0 = 32623 * 0.35824310
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84862 * 0.18851168
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13431 * 0.34940353
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96310 * 0.06024555
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2421 * 0.39189472
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53653 * 0.73952366
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30118 * 0.01309543
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25243 * 0.33326334
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84136 * 0.15883395
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16010 * 0.22560039
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32696 * 0.22725452
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49097 * 0.02427615
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36035 * 0.16304883
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60418 * 0.94660435
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43174 * 0.42692209
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67974 * 0.88400057
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9495 * 0.55487242
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18198 * 0.28317448
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62129 * 0.61177988
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97782 * 0.62677299
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90846 * 0.65835068
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63453 * 0.57226116
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 474 * 0.16563138
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77964 * 0.24921331
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 893 * 0.32915526
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75414 * 0.17980116
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9506 * 0.23550916
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25572 * 0.37405028
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24699 * 0.57677818
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94791 * 0.31950523
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59694 * 0.49310213
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75325 * 0.25547246
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16869 * 0.95074845
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94724 * 0.95587932
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12662 * 0.02085327
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60520 * 0.00104833
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 82401 * 0.32187452
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6597 * 0.50498339
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88289 * 0.24674475
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55552 * 0.39327427
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71571 * 0.97694434
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82011 * 0.95117283
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 25330 * 0.10617696
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 67453 * 0.62599930
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 30760 * 0.29262734
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'gdlaauzr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0012():
    """Extended test 12 for aggregation."""
    x_0 = 38601 * 0.93559745
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40633 * 0.05516833
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84465 * 0.86119783
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73620 * 0.07855726
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38044 * 0.05702406
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64244 * 0.57272907
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2297 * 0.74861937
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39414 * 0.98503127
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19001 * 0.55812026
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82825 * 0.58433283
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44255 * 0.14774990
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24738 * 0.85078154
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27705 * 0.45731366
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25641 * 0.77958520
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11590 * 0.60822884
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82643 * 0.78813863
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40769 * 0.22355417
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77218 * 0.28167502
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30627 * 0.18764794
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35663 * 0.94930282
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88441 * 0.18672410
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47054 * 0.39467566
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42195 * 0.70932436
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48064 * 0.46008880
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61724 * 0.94618031
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31527 * 0.19176688
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1994 * 0.21758982
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23350 * 0.26348547
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55471 * 0.44091847
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52856 * 0.20855145
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48681 * 0.07459455
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46749 * 0.07921126
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63790 * 0.61147546
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27098 * 0.24192231
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37015 * 0.17159925
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84831 * 0.62008508
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89490 * 0.66358169
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18513 * 0.43821396
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29554 * 0.88992472
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22445 * 0.01193234
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 22120 * 0.31621682
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38565 * 0.96955287
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10144 * 0.46382240
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 16541 * 0.97580032
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11148 * 0.08013435
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 9661 * 0.36341255
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 4759 * 0.52165824
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 92380 * 0.18176568
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 8436 * 0.97619832
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'fpfjavmu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0013():
    """Extended test 13 for aggregation."""
    x_0 = 63122 * 0.27926788
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20852 * 0.34918073
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30970 * 0.89194442
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39002 * 0.10655696
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25329 * 0.51277678
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2239 * 0.38002657
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62116 * 0.45352640
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63566 * 0.12412536
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75914 * 0.80281453
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46429 * 0.49337717
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19139 * 0.81072143
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89972 * 0.46169575
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20110 * 0.31860614
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31030 * 0.87344932
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33306 * 0.65912963
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32930 * 0.34072508
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41787 * 0.26391814
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61378 * 0.00365410
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89428 * 0.07697923
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21749 * 0.01113232
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86198 * 0.35291102
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48037 * 0.50999049
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78455 * 0.56061398
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1061 * 0.69223333
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1972 * 0.55529099
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98845 * 0.88357653
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32695 * 0.38549543
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79755 * 0.78849014
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'sszvuygz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0014():
    """Extended test 14 for aggregation."""
    x_0 = 20905 * 0.53306851
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44558 * 0.57624705
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12522 * 0.80748037
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3574 * 0.47969348
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5844 * 0.31131225
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5275 * 0.96302520
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62111 * 0.36883447
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79269 * 0.41485301
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73443 * 0.71632774
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38128 * 0.89126886
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7402 * 0.61379288
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92475 * 0.64831203
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80548 * 0.38415543
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60620 * 0.90406846
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13861 * 0.10605282
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28804 * 0.75630963
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76749 * 0.54632345
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32064 * 0.64123846
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89471 * 0.25147084
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4715 * 0.40269665
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76019 * 0.40238311
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'pthltigz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0015():
    """Extended test 15 for aggregation."""
    x_0 = 40739 * 0.93079889
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18179 * 0.46145464
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27350 * 0.66560109
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9505 * 0.35641144
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60686 * 0.33859624
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7727 * 0.39609603
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25032 * 0.26209128
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99697 * 0.43185089
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82760 * 0.13057001
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72129 * 0.05488754
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73989 * 0.23263811
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28696 * 0.72356114
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26575 * 0.21632595
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40264 * 0.90515842
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94430 * 0.82859787
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10949 * 0.60213833
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62699 * 0.07125195
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70440 * 0.02651549
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34430 * 0.95439491
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10694 * 0.00751316
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43104 * 0.94308967
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52967 * 0.67182948
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17466 * 0.24038662
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85278 * 0.72722641
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78644 * 0.42108819
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47567 * 0.08712755
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62158 * 0.99076605
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7716 * 0.44530349
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20031 * 0.09119716
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47649 * 0.75809505
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24330 * 0.96586309
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55050 * 0.56499422
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69984 * 0.58430858
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39478 * 0.64288999
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17134 * 0.58435987
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1966 * 0.71114678
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7891 * 0.88238525
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75735 * 0.31117906
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71498 * 0.73686823
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39862 * 0.05419929
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'twbgpfps').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0016():
    """Extended test 16 for aggregation."""
    x_0 = 28023 * 0.74360651
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78484 * 0.22037344
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30699 * 0.79545333
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23848 * 0.01717029
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77772 * 0.70494585
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42042 * 0.57558937
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67618 * 0.19104528
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72069 * 0.02154772
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93556 * 0.79347727
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82800 * 0.66696007
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22421 * 0.42045120
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 919 * 0.70048746
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42940 * 0.29707728
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57781 * 0.31929717
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61640 * 0.09407465
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70705 * 0.65847932
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63311 * 0.76144664
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6724 * 0.21861097
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82356 * 0.05375867
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1060 * 0.29555302
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27156 * 0.07175781
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54715 * 0.29530964
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26456 * 0.53383570
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90753 * 0.96767363
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19900 * 0.73802260
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4118 * 0.79167629
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11519 * 0.65124927
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17587 * 0.89014580
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86244 * 0.95928371
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98615 * 0.24545466
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33810 * 0.67973325
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17518 * 0.14754125
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13020 * 0.50901384
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44611 * 0.60795585
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55083 * 0.18036824
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21952 * 0.09633669
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3672 * 0.50952712
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17289 * 0.63801309
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8577 * 0.91804162
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67707 * 0.74709381
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49162 * 0.95379002
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13788 * 0.54437872
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 53208 * 0.73621327
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'bdlfbzoz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0017():
    """Extended test 17 for aggregation."""
    x_0 = 71491 * 0.90586350
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65897 * 0.72730828
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34696 * 0.58312830
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4646 * 0.58651808
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39773 * 0.62413454
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1584 * 0.90008339
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51675 * 0.26991274
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8834 * 0.58788694
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39396 * 0.64829684
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35648 * 0.10593700
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59233 * 0.20179136
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 638 * 0.27689652
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81162 * 0.69907968
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11457 * 0.01008676
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24013 * 0.17331181
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15068 * 0.14278667
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97965 * 0.11347602
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23232 * 0.26389249
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89282 * 0.19016793
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40248 * 0.99612409
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23131 * 0.69774115
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29541 * 0.66631953
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67208 * 0.52870424
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18494 * 0.66022403
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52479 * 0.29241548
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ewmcnwao').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0018():
    """Extended test 18 for aggregation."""
    x_0 = 17771 * 0.20847701
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89119 * 0.43965286
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27947 * 0.13438700
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97409 * 0.44811853
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93113 * 0.50379466
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14145 * 0.76443085
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48589 * 0.00427528
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29350 * 0.54009401
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65149 * 0.49429545
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35035 * 0.99020040
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69972 * 0.99493478
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43917 * 0.23860675
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51381 * 0.72534230
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7514 * 0.98439951
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84484 * 0.29961093
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47608 * 0.16058367
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37458 * 0.95817849
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88272 * 0.91519586
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58483 * 0.67646518
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80071 * 0.80683924
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23302 * 0.79911078
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90134 * 0.24046972
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22965 * 0.18932864
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19434 * 0.77411222
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65996 * 0.53843167
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33113 * 0.21812702
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13051 * 0.81216553
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28258 * 0.72877561
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58252 * 0.66783154
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14038 * 0.50168963
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'dtvhqpmv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0019():
    """Extended test 19 for aggregation."""
    x_0 = 80119 * 0.33059705
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89452 * 0.29787347
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54367 * 0.29735677
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20486 * 0.47724171
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87110 * 0.74518780
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28964 * 0.10202161
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55400 * 0.95433144
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51763 * 0.61172925
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83531 * 0.80298938
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80238 * 0.32157244
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28914 * 0.46965971
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 687 * 0.45469158
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68688 * 0.13424260
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46433 * 0.93468829
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35658 * 0.82221989
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12630 * 0.83762202
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60835 * 0.30230485
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33473 * 0.48063354
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32416 * 0.42275792
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38309 * 0.33222331
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62563 * 0.23882817
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18054 * 0.72241542
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38676 * 0.26556828
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57019 * 0.64763055
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22314 * 0.78557315
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24880 * 0.85927825
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41184 * 0.76278419
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52002 * 0.77454173
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92802 * 0.63714761
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29772 * 0.16232792
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90559 * 0.91700983
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58841 * 0.53399401
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4637 * 0.92026141
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2419 * 0.09635079
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16934 * 0.17432127
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40443 * 0.86876771
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19895 * 0.34461105
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85133 * 0.70333023
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 50416 * 0.30626901
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 61513 * 0.52875386
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 31824 * 0.55189144
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 29400 * 0.61494747
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 58945 * 0.33022495
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 60301 * 0.30067619
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71253 * 0.84260176
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 31087 * 0.62049440
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 82364 * 0.59507924
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'mvaourzb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0020():
    """Extended test 20 for aggregation."""
    x_0 = 84566 * 0.08752812
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17961 * 0.33856225
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95768 * 0.60816917
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75391 * 0.54694721
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57883 * 0.41150093
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83209 * 0.45761103
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12648 * 0.80629996
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79839 * 0.37045944
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60631 * 0.41562776
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52816 * 0.73360380
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36668 * 0.92090393
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 846 * 0.63296013
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44188 * 0.79612600
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62015 * 0.92330201
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3671 * 0.68825078
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45950 * 0.33152861
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6812 * 0.58478188
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23618 * 0.87057035
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41724 * 0.36202183
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9833 * 0.73312699
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39882 * 0.71292711
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75791 * 0.10550922
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21224 * 0.14503945
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75814 * 0.85556059
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29220 * 0.90612213
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76448 * 0.43619355
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67251 * 0.71970877
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42793 * 0.80415391
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42713 * 0.33858367
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92222 * 0.17898699
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39692 * 0.02459961
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33025 * 0.02483976
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98761 * 0.87166031
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60142 * 0.68660441
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54679 * 0.20304092
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91868 * 0.08797668
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61160 * 0.73602523
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96613 * 0.85484703
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78359 * 0.11448572
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28549 * 0.06706314
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54194 * 0.81806834
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40115 * 0.52538227
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46327 * 0.88531186
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58984 * 0.70691118
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 63098 * 0.69832637
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 14082 * 0.70807136
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 86974 * 0.02152536
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 48797 * 0.10645527
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 12012 * 0.87269934
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 38739 * 0.02820137
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'gkjeeltk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0021():
    """Extended test 21 for aggregation."""
    x_0 = 68208 * 0.76873195
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29322 * 0.46182165
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 586 * 0.01049682
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97839 * 0.66442318
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5543 * 0.98793118
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69856 * 0.44590630
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 885 * 0.40250536
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32811 * 0.00495468
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55847 * 0.06717086
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67020 * 0.38036475
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44247 * 0.25710668
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54183 * 0.83953303
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22305 * 0.47592616
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78470 * 0.89585569
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26358 * 0.42735972
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47312 * 0.36467507
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44964 * 0.15646142
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26018 * 0.69642168
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93799 * 0.67570992
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68681 * 0.78755834
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13886 * 0.79152395
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1008 * 0.78977136
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4652 * 0.26899208
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90218 * 0.16209613
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23413 * 0.07112393
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76034 * 0.51953602
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3255 * 0.15271488
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45183 * 0.63426240
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39285 * 0.05970964
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27404 * 0.51720891
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40825 * 0.89757226
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87737 * 0.24399099
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29336 * 0.41734429
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72070 * 0.68812810
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68731 * 0.02325876
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74823 * 0.93237915
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20633 * 0.75378185
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86221 * 0.29105639
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48271 * 0.03633871
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2580 * 0.28473624
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86199 * 0.93008790
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21862 * 0.41475132
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28952 * 0.63421260
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'bgipofxk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0022():
    """Extended test 22 for aggregation."""
    x_0 = 41847 * 0.20495818
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56380 * 0.17555815
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52642 * 0.50532131
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1135 * 0.54314627
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98547 * 0.57654252
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48412 * 0.99554235
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49501 * 0.30984280
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95939 * 0.76456297
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46214 * 0.18515508
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77120 * 0.30219518
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61474 * 0.02190064
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42826 * 0.18857816
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60625 * 0.25900489
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4283 * 0.53527629
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41287 * 0.40832933
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77718 * 0.51346877
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61801 * 0.21905153
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86783 * 0.25602979
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9395 * 0.95480555
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9864 * 0.94430792
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63983 * 0.32505573
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 365 * 0.18272587
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26508 * 0.90315832
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42588 * 0.11135500
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44689 * 0.10872595
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76244 * 0.11094256
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55333 * 0.58824867
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21354 * 0.64884331
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38287 * 0.79173460
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85652 * 0.03711916
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76679 * 0.93317196
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93998 * 0.25847806
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75761 * 0.97334645
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30910 * 0.75316181
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29331 * 0.96657190
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26148 * 0.12090318
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86095 * 0.40569168
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38864 * 0.80107669
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'dgsqxbob').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0023():
    """Extended test 23 for aggregation."""
    x_0 = 63058 * 0.63762142
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75584 * 0.16388053
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34789 * 0.68416798
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69529 * 0.59943421
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28575 * 0.73310047
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69497 * 0.57162833
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45124 * 0.61029421
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15407 * 0.39206984
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85100 * 0.96370748
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58955 * 0.95496141
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74557 * 0.71159432
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34004 * 0.97861285
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73 * 0.88007970
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30896 * 0.16221188
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41123 * 0.58207357
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81551 * 0.72832918
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57439 * 0.54050172
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89255 * 0.55982253
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50129 * 0.99630207
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8300 * 0.56532966
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28703 * 0.30439986
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43153 * 0.77669307
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57246 * 0.62454474
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66785 * 0.99237650
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15812 * 0.64189535
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28608 * 0.47721250
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86820 * 0.09088943
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23974 * 0.26854462
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25127 * 0.13292009
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56559 * 0.82710159
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5641 * 0.87067647
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5057 * 0.62296324
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43862 * 0.01034153
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31525 * 0.22991076
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58716 * 0.68902275
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38 * 0.51869151
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75943 * 0.68525420
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27771 * 0.31471887
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 3431 * 0.73276636
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75185 * 0.78772105
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98794 * 0.86761164
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81792 * 0.68848920
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88718 * 0.62011309
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 18155 * 0.09313158
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23083 * 0.52916224
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 46064 * 0.61358376
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 83074 * 0.27886548
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 243 * 0.36676021
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'aavejimv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0024():
    """Extended test 24 for aggregation."""
    x_0 = 13245 * 0.00437155
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99047 * 0.67872559
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90594 * 0.78863414
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64087 * 0.83265098
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62313 * 0.36038800
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72466 * 0.80463644
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89695 * 0.59056138
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94385 * 0.09176246
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19884 * 0.19515562
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17117 * 0.03579253
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71143 * 0.64209606
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25591 * 0.44715956
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94675 * 0.54637468
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50916 * 0.66726982
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86654 * 0.98274198
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87648 * 0.26449653
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76915 * 0.64873339
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95518 * 0.75434678
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 403 * 0.97828920
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21165 * 0.29390824
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19154 * 0.64935063
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18425 * 0.22006147
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32612 * 0.48487534
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99975 * 0.69069331
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40906 * 0.05999339
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95217 * 0.86331466
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62325 * 0.65472550
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'xtnshujq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0025():
    """Extended test 25 for aggregation."""
    x_0 = 66249 * 0.10749618
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28396 * 0.32266297
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68346 * 0.19299451
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44388 * 0.21638885
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61053 * 0.03962656
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17474 * 0.21564917
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24340 * 0.52084777
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27629 * 0.80005866
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72242 * 0.40953336
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14421 * 0.78592865
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3046 * 0.06622804
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35582 * 0.61557938
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30729 * 0.00868483
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48571 * 0.55915760
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48310 * 0.45761387
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9562 * 0.94485704
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44617 * 0.68386927
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64058 * 0.79845968
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40002 * 0.73602295
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96010 * 0.06534035
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81518 * 0.03393154
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16332 * 0.65504359
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90153 * 0.20121442
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7940 * 0.96471958
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17326 * 0.82971444
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70087 * 0.91550694
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92400 * 0.58645190
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93529 * 0.46230805
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14708 * 0.81606059
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 645 * 0.83438697
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87574 * 0.94387846
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95943 * 0.35263870
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6939 * 0.54066219
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42669 * 0.69240459
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60399 * 0.66737417
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'nrqvwxwv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0026():
    """Extended test 26 for aggregation."""
    x_0 = 54883 * 0.01710173
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5171 * 0.48579377
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71288 * 0.01798667
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51002 * 0.07015113
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 593 * 0.40285469
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74513 * 0.90748778
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28989 * 0.61070357
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66426 * 0.68677120
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88232 * 0.91116993
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74180 * 0.04401843
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29048 * 0.56127419
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49963 * 0.77240702
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80887 * 0.41176218
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54685 * 0.40241132
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95159 * 0.73622999
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53798 * 0.01542421
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77934 * 0.27130590
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33872 * 0.51040929
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45672 * 0.82359749
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83446 * 0.39549657
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23854 * 0.18192141
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20610 * 0.88382752
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3249 * 0.96839347
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38527 * 0.12326270
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4735 * 0.07429234
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47153 * 0.46527731
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90518 * 0.45053840
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20020 * 0.10874221
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33871 * 0.00586171
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44530 * 0.58721307
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74547 * 0.37007715
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79813 * 0.00304286
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21449 * 0.67325170
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60301 * 0.76072328
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30526 * 0.91205836
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23799 * 0.42057853
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49393 * 0.90998360
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17117 * 0.85411314
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25228 * 0.70685958
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94870 * 0.42441219
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36185 * 0.58034270
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36489 * 0.70737306
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 98172 * 0.54759510
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 78093 * 0.30194882
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 16697 * 0.16292493
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'ehhrqaey').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0027():
    """Extended test 27 for aggregation."""
    x_0 = 57262 * 0.90968729
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91948 * 0.20071466
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27514 * 0.35148441
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14607 * 0.14770522
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42719 * 0.23514288
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71693 * 0.76676418
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8265 * 0.44058078
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83948 * 0.59370743
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46463 * 0.90192843
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21963 * 0.67738201
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74657 * 0.26488080
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67009 * 0.69178664
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96455 * 0.74279131
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46343 * 0.51930885
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39292 * 0.40858042
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46527 * 0.57773969
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31790 * 0.95761672
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75155 * 0.30627216
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39173 * 0.61311722
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85454 * 0.48697275
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62459 * 0.29168316
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59332 * 0.82800003
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9917 * 0.68644328
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11255 * 0.27024441
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92133 * 0.49000811
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'woobwlxc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0028():
    """Extended test 28 for aggregation."""
    x_0 = 32534 * 0.82731669
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73307 * 0.91224212
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43349 * 0.23919693
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63166 * 0.45256673
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78888 * 0.72793192
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6202 * 0.64855215
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73137 * 0.62387751
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91361 * 0.66578376
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63044 * 0.67861831
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85486 * 0.42644991
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26748 * 0.73849242
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54209 * 0.91644662
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87576 * 0.17771677
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32112 * 0.66131339
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11319 * 0.44727161
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67133 * 0.91179107
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93138 * 0.60249514
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84613 * 0.21107946
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20958 * 0.04333733
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74241 * 0.26592490
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90948 * 0.06378020
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75821 * 0.69028048
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49163 * 0.79441997
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85366 * 0.04358701
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19798 * 0.45856004
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2254 * 0.94897461
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18436 * 0.94610087
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47532 * 0.90424113
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70380 * 0.48871408
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67523 * 0.26110860
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62890 * 0.50734642
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'vmomxjzi').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0029():
    """Extended test 29 for aggregation."""
    x_0 = 94281 * 0.91041032
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53002 * 0.55640224
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26554 * 0.31993075
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40220 * 0.49537537
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17421 * 0.85889432
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84920 * 0.49707567
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55603 * 0.93500371
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63043 * 0.64577482
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22100 * 0.98318431
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47887 * 0.92350037
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74571 * 0.65328858
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81166 * 0.36770909
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51529 * 0.87871374
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6477 * 0.57304784
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33977 * 0.13919159
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67156 * 0.31839863
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75329 * 0.19884615
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81872 * 0.63084410
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57369 * 0.39490686
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35072 * 0.40261310
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82013 * 0.59830653
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96503 * 0.35456552
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91928 * 0.14443797
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41645 * 0.12500996
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47616 * 0.09840428
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6197 * 0.05931685
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85394 * 0.70387767
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3387 * 0.49651436
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54978 * 0.27213392
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21993 * 0.97538461
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39699 * 0.95381489
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60641 * 0.76426425
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74589 * 0.95016620
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37634 * 0.42635416
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48295 * 0.63074122
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74099 * 0.38514845
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20530 * 0.77689331
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35795 * 0.11967917
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6932 * 0.35573657
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'mjdmaeou').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0030():
    """Extended test 30 for aggregation."""
    x_0 = 72778 * 0.92690464
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82289 * 0.34829250
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90485 * 0.39999278
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69791 * 0.76551391
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91043 * 0.06767830
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56119 * 0.43473822
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54590 * 0.91847175
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97539 * 0.16518028
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31708 * 0.53819544
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51813 * 0.23235831
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88033 * 0.50154618
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49251 * 0.35623853
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79678 * 0.88224412
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8442 * 0.54965087
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 480 * 0.01715116
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69844 * 0.11632145
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30772 * 0.20410546
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26026 * 0.25026470
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19918 * 0.65037384
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50198 * 0.83247204
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19699 * 0.82360201
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5602 * 0.07398589
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'ynlitemw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0031():
    """Extended test 31 for aggregation."""
    x_0 = 55347 * 0.24458352
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80372 * 0.40523199
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39218 * 0.12721639
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59211 * 0.69056393
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51122 * 0.06494728
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34484 * 0.45467350
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15008 * 0.49568951
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62706 * 0.38854199
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89082 * 0.49914204
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91678 * 0.85854655
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65285 * 0.54553899
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70274 * 0.61753004
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67493 * 0.07853935
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29386 * 0.35172423
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23686 * 0.69275367
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54917 * 0.39777991
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3746 * 0.91745233
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30243 * 0.30299048
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92974 * 0.23344032
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46029 * 0.96891727
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8760 * 0.04855517
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40084 * 0.45548209
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96454 * 0.11098106
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30108 * 0.57792980
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53917 * 0.75788411
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89248 * 0.79091798
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39370 * 0.58751208
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34622 * 0.27196339
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17758 * 0.70393448
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14430 * 0.51455477
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96578 * 0.67914928
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39605 * 0.15375307
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92493 * 0.82037281
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13547 * 0.68948593
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68724 * 0.77603846
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54653 * 0.56399070
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53728 * 0.62881408
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55624 * 0.73761306
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 95089 * 0.43985940
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59401 * 0.69604289
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86845 * 0.39196995
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 95672 * 0.63347881
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62949 * 0.62769436
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 9094 * 0.82151537
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86500 * 0.78095858
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 88685 * 0.15776234
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 82785 * 0.33524245
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 67720 * 0.11402346
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 26080 * 0.34172326
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'xidmoiyh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0032():
    """Extended test 32 for aggregation."""
    x_0 = 22341 * 0.55066188
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53124 * 0.53603532
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81314 * 0.49642648
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51203 * 0.81370660
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83868 * 0.67437651
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11320 * 0.50427162
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54242 * 0.30888253
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12183 * 0.04809250
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94467 * 0.73823668
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54346 * 0.21911545
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64043 * 0.01599024
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98798 * 0.83039718
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70535 * 0.38995750
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47758 * 0.47080978
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27676 * 0.99737809
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84146 * 0.58434970
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89802 * 0.74686078
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69606 * 0.23309122
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98320 * 0.10318753
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87041 * 0.10585845
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51115 * 0.04854932
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37831 * 0.51276936
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55868 * 0.86020823
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83880 * 0.08336762
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26070 * 0.62666043
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27071 * 0.78011325
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56129 * 0.26393895
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32980 * 0.56716870
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44755 * 0.53438042
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58887 * 0.03090408
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65357 * 0.90693022
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8082 * 0.49336497
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71661 * 0.86822388
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 505 * 0.48452036
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30826 * 0.83320786
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6671 * 0.87012111
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61270 * 0.61052225
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55346 * 0.43057112
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43032 * 0.37796997
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32463 * 0.46274535
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8311 * 0.92508309
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 78762 * 0.62459178
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9991 * 0.28558200
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99091 * 0.52453037
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'ckzhkohr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0033():
    """Extended test 33 for aggregation."""
    x_0 = 27098 * 0.05985734
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24059 * 0.12398981
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16501 * 0.97054145
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1155 * 0.19223728
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19244 * 0.89174918
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59384 * 0.91448151
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33157 * 0.21447384
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43811 * 0.69362296
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49511 * 0.90130419
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18138 * 0.85813398
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50719 * 0.67729068
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55666 * 0.83703803
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82342 * 0.26360503
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72470 * 0.22027766
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78495 * 0.80602599
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41289 * 0.71080606
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65504 * 0.05805631
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44402 * 0.85368637
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93880 * 0.90472568
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14036 * 0.27416899
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90938 * 0.44001419
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75662 * 0.48695206
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8145 * 0.92987493
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32907 * 0.37919954
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19621 * 0.27422123
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84878 * 0.07456074
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67670 * 0.21975391
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29206 * 0.58480697
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18782 * 0.72519586
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52052 * 0.84514266
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49508 * 0.14014688
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58000 * 0.89708430
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39822 * 0.90719905
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87308 * 0.99514505
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97037 * 0.55917706
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34716 * 0.05240983
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20122 * 0.62569541
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64019 * 0.66451439
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2168 * 0.96283576
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92663 * 0.78308608
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8741 * 0.75244835
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'kjypdbsr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0034():
    """Extended test 34 for aggregation."""
    x_0 = 16445 * 0.59439771
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97764 * 0.87313630
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11529 * 0.92826315
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22644 * 0.07316286
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89626 * 0.29213807
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12764 * 0.17614671
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53275 * 0.14454729
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95551 * 0.26355621
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14777 * 0.90330844
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34217 * 0.69808855
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92625 * 0.34672271
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33018 * 0.47726859
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6928 * 0.35294624
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31303 * 0.19990337
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20124 * 0.05690396
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83002 * 0.77999089
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13360 * 0.97434387
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30083 * 0.22143311
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40661 * 0.56062863
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92675 * 0.05037652
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5213 * 0.04476457
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88820 * 0.94016824
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32673 * 0.72760069
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46654 * 0.44138572
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88826 * 0.73917510
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22245 * 0.60040121
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85829 * 0.88857219
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49780 * 0.09878315
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30673 * 0.66673554
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82212 * 0.18532267
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72504 * 0.14461024
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44887 * 0.43579582
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33078 * 0.58964349
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99754 * 0.02585763
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8507 * 0.35000615
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'zlsrcvzi').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0035():
    """Extended test 35 for aggregation."""
    x_0 = 97690 * 0.32366445
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93194 * 0.00060055
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58162 * 0.67868377
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72041 * 0.10406108
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71811 * 0.62423736
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79327 * 0.07207889
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74233 * 0.71320577
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65927 * 0.41222444
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68809 * 0.52827602
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40323 * 0.45931783
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99085 * 0.82744861
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90476 * 0.30937601
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65653 * 0.05426002
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84572 * 0.00512684
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96073 * 0.74023974
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85656 * 0.00859802
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73402 * 0.03078823
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38944 * 0.57456568
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23116 * 0.06743043
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28134 * 0.44017377
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94084 * 0.69101196
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9710 * 0.60629603
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96991 * 0.63448393
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38890 * 0.56754871
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83926 * 0.47574861
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45807 * 0.15275660
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95010 * 0.60638214
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78536 * 0.07589613
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74354 * 0.60115847
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75943 * 0.21826027
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 842 * 0.58833846
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41799 * 0.27807063
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33441 * 0.56745551
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31587 * 0.53313281
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61059 * 0.44776801
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85657 * 0.36965977
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68246 * 0.32731626
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15886 * 0.79329110
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49210 * 0.78502921
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41461 * 0.92375825
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71852 * 0.63330232
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 61301 * 0.23639088
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 92222 * 0.92509749
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'gfghtklx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0036():
    """Extended test 36 for aggregation."""
    x_0 = 62217 * 0.31579129
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67848 * 0.16218889
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7129 * 0.47265510
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21214 * 0.97843625
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16260 * 0.60542823
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43690 * 0.10636802
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35922 * 0.55976201
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7337 * 0.49825316
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55209 * 0.87858520
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69017 * 0.88917887
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3837 * 0.13730840
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21507 * 0.55086233
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66745 * 0.85567672
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73645 * 0.92587413
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16651 * 0.76090649
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24445 * 0.61453090
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33027 * 0.36651048
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11412 * 0.11113882
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67081 * 0.02886220
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55739 * 0.25972909
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8957 * 0.81560117
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15535 * 0.95484282
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63180 * 0.39286616
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34715 * 0.25979563
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50256 * 0.93175048
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95831 * 0.16274811
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77805 * 0.24881740
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77929 * 0.21025061
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60301 * 0.99462676
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30889 * 0.44803951
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38396 * 0.67577912
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13455 * 0.04524624
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24186 * 0.97839593
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80331 * 0.18115682
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3159 * 0.14310211
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45790 * 0.25951046
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'wdmauxlp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0037():
    """Extended test 37 for aggregation."""
    x_0 = 27539 * 0.13387087
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32948 * 0.47530410
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78277 * 0.51011520
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8003 * 0.78452465
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71208 * 0.15156298
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99331 * 0.12271510
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94865 * 0.01270595
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28401 * 0.62008099
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41023 * 0.25433349
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72848 * 0.05776379
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78437 * 0.38686520
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70105 * 0.94298191
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65693 * 0.85574348
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15033 * 0.05837342
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98084 * 0.78424679
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94381 * 0.58340942
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28721 * 0.28403901
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91455 * 0.52731944
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82230 * 0.73513308
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85809 * 0.69427878
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14294 * 0.94433459
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7079 * 0.82656790
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60785 * 0.70305405
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8257 * 0.30874383
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33349 * 0.28443374
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38807 * 0.03076572
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58145 * 0.98654298
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14342 * 0.96903225
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45858 * 0.36565668
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35013 * 0.40519221
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85845 * 0.31922451
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88800 * 0.65513768
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23822 * 0.09819757
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58158 * 0.83619994
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85937 * 0.54894536
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52847 * 0.64334166
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29158 * 0.26588586
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29616 * 0.35980052
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73157 * 0.90428425
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47473 * 0.38416636
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 58503 * 0.95344348
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53312 * 0.76011276
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 45110 * 0.35471402
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 9725 * 0.21312816
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 74720 * 0.92452917
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 83094 * 0.59471380
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 7247 * 0.11056218
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 33544 * 0.40442840
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'suqhmpbv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0038():
    """Extended test 38 for aggregation."""
    x_0 = 39617 * 0.63204415
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65447 * 0.50393353
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31142 * 0.53644952
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60059 * 0.19684394
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60073 * 0.80896874
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50015 * 0.94252443
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61122 * 0.45044606
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31077 * 0.01628848
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82051 * 0.72792549
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 688 * 0.95011880
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72540 * 0.02719256
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55369 * 0.91563297
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3558 * 0.47786598
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29675 * 0.66701560
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49316 * 0.24118212
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26789 * 0.49897355
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55991 * 0.44090577
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42486 * 0.33492712
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84535 * 0.07965588
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56098 * 0.80269686
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58140 * 0.28438206
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8819 * 0.99154229
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35134 * 0.67959254
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18903 * 0.94331840
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17379 * 0.23483886
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1736 * 0.63011574
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21441 * 0.55545465
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54593 * 0.89639789
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54294 * 0.60274180
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5960 * 0.41189062
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73939 * 0.37534741
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12722 * 0.05907860
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70550 * 0.29859839
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35334 * 0.04615608
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45923 * 0.82289190
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45538 * 0.79504657
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20279 * 0.30178935
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72360 * 0.32268017
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46032 * 0.66975072
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98954 * 0.50609965
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'khteohix').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0039():
    """Extended test 39 for aggregation."""
    x_0 = 63734 * 0.74891255
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84537 * 0.55998280
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78579 * 0.87360819
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59777 * 0.24837505
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48941 * 0.66440987
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31818 * 0.09341315
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11790 * 0.66097393
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86074 * 0.20720928
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76811 * 0.61642612
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82562 * 0.33474284
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80776 * 0.38393478
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14454 * 0.77975215
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31313 * 0.33426431
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13609 * 0.91478751
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81767 * 0.93819918
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51247 * 0.26958258
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3149 * 0.97411813
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34715 * 0.13096533
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84439 * 0.85847751
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27673 * 0.46588547
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46056 * 0.43855643
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16491 * 0.25045667
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90269 * 0.71763782
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66883 * 0.17350634
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14805 * 0.94669508
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'lnntsyeo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0040():
    """Extended test 40 for aggregation."""
    x_0 = 767 * 0.97092823
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87506 * 0.59848174
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3894 * 0.59131152
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63359 * 0.97836153
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72731 * 0.49205368
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78907 * 0.89649814
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16885 * 0.17779887
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14376 * 0.11108241
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 406 * 0.15951681
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68085 * 0.89395188
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73174 * 0.61131482
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54020 * 0.07720125
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71683 * 0.97850624
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80641 * 0.31842670
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18603 * 0.18902850
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8084 * 0.33306373
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7331 * 0.45724886
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90240 * 0.93165490
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87426 * 0.73149708
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64274 * 0.87948174
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57652 * 0.79571707
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51 * 0.94837291
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41163 * 0.55496210
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91259 * 0.29998154
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13878 * 0.52938139
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66971 * 0.19759270
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8321 * 0.85948420
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12017 * 0.96974170
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25201 * 0.18837518
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98890 * 0.61081254
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34398 * 0.97413743
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40404 * 0.29641702
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70307 * 0.03668624
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60157 * 0.04982526
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80494 * 0.47983004
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98398 * 0.15307485
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 82042 * 0.66914011
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19187 * 0.99556435
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'eezcoaii').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0041():
    """Extended test 41 for aggregation."""
    x_0 = 27841 * 0.45599293
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12454 * 0.57861553
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57329 * 0.60696417
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4194 * 0.87077731
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28020 * 0.17240004
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2303 * 0.73228852
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88399 * 0.29077026
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47458 * 0.32319209
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94940 * 0.76568423
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80333 * 0.04830890
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60909 * 0.82605863
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99087 * 0.72299155
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3466 * 0.48772883
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81323 * 0.86762880
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4567 * 0.32793567
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63531 * 0.50969782
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13086 * 0.03132227
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29572 * 0.42967116
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37487 * 0.18435551
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72731 * 0.75382045
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34204 * 0.84537164
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54097 * 0.63006916
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85240 * 0.99461946
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7818 * 0.25799429
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20313 * 0.78866758
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'knortvtz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0042():
    """Extended test 42 for aggregation."""
    x_0 = 10389 * 0.03536510
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75129 * 0.61055935
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46909 * 0.10818064
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71138 * 0.01855978
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46328 * 0.00642740
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67124 * 0.64766027
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92275 * 0.03664464
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31945 * 0.61243116
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97751 * 0.68430169
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66185 * 0.98083430
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54572 * 0.68861935
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49062 * 0.83096893
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53433 * 0.98516590
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98599 * 0.69244821
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8469 * 0.95988569
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71623 * 0.43114329
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14708 * 0.95236826
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56505 * 0.02670838
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15708 * 0.71739293
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1975 * 0.10208629
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3500 * 0.58777086
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67694 * 0.02755057
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46678 * 0.55745085
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32190 * 0.58877524
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89487 * 0.48579638
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81517 * 0.86948978
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1458 * 0.85044726
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14121 * 0.46011131
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43412 * 0.69678123
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'lmanqbux').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0043():
    """Extended test 43 for aggregation."""
    x_0 = 22971 * 0.98855551
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96606 * 0.00566925
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97437 * 0.60457074
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81098 * 0.39202403
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35961 * 0.06735958
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56679 * 0.95703239
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94955 * 0.92735850
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91429 * 0.21064638
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71180 * 0.32382344
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65611 * 0.49545797
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28356 * 0.12121184
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81309 * 0.48017534
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5771 * 0.86566003
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65983 * 0.69722751
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90984 * 0.36845063
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5825 * 0.84757614
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98809 * 0.95512402
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20881 * 0.44128952
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83847 * 0.28107757
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26278 * 0.32732939
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14544 * 0.70734055
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16862 * 0.30012836
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'szvhfsuf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0044():
    """Extended test 44 for aggregation."""
    x_0 = 5909 * 0.55471276
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68508 * 0.26577606
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82941 * 0.44730057
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97838 * 0.14337836
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36644 * 0.90455937
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51507 * 0.99958535
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66537 * 0.56306729
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92266 * 0.45855935
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81631 * 0.66514615
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46524 * 0.01818328
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14595 * 0.29867322
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75134 * 0.68717021
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33359 * 0.94573193
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41214 * 0.64306120
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58001 * 0.00500843
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17319 * 0.08500434
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19870 * 0.91380278
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62000 * 0.80365211
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97090 * 0.14741181
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78510 * 0.13004715
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43535 * 0.91439003
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46018 * 0.54183759
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8492 * 0.74454745
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93229 * 0.84960946
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75674 * 0.67097895
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32222 * 0.96208920
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30193 * 0.98821176
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73353 * 0.34591658
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65448 * 0.52284834
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17454 * 0.60325948
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'lpacnzmr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0045():
    """Extended test 45 for aggregation."""
    x_0 = 62742 * 0.69879424
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38035 * 0.85299034
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29423 * 0.20081469
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89267 * 0.97334013
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75200 * 0.65845178
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78512 * 0.67180901
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81308 * 0.26734591
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94302 * 0.31876831
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75054 * 0.44950960
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6416 * 0.08813719
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14019 * 0.16449933
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79290 * 0.40852151
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12534 * 0.18624585
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7476 * 0.56057930
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66337 * 0.75955818
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 367 * 0.83866421
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61908 * 0.50689103
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39969 * 0.29802632
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10459 * 0.29067365
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35064 * 0.96467321
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68553 * 0.47539384
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41361 * 0.08804434
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75257 * 0.08913203
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36746 * 0.53262935
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29440 * 0.63122697
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82475 * 0.45745418
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'kpdpxliy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0046():
    """Extended test 46 for aggregation."""
    x_0 = 52137 * 0.51572048
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91077 * 0.84338541
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28016 * 0.27461607
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50542 * 0.89848247
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41801 * 0.74102416
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41588 * 0.91507422
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97059 * 0.24960477
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1426 * 0.37395269
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28518 * 0.65673182
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53406 * 0.77693491
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84262 * 0.17732475
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46690 * 0.21378524
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10333 * 0.89085474
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48237 * 0.87810161
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27814 * 0.47894702
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73407 * 0.72529860
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52677 * 0.64553214
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11386 * 0.46286620
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23128 * 0.68532313
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32489 * 0.33744338
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64804 * 0.09739857
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76107 * 0.80799518
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3843 * 0.70611899
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79609 * 0.97106271
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6289 * 0.92688668
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97594 * 0.09609370
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64281 * 0.35569068
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5051 * 0.90301992
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85032 * 0.53656959
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63503 * 0.62191664
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9486 * 0.45089325
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14836 * 0.04029124
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93828 * 0.56255866
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25326 * 0.72210272
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92846 * 0.82398914
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47197 * 0.39740578
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19034 * 0.21763570
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29167 * 0.31224279
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17916 * 0.04581463
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83879 * 0.41712051
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12630 * 0.38665810
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89180 * 0.88107094
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'winjkxmm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0047():
    """Extended test 47 for aggregation."""
    x_0 = 18922 * 0.43167643
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58517 * 0.16831593
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41409 * 0.14243540
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11392 * 0.37060479
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4661 * 0.44083781
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85977 * 0.31531762
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13351 * 0.45725834
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64340 * 0.54180599
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89808 * 0.36518294
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86615 * 0.46973580
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65170 * 0.50515518
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87340 * 0.09538095
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23614 * 0.41292138
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83563 * 0.00141314
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38256 * 0.32736796
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27978 * 0.34995220
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49135 * 0.07119998
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96057 * 0.56470276
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80628 * 0.30134881
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76353 * 0.01285722
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58142 * 0.27353461
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92926 * 0.16403145
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24413 * 0.14657393
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45630 * 0.40224592
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59731 * 0.95061020
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17226 * 0.42835302
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65361 * 0.81895289
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48870 * 0.87037377
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87169 * 0.23340012
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39275 * 0.45181780
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18594 * 0.41493204
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4117 * 0.45838831
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10082 * 0.75423183
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'inmyaqdi').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0048():
    """Extended test 48 for aggregation."""
    x_0 = 2160 * 0.29961241
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2383 * 0.20455156
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64836 * 0.79255778
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64361 * 0.13192237
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26930 * 0.23237928
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81959 * 0.32362440
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56820 * 0.13189105
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40193 * 0.98953064
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21682 * 0.10001286
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41343 * 0.67816327
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60497 * 0.35665818
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75325 * 0.37712619
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76735 * 0.17645423
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62317 * 0.05646257
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41628 * 0.88854435
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26699 * 0.32182639
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52544 * 0.99447216
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81123 * 0.64446626
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70746 * 0.37110130
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36615 * 0.67327163
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17029 * 0.92295866
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45683 * 0.77887359
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18313 * 0.20798292
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82349 * 0.71874212
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93861 * 0.14154253
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98230 * 0.57048198
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28023 * 0.93521842
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24561 * 0.27159262
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94615 * 0.37596190
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63604 * 0.20284897
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56162 * 0.60305641
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69584 * 0.74495190
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83263 * 0.99956163
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61058 * 0.59164663
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8888 * 0.48030390
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23676 * 0.96817446
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16846 * 0.74162436
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91031 * 0.56047920
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84725 * 0.71093340
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'bcrtzupn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0049():
    """Extended test 49 for aggregation."""
    x_0 = 58362 * 0.49118764
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75609 * 0.51987848
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71786 * 0.80882096
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57256 * 0.15599190
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6083 * 0.34118964
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24597 * 0.32457273
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38780 * 0.88234389
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74510 * 0.89719124
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13640 * 0.15846022
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7294 * 0.53216601
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87748 * 0.01016697
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21185 * 0.92220047
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85646 * 0.25586932
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17394 * 0.65081539
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81352 * 0.81806385
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84551 * 0.41081321
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90218 * 0.66728119
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61157 * 0.43068980
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4969 * 0.01884130
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92530 * 0.83950720
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71532 * 0.46024270
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11896 * 0.37595055
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43423 * 0.18010603
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27807 * 0.39569439
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20147 * 0.80867300
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15012 * 0.29682093
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60686 * 0.63514526
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47909 * 0.58075447
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24142 * 0.59735107
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56227 * 0.74953913
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46687 * 0.98563599
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5633 * 0.29432777
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33379 * 0.92620237
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17819 * 0.26650018
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8778 * 0.38370102
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43382 * 0.39484641
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93996 * 0.15501446
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59164 * 0.20031680
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 3899 * 0.45629196
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56742 * 0.89083622
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64831 * 0.77038260
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41463 * 0.38049895
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 67371 * 0.39224119
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38246 * 0.51809115
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'juldnbut').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0050():
    """Extended test 50 for aggregation."""
    x_0 = 65554 * 0.10909832
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73661 * 0.33527751
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73645 * 0.17477431
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18898 * 0.99164257
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81513 * 0.19953855
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69305 * 0.57448636
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18482 * 0.31315796
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2391 * 0.23784093
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32517 * 0.03429310
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79962 * 0.60323890
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79294 * 0.21342479
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50972 * 0.55189723
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42898 * 0.96452886
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93506 * 0.79938314
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25912 * 0.68837758
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4431 * 0.82030850
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34142 * 0.09862727
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34447 * 0.88792302
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97714 * 0.08290049
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57018 * 0.57390554
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44219 * 0.09499813
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23176 * 0.24109240
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29298 * 0.49300638
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63239 * 0.50719514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37448 * 0.75568614
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53958 * 0.87564889
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87976 * 0.31267625
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43066 * 0.84841428
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11369 * 0.67187024
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52472 * 0.30956313
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42194 * 0.50142506
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81475 * 0.79820776
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34391 * 0.55869545
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42142 * 0.72055067
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52146 * 0.00718330
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'lpchklop').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0051():
    """Extended test 51 for aggregation."""
    x_0 = 7168 * 0.28623834
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7658 * 0.31398135
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40840 * 0.56810034
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80199 * 0.53236488
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7497 * 0.32752099
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36964 * 0.95237379
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30613 * 0.84686469
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20468 * 0.53010667
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58121 * 0.71241771
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3887 * 0.33789686
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15790 * 0.98890081
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65083 * 0.58477504
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37195 * 0.32403294
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95474 * 0.03371169
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17386 * 0.83162950
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43731 * 0.69326308
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52379 * 0.57132793
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23355 * 0.58862404
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79467 * 0.44913941
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36904 * 0.69343629
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63907 * 0.44653618
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29712 * 0.27906279
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38493 * 0.27926634
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99855 * 0.49569774
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19689 * 0.47316858
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30896 * 0.46111660
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57310 * 0.01790052
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91007 * 0.24608082
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94590 * 0.78584096
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50154 * 0.40070823
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45958 * 0.60259905
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7793 * 0.97632474
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36057 * 0.69483113
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58846 * 0.91602102
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45486 * 0.32085915
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 989 * 0.44377546
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89751 * 0.48160393
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41152 * 0.14529836
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78935 * 0.63174249
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67141 * 0.18649397
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4592 * 0.37437890
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6601 * 0.34443655
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11031 * 0.65713048
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 45843 * 0.31808813
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 31951 * 0.95202401
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 92544 * 0.29560186
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 13087 * 0.39289150
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'aacskoqk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0052():
    """Extended test 52 for aggregation."""
    x_0 = 68107 * 0.11249741
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53669 * 0.71664999
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67771 * 0.32438070
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69782 * 0.82348658
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86194 * 0.46771109
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48680 * 0.60377783
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81569 * 0.16576720
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60409 * 0.26740705
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53430 * 0.75041171
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17554 * 0.15137993
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56097 * 0.09849755
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89713 * 0.07843369
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81659 * 0.83950449
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56157 * 0.00619891
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64510 * 0.27739897
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39974 * 0.61848971
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97338 * 0.74686903
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80429 * 0.82134668
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54827 * 0.23466867
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99169 * 0.11013037
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60599 * 0.11914411
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81516 * 0.90631650
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68777 * 0.45671638
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14958 * 0.97283853
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86917 * 0.71624292
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69633 * 0.30122639
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18341 * 0.29902538
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8399 * 0.72058918
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24118 * 0.62598684
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10580 * 0.55907830
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35191 * 0.48903012
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41043 * 0.49248193
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96201 * 0.22794351
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25969 * 0.14292288
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17536 * 0.38594741
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45076 * 0.34398908
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30428 * 0.80178658
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'ooggbujt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0053():
    """Extended test 53 for aggregation."""
    x_0 = 40537 * 0.88453615
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66214 * 0.43936164
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19178 * 0.88292445
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34098 * 0.93688014
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12743 * 0.47401279
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85019 * 0.89348776
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89490 * 0.72977950
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26252 * 0.16704478
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71011 * 0.52351776
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6890 * 0.68635251
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12285 * 0.68669377
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 102 * 0.74995254
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15190 * 0.55202400
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42071 * 0.72139880
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7553 * 0.50111692
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50156 * 0.11873470
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21844 * 0.62894822
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2696 * 0.86029060
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59076 * 0.31044818
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56052 * 0.89154915
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48015 * 0.24411998
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79381 * 0.11642417
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5745 * 0.10752389
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17489 * 0.25667823
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26575 * 0.07984244
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 996 * 0.34906017
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52541 * 0.55826006
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59584 * 0.22543850
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85824 * 0.74678164
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67339 * 0.02200125
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43030 * 0.20148659
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 34172 * 0.62893519
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50199 * 0.69566214
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81113 * 0.75403471
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20869 * 0.59349151
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74408 * 0.54814070
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66184 * 0.73273976
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 76677 * 0.92574141
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9588 * 0.90791815
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44075 * 0.93598955
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85334 * 0.20245189
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21411 * 0.55808847
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28381 * 0.32169893
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 79779 * 0.17199507
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 90280 * 0.69359928
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 64488 * 0.06958227
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 59586 * 0.86898619
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 26041 * 0.27751787
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 6751 * 0.91973020
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'ohcrinyf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0054():
    """Extended test 54 for aggregation."""
    x_0 = 21271 * 0.84768174
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78280 * 0.21430780
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14376 * 0.73076507
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49151 * 0.89878341
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5590 * 0.06794878
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88587 * 0.87168822
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64834 * 0.46585236
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34646 * 0.78538869
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38484 * 0.06999461
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9527 * 0.11721346
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13089 * 0.52250934
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87119 * 0.45007114
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17411 * 0.61849102
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64620 * 0.72755955
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43791 * 0.55036174
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73483 * 0.78503429
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37822 * 0.37952008
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59517 * 0.09036216
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77518 * 0.13027105
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69030 * 0.70091275
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56136 * 0.39438270
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31681 * 0.26247398
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98743 * 0.29820335
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8998 * 0.14646654
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58874 * 0.08317241
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5831 * 0.72656177
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79244 * 0.09269842
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78100 * 0.67233182
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14996 * 0.78598637
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78440 * 0.44173843
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96759 * 0.47881925
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96274 * 0.29638587
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3930 * 0.64851152
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73414 * 0.98368016
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12402 * 0.75056571
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 92358 * 0.38195971
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16093 * 0.37057285
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1182 * 0.47556201
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 33998 * 0.00546435
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23884 * 0.41819292
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'latfmoaz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0055():
    """Extended test 55 for aggregation."""
    x_0 = 17319 * 0.39767435
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22586 * 0.19534230
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98664 * 0.90698637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38393 * 0.10577303
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15491 * 0.57841208
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59494 * 0.09043202
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28178 * 0.66071485
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48317 * 0.74174935
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86143 * 0.84824758
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58669 * 0.15208086
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63448 * 0.35019228
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98199 * 0.17740925
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9595 * 0.34565504
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27450 * 0.36032901
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66109 * 0.68563497
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35887 * 0.69666423
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58938 * 0.82529189
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36532 * 0.34078904
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91967 * 0.81975130
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43607 * 0.83870688
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42592 * 0.91370385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35450 * 0.82626582
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89124 * 0.08076928
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63075 * 0.19898957
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54297 * 0.80166759
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3260 * 0.80371226
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86436 * 0.43198269
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25029 * 0.51876415
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81946 * 0.69507196
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95092 * 0.20294247
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ymkocxdl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0056():
    """Extended test 56 for aggregation."""
    x_0 = 23971 * 0.10792354
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57069 * 0.72228427
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58079 * 0.50782674
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64071 * 0.98038750
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48856 * 0.07647516
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38858 * 0.33000449
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13543 * 0.42012068
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40621 * 0.49456510
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44821 * 0.51728426
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55837 * 0.31005775
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77768 * 0.94067858
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55268 * 0.18322878
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76001 * 0.61594057
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65896 * 0.41359009
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67558 * 0.54659984
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91982 * 0.96428775
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93979 * 0.24743936
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86944 * 0.95040156
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64129 * 0.66014145
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1822 * 0.75761017
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68955 * 0.08291543
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22517 * 0.24651409
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10368 * 0.99216193
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65065 * 0.27685009
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60034 * 0.78604664
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2397 * 0.20304177
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22226 * 0.94851144
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32442 * 0.69861599
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6089 * 0.20883463
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28071 * 0.55625612
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32313 * 0.23833510
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98298 * 0.78761034
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32673 * 0.64189334
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19024 * 0.76694813
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10077 * 0.73158593
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98691 * 0.24916050
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29676 * 0.47805837
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17456 * 0.12034948
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45331 * 0.21877320
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40191 * 0.02717025
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86930 * 0.50225772
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 28531 * 0.41502026
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35895 * 0.57927438
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20929 * 0.21160422
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 99363 * 0.91220170
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 54289 * 0.61133383
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 44797 * 0.26659168
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 96805 * 0.96664621
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 89857 * 0.95626986
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'uvozcpfn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0057():
    """Extended test 57 for aggregation."""
    x_0 = 48944 * 0.43941075
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60458 * 0.44230393
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37204 * 0.18264140
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14139 * 0.72803295
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20710 * 0.33883251
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57028 * 0.21784575
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67043 * 0.25535863
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32424 * 0.08713600
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57817 * 0.94768069
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15483 * 0.77614795
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37170 * 0.82042786
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87326 * 0.17731857
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68045 * 0.08415445
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16952 * 0.04626579
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31440 * 0.43041322
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72515 * 0.05382736
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88497 * 0.05118802
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92110 * 0.99330817
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86384 * 0.83105763
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96230 * 0.68120221
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95725 * 0.21219410
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72915 * 0.82798188
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29597 * 0.19077609
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48922 * 0.61648436
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17173 * 0.01994507
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5117 * 0.97295008
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37543 * 0.54157185
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68425 * 0.29677326
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87308 * 0.25285480
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'lmcpdame').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0058():
    """Extended test 58 for aggregation."""
    x_0 = 34638 * 0.69292155
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55233 * 0.48956200
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21882 * 0.76015768
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74881 * 0.27997651
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82382 * 0.93236765
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65477 * 0.46766592
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85816 * 0.09776908
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94201 * 0.77752521
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48050 * 0.79611445
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98209 * 0.94336097
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56520 * 0.10421110
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65761 * 0.83373286
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1568 * 0.24805592
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88759 * 0.59106043
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11656 * 0.92170882
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20825 * 0.85476623
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21827 * 0.81267902
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32114 * 0.36557545
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64718 * 0.00208963
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77264 * 0.07610182
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4461 * 0.40068930
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33091 * 0.45436643
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95512 * 0.75228522
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86427 * 0.50678228
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72560 * 0.72386349
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42516 * 0.74207187
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36300 * 0.90123022
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63748 * 0.92147895
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82051 * 0.41287517
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6968 * 0.68183171
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63692 * 0.12892137
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42180 * 0.11264243
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50325 * 0.66175348
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95075 * 0.43024749
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7653 * 0.05696269
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79791 * 0.97504933
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49805 * 0.24681810
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36129 * 0.93923945
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46797 * 0.58225492
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62246 * 0.94006076
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 30423 * 0.32943591
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82484 * 0.58973799
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95494 * 0.66907307
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 5521 * 0.64443794
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 3812 * 0.55548713
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 44783 * 0.88187389
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 87721 * 0.64961434
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 43675 * 0.35529428
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 3989 * 0.27011043
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'cnepdwil').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0059():
    """Extended test 59 for aggregation."""
    x_0 = 13288 * 0.91942742
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76458 * 0.54234032
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38247 * 0.15931549
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78319 * 0.91379196
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6130 * 0.12307037
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31810 * 0.99030643
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35376 * 0.01158439
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16160 * 0.68745799
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13213 * 0.71669153
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90990 * 0.67767862
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80641 * 0.38821004
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23353 * 0.05094372
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27672 * 0.06715895
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38514 * 0.97401266
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56157 * 0.98870056
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77419 * 0.66999184
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50951 * 0.50943073
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38634 * 0.05639766
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53188 * 0.70083985
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52827 * 0.72659590
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37129 * 0.32882274
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22950 * 0.36588672
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73871 * 0.06274417
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56899 * 0.53847903
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70777 * 0.55189314
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46000 * 0.02962929
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79655 * 0.04223785
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24967 * 0.07971107
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7572 * 0.86181837
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6514 * 0.04323503
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3779 * 0.42044666
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70474 * 0.34423568
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81878 * 0.51183256
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99789 * 0.48617417
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16235 * 0.23211319
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13229 * 0.95978675
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61360 * 0.56890176
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32396 * 0.02727057
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45224 * 0.30596228
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46653 * 0.36611614
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37955 * 0.42718015
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9598 * 0.80827652
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23217 * 0.72810119
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'jsvusnox').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0060():
    """Extended test 60 for aggregation."""
    x_0 = 52951 * 0.46918701
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93090 * 0.21546477
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80555 * 0.76842324
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23668 * 0.77232047
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4440 * 0.89540103
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 633 * 0.73927994
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21897 * 0.38066879
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64719 * 0.41638174
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97741 * 0.25565660
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65623 * 0.77583417
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84541 * 0.19136142
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61068 * 0.54664435
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60444 * 0.93388668
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87135 * 0.02833599
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13176 * 0.21971965
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55088 * 0.64596140
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43307 * 0.99811012
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81141 * 0.87940075
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10609 * 0.96968161
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96957 * 0.37666020
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89819 * 0.70402628
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64745 * 0.86551621
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74770 * 0.85220731
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86849 * 0.14960266
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23107 * 0.16970464
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77762 * 0.09031319
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98539 * 0.76181306
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41618 * 0.95017671
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20604 * 0.51288733
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84232 * 0.42552284
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88299 * 0.39595922
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75368 * 0.38254644
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40797 * 0.58192338
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63031 * 0.61179377
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77963 * 0.82840454
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15023 * 0.40475865
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 38889 * 0.44261330
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12271 * 0.70376730
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81685 * 0.95694847
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82854 * 0.51378002
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12605 * 0.11819808
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 29221 * 0.57364513
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 27248 * 0.80671767
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'nhzanlio').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0061():
    """Extended test 61 for aggregation."""
    x_0 = 53292 * 0.18720435
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2340 * 0.78004872
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33467 * 0.53055533
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75689 * 0.69159060
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83804 * 0.07890021
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32963 * 0.07337458
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7259 * 0.22179846
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27103 * 0.29963846
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72355 * 0.72129032
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48419 * 0.92713054
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80916 * 0.68635623
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42316 * 0.54550897
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30877 * 0.98696284
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84146 * 0.56424256
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67328 * 0.43769868
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9774 * 0.17587577
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79429 * 0.28047095
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2811 * 0.70952228
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65385 * 0.07707290
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73083 * 0.98315791
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70683 * 0.69016046
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56016 * 0.95021897
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22110 * 0.26737028
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79114 * 0.52525035
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73113 * 0.29430143
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78420 * 0.16853515
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36403 * 0.20679665
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'vtfofign').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0062():
    """Extended test 62 for aggregation."""
    x_0 = 15169 * 0.63648472
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2023 * 0.42103718
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54339 * 0.23340676
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75280 * 0.70700160
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57698 * 0.42500872
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51451 * 0.49688610
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75321 * 0.77014609
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15944 * 0.08769891
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83997 * 0.80975884
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32428 * 0.78875404
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91932 * 0.18783355
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30357 * 0.31346249
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29964 * 0.95876911
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22334 * 0.55558917
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49942 * 0.97250029
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69995 * 0.30667107
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61398 * 0.45672973
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56898 * 0.20225954
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80826 * 0.57595328
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33947 * 0.62283311
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47695 * 0.43981894
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24799 * 0.31567833
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'wrcjphnc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0063():
    """Extended test 63 for aggregation."""
    x_0 = 41195 * 0.94244919
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13136 * 0.47360983
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93037 * 0.46667484
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62109 * 0.40808945
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94676 * 0.84030942
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89999 * 0.12855861
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2947 * 0.73848693
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85063 * 0.88128661
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35994 * 0.38845849
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80796 * 0.08083331
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69061 * 0.71333369
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21820 * 0.99681166
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43516 * 0.00730190
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46509 * 0.01770628
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61231 * 0.02872980
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87670 * 0.17107954
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7719 * 0.44160668
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67021 * 0.66226372
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67932 * 0.93297641
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41332 * 0.24663143
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41545 * 0.39082372
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83896 * 0.16262879
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'zfcysiub').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0064():
    """Extended test 64 for aggregation."""
    x_0 = 77631 * 0.47481572
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6034 * 0.89014018
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35897 * 0.36173737
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98520 * 0.21976811
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16818 * 0.69536976
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51838 * 0.59045756
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40217 * 0.80101981
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36902 * 0.45835317
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4104 * 0.26933293
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42881 * 0.01615138
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49414 * 0.62240772
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31795 * 0.61498534
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72900 * 0.45643603
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98863 * 0.04986959
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90497 * 0.10688872
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3637 * 0.32918024
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24694 * 0.24834662
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19123 * 0.88642464
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83199 * 0.76869115
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46690 * 0.38982164
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'mhxafvoo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0065():
    """Extended test 65 for aggregation."""
    x_0 = 70525 * 0.25832378
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64135 * 0.17035388
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23980 * 0.29179461
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85579 * 0.91627489
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79732 * 0.09937229
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48341 * 0.61214531
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53350 * 0.63934289
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77909 * 0.72567996
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91669 * 0.35251174
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39067 * 0.11644467
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16857 * 0.17071932
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44249 * 0.04841053
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57612 * 0.28528435
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35933 * 0.58868915
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8218 * 0.65870189
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13490 * 0.53543237
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29654 * 0.63669195
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42272 * 0.78720922
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82523 * 0.69188526
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53150 * 0.55497809
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41221 * 0.82129038
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6266 * 0.17173362
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3131 * 0.86884113
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97398 * 0.06191136
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61618 * 0.91967074
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29122 * 0.65804687
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33105 * 0.01731525
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25446 * 0.61340271
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24837 * 0.23320479
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1889 * 0.21590232
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6730 * 0.29163685
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45098 * 0.98126129
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32182 * 0.33587010
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51487 * 0.94224421
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52669 * 0.32865766
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18101 * 0.44242264
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99086 * 0.79273817
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42112 * 0.55125649
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16495 * 0.74119202
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97690 * 0.70679452
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3824 * 0.02547111
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 78828 * 0.02478246
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46058 * 0.14975461
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 21792 * 0.30000329
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 34779 * 0.26841129
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 58354 * 0.81525957
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'vsfvqsou').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0066():
    """Extended test 66 for aggregation."""
    x_0 = 46191 * 0.03739841
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26029 * 0.19533985
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32294 * 0.58602310
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63881 * 0.52961121
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74211 * 0.21444658
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84895 * 0.99754834
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40992 * 0.34479754
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43932 * 0.00549007
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92414 * 0.71384002
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98610 * 0.52917073
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19227 * 0.16962060
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97194 * 0.66406750
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60976 * 0.76633100
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80518 * 0.02795683
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38085 * 0.12210369
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86712 * 0.49152319
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82803 * 0.25528745
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91665 * 0.15209626
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99124 * 0.03413386
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49571 * 0.33758963
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19733 * 0.55478123
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88607 * 0.08132711
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14792 * 0.97620955
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96382 * 0.73408284
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53948 * 0.73527177
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66514 * 0.08635194
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88076 * 0.20617418
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98632 * 0.21785319
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21501 * 0.60937767
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79328 * 0.76833829
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94783 * 0.77531420
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67365 * 0.54934562
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2745 * 0.13212376
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79115 * 0.15538887
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46543 * 0.28872149
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88963 * 0.65985862
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76571 * 0.56496167
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82537 * 0.99492361
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 22561 * 0.34397053
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59265 * 0.99710118
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11142 * 0.54281032
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3106 * 0.04404220
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'vvszycga').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0067():
    """Extended test 67 for aggregation."""
    x_0 = 30158 * 0.44782554
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88211 * 0.93886874
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77813 * 0.67437324
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44953 * 0.48080471
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15108 * 0.05474619
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67169 * 0.58921002
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45857 * 0.72074328
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13955 * 0.11376456
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54811 * 0.72698619
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59812 * 0.38362833
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14888 * 0.60244773
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12449 * 0.15849832
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78841 * 0.48819472
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67843 * 0.87915359
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57028 * 0.57988518
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59905 * 0.61774607
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14513 * 0.27252890
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16218 * 0.26140671
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38049 * 0.18727981
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89941 * 0.49449138
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43966 * 0.40775869
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63611 * 0.47554576
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29433 * 0.85130184
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18953 * 0.60580632
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85427 * 0.53759020
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91223 * 0.53511276
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83995 * 0.53283540
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77710 * 0.96674790
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37846 * 0.55527810
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1044 * 0.52641913
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65890 * 0.04166711
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1318 * 0.48819251
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24192 * 0.50844381
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75168 * 0.59900805
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14579 * 0.42435821
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33380 * 0.29784581
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28345 * 0.53835926
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18206 * 0.63378426
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20689 * 0.11343522
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23525 * 0.33264296
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 31781 * 0.56197498
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70442 * 0.84863516
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 25536 * 0.24433831
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 30042 * 0.70220459
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 43465 * 0.10890363
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 5148 * 0.22932930
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 14657 * 0.74564528
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 75728 * 0.75715806
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 5320 * 0.38338854
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 94732 * 0.40752877
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'vrwaqbok').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0068():
    """Extended test 68 for aggregation."""
    x_0 = 89440 * 0.02393626
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74314 * 0.74468933
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3666 * 0.73179259
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84787 * 0.71743277
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70184 * 0.85420782
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95665 * 0.97205445
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35362 * 0.92815514
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20341 * 0.45391717
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40237 * 0.95049870
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81833 * 0.38273507
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63417 * 0.24651320
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78228 * 0.15840790
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15744 * 0.97138868
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16046 * 0.22387991
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62574 * 0.91908993
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44615 * 0.47163747
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20418 * 0.06280104
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47028 * 0.79089655
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36626 * 0.97282767
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61008 * 0.49718889
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84276 * 0.52866374
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49378 * 0.35858048
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28592 * 0.03127890
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39635 * 0.28428694
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37033 * 0.60193920
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55551 * 0.12488600
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86257 * 0.15931609
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18466 * 0.09788090
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60103 * 0.29036119
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10853 * 0.50041641
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45558 * 0.47505531
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90169 * 0.73236378
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17044 * 0.53049851
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90825 * 0.62191753
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26824 * 0.76071850
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71649 * 0.23211772
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39245 * 0.51968618
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4248 * 0.11766925
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43921 * 0.55897517
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74418 * 0.83972815
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81326 * 0.27114266
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3250 * 0.35376205
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'twpyusad').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_0_0069():
    """Extended test 69 for aggregation."""
    x_0 = 69603 * 0.74361397
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1061 * 0.83517954
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12991 * 0.08543609
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37968 * 0.58663629
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55181 * 0.65742233
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46893 * 0.28584752
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62898 * 0.20988615
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35830 * 0.44414279
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58744 * 0.92187986
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56872 * 0.82337489
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43478 * 0.62150362
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22554 * 0.16913837
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19023 * 0.11021685
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29760 * 0.77259173
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62903 * 0.16261509
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63491 * 0.46417990
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83959 * 0.91444197
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52483 * 0.71316585
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37090 * 0.36748833
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74572 * 0.48228693
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80575 * 0.88974692
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88929 * 0.22159911
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6159 * 0.43743270
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31289 * 0.97487698
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41716 * 0.90403897
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78833 * 0.02040461
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90038 * 0.59784361
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18269 * 0.93965743
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68533 * 0.55503967
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48695 * 0.27021121
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91436 * 0.91267078
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31791 * 0.35269494
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'lgxybboi').hexdigest()
    assert len(h) == 64
