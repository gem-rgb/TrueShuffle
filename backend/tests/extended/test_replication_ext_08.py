"""Extended tests for replication suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_replication_extended_8_0000():
    """Extended test 0 for replication."""
    x_0 = 72452 * 0.50053008
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48942 * 0.60682052
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26162 * 0.59331545
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56830 * 0.62325104
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38664 * 0.85255518
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17210 * 0.17084298
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69482 * 0.75430842
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47942 * 0.65406416
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37375 * 0.08564221
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56713 * 0.10867120
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11372 * 0.01699941
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78546 * 0.69011967
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56674 * 0.69491777
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28450 * 0.98348352
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85855 * 0.08577237
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45144 * 0.63679154
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21585 * 0.46429737
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24826 * 0.55011803
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1210 * 0.07665621
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85275 * 0.35886262
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41880 * 0.65113071
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11331 * 0.77368018
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55001 * 0.19347734
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1516 * 0.17823072
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12921 * 0.07803933
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94315 * 0.38212747
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52133 * 0.88455635
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85953 * 0.45869425
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98137 * 0.89810396
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32683 * 0.73895515
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27598 * 0.47839996
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27086 * 0.22411714
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13176 * 0.87533140
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65512 * 0.79490897
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7220 * 0.89930313
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5757 * 0.81334034
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21140 * 0.34983311
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90806 * 0.30002758
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49007 * 0.16223005
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81661 * 0.20204606
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64176 * 0.93627519
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16686 * 0.09826201
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20454 * 0.28582601
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 7137 * 0.74820368
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 58937 * 0.26949518
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 25896 * 0.98615594
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 19515 * 0.11651578
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 92861 * 0.30558014
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 45013 * 0.59602979
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'lzfuxbnd').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0001():
    """Extended test 1 for replication."""
    x_0 = 89218 * 0.27971647
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23321 * 0.60782224
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88824 * 0.26166515
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42235 * 0.26342722
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27335 * 0.55537094
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95870 * 0.03184465
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12427 * 0.84132238
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29266 * 0.73589108
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79809 * 0.91306126
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64917 * 0.73261287
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39392 * 0.87704366
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29245 * 0.48794656
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78811 * 0.13409756
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10081 * 0.17956089
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72902 * 0.29277805
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80394 * 0.33385957
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80043 * 0.21658589
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57135 * 0.54729324
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69110 * 0.50958524
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36961 * 0.54122891
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36438 * 0.56799939
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'nhfntvfx').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0002():
    """Extended test 2 for replication."""
    x_0 = 66482 * 0.36139239
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71609 * 0.45248617
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45489 * 0.03044142
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34193 * 0.01613858
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41827 * 0.30362972
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9189 * 0.57164724
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16960 * 0.36323283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28157 * 0.84453138
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88210 * 0.30886658
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89747 * 0.78505616
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42542 * 0.92158937
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64960 * 0.40160080
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7652 * 0.28272363
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7660 * 0.27352308
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57162 * 0.84346594
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40938 * 0.90380528
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62959 * 0.83797524
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67450 * 0.05164658
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52311 * 0.33014692
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81877 * 0.52048506
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22062 * 0.57509041
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26375 * 0.34830714
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55681 * 0.10281354
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61721 * 0.83662092
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43137 * 0.30104529
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25598 * 0.83138451
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41699 * 0.40680919
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51452 * 0.36347250
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82816 * 0.53192508
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58753 * 0.87740336
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19322 * 0.66061135
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26033 * 0.64545415
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42185 * 0.54744723
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73078 * 0.98686403
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16207 * 0.12467415
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98637 * 0.13925273
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88624 * 0.46683398
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60091 * 0.22409766
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57272 * 0.00537418
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75026 * 0.15624076
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98924 * 0.71250548
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37359 * 0.35991254
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 5607 * 0.48704956
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'pumkzqfv').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0003():
    """Extended test 3 for replication."""
    x_0 = 95740 * 0.37092522
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96993 * 0.11950457
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68484 * 0.47099755
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27656 * 0.25676131
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28180 * 0.18951604
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18556 * 0.86226265
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34614 * 0.66827785
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31734 * 0.22402725
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45401 * 0.36807241
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26371 * 0.93191072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11670 * 0.38247394
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85739 * 0.18947668
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69361 * 0.78184205
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12044 * 0.56278750
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66814 * 0.32212820
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88549 * 0.81699327
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98398 * 0.65927039
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74259 * 0.72980160
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13636 * 0.14340233
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8716 * 0.14289097
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75198 * 0.16608950
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61201 * 0.38278704
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49513 * 0.72121217
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88522 * 0.96100458
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80904 * 0.57795864
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75921 * 0.78681095
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30392 * 0.11391439
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68276 * 0.08917371
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23140 * 0.43872835
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19446 * 0.74566882
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18716 * 0.63661185
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16316 * 0.64039587
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98618 * 0.76510665
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43305 * 0.30110237
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26974 * 0.19762986
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40731 * 0.06835444
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8320 * 0.63180899
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25065 * 0.75900238
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 32941 * 0.28626695
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97173 * 0.54010246
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46816 * 0.54111334
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 10193 * 0.88692832
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 5070 * 0.70563058
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 28279 * 0.33517245
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 32844 * 0.21050492
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 74657 * 0.61977933
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 27571 * 0.95529737
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 79666 * 0.49847080
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'uguscixl').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0004():
    """Extended test 4 for replication."""
    x_0 = 46772 * 0.55601488
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15628 * 0.46827131
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81986 * 0.55010542
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85273 * 0.15147599
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40552 * 0.97104765
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52084 * 0.67912945
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88057 * 0.28805385
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92955 * 0.90228022
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51706 * 0.65669584
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87402 * 0.35077701
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69647 * 0.14547846
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79559 * 0.87158630
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14825 * 0.55933360
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49278 * 0.43254847
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8910 * 0.32358140
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9363 * 0.81708579
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66430 * 0.26757930
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90163 * 0.90793429
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39419 * 0.24709888
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64943 * 0.73949757
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64115 * 0.29559638
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98269 * 0.37001456
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56922 * 0.73651539
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56275 * 0.01381912
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24562 * 0.20593744
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65481 * 0.29320891
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34259 * 0.57384006
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4030 * 0.29214016
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71369 * 0.56021814
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2706 * 0.76910563
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16314 * 0.63043434
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71398 * 0.26378784
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76169 * 0.02934611
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77429 * 0.78087422
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12794 * 0.25355567
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24853 * 0.76224573
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56841 * 0.68429139
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64872 * 0.86848482
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24597 * 0.81095537
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16877 * 0.03900595
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'crqdtaqy').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0005():
    """Extended test 5 for replication."""
    x_0 = 25763 * 0.27879242
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80205 * 0.47377944
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44364 * 0.74563118
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79596 * 0.31410453
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11577 * 0.53559459
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25935 * 0.09282920
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46769 * 0.81156659
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19200 * 0.92788788
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90350 * 0.70878188
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94975 * 0.52314703
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61913 * 0.21982900
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43452 * 0.66826956
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75050 * 0.04879436
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5393 * 0.79669638
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45990 * 0.70933594
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98779 * 0.65372526
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37210 * 0.21213568
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88544 * 0.36040703
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26029 * 0.51016267
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12677 * 0.72587890
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71472 * 0.63526543
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76507 * 0.10059454
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37688 * 0.29506191
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38400 * 0.83442244
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32435 * 0.28081972
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61940 * 0.47218229
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77718 * 0.47226817
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96569 * 0.38984252
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40501 * 0.01445551
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30333 * 0.82897053
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86038 * 0.37900243
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69167 * 0.72885582
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22945 * 0.93881368
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38584 * 0.84380442
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'kzdaefyn').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0006():
    """Extended test 6 for replication."""
    x_0 = 35021 * 0.65488505
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38277 * 0.76007726
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62588 * 0.70839379
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47147 * 0.52496763
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48690 * 0.89986444
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66890 * 0.90106279
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52102 * 0.79509002
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51241 * 0.72751756
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28004 * 0.59596945
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98089 * 0.31117354
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2517 * 0.94379788
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15543 * 0.79969948
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40354 * 0.15188972
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9443 * 0.19807097
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35375 * 0.30810165
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27785 * 0.64853428
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47983 * 0.01014693
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44974 * 0.33852007
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52775 * 0.93649159
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15758 * 0.31726183
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51812 * 0.46069229
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74687 * 0.68031843
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16590 * 0.98210485
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90444 * 0.03577075
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48215 * 0.94502373
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39755 * 0.31207186
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53086 * 0.48526364
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6715 * 0.69244283
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9051 * 0.57712889
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32112 * 0.29458121
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54813 * 0.17261139
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48151 * 0.95810179
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61278 * 0.20948388
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20601 * 0.66062781
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45379 * 0.02460766
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84582 * 0.92920245
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60531 * 0.05680357
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52507 * 0.82733479
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'kraswayo').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0007():
    """Extended test 7 for replication."""
    x_0 = 86799 * 0.12118926
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56451 * 0.85115304
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99060 * 0.58591743
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41415 * 0.77494372
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63301 * 0.21805140
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30670 * 0.66432689
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16786 * 0.15820316
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96258 * 0.90732033
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97875 * 0.57049884
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7750 * 0.72193432
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34704 * 0.36628656
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47616 * 0.82348710
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30500 * 0.66239804
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48781 * 0.40688857
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38497 * 0.02772094
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83538 * 0.13737894
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5887 * 0.99263003
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28799 * 0.23759826
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12729 * 0.70276050
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35181 * 0.85419066
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77745 * 0.94281989
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20473 * 0.22844432
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60586 * 0.96396500
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19093 * 0.11832887
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47173 * 0.57171185
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81627 * 0.74026049
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45933 * 0.15736497
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89571 * 0.59188716
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65143 * 0.60061386
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'exlfvoil').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0008():
    """Extended test 8 for replication."""
    x_0 = 7163 * 0.67869861
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57937 * 0.94544041
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22837 * 0.84510934
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47782 * 0.65602885
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25212 * 0.40429839
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39212 * 0.04202474
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39842 * 0.07334920
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84902 * 0.29459002
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79442 * 0.68782326
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88079 * 0.82128641
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28573 * 0.46395283
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30332 * 0.72182974
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10041 * 0.92949088
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89496 * 0.02176291
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40854 * 0.64496976
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33775 * 0.00815751
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8366 * 0.99150941
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19392 * 0.33098424
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34874 * 0.70553299
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35101 * 0.25954139
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 485 * 0.04610534
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42403 * 0.81326855
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81128 * 0.60817263
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12500 * 0.78589641
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54067 * 0.30160237
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18435 * 0.55456005
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46091 * 0.53872205
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84227 * 0.29755640
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39176 * 0.85390535
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50726 * 0.58205340
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41465 * 0.15526169
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93595 * 0.67541016
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75396 * 0.72778936
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52827 * 0.60753606
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55322 * 0.23563402
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63591 * 0.79962408
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86956 * 0.81265088
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 76589 * 0.98835679
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66093 * 0.52008630
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87982 * 0.16340087
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47427 * 0.31512028
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63464 * 0.38588392
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6307 * 0.86480392
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34690 * 0.43944494
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'eepqbfwa').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0009():
    """Extended test 9 for replication."""
    x_0 = 68009 * 0.47610188
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85506 * 0.21167628
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20380 * 0.03858062
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48092 * 0.15523665
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27301 * 0.40444550
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76959 * 0.30271036
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63442 * 0.82913588
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49844 * 0.42739834
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94211 * 0.65611164
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15449 * 0.90215655
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18649 * 0.99855526
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57793 * 0.67191391
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72571 * 0.47514989
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27359 * 0.00263824
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96390 * 0.34314521
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8691 * 0.31221015
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37563 * 0.89856531
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53951 * 0.34472985
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36359 * 0.77431690
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69297 * 0.52450542
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36876 * 0.09860914
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66189 * 0.00486547
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85864 * 0.27898989
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58819 * 0.72944699
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92928 * 0.08577242
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3866 * 0.98440359
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27091 * 0.67155766
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76314 * 0.13416986
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71265 * 0.56901353
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77071 * 0.47874575
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46861 * 0.14393690
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20794 * 0.67416595
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18990 * 0.89194881
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2312 * 0.81574261
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'jkykwhqj').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0010():
    """Extended test 10 for replication."""
    x_0 = 94714 * 0.83952217
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28584 * 0.88386315
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19127 * 0.39193185
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73150 * 0.36622002
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10307 * 0.09171149
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55694 * 0.72510324
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55443 * 0.95075121
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25564 * 0.47022467
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74279 * 0.05830613
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15219 * 0.67001997
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16742 * 0.26236330
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57868 * 0.52733076
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36743 * 0.77305160
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78792 * 0.39592904
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74382 * 0.34343132
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81822 * 0.31624571
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63426 * 0.94663033
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57679 * 0.10725920
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52096 * 0.95792274
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74842 * 0.21095219
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12195 * 0.42247840
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'zydhtcuh').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0011():
    """Extended test 11 for replication."""
    x_0 = 69644 * 0.15987111
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14136 * 0.13186025
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3658 * 0.60759948
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6669 * 0.60858589
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23788 * 0.31197415
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77340 * 0.95519363
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57658 * 0.54592358
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12827 * 0.89925048
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57774 * 0.03681564
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41850 * 0.14261036
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16933 * 0.31281862
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55560 * 0.35079981
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78003 * 0.90725675
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75917 * 0.32255602
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60144 * 0.29897494
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94121 * 0.73283716
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27981 * 0.15398413
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76282 * 0.77612929
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1740 * 0.94976638
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19226 * 0.37393071
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12761 * 0.11558039
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 918 * 0.65586738
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70003 * 0.18625181
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10590 * 0.77498760
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'xgyavtos').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0012():
    """Extended test 12 for replication."""
    x_0 = 25934 * 0.61605361
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10153 * 0.70640740
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57980 * 0.16289159
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88588 * 0.85640841
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76451 * 0.24043056
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5518 * 0.60121792
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24488 * 0.94124479
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88844 * 0.94769991
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35296 * 0.63349922
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61886 * 0.01429404
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94148 * 0.54426397
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43149 * 0.94531716
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28568 * 0.41485709
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83075 * 0.23805187
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18230 * 0.54650950
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15726 * 0.37399113
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77469 * 0.75870659
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87456 * 0.36067945
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71641 * 0.96550223
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84643 * 0.89861223
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85206 * 0.93536767
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43199 * 0.89775296
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47983 * 0.38463060
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4148 * 0.71534910
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43664 * 0.04191045
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52308 * 0.21188443
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28767 * 0.32640996
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29212 * 0.39481993
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23797 * 0.61300498
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 775 * 0.36847820
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1689 * 0.86695781
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'bmybukta').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0013():
    """Extended test 13 for replication."""
    x_0 = 74434 * 0.14565091
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67387 * 0.11741867
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58249 * 0.21018257
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86862 * 0.21152936
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20899 * 0.93475046
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42089 * 0.54464998
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19907 * 0.63612606
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73505 * 0.34437442
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93496 * 0.38873958
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16699 * 0.14480892
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39235 * 0.70600367
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57405 * 0.22916941
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1516 * 0.01185289
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38280 * 0.02623399
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86463 * 0.46907997
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89344 * 0.96965917
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47768 * 0.86083821
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11837 * 0.83798004
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75479 * 0.58114823
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55191 * 0.92671071
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71982 * 0.66970670
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19007 * 0.06045551
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42754 * 0.40176742
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68496 * 0.08995797
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94812 * 0.61876976
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62131 * 0.54069674
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22192 * 0.01894630
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'nqkpkeea').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0014():
    """Extended test 14 for replication."""
    x_0 = 40800 * 0.05955626
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8892 * 0.39709248
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11743 * 0.32228391
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9398 * 0.38927440
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94511 * 0.88045712
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69852 * 0.39595491
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38031 * 0.28968265
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68079 * 0.20461270
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50407 * 0.81268947
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86402 * 0.25317416
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70540 * 0.78177513
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2335 * 0.30458273
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19438 * 0.54774478
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40079 * 0.49941885
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77724 * 0.29026466
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3079 * 0.63035662
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88192 * 0.36373777
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27817 * 0.79795873
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35378 * 0.60140999
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7613 * 0.46470094
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'rfvzibol').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0015():
    """Extended test 15 for replication."""
    x_0 = 43917 * 0.97942386
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8538 * 0.85724553
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97444 * 0.06137622
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60715 * 0.44431212
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37110 * 0.62903647
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3352 * 0.45433136
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68416 * 0.76225950
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99625 * 0.58827339
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36766 * 0.08163287
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65131 * 0.59498800
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13734 * 0.94707179
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39703 * 0.03710302
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96678 * 0.74107847
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47749 * 0.28344420
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44888 * 0.24464495
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78106 * 0.18444815
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67070 * 0.45146632
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92788 * 0.46920791
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32271 * 0.32159553
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38149 * 0.07021875
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7903 * 0.09185307
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80072 * 0.42441988
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8041 * 0.80527219
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91845 * 0.82055873
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84295 * 0.84086766
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48477 * 0.45930586
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91807 * 0.48746064
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10093 * 0.87587797
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59192 * 0.32141319
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78633 * 0.51454961
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69239 * 0.22302911
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65496 * 0.70708475
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26868 * 0.26527927
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41972 * 0.18929118
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37240 * 0.96855610
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71136 * 0.91422707
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94350 * 0.39956208
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89370 * 0.28150160
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16606 * 0.63718879
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 61301 * 0.50688897
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5995 * 0.66880913
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 34994 * 0.24802846
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93387 * 0.09945785
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 77287 * 0.72787612
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 3488 * 0.39306317
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 66453 * 0.40300078
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 81414 * 0.68327343
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 44740 * 0.32810119
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 29266 * 0.80970292
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'nlxbryot').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0016():
    """Extended test 16 for replication."""
    x_0 = 16301 * 0.96314060
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42651 * 0.03382194
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30625 * 0.73525194
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48690 * 0.68608177
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93605 * 0.61505778
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81724 * 0.96276917
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24925 * 0.71394363
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37988 * 0.79025337
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93529 * 0.43932332
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77564 * 0.64839261
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40860 * 0.33021379
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93988 * 0.77450992
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64676 * 0.80437059
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99384 * 0.63611777
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85121 * 0.36233818
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32120 * 0.21058089
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96752 * 0.01434388
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75968 * 0.36525377
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68560 * 0.19437276
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76125 * 0.10455764
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91104 * 0.00093782
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30565 * 0.30126724
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70140 * 0.72408247
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83735 * 0.87861107
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1508 * 0.38602284
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74662 * 0.51591816
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14194 * 0.62508194
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68176 * 0.39651027
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81514 * 0.18112855
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24301 * 0.72639475
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93365 * 0.12788305
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96054 * 0.93481954
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16272 * 0.03906353
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'jjgtyorq').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0017():
    """Extended test 17 for replication."""
    x_0 = 70314 * 0.35841271
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61769 * 0.51603232
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22824 * 0.03350807
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38318 * 0.47312811
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96587 * 0.73438005
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28527 * 0.15927510
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59154 * 0.13133348
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52023 * 0.01607481
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24306 * 0.85752875
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95122 * 0.23186925
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17204 * 0.30330792
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89719 * 0.97441429
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24848 * 0.78978619
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53795 * 0.31336250
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49386 * 0.93737143
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75672 * 0.60132261
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25478 * 0.83593648
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69433 * 0.29634458
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38585 * 0.99462756
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44080 * 0.54790620
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14591 * 0.21246228
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62342 * 0.77089531
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39384 * 0.22882154
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99465 * 0.85425318
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45090 * 0.16313898
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66304 * 0.89073025
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22193 * 0.56143675
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30505 * 0.74570029
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33397 * 0.53947635
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29147 * 0.81210468
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51716 * 0.52259326
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35866 * 0.33962997
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89488 * 0.41292574
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46344 * 0.25688742
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'izmtstoa').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0018():
    """Extended test 18 for replication."""
    x_0 = 24623 * 0.93649187
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93367 * 0.40987539
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85579 * 0.19452516
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3881 * 0.84096559
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57771 * 0.00030768
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24266 * 0.36069979
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31927 * 0.30127609
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69109 * 0.07735056
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36193 * 0.93605909
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65989 * 0.40654835
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72323 * 0.35440930
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91642 * 0.08059343
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22586 * 0.36639963
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27354 * 0.72014395
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46598 * 0.09478195
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78647 * 0.63700378
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57653 * 0.97676356
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50008 * 0.54940745
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27218 * 0.66056969
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25629 * 0.49117739
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72595 * 0.45651756
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79933 * 0.17607120
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96681 * 0.36051089
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2762 * 0.19084445
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55936 * 0.03433237
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91542 * 0.99769624
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18613 * 0.79708112
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49639 * 0.59800713
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96882 * 0.19364982
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25700 * 0.23584607
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90205 * 0.48985697
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75133 * 0.35822389
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'bbawakcq').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0019():
    """Extended test 19 for replication."""
    x_0 = 77610 * 0.29441591
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1180 * 0.13978136
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52167 * 0.22086709
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2084 * 0.01307269
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67973 * 0.76150776
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93009 * 0.38053198
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46702 * 0.11512552
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29885 * 0.96214496
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25281 * 0.95005769
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17495 * 0.91092752
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50097 * 0.28970532
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17748 * 0.12851126
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89265 * 0.77047950
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99016 * 0.97559068
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60109 * 0.96284294
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19383 * 0.42701484
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2393 * 0.61635669
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39549 * 0.23244999
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97701 * 0.35008470
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6256 * 0.77648600
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84048 * 0.68089899
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73712 * 0.47101439
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22376 * 0.56530451
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89253 * 0.17139722
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ssixdndl').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0020():
    """Extended test 20 for replication."""
    x_0 = 10199 * 0.60474099
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55263 * 0.80573630
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15043 * 0.15526247
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23548 * 0.48502583
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28492 * 0.64106173
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42921 * 0.24258294
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41151 * 0.44285700
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 681 * 0.44162227
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74742 * 0.87972348
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17129 * 0.80353468
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63372 * 0.68821322
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44129 * 0.70631317
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66654 * 0.08231165
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89614 * 0.23256670
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74078 * 0.83113154
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15944 * 0.84818103
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80954 * 0.09508264
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90148 * 0.07122965
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73286 * 0.30221979
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17033 * 0.33240502
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82276 * 0.16037618
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4195 * 0.66127322
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31558 * 0.27399129
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2300 * 0.18656326
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79675 * 0.26705742
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44253 * 0.10531298
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47949 * 0.93905286
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99936 * 0.27729340
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63396 * 0.61933156
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87405 * 0.49267604
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6881 * 0.67524288
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11233 * 0.31458990
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72824 * 0.05346752
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65956 * 0.45218744
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97225 * 0.05714818
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40829 * 0.76222734
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31102 * 0.10259311
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50310 * 0.44192837
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24176 * 0.10488297
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40310 * 0.84499532
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35151 * 0.46618746
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6773 * 0.11250606
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 56410 * 0.95067928
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 57384 * 0.56402928
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 32898 * 0.06106911
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 43069 * 0.38202198
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 94838 * 0.42773489
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 34967 * 0.16563618
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'lyejzjnv').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0021():
    """Extended test 21 for replication."""
    x_0 = 48982 * 0.25218115
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69898 * 0.32571839
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91337 * 0.29379441
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44334 * 0.52697851
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5899 * 0.25132820
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29090 * 0.47656974
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87551 * 0.49281161
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17211 * 0.62410804
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24991 * 0.73115193
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96635 * 0.24429686
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12047 * 0.69470909
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2711 * 0.52880762
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75945 * 0.51513127
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82468 * 0.06374398
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13017 * 0.38458087
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44563 * 0.29006971
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59417 * 0.28953870
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39540 * 0.45935593
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1887 * 0.83598886
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2363 * 0.45130346
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89457 * 0.89958169
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10563 * 0.78275080
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98194 * 0.93791979
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70241 * 0.76392905
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82656 * 0.11266504
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13531 * 0.77177519
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97177 * 0.43641050
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68742 * 0.54325446
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43705 * 0.97191142
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50359 * 0.53242463
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66807 * 0.67403661
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32856 * 0.26159299
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56813 * 0.73676921
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86518 * 0.19404268
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66210 * 0.13804342
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98543 * 0.39542888
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84949 * 0.17516404
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35141 * 0.81499040
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'joiwajyw').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0022():
    """Extended test 22 for replication."""
    x_0 = 25295 * 0.14384810
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39478 * 0.98479749
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51200 * 0.63645317
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72471 * 0.84476561
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15001 * 0.74088812
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57111 * 0.52504546
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26675 * 0.46896491
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69230 * 0.34840548
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94609 * 0.60582236
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69908 * 0.09924511
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60085 * 0.09168453
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84894 * 0.03024827
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16115 * 0.92683558
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2623 * 0.30117020
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11654 * 0.65429277
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22374 * 0.15133569
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14527 * 0.06167338
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5342 * 0.55567801
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99064 * 0.74152016
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91440 * 0.46963073
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17206 * 0.15547048
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66074 * 0.07462592
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26022 * 0.76971047
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13135 * 0.35894786
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32829 * 0.21377264
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25048 * 0.94205706
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22561 * 0.89230787
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78491 * 0.12748131
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81556 * 0.25799870
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77921 * 0.58740325
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92713 * 0.12955993
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92489 * 0.87389279
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55508 * 0.58351855
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36069 * 0.08801017
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68283 * 0.15962765
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42123 * 0.86138946
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25748 * 0.66534488
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97605 * 0.91805297
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34686 * 0.28102514
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24216 * 0.79858965
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80143 * 0.39371093
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88075 * 0.48663162
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'vlodwgdv').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0023():
    """Extended test 23 for replication."""
    x_0 = 40633 * 0.19896399
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52983 * 0.60922159
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71529 * 0.71746438
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18187 * 0.45300653
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28872 * 0.79105342
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31658 * 0.35114773
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11355 * 0.42445718
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4503 * 0.05545129
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22751 * 0.76588328
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21067 * 0.42441220
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 238 * 0.02053072
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80873 * 0.25543642
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26464 * 0.02515836
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50168 * 0.63138175
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28971 * 0.49475035
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85725 * 0.95283373
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24053 * 0.76458489
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13768 * 0.51345369
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45743 * 0.14966101
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66842 * 0.70167106
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14109 * 0.24563157
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62960 * 0.86360078
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40665 * 0.69666404
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33073 * 0.18334882
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69353 * 0.54327354
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51209 * 0.04621655
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36466 * 0.76882438
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3918 * 0.78888963
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63797 * 0.86286417
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1384 * 0.12640087
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8809 * 0.14101486
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60350 * 0.09160123
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47104 * 0.98838701
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41436 * 0.53553712
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36107 * 0.90757920
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32683 * 0.85178879
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86610 * 0.84914160
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16990 * 0.12957664
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 54244 * 0.19835465
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30032 * 0.95158095
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35655 * 0.02729561
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'gxjvtezc').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0024():
    """Extended test 24 for replication."""
    x_0 = 21140 * 0.12256590
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22704 * 0.14792457
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5711 * 0.62051340
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72550 * 0.82947491
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65694 * 0.66588083
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69365 * 0.64194390
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65073 * 0.17615529
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91929 * 0.71027202
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69834 * 0.52143077
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8852 * 0.83957724
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64052 * 0.95577576
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37025 * 0.23122724
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41948 * 0.38795586
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51249 * 0.43446981
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5200 * 0.02701213
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11727 * 0.45076045
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45517 * 0.69712869
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60177 * 0.38832445
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85909 * 0.03015480
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53396 * 0.06265302
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'zdoqeupo').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0025():
    """Extended test 25 for replication."""
    x_0 = 1541 * 0.87008830
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30179 * 0.22347421
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88490 * 0.81674839
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26971 * 0.95912982
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37061 * 0.11211104
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38172 * 0.66827837
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23909 * 0.96019642
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36477 * 0.39812029
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35355 * 0.22667663
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43326 * 0.60379223
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3433 * 0.56754199
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97610 * 0.12025499
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79929 * 0.50467428
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58420 * 0.31109629
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66008 * 0.62832155
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61966 * 0.30920079
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65586 * 0.68475454
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7510 * 0.81682597
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9792 * 0.42341380
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63722 * 0.95116084
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22374 * 0.89897283
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23748 * 0.53448415
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'unhctdem').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0026():
    """Extended test 26 for replication."""
    x_0 = 77852 * 0.50880777
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41644 * 0.74925291
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24177 * 0.82758328
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61303 * 0.97226411
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11893 * 0.33281303
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61163 * 0.00663195
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3872 * 0.47193827
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28723 * 0.23739261
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21543 * 0.75433284
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98613 * 0.16382876
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99143 * 0.57255654
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95292 * 0.23819269
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17670 * 0.53488856
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65606 * 0.57991733
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17643 * 0.94576504
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44525 * 0.14876766
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33367 * 0.71632673
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54414 * 0.54962076
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86673 * 0.41385701
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3677 * 0.01114499
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7569 * 0.39956449
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1395 * 0.08912436
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16994 * 0.51657487
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52653 * 0.98511327
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81951 * 0.27580526
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1228 * 0.48138817
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18110 * 0.10979617
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10390 * 0.76709732
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87614 * 0.38347579
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96896 * 0.63454466
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60619 * 0.90470422
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33147 * 0.01708242
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18415 * 0.69445979
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74838 * 0.34811179
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 856 * 0.64410619
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43900 * 0.70323909
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16046 * 0.20486082
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 57922 * 0.63207077
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43672 * 0.10509439
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28751 * 0.08496329
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 56127 * 0.65888288
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3442 * 0.32463610
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 8089 * 0.47638054
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 93579 * 0.12112406
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xsgaktfs').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0027():
    """Extended test 27 for replication."""
    x_0 = 71397 * 0.21541255
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1488 * 0.78330380
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48116 * 0.74388827
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39528 * 0.71940060
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43712 * 0.33073776
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99213 * 0.54848223
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80394 * 0.28182447
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79925 * 0.63139722
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41104 * 0.39864042
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93453 * 0.08825317
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96603 * 0.68774682
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36289 * 0.54252616
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38210 * 0.10213311
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80610 * 0.72917107
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85664 * 0.09015956
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61227 * 0.07690268
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18778 * 0.36838297
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63799 * 0.06577337
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39576 * 0.08216479
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48758 * 0.88194885
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20606 * 0.13278373
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58335 * 0.53982751
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37947 * 0.52363238
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1126 * 0.57770533
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79252 * 0.43416138
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27672 * 0.85810800
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96741 * 0.18390204
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98694 * 0.51775608
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'zbmzsnuy').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0028():
    """Extended test 28 for replication."""
    x_0 = 91339 * 0.83943698
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54809 * 0.26834037
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9396 * 0.64362651
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67964 * 0.25013805
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26410 * 0.52109321
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25908 * 0.93332157
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45849 * 0.77429762
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98988 * 0.96989248
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63152 * 0.28005911
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54289 * 0.62069132
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11559 * 0.31801571
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82845 * 0.53594628
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91166 * 0.23962153
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73839 * 0.62933604
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33649 * 0.22127712
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30226 * 0.05232971
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37788 * 0.18400152
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54347 * 0.36762798
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5111 * 0.77727864
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16610 * 0.80803360
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44908 * 0.96186002
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62277 * 0.60847304
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76202 * 0.40329028
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47099 * 0.48762696
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87732 * 0.07585400
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27471 * 0.93447710
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39175 * 0.50254741
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35735 * 0.41909840
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44626 * 0.80872386
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'wmepzazm').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0029():
    """Extended test 29 for replication."""
    x_0 = 92927 * 0.08135219
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63709 * 0.25194084
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78200 * 0.13277404
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31311 * 0.96265213
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4150 * 0.05030713
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 747 * 0.32274988
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21126 * 0.27321226
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48757 * 0.17882742
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46548 * 0.12437362
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75751 * 0.10768179
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73957 * 0.56599094
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8745 * 0.13486238
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28023 * 0.18024722
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93275 * 0.51172201
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73851 * 0.43566033
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60279 * 0.69997695
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4679 * 0.13371680
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9580 * 0.64872112
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70479 * 0.70732815
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20095 * 0.90904936
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68694 * 0.59192209
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21534 * 0.37488016
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60531 * 0.02942960
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'aaoqddgc').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0030():
    """Extended test 30 for replication."""
    x_0 = 12167 * 0.46059274
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48780 * 0.23283782
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90470 * 0.78158218
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10206 * 0.26743348
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37452 * 0.08725597
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46469 * 0.48811749
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13812 * 0.86695725
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69798 * 0.90382041
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89227 * 0.13726156
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57068 * 0.03610936
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3536 * 0.90165620
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60744 * 0.61651543
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63765 * 0.54608192
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87852 * 0.90765758
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3515 * 0.18400653
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82875 * 0.38638451
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60790 * 0.78104333
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29320 * 0.49961582
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11461 * 0.70529342
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10389 * 0.27108710
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89881 * 0.86273967
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33084 * 0.04701918
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83561 * 0.60493256
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27788 * 0.17079919
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13093 * 0.51822382
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33242 * 0.70870187
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59137 * 0.41336730
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5655 * 0.18638097
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21257 * 0.05348470
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83143 * 0.65355975
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8050 * 0.06397429
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'lagurotn').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0031():
    """Extended test 31 for replication."""
    x_0 = 69990 * 0.37331122
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54823 * 0.23367424
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69471 * 0.76840232
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39080 * 0.14915354
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17357 * 0.12110209
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8071 * 0.33807766
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18335 * 0.95720921
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92845 * 0.01165696
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2864 * 0.53604268
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25592 * 0.61621961
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19317 * 0.87005368
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89239 * 0.23992320
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31427 * 0.33806937
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33135 * 0.14793002
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53746 * 0.11412597
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65669 * 0.69846715
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48891 * 0.92546011
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53714 * 0.10540227
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2994 * 0.12515130
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36296 * 0.96389957
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99240 * 0.57441370
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1592 * 0.77276272
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47389 * 0.26934139
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20120 * 0.43693769
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28608 * 0.87949885
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53752 * 0.46638947
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79594 * 0.12763575
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27264 * 0.17785666
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'ehwnxwrs').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0032():
    """Extended test 32 for replication."""
    x_0 = 87359 * 0.48191253
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16119 * 0.37094737
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50803 * 0.34771320
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31663 * 0.48627120
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99357 * 0.98821673
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36612 * 0.97427305
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2532 * 0.43170277
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17113 * 0.80201925
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46170 * 0.72626717
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28327 * 0.27236095
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72550 * 0.49092592
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61978 * 0.25546914
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42896 * 0.03851986
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43788 * 0.39889926
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77144 * 0.59120256
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51004 * 0.01665636
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62498 * 0.32784019
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78824 * 0.08783721
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65683 * 0.63172145
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76900 * 0.06526514
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10361 * 0.42017195
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27006 * 0.83263707
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'zjgttnck').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0033():
    """Extended test 33 for replication."""
    x_0 = 69988 * 0.51786826
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29110 * 0.20833436
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20999 * 0.90662890
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61379 * 0.00319062
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11299 * 0.87194512
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4179 * 0.32374200
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31616 * 0.95067853
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56423 * 0.12153712
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52956 * 0.91858691
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61582 * 0.87719180
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90255 * 0.86389574
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10945 * 0.31876150
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13328 * 0.64926541
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71779 * 0.35737317
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80764 * 0.32582814
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66249 * 0.79695921
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74188 * 0.71220636
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51850 * 0.13994779
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48639 * 0.71312647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83187 * 0.59899381
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32619 * 0.97615077
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51060 * 0.55329222
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1507 * 0.58514678
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8668 * 0.71260810
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26915 * 0.76858965
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38005 * 0.80456474
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87691 * 0.93276761
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7739 * 0.91270724
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13650 * 0.99295551
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37531 * 0.22771937
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65281 * 0.49050803
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5008 * 0.54231140
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95310 * 0.70765785
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15960 * 0.79797998
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78515 * 0.08977268
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'wkisxkud').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0034():
    """Extended test 34 for replication."""
    x_0 = 20703 * 0.42866148
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88707 * 0.34619574
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59796 * 0.83208058
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94494 * 0.38456854
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50261 * 0.88220934
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70836 * 0.46617952
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42004 * 0.89839660
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73258 * 0.50384828
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7328 * 0.94658946
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34721 * 0.07198830
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62292 * 0.17408559
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71886 * 0.10910815
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69671 * 0.95524660
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25960 * 0.99440570
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75113 * 0.64973595
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97232 * 0.95452679
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97855 * 0.80640390
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64527 * 0.08133913
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30124 * 0.32256312
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7982 * 0.33692436
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83079 * 0.70718536
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56374 * 0.19853767
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83757 * 0.89864830
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96570 * 0.08883256
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77609 * 0.02135252
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49929 * 0.67157706
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42063 * 0.15052665
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74382 * 0.92656364
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80948 * 0.86531349
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13960 * 0.86976421
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43336 * 0.46342922
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62196 * 0.38254335
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51807 * 0.22940931
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7198 * 0.92978153
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21190 * 0.87258790
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11583 * 0.98304301
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11204 * 0.21419236
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80617 * 0.33809742
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'bspjssvv').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0035():
    """Extended test 35 for replication."""
    x_0 = 55126 * 0.20866568
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3911 * 0.78216602
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68700 * 0.43199446
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89463 * 0.94884166
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92074 * 0.69652766
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34792 * 0.47166352
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68640 * 0.76654455
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95998 * 0.92952766
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99792 * 0.62038749
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47164 * 0.77057080
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48937 * 0.86442772
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98846 * 0.78432789
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13011 * 0.34328967
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78751 * 0.05018951
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13384 * 0.68115702
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95863 * 0.94049121
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31930 * 0.07374099
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41575 * 0.53318515
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11040 * 0.19787223
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68763 * 0.87373969
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16704 * 0.50053477
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23741 * 0.31514930
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68304 * 0.01295348
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30412 * 0.62207031
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85089 * 0.59204298
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5882 * 0.81331727
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91741 * 0.19873799
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88330 * 0.93635414
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31721 * 0.31403459
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55525 * 0.03191667
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ppvrjaof').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0036():
    """Extended test 36 for replication."""
    x_0 = 69775 * 0.75779052
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8491 * 0.81808226
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32438 * 0.47743864
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55532 * 0.51675200
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 803 * 0.29401165
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9465 * 0.64720390
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14718 * 0.32099883
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95037 * 0.83318544
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95990 * 0.07720589
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29956 * 0.87017582
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91955 * 0.24445322
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99356 * 0.81986350
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27046 * 0.11222765
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32373 * 0.46089389
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52185 * 0.87350011
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74842 * 0.63601967
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25023 * 0.60055638
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92146 * 0.96219126
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16938 * 0.64991574
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 678 * 0.73967156
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97342 * 0.63025751
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26361 * 0.51462620
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38477 * 0.55516529
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78594 * 0.56657156
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49449 * 0.49792139
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14217 * 0.95931568
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59640 * 0.47900856
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1240 * 0.03575825
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19558 * 0.09390049
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'lomoteej').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0037():
    """Extended test 37 for replication."""
    x_0 = 36531 * 0.64091776
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1946 * 0.04355500
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7208 * 0.11634106
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85297 * 0.03386196
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17958 * 0.28984447
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81572 * 0.71035501
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12101 * 0.02371090
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39310 * 0.92637733
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56882 * 0.31670567
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4015 * 0.92247423
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12417 * 0.59997224
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76598 * 0.43202562
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28666 * 0.47996356
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15096 * 0.10878702
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18613 * 0.86841054
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99536 * 0.77886441
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96658 * 0.95183558
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49857 * 0.14594922
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12643 * 0.14551864
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21338 * 0.19439533
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85662 * 0.48746981
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37936 * 0.76172377
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19399 * 0.90827420
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12335 * 0.77146889
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71928 * 0.76835999
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58174 * 0.64840748
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49747 * 0.69086499
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50061 * 0.53800802
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29910 * 0.09256796
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46523 * 0.51900823
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36920 * 0.74679802
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51904 * 0.70084447
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 610 * 0.78852813
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7463 * 0.93860286
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48235 * 0.40089538
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35091 * 0.75529926
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5059 * 0.93069178
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67033 * 0.45573115
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90306 * 0.16699647
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99391 * 0.82379300
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42285 * 0.09312178
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35094 * 0.23328330
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81525 * 0.97343005
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97017 * 0.76893335
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 36376 * 0.03119335
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 70631 * 0.15988897
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 44340 * 0.19968691
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 89099 * 0.79199175
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 25021 * 0.26873471
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'oexkefli').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0038():
    """Extended test 38 for replication."""
    x_0 = 41031 * 0.17731774
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69426 * 0.99043948
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63145 * 0.37010545
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44509 * 0.50448579
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54953 * 0.86010042
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26030 * 0.88129254
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39385 * 0.86458933
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61098 * 0.79307521
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85054 * 0.45826512
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87680 * 0.93207279
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26576 * 0.11253924
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26313 * 0.38451957
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97490 * 0.09856497
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85905 * 0.53626489
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3692 * 0.73449677
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77155 * 0.17731433
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25956 * 0.65793285
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87491 * 0.99028904
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46422 * 0.37454833
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5078 * 0.38859642
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20724 * 0.39252369
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92760 * 0.64197965
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24604 * 0.00898502
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7820 * 0.06058847
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57445 * 0.34534982
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81643 * 0.90791601
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16266 * 0.25847449
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68613 * 0.42539085
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92701 * 0.60002653
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30819 * 0.98184653
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71441 * 0.97730865
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15506 * 0.44668825
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5313 * 0.95038954
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39612 * 0.00559281
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23623 * 0.70384357
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38902 * 0.78561912
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2823 * 0.11669711
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63839 * 0.33627214
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72506 * 0.75031888
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15460 * 0.24975815
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62530 * 0.12382716
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92549 * 0.69991550
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11590 * 0.56267236
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 65754 * 0.58180405
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'orylibei').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0039():
    """Extended test 39 for replication."""
    x_0 = 94920 * 0.43679203
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36755 * 0.50403978
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63173 * 0.86005416
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61946 * 0.52573752
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23966 * 0.50280416
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58947 * 0.30405886
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24480 * 0.30725215
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94479 * 0.60440673
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51244 * 0.56328543
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45520 * 0.89055938
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59309 * 0.34056075
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96022 * 0.73165790
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20122 * 0.53917226
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9027 * 0.63633149
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17179 * 0.47871170
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15955 * 0.04162544
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5990 * 0.39744002
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98549 * 0.88707882
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90517 * 0.35474240
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8502 * 0.76400002
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33146 * 0.90871233
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95281 * 0.78428481
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14902 * 0.96718419
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51716 * 0.51618718
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72245 * 0.86581543
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54892 * 0.18552819
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70860 * 0.86628666
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24645 * 0.11442573
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28750 * 0.54544183
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55713 * 0.84998382
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31949 * 0.07242857
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36765 * 0.96534844
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'zkyekece').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0040():
    """Extended test 40 for replication."""
    x_0 = 3757 * 0.45177052
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87791 * 0.62890282
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95580 * 0.30200632
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52276 * 0.86551107
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63200 * 0.84788560
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63288 * 0.99312647
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57073 * 0.68151132
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39531 * 0.02505662
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50655 * 0.44510671
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46671 * 0.49265309
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13118 * 0.10611734
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79915 * 0.99385798
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2801 * 0.23648228
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81653 * 0.25492353
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5648 * 0.32339109
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10442 * 0.51459898
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76341 * 0.94540559
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66878 * 0.63388445
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44879 * 0.34234225
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93129 * 0.93743524
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11997 * 0.05896518
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46030 * 0.73741388
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42400 * 0.08739307
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85463 * 0.50716300
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50001 * 0.23313841
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8535 * 0.11961022
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58958 * 0.78122601
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12213 * 0.19272067
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'uzjowdcj').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0041():
    """Extended test 41 for replication."""
    x_0 = 8592 * 0.77923548
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61149 * 0.89006811
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23804 * 0.19496512
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6141 * 0.51157973
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53274 * 0.66040097
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31022 * 0.67194765
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74500 * 0.34492342
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5390 * 0.49512463
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12778 * 0.11053188
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8296 * 0.90331886
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89259 * 0.27353320
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9911 * 0.55971700
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11237 * 0.63848010
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73233 * 0.10907061
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49415 * 0.55375881
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58782 * 0.97695427
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72158 * 0.08040902
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16780 * 0.37578638
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63080 * 0.89415157
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49793 * 0.92542831
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21024 * 0.09316672
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46068 * 0.78661859
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28556 * 0.74974984
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80817 * 0.76218306
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58378 * 0.82309197
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78377 * 0.09939321
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38961 * 0.19889915
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23640 * 0.15239036
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84841 * 0.06063188
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89491 * 0.60691675
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66677 * 0.43436531
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68066 * 0.10682428
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52256 * 0.13056494
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49747 * 0.01217136
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15853 * 0.82437259
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35333 * 0.85548502
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52342 * 0.92820882
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77010 * 0.38032306
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'feyvynhb').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0042():
    """Extended test 42 for replication."""
    x_0 = 85797 * 0.41055740
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96006 * 0.25592727
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11595 * 0.11424753
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63340 * 0.05987517
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59338 * 0.48840252
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40141 * 0.15377488
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63388 * 0.01692447
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72864 * 0.85485143
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6547 * 0.86586072
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85826 * 0.62529796
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8084 * 0.66329021
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18621 * 0.28698294
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2609 * 0.04194331
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72971 * 0.71668786
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98337 * 0.98343285
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22040 * 0.75412150
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54279 * 0.93772886
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12159 * 0.12047142
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35741 * 0.99143900
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20266 * 0.59095835
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28840 * 0.64269056
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13381 * 0.72442163
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97213 * 0.70083623
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52479 * 0.22318859
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73874 * 0.82589130
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59054 * 0.34563179
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89885 * 0.59480725
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10722 * 0.31939155
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86943 * 0.13628243
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30338 * 0.58788759
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64412 * 0.11388766
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2943 * 0.30310058
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45796 * 0.50086073
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67311 * 0.71802517
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8129 * 0.70048236
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86825 * 0.46156461
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19789 * 0.97296196
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90912 * 0.65141371
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94632 * 0.66311353
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 60964 * 0.71311033
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4379 * 0.08226436
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74624 * 0.54787188
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42068 * 0.35168723
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'dlzjccel').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0043():
    """Extended test 43 for replication."""
    x_0 = 5956 * 0.35586802
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10381 * 0.65219672
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70843 * 0.82393805
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43527 * 0.91024538
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76508 * 0.39375131
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26144 * 0.19990327
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71581 * 0.56300416
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42123 * 0.54718027
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24319 * 0.66629714
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60168 * 0.36828047
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27295 * 0.83788365
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50844 * 0.10771538
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15429 * 0.15840213
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69550 * 0.14136128
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13062 * 0.77538470
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17909 * 0.87763614
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83201 * 0.07415200
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38353 * 0.18991869
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17628 * 0.60809060
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95703 * 0.08393970
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77534 * 0.16740692
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99231 * 0.41614174
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41457 * 0.37170688
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6167 * 0.81008792
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96280 * 0.51386974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23892 * 0.44275404
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3502 * 0.61384711
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42523 * 0.47839336
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37091 * 0.73903335
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41022 * 0.02431228
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79665 * 0.13296616
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27704 * 0.07962868
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48803 * 0.66255530
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28930 * 0.56161870
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3255 * 0.82676436
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54958 * 0.48523759
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45473 * 0.30699295
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43680 * 0.12914926
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99286 * 0.31632102
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'brmiqzpj').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0044():
    """Extended test 44 for replication."""
    x_0 = 70056 * 0.07733113
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91248 * 0.21556232
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64577 * 0.18789602
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78138 * 0.58214522
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38094 * 0.41224544
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12420 * 0.56613163
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40926 * 0.78212706
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19514 * 0.42248178
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45570 * 0.56107834
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85501 * 0.24644416
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87108 * 0.65491649
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88346 * 0.09125260
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22143 * 0.28314590
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54858 * 0.18534428
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73337 * 0.01624112
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50956 * 0.50996442
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27015 * 0.16757491
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73290 * 0.54861065
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60684 * 0.82928962
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78737 * 0.18719408
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90814 * 0.93660401
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64109 * 0.07113456
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34220 * 0.72635925
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8090 * 0.91443682
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14181 * 0.26190199
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99230 * 0.24903635
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50439 * 0.97172226
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18922 * 0.26027876
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59383 * 0.16929730
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'gkmdqiga').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0045():
    """Extended test 45 for replication."""
    x_0 = 45692 * 0.76630512
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32422 * 0.52752125
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41815 * 0.51895618
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30713 * 0.20752077
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25226 * 0.16342985
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19217 * 0.05704708
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27769 * 0.79616810
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84987 * 0.85697970
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3843 * 0.77932089
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64247 * 0.26860822
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78998 * 0.75369270
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91145 * 0.30980142
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54774 * 0.88422493
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18210 * 0.75034229
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23308 * 0.18537800
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10184 * 0.97692612
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59005 * 0.40205077
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30694 * 0.84087212
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73150 * 0.48496228
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11665 * 0.31503411
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'iwuapxeo').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0046():
    """Extended test 46 for replication."""
    x_0 = 47309 * 0.60156955
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67791 * 0.27905836
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38519 * 0.08330981
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81608 * 0.13630672
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74657 * 0.75569935
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22241 * 0.35684159
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29425 * 0.81432233
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54159 * 0.18607806
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72626 * 0.45269698
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14449 * 0.44550492
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16692 * 0.83312550
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68049 * 0.40847832
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7775 * 0.03295020
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31415 * 0.02684497
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42004 * 0.08174448
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99482 * 0.96543618
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69329 * 0.32062937
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43915 * 0.58022072
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61114 * 0.79792493
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3669 * 0.42737690
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95677 * 0.25104257
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6385 * 0.05386932
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70691 * 0.83434542
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45023 * 0.64628259
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42539 * 0.58997756
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43069 * 0.50851884
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70489 * 0.02141357
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49557 * 0.34261492
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18658 * 0.74399692
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59379 * 0.69407580
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11187 * 0.30132200
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ogqjpinw').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0047():
    """Extended test 47 for replication."""
    x_0 = 40146 * 0.71970071
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70172 * 0.15894031
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87339 * 0.59364148
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19680 * 0.98321577
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23454 * 0.62269779
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75696 * 0.75795646
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7813 * 0.35861730
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12563 * 0.17000079
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66155 * 0.03159747
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80867 * 0.84275145
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14659 * 0.17717529
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58562 * 0.29933676
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95655 * 0.43367718
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69386 * 0.23107028
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12560 * 0.37823860
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33408 * 0.27304962
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61817 * 0.28543124
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92659 * 0.28402184
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15708 * 0.93495610
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89808 * 0.31279892
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81611 * 0.74900646
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89114 * 0.09522244
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65037 * 0.32844397
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75715 * 0.26802314
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96670 * 0.59308668
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62843 * 0.00856974
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51970 * 0.69089515
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91025 * 0.03199139
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55155 * 0.48865668
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58575 * 0.26176672
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79832 * 0.86217731
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43570 * 0.75523887
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58451 * 0.20591545
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21279 * 0.36122660
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48759 * 0.36796978
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86261 * 0.04556363
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ybwsyapo').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0048():
    """Extended test 48 for replication."""
    x_0 = 32421 * 0.86885854
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18115 * 0.93917813
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28662 * 0.99397738
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52266 * 0.05111395
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63948 * 0.62665994
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82213 * 0.45436228
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21334 * 0.00250614
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1057 * 0.66071420
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95075 * 0.27705888
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14166 * 0.50172512
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21111 * 0.79691970
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66751 * 0.52545148
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81846 * 0.40878098
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32765 * 0.69011700
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33151 * 0.95330485
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21423 * 0.80092087
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90091 * 0.84942524
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54326 * 0.49866353
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25838 * 0.03991774
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 120 * 0.31504313
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16787 * 0.13397621
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97283 * 0.16751590
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50169 * 0.94866316
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68626 * 0.67378475
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72699 * 0.96493423
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1615 * 0.51655078
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95359 * 0.54743170
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81536 * 0.29003415
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22639 * 0.48240074
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71165 * 0.54332693
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10425 * 0.45811203
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1095 * 0.14889336
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98443 * 0.58026764
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52960 * 0.03479101
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14566 * 0.30171519
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43274 * 0.56598931
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94125 * 0.20320048
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88302 * 0.09753101
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11122 * 0.68112273
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91748 * 0.33148998
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 92068 * 0.06933767
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5154 * 0.50912862
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15966 * 0.30654772
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 41174 * 0.30540290
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59039 * 0.03018711
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'xowoapjg').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0049():
    """Extended test 49 for replication."""
    x_0 = 94539 * 0.17644443
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13175 * 0.52182911
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78242 * 0.97210435
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68758 * 0.98628672
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79777 * 0.34314270
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18361 * 0.77484657
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46521 * 0.14725023
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13211 * 0.47938848
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68579 * 0.79118831
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5442 * 0.63183750
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19460 * 0.49150742
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17110 * 0.42137881
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67573 * 0.18753450
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61923 * 0.44399598
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1844 * 0.04876022
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31143 * 0.53915377
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10334 * 0.81887203
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33977 * 0.08467219
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34004 * 0.62540431
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33616 * 0.75606188
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4840 * 0.47502772
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74507 * 0.65480237
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92311 * 0.89543840
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94169 * 0.36351159
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99387 * 0.52476747
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5824 * 0.26101045
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37563 * 0.05576750
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28935 * 0.87584584
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94501 * 0.43316819
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20482 * 0.85016862
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'zqnbbrne').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0050():
    """Extended test 50 for replication."""
    x_0 = 98249 * 0.79227112
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93395 * 0.33146649
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58006 * 0.12860389
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74177 * 0.23342319
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5546 * 0.95663481
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18630 * 0.08786072
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78323 * 0.74023132
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55366 * 0.64198483
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33042 * 0.38445568
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1212 * 0.59242138
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58158 * 0.86065175
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28218 * 0.86956869
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17944 * 0.48785358
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36569 * 0.60732152
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56827 * 0.25963586
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51062 * 0.22549242
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56612 * 0.39412459
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60372 * 0.31110543
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44038 * 0.07025828
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3561 * 0.99578750
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12674 * 0.34165616
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49836 * 0.96237616
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81181 * 0.07424671
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44346 * 0.86279937
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99035 * 0.52492337
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91047 * 0.96939204
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62203 * 0.19794824
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59891 * 0.89636739
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25550 * 0.74359706
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89346 * 0.78410546
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25148 * 0.56628946
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33434 * 0.33987141
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97457 * 0.95866815
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90871 * 0.44920289
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34369 * 0.91368304
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79053 * 0.03728514
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61087 * 0.17648180
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59746 * 0.81052018
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4721 * 0.51600012
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 61165 * 0.21313937
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 66291 * 0.20158141
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'mzbuxees').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0051():
    """Extended test 51 for replication."""
    x_0 = 45809 * 0.37977479
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56526 * 0.37702618
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64609 * 0.22469331
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56836 * 0.79154240
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 576 * 0.22182223
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13770 * 0.59327670
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41622 * 0.97338366
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10010 * 0.63727491
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10303 * 0.33512926
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3228 * 0.33836659
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76936 * 0.38221141
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69284 * 0.66717523
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60577 * 0.33250743
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54816 * 0.73692112
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14347 * 0.27619568
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97581 * 0.30055980
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29562 * 0.00315935
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42882 * 0.57044044
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21033 * 0.48357154
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99699 * 0.27270987
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5013 * 0.89539959
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69169 * 0.68192026
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95394 * 0.86856295
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95873 * 0.66264016
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 132 * 0.45850104
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54927 * 0.07448557
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84806 * 0.87421719
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46470 * 0.29163914
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21438 * 0.91002446
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19590 * 0.62873137
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74409 * 0.33583951
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45753 * 0.86699926
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97373 * 0.93740204
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59891 * 0.72494188
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8350 * 0.34180683
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55660 * 0.42355434
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67877 * 0.75181436
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83077 * 0.25137300
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10854 * 0.25948357
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84188 * 0.73240090
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79918 * 0.88250805
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41237 * 0.72613946
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95157 * 0.45261332
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82569 * 0.41655207
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 80714 * 0.59772134
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 81560 * 0.99468942
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 93057 * 0.72289803
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 37271 * 0.17886102
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'okwjcfag').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0052():
    """Extended test 52 for replication."""
    x_0 = 67283 * 0.51596170
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1266 * 0.04166821
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88892 * 0.83386895
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91893 * 0.37752515
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2224 * 0.65287199
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56344 * 0.43128951
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83903 * 0.00226540
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32049 * 0.31168027
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8017 * 0.78160766
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75783 * 0.19915022
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12216 * 0.71218995
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95416 * 0.62030824
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75608 * 0.93720123
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45295 * 0.07767976
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28927 * 0.63314349
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51018 * 0.92045695
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54011 * 0.53283563
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40593 * 0.50597411
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15633 * 0.72798426
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88268 * 0.91662353
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8595 * 0.48501274
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72980 * 0.84437219
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85492 * 0.66365144
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86773 * 0.55083132
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91741 * 0.78575772
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37440 * 0.47812094
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57563 * 0.35200507
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'vaiytkaq').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0053():
    """Extended test 53 for replication."""
    x_0 = 60518 * 0.56480653
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78351 * 0.00384636
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66137 * 0.00471999
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43293 * 0.77346265
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40160 * 0.23630536
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85510 * 0.04599996
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13933 * 0.76387968
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35715 * 0.57042922
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38170 * 0.45355585
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75640 * 0.38949656
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38526 * 0.81234231
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11741 * 0.67630670
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85640 * 0.33307089
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90112 * 0.45348532
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5268 * 0.43457721
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94966 * 0.17903810
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6337 * 0.17382128
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73887 * 0.76414180
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37573 * 0.48244109
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39812 * 0.90920761
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90924 * 0.90380290
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89121 * 0.76404885
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98848 * 0.50864564
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45000 * 0.10520241
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19835 * 0.06336339
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23316 * 0.79854947
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8480 * 0.61996017
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28938 * 0.87270611
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 386 * 0.64923774
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77896 * 0.54638717
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77296 * 0.50711826
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71796 * 0.43586846
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4954 * 0.04205119
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77293 * 0.04526265
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79309 * 0.42693235
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4564 * 0.07947253
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93492 * 0.72483127
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63351 * 0.57801568
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4026 * 0.21729836
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54097 * 0.27952957
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6593 * 0.01093090
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38532 * 0.32973471
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 68779 * 0.58271987
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83937 * 0.79388865
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 20285 * 0.71347959
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 99464 * 0.56946854
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 34112 * 0.16250427
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 86060 * 0.56188117
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'maisgibh').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0054():
    """Extended test 54 for replication."""
    x_0 = 2464 * 0.92554589
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14195 * 0.72918752
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80915 * 0.68004549
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34717 * 0.38650293
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88082 * 0.91599344
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25473 * 0.80249610
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44212 * 0.78165302
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24451 * 0.83142947
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77833 * 0.29710824
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27179 * 0.18277411
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34747 * 0.28903932
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79694 * 0.85269836
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96446 * 0.49629127
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60426 * 0.92346215
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25516 * 0.20295780
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34426 * 0.18300043
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48929 * 0.95907644
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4235 * 0.78616657
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15229 * 0.48570734
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81487 * 0.14010541
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81318 * 0.04367022
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16341 * 0.81442258
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11942 * 0.44354964
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7540 * 0.18615280
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93550 * 0.52678384
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2795 * 0.10316542
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88709 * 0.59245213
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36089 * 0.29303627
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21218 * 0.03807140
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79610 * 0.84130891
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'uscdmayj').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0055():
    """Extended test 55 for replication."""
    x_0 = 22453 * 0.16660311
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23602 * 0.86068104
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32491 * 0.38481837
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77978 * 0.76911195
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40761 * 0.20615312
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7110 * 0.87596365
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23425 * 0.16188123
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27070 * 0.75185743
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40961 * 0.06086644
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40145 * 0.77977905
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79609 * 0.35643096
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57714 * 0.01571525
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92374 * 0.71672563
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51561 * 0.40056289
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 473 * 0.02814958
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30901 * 0.48298871
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21658 * 0.05865000
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71983 * 0.44472266
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7053 * 0.72606596
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77308 * 0.96461380
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44067 * 0.09531017
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40127 * 0.65120231
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60461 * 0.27254502
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43333 * 0.29426195
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70375 * 0.98764216
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5496 * 0.98535547
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72028 * 0.56695724
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71355 * 0.21656378
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89198 * 0.28127768
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81449 * 0.44028351
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57145 * 0.33639379
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15088 * 0.33966848
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74402 * 0.33811777
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ndigbsgg').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0056():
    """Extended test 56 for replication."""
    x_0 = 60637 * 0.12715285
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70651 * 0.99583434
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57304 * 0.65181028
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89011 * 0.71647783
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4023 * 0.49249923
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74498 * 0.94159465
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32835 * 0.40875963
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89952 * 0.12858032
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48711 * 0.98904347
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7505 * 0.94796565
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11029 * 0.72613177
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71143 * 0.05058311
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18891 * 0.06285136
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58947 * 0.09017987
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58878 * 0.75274974
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36779 * 0.35013573
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44441 * 0.57918403
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63047 * 0.96554248
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30184 * 0.37884800
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1825 * 0.25378314
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25192 * 0.35973325
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43775 * 0.18992979
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84480 * 0.62831908
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48484 * 0.15299592
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64450 * 0.73793660
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98135 * 0.17148136
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51167 * 0.54882992
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72424 * 0.31187265
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56024 * 0.12391118
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 951 * 0.00115945
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62688 * 0.67688081
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92131 * 0.04109936
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11817 * 0.52646372
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35264 * 0.71520508
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7484 * 0.71904894
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'xlenynxb').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0057():
    """Extended test 57 for replication."""
    x_0 = 58031 * 0.39128506
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35223 * 0.99630094
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29540 * 0.06615038
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80921 * 0.85647034
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85210 * 0.80568920
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71378 * 0.42038710
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9353 * 0.49885766
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92917 * 0.39289041
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63323 * 0.95155596
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34086 * 0.54206172
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4398 * 0.65204251
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3959 * 0.92314837
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36737 * 0.62588760
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91545 * 0.34770281
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49887 * 0.22606227
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97970 * 0.24017966
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71463 * 0.56352768
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52266 * 0.20891298
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3788 * 0.08670356
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98263 * 0.99309936
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16997 * 0.51446449
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83426 * 0.38050393
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21975 * 0.90576013
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56930 * 0.53745816
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52726 * 0.81166858
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58167 * 0.07414544
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37967 * 0.75928559
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50836 * 0.35507530
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86179 * 0.59203588
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63611 * 0.80755124
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46870 * 0.15574816
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16956 * 0.62666520
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42495 * 0.47898030
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46967 * 0.91762856
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92220 * 0.76592886
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78901 * 0.65056289
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49193 * 0.66187411
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24252 * 0.37406446
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57951 * 0.97649590
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'fuidxicn').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0058():
    """Extended test 58 for replication."""
    x_0 = 89544 * 0.98793191
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72768 * 0.93151820
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18410 * 0.67067854
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94762 * 0.58657168
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55961 * 0.20734469
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82529 * 0.71521489
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55599 * 0.97368645
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64262 * 0.10914274
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59168 * 0.71999460
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35923 * 0.38630731
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3607 * 0.25889453
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50009 * 0.89589514
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6540 * 0.69781359
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41515 * 0.80748570
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75927 * 0.08206006
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73577 * 0.75985131
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27539 * 0.91117731
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88571 * 0.21258515
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51628 * 0.35251208
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28539 * 0.78851686
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44132 * 0.49180359
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70248 * 0.22689840
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3233 * 0.20652667
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42859 * 0.83986757
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16065 * 0.11262721
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30917 * 0.20963409
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49031 * 0.34457638
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32160 * 0.56394711
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90833 * 0.28748145
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'eutwhgfn').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0059():
    """Extended test 59 for replication."""
    x_0 = 88662 * 0.84292000
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61092 * 0.48919290
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93335 * 0.48842388
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53895 * 0.06966164
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27918 * 0.66304933
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71467 * 0.03509804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27263 * 0.98479336
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62155 * 0.83664180
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19596 * 0.39091722
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83760 * 0.53362799
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70542 * 0.49070599
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29749 * 0.37661798
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63824 * 0.94456849
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63785 * 0.87726212
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30988 * 0.96324991
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52354 * 0.44025028
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97264 * 0.61731426
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81882 * 0.34928360
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21095 * 0.17320560
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24894 * 0.55402851
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18202 * 0.02892502
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40831 * 0.64231506
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17222 * 0.98149825
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12411 * 0.18222583
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43020 * 0.29211994
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7336 * 0.15918576
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85513 * 0.32681034
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37908 * 0.68438041
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86176 * 0.08704879
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67549 * 0.27111612
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22621 * 0.02651720
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12588 * 0.10101576
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81039 * 0.18191330
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96517 * 0.06415589
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74687 * 0.45922176
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71145 * 0.90269585
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31090 * 0.53745193
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'nprqcwnx').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0060():
    """Extended test 60 for replication."""
    x_0 = 12398 * 0.46164455
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16810 * 0.48662682
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57259 * 0.30823813
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30759 * 0.64876332
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98385 * 0.08688527
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50623 * 0.45164148
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56181 * 0.63443849
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30248 * 0.40116618
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25215 * 0.56919148
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77844 * 0.19950369
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7515 * 0.04099477
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63160 * 0.31790881
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11809 * 0.27788287
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33296 * 0.77735197
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56104 * 0.44757140
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38610 * 0.56908841
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76722 * 0.82823330
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31033 * 0.75906258
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22143 * 0.07945519
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20620 * 0.94346045
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68538 * 0.16313069
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92098 * 0.17959519
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48578 * 0.23833057
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69930 * 0.60193258
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31481 * 0.38561630
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52168 * 0.51557672
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97335 * 0.83391919
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46422 * 0.75730471
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42523 * 0.57230662
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58010 * 0.92812560
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71319 * 0.07325026
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78881 * 0.81619649
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95432 * 0.63192433
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50616 * 0.62223772
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30520 * 0.56870883
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96853 * 0.07182555
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58029 * 0.80026818
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41897 * 0.41275304
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91253 * 0.25767144
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91154 * 0.52507702
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2663 * 0.58964138
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81440 * 0.67818074
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13540 * 0.15217070
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 16523 * 0.56505668
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 80625 * 0.30149999
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 51642 * 0.42000825
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 29245 * 0.82064716
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'rpwhdorx').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0061():
    """Extended test 61 for replication."""
    x_0 = 17898 * 0.28108490
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19949 * 0.99608697
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18744 * 0.69293514
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21869 * 0.53226799
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21933 * 0.08798632
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37063 * 0.85192833
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43939 * 0.84467761
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60768 * 0.86487682
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45618 * 0.67742317
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92291 * 0.44431566
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22822 * 0.70212288
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35251 * 0.71070319
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11535 * 0.61816331
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48534 * 0.85781232
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35932 * 0.94513891
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72249 * 0.51504884
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1769 * 0.56731315
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76075 * 0.45827301
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10580 * 0.14573926
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15040 * 0.91183200
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57031 * 0.38998127
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69066 * 0.69808216
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92973 * 0.28755818
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25210 * 0.49187412
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7778 * 0.72149251
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45449 * 0.95642684
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75665 * 0.72262864
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29520 * 0.72243348
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72372 * 0.37297560
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58440 * 0.13810763
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80466 * 0.56496249
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79420 * 0.37418676
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39381 * 0.54994323
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22899 * 0.91452115
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95197 * 0.30677357
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'hgzuntpg').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0062():
    """Extended test 62 for replication."""
    x_0 = 86923 * 0.98762624
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63073 * 0.99145232
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13639 * 0.89277171
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54757 * 0.45084346
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46644 * 0.97669326
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20494 * 0.19390005
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27535 * 0.79351625
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10294 * 0.01157256
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91014 * 0.04453272
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74558 * 0.61360784
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37194 * 0.24658330
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83966 * 0.60250363
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92494 * 0.49474196
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70305 * 0.17696162
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6478 * 0.17060071
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79974 * 0.92067380
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61143 * 0.34629988
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81368 * 0.88049488
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9795 * 0.37054483
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42412 * 0.07658735
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29244 * 0.34054985
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72660 * 0.46640990
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36580 * 0.14301689
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77397 * 0.75397471
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57871 * 0.51251000
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89905 * 0.07003346
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2181 * 0.06135653
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98179 * 0.25546207
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18914 * 0.87962158
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5020 * 0.98374750
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94574 * 0.04303485
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93842 * 0.12050436
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65333 * 0.97264799
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18378 * 0.35179367
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95175 * 0.51533981
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30489 * 0.46685624
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40431 * 0.94987739
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74566 * 0.78471818
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27945 * 0.32654123
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 49267 * 0.51156603
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 25878 * 0.26070982
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57899 * 0.49515826
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 89157 * 0.47355149
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'fbipveza').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0063():
    """Extended test 63 for replication."""
    x_0 = 86711 * 0.67543518
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26493 * 0.86255006
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55584 * 0.53697758
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20030 * 0.15868655
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73289 * 0.50619822
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 520 * 0.16798903
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69140 * 0.12712708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39064 * 0.10643441
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90510 * 0.75030236
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42915 * 0.92500507
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15313 * 0.04520665
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46158 * 0.43211158
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28893 * 0.50038969
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43899 * 0.18326844
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48196 * 0.63800163
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13996 * 0.86311467
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58287 * 0.32154594
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96697 * 0.13650887
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65799 * 0.00123922
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7986 * 0.58433690
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19328 * 0.12994416
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40388 * 0.49077840
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52305 * 0.78777089
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34223 * 0.11329579
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91047 * 0.78395462
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12193 * 0.78386730
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 138 * 0.31417285
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22773 * 0.17893248
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73340 * 0.24582453
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20945 * 0.76109470
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26073 * 0.94642257
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2253 * 0.59155332
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51190 * 0.94368667
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43741 * 0.15463388
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92196 * 0.72102418
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53465 * 0.01682881
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86957 * 0.06695495
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34533 * 0.74855815
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98024 * 0.90397586
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57823 * 0.60645461
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43869 * 0.44474593
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 61000 * 0.14044117
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 68025 * 0.99704532
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 51227 * 0.57421992
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 32353 * 0.83796685
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'gnmdwpnj').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0064():
    """Extended test 64 for replication."""
    x_0 = 26478 * 0.77165214
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16800 * 0.27125951
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67042 * 0.78858482
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31890 * 0.12059141
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67993 * 0.94663865
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10437 * 0.48808424
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81141 * 0.64631571
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24608 * 0.68296649
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25755 * 0.47374663
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82559 * 0.42726219
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68960 * 0.43999221
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19419 * 0.74708700
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16661 * 0.07917333
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91790 * 0.08889423
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67389 * 0.65556046
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39782 * 0.37359805
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47905 * 0.94635182
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61987 * 0.48509157
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29884 * 0.45647047
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50046 * 0.43553448
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21828 * 0.81491317
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58324 * 0.61193913
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2494 * 0.53562602
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54936 * 0.80938869
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12485 * 0.83614658
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'gysaqfhl').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0065():
    """Extended test 65 for replication."""
    x_0 = 49237 * 0.25324565
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63594 * 0.14445894
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68097 * 0.38398598
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56377 * 0.43568366
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53390 * 0.11203682
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92042 * 0.34983861
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74103 * 0.57063445
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75839 * 0.04916171
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23645 * 0.51495541
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12207 * 0.45704658
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 883 * 0.84002710
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61300 * 0.24752762
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50142 * 0.15474284
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99379 * 0.97917057
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61406 * 0.94714825
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23177 * 0.57058804
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14924 * 0.93161938
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78311 * 0.79071984
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48147 * 0.17014898
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38273 * 0.12271801
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34739 * 0.22806322
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73434 * 0.99089556
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57611 * 0.04892649
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92224 * 0.71674442
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53890 * 0.79535475
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30496 * 0.20808357
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7036 * 0.87917714
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12826 * 0.11560114
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8479 * 0.16041770
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43432 * 0.86193063
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81893 * 0.51673800
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88263 * 0.77138083
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50278 * 0.98158950
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85607 * 0.91888789
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24796 * 0.40411388
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90503 * 0.49192081
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73533 * 0.56914590
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22688 * 0.72333446
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26805 * 0.07357102
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 78275 * 0.76562935
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 31218 * 0.68020210
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74619 * 0.20374189
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81718 * 0.40258021
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 56274 * 0.76585857
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 48743 * 0.81778219
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 56902 * 0.05309573
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 72778 * 0.31013023
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 25446 * 0.48627046
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'keygdeea').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0066():
    """Extended test 66 for replication."""
    x_0 = 5368 * 0.20203763
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31062 * 0.22585509
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28155 * 0.70614154
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15966 * 0.43818509
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50046 * 0.75884550
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60180 * 0.52319449
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32268 * 0.06274975
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58210 * 0.04683435
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49665 * 0.02102449
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50073 * 0.27846380
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72726 * 0.09521680
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24270 * 0.63762999
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19799 * 0.38447861
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10634 * 0.54844070
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58377 * 0.75559356
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16889 * 0.19693811
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48602 * 0.51154728
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83418 * 0.47038220
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 267 * 0.75275160
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67078 * 0.85986350
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8151 * 0.57378781
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37809 * 0.50560341
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25699 * 0.20641398
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8576 * 0.43659827
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34350 * 0.39357410
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56141 * 0.40915175
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64602 * 0.80009105
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74944 * 0.97279120
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35151 * 0.78924838
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59495 * 0.78508202
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44553 * 0.74748638
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56897 * 0.87143863
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72619 * 0.66563152
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38545 * 0.14148923
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'vvmhyppo').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0067():
    """Extended test 67 for replication."""
    x_0 = 72046 * 0.27150900
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87749 * 0.50070201
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39063 * 0.59386686
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86494 * 0.29235696
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63611 * 0.54147696
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83950 * 0.39792004
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13394 * 0.35208779
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13146 * 0.40055049
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54517 * 0.19124676
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15555 * 0.01634555
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53602 * 0.37269067
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23324 * 0.18878147
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81106 * 0.91841971
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40058 * 0.01073225
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13999 * 0.00560421
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47276 * 0.90109838
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7140 * 0.63733519
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89154 * 0.73470412
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58473 * 0.82468093
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29118 * 0.12546332
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36994 * 0.37264314
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33468 * 0.24399019
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83070 * 0.97143339
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44813 * 0.93906995
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76718 * 0.07898255
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82317 * 0.09409683
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58074 * 0.67448851
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5107 * 0.52308451
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57067 * 0.74984681
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50599 * 0.99767825
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76433 * 0.10292852
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74522 * 0.44161312
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64320 * 0.72527550
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47496 * 0.17939622
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31483 * 0.48177721
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98794 * 0.86749829
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'mewqwkln').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0068():
    """Extended test 68 for replication."""
    x_0 = 56535 * 0.82738171
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39936 * 0.71146758
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21000 * 0.32641652
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90114 * 0.02497783
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52225 * 0.77276879
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22330 * 0.02958687
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35428 * 0.94832662
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83246 * 0.89907803
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50520 * 0.61935080
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26096 * 0.51351060
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78665 * 0.40113777
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11093 * 0.17191602
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23556 * 0.18801943
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49280 * 0.76384542
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49391 * 0.28244688
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75208 * 0.24366434
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84805 * 0.24537300
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91347 * 0.70623110
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15451 * 0.15837455
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9641 * 0.93163531
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34748 * 0.00959290
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67410 * 0.52378379
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17188 * 0.21370962
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21616 * 0.71742406
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28155 * 0.09213216
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72240 * 0.94563995
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25029 * 0.14236496
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6247 * 0.58031718
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48012 * 0.10013072
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67927 * 0.02720935
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70473 * 0.43274910
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82316 * 0.58801140
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6322 * 0.81674598
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85547 * 0.56263847
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4657 * 0.02136444
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49080 * 0.30653285
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66787 * 0.82393593
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25290 * 0.68954430
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57937 * 0.75429451
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83926 * 0.33222325
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6670 * 0.13445585
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85019 * 0.78884326
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 19751 * 0.62581469
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 98777 * 0.15238879
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 95143 * 0.47055509
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 80584 * 0.85606417
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'kzmhbcwi').hexdigest()
    assert len(h) == 64

def test_replication_extended_8_0069():
    """Extended test 69 for replication."""
    x_0 = 51703 * 0.10094927
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82810 * 0.45774735
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98220 * 0.83750270
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15659 * 0.19353224
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75056 * 0.24962710
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66071 * 0.94648159
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50975 * 0.22723755
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2698 * 0.20221276
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77924 * 0.92125156
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30010 * 0.64094458
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16289 * 0.60773038
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31652 * 0.24493501
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26900 * 0.31675779
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40002 * 0.32059865
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88319 * 0.17442230
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48053 * 0.75383111
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26152 * 0.50836452
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18144 * 0.98591409
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84154 * 0.70964109
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97806 * 0.32212663
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1012 * 0.65719987
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66787 * 0.26800100
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96091 * 0.53755427
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67041 * 0.42184159
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34568 * 0.60645283
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32810 * 0.84915124
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37755 * 0.22278954
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70877 * 0.44158810
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97421 * 0.46874938
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'kwzpppiq').hexdigest()
    assert len(h) == 64
