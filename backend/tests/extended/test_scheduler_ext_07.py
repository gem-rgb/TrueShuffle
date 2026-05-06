"""Extended tests for scheduler suite 7."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_scheduler_extended_7_0000():
    """Extended test 0 for scheduler."""
    x_0 = 4640 * 0.31134852
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7218 * 0.00712821
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59153 * 0.90106834
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31760 * 0.05004626
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59338 * 0.16950004
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18949 * 0.63646892
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31983 * 0.61907786
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17825 * 0.41174509
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46376 * 0.09815525
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36358 * 0.14744916
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93722 * 0.37113927
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73281 * 0.53011694
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25019 * 0.76876692
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31963 * 0.19986069
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75694 * 0.90939935
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65579 * 0.23931307
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80780 * 0.60879633
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65758 * 0.31851455
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65584 * 0.18245462
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81534 * 0.51633909
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9480 * 0.12269187
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58711 * 0.69614246
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82223 * 0.23962494
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47411 * 0.08168477
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70050 * 0.05959962
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77967 * 0.44426778
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66803 * 0.19647380
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34825 * 0.75663002
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66295 * 0.78851035
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19161 * 0.27293313
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47858 * 0.58746614
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'xsalotco').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0001():
    """Extended test 1 for scheduler."""
    x_0 = 24683 * 0.79685930
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86202 * 0.73807166
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58605 * 0.38677939
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33753 * 0.82777714
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20946 * 0.69460265
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18588 * 0.52080052
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83890 * 0.24460182
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49603 * 0.15418632
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1401 * 0.80908496
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63039 * 0.57812434
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84872 * 0.84365675
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35582 * 0.59706887
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72550 * 0.71671200
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57603 * 0.13976279
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2268 * 0.89558879
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46827 * 0.56196402
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64480 * 0.16400942
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97555 * 0.38422672
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67248 * 0.50348940
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94814 * 0.11720429
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53152 * 0.39842838
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88149 * 0.05352894
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'ypyhwomi').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0002():
    """Extended test 2 for scheduler."""
    x_0 = 85953 * 0.41716530
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 647 * 0.58722478
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73070 * 0.24495112
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46847 * 0.83069013
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38056 * 0.29500151
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28863 * 0.69627844
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91737 * 0.73170728
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53982 * 0.86544047
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46247 * 0.54787970
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69785 * 0.51940333
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90575 * 0.83499869
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92349 * 0.14143822
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68860 * 0.26852864
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14477 * 0.62853678
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64168 * 0.73629470
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46933 * 0.01488241
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21230 * 0.12177577
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43595 * 0.97506995
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60644 * 0.39585470
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42135 * 0.84531791
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93501 * 0.23717671
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7615 * 0.54201856
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17458 * 0.93668449
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96217 * 0.41534598
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40516 * 0.56705752
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25459 * 0.82643319
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39590 * 0.72393194
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64645 * 0.41725039
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62509 * 0.65547412
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38069 * 0.54391663
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63087 * 0.56240907
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36772 * 0.61206676
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63074 * 0.01888356
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84149 * 0.42894942
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38579 * 0.30306463
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88619 * 0.63796718
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24264 * 0.44270487
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'zhswjyqm').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0003():
    """Extended test 3 for scheduler."""
    x_0 = 57643 * 0.99772679
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28331 * 0.50806416
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23085 * 0.04222209
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46686 * 0.50878831
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61257 * 0.64056592
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18408 * 0.42186656
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37276 * 0.46356736
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46256 * 0.12893834
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13506 * 0.04864786
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7412 * 0.45938026
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90207 * 0.28295013
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98679 * 0.72572809
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75825 * 0.01401572
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94569 * 0.63725886
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6910 * 0.65154337
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5747 * 0.95267562
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13364 * 0.23072044
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90522 * 0.33258565
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90796 * 0.67105047
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60549 * 0.23797710
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99016 * 0.22989084
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64228 * 0.24334593
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14694 * 0.45318896
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19083 * 0.03421353
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23013 * 0.22487156
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96675 * 0.16960235
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21291 * 0.65475246
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86063 * 0.81904479
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30417 * 0.41608007
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53883 * 0.05664839
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44933 * 0.16217118
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59680 * 0.79379634
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7080 * 0.49042654
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'vhvlxreg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0004():
    """Extended test 4 for scheduler."""
    x_0 = 56643 * 0.17336920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15686 * 0.11566078
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88102 * 0.69559992
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46263 * 0.85316839
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36203 * 0.39315381
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89787 * 0.10172804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63163 * 0.52807305
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18545 * 0.63992306
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39710 * 0.20038867
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31668 * 0.15251074
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77578 * 0.50267638
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77961 * 0.74437155
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17406 * 0.63124934
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30524 * 0.05784910
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11507 * 0.47507767
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95744 * 0.93237322
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19103 * 0.29347981
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71033 * 0.66050689
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79579 * 0.30029911
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50008 * 0.59650820
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75244 * 0.62039022
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95413 * 0.71984367
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17497 * 0.38282446
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7092 * 0.62559505
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4258 * 0.45029750
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87360 * 0.35372025
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63081 * 0.17843111
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16392 * 0.28835770
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69750 * 0.72865424
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31710 * 0.66328157
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44244 * 0.13221562
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17718 * 0.91749199
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92296 * 0.62655491
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64207 * 0.19792258
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59954 * 0.81059066
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64001 * 0.57986588
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25358 * 0.58185576
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94834 * 0.85392787
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57915 * 0.05119926
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2544 * 0.65746184
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75859 * 0.51493829
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'ngacenhp').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0005():
    """Extended test 5 for scheduler."""
    x_0 = 58148 * 0.55192404
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99672 * 0.71179498
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17786 * 0.40261635
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65299 * 0.02215018
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10822 * 0.90995501
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49093 * 0.41349028
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34500 * 0.61675816
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61068 * 0.60156547
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2737 * 0.03619326
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35159 * 0.89570075
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60458 * 0.77275792
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21783 * 0.22690573
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20773 * 0.02754449
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4002 * 0.02998065
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43361 * 0.07210002
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70773 * 0.99949168
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26505 * 0.01868891
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28608 * 0.48400840
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5685 * 0.85892891
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90111 * 0.02460281
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42777 * 0.09826560
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65918 * 0.52467035
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18054 * 0.38770667
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30709 * 0.06753593
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14900 * 0.68360493
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14746 * 0.80408848
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84766 * 0.62674517
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74738 * 0.15390865
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32675 * 0.80396552
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60077 * 0.83374252
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38196 * 0.73366143
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86281 * 0.03966409
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43663 * 0.52417417
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99704 * 0.33143931
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53127 * 0.63844157
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45374 * 0.54810249
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48293 * 0.82153853
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82433 * 0.13196805
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ukzgpoyv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0006():
    """Extended test 6 for scheduler."""
    x_0 = 99836 * 0.73545697
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85284 * 0.90118943
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29543 * 0.53873644
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30458 * 0.40293462
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94959 * 0.57576773
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78712 * 0.52697631
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45917 * 0.19236703
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86685 * 0.14770676
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22497 * 0.72076155
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55627 * 0.20719251
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15319 * 0.90198581
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73446 * 0.37645308
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97750 * 0.56322632
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92095 * 0.56351947
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11900 * 0.13416323
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70027 * 0.00221081
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40375 * 0.97775938
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59235 * 0.11880921
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52890 * 0.52199158
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95722 * 0.84419420
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44013 * 0.17137294
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8737 * 0.97927190
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92816 * 0.56313496
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9226 * 0.62376131
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34861 * 0.42993802
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81999 * 0.84594736
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87137 * 0.16334162
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44280 * 0.58233786
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58043 * 0.94900672
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70910 * 0.57927179
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55 * 0.64043746
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38573 * 0.09887481
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15361 * 0.66232228
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47507 * 0.77309107
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33090 * 0.68627112
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99398 * 0.52547367
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22557 * 0.75881052
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60837 * 0.42022342
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12762 * 0.41929112
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25164 * 0.33951064
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11437 * 0.06701422
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66384 * 0.47917552
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16224 * 0.43705764
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34738 * 0.77343420
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'vlilbfom').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0007():
    """Extended test 7 for scheduler."""
    x_0 = 9756 * 0.65729174
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63416 * 0.18798364
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39560 * 0.24688189
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95329 * 0.18817230
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49168 * 0.18133079
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16005 * 0.68155212
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75577 * 0.35483656
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62958 * 0.97598140
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99031 * 0.83079314
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51170 * 0.17749514
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27619 * 0.33822251
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3685 * 0.73349409
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47395 * 0.47143286
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61272 * 0.43634783
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21116 * 0.77035752
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17787 * 0.47470159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73106 * 0.67389101
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54308 * 0.02009829
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97560 * 0.66797268
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81518 * 0.12157754
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47414 * 0.00142698
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16789 * 0.75941551
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92694 * 0.85123136
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70276 * 0.72227156
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19938 * 0.14777991
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43223 * 0.65084902
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94157 * 0.42120143
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77042 * 0.35105430
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67454 * 0.27102765
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20089 * 0.06035987
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34994 * 0.60904412
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43465 * 0.56252829
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53888 * 0.62149935
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61817 * 0.51848685
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44518 * 0.02969482
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42414 * 0.81813602
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13667 * 0.99463974
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86758 * 0.00184537
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6334 * 0.57954436
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 78919 * 0.81219873
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91644 * 0.05297005
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 76878 * 0.14217364
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9534 * 0.21264907
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39625 * 0.51594669
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35103 * 0.59922392
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 56566 * 0.99411204
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 53315 * 0.38370513
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 56825 * 0.80688526
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 81136 * 0.54220192
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 80912 * 0.49040926
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'mzjpyyyi').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0008():
    """Extended test 8 for scheduler."""
    x_0 = 85654 * 0.79676689
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85992 * 0.81541339
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95485 * 0.87149717
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69124 * 0.33791182
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21217 * 0.22043673
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13905 * 0.15468043
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38283 * 0.91501691
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99270 * 0.44668125
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40428 * 0.48618861
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63458 * 0.35434639
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77831 * 0.27812401
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91151 * 0.01405500
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65733 * 0.79824872
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80108 * 0.06745403
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46069 * 0.13543971
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9597 * 0.63083559
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71554 * 0.76338907
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40011 * 0.78128434
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86770 * 0.25447626
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7984 * 0.47147774
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86108 * 0.14166857
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82952 * 0.89999500
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86914 * 0.55583923
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 906 * 0.76306328
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74157 * 0.40898956
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39353 * 0.03616370
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77118 * 0.25735452
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88282 * 0.34643315
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74858 * 0.86974421
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94168 * 0.18943502
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 343 * 0.72023302
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13978 * 0.58144386
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9913 * 0.79303848
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79422 * 0.53076221
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63885 * 0.46129927
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'eojmxhug').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0009():
    """Extended test 9 for scheduler."""
    x_0 = 40955 * 0.91724440
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37967 * 0.20630928
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80892 * 0.71553386
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88482 * 0.33734354
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85341 * 0.19752118
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81889 * 0.47242893
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8869 * 0.02711353
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38481 * 0.27550348
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19908 * 0.43247257
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91398 * 0.54556781
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32243 * 0.77778661
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32305 * 0.99300533
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35246 * 0.04490782
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73476 * 0.68151513
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73076 * 0.80030099
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21160 * 0.62047345
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81256 * 0.30320769
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82679 * 0.03952758
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55663 * 0.65746632
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29957 * 0.01708063
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56138 * 0.31139049
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92194 * 0.53788127
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23172 * 0.52599392
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84745 * 0.09931858
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18390 * 0.73219526
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26789 * 0.26401004
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28062 * 0.43355584
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91714 * 0.00296203
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17271 * 0.21337977
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81842 * 0.91689651
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52543 * 0.96184124
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75711 * 0.69995613
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32269 * 0.50827317
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13337 * 0.39300179
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86557 * 0.12616129
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99889 * 0.60548767
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8614 * 0.16445518
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92402 * 0.88436243
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43234 * 0.40968306
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23232 * 0.92216819
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47886 * 0.94933648
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54254 * 0.89356779
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70574 * 0.76432392
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69156 * 0.73549535
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79954 * 0.65522494
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'saebqoij').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0010():
    """Extended test 10 for scheduler."""
    x_0 = 98450 * 0.74015321
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14177 * 0.39712510
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82898 * 0.41626097
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48055 * 0.59955648
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12322 * 0.74369949
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97784 * 0.85148229
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56775 * 0.81611297
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26615 * 0.46505914
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62233 * 0.40246358
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17672 * 0.63861602
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34838 * 0.36789353
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31745 * 0.36175057
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56257 * 0.48222524
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41597 * 0.23355124
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14805 * 0.26466429
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78837 * 0.57004551
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73348 * 0.62370402
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1654 * 0.74651273
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14578 * 0.42795394
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88293 * 0.24524261
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63658 * 0.97903281
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11536 * 0.46377394
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84204 * 0.38017567
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2606 * 0.77334111
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70408 * 0.93776043
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77524 * 0.46227327
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29746 * 0.11959166
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17273 * 0.79949963
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27971 * 0.19431997
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39469 * 0.39454479
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27338 * 0.27358205
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81529 * 0.00360703
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85335 * 0.93472547
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95512 * 0.58756404
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99810 * 0.32328100
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88998 * 0.78394637
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'mkmjkflf').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0011():
    """Extended test 11 for scheduler."""
    x_0 = 35999 * 0.07584077
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16718 * 0.34989348
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17817 * 0.06018034
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69998 * 0.43950702
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99946 * 0.90189199
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41692 * 0.01039046
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7590 * 0.83843609
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73530 * 0.68166355
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40182 * 0.79709481
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10894 * 0.57248358
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66354 * 0.58216680
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80194 * 0.61207941
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56768 * 0.35658151
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69468 * 0.95422262
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34399 * 0.96305524
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98727 * 0.83255967
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99630 * 0.56172378
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56963 * 0.43232088
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18321 * 0.38814024
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53489 * 0.78300992
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11439 * 0.81626158
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4357 * 0.61219018
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44411 * 0.75697208
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51245 * 0.83060785
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14857 * 0.19363107
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23947 * 0.73832044
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38539 * 0.82950936
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3668 * 0.98465480
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13387 * 0.87559222
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80882 * 0.82443547
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54982 * 0.85166625
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96780 * 0.34828415
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60316 * 0.96792364
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80020 * 0.56953800
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63194 * 0.71115372
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14648 * 0.82199733
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60024 * 0.70991289
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20814 * 0.11115283
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91369 * 0.79661413
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74161 * 0.69109280
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'yvowucwl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0012():
    """Extended test 12 for scheduler."""
    x_0 = 74487 * 0.77798688
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74605 * 0.91459795
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41887 * 0.71311660
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37122 * 0.11739243
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57865 * 0.35884401
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4400 * 0.02516801
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64787 * 0.08438969
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81677 * 0.02454061
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62552 * 0.27155672
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1155 * 0.02574707
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27192 * 0.32464353
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39777 * 0.72020378
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66892 * 0.49222994
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80439 * 0.11264875
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40531 * 0.15065326
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77853 * 0.26076689
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24147 * 0.84703808
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96930 * 0.31051708
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89080 * 0.44369822
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5448 * 0.11021937
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8276 * 0.29519914
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84190 * 0.63446930
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93903 * 0.27386258
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70568 * 0.77939152
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73734 * 0.09241692
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3348 * 0.13865559
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57779 * 0.06487324
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96730 * 0.58195161
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94456 * 0.00659093
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39140 * 0.43222624
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8428 * 0.49460324
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73518 * 0.38437284
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69428 * 0.07110756
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57987 * 0.42296736
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30235 * 0.65057148
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42274 * 0.57287679
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24693 * 0.01475249
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18119 * 0.00243006
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20587 * 0.44545644
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73110 * 0.32929406
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80928 * 0.50866580
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37532 * 0.06396752
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 38860 * 0.08093670
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 86870 * 0.68950375
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'vnmdlqvo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0013():
    """Extended test 13 for scheduler."""
    x_0 = 77642 * 0.80057900
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40243 * 0.71790121
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33982 * 0.29264604
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28063 * 0.42051672
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74531 * 0.07509574
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 984 * 0.94699571
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89232 * 0.79535237
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85151 * 0.83491918
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50636 * 0.23665509
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29540 * 0.51153823
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37855 * 0.97176746
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59037 * 0.54188014
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45106 * 0.18104711
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10023 * 0.92978493
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67703 * 0.17111871
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59569 * 0.32614194
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4697 * 0.20956805
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20386 * 0.41229721
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71403 * 0.94380519
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46616 * 0.70252207
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'zptatwfk').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0014():
    """Extended test 14 for scheduler."""
    x_0 = 69625 * 0.70783465
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47034 * 0.47783898
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76422 * 0.27827575
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28900 * 0.72731432
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23428 * 0.43422214
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12657 * 0.39832711
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62021 * 0.47479901
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98956 * 0.92374270
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13181 * 0.49538175
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92101 * 0.47830895
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21846 * 0.15765995
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93832 * 0.83468757
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65769 * 0.96351668
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17627 * 0.77872639
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2267 * 0.91687112
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85306 * 0.22962591
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29995 * 0.56051745
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 731 * 0.71067774
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3073 * 0.81111911
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65860 * 0.09789237
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29796 * 0.54094285
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83002 * 0.64305545
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70864 * 0.21269717
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38708 * 0.65347397
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16638 * 0.22000098
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15333 * 0.67160706
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11990 * 0.32862783
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11078 * 0.54243130
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44806 * 0.47499552
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28031 * 0.39419687
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8947 * 0.71660951
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'uqfdiorx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0015():
    """Extended test 15 for scheduler."""
    x_0 = 96825 * 0.60257898
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60119 * 0.10777792
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54998 * 0.02849260
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64989 * 0.00603321
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53289 * 0.22375607
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32928 * 0.08067359
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 850 * 0.71309126
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48775 * 0.69169222
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28893 * 0.94370482
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4783 * 0.31399226
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21900 * 0.26402775
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66642 * 0.81652882
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20429 * 0.56875559
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1350 * 0.56565782
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27594 * 0.95053048
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98191 * 0.08387409
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91468 * 0.33240641
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11491 * 0.22741789
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63768 * 0.27673502
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83399 * 0.24882260
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98230 * 0.88403272
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20100 * 0.06186320
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18942 * 0.71163817
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6268 * 0.88663517
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27368 * 0.40411345
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91722 * 0.80397652
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44897 * 0.96731070
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68395 * 0.64874514
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11466 * 0.06109626
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95820 * 0.06914144
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47054 * 0.25594501
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52331 * 0.90926956
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45677 * 0.55230705
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15644 * 0.10469828
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65128 * 0.26182679
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23228 * 0.06563827
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74666 * 0.15979524
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'dudwasbw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0016():
    """Extended test 16 for scheduler."""
    x_0 = 50695 * 0.10765487
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76430 * 0.49498043
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30137 * 0.54761906
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74356 * 0.95757785
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24470 * 0.74362044
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49877 * 0.49332341
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57399 * 0.60481170
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79161 * 0.89785984
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56089 * 0.58976973
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86824 * 0.79772130
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77160 * 0.88299406
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63512 * 0.21968325
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91002 * 0.88147514
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37617 * 0.98001024
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58284 * 0.95530073
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24519 * 0.26863218
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79365 * 0.98955870
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19429 * 0.58553613
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72848 * 0.57138340
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67610 * 0.22460172
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60705 * 0.39871906
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66027 * 0.43032918
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27042 * 0.56031321
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81809 * 0.29838022
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26303 * 0.01251680
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40493 * 0.20602843
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70695 * 0.10438893
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73913 * 0.53912845
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66027 * 0.98797694
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44006 * 0.33174327
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89683 * 0.27213619
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6689 * 0.50724073
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40708 * 0.58697539
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19056 * 0.97316253
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84202 * 0.18893764
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86728 * 0.03524698
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69350 * 0.85166104
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3281 * 0.33686431
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59627 * 0.05895981
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93546 * 0.68873171
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21292 * 0.84034336
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 24142 * 0.98714820
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 4261 * 0.39538163
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 77897 * 0.59902552
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61186 * 0.94417640
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 22513 * 0.26408493
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 62800 * 0.93980882
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 51099 * 0.75393636
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 3785 * 0.61808064
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 79113 * 0.39576328
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'znntyzob').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0017():
    """Extended test 17 for scheduler."""
    x_0 = 97368 * 0.54125695
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40906 * 0.42757297
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50962 * 0.21316671
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45914 * 0.01549122
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12350 * 0.39393396
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5874 * 0.02897314
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19654 * 0.29093109
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18831 * 0.47698889
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43393 * 0.45996151
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97843 * 0.48282935
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80482 * 0.38123776
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45821 * 0.10647606
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49524 * 0.56418517
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43594 * 0.66813160
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1545 * 0.41598050
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4543 * 0.58073081
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46759 * 0.45046058
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34411 * 0.89214862
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77610 * 0.46438894
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46052 * 0.14675467
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11315 * 0.03216869
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9592 * 0.46843191
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26724 * 0.73140538
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78537 * 0.68764339
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46519 * 0.50429650
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27712 * 0.23849260
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44988 * 0.66204033
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10451 * 0.00633181
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64165 * 0.98001036
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19711 * 0.20947963
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48232 * 0.78957616
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98930 * 0.54010733
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19951 * 0.91165561
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94576 * 0.30218766
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lexoxmoo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0018():
    """Extended test 18 for scheduler."""
    x_0 = 247 * 0.30735487
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96178 * 0.73490492
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89996 * 0.89264930
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70362 * 0.02338673
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85352 * 0.47513516
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93493 * 0.98000043
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46143 * 0.44032237
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5818 * 0.41909889
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27852 * 0.42530051
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91344 * 0.01487526
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61279 * 0.08580366
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30120 * 0.80190736
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86057 * 0.84860186
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16053 * 0.51151130
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83746 * 0.07335066
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54761 * 0.26200057
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46872 * 0.70293884
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83296 * 0.83339055
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19365 * 0.63290231
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60613 * 0.03605109
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98607 * 0.85423727
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13042 * 0.29537851
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45627 * 0.66216976
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77067 * 0.46295853
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50647 * 0.04296189
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35680 * 0.90114744
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98491 * 0.03681051
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17689 * 0.73785172
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79162 * 0.89025549
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90193 * 0.70150259
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10545 * 0.31397764
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66942 * 0.30426920
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11398 * 0.65106732
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99318 * 0.95592699
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18554 * 0.55179697
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13690 * 0.06681936
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64357 * 0.63917343
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63319 * 0.52829538
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70343 * 0.55212717
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32620 * 0.06403737
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 9506 * 0.64232219
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 32112 * 0.92895347
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96339 * 0.72144863
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 9181 * 0.47164696
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 80870 * 0.88884914
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 66897 * 0.45058200
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'wpvdafeu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0019():
    """Extended test 19 for scheduler."""
    x_0 = 49950 * 0.64088062
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89915 * 0.78871542
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36483 * 0.55549740
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44984 * 0.96888773
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67645 * 0.60868115
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5642 * 0.06808873
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31561 * 0.57888955
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16219 * 0.29359788
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99087 * 0.87134317
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80171 * 0.48664020
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17017 * 0.67661599
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76654 * 0.46602902
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32626 * 0.32367319
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64179 * 0.89709062
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5080 * 0.73864225
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93139 * 0.99315022
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7097 * 0.40558963
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38608 * 0.97425593
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48645 * 0.93504901
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73933 * 0.89169967
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87002 * 0.56806435
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18234 * 0.99341673
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82086 * 0.14567543
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'txachlyu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0020():
    """Extended test 20 for scheduler."""
    x_0 = 60653 * 0.34294150
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21572 * 0.41795668
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64008 * 0.44262094
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61121 * 0.09249203
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55400 * 0.88242136
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60872 * 0.84769426
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51134 * 0.41013799
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32386 * 0.14362292
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31860 * 0.28012778
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52258 * 0.52542281
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26233 * 0.41489376
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39867 * 0.26285719
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41724 * 0.51109777
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75937 * 0.51416841
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9165 * 0.11865778
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93561 * 0.67720813
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12044 * 0.20404245
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91593 * 0.92879202
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29087 * 0.00379127
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73974 * 0.00119065
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20852 * 0.49318912
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45398 * 0.75877699
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6151 * 0.75419301
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'dqbswbrw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0021():
    """Extended test 21 for scheduler."""
    x_0 = 15537 * 0.42509800
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18416 * 0.45990756
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29175 * 0.01172700
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16058 * 0.38596349
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91749 * 0.15523743
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53449 * 0.85816195
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68300 * 0.75446287
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43772 * 0.33595967
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53510 * 0.54277951
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3648 * 0.50195695
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52314 * 0.05313889
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66122 * 0.71861019
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1127 * 0.74277628
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32049 * 0.76840101
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21859 * 0.24359375
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3830 * 0.25682858
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92211 * 0.94479253
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19117 * 0.81491412
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17692 * 0.33569605
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40135 * 0.48468472
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10493 * 0.34722612
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31333 * 0.81618015
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38027 * 0.08687579
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6748 * 0.29594033
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16655 * 0.14044762
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1561 * 0.35730182
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58036 * 0.09732488
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77408 * 0.90498299
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52968 * 0.48434548
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98759 * 0.00607855
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91765 * 0.32641404
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13659 * 0.56722535
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96729 * 0.39542137
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34303 * 0.87111709
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60247 * 0.03057257
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98348 * 0.96909266
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39708 * 0.80962313
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12437 * 0.73421381
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52810 * 0.16499279
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55431 * 0.73685880
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86094 * 0.61017314
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14821 * 0.10937259
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15971 * 0.48281628
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11362 * 0.31450386
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 20377 * 0.79140785
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 8666 * 0.99835899
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 37253 * 0.37953045
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 21727 * 0.22235596
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 95829 * 0.74459103
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 97424 * 0.90740765
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'fhcxtuhu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0022():
    """Extended test 22 for scheduler."""
    x_0 = 45101 * 0.69199328
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49926 * 0.68517944
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4663 * 0.64759181
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6065 * 0.59185236
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84463 * 0.38041872
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62486 * 0.50740896
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8692 * 0.56890146
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42502 * 0.40914769
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65980 * 0.44223325
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99797 * 0.42702444
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63402 * 0.91313387
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56236 * 0.31394191
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51047 * 0.04671796
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94603 * 0.02095141
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47787 * 0.43770847
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28009 * 0.57916555
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13975 * 0.78585941
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44156 * 0.70969695
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82884 * 0.87766837
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65052 * 0.96804751
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62819 * 0.95869491
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55658 * 0.20481415
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56095 * 0.90332087
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91255 * 0.86054644
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39700 * 0.73026157
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45184 * 0.51398595
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15909 * 0.03469246
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13931 * 0.07259119
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36013 * 0.36751049
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74112 * 0.09000588
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78337 * 0.20827823
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36254 * 0.68980181
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 818 * 0.85660194
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'njymbycy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0023():
    """Extended test 23 for scheduler."""
    x_0 = 89194 * 0.44710349
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58729 * 0.35605233
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56464 * 0.93683882
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39338 * 0.19777324
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88212 * 0.83716812
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60298 * 0.68010067
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9994 * 0.80100059
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74233 * 0.83222660
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67602 * 0.27190207
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30985 * 0.31742198
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25373 * 0.29952032
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83456 * 0.91635249
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1423 * 0.18263645
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51054 * 0.17404829
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17057 * 0.85478041
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63162 * 0.33721407
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82439 * 0.86129341
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3009 * 0.05551815
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28230 * 0.15432801
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64923 * 0.45990930
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22168 * 0.97594237
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17925 * 0.36063462
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18678 * 0.74306787
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84061 * 0.06400006
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16841 * 0.82457632
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15676 * 0.45972152
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14034 * 0.14808749
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'wmrqfebd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0024():
    """Extended test 24 for scheduler."""
    x_0 = 17567 * 0.61502485
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31760 * 0.68748098
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15847 * 0.19523130
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8116 * 0.08687047
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52481 * 0.25019400
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84959 * 0.10590994
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93591 * 0.06087119
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63878 * 0.05045190
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89451 * 0.35405625
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80116 * 0.75467622
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90794 * 0.65826186
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7962 * 0.18377999
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58189 * 0.44196847
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73864 * 0.81009607
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78559 * 0.98106387
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8198 * 0.84296327
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58813 * 0.72676032
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75623 * 0.04960385
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2189 * 0.96213755
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28948 * 0.18197727
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60025 * 0.49502855
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98596 * 0.42811663
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36349 * 0.31590130
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49652 * 0.74741703
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28360 * 0.88398239
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43195 * 0.68279645
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'scjypgix').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0025():
    """Extended test 25 for scheduler."""
    x_0 = 44988 * 0.22526395
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59172 * 0.50877835
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23479 * 0.98034414
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18180 * 0.07718237
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88641 * 0.68951449
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16209 * 0.13528392
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13593 * 0.30769688
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89299 * 0.61126962
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59145 * 0.53392627
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24622 * 0.04147677
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98757 * 0.53653163
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71600 * 0.33270945
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30206 * 0.21275059
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21917 * 0.23042940
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5923 * 0.36354199
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70490 * 0.19839727
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60496 * 0.47381827
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80708 * 0.53727629
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26604 * 0.22554974
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95479 * 0.02758514
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60877 * 0.17196431
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3955 * 0.93628750
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47834 * 0.37486449
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7177 * 0.39075518
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63237 * 0.25186320
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36626 * 0.02019987
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99127 * 0.23116134
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64478 * 0.63226622
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84866 * 0.38369598
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11905 * 0.55784187
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97127 * 0.87690504
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62211 * 0.98321372
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38166 * 0.12858873
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73736 * 0.70441118
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28023 * 0.53609740
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13216 * 0.24118227
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79479 * 0.83755507
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96966 * 0.28678271
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38942 * 0.01621626
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85416 * 0.50295762
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6359 * 0.62890209
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45735 * 0.92079009
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 94672 * 0.26356407
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82273 * 0.08371131
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xazgnync').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0026():
    """Extended test 26 for scheduler."""
    x_0 = 8935 * 0.97964589
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31271 * 0.95758678
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76855 * 0.29252895
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62395 * 0.75661678
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66986 * 0.90497233
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16045 * 0.16774013
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28483 * 0.68432032
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32124 * 0.73800104
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39363 * 0.06891535
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56343 * 0.07318347
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98716 * 0.49524346
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39978 * 0.67466560
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94712 * 0.62806897
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94081 * 0.42279054
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60730 * 0.05804679
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29722 * 0.56039017
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85315 * 0.93369760
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27994 * 0.07734297
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1997 * 0.07601853
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70616 * 0.78845204
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81574 * 0.30188591
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90231 * 0.87248447
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45569 * 0.14063669
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85662 * 0.79357843
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53269 * 0.31121493
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40250 * 0.51869744
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34934 * 0.68136961
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20179 * 0.68049395
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25827 * 0.57856650
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55221 * 0.58583485
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80096 * 0.27138205
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92861 * 0.50935013
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3747 * 0.02758941
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60707 * 0.96745755
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'dhgoxkde').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0027():
    """Extended test 27 for scheduler."""
    x_0 = 57942 * 0.94040204
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71231 * 0.54101238
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1507 * 0.35812313
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92550 * 0.46449940
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77335 * 0.66908724
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95546 * 0.79923671
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71969 * 0.92514151
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21398 * 0.16742918
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29176 * 0.51399112
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27172 * 0.74977031
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77686 * 0.08863610
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23031 * 0.77291343
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77978 * 0.94099093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32946 * 0.38322162
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38496 * 0.47375607
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78480 * 0.86163086
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65990 * 0.10907971
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56639 * 0.00454889
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75479 * 0.72027428
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40425 * 0.19499539
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45348 * 0.38882751
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70925 * 0.17260478
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6145 * 0.30429947
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61941 * 0.23310739
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4874 * 0.91378198
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90916 * 0.08068028
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10911 * 0.86794357
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17540 * 0.80230581
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24274 * 0.73566998
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99205 * 0.13773758
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43181 * 0.24391935
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13341 * 0.66144922
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39235 * 0.42080049
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68447 * 0.99625353
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'cxfmxsvn').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0028():
    """Extended test 28 for scheduler."""
    x_0 = 29622 * 0.73451479
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17440 * 0.40851045
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83539 * 0.21765145
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22146 * 0.39522267
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96377 * 0.83217620
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84257 * 0.88933561
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85103 * 0.24834653
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75792 * 0.65407182
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61578 * 0.71207856
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27379 * 0.36886486
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79312 * 0.61685900
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9535 * 0.47752740
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67433 * 0.41007142
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9890 * 0.82931584
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75250 * 0.46605032
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31946 * 0.27261054
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71523 * 0.20830044
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42165 * 0.63909496
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50830 * 0.72951390
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58515 * 0.07717470
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17178 * 0.67888300
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18870 * 0.47375299
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45348 * 0.71527787
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42826 * 0.23010674
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94286 * 0.70373661
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29601 * 0.60507693
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71626 * 0.76466632
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27739 * 0.62221330
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32203 * 0.77496810
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27341 * 0.09024563
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1036 * 0.44737269
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13696 * 0.47862291
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56561 * 0.64388283
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82285 * 0.55605636
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71889 * 0.05603354
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30312 * 0.93482837
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67447 * 0.89556894
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'rcgtohtv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0029():
    """Extended test 29 for scheduler."""
    x_0 = 49018 * 0.89199971
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8297 * 0.61907413
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57417 * 0.45792366
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29367 * 0.39445032
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20256 * 0.24906199
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55570 * 0.56941273
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7729 * 0.21262927
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30019 * 0.25021016
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46436 * 0.19972674
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53507 * 0.63304860
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24880 * 0.92975931
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13097 * 0.70450094
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93919 * 0.66491643
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33439 * 0.88704344
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82710 * 0.47864219
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46166 * 0.21514453
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49921 * 0.71993657
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32223 * 0.16826066
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53265 * 0.14286473
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4159 * 0.31745454
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2397 * 0.32974181
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45603 * 0.40858418
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93112 * 0.57311145
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9080 * 0.02573876
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23446 * 0.18215461
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94547 * 0.63802508
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29298 * 0.03540441
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6802 * 0.41478220
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'ecoezuad').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0030():
    """Extended test 30 for scheduler."""
    x_0 = 7799 * 0.70370484
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70856 * 0.06565917
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9214 * 0.60544034
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62212 * 0.68191748
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79264 * 0.67975012
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2564 * 0.23451369
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1605 * 0.17477566
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59972 * 0.58234588
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49536 * 0.56864435
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91779 * 0.93164751
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78144 * 0.93591241
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6282 * 0.84910700
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6071 * 0.79737185
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46238 * 0.43387466
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42943 * 0.86308189
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15343 * 0.07599477
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12724 * 0.79682799
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76022 * 0.35812273
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59005 * 0.73066129
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66361 * 0.92795986
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52547 * 0.32656931
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50632 * 0.78121096
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98894 * 0.29237731
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91772 * 0.31311293
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16896 * 0.75805033
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20487 * 0.08531204
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75660 * 0.13158649
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'eqpkzurn').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0031():
    """Extended test 31 for scheduler."""
    x_0 = 69254 * 0.91541645
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5087 * 0.28214436
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9916 * 0.84568870
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95008 * 0.45554809
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48528 * 0.70430799
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50609 * 0.32454516
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15127 * 0.76768862
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83177 * 0.91780762
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52896 * 0.59451948
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52168 * 0.09531397
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53215 * 0.15062818
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46476 * 0.64860306
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45092 * 0.04245487
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43764 * 0.53655698
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91960 * 0.96478927
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70321 * 0.31876005
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13945 * 0.92308158
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74026 * 0.31014019
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2182 * 0.33327815
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9675 * 0.11298432
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65038 * 0.36999925
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73171 * 0.11899363
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61867 * 0.70306565
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22136 * 0.08851051
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39347 * 0.13764942
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ggwkdoiq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0032():
    """Extended test 32 for scheduler."""
    x_0 = 43008 * 0.50476799
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81857 * 0.81287675
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52720 * 0.82298218
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88783 * 0.25054427
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90271 * 0.99585925
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95499 * 0.36357061
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46660 * 0.45620682
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10568 * 0.17831529
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85733 * 0.68534149
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24528 * 0.00444137
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62923 * 0.39461620
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12154 * 0.51439901
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47480 * 0.59278206
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93884 * 0.43158293
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49929 * 0.11317243
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77734 * 0.44472836
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18264 * 0.77850853
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87384 * 0.05604519
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26712 * 0.75017013
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43017 * 0.95152198
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65568 * 0.30865056
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6036 * 0.77755337
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 361 * 0.38072961
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4418 * 0.19034972
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40542 * 0.75158409
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37174 * 0.08199544
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33271 * 0.53279535
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13060 * 0.95020309
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38132 * 0.25110005
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80239 * 0.44342013
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52078 * 0.46268811
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83719 * 0.00148436
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47163 * 0.74274828
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51155 * 0.96759023
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4053 * 0.45059611
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15095 * 0.10449755
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46036 * 0.87589157
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6126 * 0.48749679
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'xacbitoo').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0033():
    """Extended test 33 for scheduler."""
    x_0 = 14328 * 0.37857153
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36372 * 0.05537860
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43782 * 0.45609523
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48233 * 0.60077024
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97601 * 0.06822341
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82242 * 0.65001767
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88401 * 0.70294849
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91699 * 0.79166423
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28074 * 0.09962245
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56542 * 0.17234361
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40961 * 0.97409529
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98069 * 0.88769282
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61999 * 0.83762698
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38350 * 0.51728184
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55649 * 0.22117706
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91640 * 0.97947187
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99499 * 0.95461796
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82830 * 0.29829446
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30746 * 0.68158030
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25688 * 0.38196331
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61910 * 0.46164962
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12718 * 0.42039376
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37628 * 0.28510323
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62319 * 0.94497514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10765 * 0.83190464
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56252 * 0.69436516
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26068 * 0.47597322
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14514 * 0.22831591
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63983 * 0.27890982
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4270 * 0.01241833
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30796 * 0.87420670
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30795 * 0.35942194
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59713 * 0.10655797
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1622 * 0.49587475
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67968 * 0.12954355
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12860 * 0.55127460
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84015 * 0.66463256
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63780 * 0.89081192
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98389 * 0.51796713
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'dkgxavdx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0034():
    """Extended test 34 for scheduler."""
    x_0 = 55406 * 0.21186536
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77318 * 0.04904436
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46355 * 0.53173841
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49123 * 0.61133301
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94848 * 0.79643910
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83730 * 0.63256905
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89311 * 0.95084441
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33778 * 0.46041177
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57097 * 0.93388503
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93432 * 0.62436426
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24118 * 0.72944597
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23022 * 0.48934297
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41658 * 0.75185080
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37692 * 0.62344788
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16540 * 0.51619011
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56724 * 0.89135656
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41663 * 0.20950171
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41119 * 0.29108676
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28794 * 0.13735640
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68479 * 0.11338807
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84393 * 0.64966994
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79108 * 0.65110703
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34423 * 0.16786420
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66383 * 0.84339127
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48974 * 0.82852992
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61634 * 0.05132445
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10514 * 0.16941516
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76570 * 0.54525274
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87408 * 0.39687536
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30879 * 0.37677595
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83935 * 0.59799854
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ctbnrogf').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0035():
    """Extended test 35 for scheduler."""
    x_0 = 32666 * 0.47071067
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22038 * 0.60807151
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94651 * 0.33498469
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50610 * 0.30838384
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94074 * 0.47697145
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82251 * 0.26064643
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38701 * 0.20728079
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51177 * 0.52561927
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45882 * 0.97704333
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82010 * 0.50525958
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37343 * 0.60597537
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11071 * 0.27612498
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12197 * 0.18867605
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89913 * 0.46153085
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44085 * 0.13041535
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28393 * 0.39620175
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75337 * 0.33517529
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57927 * 0.40506420
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51686 * 0.67272051
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50725 * 0.44165331
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5135 * 0.31368687
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90174 * 0.29323809
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56705 * 0.72340614
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45958 * 0.69081016
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31909 * 0.43933813
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44918 * 0.51640980
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51863 * 0.89072774
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73383 * 0.67142021
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14360 * 0.35418725
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34058 * 0.97052468
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24599 * 0.48425752
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44299 * 0.39699091
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22172 * 0.98815420
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 293 * 0.19951295
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72205 * 0.88178095
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94652 * 0.09730949
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70329 * 0.60030675
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71014 * 0.49639766
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75927 * 0.58157673
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75231 * 0.98715020
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17235 * 0.73598831
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 76578 * 0.29606903
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1918 * 0.37904752
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 62115 * 0.73353074
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'tsjywqne').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0036():
    """Extended test 36 for scheduler."""
    x_0 = 19140 * 0.99285886
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5807 * 0.26574449
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62565 * 0.63975792
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99570 * 0.50506485
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67221 * 0.22877642
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77757 * 0.05645486
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33145 * 0.98136624
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46878 * 0.12392343
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87201 * 0.01957607
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97043 * 0.21203814
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54995 * 0.23766420
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16539 * 0.89259551
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64933 * 0.52081669
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59631 * 0.42619920
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41391 * 0.86877905
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28043 * 0.71248057
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96946 * 0.94166973
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5737 * 0.73931568
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19090 * 0.30691982
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30437 * 0.86736982
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'bpgafbbw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0037():
    """Extended test 37 for scheduler."""
    x_0 = 60705 * 0.89961767
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 217 * 0.54787608
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33251 * 0.30624461
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48008 * 0.19078624
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38414 * 0.81099755
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61159 * 0.65967159
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75470 * 0.99879155
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45326 * 0.04459934
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49180 * 0.18579073
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6450 * 0.74305380
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82766 * 0.95713312
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63240 * 0.31502802
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3151 * 0.08709839
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63661 * 0.36443568
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55724 * 0.59174948
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98441 * 0.78131864
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25747 * 0.20574000
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51320 * 0.61317736
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83633 * 0.26420784
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76266 * 0.57698974
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71016 * 0.94802775
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'pidbbtyr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0038():
    """Extended test 38 for scheduler."""
    x_0 = 30046 * 0.10592492
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25741 * 0.22169994
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13528 * 0.11239729
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80571 * 0.89829447
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86557 * 0.93560769
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39913 * 0.79728969
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35224 * 0.68554908
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74817 * 0.16188209
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10204 * 0.89212221
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37212 * 0.77716266
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39127 * 0.17700947
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43285 * 0.12041222
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48081 * 0.95569007
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76330 * 0.36699410
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38334 * 0.76105824
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77835 * 0.99257334
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58116 * 0.60703391
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87934 * 0.68616235
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50641 * 0.46982531
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59062 * 0.19063249
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 658 * 0.33384691
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72162 * 0.82308049
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69191 * 0.26338352
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79170 * 0.04428761
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82574 * 0.28949629
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92068 * 0.49300383
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5914 * 0.12780716
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99452 * 0.62561529
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54200 * 0.35163814
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 144 * 0.78012876
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'xkgnvxtd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0039():
    """Extended test 39 for scheduler."""
    x_0 = 12974 * 0.25689614
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44499 * 0.18987924
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95033 * 0.69508732
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14799 * 0.11161184
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22418 * 0.68765425
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10762 * 0.01870671
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41321 * 0.56957751
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15239 * 0.48850865
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28251 * 0.48861861
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81921 * 0.47281790
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92705 * 0.51793350
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23585 * 0.51840202
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54717 * 0.74788043
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98776 * 0.57906818
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13561 * 0.80171368
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40547 * 0.20224864
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43735 * 0.01861092
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58552 * 0.46669829
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64594 * 0.89188115
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41497 * 0.05751613
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94293 * 0.65051447
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11320 * 0.08543036
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50900 * 0.31996065
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80573 * 0.30149646
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13804 * 0.38962818
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92749 * 0.09931721
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34092 * 0.32900930
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1474 * 0.10663641
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27856 * 0.90043506
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80550 * 0.76471970
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24961 * 0.07323839
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61827 * 0.23273991
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84212 * 0.95035260
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51842 * 0.20065082
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61649 * 0.99688744
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12622 * 0.34583527
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54560 * 0.46301472
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68237 * 0.63298495
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37308 * 0.39062408
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42652 * 0.00189692
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88639 * 0.62421965
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 8109 * 0.55346632
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 27538 * 0.60701327
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97807 * 0.13315388
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 22532 * 0.70267540
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 43896 * 0.06169337
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 64685 * 0.16874090
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 61302 * 0.58487103
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 1214 * 0.76709597
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 96068 * 0.05786751
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'mydxiwwv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0040():
    """Extended test 40 for scheduler."""
    x_0 = 25686 * 0.18970501
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53474 * 0.73652835
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60406 * 0.26941635
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21579 * 0.91165314
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34183 * 0.94539484
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6003 * 0.79839904
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36688 * 0.66690867
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27640 * 0.14363784
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74682 * 0.20248365
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25525 * 0.15538771
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69427 * 0.47539413
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86541 * 0.39487087
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56917 * 0.38705514
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17549 * 0.28980167
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48931 * 0.52228219
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20230 * 0.78729965
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13525 * 0.69213916
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3188 * 0.12369584
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99548 * 0.02053113
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87474 * 0.57788463
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49825 * 0.32334310
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85056 * 0.87305933
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59041 * 0.53580989
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58849 * 0.95770830
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75045 * 0.35078626
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94434 * 0.98461453
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33415 * 0.85806549
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51030 * 0.09191150
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22159 * 0.14863679
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18996 * 0.21854655
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65403 * 0.88087479
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76454 * 0.19489240
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30317 * 0.26455312
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38934 * 0.65633997
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11681 * 0.81621514
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87799 * 0.21673517
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2702 * 0.95363630
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40820 * 0.42768129
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67974 * 0.73794681
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 37278 * 0.07013735
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86036 * 0.34085941
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12040 * 0.13119579
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 84606 * 0.98378249
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'hgdvqved').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0041():
    """Extended test 41 for scheduler."""
    x_0 = 23600 * 0.81377220
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15289 * 0.92407374
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22658 * 0.78595464
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38178 * 0.89376313
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13685 * 0.88656055
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30436 * 0.81553410
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66201 * 0.98586242
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6592 * 0.33863738
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24581 * 0.29001044
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58342 * 0.74513567
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27689 * 0.61802835
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24707 * 0.17656811
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35828 * 0.97620912
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54411 * 0.45438269
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40903 * 0.92853577
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92562 * 0.33263121
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96425 * 0.17685354
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73374 * 0.01064296
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16171 * 0.48199590
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96529 * 0.70007132
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64573 * 0.71159830
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75180 * 0.11783453
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84569 * 0.46180539
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'umjsyqyz').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0042():
    """Extended test 42 for scheduler."""
    x_0 = 92892 * 0.60842982
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53671 * 0.14127483
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19087 * 0.03201102
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69898 * 0.67134663
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82830 * 0.45146818
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37438 * 0.69147518
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61689 * 0.09639956
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90394 * 0.85101546
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5872 * 0.98805308
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61473 * 0.49734348
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11189 * 0.28242106
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79143 * 0.38260543
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76412 * 0.99519548
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45820 * 0.12683577
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93186 * 0.12526927
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11001 * 0.71253204
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3158 * 0.04368864
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56088 * 0.57329573
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29507 * 0.69635670
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92370 * 0.58670392
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21215 * 0.44448724
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13788 * 0.15047189
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37593 * 0.06945613
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49063 * 0.58122601
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'momeobvc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0043():
    """Extended test 43 for scheduler."""
    x_0 = 50195 * 0.65009081
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5896 * 0.50084597
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32925 * 0.45045931
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37815 * 0.79700395
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3412 * 0.95876826
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90815 * 0.57530527
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51267 * 0.56677293
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93533 * 0.99347238
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56919 * 0.90874227
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15967 * 0.42141524
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70226 * 0.06676675
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2094 * 0.50386783
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29780 * 0.95705690
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42025 * 0.42226519
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58972 * 0.67207647
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60959 * 0.82447345
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63816 * 0.97703969
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34387 * 0.63123559
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49259 * 0.54103299
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99794 * 0.79525385
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71322 * 0.91778194
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25945 * 0.80080463
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48220 * 0.13690831
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8175 * 0.19728018
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'affpladr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0044():
    """Extended test 44 for scheduler."""
    x_0 = 39496 * 0.44969240
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48424 * 0.47597030
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62534 * 0.30000044
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72122 * 0.94440406
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4308 * 0.27887768
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32229 * 0.59500867
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97894 * 0.31983771
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79325 * 0.84363436
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82360 * 0.16163134
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62663 * 0.73115870
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42809 * 0.75236232
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36328 * 0.08631684
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89489 * 0.86437127
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2290 * 0.23066776
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8737 * 0.82105506
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90909 * 0.80204884
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73868 * 0.00134047
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23475 * 0.73548616
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33839 * 0.87222662
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40237 * 0.99008638
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57958 * 0.58354847
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61580 * 0.32286590
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89798 * 0.74829225
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ezmmhwtl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0045():
    """Extended test 45 for scheduler."""
    x_0 = 8903 * 0.58336021
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60252 * 0.19548069
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59717 * 0.04288869
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46403 * 0.89721354
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67212 * 0.56301766
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32732 * 0.59044664
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8550 * 0.03052892
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47518 * 0.61876856
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85585 * 0.92070681
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62265 * 0.74526761
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34037 * 0.73067808
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81113 * 0.94866728
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60656 * 0.91212369
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9716 * 0.12541102
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38742 * 0.09408305
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65233 * 0.23867780
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28507 * 0.70925648
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69430 * 0.98409789
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78825 * 0.32882401
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63227 * 0.57128982
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3257 * 0.72554261
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47759 * 0.21262011
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28588 * 0.23659762
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99285 * 0.33364086
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95741 * 0.44769669
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53704 * 0.44605772
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54135 * 0.56742926
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78613 * 0.06226165
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67723 * 0.65882245
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54684 * 0.86279826
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8801 * 0.62688422
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47188 * 0.11753959
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54997 * 0.91280884
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14550 * 0.92105773
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90515 * 0.10365028
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5940 * 0.89697087
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57093 * 0.55430410
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3334 * 0.94154901
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87359 * 0.12677521
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59242 * 0.80500875
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4007 * 0.39322337
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 24488 * 0.40225698
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20149 * 0.73571928
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11727 * 0.10529057
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'vcwstbrr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0046():
    """Extended test 46 for scheduler."""
    x_0 = 86785 * 0.04003906
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66248 * 0.21836996
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16974 * 0.52649890
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66842 * 0.52184135
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65095 * 0.50437153
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5904 * 0.14984972
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83285 * 0.12770274
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56502 * 0.64825473
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71132 * 0.35916467
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42182 * 0.12733908
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4024 * 0.28015210
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34664 * 0.11157980
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44831 * 0.69849366
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45539 * 0.89205665
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96528 * 0.52016064
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30831 * 0.07037823
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84529 * 0.41638733
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18335 * 0.73857117
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7820 * 0.53182108
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40709 * 0.11318698
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15189 * 0.76162558
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88937 * 0.10059568
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41658 * 0.01440028
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38930 * 0.49123846
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79630 * 0.36700034
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47871 * 0.84934282
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48480 * 0.21572113
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1652 * 0.48204427
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29078 * 0.18632742
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54117 * 0.37764531
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65743 * 0.76512584
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71809 * 0.49864496
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64632 * 0.65143367
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43764 * 0.76407101
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58321 * 0.25291151
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56200 * 0.92301095
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78873 * 0.22125998
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18357 * 0.50398940
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37100 * 0.57823776
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76913 * 0.52333936
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 57905 * 0.88076785
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22893 * 0.04829829
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20959 * 0.14524986
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'pnnjdcku').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0047():
    """Extended test 47 for scheduler."""
    x_0 = 47527 * 0.12677096
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72747 * 0.11214860
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75583 * 0.25287095
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85986 * 0.36514358
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98353 * 0.07100377
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64218 * 0.92991358
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5795 * 0.51029098
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1850 * 0.53875558
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26719 * 0.49998602
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13686 * 0.66604146
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66894 * 0.72806776
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53317 * 0.10262517
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17130 * 0.44663864
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55504 * 0.20003750
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34674 * 0.52662144
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18292 * 0.02926078
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39086 * 0.73641622
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37098 * 0.48843745
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24184 * 0.20506154
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67713 * 0.25433221
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56438 * 0.11685694
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44909 * 0.80220580
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42317 * 0.40481481
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'hmfmzkkg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0048():
    """Extended test 48 for scheduler."""
    x_0 = 54466 * 0.53849857
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80191 * 0.35549155
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40955 * 0.33083954
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81293 * 0.66185363
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80848 * 0.82384294
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76125 * 0.07815252
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81644 * 0.10335643
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94742 * 0.08928503
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34736 * 0.02743671
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82546 * 0.42581892
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52013 * 0.96475909
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51466 * 0.97078233
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28048 * 0.71938109
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51237 * 0.35981113
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50378 * 0.05897298
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89671 * 0.82871825
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44483 * 0.22630555
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61102 * 0.76585565
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8541 * 0.87209291
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45402 * 0.78439270
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43140 * 0.98430693
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21290 * 0.25080765
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50278 * 0.79865947
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23436 * 0.60040125
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46402 * 0.13336166
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28572 * 0.49654836
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99403 * 0.37863381
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42952 * 0.69234631
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48828 * 0.03017057
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16453 * 0.43409513
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91496 * 0.90463744
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64374 * 0.53613111
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40966 * 0.81895811
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17651 * 0.40964582
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21673 * 0.19882266
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54306 * 0.70947921
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49216 * 0.41890701
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33928 * 0.80897627
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42190 * 0.28250348
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 27791 * 0.57967750
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45026 * 0.01153319
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88975 * 0.98677170
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 51794 * 0.74872068
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 62555 * 0.99500545
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 22439 * 0.67198429
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 13198 * 0.75243847
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 89945 * 0.72703157
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 92752 * 0.44620240
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 74786 * 0.10697098
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 23123 * 0.26155931
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'utzbighh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0049():
    """Extended test 49 for scheduler."""
    x_0 = 92921 * 0.48296548
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9131 * 0.33508582
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98765 * 0.54973032
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57464 * 0.99875138
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55779 * 0.95076493
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80498 * 0.59586176
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9142 * 0.12185536
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74651 * 0.78919023
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10526 * 0.98428488
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55616 * 0.80229495
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18602 * 0.09677161
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4306 * 0.31099597
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83533 * 0.00268405
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65245 * 0.12389557
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77362 * 0.10950453
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84500 * 0.66785338
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96323 * 0.43062080
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8894 * 0.59714031
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84818 * 0.62201018
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45300 * 0.93138963
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'fiixmaqc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0050():
    """Extended test 50 for scheduler."""
    x_0 = 93925 * 0.68842488
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65708 * 0.66675604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10255 * 0.51769679
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 473 * 0.13981444
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90081 * 0.34968302
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39243 * 0.83696006
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91900 * 0.93260952
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67734 * 0.65245588
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9208 * 0.74540586
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22689 * 0.26959120
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33109 * 0.72440266
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44610 * 0.53542571
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41420 * 0.91164946
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66992 * 0.39770901
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24435 * 0.35871834
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61349 * 0.68179961
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63981 * 0.62145684
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61601 * 0.62141201
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83144 * 0.35945952
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90949 * 0.39987720
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36445 * 0.59741673
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46828 * 0.14792375
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67196 * 0.44208979
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99440 * 0.28444275
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25323 * 0.68389267
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1859 * 0.13432475
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11982 * 0.00477606
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74708 * 0.45873364
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51957 * 0.16095088
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96749 * 0.89702384
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88025 * 0.03701896
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7613 * 0.86224442
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39952 * 0.44478487
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49152 * 0.84933812
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26642 * 0.55111045
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51645 * 0.41968932
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'cmjjvdyh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0051():
    """Extended test 51 for scheduler."""
    x_0 = 89335 * 0.75734635
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43630 * 0.03128192
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89923 * 0.55456451
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96317 * 0.92553068
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92683 * 0.53664042
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19666 * 0.23616220
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48225 * 0.88142213
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14664 * 0.91425301
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35916 * 0.73388616
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31302 * 0.24662781
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61167 * 0.74942726
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2284 * 0.15541618
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81494 * 0.18300727
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15789 * 0.58701744
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40178 * 0.08807774
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12415 * 0.24733170
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40136 * 0.25057543
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21729 * 0.06091673
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89281 * 0.26040160
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63791 * 0.51405696
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15851 * 0.85649324
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21959 * 0.81795292
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63834 * 0.90915961
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88187 * 0.02798912
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61223 * 0.95561954
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79928 * 0.06184939
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62038 * 0.54575280
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81395 * 0.12738813
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30183 * 0.83393349
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14634 * 0.09228622
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59822 * 0.72944732
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87052 * 0.22923712
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24475 * 0.87556108
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68652 * 0.49662392
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'bvlrkjiz').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0052():
    """Extended test 52 for scheduler."""
    x_0 = 7858 * 0.95488762
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51160 * 0.78605161
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49931 * 0.22378122
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96830 * 0.62311542
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24844 * 0.23446705
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98664 * 0.26022880
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99212 * 0.87792223
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17846 * 0.03979212
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94011 * 0.82536227
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94230 * 0.97874008
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58012 * 0.95843671
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66714 * 0.50842028
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52459 * 0.47907118
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10671 * 0.78665319
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95888 * 0.64908339
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6941 * 0.02349782
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25749 * 0.70147467
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1010 * 0.68383815
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36746 * 0.43108415
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55566 * 0.78547334
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2874 * 0.16529785
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74643 * 0.02130155
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89105 * 0.52707719
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25951 * 0.46051004
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10504 * 0.95919534
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98541 * 0.20975623
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2591 * 0.50057846
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84013 * 0.66591939
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71498 * 0.80444795
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72093 * 0.66771837
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99671 * 0.22877149
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42615 * 0.34234877
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29017 * 0.18334771
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15489 * 0.59275315
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81176 * 0.14205125
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3404 * 0.03437828
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3385 * 0.51533359
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80948 * 0.96153642
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 68618 * 0.04889878
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52558 * 0.96474920
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'umwbjunl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0053():
    """Extended test 53 for scheduler."""
    x_0 = 40728 * 0.04569472
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97805 * 0.50862635
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90524 * 0.30007792
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23023 * 0.67094290
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52182 * 0.97592050
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7875 * 0.51699399
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54496 * 0.90644231
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86865 * 0.26802657
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80734 * 0.96659139
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71490 * 0.98141042
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25477 * 0.69734697
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23680 * 0.58767144
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37310 * 0.65287148
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50473 * 0.28897837
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41476 * 0.63585786
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39277 * 0.21434903
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4757 * 0.04354691
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39323 * 0.12180915
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10925 * 0.87227272
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65569 * 0.67380628
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68073 * 0.17519623
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85569 * 0.07433866
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18756 * 0.66380067
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1626 * 0.26870680
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69565 * 0.66904987
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83825 * 0.58301350
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4166 * 0.48156868
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91882 * 0.73566930
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2741 * 0.12902636
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31689 * 0.85539508
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81868 * 0.40193147
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39150 * 0.79092394
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42517 * 0.71058748
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53530 * 0.47738392
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5691 * 0.98668738
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32669 * 0.77840514
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47922 * 0.11218989
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59260 * 0.26038575
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77530 * 0.71358396
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62340 * 0.97909328
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74381 * 0.93659858
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39454 * 0.67570020
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 7836 * 0.23985615
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36114 * 0.02868002
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 57675 * 0.54688491
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 54685 * 0.07412715
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 29541 * 0.64578037
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 17644 * 0.19291924
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'jdwvraxj').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0054():
    """Extended test 54 for scheduler."""
    x_0 = 22610 * 0.06542707
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16511 * 0.16781308
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36091 * 0.75862974
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70208 * 0.52489128
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36464 * 0.76292802
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53513 * 0.69019751
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80302 * 0.66607356
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53765 * 0.19469796
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30787 * 0.80942064
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52974 * 0.97408222
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52422 * 0.23999547
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70952 * 0.95577598
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65026 * 0.85309222
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21994 * 0.96961551
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71021 * 0.65090976
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58865 * 0.53574813
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99339 * 0.09068514
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63635 * 0.98764821
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38619 * 0.85664838
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24968 * 0.70045108
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86969 * 0.03793971
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13664 * 0.33057117
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67770 * 0.63679613
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71811 * 0.93579201
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24729 * 0.06401043
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71057 * 0.84248539
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96187 * 0.44917674
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37016 * 0.67875547
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6802 * 0.19117889
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95202 * 0.68063061
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57537 * 0.74512444
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66950 * 0.83699607
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65167 * 0.34355767
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52288 * 0.53325413
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17935 * 0.01478800
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5532 * 0.86162587
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54589 * 0.03897742
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63868 * 0.61850259
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 85968 * 0.91566375
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22590 * 0.69583979
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77467 * 0.93133731
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82515 * 0.22573793
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 61813 * 0.12508433
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84964 * 0.58670211
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 69330 * 0.75894886
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 77320 * 0.07253722
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'ybxhiuon').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0055():
    """Extended test 55 for scheduler."""
    x_0 = 72207 * 0.18626503
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15636 * 0.90343136
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72024 * 0.80067031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26811 * 0.46666656
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46717 * 0.33801578
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17631 * 0.15247838
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32456 * 0.27863041
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42449 * 0.16430095
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57966 * 0.73223231
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44995 * 0.79450798
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84369 * 0.92156966
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10763 * 0.18678858
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90656 * 0.83568673
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23943 * 0.23599328
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52285 * 0.53451777
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57454 * 0.98025080
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37765 * 0.03372630
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97387 * 0.77654427
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79689 * 0.34863200
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63590 * 0.93159439
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27684 * 0.50725849
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44370 * 0.90853421
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85333 * 0.88614716
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40108 * 0.88857264
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91414 * 0.03006873
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'xkbxusny').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0056():
    """Extended test 56 for scheduler."""
    x_0 = 4017 * 0.01915141
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2033 * 0.87567058
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30078 * 0.65779211
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21853 * 0.03628610
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63959 * 0.99340872
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65522 * 0.93285022
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16683 * 0.83973242
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97084 * 0.95934212
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71234 * 0.74536012
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94010 * 0.29384731
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9928 * 0.16124923
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77484 * 0.02366907
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84749 * 0.11611996
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97762 * 0.22758157
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6711 * 0.34834921
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75614 * 0.64665693
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35434 * 0.86826465
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8162 * 0.05307635
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76562 * 0.48504815
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17505 * 0.42245380
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35049 * 0.62042192
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60599 * 0.53904112
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 566 * 0.01592628
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6935 * 0.12338149
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91113 * 0.92287710
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15522 * 0.68829353
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81201 * 0.27328990
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96344 * 0.77968122
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90449 * 0.66586759
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26634 * 0.35074823
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58237 * 0.77277888
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11732 * 0.16386455
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35128 * 0.16001284
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93011 * 0.69117821
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62322 * 0.94712188
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85061 * 0.61587360
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39831 * 0.67710454
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9408 * 0.73572842
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37414 * 0.52747873
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56880 * 0.69362268
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'pvcdmgcx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0057():
    """Extended test 57 for scheduler."""
    x_0 = 70050 * 0.90033182
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36434 * 0.77497828
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9494 * 0.76705671
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2233 * 0.39962307
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3029 * 0.19583682
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1930 * 0.19144520
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62646 * 0.22589728
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41438 * 0.52513737
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17360 * 0.99060551
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29277 * 0.23789081
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2517 * 0.31097471
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4501 * 0.16972227
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31919 * 0.97016552
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19132 * 0.96149673
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83740 * 0.46077793
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58543 * 0.69775407
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13214 * 0.02646986
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42848 * 0.21794042
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40883 * 0.49895651
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28041 * 0.42947558
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6729 * 0.60268858
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51864 * 0.92806739
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90001 * 0.61444457
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46910 * 0.62055467
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48594 * 0.34254265
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33206 * 0.77543946
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17498 * 0.80607070
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69778 * 0.61885438
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73640 * 0.10488988
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 650 * 0.75753207
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82344 * 0.97944223
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64042 * 0.46513600
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31838 * 0.87277697
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40222 * 0.99219591
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96007 * 0.22642171
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56993 * 0.56035352
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83224 * 0.20057089
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9948 * 0.28569793
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83833 * 0.96786556
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86516 * 0.13343979
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5555 * 0.47994066
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 597 * 0.39558071
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57748 * 0.52712641
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'gbtnkyfc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0058():
    """Extended test 58 for scheduler."""
    x_0 = 28291 * 0.12393112
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28372 * 0.00586829
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84619 * 0.72103380
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21962 * 0.32198001
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91659 * 0.51477112
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76469 * 0.72671699
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46592 * 0.98053269
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21499 * 0.47950121
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1631 * 0.93161423
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46691 * 0.55524662
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16768 * 0.13634500
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16042 * 0.94935654
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30257 * 0.75165804
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30127 * 0.53850533
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76280 * 0.63246357
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34822 * 0.21341231
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32948 * 0.98841471
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15954 * 0.24380867
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19252 * 0.12426385
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71441 * 0.87034981
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17573 * 0.84324331
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87500 * 0.95858050
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43295 * 0.06378076
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52417 * 0.41486588
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12028 * 0.09653735
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87480 * 0.03642912
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68463 * 0.92218036
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45091 * 0.67171545
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78167 * 0.29668481
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56433 * 0.35339733
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38044 * 0.57069280
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79050 * 0.58170292
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35834 * 0.67220193
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16301 * 0.19969561
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73487 * 0.66973458
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48963 * 0.90200185
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28763 * 0.67149483
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61463 * 0.17662127
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94820 * 0.27371779
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ajfzbjso').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0059():
    """Extended test 59 for scheduler."""
    x_0 = 61074 * 0.56917386
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93843 * 0.62286276
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79366 * 0.18059169
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85637 * 0.23599600
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57919 * 0.01905948
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68866 * 0.23103085
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71103 * 0.67134512
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95618 * 0.41113634
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62624 * 0.94561080
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68334 * 0.16466506
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53300 * 0.71422164
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65855 * 0.74817551
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25438 * 0.30753149
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28754 * 0.39816887
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34520 * 0.93893567
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97731 * 0.21274912
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67780 * 0.07922192
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91394 * 0.95177357
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23557 * 0.97584484
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53041 * 0.79183171
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20422 * 0.73931076
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58545 * 0.98256545
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30988 * 0.22296133
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96602 * 0.58388201
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92547 * 0.36756226
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37564 * 0.22592175
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48463 * 0.46950071
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84419 * 0.27592868
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49356 * 0.35060170
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'dejtlmsl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0060():
    """Extended test 60 for scheduler."""
    x_0 = 10898 * 0.85596485
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37811 * 0.20626446
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58863 * 0.71850886
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24803 * 0.36173942
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41891 * 0.64553880
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56705 * 0.81876627
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38411 * 0.33926925
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54730 * 0.55017610
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6546 * 0.10054051
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69207 * 0.44894500
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41485 * 0.41638925
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88514 * 0.56508625
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27795 * 0.80692947
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74937 * 0.19038372
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16952 * 0.67786360
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43767 * 0.90999359
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14958 * 0.51675403
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20352 * 0.32935574
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8937 * 0.71875261
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48910 * 0.17609584
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 292 * 0.56806216
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82123 * 0.87617694
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82918 * 0.34405908
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10385 * 0.35795458
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93371 * 0.37231413
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86254 * 0.64843299
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78009 * 0.43028347
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71597 * 0.74712342
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21845 * 0.19855686
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'gacoujbi').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0061():
    """Extended test 61 for scheduler."""
    x_0 = 38843 * 0.87075838
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45165 * 0.17979214
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50729 * 0.65749317
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76083 * 0.00939051
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96077 * 0.77235006
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15157 * 0.55741483
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98610 * 0.61566477
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83600 * 0.58262658
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27934 * 0.73009690
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38790 * 0.87952585
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78909 * 0.23090981
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68820 * 0.20087269
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54909 * 0.16906834
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94338 * 0.89001405
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61570 * 0.83394517
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63601 * 0.99477385
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 506 * 0.43795706
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62319 * 0.95024409
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94291 * 0.29555973
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30671 * 0.06445663
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7382 * 0.62747515
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78242 * 0.13122155
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6855 * 0.30353897
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44149 * 0.83702463
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80947 * 0.64354352
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 392 * 0.08415550
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97640 * 0.85370201
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23167 * 0.15594172
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58203 * 0.92576084
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89880 * 0.75249371
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57647 * 0.46265666
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70859 * 0.29202102
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63044 * 0.66986864
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68198 * 0.63568293
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66093 * 0.04574620
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89275 * 0.42069435
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71447 * 0.77555232
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53580 * 0.02388397
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41910 * 0.20446910
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97847 * 0.61539099
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'zsfaruxy').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0062():
    """Extended test 62 for scheduler."""
    x_0 = 28241 * 0.76304160
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11882 * 0.23895257
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18732 * 0.93973030
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58411 * 0.20632684
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67300 * 0.22500760
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41644 * 0.99794855
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15224 * 0.58471914
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16594 * 0.41454202
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41327 * 0.27239211
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85838 * 0.01085142
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9106 * 0.27066329
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38923 * 0.65999334
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43935 * 0.97029569
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7203 * 0.81432848
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17216 * 0.89996461
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63618 * 0.75387736
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45365 * 0.08060654
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3277 * 0.08055063
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64940 * 0.32187124
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94616 * 0.08276349
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92517 * 0.54805741
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21011 * 0.51559802
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73703 * 0.02608335
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71754 * 0.19634417
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18905 * 0.33794639
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'kgpvtjmx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0063():
    """Extended test 63 for scheduler."""
    x_0 = 81321 * 0.21626471
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42540 * 0.54820816
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32893 * 0.71200374
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86194 * 0.04838534
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49993 * 0.24643670
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67025 * 0.05031862
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87617 * 0.64643865
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84584 * 0.46029762
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10832 * 0.62754026
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54256 * 0.81303184
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4520 * 0.91056905
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57192 * 0.06506253
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51162 * 0.97577937
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42354 * 0.66654014
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20574 * 0.85426984
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 103 * 0.63307673
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53676 * 0.22235697
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8101 * 0.58788230
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82380 * 0.84721227
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67107 * 0.90567878
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20516 * 0.73369241
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49695 * 0.21623740
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18661 * 0.14951744
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79161 * 0.49975229
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94892 * 0.64548972
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76681 * 0.61353707
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72514 * 0.65356531
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90899 * 0.23567036
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35645 * 0.41749147
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7436 * 0.15726071
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94400 * 0.31753509
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2249 * 0.88783436
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49796 * 0.13306599
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52475 * 0.44830165
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81015 * 0.41470763
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82314 * 0.09523253
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78081 * 0.41836196
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8330 * 0.55111375
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93246 * 0.23226452
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33809 * 0.37363444
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 28087 * 0.06373082
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 11950 * 0.16437363
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'wdxtouhx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0064():
    """Extended test 64 for scheduler."""
    x_0 = 36670 * 0.96279141
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34620 * 0.48166523
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84804 * 0.00858969
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89234 * 0.88315228
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92361 * 0.65460617
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58342 * 0.55395586
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57443 * 0.13748016
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12478 * 0.25028429
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4249 * 0.82798652
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99453 * 0.83557319
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2218 * 0.00609898
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76449 * 0.28514483
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44509 * 0.78351867
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30126 * 0.47804428
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77979 * 0.80522726
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20978 * 0.68065422
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37692 * 0.24385562
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86175 * 0.63905937
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31716 * 0.59230058
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41078 * 0.38355412
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57166 * 0.34139699
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30540 * 0.82180475
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43530 * 0.11294368
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78856 * 0.34855126
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88165 * 0.82220607
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'elmrdgpl').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0065():
    """Extended test 65 for scheduler."""
    x_0 = 34341 * 0.96230569
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21654 * 0.06124559
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72607 * 0.79633639
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16106 * 0.15529624
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2158 * 0.78403559
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48077 * 0.49134397
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46615 * 0.22671229
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1865 * 0.81183274
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41929 * 0.71291713
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77417 * 0.92617140
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5981 * 0.70978074
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81960 * 0.98717230
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49059 * 0.30748454
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53577 * 0.50340139
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84987 * 0.95431805
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8454 * 0.86293654
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58445 * 0.26279862
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55466 * 0.56416070
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44674 * 0.00554165
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13410 * 0.41521011
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69831 * 0.56949043
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74200 * 0.31695914
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18901 * 0.03838839
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82708 * 0.71683748
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61310 * 0.85254968
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34948 * 0.91967742
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64237 * 0.19751360
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84083 * 0.44196715
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49407 * 0.97446158
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33857 * 0.19344075
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25420 * 0.52109876
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'lsnltlme').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0066():
    """Extended test 66 for scheduler."""
    x_0 = 14280 * 0.76114846
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82731 * 0.97643156
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64457 * 0.37568176
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10028 * 0.25690740
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79982 * 0.88680335
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72662 * 0.90701010
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1852 * 0.26562675
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24407 * 0.45267336
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69536 * 0.58441870
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76049 * 0.87930276
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82719 * 0.46173725
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21885 * 0.80353387
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36332 * 0.35635873
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87538 * 0.72015366
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16988 * 0.95025897
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86420 * 0.45309020
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39334 * 0.87965407
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24482 * 0.44647039
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10707 * 0.81584792
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35795 * 0.75368973
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32242 * 0.35975369
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38184 * 0.81576605
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85731 * 0.61291389
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33529 * 0.69806379
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25316 * 0.63038437
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68181 * 0.34516772
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77406 * 0.76399109
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18296 * 0.22118595
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36038 * 0.15754703
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40608 * 0.99086697
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97169 * 0.20088135
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35058 * 0.94867831
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9738 * 0.83601875
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69886 * 0.85419883
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24433 * 0.27197212
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7557 * 0.96449146
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51005 * 0.63103851
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1739 * 0.62427988
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35231 * 0.59918633
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9670 * 0.68472746
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85807 * 0.00583860
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4783 * 0.50759762
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96281 * 0.06045983
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 1836 * 0.00015665
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 37307 * 0.88583770
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 71266 * 0.37793494
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 36000 * 0.66474080
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 12311 * 0.50881728
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 583 * 0.16460588
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'hosbxyjc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0067():
    """Extended test 67 for scheduler."""
    x_0 = 4504 * 0.21270089
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51978 * 0.80738493
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97954 * 0.22558740
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33229 * 0.02447664
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65782 * 0.92728386
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81865 * 0.63098562
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99226 * 0.03740912
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19867 * 0.78008789
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87407 * 0.36270031
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13340 * 0.50185585
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56757 * 0.47737080
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88338 * 0.06304886
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20912 * 0.73728921
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1698 * 0.50762857
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20990 * 0.27890342
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84608 * 0.40071755
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89962 * 0.23731539
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30568 * 0.88030036
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26469 * 0.21101224
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40543 * 0.25609219
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22477 * 0.99387117
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97064 * 0.19069016
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50529 * 0.00867997
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95641 * 0.21910269
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57804 * 0.36072252
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1170 * 0.63045970
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92172 * 0.88894180
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26637 * 0.96226323
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24979 * 0.69042673
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67294 * 0.00209671
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'gisxcrzw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0068():
    """Extended test 68 for scheduler."""
    x_0 = 13400 * 0.65746623
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61069 * 0.93093579
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45424 * 0.89139574
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3704 * 0.67586876
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2657 * 0.31112065
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 670 * 0.28479759
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8768 * 0.79471610
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79327 * 0.44833789
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4175 * 0.94559248
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69167 * 0.22680030
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56366 * 0.44229758
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44499 * 0.71722006
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77082 * 0.47844749
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64785 * 0.29906637
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54921 * 0.57831891
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3032 * 0.49180996
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85270 * 0.63472111
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48382 * 0.27689176
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90437 * 0.32427906
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66846 * 0.45856054
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47913 * 0.65214521
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18631 * 0.47483172
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98886 * 0.99275351
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67347 * 0.65653948
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90161 * 0.25676418
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98475 * 0.49187177
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1397 * 0.38991961
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20923 * 0.39331773
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95586 * 0.30458283
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38834 * 0.41692303
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44270 * 0.03870037
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53477 * 0.03346714
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11335 * 0.45285790
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15218 * 0.20103035
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90425 * 0.17180120
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18923 * 0.74317705
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23103 * 0.58866211
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62363 * 0.56655693
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81421 * 0.88136453
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34991 * 0.00271388
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21229 * 0.73101240
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82544 * 0.65908536
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13150 * 0.05126611
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 54971 * 0.66478655
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 22424 * 0.17328063
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 52541 * 0.63640565
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 27770 * 0.19392314
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 6292 * 0.98047963
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'vzngtktw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_7_0069():
    """Extended test 69 for scheduler."""
    x_0 = 10247 * 0.83629525
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12681 * 0.57960707
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60804 * 0.89837460
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49899 * 0.61815905
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50012 * 0.88291333
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43070 * 0.14113918
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55506 * 0.80266007
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82869 * 0.44304982
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6690 * 0.11822418
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80257 * 0.44844137
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76514 * 0.53893808
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12544 * 0.41537860
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24388 * 0.84105888
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13406 * 0.72871341
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83926 * 0.11941201
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73518 * 0.20763382
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58971 * 0.37073950
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59977 * 0.49274937
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34763 * 0.15371042
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60237 * 0.79716459
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14985 * 0.70626930
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42115 * 0.39798327
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77081 * 0.73339369
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72649 * 0.75512458
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32396 * 0.86268456
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37005 * 0.53139220
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1023 * 0.05268366
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 183 * 0.88102679
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47878 * 0.63273253
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1522 * 0.37506066
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80627 * 0.16762979
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29302 * 0.94715933
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59260 * 0.22613487
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93324 * 0.03424507
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92172 * 0.65993062
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57369 * 0.90020758
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92036 * 0.90244750
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 14613 * 0.37607153
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 68503 * 0.29430829
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20374 * 0.05629736
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 26270 * 0.80652999
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 94597 * 0.33777327
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14924 * 0.16500018
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'cpldcpsj').hexdigest()
    assert len(h) == 64
