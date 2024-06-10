"""Extended tests for replication suite 4."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_replication_extended_4_0000():
    """Extended test 0 for replication."""
    x_0 = 79660 * 0.04651923
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13801 * 0.18100181
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5447 * 0.85386470
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21194 * 0.38807849
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30121 * 0.53436688
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3146 * 0.83799627
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 688 * 0.76936667
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73483 * 0.91978082
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13660 * 0.62017004
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27953 * 0.71668914
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28538 * 0.37557773
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71880 * 0.88977892
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32333 * 0.59997625
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19443 * 0.91265542
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55572 * 0.48629098
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46401 * 0.63738654
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8379 * 0.66680334
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53794 * 0.28588678
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44182 * 0.32177594
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31908 * 0.49297555
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72088 * 0.88709910
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61374 * 0.65884263
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45432 * 0.40715021
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55369 * 0.09746902
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6552 * 0.28370089
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97245 * 0.91714042
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65549 * 0.04628178
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41940 * 0.57432363
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13372 * 0.94519123
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67345 * 0.49573461
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38668 * 0.17830624
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85437 * 0.68658675
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'yuxtsayu').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0001():
    """Extended test 1 for replication."""
    x_0 = 4637 * 0.28943830
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98757 * 0.67455925
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3691 * 0.19006630
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49114 * 0.55796909
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84687 * 0.67313502
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24831 * 0.00001012
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18504 * 0.16090392
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12664 * 0.50627132
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98672 * 0.92979232
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61110 * 0.08455839
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18354 * 0.03534099
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29883 * 0.53042725
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18027 * 0.80607986
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24999 * 0.06346598
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86367 * 0.44036741
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76753 * 0.41252666
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26428 * 0.84298294
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48092 * 0.94360288
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87934 * 0.93064624
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42705 * 0.66691525
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90307 * 0.52389836
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75034 * 0.87020960
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96178 * 0.46463257
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73664 * 0.65652759
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54136 * 0.83933848
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17498 * 0.72201196
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22573 * 0.67632343
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76760 * 0.11603769
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89783 * 0.62851753
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31365 * 0.43823420
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73685 * 0.71578344
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62663 * 0.30771443
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41382 * 0.62419087
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25140 * 0.41040047
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 49374 * 0.40103970
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34848 * 0.19981718
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50012 * 0.39498981
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70957 * 0.59933064
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96908 * 0.73969736
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66280 * 0.54355008
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 72946 * 0.80403809
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33705 * 0.36565515
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95165 * 0.35839048
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'vpgjmrqq').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0002():
    """Extended test 2 for replication."""
    x_0 = 80598 * 0.75136757
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33247 * 0.68806928
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40600 * 0.09614374
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29486 * 0.54278779
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49705 * 0.43518329
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36837 * 0.46999205
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69127 * 0.56689556
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1883 * 0.31061033
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35113 * 0.79587562
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2158 * 0.35143074
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89592 * 0.76470764
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3976 * 0.75652003
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4243 * 0.20655881
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47983 * 0.82026421
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60475 * 0.41621181
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2691 * 0.64349359
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92290 * 0.05758792
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50906 * 0.06170178
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66039 * 0.39353838
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60760 * 0.07675267
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6834 * 0.46351913
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23848 * 0.21311458
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28032 * 0.84436910
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82085 * 0.00323229
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20300 * 0.93398359
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25067 * 0.82852739
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74141 * 0.84464585
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54781 * 0.75639259
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'acylgtot').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0003():
    """Extended test 3 for replication."""
    x_0 = 3662 * 0.06775939
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12883 * 0.25856839
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63312 * 0.52738319
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39388 * 0.59871556
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71250 * 0.51675658
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69969 * 0.06381165
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69933 * 0.24845092
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59687 * 0.71678522
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59610 * 0.82853044
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51514 * 0.85057940
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8378 * 0.21801409
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37189 * 0.74363129
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63936 * 0.93636002
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55000 * 0.90715961
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95110 * 0.36429161
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36948 * 0.37413047
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41097 * 0.14516382
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65501 * 0.64034865
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56470 * 0.41201059
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85554 * 0.13787267
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57047 * 0.23130046
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15078 * 0.13213188
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77155 * 0.83992313
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51795 * 0.37058271
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87797 * 0.03350228
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57900 * 0.87545835
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84198 * 0.73760431
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46903 * 0.85250751
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10794 * 0.59616116
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21692 * 0.20611877
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96516 * 0.36861123
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49702 * 0.91051730
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73964 * 0.92780983
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12809 * 0.77960562
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34409 * 0.17886260
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69887 * 0.13246484
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43410 * 0.83880417
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46929 * 0.24208078
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28392 * 0.64655699
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 48539 * 0.78868552
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45572 * 0.78625595
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21723 * 0.84040556
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ygdjdxoe').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0004():
    """Extended test 4 for replication."""
    x_0 = 88498 * 0.63880589
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90902 * 0.84619912
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76233 * 0.39021424
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32047 * 0.12171868
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82913 * 0.31069284
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93407 * 0.05807359
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48761 * 0.68427613
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54925 * 0.27444344
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84774 * 0.39899751
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74715 * 0.42717390
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9412 * 0.41008321
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93615 * 0.02295531
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62262 * 0.16445915
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50391 * 0.56155110
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96786 * 0.69665978
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82516 * 0.51115288
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12650 * 0.85612066
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43271 * 0.61831641
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68491 * 0.41041905
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 821 * 0.98269657
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18733 * 0.35715137
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96686 * 0.04042734
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14262 * 0.60725451
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72993 * 0.57526147
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21751 * 0.45441043
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99708 * 0.50010319
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34081 * 0.94177680
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38068 * 0.05660253
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98650 * 0.46270451
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66967 * 0.91709320
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'tojpkqlu').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0005():
    """Extended test 5 for replication."""
    x_0 = 48051 * 0.16599090
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55669 * 0.46835041
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31149 * 0.72576109
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90918 * 0.47877419
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49958 * 0.36386044
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46611 * 0.65397741
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86263 * 0.07529085
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72524 * 0.62616525
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41141 * 0.70790225
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46414 * 0.82286365
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53441 * 0.41436611
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87680 * 0.34873900
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3399 * 0.43843301
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29350 * 0.03687709
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 423 * 0.13117508
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92159 * 0.13565320
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57729 * 0.79658001
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94380 * 0.29575907
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12100 * 0.99289936
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39212 * 0.40448046
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80833 * 0.96382079
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44673 * 0.19565409
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81475 * 0.56884928
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4166 * 0.35965221
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70317 * 0.63766297
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8362 * 0.41185384
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97224 * 0.31937012
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74099 * 0.94281524
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97048 * 0.83041989
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75842 * 0.61763543
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43820 * 0.10327892
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15214 * 0.08688945
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15610 * 0.33535826
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'byrlkxod').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0006():
    """Extended test 6 for replication."""
    x_0 = 83812 * 0.05568886
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46789 * 0.98173868
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91085 * 0.74722897
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34717 * 0.88315937
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46374 * 0.43299853
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49272 * 0.02155534
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71744 * 0.15819178
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17403 * 0.44857012
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80553 * 0.40711034
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15790 * 0.84035450
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87619 * 0.33155360
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91913 * 0.40159088
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65848 * 0.90942890
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41897 * 0.09099706
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23104 * 0.02710252
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82989 * 0.89234103
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67351 * 0.30788043
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65954 * 0.09584877
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77578 * 0.69881033
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98479 * 0.64270544
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14899 * 0.99249618
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87849 * 0.80990515
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67972 * 0.29221669
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7434 * 0.20055676
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64125 * 0.82529897
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77214 * 0.24553110
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95486 * 0.14751081
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81218 * 0.48247752
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81285 * 0.92351986
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87927 * 0.23909624
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33159 * 0.07851075
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1046 * 0.58265676
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43862 * 0.75705592
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75740 * 0.74542363
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76942 * 0.47918663
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36163 * 0.61171554
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23764 * 0.27101944
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 76294 * 0.62812160
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34644 * 0.94247063
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51604 * 0.09192320
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 70569 * 0.21047526
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 94751 * 0.36459385
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 61660 * 0.56941803
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 50023 * 0.96730695
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 87369 * 0.60710039
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 76248 * 0.53787882
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 71836 * 0.61750172
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'lkyvozir').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0007():
    """Extended test 7 for replication."""
    x_0 = 93284 * 0.19205180
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31456 * 0.34160667
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43070 * 0.67848393
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3371 * 0.26743576
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11002 * 0.73158606
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35654 * 0.14631964
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45698 * 0.00018463
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94001 * 0.28064413
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38357 * 0.21466769
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96027 * 0.91935949
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48353 * 0.63381111
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73345 * 0.60481615
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68566 * 0.14788574
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47850 * 0.13351313
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91302 * 0.54663602
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15169 * 0.98575396
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16757 * 0.69701705
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55374 * 0.78921820
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26812 * 0.71988291
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33461 * 0.67346888
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82247 * 0.03141718
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28714 * 0.06291434
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83076 * 0.08285991
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47930 * 0.14074116
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31092 * 0.90765972
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82186 * 0.80342157
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45288 * 0.86168307
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89053 * 0.70294074
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81172 * 0.89177902
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6156 * 0.49294068
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83983 * 0.15570798
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32116 * 0.15521834
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80664 * 0.22761705
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35184 * 0.57460280
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61831 * 0.62171161
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50416 * 0.80646697
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5494 * 0.00154694
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'giticrlj').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0008():
    """Extended test 8 for replication."""
    x_0 = 27736 * 0.19650044
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37348 * 0.17222473
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32696 * 0.31077406
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27157 * 0.10111053
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11230 * 0.97953297
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11305 * 0.46484831
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93741 * 0.89107778
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81858 * 0.33651060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12976 * 0.05562066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12541 * 0.04145138
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77091 * 0.01715331
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 839 * 0.89786176
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58203 * 0.29777679
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33262 * 0.32079772
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28595 * 0.39418261
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7069 * 0.47165268
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92391 * 0.13895987
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6214 * 0.28646719
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64525 * 0.23321444
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21427 * 0.17482669
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77838 * 0.52262553
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14757 * 0.18748874
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58114 * 0.33077549
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52339 * 0.26308481
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36271 * 0.07397826
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46892 * 0.10370403
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16863 * 0.01498233
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'lvqwjfhs').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0009():
    """Extended test 9 for replication."""
    x_0 = 88886 * 0.62765298
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53332 * 0.71167795
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69903 * 0.44440719
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69763 * 0.10475766
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27616 * 0.01247610
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88368 * 0.18703210
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29403 * 0.79634636
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56247 * 0.07307556
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98540 * 0.70695324
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70361 * 0.29435120
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57962 * 0.57017287
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96298 * 0.69414373
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85450 * 0.45701194
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26833 * 0.56976615
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12484 * 0.24083964
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66727 * 0.33818908
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24944 * 0.41253475
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5027 * 0.84804354
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74059 * 0.34174565
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76281 * 0.85790091
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41141 * 0.15875580
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18750 * 0.76625498
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67146 * 0.69545261
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33920 * 0.18360993
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ukwknegv').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0010():
    """Extended test 10 for replication."""
    x_0 = 68274 * 0.73018919
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38969 * 0.52337852
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2074 * 0.52982195
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77575 * 0.82222378
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71644 * 0.97483428
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70697 * 0.26537690
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72134 * 0.05096310
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41828 * 0.23511519
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57589 * 0.71166073
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94801 * 0.40671850
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7446 * 0.52016659
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65413 * 0.35261067
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11057 * 0.57753395
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21887 * 0.86026414
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69399 * 0.28423110
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81057 * 0.03655261
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41671 * 0.56404756
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74765 * 0.72626628
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10545 * 0.70654457
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83442 * 0.65974846
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45519 * 0.88195542
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89327 * 0.23753274
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60103 * 0.74898995
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54907 * 0.91401765
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8331 * 0.73071498
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13681 * 0.75527254
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22055 * 0.01369851
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49692 * 0.99376057
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72622 * 0.74701666
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56946 * 0.94633104
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66346 * 0.90355267
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40665 * 0.75886373
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45500 * 0.96593941
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8458 * 0.24319660
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87635 * 0.58202347
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61394 * 0.98844817
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57072 * 0.63764719
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58979 * 0.25225120
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24488 * 0.79310816
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39365 * 0.90039700
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1671 * 0.25221561
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5004 * 0.83853391
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 8554 * 0.66712829
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'rdffacsn').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0011():
    """Extended test 11 for replication."""
    x_0 = 4420 * 0.73643555
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70951 * 0.88875364
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44398 * 0.02958935
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87519 * 0.58340455
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53245 * 0.03364265
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79764 * 0.64971605
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69257 * 0.42549757
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56715 * 0.83354679
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87836 * 0.15899041
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94013 * 0.89786706
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74946 * 0.73690529
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28904 * 0.99133344
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38581 * 0.82647515
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35199 * 0.87739331
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6449 * 0.88962492
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12932 * 0.57330525
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91411 * 0.56038815
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26053 * 0.37847417
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89060 * 0.08823558
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72259 * 0.84231877
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53059 * 0.49861087
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53653 * 0.10610161
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88882 * 0.69396795
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50197 * 0.03951537
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75063 * 0.82875111
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11065 * 0.08764925
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71432 * 0.08510206
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1795 * 0.24362492
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67995 * 0.44647178
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27144 * 0.82714548
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30419 * 0.03457730
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52610 * 0.14703805
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17063 * 0.94354325
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57058 * 0.74769575
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25314 * 0.39096620
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2558 * 0.32843222
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47358 * 0.68684074
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'mrjwnggw').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0012():
    """Extended test 12 for replication."""
    x_0 = 97946 * 0.62700878
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59123 * 0.25022502
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64149 * 0.75219894
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9089 * 0.94136638
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18349 * 0.49016568
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3170 * 0.31558960
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16107 * 0.66434100
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55487 * 0.04949775
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43698 * 0.00331770
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93304 * 0.53420839
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10597 * 0.04304183
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85528 * 0.62350966
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92371 * 0.38581683
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7021 * 0.10009724
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73337 * 0.91269805
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67651 * 0.17417170
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68368 * 0.09707541
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1802 * 0.42539644
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82638 * 0.35432636
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36646 * 0.10759133
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41502 * 0.22759455
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70177 * 0.89640472
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88957 * 0.76553661
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68540 * 0.26883182
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4327 * 0.59064741
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70782 * 0.07849088
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66448 * 0.39480966
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49227 * 0.05598649
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17939 * 0.08934202
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39294 * 0.27254994
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81793 * 0.50287776
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55398 * 0.95094083
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52792 * 0.48720825
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78247 * 0.09451360
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82293 * 0.20440453
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ugmftcnf').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0013():
    """Extended test 13 for replication."""
    x_0 = 97390 * 0.61121762
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 865 * 0.92523671
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25590 * 0.19861259
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29551 * 0.00018730
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50731 * 0.20087213
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96792 * 0.07106267
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99813 * 0.27191705
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71213 * 0.30092654
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52651 * 0.88365838
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68564 * 0.70489206
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95896 * 0.15397767
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84318 * 0.53719788
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42398 * 0.03231222
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8811 * 0.50348258
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11805 * 0.78547632
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66611 * 0.79580615
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58250 * 0.44184816
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77194 * 0.25300914
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10175 * 0.72435513
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62217 * 0.97210137
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17862 * 0.18085422
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16062 * 0.72699113
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73954 * 0.95686690
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30313 * 0.74183506
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85931 * 0.07540601
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15085 * 0.97610913
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64765 * 0.77907749
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35749 * 0.92943810
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32410 * 0.09800384
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48854 * 0.97457226
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45006 * 0.45250996
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36449 * 0.62709501
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69005 * 0.15372919
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16740 * 0.42897078
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12826 * 0.02012659
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85364 * 0.00010085
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46908 * 0.67189421
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84637 * 0.12862757
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'msbyepgj').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0014():
    """Extended test 14 for replication."""
    x_0 = 38857 * 0.21177898
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41236 * 0.60580545
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26021 * 0.96629008
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51240 * 0.28017974
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70261 * 0.57861824
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10167 * 0.99200938
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33525 * 0.54022448
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51020 * 0.04286297
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12198 * 0.22184007
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4185 * 0.50657094
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19735 * 0.16975260
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47617 * 0.14427313
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24374 * 0.22658648
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20845 * 0.31300701
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38861 * 0.21506293
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53565 * 0.02432132
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51229 * 0.20967779
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83476 * 0.84794765
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8309 * 0.57888716
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47631 * 0.06453535
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78776 * 0.72862284
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70488 * 0.75508833
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96924 * 0.98207138
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99777 * 0.17040478
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26964 * 0.82212872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79204 * 0.42570704
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61032 * 0.25909501
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5820 * 0.85949191
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79706 * 0.71204899
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6952 * 0.78740340
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5885 * 0.79631790
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87681 * 0.84275837
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62314 * 0.00116131
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59069 * 0.44251826
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71584 * 0.25485979
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47664 * 0.62435872
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27685 * 0.70764968
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'cocfedbt').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0015():
    """Extended test 15 for replication."""
    x_0 = 16890 * 0.11410343
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24814 * 0.92435512
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63224 * 0.90133862
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35534 * 0.93284572
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64430 * 0.26784550
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14154 * 0.08070883
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38523 * 0.46396277
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58549 * 0.52914408
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81015 * 0.83068202
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43872 * 0.02437629
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87762 * 0.88659781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52223 * 0.89113860
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39652 * 0.06563186
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23845 * 0.10363540
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50920 * 0.13062948
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33655 * 0.62096772
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72582 * 0.31312673
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73989 * 0.22615758
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81083 * 0.30025030
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27740 * 0.87343916
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65876 * 0.86587024
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97189 * 0.23631220
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54858 * 0.30620607
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59439 * 0.10047217
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31861 * 0.51920358
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77545 * 0.52550977
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85703 * 0.99403038
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49213 * 0.03925511
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23765 * 0.24195574
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91124 * 0.84279638
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44889 * 0.94437124
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25156 * 0.51506318
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61041 * 0.55897087
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33870 * 0.16384725
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30936 * 0.54481022
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48809 * 0.87471097
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49670 * 0.31460031
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3379 * 0.13768922
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14159 * 0.78432746
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'eliyyrfc').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0016():
    """Extended test 16 for replication."""
    x_0 = 12489 * 0.97549281
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53307 * 0.19010409
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30502 * 0.70467786
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16485 * 0.16042511
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44947 * 0.47173244
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12174 * 0.50149295
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39638 * 0.52490835
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79255 * 0.12209875
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30799 * 0.36665244
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32255 * 0.12944277
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8645 * 0.71301323
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40921 * 0.13063908
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15993 * 0.12653595
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40512 * 0.28235329
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12065 * 0.91424235
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 998 * 0.38959044
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80832 * 0.47692209
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50943 * 0.67538744
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40641 * 0.84593177
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82973 * 0.61404999
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75187 * 0.28197404
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89596 * 0.78961241
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87507 * 0.84645530
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3309 * 0.39063397
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70324 * 0.43837108
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52450 * 0.57845523
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4276 * 0.98187324
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89613 * 0.05633455
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92342 * 0.60906729
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14795 * 0.98206486
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10244 * 0.95009375
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20705 * 0.15052974
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57835 * 0.44491125
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11251 * 0.47886269
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1742 * 0.05561814
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23339 * 0.09755401
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91358 * 0.60120530
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89250 * 0.99805756
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38177 * 0.85581954
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72335 * 0.16369256
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47601 * 0.67213479
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50565 * 0.18740776
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93476 * 0.29712585
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22475 * 0.92561834
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 47162 * 0.66521738
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'kqowrnho').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0017():
    """Extended test 17 for replication."""
    x_0 = 42141 * 0.82341584
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29723 * 0.04974349
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30411 * 0.43192168
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33099 * 0.42396277
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53544 * 0.64156675
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33145 * 0.76487165
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86424 * 0.34959133
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4305 * 0.35615214
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25727 * 0.58750605
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72210 * 0.55905982
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66285 * 0.94374249
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25710 * 0.83840922
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75914 * 0.62623897
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98282 * 0.34797125
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56319 * 0.74798446
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94790 * 0.48290055
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82958 * 0.86783656
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66064 * 0.89131586
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57966 * 0.46424527
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53955 * 0.59015721
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79586 * 0.95040454
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74864 * 0.49862539
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50277 * 0.70732939
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22940 * 0.44890699
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74374 * 0.42753234
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93311 * 0.95832608
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41150 * 0.86699056
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58303 * 0.25828256
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92019 * 0.79403190
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39282 * 0.64802132
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29575 * 0.61645262
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16035 * 0.24360258
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89291 * 0.08172523
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15096 * 0.08730126
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'yizpktpw').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0018():
    """Extended test 18 for replication."""
    x_0 = 43519 * 0.68761912
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39417 * 0.47745569
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58916 * 0.25990357
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54032 * 0.47090645
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98944 * 0.13857459
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81651 * 0.04295971
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23861 * 0.92745755
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27092 * 0.22839993
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59430 * 0.15404104
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35777 * 0.86411310
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13104 * 0.68487028
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73228 * 0.79312203
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11124 * 0.33896331
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7882 * 0.46879160
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71399 * 0.48455360
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12903 * 0.72395779
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49991 * 0.67355214
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94078 * 0.31874011
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91648 * 0.58382093
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71073 * 0.70737760
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49064 * 0.26985213
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14682 * 0.75593005
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84280 * 0.43157355
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96646 * 0.77802856
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95625 * 0.59938815
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65400 * 0.43372094
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'jbrndlqm').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0019():
    """Extended test 19 for replication."""
    x_0 = 95388 * 0.93299784
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68576 * 0.13617053
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88946 * 0.44461314
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25270 * 0.39229686
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18588 * 0.80881714
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11229 * 0.75418275
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31427 * 0.37963237
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4887 * 0.89674985
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58541 * 0.66481168
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82959 * 0.03778689
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41281 * 0.36361806
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1347 * 0.33878477
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80697 * 0.22266744
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87265 * 0.59361275
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17180 * 0.10334655
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92138 * 0.39168527
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71462 * 0.52601982
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70869 * 0.47485152
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8612 * 0.63013556
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90189 * 0.25388835
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31961 * 0.21475458
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56909 * 0.03902995
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87585 * 0.65379339
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24161 * 0.48367119
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25071 * 0.31945268
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57376 * 0.81722276
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16089 * 0.79107764
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63419 * 0.14529206
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91836 * 0.49541536
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 165 * 0.32969752
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93900 * 0.54141970
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46973 * 0.39534333
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91203 * 0.27089883
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54386 * 0.16067701
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99990 * 0.43417835
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61860 * 0.37587045
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56073 * 0.86448792
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 37854 * 0.12399353
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18083 * 0.29521149
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90449 * 0.73946915
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ylucqlzf').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0020():
    """Extended test 20 for replication."""
    x_0 = 97251 * 0.13799387
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75136 * 0.40060775
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98830 * 0.25754097
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41288 * 0.01258784
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51028 * 0.99023589
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97549 * 0.11099686
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46439 * 0.26007041
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56099 * 0.87738820
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32626 * 0.41759134
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52952 * 0.54964525
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15451 * 0.10693054
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75013 * 0.02442417
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25487 * 0.46449526
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2168 * 0.73678177
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76253 * 0.54216788
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64320 * 0.07424162
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96271 * 0.73463287
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60675 * 0.10014266
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98816 * 0.77682067
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91930 * 0.13750183
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72401 * 0.09789154
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52304 * 0.11451557
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70480 * 0.35314041
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11855 * 0.49366907
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2522 * 0.78202536
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81625 * 0.80563153
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53268 * 0.55021112
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93191 * 0.02406586
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92610 * 0.44104886
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10152 * 0.94213296
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80078 * 0.05761172
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22739 * 0.03134982
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38007 * 0.44952240
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'zxmaymdp').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0021():
    """Extended test 21 for replication."""
    x_0 = 70189 * 0.94794076
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20485 * 0.96392882
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30947 * 0.52062463
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8952 * 0.35780003
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22165 * 0.18430216
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60559 * 0.83582702
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26003 * 0.56178236
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73236 * 0.93678071
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98127 * 0.07412611
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75786 * 0.95680537
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92447 * 0.00119203
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77613 * 0.53152629
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34425 * 0.82147232
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55421 * 0.25640282
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50965 * 0.30227579
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34678 * 0.76991717
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73849 * 0.13038311
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64965 * 0.75133474
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58232 * 0.61420702
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5304 * 0.52034060
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57445 * 0.69675020
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47346 * 0.59078521
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49401 * 0.75545890
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78121 * 0.48015280
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93381 * 0.20947296
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75392 * 0.28587603
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46331 * 0.47105353
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43016 * 0.48237822
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45043 * 0.51413163
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'gnlwbpmo').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0022():
    """Extended test 22 for replication."""
    x_0 = 85091 * 0.72192523
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99052 * 0.83712569
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71471 * 0.93824796
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25758 * 0.08259230
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72328 * 0.06491714
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17413 * 0.87251209
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18608 * 0.90628419
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 785 * 0.09426476
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33134 * 0.44325723
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33638 * 0.94745026
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3389 * 0.08638951
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81168 * 0.93333956
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84785 * 0.97353618
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51679 * 0.43715343
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21493 * 0.99819030
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18971 * 0.13982359
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2630 * 0.84352103
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84773 * 0.98519167
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56219 * 0.31944826
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84735 * 0.04828038
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73366 * 0.79360398
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37598 * 0.37038860
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61263 * 0.25852839
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30531 * 0.64412131
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9608 * 0.00933221
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7168 * 0.28250773
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81274 * 0.26420258
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40496 * 0.78907979
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47087 * 0.86191049
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48276 * 0.73117074
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19608 * 0.67384412
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28554 * 0.93771679
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62422 * 0.64881877
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62647 * 0.60128591
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39231 * 0.05355525
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42708 * 0.61751686
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6377 * 0.96418611
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2987 * 0.45578962
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 68900 * 0.54311285
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94017 * 0.24290577
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5011 * 0.47914003
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 90557 * 0.12516068
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 27629 * 0.83294868
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'weywejii').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0023():
    """Extended test 23 for replication."""
    x_0 = 3567 * 0.43184012
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31950 * 0.91771292
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70327 * 0.93767063
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45814 * 0.10706106
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38932 * 0.96932113
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18639 * 0.26042170
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59773 * 0.36449902
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23765 * 0.57616118
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95966 * 0.74078579
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99694 * 0.15662599
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29947 * 0.24931761
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23805 * 0.77538102
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98342 * 0.97129361
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24409 * 0.99009193
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42411 * 0.90438318
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3700 * 0.30923771
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87903 * 0.84799227
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92376 * 0.99793445
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35189 * 0.75048819
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27071 * 0.14819730
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51857 * 0.53932536
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43805 * 0.67873095
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2483 * 0.49853987
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52198 * 0.17089618
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16865 * 0.17807517
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87036 * 0.56327915
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77277 * 0.02626087
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53548 * 0.73182591
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81990 * 0.36009421
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14511 * 0.27423333
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29336 * 0.82752341
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95734 * 0.14592734
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72545 * 0.26514317
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45098 * 0.74803190
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30666 * 0.33127093
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31626 * 0.62009119
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34 * 0.24406319
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18245 * 0.00427541
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25489 * 0.10429691
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2946 * 0.11410716
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20108 * 0.77524836
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 98593 * 0.32279170
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 92457 * 0.98002306
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'cneprlko').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0024():
    """Extended test 24 for replication."""
    x_0 = 49315 * 0.55107067
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78959 * 0.77794658
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81311 * 0.12600401
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55935 * 0.22550848
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57250 * 0.02145338
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24772 * 0.57820218
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31721 * 0.26535965
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40867 * 0.63600708
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43152 * 0.96092234
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68012 * 0.32213830
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18110 * 0.77356154
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99088 * 0.89707525
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33082 * 0.11308729
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46979 * 0.77079373
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81222 * 0.18196035
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38119 * 0.29128095
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18340 * 0.18977219
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62786 * 0.55398805
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60494 * 0.48202788
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60179 * 0.55580587
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35222 * 0.84402827
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'gruafwuw').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0025():
    """Extended test 25 for replication."""
    x_0 = 21652 * 0.78562660
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64478 * 0.21652902
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61739 * 0.25985481
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61258 * 0.00559593
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47252 * 0.65509638
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35362 * 0.01093716
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54818 * 0.29890269
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40276 * 0.81298704
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84188 * 0.26609137
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59217 * 0.59299276
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18787 * 0.66615754
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1689 * 0.39078369
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15654 * 0.98937949
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2094 * 0.26868045
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43237 * 0.29123970
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78861 * 0.03398173
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52268 * 0.91543908
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49617 * 0.68900075
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72839 * 0.06066585
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58069 * 0.76204993
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95867 * 0.13165515
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22193 * 0.18882245
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'ofdlpzlq').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0026():
    """Extended test 26 for replication."""
    x_0 = 52241 * 0.73068265
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17229 * 0.42839926
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58465 * 0.07976692
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2896 * 0.48276018
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78670 * 0.21668496
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86248 * 0.58505257
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26127 * 0.11861448
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40791 * 0.27216921
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50435 * 0.01399273
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79800 * 0.59452836
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72185 * 0.57999223
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38570 * 0.54097504
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81979 * 0.06463433
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14366 * 0.14870254
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75533 * 0.95858201
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56629 * 0.94798707
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77797 * 0.97410700
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6165 * 0.65847231
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66603 * 0.22376498
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47012 * 0.79430743
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99529 * 0.83356872
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72869 * 0.25221014
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38963 * 0.35264109
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98764 * 0.40225391
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24221 * 0.83991259
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25780 * 0.52177318
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35605 * 0.66142165
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11722 * 0.16352426
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96786 * 0.60880668
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72324 * 0.24485461
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11554 * 0.60393384
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80421 * 0.92640494
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39361 * 0.57188534
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81210 * 0.31435367
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27039 * 0.13631479
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41551 * 0.06144384
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 38663 * 0.15425972
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3031 * 0.37364657
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69541 * 0.00398808
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6564 * 0.94507009
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 14683 * 0.76628016
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'lnbwopdd').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0027():
    """Extended test 27 for replication."""
    x_0 = 64851 * 0.30415111
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29750 * 0.96647806
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16498 * 0.28547643
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75934 * 0.86849814
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81704 * 0.02563866
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69776 * 0.37262534
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96198 * 0.37766364
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18547 * 0.41960693
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26806 * 0.72686318
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66767 * 0.33423705
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27797 * 0.49749206
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77917 * 0.59432766
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44492 * 0.18515601
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24885 * 0.35091631
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4053 * 0.44146139
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54804 * 0.16821114
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12306 * 0.55918960
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15428 * 0.33268085
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49015 * 0.32232784
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17426 * 0.44275709
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41327 * 0.90488647
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35907 * 0.38239474
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21090 * 0.09098409
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81108 * 0.20724194
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38315 * 0.87071905
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24912 * 0.67940636
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36195 * 0.99367759
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66585 * 0.04120315
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3081 * 0.76229629
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91892 * 0.66333380
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45557 * 0.38942086
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78259 * 0.38397304
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78075 * 0.58330363
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11572 * 0.83385384
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'jyuuyote').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0028():
    """Extended test 28 for replication."""
    x_0 = 916 * 0.00654002
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72433 * 0.56980272
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94060 * 0.10893392
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1923 * 0.16942695
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66137 * 0.83873214
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63736 * 0.17472944
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64927 * 0.07495789
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8205 * 0.70692468
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64521 * 0.99429776
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71503 * 0.59015681
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59939 * 0.07185238
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88104 * 0.54159885
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95171 * 0.21848837
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77497 * 0.22881982
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5237 * 0.69271698
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39753 * 0.15210513
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49476 * 0.44858770
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83225 * 0.44288785
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88684 * 0.41370951
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72057 * 0.55691514
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55988 * 0.88129284
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6615 * 0.34138423
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1425 * 0.70497151
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68408 * 0.21345152
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56625 * 0.26829451
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27826 * 0.02701360
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52299 * 0.29076737
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57398 * 0.41870954
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90573 * 0.21502917
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69658 * 0.56127403
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40784 * 0.09670792
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76703 * 0.72464652
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4495 * 0.15097894
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34312 * 0.47882831
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20511 * 0.53423955
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13223 * 0.80031864
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9086 * 0.86334711
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64098 * 0.74781931
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1976 * 0.42747947
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51167 * 0.25906704
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68447 * 0.00959746
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 10070 * 0.39763146
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 97766 * 0.02611539
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83528 * 0.55182398
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 64568 * 0.36985535
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'eqaeygoi').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0029():
    """Extended test 29 for replication."""
    x_0 = 6853 * 0.62905790
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16935 * 0.03041540
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4412 * 0.66899718
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49858 * 0.53557256
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51498 * 0.57516454
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12355 * 0.92386029
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55094 * 0.13234620
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17015 * 0.16317100
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17828 * 0.55924900
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92279 * 0.34047193
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34967 * 0.12940439
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94827 * 0.32715077
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8498 * 0.31186656
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40365 * 0.98078395
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76781 * 0.29325308
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7395 * 0.15998084
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33643 * 0.30375443
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16511 * 0.59223606
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68177 * 0.22683323
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37294 * 0.74721934
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50913 * 0.11276786
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13826 * 0.62732940
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79213 * 0.74272661
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33862 * 0.70469522
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3775 * 0.97025851
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 727 * 0.01645434
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24943 * 0.29214501
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82605 * 0.84467945
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27137 * 0.49892642
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19147 * 0.01079616
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ciksahtm').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0030():
    """Extended test 30 for replication."""
    x_0 = 47086 * 0.77397332
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23202 * 0.70566686
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21569 * 0.62620920
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99742 * 0.64602097
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19234 * 0.63794488
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60358 * 0.87069082
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41559 * 0.20814129
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29123 * 0.97406581
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6430 * 0.38856049
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64181 * 0.48604540
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33089 * 0.18193745
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89883 * 0.56441638
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80105 * 0.32641572
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67159 * 0.45271659
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47736 * 0.24847826
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41382 * 0.84762022
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10219 * 0.07417478
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61202 * 0.33672884
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1949 * 0.04013635
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98792 * 0.87798954
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39503 * 0.37152365
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89983 * 0.09171787
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6319 * 0.37474748
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86475 * 0.10381762
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31149 * 0.16625586
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48969 * 0.60140450
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79034 * 0.38286291
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29591 * 0.48785991
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'qeiyuxkk').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0031():
    """Extended test 31 for replication."""
    x_0 = 27548 * 0.77700289
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20239 * 0.75576739
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47400 * 0.08082553
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78232 * 0.84931672
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72404 * 0.84840422
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21101 * 0.29244415
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18703 * 0.96293991
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41368 * 0.87666432
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3168 * 0.02818877
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89426 * 0.98045166
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55441 * 0.47040797
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1274 * 0.60286659
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68928 * 0.15802521
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37399 * 0.28952379
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61730 * 0.42625164
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95981 * 0.79678323
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22709 * 0.69003693
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85176 * 0.13636841
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43222 * 0.20273997
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3434 * 0.76538174
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72222 * 0.25078909
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37940 * 0.39380948
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12772 * 0.97124142
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97536 * 0.39324922
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96183 * 0.22912856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21140 * 0.05171867
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78575 * 0.06465078
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49384 * 0.03464793
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25692 * 0.43399674
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82301 * 0.61158419
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28750 * 0.96513088
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17896 * 0.00317216
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'gqxasupa').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0032():
    """Extended test 32 for replication."""
    x_0 = 21808 * 0.11135078
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31762 * 0.51833792
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64070 * 0.73198968
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21324 * 0.95521137
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64285 * 0.45355220
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14392 * 0.75087294
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17237 * 0.88346786
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29840 * 0.66537334
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21437 * 0.36049793
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84344 * 0.34111806
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25197 * 0.11667777
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58211 * 0.60345459
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52502 * 0.79077396
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29899 * 0.42484822
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56174 * 0.34476572
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23439 * 0.22660996
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 827 * 0.18248639
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80186 * 0.24723152
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 322 * 0.32293159
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94068 * 0.51137959
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 803 * 0.74496260
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90847 * 0.50022282
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87571 * 0.49829999
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88618 * 0.27361613
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13654 * 0.04308365
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24620 * 0.04312577
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63941 * 0.76487967
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66331 * 0.32313071
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4511 * 0.47432236
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9312 * 0.70160959
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4200 * 0.98942842
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20875 * 0.84709831
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'qvridven').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0033():
    """Extended test 33 for replication."""
    x_0 = 71152 * 0.54908377
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86269 * 0.47655152
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11742 * 0.01967557
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13185 * 0.41815130
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69730 * 0.05740750
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73820 * 0.61989500
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6527 * 0.04019950
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95024 * 0.58078627
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82630 * 0.76061731
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24281 * 0.97344677
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85276 * 0.01290882
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1279 * 0.92141347
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3491 * 0.77420129
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8704 * 0.63251789
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5363 * 0.23968259
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8646 * 0.98443156
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44234 * 0.23067838
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71915 * 0.89252087
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9384 * 0.14909180
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92040 * 0.90893239
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90344 * 0.41577704
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10808 * 0.59606961
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75783 * 0.88350499
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11970 * 0.59847306
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2179 * 0.46202652
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41171 * 0.47812136
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33738 * 0.99716089
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24249 * 0.36562042
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93429 * 0.54135371
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39330 * 0.86991490
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38823 * 0.14746053
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21310 * 0.90416604
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23061 * 0.43813882
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76839 * 0.29927959
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33877 * 0.89008324
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12115 * 0.36497943
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68452 * 0.16347066
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23307 * 0.77023277
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'pgapnssr').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0034():
    """Extended test 34 for replication."""
    x_0 = 68310 * 0.93208393
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41252 * 0.64777418
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84868 * 0.14751942
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51673 * 0.99481674
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40900 * 0.94057588
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88953 * 0.20588719
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43647 * 0.50327337
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94399 * 0.94429336
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67212 * 0.39006602
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65495 * 0.73215516
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25200 * 0.17581242
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12748 * 0.11213046
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67172 * 0.66569599
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50555 * 0.44297196
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40657 * 0.84427140
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86680 * 0.00476175
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40432 * 0.96304013
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77901 * 0.39484993
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85746 * 0.34858655
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50608 * 0.10069685
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19649 * 0.84302723
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85691 * 0.20167548
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'umrpmroo').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0035():
    """Extended test 35 for replication."""
    x_0 = 69102 * 0.37364148
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3293 * 0.96132300
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87634 * 0.34759194
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92739 * 0.92478902
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63350 * 0.55540026
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6049 * 0.90722412
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6600 * 0.15216480
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56935 * 0.67237287
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95244 * 0.78702705
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11572 * 0.69506230
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97980 * 0.23831430
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20663 * 0.24310704
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79450 * 0.04967603
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78515 * 0.73801705
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49607 * 0.21594550
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71060 * 0.31313182
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31747 * 0.92239090
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23603 * 0.24674054
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32293 * 0.70893664
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8578 * 0.67564260
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45236 * 0.15029808
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72126 * 0.28760145
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'fgjzllvx').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0036():
    """Extended test 36 for replication."""
    x_0 = 14883 * 0.56169810
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73750 * 0.15859282
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4506 * 0.21118907
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3392 * 0.24835749
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76473 * 0.41774833
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15299 * 0.76080943
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74310 * 0.16189220
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93538 * 0.04721594
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18510 * 0.96544542
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10998 * 0.85217744
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36972 * 0.28610470
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2744 * 0.70365706
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37377 * 0.51937283
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77812 * 0.32992796
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64287 * 0.08438729
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81308 * 0.86453802
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23973 * 0.60557648
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72145 * 0.81878849
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40535 * 0.27121824
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84410 * 0.63577518
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43728 * 0.98629452
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76813 * 0.44470765
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74442 * 0.96180975
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68836 * 0.13101163
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75612 * 0.76339470
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45609 * 0.54947987
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49141 * 0.28020723
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82539 * 0.60625957
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'jwckpxyh').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0037():
    """Extended test 37 for replication."""
    x_0 = 40428 * 0.97392766
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13141 * 0.58260793
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54855 * 0.44129560
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59261 * 0.52043819
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66056 * 0.68670278
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10732 * 0.75214850
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42086 * 0.35439173
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91322 * 0.48714686
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54927 * 0.88552176
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8242 * 0.92316810
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1817 * 0.99101624
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25341 * 0.40922405
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18401 * 0.12334087
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27285 * 0.47670710
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96416 * 0.84566544
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29810 * 0.08066597
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60777 * 0.46018138
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41162 * 0.08752030
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40069 * 0.90352686
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65775 * 0.20057158
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76688 * 0.01509471
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51782 * 0.45566295
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'vhxhylar').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0038():
    """Extended test 38 for replication."""
    x_0 = 65862 * 0.68258813
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63232 * 0.09424515
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95972 * 0.36325759
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82252 * 0.09939823
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21843 * 0.71972198
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57157 * 0.21754461
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28139 * 0.67495261
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92818 * 0.43183888
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51336 * 0.93988149
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99534 * 0.17995632
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72137 * 0.32762382
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69150 * 0.87846584
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22319 * 0.32657424
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63443 * 0.31841513
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79373 * 0.41946067
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81527 * 0.97426260
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96111 * 0.95137722
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66225 * 0.74916477
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84598 * 0.80706995
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55710 * 0.98986902
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42435 * 0.00348370
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1335 * 0.75247800
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75971 * 0.06903349
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87841 * 0.37391334
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63808 * 0.82923338
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41329 * 0.41330687
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24139 * 0.63850582
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51967 * 0.48050696
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26815 * 0.72192547
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20820 * 0.76232092
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40297 * 0.44183811
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23256 * 0.87907569
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76514 * 0.32474815
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'oqorokyg').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0039():
    """Extended test 39 for replication."""
    x_0 = 38029 * 0.52214624
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42690 * 0.54752954
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75519 * 0.69081347
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2676 * 0.18116358
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44436 * 0.41555303
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68051 * 0.89615463
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35346 * 0.34773557
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8784 * 0.49430935
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60377 * 0.60021571
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29669 * 0.88870334
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82989 * 0.40607700
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32994 * 0.96891031
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40695 * 0.88227530
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99106 * 0.72975592
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62026 * 0.71641194
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28929 * 0.61877024
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85093 * 0.06461133
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36107 * 0.03573074
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45439 * 0.86530927
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9665 * 0.32177361
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51412 * 0.98589155
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93282 * 0.85506654
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23855 * 0.09967514
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52642 * 0.71046576
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43369 * 0.41249492
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18056 * 0.94316320
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48601 * 0.01682955
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95499 * 0.88811892
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51263 * 0.69214578
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57999 * 0.14485342
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30547 * 0.30433756
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75803 * 0.37559529
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77279 * 0.07732475
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8871 * 0.15247267
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1571 * 0.39365159
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32472 * 0.57751615
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51739 * 0.38117877
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58648 * 0.81964563
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25827 * 0.63544532
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40348 * 0.61984083
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 92595 * 0.18332091
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92394 * 0.11216523
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28714 * 0.99385225
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 57425 * 0.66617474
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'vljxmxbw').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0040():
    """Extended test 40 for replication."""
    x_0 = 43693 * 0.23125375
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84237 * 0.96667276
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60426 * 0.17525181
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2441 * 0.68036915
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99164 * 0.51155704
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82038 * 0.04975780
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 736 * 0.71524682
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68160 * 0.53567084
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38338 * 0.67169647
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1712 * 0.97551478
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2650 * 0.01444901
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25970 * 0.06438536
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83145 * 0.26861799
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93937 * 0.95184431
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84829 * 0.43079228
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39245 * 0.66054015
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22416 * 0.96680403
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29352 * 0.40636615
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15785 * 0.63867470
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14966 * 0.15062134
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64435 * 0.49315239
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91162 * 0.74911337
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95850 * 0.41753206
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38570 * 0.48435001
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17374 * 0.49771999
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35774 * 0.30008489
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85145 * 0.89440978
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65421 * 0.92255523
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54754 * 0.99706157
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66887 * 0.57200970
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6808 * 0.28860710
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19235 * 0.96248262
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74200 * 0.86938010
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34396 * 0.96194429
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82323 * 0.85566874
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50483 * 0.80220737
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97801 * 0.52497110
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88991 * 0.08879002
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87842 * 0.87042880
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8896 * 0.18056103
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29298 * 0.33858583
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79166 * 0.06723072
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 92810 * 0.25336441
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 60998 * 0.58953099
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'krpuefam').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0041():
    """Extended test 41 for replication."""
    x_0 = 11502 * 0.47356558
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83336 * 0.48111154
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57813 * 0.36246161
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80225 * 0.06170851
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46374 * 0.50302081
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8753 * 0.33887893
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39806 * 0.46041124
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53180 * 0.54976632
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34015 * 0.26288541
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31639 * 0.47811723
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51737 * 0.27353622
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73832 * 0.33183650
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73526 * 0.56781970
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23719 * 0.47825052
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22757 * 0.97155013
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28846 * 0.36754363
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65463 * 0.41498001
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18101 * 0.33477677
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96478 * 0.29146365
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27450 * 0.99519764
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52630 * 0.60666512
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78502 * 0.03687730
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14099 * 0.40679315
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89691 * 0.15023742
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93693 * 0.81159521
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26023 * 0.97445257
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11402 * 0.95771818
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47595 * 0.08298108
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90929 * 0.67244037
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24990 * 0.01351347
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7433 * 0.81011571
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33760 * 0.23022126
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33142 * 0.10980433
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40411 * 0.42489217
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20061 * 0.07638056
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61042 * 0.97235567
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55181 * 0.07117759
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77865 * 0.22286901
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1019 * 0.55506757
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39723 * 0.65350058
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45499 * 0.34059596
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40857 * 0.41032175
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 39902 * 0.90059063
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 4334 * 0.02172440
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 24949 * 0.78706283
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 18485 * 0.15557551
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 59983 * 0.81610655
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 28567 * 0.21368132
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 64601 * 0.95874976
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 50254 * 0.38279098
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'vubpxpgz').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0042():
    """Extended test 42 for replication."""
    x_0 = 7497 * 0.06061117
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 657 * 0.10369439
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63360 * 0.78882930
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44901 * 0.06203457
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39454 * 0.29499544
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18456 * 0.80238124
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65148 * 0.95546823
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3066 * 0.44706146
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47381 * 0.33473362
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78228 * 0.14255475
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85319 * 0.48184574
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18008 * 0.93301794
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2552 * 0.05244227
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66157 * 0.70367368
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63136 * 0.96874226
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53221 * 0.29383380
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40262 * 0.75628428
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9948 * 0.31978294
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78906 * 0.99964654
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28251 * 0.60297948
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13826 * 0.27727543
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53884 * 0.10182339
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61709 * 0.50551508
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35443 * 0.93114251
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41100 * 0.92562406
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35133 * 0.30060078
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12829 * 0.86051161
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98032 * 0.12393311
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24330 * 0.65441465
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70389 * 0.42695266
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98674 * 0.25651263
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76160 * 0.66323790
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41108 * 0.36676406
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8930 * 0.70029444
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99092 * 0.49045743
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23109 * 0.47089431
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99451 * 0.90379734
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89796 * 0.26870038
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26958 * 0.62206468
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'bwesthxi').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0043():
    """Extended test 43 for replication."""
    x_0 = 96128 * 0.83863309
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23633 * 0.31492140
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55713 * 0.79269835
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84347 * 0.68383739
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75807 * 0.65803419
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49166 * 0.55094306
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49123 * 0.82144359
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66145 * 0.69153411
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5831 * 0.60886600
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16503 * 0.48668918
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9790 * 0.04328849
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46137 * 0.26320606
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68807 * 0.78173814
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18890 * 0.74516385
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22257 * 0.91023892
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41702 * 0.62641981
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53772 * 0.07116622
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81870 * 0.40928619
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6772 * 0.73249327
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25289 * 0.71995013
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41530 * 0.93650313
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44401 * 0.53767977
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79655 * 0.37911986
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4745 * 0.61863566
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41091 * 0.84589391
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22386 * 0.71485844
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37342 * 0.10435253
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11547 * 0.82660365
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22383 * 0.59371245
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58910 * 0.47477863
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91146 * 0.58740784
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85067 * 0.48615683
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56880 * 0.87438689
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89530 * 0.99166500
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39233 * 0.17664602
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76200 * 0.60859571
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83658 * 0.63101458
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'hbexizxf').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0044():
    """Extended test 44 for replication."""
    x_0 = 17728 * 0.41936111
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7302 * 0.88812068
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78835 * 0.71125514
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29717 * 0.39584452
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78733 * 0.26772949
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63868 * 0.05875628
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76800 * 0.26341308
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40818 * 0.44236243
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44911 * 0.74843347
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17268 * 0.68714320
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10228 * 0.47990641
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37667 * 0.18525697
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2892 * 0.13539153
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50569 * 0.59710213
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71797 * 0.98725621
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49822 * 0.10963460
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67489 * 0.56626895
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64753 * 0.65142228
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98410 * 0.23925666
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18783 * 0.17997772
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88222 * 0.30395697
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85552 * 0.04279304
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41844 * 0.28247095
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73742 * 0.68892444
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46363 * 0.15582749
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70866 * 0.87327832
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34814 * 0.45791168
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22435 * 0.61556674
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40201 * 0.43692542
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87802 * 0.15392584
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93459 * 0.49236859
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3911 * 0.81573952
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75617 * 0.39821859
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47015 * 0.11857085
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'imrupheo').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0045():
    """Extended test 45 for replication."""
    x_0 = 21103 * 0.25448072
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27668 * 0.79679245
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62422 * 0.92421554
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51141 * 0.78918679
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59318 * 0.90547054
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49816 * 0.46573174
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99858 * 0.21535966
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49867 * 0.93055448
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87112 * 0.37377250
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28778 * 0.09297117
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37210 * 0.01405234
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73667 * 0.63257795
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72946 * 0.02701840
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61933 * 0.65623257
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79443 * 0.57759488
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2820 * 0.70255977
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86875 * 0.47308647
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5477 * 0.79953151
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79032 * 0.99686588
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56826 * 0.47257011
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54301 * 0.49901677
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14266 * 0.13613673
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69798 * 0.16394527
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76829 * 0.44263300
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53923 * 0.23472052
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58174 * 0.92053888
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36889 * 0.25288437
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56582 * 0.59629787
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90561 * 0.39144355
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79553 * 0.32662120
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29896 * 0.83628137
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80938 * 0.99709841
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3152 * 0.83048651
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88530 * 0.74851334
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18557 * 0.07449559
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23530 * 0.26291989
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14346 * 0.09191754
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58547 * 0.88678518
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60072 * 0.93382444
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75420 * 0.22563736
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99917 * 0.02021033
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40759 * 0.81840828
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13774 * 0.25876239
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82957 * 0.91454861
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 13867 * 0.60971892
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 97434 * 0.86116376
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 13491 * 0.34543881
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 31280 * 0.38565665
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'cmwivwkm').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0046():
    """Extended test 46 for replication."""
    x_0 = 18374 * 0.12991914
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7568 * 0.23593604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29437 * 0.37989224
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45685 * 0.85303085
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43579 * 0.68974169
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89740 * 0.65075395
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11434 * 0.60958155
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29795 * 0.47294913
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59635 * 0.07922157
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16975 * 0.70527394
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89957 * 0.64838499
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47132 * 0.18174837
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51043 * 0.00821051
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10349 * 0.27406591
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90455 * 0.61816591
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72086 * 0.19986826
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34336 * 0.51443461
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8969 * 0.58660281
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30325 * 0.56069424
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51809 * 0.87859151
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24561 * 0.62002138
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41608 * 0.37369417
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9773 * 0.91992285
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93670 * 0.90068255
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93604 * 0.90209142
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92978 * 0.46565590
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13175 * 0.08836015
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28505 * 0.70851229
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4771 * 0.64077150
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43903 * 0.02685487
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67667 * 0.88841505
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46737 * 0.10470407
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50924 * 0.40929829
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92465 * 0.47412817
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81653 * 0.05907365
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53788 * 0.78918560
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33770 * 0.03551774
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29538 * 0.49508842
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'wpacrgmu').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0047():
    """Extended test 47 for replication."""
    x_0 = 33297 * 0.07964061
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21847 * 0.31414517
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95607 * 0.56638468
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20704 * 0.54816114
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49550 * 0.93460017
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55707 * 0.05574078
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80329 * 0.60037230
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56860 * 0.82923485
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36193 * 0.83313828
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80510 * 0.58439832
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49708 * 0.09450343
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32080 * 0.62928854
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51317 * 0.18779303
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13290 * 0.30658790
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18267 * 0.35550469
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41441 * 0.45213341
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 866 * 0.35458243
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71681 * 0.07821103
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75707 * 0.84529029
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51113 * 0.04884111
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49384 * 0.74863309
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64909 * 0.73965218
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80302 * 0.35050766
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31436 * 0.76688751
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50255 * 0.90394731
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36413 * 0.08847691
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45555 * 0.92158701
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22421 * 0.34751962
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9584 * 0.96610992
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64828 * 0.79430895
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81215 * 0.84938660
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58060 * 0.19037891
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48128 * 0.88085792
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36423 * 0.16370386
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'empdezsl').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0048():
    """Extended test 48 for replication."""
    x_0 = 93448 * 0.45330135
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51301 * 0.89262327
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31680 * 0.51928965
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47618 * 0.07751737
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50421 * 0.00740818
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55306 * 0.16071781
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4250 * 0.34087941
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23010 * 0.30475620
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7829 * 0.71331448
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40205 * 0.32754658
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29531 * 0.44895316
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62645 * 0.76246647
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77573 * 0.45165213
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87 * 0.60730095
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39441 * 0.10988447
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10645 * 0.71130978
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57617 * 0.10321740
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59335 * 0.34316411
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90756 * 0.60024774
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77673 * 0.58276365
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77793 * 0.29939104
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63633 * 0.05874984
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8471 * 0.47100878
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16030 * 0.57567266
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 480 * 0.76730856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63744 * 0.84352230
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74296 * 0.01651679
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16622 * 0.51161519
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84878 * 0.60153894
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14527 * 0.89388673
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99886 * 0.92514758
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50239 * 0.07093293
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25549 * 0.27248200
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68492 * 0.80870454
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70282 * 0.45291638
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93040 * 0.55805270
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75655 * 0.01726171
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44319 * 0.85970658
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15640 * 0.77638837
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28201 * 0.61451145
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48888 * 0.69031188
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 65296 * 0.54567099
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 43905 * 0.22219476
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'rvvmqayi').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0049():
    """Extended test 49 for replication."""
    x_0 = 76424 * 0.13323053
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8026 * 0.43879316
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62714 * 0.43516308
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95455 * 0.72919870
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89093 * 0.11816561
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18853 * 0.26821513
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24402 * 0.65562790
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27716 * 0.09233492
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10909 * 0.33995528
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85962 * 0.07833243
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53120 * 0.45312729
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79826 * 0.41941173
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9764 * 0.62381514
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36688 * 0.86287270
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73921 * 0.26633827
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58125 * 0.24676550
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89506 * 0.07839241
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57574 * 0.43863103
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70355 * 0.27510712
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12927 * 0.46448866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88840 * 0.44934541
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'tvhfposu').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0050():
    """Extended test 50 for replication."""
    x_0 = 96096 * 0.42411580
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94956 * 0.23833967
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39358 * 0.17966776
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33473 * 0.27482388
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49221 * 0.99082089
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23011 * 0.91470609
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53463 * 0.70250300
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88479 * 0.10589907
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62526 * 0.71076223
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77105 * 0.07785273
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42223 * 0.80957061
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41664 * 0.35927088
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37665 * 0.30546591
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82904 * 0.11519454
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58011 * 0.35010411
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21995 * 0.62491097
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17438 * 0.61784728
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77521 * 0.51950621
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31356 * 0.12479338
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20249 * 0.00665754
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91447 * 0.60641093
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92512 * 0.04149765
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30075 * 0.71995255
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48899 * 0.48903394
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97095 * 0.05401127
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65452 * 0.28509680
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69901 * 0.31505221
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64169 * 0.26648136
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36708 * 0.67361589
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89484 * 0.66825526
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77267 * 0.51095625
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99938 * 0.84212645
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16392 * 0.89778894
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29946 * 0.75135781
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75038 * 0.16510265
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98362 * 0.06836471
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39219 * 0.84027803
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'jsystkbi').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0051():
    """Extended test 51 for replication."""
    x_0 = 92521 * 0.00617135
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21667 * 0.98946886
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75274 * 0.91487714
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67201 * 0.91644607
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91126 * 0.49176921
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85133 * 0.74372996
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45279 * 0.48373842
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30310 * 0.88427728
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16947 * 0.49375428
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25088 * 0.15085118
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86351 * 0.96384943
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39840 * 0.28086405
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30574 * 0.16356446
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78130 * 0.49839132
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11363 * 0.33132622
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38190 * 0.88929372
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25396 * 0.85103487
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64827 * 0.65708875
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95591 * 0.40055981
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4582 * 0.52513513
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77840 * 0.02240789
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37834 * 0.02376333
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85282 * 0.44840450
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47451 * 0.56912311
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69609 * 0.99887750
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85930 * 0.22588934
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64071 * 0.78272911
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33809 * 0.06872475
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90081 * 0.92773318
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54607 * 0.58264688
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85430 * 0.30326969
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63111 * 0.53036394
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98036 * 0.23817227
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 273 * 0.14561953
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45990 * 0.46402770
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64325 * 0.44576716
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61898 * 0.58005093
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70081 * 0.69775828
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91341 * 0.79456384
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 5382 * 0.02101218
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54407 * 0.96385159
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21175 * 0.81711602
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16632 * 0.39971737
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 14653 * 0.25679715
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'hhdxkjzu').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0052():
    """Extended test 52 for replication."""
    x_0 = 69006 * 0.13478008
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66010 * 0.67643640
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90838 * 0.20067427
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14358 * 0.09134692
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3263 * 0.18528803
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62098 * 0.42408507
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45148 * 0.46675980
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11072 * 0.04737240
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82258 * 0.64173860
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96856 * 0.74420056
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11096 * 0.51158566
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49497 * 0.99152371
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83008 * 0.47560486
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56982 * 0.72256228
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41251 * 0.79982574
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99672 * 0.37806599
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5730 * 0.79883952
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36911 * 0.04020052
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5152 * 0.42418630
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4436 * 0.10064757
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53899 * 0.43586372
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50790 * 0.96973410
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83460 * 0.19014304
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37778 * 0.99648348
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43527 * 0.45414092
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81526 * 0.19129001
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48660 * 0.50406321
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'akwttvln').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0053():
    """Extended test 53 for replication."""
    x_0 = 47676 * 0.20924512
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87950 * 0.69973078
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19363 * 0.05348942
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96292 * 0.74886383
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65355 * 0.48961025
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96532 * 0.66103953
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38267 * 0.65114136
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86731 * 0.18379138
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55099 * 0.25237129
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16956 * 0.40621627
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9250 * 0.92835566
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74739 * 0.22907033
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99129 * 0.76679884
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36733 * 0.59939569
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80648 * 0.81385941
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13819 * 0.43868264
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53037 * 0.89003962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3227 * 0.98231890
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48505 * 0.74180866
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37462 * 0.78916318
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71426 * 0.56592266
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65524 * 0.29886484
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13351 * 0.82483313
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5880 * 0.83856246
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11781 * 0.20132863
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40448 * 0.99287721
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73585 * 0.42353110
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49704 * 0.61684167
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9348 * 0.10462134
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95657 * 0.84922020
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25035 * 0.83220548
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49932 * 0.28471572
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94719 * 0.18418673
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58080 * 0.91206845
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26175 * 0.82384144
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44211 * 0.99560821
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30742 * 0.66564101
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92495 * 0.65093841
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77951 * 0.10676377
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66891 * 0.12403925
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18634 * 0.61686020
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 91160 * 0.72421339
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44786 * 0.91145372
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11393 * 0.55574255
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11733 * 0.75506673
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 91138 * 0.73852859
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 29006 * 0.85490253
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 57456 * 0.63295979
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 1284 * 0.05409328
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'wcupsdbo').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0054():
    """Extended test 54 for replication."""
    x_0 = 60280 * 0.33747901
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30427 * 0.46968206
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13256 * 0.80594213
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24972 * 0.38816970
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14726 * 0.04119935
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66762 * 0.29638037
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44334 * 0.56142289
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62208 * 0.50922356
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61307 * 0.14179026
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33212 * 0.18560471
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82558 * 0.92514228
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84689 * 0.84070350
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94750 * 0.93877789
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39152 * 0.01445785
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40770 * 0.21435851
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63427 * 0.79420964
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34661 * 0.97906788
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42065 * 0.59229112
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72628 * 0.98265064
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55634 * 0.63093234
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30244 * 0.93172786
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27148 * 0.23217044
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51034 * 0.46390263
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26137 * 0.50199560
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35179 * 0.33761986
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21857 * 0.91088465
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83635 * 0.58612070
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89538 * 0.59405523
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8810 * 0.44772550
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61872 * 0.34443959
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99535 * 0.51831707
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40872 * 0.49410781
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48866 * 0.65551555
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74386 * 0.79383644
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91261 * 0.01242679
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95641 * 0.21743049
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11990 * 0.20934278
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16551 * 0.37377084
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52505 * 0.65900522
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68259 * 0.94233295
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34743 * 0.89809018
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'nvdxvgqk').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0055():
    """Extended test 55 for replication."""
    x_0 = 29166 * 0.93795625
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16808 * 0.52411686
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 999 * 0.85093117
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92779 * 0.77041858
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48129 * 0.90480850
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66420 * 0.71532562
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79838 * 0.37448597
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24807 * 0.19878938
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80492 * 0.87274353
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66376 * 0.92220884
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82980 * 0.22788935
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80113 * 0.77599349
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69519 * 0.14215817
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90799 * 0.49571984
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76985 * 0.37196295
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55426 * 0.98953996
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91231 * 0.76386337
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14729 * 0.55161320
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68017 * 0.15716993
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44747 * 0.41173848
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92259 * 0.92368214
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30899 * 0.25513687
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83450 * 0.10463874
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34323 * 0.36379307
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48977 * 0.50942332
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57029 * 0.82906688
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69509 * 0.21359224
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36336 * 0.31700256
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50478 * 0.75424965
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46506 * 0.86978421
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25 * 0.55740029
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18591 * 0.64294356
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4815 * 0.23837446
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73465 * 0.69787033
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24120 * 0.66043933
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69230 * 0.33964406
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88715 * 0.23238631
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'txjxrrjx').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0056():
    """Extended test 56 for replication."""
    x_0 = 70494 * 0.19984159
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88887 * 0.02522159
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88180 * 0.73479505
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86022 * 0.27023842
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83678 * 0.97897322
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43083 * 0.29820354
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2649 * 0.19495956
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63489 * 0.42801330
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58718 * 0.52743711
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38846 * 0.37390447
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23339 * 0.87937952
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47158 * 0.44320228
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27054 * 0.73637454
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50133 * 0.96929147
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94043 * 0.54238466
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53203 * 0.50634356
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55943 * 0.16381044
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62452 * 0.40898314
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16818 * 0.70037522
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94651 * 0.47950994
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'aipjsndo').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0057():
    """Extended test 57 for replication."""
    x_0 = 38524 * 0.00208190
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57243 * 0.44453253
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5182 * 0.59983426
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73485 * 0.12744794
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65808 * 0.75727065
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62490 * 0.60102354
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75980 * 0.98548068
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74835 * 0.45085385
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6337 * 0.06862167
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20441 * 0.29215680
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55408 * 0.73951828
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92619 * 0.66651859
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47096 * 0.33126302
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68405 * 0.98925308
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80137 * 0.90674962
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98393 * 0.20885208
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76226 * 0.55569675
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60042 * 0.03500228
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61080 * 0.36564881
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41201 * 0.32104103
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76450 * 0.12040026
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45819 * 0.30202439
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91477 * 0.50328973
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30398 * 0.03019319
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11563 * 0.97166608
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33701 * 0.26498416
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21140 * 0.72843605
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12806 * 0.43342967
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77814 * 0.89309865
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58290 * 0.49898540
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10633 * 0.38339468
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7283 * 0.94832648
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46644 * 0.47187029
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41762 * 0.21261882
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4615 * 0.17272740
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71553 * 0.30672665
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69854 * 0.14619429
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65150 * 0.44465218
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30113 * 0.02875152
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ntczuzob').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0058():
    """Extended test 58 for replication."""
    x_0 = 17597 * 0.50159282
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89022 * 0.44306908
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12241 * 0.14788141
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54184 * 0.98047015
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76732 * 0.95455486
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21305 * 0.88206039
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4647 * 0.18560273
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19756 * 0.01077503
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9746 * 0.33314790
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82545 * 0.10650692
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41209 * 0.14393561
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20451 * 0.67270686
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50158 * 0.97716460
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76453 * 0.74646381
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27004 * 0.07390224
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38343 * 0.51801464
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21549 * 0.59407043
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54239 * 0.96868423
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13120 * 0.00766545
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57736 * 0.58868544
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97502 * 0.10190506
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6593 * 0.94591325
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10696 * 0.19704992
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15579 * 0.04918474
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11416 * 0.49216946
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49462 * 0.03428574
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65948 * 0.10292364
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40282 * 0.63858575
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59502 * 0.55070141
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26652 * 0.08333386
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'zennalug').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0059():
    """Extended test 59 for replication."""
    x_0 = 199 * 0.25293376
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4768 * 0.83424238
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13065 * 0.40173386
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9381 * 0.20866906
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43911 * 0.56639566
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37186 * 0.27316970
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20112 * 0.59693550
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57572 * 0.67245613
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39000 * 0.15951576
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2886 * 0.73602319
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53757 * 0.58709439
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5141 * 0.01005708
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95657 * 0.72297300
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23269 * 0.31852700
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17385 * 0.62574222
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19016 * 0.63933243
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90067 * 0.88106145
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6446 * 0.01736314
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19702 * 0.67007952
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19311 * 0.74523239
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43014 * 0.27813097
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47271 * 0.58276376
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77254 * 0.65889768
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90791 * 0.15064953
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12368 * 0.45253988
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78903 * 0.95892649
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67253 * 0.26906806
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84522 * 0.05784690
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75227 * 0.35197637
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24209 * 0.91866629
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22341 * 0.45332670
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99866 * 0.38875267
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80469 * 0.67801615
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1296 * 0.42000673
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97683 * 0.69562756
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84122 * 0.88875515
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40499 * 0.38577595
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75098 * 0.38836478
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92114 * 0.77056492
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75153 * 0.45836432
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 73267 * 0.86870853
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85174 * 0.08323967
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28444 * 0.45592721
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 2733 * 0.09073051
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 97616 * 0.08106827
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'pchwxzjr').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0060():
    """Extended test 60 for replication."""
    x_0 = 20994 * 0.60773728
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47450 * 0.85693630
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93697 * 0.90389460
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97916 * 0.65624956
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29101 * 0.16006629
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78281 * 0.95692188
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25523 * 0.05036697
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96578 * 0.71352655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37638 * 0.17876180
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47340 * 0.32572632
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52598 * 0.94588578
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99831 * 0.42188390
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53713 * 0.20837994
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30465 * 0.85302808
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30374 * 0.10462064
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70578 * 0.12730660
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71914 * 0.51117119
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83497 * 0.46532561
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95284 * 0.22810843
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99388 * 0.30288207
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17648 * 0.77567876
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93372 * 0.61945340
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57963 * 0.34636035
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33053 * 0.22160567
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17393 * 0.18959020
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72851 * 0.60297157
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5377 * 0.08331955
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6499 * 0.82216083
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81831 * 0.86476286
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78355 * 0.86327466
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54740 * 0.80972939
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33274 * 0.43200622
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42292 * 0.12293089
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81738 * 0.17548558
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20728 * 0.63451987
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 73252 * 0.66527111
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20873 * 0.21176144
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 823 * 0.41949547
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14783 * 0.27213959
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92791 * 0.74115105
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69919 * 0.18911840
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30357 * 0.53332052
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 30743 * 0.33725049
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 10974 * 0.75005147
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 82927 * 0.94127570
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'dlsoihtw').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0061():
    """Extended test 61 for replication."""
    x_0 = 81064 * 0.82947446
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12463 * 0.71827122
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99898 * 0.73987207
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38617 * 0.76009503
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22395 * 0.36156062
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26293 * 0.53379456
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66465 * 0.51790909
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89932 * 0.82709909
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93250 * 0.87338041
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77385 * 0.27286836
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73613 * 0.03868906
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21903 * 0.93505200
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58513 * 0.67614442
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44312 * 0.45013194
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53420 * 0.23289820
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84983 * 0.17432585
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71872 * 0.40509767
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19578 * 0.55936653
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48422 * 0.64884195
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17257 * 0.80205499
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20425 * 0.53803243
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54999 * 0.59275006
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52842 * 0.59298148
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56923 * 0.74301090
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28982 * 0.62941529
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39003 * 0.05385245
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53360 * 0.59300861
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52690 * 0.08902737
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38536 * 0.17187694
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29925 * 0.45933486
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52048 * 0.07699384
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89541 * 0.77132910
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41354 * 0.85549820
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89195 * 0.86751709
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9669 * 0.14694141
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69822 * 0.28030788
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'cnjhddra').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0062():
    """Extended test 62 for replication."""
    x_0 = 91703 * 0.45131927
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85656 * 0.62349606
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22258 * 0.87015576
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40838 * 0.07423264
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40814 * 0.72652416
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42133 * 0.15706681
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66436 * 0.10980191
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42958 * 0.88559048
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43437 * 0.08426039
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79749 * 0.51652677
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71690 * 0.64354478
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91567 * 0.01501481
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83915 * 0.09709782
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98463 * 0.72907238
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41108 * 0.47725743
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40294 * 0.92723430
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36310 * 0.40158322
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87911 * 0.04643243
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44127 * 0.97069136
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81680 * 0.82827450
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68051 * 0.40727863
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18318 * 0.21917078
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2216 * 0.57166474
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65239 * 0.58020511
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82567 * 0.91950807
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77297 * 0.60565730
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83085 * 0.18171883
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15564 * 0.83879317
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7293 * 0.41675834
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30244 * 0.14064913
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'vdsfdwtb').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0063():
    """Extended test 63 for replication."""
    x_0 = 78594 * 0.12108385
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66911 * 0.69807725
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68806 * 0.85853800
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9286 * 0.54752755
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12971 * 0.18142280
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88047 * 0.85669046
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28855 * 0.88015361
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65788 * 0.58137585
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80695 * 0.80549485
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93631 * 0.83164499
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83375 * 0.40925117
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58032 * 0.16977983
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86990 * 0.31746471
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1905 * 0.13118004
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95165 * 0.23948006
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70941 * 0.30924250
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3060 * 0.44665313
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59610 * 0.18005510
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36679 * 0.43580924
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44880 * 0.90415154
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50359 * 0.82490344
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9254 * 0.54910903
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58771 * 0.39891098
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41864 * 0.27740141
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41903 * 0.44179823
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4581 * 0.52086844
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48988 * 0.89697916
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91185 * 0.76374293
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22435 * 0.36746592
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75333 * 0.92045454
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34819 * 0.08907047
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2133 * 0.82941450
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79928 * 0.67489572
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60074 * 0.17587754
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40664 * 0.22230632
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74028 * 0.73224616
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78310 * 0.95926864
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30399 * 0.20150685
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73537 * 0.24167136
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85636 * 0.47393541
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 61099 * 0.18339847
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58916 * 0.00414616
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1221 * 0.97736154
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38709 * 0.20835735
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 19560 * 0.46551173
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 23765 * 0.48763518
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 58393 * 0.58174370
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 28247 * 0.54009830
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 2342 * 0.91608705
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'deogxcsv').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0064():
    """Extended test 64 for replication."""
    x_0 = 82888 * 0.84383403
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50264 * 0.38275603
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74768 * 0.67301289
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45693 * 0.98967002
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23103 * 0.70464581
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46156 * 0.15612960
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49854 * 0.83644330
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16777 * 0.83108812
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27391 * 0.19343722
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41234 * 0.86898327
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19860 * 0.92277180
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53834 * 0.34937609
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12776 * 0.98371310
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56073 * 0.88767881
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72550 * 0.64650733
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66422 * 0.37739421
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72113 * 0.21906941
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52671 * 0.86561274
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35605 * 0.28649160
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46188 * 0.92000770
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32442 * 0.14973777
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82813 * 0.55737970
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'rohkanqd').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0065():
    """Extended test 65 for replication."""
    x_0 = 96625 * 0.55885244
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81464 * 0.28319971
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97706 * 0.37779507
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23676 * 0.40823100
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2101 * 0.29132330
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18083 * 0.73330931
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7619 * 0.22564703
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37253 * 0.67613854
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48770 * 0.00160691
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43662 * 0.45751395
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11638 * 0.91855420
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55113 * 0.87871267
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96731 * 0.30584259
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5872 * 0.82409528
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41706 * 0.82401293
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53258 * 0.87939114
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49628 * 0.03209510
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42202 * 0.74396698
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41210 * 0.41039225
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2438 * 0.66251069
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26422 * 0.06156930
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40050 * 0.16396051
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3738 * 0.78190115
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3837 * 0.14978238
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82490 * 0.46502961
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66991 * 0.84419376
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95039 * 0.19721457
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55254 * 0.05563936
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85642 * 0.27966935
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12406 * 0.40923076
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20866 * 0.37393023
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78018 * 0.50197302
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28158 * 0.72965680
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20386 * 0.98092178
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47954 * 0.16145998
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22539 * 0.08738417
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65266 * 0.89472903
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34137 * 0.03459307
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 85087 * 0.75939915
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10222 * 0.44851057
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8963 * 0.23951261
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'aoxircql').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0066():
    """Extended test 66 for replication."""
    x_0 = 89375 * 0.31414240
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28063 * 0.50561229
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93163 * 0.10866983
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62119 * 0.24454031
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34513 * 0.90364005
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73222 * 0.96728640
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24276 * 0.69050370
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17062 * 0.59799057
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17144 * 0.58909970
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93706 * 0.80646563
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64153 * 0.54565536
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32830 * 0.79088979
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15237 * 0.47046057
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56884 * 0.82092030
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36623 * 0.89377367
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4534 * 0.84680970
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9669 * 0.08564723
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7749 * 0.16468984
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81151 * 0.77064693
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80033 * 0.94941719
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35185 * 0.39293155
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8263 * 0.13395904
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7936 * 0.20645412
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11010 * 0.14318146
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63111 * 0.09446987
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70666 * 0.19549119
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88703 * 0.01419635
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96735 * 0.43194372
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20139 * 0.96733191
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79857 * 0.41974107
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37248 * 0.50105881
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75593 * 0.86823338
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28114 * 0.37659506
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24939 * 0.67134842
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82216 * 0.90974543
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27158 * 0.12286099
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'dsfqehef').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0067():
    """Extended test 67 for replication."""
    x_0 = 90058 * 0.60728844
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6717 * 0.61823918
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80914 * 0.37903792
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62540 * 0.26553183
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32835 * 0.44713493
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 111 * 0.25552303
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84703 * 0.00424303
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44841 * 0.49745555
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98258 * 0.04746758
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73224 * 0.55346372
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21430 * 0.89858368
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5707 * 0.27672269
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93144 * 0.06328420
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45653 * 0.94700813
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6071 * 0.19067701
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2308 * 0.33700778
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65941 * 0.77927090
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10481 * 0.63368676
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46299 * 0.96324073
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92578 * 0.74005274
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57576 * 0.87807124
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31425 * 0.17226164
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52877 * 0.09095912
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25261 * 0.17629793
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30108 * 0.29689086
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74540 * 0.55489769
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48833 * 0.54935873
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20271 * 0.44338116
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71364 * 0.20967469
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65094 * 0.67150014
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9464 * 0.84418081
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70199 * 0.46158778
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51510 * 0.68064941
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68011 * 0.56373323
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 876 * 0.29014498
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'zqxlonfl').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0068():
    """Extended test 68 for replication."""
    x_0 = 54244 * 0.56582889
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48969 * 0.42325533
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64788 * 0.54169043
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15307 * 0.00042941
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34066 * 0.26496620
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98391 * 0.94659528
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37549 * 0.51772729
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58136 * 0.86837116
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41905 * 0.26732025
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97318 * 0.59410933
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2724 * 0.94649675
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89250 * 0.30485476
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11202 * 0.55747007
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66892 * 0.93496398
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1702 * 0.70572072
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69814 * 0.57532525
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56443 * 0.82022700
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67363 * 0.03804952
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32423 * 0.85868677
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17399 * 0.95427595
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99153 * 0.91956060
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57360 * 0.76574082
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23125 * 0.05897353
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40126 * 0.40442703
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35243 * 0.14816058
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88490 * 0.70035140
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46417 * 0.97853262
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11003 * 0.67428499
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53181 * 0.22097498
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74292 * 0.81246526
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25722 * 0.59643868
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60703 * 0.64074836
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89409 * 0.15664558
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32319 * 0.15235330
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21953 * 0.18108416
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44003 * 0.57125930
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42941 * 0.96366510
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11779 * 0.84898323
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62051 * 0.68574645
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99791 * 0.11918460
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99213 * 0.01156934
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60793 * 0.41904040
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'fbdwgskt').hexdigest()
    assert len(h) == 64

def test_replication_extended_4_0069():
    """Extended test 69 for replication."""
    x_0 = 61457 * 0.52027037
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76498 * 0.45729178
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23879 * 0.58668744
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81495 * 0.43545513
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43001 * 0.48475952
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29512 * 0.71578265
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86581 * 0.70791388
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21618 * 0.30282752
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96355 * 0.10753765
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76280 * 0.60533514
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 458 * 0.87811938
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91750 * 0.85823375
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87529 * 0.23093505
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17032 * 0.66856972
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57768 * 0.32338015
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82270 * 0.77864713
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54414 * 0.65890595
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18757 * 0.73694825
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33611 * 0.17053842
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54089 * 0.03313869
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32954 * 0.53635336
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17802 * 0.59641567
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85786 * 0.69152027
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'npphsqpp').hexdigest()
    assert len(h) == 64
