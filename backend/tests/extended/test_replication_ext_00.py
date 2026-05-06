"""Extended tests for replication suite 0."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_replication_extended_0_0000():
    """Extended test 0 for replication."""
    x_0 = 741 * 0.54484022
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81425 * 0.80040391
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49190 * 0.78014495
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95894 * 0.25242271
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22597 * 0.45990205
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97135 * 0.23799295
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 654 * 0.38837915
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53878 * 0.08531614
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27938 * 0.76867392
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54980 * 0.09075430
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76985 * 0.86959698
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5070 * 0.78834726
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73630 * 0.78990144
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14240 * 0.80124944
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82234 * 0.74304694
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48472 * 0.28491077
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19180 * 0.33455536
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4283 * 0.04957470
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81844 * 0.13731929
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47165 * 0.18036355
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33221 * 0.16438988
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48472 * 0.46503104
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20580 * 0.89913956
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14563 * 0.07836694
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47643 * 0.46189127
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15701 * 0.75995947
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40232 * 0.76360104
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52326 * 0.70140940
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61689 * 0.19553376
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78488 * 0.28076563
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47861 * 0.19710267
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82181 * 0.41579940
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82863 * 0.28243654
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67027 * 0.27050279
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30365 * 0.76129210
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38123 * 0.34239574
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36111 * 0.86274412
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83314 * 0.38952002
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 7341 * 0.57776648
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ddoylijj').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0001():
    """Extended test 1 for replication."""
    x_0 = 78425 * 0.00294390
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57557 * 0.78169033
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3957 * 0.53306662
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20961 * 0.42135250
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65414 * 0.71950834
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28821 * 0.63495078
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54973 * 0.32569368
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86718 * 0.98086367
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40495 * 0.09245708
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59796 * 0.31057130
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73685 * 0.41699913
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16889 * 0.77787075
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58742 * 0.27346498
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44194 * 0.62103947
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17364 * 0.16251587
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49015 * 0.20662120
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60391 * 0.01434957
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1264 * 0.37512220
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67242 * 0.34287540
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48756 * 0.78015092
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43159 * 0.02727777
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51797 * 0.75166515
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25888 * 0.05393021
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32756 * 0.25496747
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46392 * 0.44316787
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10078 * 0.34526959
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18922 * 0.95956390
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63834 * 0.50580682
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9725 * 0.99328896
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57500 * 0.19505429
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44082 * 0.73595630
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41682 * 0.25073862
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59987 * 0.13537283
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29059 * 0.09607911
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22765 * 0.32062374
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50827 * 0.80573269
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63520 * 0.15924196
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25347 * 0.99241489
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96028 * 0.63346395
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21730 * 0.30159237
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48275 * 0.77752143
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 75610 * 0.71953058
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 49646 * 0.47521304
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 14715 * 0.67919752
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 7447 * 0.21885162
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 61233 * 0.92243598
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 15357 * 0.13226357
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 43816 * 0.35708894
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'wvcgfuxq').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0002():
    """Extended test 2 for replication."""
    x_0 = 48742 * 0.04192122
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87626 * 0.38107797
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52909 * 0.16225745
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93605 * 0.16980209
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13147 * 0.88297675
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60431 * 0.87575047
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39250 * 0.05168708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72636 * 0.10239519
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64421 * 0.27474149
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2983 * 0.00209617
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28608 * 0.29110727
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12624 * 0.92639541
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99922 * 0.51447223
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80875 * 0.03563816
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57687 * 0.62445890
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86546 * 0.28985575
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25941 * 0.57928738
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10681 * 0.45328331
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85733 * 0.33303124
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37050 * 0.96922982
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21934 * 0.13090951
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82704 * 0.79084204
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93914 * 0.68390739
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6421 * 0.99950793
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41668 * 0.88612233
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44530 * 0.35678428
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8354 * 0.08559070
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20218 * 0.48842629
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12957 * 0.61955881
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19506 * 0.44723689
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96975 * 0.04154421
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41654 * 0.61147040
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88471 * 0.09450789
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69278 * 0.49724536
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'nkiyhdrf').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0003():
    """Extended test 3 for replication."""
    x_0 = 70189 * 0.51738520
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7907 * 0.00319037
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66865 * 0.27941111
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78714 * 0.58469378
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9183 * 0.88272528
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55439 * 0.20235584
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89847 * 0.28133620
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92065 * 0.63912826
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88339 * 0.90872911
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70773 * 0.27089887
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46422 * 0.81485327
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21226 * 0.06676590
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99718 * 0.15381921
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8634 * 0.43555518
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30870 * 0.10814290
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96511 * 0.17609646
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14039 * 0.62083983
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46678 * 0.18024093
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79301 * 0.50738812
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70929 * 0.03796474
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22793 * 0.97888492
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19659 * 0.94270588
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38397 * 0.15924614
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13263 * 0.04564971
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54269 * 0.54862869
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63457 * 0.26165975
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19039 * 0.43808962
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28054 * 0.42102190
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68053 * 0.39123754
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ugzenoic').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0004():
    """Extended test 4 for replication."""
    x_0 = 24709 * 0.61410350
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59430 * 0.13500554
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46965 * 0.76859923
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54456 * 0.93851994
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97463 * 0.84630923
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35672 * 0.03543907
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98550 * 0.56770042
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85169 * 0.69102851
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 906 * 0.91900076
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59790 * 0.06637879
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16720 * 0.35765275
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33574 * 0.27480154
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55243 * 0.22465003
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46902 * 0.42685756
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6804 * 0.31119475
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46376 * 0.43350873
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13506 * 0.34727934
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89194 * 0.39498367
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84775 * 0.19507407
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54804 * 0.82405182
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54929 * 0.81235085
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59365 * 0.70382455
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31830 * 0.63216886
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33403 * 0.95591492
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'iizbyvfi').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0005():
    """Extended test 5 for replication."""
    x_0 = 87832 * 0.97332194
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17316 * 0.94167276
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7811 * 0.50909951
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21003 * 0.43627026
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52497 * 0.67939515
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48405 * 0.44426921
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63826 * 0.09908204
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31490 * 0.09339249
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17274 * 0.69861544
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69649 * 0.97630455
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55599 * 0.75845049
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33951 * 0.04899625
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56408 * 0.58096363
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82598 * 0.74709006
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88129 * 0.55164984
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16285 * 0.69776770
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26405 * 0.95584461
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70565 * 0.74440993
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22644 * 0.84971246
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13743 * 0.44279900
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77666 * 0.84393267
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99803 * 0.90151387
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29653 * 0.07428338
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9202 * 0.50670980
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'qtqplqhh').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0006():
    """Extended test 6 for replication."""
    x_0 = 3203 * 0.88202856
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14247 * 0.26357511
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55234 * 0.35977528
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18799 * 0.26121107
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44156 * 0.23132910
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50983 * 0.55595078
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60075 * 0.19775938
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57274 * 0.44175789
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17507 * 0.34441357
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81609 * 0.27304091
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6859 * 0.15138431
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6777 * 0.48000123
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94766 * 0.34304040
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4269 * 0.80703758
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17369 * 0.74934836
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72086 * 0.60457325
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82355 * 0.23688443
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34095 * 0.60253439
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50628 * 0.22975743
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42204 * 0.33886899
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15138 * 0.59426722
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9203 * 0.56293934
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98563 * 0.05706309
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57960 * 0.78359545
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17792 * 0.83413563
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71136 * 0.38037031
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60319 * 0.32932034
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9395 * 0.80657375
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47025 * 0.34282969
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48816 * 0.88776119
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38876 * 0.10586681
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98529 * 0.87862623
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88683 * 0.88137217
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93503 * 0.16874663
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36110 * 0.99440817
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56469 * 0.72544552
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49162 * 0.59300479
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63230 * 0.62767825
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96310 * 0.16819700
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92544 * 0.64118646
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45066 * 0.55698328
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42849 * 0.46595240
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'lxcmqmbt').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0007():
    """Extended test 7 for replication."""
    x_0 = 9062 * 0.73274145
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7605 * 0.40104770
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92302 * 0.88019895
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52727 * 0.18638190
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73417 * 0.99274291
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89774 * 0.59620821
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13350 * 0.44284746
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14261 * 0.66910456
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56617 * 0.40240489
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34962 * 0.69758242
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61655 * 0.24620907
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37474 * 0.58287152
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71659 * 0.64651137
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77336 * 0.71673715
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79119 * 0.85158618
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99444 * 0.50634802
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34918 * 0.15750692
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74384 * 0.56796867
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88580 * 0.21788327
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31617 * 0.64115349
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96875 * 0.97247256
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10273 * 0.29010076
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76657 * 0.49722602
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81677 * 0.01170212
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60528 * 0.81246516
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55224 * 0.52141803
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36111 * 0.33665199
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81127 * 0.00545628
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66148 * 0.87226905
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75779 * 0.74709152
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7541 * 0.24680000
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66927 * 0.67338573
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48450 * 0.42535744
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74549 * 0.91633544
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76422 * 0.07823133
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67264 * 0.92528886
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6416 * 0.32202810
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15014 * 0.71846440
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25126 * 0.87527635
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29719 * 0.38733401
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 56045 * 0.57726741
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22909 * 0.82391063
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 97173 * 0.88318864
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 62364 * 0.49756023
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 37066 * 0.61034927
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 69313 * 0.59761716
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'drdogdbw').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0008():
    """Extended test 8 for replication."""
    x_0 = 10954 * 0.02763936
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7033 * 0.09161061
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99549 * 0.10413581
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20835 * 0.80958528
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27045 * 0.49954939
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76987 * 0.67512117
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87726 * 0.92935132
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7817 * 0.06336270
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90745 * 0.87889883
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89852 * 0.54146344
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88750 * 0.36820811
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35471 * 0.89123950
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28261 * 0.58777393
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20289 * 0.70454712
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91291 * 0.87356758
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93958 * 0.24053740
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48590 * 0.11304715
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8494 * 0.44168115
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33438 * 0.67593531
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6868 * 0.56233873
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11442 * 0.61956786
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87256 * 0.08248463
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5964 * 0.34255960
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18053 * 0.14492755
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45808 * 0.97853986
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'oaqiaqrd').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0009():
    """Extended test 9 for replication."""
    x_0 = 61230 * 0.31270443
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98431 * 0.83552010
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83549 * 0.48183116
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14641 * 0.89366876
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98029 * 0.67419204
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13250 * 0.21707351
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54667 * 0.43222003
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5375 * 0.91647586
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19841 * 0.54861513
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18366 * 0.37350253
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65530 * 0.19703893
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4686 * 0.47630816
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17562 * 0.70945521
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54371 * 0.03872884
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74532 * 0.36659745
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87702 * 0.45224819
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64681 * 0.87990798
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7432 * 0.30447078
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3041 * 0.13377781
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21636 * 0.56094826
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14399 * 0.04409129
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9254 * 0.15084502
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31427 * 0.48474517
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90415 * 0.60314946
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66648 * 0.30989229
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70233 * 0.52489890
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63410 * 0.42019761
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30422 * 0.79278445
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95535 * 0.92612322
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 805 * 0.63828710
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5839 * 0.99415145
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18923 * 0.46164366
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86167 * 0.08372972
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32611 * 0.81922621
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7609 * 0.71592953
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32610 * 0.94810203
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91812 * 0.63646281
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33339 * 0.53830795
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 95136 * 0.94269483
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ojhsixmp').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0010():
    """Extended test 10 for replication."""
    x_0 = 52363 * 0.23459879
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44477 * 0.49021148
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32467 * 0.73508453
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80302 * 0.43975211
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39842 * 0.85780412
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97556 * 0.37284352
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71297 * 0.16063934
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3645 * 0.26606451
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92487 * 0.81568983
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93322 * 0.65550516
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25562 * 0.88534582
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26260 * 0.43712778
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70602 * 0.36322726
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91254 * 0.30943994
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99134 * 0.24663359
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81549 * 0.36886938
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21212 * 0.75260416
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25785 * 0.26506670
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23477 * 0.39040645
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26176 * 0.38287794
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85855 * 0.13311626
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82333 * 0.60410393
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42117 * 0.48525586
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54059 * 0.15421030
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14414 * 0.86400553
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47784 * 0.87148601
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51900 * 0.86566642
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99882 * 0.58106525
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81016 * 0.92705179
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48180 * 0.83126484
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72793 * 0.98726809
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32858 * 0.52533413
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27581 * 0.83036844
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20597 * 0.67267588
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45323 * 0.48758930
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34869 * 0.58692741
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71930 * 0.22776355
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4027 * 0.66623817
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 85194 * 0.06806882
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31359 * 0.53171208
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68369 * 0.74855688
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 62987 * 0.32848873
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'fgqlmrcw').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0011():
    """Extended test 11 for replication."""
    x_0 = 39826 * 0.99097135
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80923 * 0.77144365
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29341 * 0.76503808
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69654 * 0.35206126
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6648 * 0.16246892
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60057 * 0.75596222
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95756 * 0.12607708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33697 * 0.92532844
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61956 * 0.04556481
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81797 * 0.85050686
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73710 * 0.06989334
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98145 * 0.06600733
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59167 * 0.67522871
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37763 * 0.42475715
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75723 * 0.42839731
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71379 * 0.84405473
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12134 * 0.11381051
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15747 * 0.78344589
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90639 * 0.90202265
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28299 * 0.01299550
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81431 * 0.39852678
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48247 * 0.56587575
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43004 * 0.54900179
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18785 * 0.43442906
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10649 * 0.53173052
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64740 * 0.89743067
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'llazxfoe').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0012():
    """Extended test 12 for replication."""
    x_0 = 70915 * 0.33043152
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20332 * 0.35935361
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75779 * 0.09155509
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14922 * 0.68171014
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21353 * 0.71364001
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57837 * 0.58563103
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73255 * 0.35112551
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66389 * 0.90087064
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52077 * 0.94296877
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94064 * 0.45518916
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93264 * 0.20627279
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79869 * 0.86470833
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91376 * 0.63797450
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94702 * 0.14402040
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1766 * 0.36895595
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37521 * 0.13678364
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94946 * 0.49967605
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97134 * 0.48917214
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35771 * 0.44874375
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23205 * 0.71587305
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1615 * 0.63282577
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78901 * 0.03911799
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15359 * 0.36198766
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28954 * 0.58399943
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40783 * 0.53872508
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84975 * 0.25931059
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72448 * 0.44268024
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ufarrikv').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0013():
    """Extended test 13 for replication."""
    x_0 = 69114 * 0.31096457
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89925 * 0.38832569
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82222 * 0.29884351
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82938 * 0.29843839
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69127 * 0.38414292
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54711 * 0.50983559
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52133 * 0.04515484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12644 * 0.14970828
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36043 * 0.14167441
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70281 * 0.43468488
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8677 * 0.35893164
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18210 * 0.66574144
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7744 * 0.60331548
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58269 * 0.97939569
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40977 * 0.52981344
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71331 * 0.53315677
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66910 * 0.31521505
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34150 * 0.70617304
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3776 * 0.89208805
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80739 * 0.51368293
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85847 * 0.19303119
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79412 * 0.41340754
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35274 * 0.33592280
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49783 * 0.63131714
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6370 * 0.77362586
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23460 * 0.71392551
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70178 * 0.39826837
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27207 * 0.83348259
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83562 * 0.90737161
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89066 * 0.50521242
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41793 * 0.05545230
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78710 * 0.41225902
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64750 * 0.54933889
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79144 * 0.32910744
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64222 * 0.11149895
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90210 * 0.13937853
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85367 * 0.87098066
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 99586 * 0.91463246
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40550 * 0.04293518
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62650 * 0.22221346
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ouzsbvow').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0014():
    """Extended test 14 for replication."""
    x_0 = 79887 * 0.16044922
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84234 * 0.60073899
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42929 * 0.95903399
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41649 * 0.45691989
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4123 * 0.80803101
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27665 * 0.46965042
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46312 * 0.79568281
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21720 * 0.35218422
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79357 * 0.04284207
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85220 * 0.82825492
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33743 * 0.66301877
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1287 * 0.63914893
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29821 * 0.78812089
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63140 * 0.58653289
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16297 * 0.57965011
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71386 * 0.00677225
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94702 * 0.96829247
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43238 * 0.50163671
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21603 * 0.86432961
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6658 * 0.91632563
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31248 * 0.06710786
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7310 * 0.74386253
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86848 * 0.04837391
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82186 * 0.29963765
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22458 * 0.98125995
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11539 * 0.57366866
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31532 * 0.79737252
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76710 * 0.38695740
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65619 * 0.51440005
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66653 * 0.92075835
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53352 * 0.67886466
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20909 * 0.75550962
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2812 * 0.70963587
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47977 * 0.81870327
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29168 * 0.28687466
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33506 * 0.55044812
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'qgudzgvv').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0015():
    """Extended test 15 for replication."""
    x_0 = 91477 * 0.05875712
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71107 * 0.73735138
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16506 * 0.88073363
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20639 * 0.14131655
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46847 * 0.28548836
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79208 * 0.54759924
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56618 * 0.57452020
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77307 * 0.16785320
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32520 * 0.95626957
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43461 * 0.05229161
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24978 * 0.63417450
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73651 * 0.91887737
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25820 * 0.55332402
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43877 * 0.53386274
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5855 * 0.76068876
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3722 * 0.29029923
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48557 * 0.02360422
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56991 * 0.92954166
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56338 * 0.82836906
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42264 * 0.04962141
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76285 * 0.46747749
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8306 * 0.94691169
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'yrizibxk').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0016():
    """Extended test 16 for replication."""
    x_0 = 24382 * 0.38969968
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97577 * 0.91122649
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3278 * 0.91652641
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48449 * 0.64766440
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57901 * 0.56244255
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76956 * 0.34306124
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50014 * 0.54668277
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35588 * 0.30030315
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33435 * 0.13608919
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25036 * 0.78266544
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92491 * 0.34178107
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49206 * 0.09302665
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50155 * 0.34289224
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29410 * 0.46069781
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60574 * 0.96594645
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80505 * 0.42289504
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53831 * 0.89798017
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71466 * 0.43433700
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99711 * 0.37824223
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73171 * 0.08446300
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50947 * 0.93740864
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53910 * 0.29556415
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82598 * 0.60583480
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1643 * 0.09633976
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'nhnsdgwv').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0017():
    """Extended test 17 for replication."""
    x_0 = 15189 * 0.36128916
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65544 * 0.64648837
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63258 * 0.03041906
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74160 * 0.76869220
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26899 * 0.18594473
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15942 * 0.65678628
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77345 * 0.40389087
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86391 * 0.39578890
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41991 * 0.97295376
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67105 * 0.96035489
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25147 * 0.87403911
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23027 * 0.35302327
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88837 * 0.38285443
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64632 * 0.91063073
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86678 * 0.70060952
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53426 * 0.51995825
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96046 * 0.82424723
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5820 * 0.92625687
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36960 * 0.89991401
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62196 * 0.96968813
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49582 * 0.36346237
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44339 * 0.54993437
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14976 * 0.85407944
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82384 * 0.53780593
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43214 * 0.65662957
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2852 * 0.14773188
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96204 * 0.18204597
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6102 * 0.33052695
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55328 * 0.78464617
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52988 * 0.81373526
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86276 * 0.54586605
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73788 * 0.34844978
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83112 * 0.22414519
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95677 * 0.68633787
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94823 * 0.30836739
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54636 * 0.40445122
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81303 * 0.53647067
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6627 * 0.82272887
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43390 * 0.24720734
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70261 * 0.05799211
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 56652 * 0.35373381
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93826 * 0.13332918
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 56740 * 0.52339865
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 5770 * 0.66432463
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 76361 * 0.89489786
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 77351 * 0.69422931
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 19443 * 0.75388506
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'svdrmdeh').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0018():
    """Extended test 18 for replication."""
    x_0 = 14160 * 0.92145233
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23741 * 0.50325108
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31736 * 0.12137648
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79693 * 0.44249396
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44307 * 0.07093944
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97415 * 0.56373274
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36661 * 0.76874804
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86104 * 0.84170369
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36525 * 0.55171222
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7542 * 0.91895089
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76118 * 0.24964948
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71365 * 0.38419562
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38224 * 0.44438714
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65068 * 0.85540989
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79793 * 0.04634208
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16969 * 0.76273252
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3112 * 0.71821064
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44916 * 0.77378967
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10291 * 0.28163217
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23318 * 0.38329239
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19292 * 0.53601511
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53244 * 0.86189489
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93866 * 0.73774128
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89655 * 0.21556193
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1525 * 0.42836883
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86434 * 0.75915761
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19648 * 0.41250775
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53287 * 0.57649386
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76399 * 0.86144052
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91050 * 0.98259693
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75864 * 0.82577415
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19822 * 0.22702109
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34616 * 0.24602744
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50376 * 0.95702873
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4543 * 0.37913042
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'uvrfffbg').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0019():
    """Extended test 19 for replication."""
    x_0 = 59236 * 0.91765019
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39519 * 0.63069183
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7451 * 0.49903708
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91821 * 0.81647411
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31664 * 0.06133752
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35164 * 0.86844229
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4027 * 0.21203298
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75833 * 0.32694743
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89007 * 0.79083851
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37571 * 0.12570186
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25256 * 0.90882630
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15090 * 0.79010457
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34653 * 0.42953223
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43336 * 0.25553503
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73113 * 0.03033008
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96083 * 0.31587084
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94723 * 0.97215080
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71944 * 0.59434433
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6785 * 0.67478311
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22486 * 0.33435620
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52361 * 0.34255800
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14679 * 0.41832975
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63651 * 0.56804377
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21569 * 0.19240825
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9940 * 0.85623179
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86762 * 0.83160402
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58227 * 0.52151994
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2495 * 0.30730246
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6491 * 0.79222719
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96501 * 0.38965699
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'bhncavxh').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0020():
    """Extended test 20 for replication."""
    x_0 = 61092 * 0.33414245
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64233 * 0.86056287
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43920 * 0.60632822
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37261 * 0.52519685
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68371 * 0.49465925
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58984 * 0.64764012
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82735 * 0.40739081
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80126 * 0.12014755
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20710 * 0.91750211
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8531 * 0.30553850
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15026 * 0.37760437
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75028 * 0.48559094
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8720 * 0.49631423
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17335 * 0.62216552
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4586 * 0.99711978
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9371 * 0.31437049
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81931 * 0.75457348
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20122 * 0.02500498
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10354 * 0.59662210
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92419 * 0.72697188
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31256 * 0.78726630
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30459 * 0.58117285
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91037 * 0.69136870
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88697 * 0.00595652
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82042 * 0.09817570
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88137 * 0.51169944
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48304 * 0.76340773
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14012 * 0.58470778
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64245 * 0.23505009
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16327 * 0.87915282
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33068 * 0.29358339
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16257 * 0.01839486
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15369 * 0.74445113
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76259 * 0.23305924
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27410 * 0.26602592
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86413 * 0.66002371
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67253 * 0.21548264
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29966 * 0.94859814
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40550 * 0.09545211
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30427 * 0.68908756
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 33085 * 0.49828827
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 68991 * 0.39783779
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47665 * 0.12436195
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97339 * 0.50596285
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 97884 * 0.52658664
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 17070 * 0.32640412
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 90006 * 0.99884338
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 8559 * 0.91303413
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 80579 * 0.69636435
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'rzubjayc').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0021():
    """Extended test 21 for replication."""
    x_0 = 91327 * 0.16813229
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40312 * 0.20029490
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97723 * 0.35580745
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73612 * 0.35820536
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96971 * 0.72368290
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99748 * 0.88092903
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82838 * 0.67490741
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40196 * 0.46868994
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65406 * 0.52906211
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88274 * 0.47694654
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9948 * 0.77581465
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6633 * 0.01972128
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81170 * 0.45540863
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98311 * 0.66135274
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41467 * 0.64324417
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68341 * 0.33313768
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39162 * 0.18832604
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71251 * 0.10789383
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41291 * 0.89102594
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33506 * 0.84604568
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41406 * 0.57410005
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14382 * 0.09250354
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34826 * 0.74436338
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37189 * 0.37331367
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79475 * 0.31076228
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96059 * 0.56265442
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2576 * 0.23780096
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98109 * 0.36164181
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18076 * 0.61002865
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5946 * 0.23349490
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14501 * 0.78041707
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95300 * 0.78313810
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59733 * 0.56002859
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73001 * 0.98186738
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82206 * 0.77832719
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20370 * 0.31343485
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3364 * 0.05255236
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46315 * 0.05304656
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27725 * 0.08150713
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98124 * 0.66576531
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'zbahduui').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0022():
    """Extended test 22 for replication."""
    x_0 = 58050 * 0.98244373
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76093 * 0.55977511
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82073 * 0.30517414
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23774 * 0.72252999
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11712 * 0.07954769
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33242 * 0.49050634
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44651 * 0.52243534
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80291 * 0.92681871
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62347 * 0.51444477
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90217 * 0.24290871
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33800 * 0.65963686
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10280 * 0.76963784
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21072 * 0.74644174
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62639 * 0.90096502
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43904 * 0.54100807
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99775 * 0.18231247
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27412 * 0.79392757
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40053 * 0.47677519
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19192 * 0.21538273
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33197 * 0.88132817
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81560 * 0.36133855
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83329 * 0.70520014
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31380 * 0.55034540
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49745 * 0.73573559
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77403 * 0.51222511
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46324 * 0.93496042
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31746 * 0.13128262
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74054 * 0.88145218
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57468 * 0.84506918
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50046 * 0.03560975
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33014 * 0.98642286
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'obiqmbkw').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0023():
    """Extended test 23 for replication."""
    x_0 = 97140 * 0.73014292
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93804 * 0.41445029
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78319 * 0.71393501
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92288 * 0.99677634
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47920 * 0.82650574
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85993 * 0.19628456
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88600 * 0.03731390
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37753 * 0.10120581
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 846 * 0.57539467
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57766 * 0.15981754
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70324 * 0.42869179
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33194 * 0.85729127
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56070 * 0.50695121
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38168 * 0.59053946
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78854 * 0.34797515
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1381 * 0.28103211
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70610 * 0.25474273
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98774 * 0.58850418
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35303 * 0.33319498
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60366 * 0.16318683
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38620 * 0.24632626
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4849 * 0.70695254
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72865 * 0.90861138
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8902 * 0.80320842
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22338 * 0.21086408
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35822 * 0.28062028
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18366 * 0.91079970
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75452 * 0.16699884
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31787 * 0.82195936
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40930 * 0.33792638
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34687 * 0.04782501
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96361 * 0.76338192
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52529 * 0.19573484
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3904 * 0.01384553
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68971 * 0.48890925
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75071 * 0.10160059
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64535 * 0.26221172
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95344 * 0.94028682
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 7031 * 0.69160842
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86935 * 0.23935627
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ujaphdet').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0024():
    """Extended test 24 for replication."""
    x_0 = 65078 * 0.62137320
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43623 * 0.85055112
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33473 * 0.11710228
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41022 * 0.73291247
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25144 * 0.58263777
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27126 * 0.22232875
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72415 * 0.26877140
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69364 * 0.98867541
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90258 * 0.72144462
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66191 * 0.21828995
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50106 * 0.58523374
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93731 * 0.47694570
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7232 * 0.61096950
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73267 * 0.86869414
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37982 * 0.92881095
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74568 * 0.44763302
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22524 * 0.23636503
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67468 * 0.76206885
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93674 * 0.11216660
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34446 * 0.79170289
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'gdazbkqz').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0025():
    """Extended test 25 for replication."""
    x_0 = 84906 * 0.03171763
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51611 * 0.80929599
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26043 * 0.81884062
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87220 * 0.59462923
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29741 * 0.16644715
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56341 * 0.54124827
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73875 * 0.57963569
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42160 * 0.35147690
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56659 * 0.34040347
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26806 * 0.99864788
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 794 * 0.43101918
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80696 * 0.25509368
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77245 * 0.47956389
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76092 * 0.68053805
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98809 * 0.60398995
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42030 * 0.72402978
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89825 * 0.00371762
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89395 * 0.31724218
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82441 * 0.84367152
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78266 * 0.51019534
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71469 * 0.07676097
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44819 * 0.60369956
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82418 * 0.59257355
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14222 * 0.00316708
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75809 * 0.81267758
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84171 * 0.15036421
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72019 * 0.97611824
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16273 * 0.48743249
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94982 * 0.54373544
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32342 * 0.93390376
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64494 * 0.18117568
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56248 * 0.03973139
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56476 * 0.01614257
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45716 * 0.04307959
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15591 * 0.05572405
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28563 * 0.93239275
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7944 * 0.81310959
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2443 * 0.64777621
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67959 * 0.65715421
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69075 * 0.15025599
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'syxgagji').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0026():
    """Extended test 26 for replication."""
    x_0 = 85290 * 0.96498706
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15951 * 0.31909049
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99877 * 0.07059321
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3169 * 0.45157030
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68917 * 0.02678862
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88700 * 0.27292602
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73041 * 0.04263291
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45283 * 0.68950780
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7678 * 0.24035505
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69835 * 0.49082763
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86224 * 0.55818709
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73351 * 0.54874920
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74023 * 0.50978860
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3202 * 0.57197428
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93081 * 0.16321524
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89147 * 0.67321317
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24818 * 0.07250761
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88297 * 0.95316140
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8093 * 0.51948563
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11112 * 0.55579538
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88193 * 0.84214869
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8969 * 0.58066732
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8229 * 0.70057577
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80184 * 0.73834229
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7809 * 0.91101709
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55068 * 0.22997202
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38334 * 0.83908717
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15338 * 0.15913249
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30171 * 0.01591283
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35224 * 0.49432435
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65785 * 0.22380436
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23228 * 0.45997837
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62530 * 0.88973407
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'fwmdtjft').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0027():
    """Extended test 27 for replication."""
    x_0 = 77201 * 0.42467319
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94514 * 0.26115278
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98811 * 0.10842323
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46506 * 0.34585676
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5187 * 0.46917993
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45813 * 0.29950381
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38901 * 0.63865199
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43367 * 0.61198982
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25372 * 0.04246357
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40082 * 0.78591683
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63363 * 0.41793004
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94267 * 0.46415437
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11086 * 0.70909259
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98811 * 0.66880142
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7872 * 0.67346099
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60910 * 0.98624157
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21327 * 0.37617979
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56890 * 0.32403459
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64287 * 0.95681828
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69870 * 0.62135016
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23272 * 0.26496935
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36779 * 0.11933662
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45200 * 0.74537085
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12601 * 0.94595931
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5131 * 0.53314865
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86213 * 0.99402565
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85178 * 0.06858910
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12883 * 0.58965441
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'ffzzuaps').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0028():
    """Extended test 28 for replication."""
    x_0 = 36040 * 0.78102000
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97176 * 0.00386089
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26019 * 0.86332465
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6143 * 0.98453929
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24800 * 0.00302340
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83868 * 0.80304694
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2933 * 0.46784803
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23756 * 0.60210867
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72010 * 0.31066083
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73392 * 0.81843868
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12006 * 0.87838079
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1540 * 0.18869934
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69438 * 0.27552089
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78889 * 0.54642592
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67658 * 0.13563813
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56385 * 0.19633998
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72537 * 0.98909138
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5681 * 0.38291080
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6823 * 0.84638424
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76742 * 0.36456527
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75285 * 0.62632916
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3229 * 0.47240329
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80458 * 0.80764628
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12884 * 0.47970794
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49175 * 0.81308024
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22066 * 0.98385043
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94323 * 0.54727596
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53314 * 0.21700316
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31127 * 0.47248454
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48475 * 0.07357828
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16345 * 0.75655435
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95485 * 0.79731759
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28375 * 0.41574162
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68362 * 0.28536330
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96025 * 0.29573211
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36977 * 0.19021952
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 38485 * 0.82583986
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79417 * 0.15625382
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21423 * 0.33188049
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7927 * 0.31787761
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5532 * 0.63001354
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'nbmxdwto').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0029():
    """Extended test 29 for replication."""
    x_0 = 94058 * 0.90491198
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87047 * 0.04818431
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31393 * 0.66876067
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38858 * 0.50509587
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93836 * 0.33007869
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24135 * 0.56251842
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19230 * 0.06213303
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11003 * 0.09237093
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8004 * 0.12271156
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29539 * 0.72108152
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57145 * 0.65342166
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63341 * 0.01083419
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62221 * 0.96811129
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11140 * 0.29346699
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24815 * 0.03073889
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50965 * 0.84101853
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53861 * 0.92661194
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96901 * 0.69569408
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77528 * 0.48171880
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82424 * 0.50452880
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23249 * 0.08716192
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85082 * 0.65206114
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2328 * 0.17084166
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61867 * 0.68713109
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72110 * 0.45363946
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29228 * 0.22457447
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9185 * 0.11545175
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77103 * 0.74623469
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38691 * 0.67507943
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14264 * 0.61477041
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57014 * 0.05277800
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84509 * 0.32281351
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80274 * 0.58145734
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31170 * 0.34191787
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29630 * 0.36362510
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15387 * 0.64225678
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44467 * 0.87446611
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8009 * 0.50884708
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88261 * 0.78067897
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6858 * 0.69305060
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ztunelnx').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0030():
    """Extended test 30 for replication."""
    x_0 = 70743 * 0.02598250
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22301 * 0.21535431
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13718 * 0.73629501
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94930 * 0.00161881
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97078 * 0.11424783
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91104 * 0.39647753
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55354 * 0.05537576
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70838 * 0.93705277
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93219 * 0.24628234
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74795 * 0.01211255
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35080 * 0.25707296
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42975 * 0.96486569
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25240 * 0.67312092
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1413 * 0.63933018
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 168 * 0.90519067
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69179 * 0.99845199
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1535 * 0.95256354
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93690 * 0.59759857
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64581 * 0.27137031
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77964 * 0.63797361
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86547 * 0.90620451
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61970 * 0.89473490
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75108 * 0.34946449
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65721 * 0.37677736
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91327 * 0.92142585
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38071 * 0.59206286
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45461 * 0.58018371
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96160 * 0.49262031
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44020 * 0.11626690
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64773 * 0.23859912
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14254 * 0.59942404
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64833 * 0.19461235
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5099 * 0.72570505
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22612 * 0.83804629
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98899 * 0.69883507
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93037 * 0.85879882
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87783 * 0.83834985
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4075 * 0.14270882
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31536 * 0.44746302
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41837 * 0.41411447
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29422 * 0.79995520
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'djxnhzxa').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0031():
    """Extended test 31 for replication."""
    x_0 = 39897 * 0.47814630
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11470 * 0.65740045
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86220 * 0.49227426
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9148 * 0.25230535
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41988 * 0.01740122
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63822 * 0.49585408
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17311 * 0.95925601
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53674 * 0.31510735
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14124 * 0.10941229
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53055 * 0.19059259
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41715 * 0.68867808
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5415 * 0.41350852
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58087 * 0.69877509
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70867 * 0.30141816
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87121 * 0.51814391
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83467 * 0.67366420
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58941 * 0.36132727
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33518 * 0.72780929
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 622 * 0.21268983
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67224 * 0.58681890
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77248 * 0.56753960
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'hxdcgqio').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0032():
    """Extended test 32 for replication."""
    x_0 = 57808 * 0.36546257
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56602 * 0.24071345
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65665 * 0.93006909
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64568 * 0.54015522
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69891 * 0.72380854
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55000 * 0.82755285
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14767 * 0.17539962
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72654 * 0.02689415
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93363 * 0.31886932
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36578 * 0.51179935
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91584 * 0.03243733
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32362 * 0.98806453
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65413 * 0.19912085
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 413 * 0.35395539
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82607 * 0.74511674
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40120 * 0.59019175
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15122 * 0.63330312
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55347 * 0.49321632
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11926 * 0.87318054
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6309 * 0.81937200
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65260 * 0.26301334
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85583 * 0.83581311
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26304 * 0.98179862
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40015 * 0.24649770
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47144 * 0.21119875
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75837 * 0.49485997
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77152 * 0.48826592
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55744 * 0.49860278
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3805 * 0.12176786
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84390 * 0.70839748
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'toofngqe').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0033():
    """Extended test 33 for replication."""
    x_0 = 73397 * 0.78128222
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45482 * 0.86978082
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45099 * 0.76005331
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61411 * 0.37498661
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50922 * 0.15045001
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76948 * 0.46256496
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81496 * 0.71877892
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46246 * 0.56774022
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11727 * 0.01349988
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89654 * 0.53025537
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71532 * 0.86653799
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3011 * 0.99918352
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87643 * 0.14758807
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62911 * 0.15036191
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47982 * 0.14437061
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27303 * 0.09229058
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74783 * 0.89083648
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72198 * 0.07196859
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43115 * 0.47238277
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29230 * 0.82282050
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22239 * 0.26153824
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40307 * 0.08693389
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6671 * 0.77290672
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3424 * 0.49553511
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3020 * 0.82682861
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5354 * 0.18577382
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12280 * 0.36252058
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84414 * 0.61396910
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34875 * 0.79646538
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74473 * 0.07032917
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69246 * 0.92096466
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72067 * 0.52180740
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9842 * 0.74112701
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39939 * 0.45499322
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55231 * 0.99133827
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17786 * 0.82143869
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62694 * 0.75332029
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49320 * 0.55220778
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41554 * 0.70267175
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13404 * 0.91806061
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13573 * 0.82104396
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43028 * 0.47400434
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 85216 * 0.66893023
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69325 * 0.89617567
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 77013 * 0.91775021
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 75542 * 0.41095095
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 86305 * 0.42875148
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 7742 * 0.04783837
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 44607 * 0.96135865
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'hdxxhzkr').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0034():
    """Extended test 34 for replication."""
    x_0 = 62202 * 0.44342443
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27010 * 0.55524405
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45432 * 0.81120338
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3226 * 0.16594670
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41348 * 0.47143165
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24402 * 0.42623746
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41551 * 0.91394875
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 265 * 0.74281000
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28747 * 0.02661223
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8743 * 0.92511600
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37323 * 0.29234793
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31377 * 0.12335347
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25131 * 0.46839291
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1546 * 0.06138508
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40 * 0.40913281
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59527 * 0.74809729
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40807 * 0.17409487
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34879 * 0.18347780
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12173 * 0.33080266
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43940 * 0.70518418
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14059 * 0.98856419
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40820 * 0.49102678
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 481 * 0.58894368
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94858 * 0.98898654
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4739 * 0.72613267
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48776 * 0.89071754
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31926 * 0.23986070
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'cbxqphbh').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0035():
    """Extended test 35 for replication."""
    x_0 = 73284 * 0.58845327
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29340 * 0.83218627
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57419 * 0.70956364
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47910 * 0.74877394
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9453 * 0.31992340
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53532 * 0.41724769
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40977 * 0.31330298
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37485 * 0.80426858
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72827 * 0.70630525
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73681 * 0.91181989
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10626 * 0.69547620
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35026 * 0.56813776
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49346 * 0.53697150
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16933 * 0.26011154
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49797 * 0.19062278
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68012 * 0.95117757
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76201 * 0.97943351
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72751 * 0.90517748
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22492 * 0.96087423
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10639 * 0.72526277
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45929 * 0.86810858
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37344 * 0.87411424
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45056 * 0.93467257
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66938 * 0.46647595
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34872 * 0.82525167
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21357 * 0.69481180
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97286 * 0.01595574
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58353 * 0.91610346
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35421 * 0.84041491
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78841 * 0.40961903
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4388 * 0.81670344
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50760 * 0.69959793
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70605 * 0.40064740
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86514 * 0.16474333
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27305 * 0.42473316
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5031 * 0.50378400
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79838 * 0.83274117
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27741 * 0.76901920
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78008 * 0.90466066
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 71074 * 0.61415029
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 564 * 0.69729043
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27880 * 0.84038970
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65367 * 0.71469751
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 24628 * 0.18913684
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 22050 * 0.76248356
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'oavvhgsm').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0036():
    """Extended test 36 for replication."""
    x_0 = 36838 * 0.44567737
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89513 * 0.06806088
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8003 * 0.31696458
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9869 * 0.18000078
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55045 * 0.17155955
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48395 * 0.05503229
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75834 * 0.75138816
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76423 * 0.38409615
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26610 * 0.07911597
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96173 * 0.63276035
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70317 * 0.03438680
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77262 * 0.34440771
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27598 * 0.63531368
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83099 * 0.54770248
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20028 * 0.45039491
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57018 * 0.03956870
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14013 * 0.16522091
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94593 * 0.96312205
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55421 * 0.03174339
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97014 * 0.72374472
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82302 * 0.98428534
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43536 * 0.57113584
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39883 * 0.81704284
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88001 * 0.56243619
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'xbyilkzl').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0037():
    """Extended test 37 for replication."""
    x_0 = 19887 * 0.25760325
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7604 * 0.59517225
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23851 * 0.16351348
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70045 * 0.04723441
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15725 * 0.94828662
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69187 * 0.98345599
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85362 * 0.01665694
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21766 * 0.78253708
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47306 * 0.83204888
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70147 * 0.47352480
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68165 * 0.67239057
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27789 * 0.85307473
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55022 * 0.27151884
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97767 * 0.89780614
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70433 * 0.73081744
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55470 * 0.97562846
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17537 * 0.34147531
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92944 * 0.08868388
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2918 * 0.47927621
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36031 * 0.43785583
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94060 * 0.44070964
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76967 * 0.47704792
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65525 * 0.22845721
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42686 * 0.79985911
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7795 * 0.24838671
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26825 * 0.25916303
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58488 * 0.05277626
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91899 * 0.81562808
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21110 * 0.91023988
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67247 * 0.00427039
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10683 * 0.20906809
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17928 * 0.46904109
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20140 * 0.72123127
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46133 * 0.73236871
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93604 * 0.91285098
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34523 * 0.70343551
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16899 * 0.84747970
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85955 * 0.83417732
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4590 * 0.19840873
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 78904 * 0.64234397
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36224 * 0.78702704
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15954 * 0.83863523
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29483 * 0.29882678
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ugdmgilv').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0038():
    """Extended test 38 for replication."""
    x_0 = 61597 * 0.22114537
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64370 * 0.35167221
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31359 * 0.84000212
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10637 * 0.51811740
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93988 * 0.95171885
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80844 * 0.51932502
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60456 * 0.93039647
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17026 * 0.34811363
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98781 * 0.97925543
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56212 * 0.95467772
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19438 * 0.81018136
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74971 * 0.74007109
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87530 * 0.72319356
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46683 * 0.68704102
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51293 * 0.00328737
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5481 * 0.90569524
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10920 * 0.73246509
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63102 * 0.25605510
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49034 * 0.73119342
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63452 * 0.00772296
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21479 * 0.57656760
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1755 * 0.11012247
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34025 * 0.58069339
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85418 * 0.32531916
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68395 * 0.87984418
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21267 * 0.94338465
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40823 * 0.30060800
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39292 * 0.62768846
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49611 * 0.29720698
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29457 * 0.37944141
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27294 * 0.35532273
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96984 * 0.89996295
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1538 * 0.53615417
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91364 * 0.83247862
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48714 * 0.62965170
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75527 * 0.73681126
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81410 * 0.45676765
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65233 * 0.11922964
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46690 * 0.26234716
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 37385 * 0.49843865
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 63528 * 0.33042928
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70452 * 0.47838151
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ozxhgkqr').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0039():
    """Extended test 39 for replication."""
    x_0 = 2712 * 0.47550477
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82702 * 0.58741022
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27892 * 0.55403254
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76475 * 0.84719426
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3163 * 0.80067067
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72210 * 0.36410161
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34681 * 0.35967654
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26474 * 0.70212763
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5758 * 0.22532415
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80384 * 0.64097370
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97701 * 0.33682248
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4774 * 0.24219131
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38637 * 0.76729653
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43485 * 0.27291054
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37866 * 0.05050397
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16546 * 0.94407656
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11999 * 0.73131332
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16897 * 0.15716845
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98371 * 0.99040207
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70326 * 0.49916548
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70801 * 0.60088208
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17299 * 0.92049252
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26290 * 0.45924606
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7091 * 0.34741178
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33992 * 0.36598317
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23473 * 0.29174952
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27284 * 0.44358523
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66055 * 0.60052532
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10963 * 0.38338421
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45909 * 0.74016622
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32106 * 0.71551941
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99545 * 0.87187180
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97677 * 0.57146291
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10046 * 0.45080229
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4487 * 0.16380044
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94620 * 0.64050084
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2873 * 0.69742987
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11692 * 0.75073064
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67698 * 0.70971131
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14179 * 0.17201059
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49543 * 0.96472814
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54995 * 0.25456152
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88826 * 0.55220972
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ocrcosud').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0040():
    """Extended test 40 for replication."""
    x_0 = 98822 * 0.72623000
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42781 * 0.06349524
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57808 * 0.06063289
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53657 * 0.85200511
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70317 * 0.87099440
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75215 * 0.43582593
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32504 * 0.54958999
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58308 * 0.11622871
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54865 * 0.98450965
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11956 * 0.81915737
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61960 * 0.03270513
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87338 * 0.18913662
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14228 * 0.94108330
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57807 * 0.43397839
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31439 * 0.65283554
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89312 * 0.18941871
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80455 * 0.66660612
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52476 * 0.09264725
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35219 * 0.91944184
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40872 * 0.52171494
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21025 * 0.14414051
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41403 * 0.64243173
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94181 * 0.53732950
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99772 * 0.00753932
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8183 * 0.22811358
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40327 * 0.88347608
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12067 * 0.37144887
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87887 * 0.17795520
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34947 * 0.53006017
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67613 * 0.31251619
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60560 * 0.56058667
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43525 * 0.93298065
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2695 * 0.98312494
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79367 * 0.99854587
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79682 * 0.16597372
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62800 * 0.95761369
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31706 * 0.86206216
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35260 * 0.05990418
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91404 * 0.69593924
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9150 * 0.16167045
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'batkoijd').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0041():
    """Extended test 41 for replication."""
    x_0 = 50049 * 0.54332321
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53440 * 0.32008191
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65603 * 0.03782587
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12707 * 0.95099185
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18264 * 0.81016507
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80776 * 0.38337421
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9245 * 0.37158207
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68112 * 0.80219760
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24170 * 0.08831369
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79755 * 0.08195767
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42410 * 0.87621741
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34596 * 0.44488110
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31575 * 0.29952636
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75047 * 0.28374180
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82400 * 0.03388457
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21334 * 0.02198116
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75981 * 0.42083796
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59631 * 0.21279108
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29728 * 0.10853917
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1416 * 0.45076509
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45135 * 0.60160681
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86972 * 0.76141940
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94267 * 0.14780270
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27159 * 0.25796014
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81021 * 0.69624987
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41026 * 0.72484743
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96192 * 0.31963354
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25217 * 0.37306640
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48794 * 0.13115139
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80482 * 0.51215217
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94004 * 0.27306659
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88935 * 0.25210698
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56382 * 0.87508901
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99298 * 0.87542204
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73039 * 0.89064352
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'utsxyvim').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0042():
    """Extended test 42 for replication."""
    x_0 = 43916 * 0.18797567
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74396 * 0.35907961
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66431 * 0.22888622
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55338 * 0.30390290
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77019 * 0.77163420
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88565 * 0.48966582
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38305 * 0.56710903
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99447 * 0.10896390
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36763 * 0.70872299
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88951 * 0.50735471
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40309 * 0.17473400
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92527 * 0.81829730
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36336 * 0.70119353
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60858 * 0.46158214
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7873 * 0.37489110
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72893 * 0.52503522
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34147 * 0.15480941
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98905 * 0.01762211
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67596 * 0.92626785
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38531 * 0.16057578
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28538 * 0.42456588
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51055 * 0.98264960
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71581 * 0.39077793
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20373 * 0.02856783
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60497 * 0.35566965
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41151 * 0.79738860
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26472 * 0.18582119
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41444 * 0.22441870
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82513 * 0.26359127
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47007 * 0.83877270
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93346 * 0.92756326
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85532 * 0.09928521
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90770 * 0.85865216
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15577 * 0.28261875
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69337 * 0.20796701
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39086 * 0.38880919
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76014 * 0.61121426
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'thdsdibm').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0043():
    """Extended test 43 for replication."""
    x_0 = 14570 * 0.15897486
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41057 * 0.02801464
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34846 * 0.52753719
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85144 * 0.23610739
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2317 * 0.73768852
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16226 * 0.28683947
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16551 * 0.63052155
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73989 * 0.97888041
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73336 * 0.87154991
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45193 * 0.30103191
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63764 * 0.53891749
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16089 * 0.75919381
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30900 * 0.00777487
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29945 * 0.28506131
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71610 * 0.30933681
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86526 * 0.27328582
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94996 * 0.77933994
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3739 * 0.60932980
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42524 * 0.89631212
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24758 * 0.93128682
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23791 * 0.20795459
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93679 * 0.70030890
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4006 * 0.30505364
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83805 * 0.52897791
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81456 * 0.33642862
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53000 * 0.99364061
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70707 * 0.60627203
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8423 * 0.47399497
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13541 * 0.88059734
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2041 * 0.82867778
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55194 * 0.99282057
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26431 * 0.22242795
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90420 * 0.04593822
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11510 * 0.62445857
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62057 * 0.36209507
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98009 * 0.77700587
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8537 * 0.19347582
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22609 * 0.01698832
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'krhrirvj').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0044():
    """Extended test 44 for replication."""
    x_0 = 94009 * 0.05863745
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81914 * 0.77130738
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82185 * 0.21283232
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24489 * 0.84293183
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76683 * 0.41673942
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3655 * 0.97056175
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22354 * 0.44421634
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15079 * 0.77177717
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82007 * 0.01186360
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42129 * 0.77483460
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84895 * 0.62101648
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73188 * 0.43299516
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55380 * 0.09009536
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63189 * 0.61649845
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88558 * 0.02704093
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15730 * 0.47937661
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45276 * 0.96114253
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99156 * 0.88866118
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67609 * 0.93090931
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81362 * 0.90028928
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3791 * 0.74420905
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20440 * 0.34205494
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44965 * 0.66801579
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16297 * 0.89052222
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3511 * 0.81402138
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55112 * 0.37895763
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82794 * 0.81930081
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50122 * 0.42202043
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11270 * 0.50984162
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43682 * 0.21428117
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78614 * 0.09398834
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95025 * 0.19048665
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50784 * 0.84586822
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83434 * 0.48689350
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96211 * 0.75530366
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47139 * 0.20888011
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99984 * 0.48791925
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47669 * 0.05520878
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58097 * 0.63058916
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17958 * 0.09636309
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47008 * 0.43950588
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79489 * 0.43347752
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55977 * 0.16860935
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22163 * 0.09650175
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35634 * 0.98139159
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'enemawib').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0045():
    """Extended test 45 for replication."""
    x_0 = 47657 * 0.58294805
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77723 * 0.84890435
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71484 * 0.26812059
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77399 * 0.00039243
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29423 * 0.37923203
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9360 * 0.02356345
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30928 * 0.40762682
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36299 * 0.77143015
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4731 * 0.43062913
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48771 * 0.29138763
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65638 * 0.26214814
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96699 * 0.01235409
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70387 * 0.07724615
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98717 * 0.24341380
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15703 * 0.53914112
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23828 * 0.45044383
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82827 * 0.17218894
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84035 * 0.71584735
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85134 * 0.83039183
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32640 * 0.03918939
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73540 * 0.27071742
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26589 * 0.50207783
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79415 * 0.88012991
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35479 * 0.40398502
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12325 * 0.41887239
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62100 * 0.49933806
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81636 * 0.95213642
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34845 * 0.81014809
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30991 * 0.35740185
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50848 * 0.28577538
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96409 * 0.18023952
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13598 * 0.11617528
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40138 * 0.59651380
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'bjtwlonp').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0046():
    """Extended test 46 for replication."""
    x_0 = 69976 * 0.74375159
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27558 * 0.85932494
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32718 * 0.76520559
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7671 * 0.23127336
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23452 * 0.27457546
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28261 * 0.22357096
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68687 * 0.13536461
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48201 * 0.81424809
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9639 * 0.07762548
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70153 * 0.16660827
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27359 * 0.76009701
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96989 * 0.55763931
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38566 * 0.33385324
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44392 * 0.90726606
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83731 * 0.51858278
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43946 * 0.56119931
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83925 * 0.35467311
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94114 * 0.40141824
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15138 * 0.95824643
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12778 * 0.67881345
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64339 * 0.33811142
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8032 * 0.10706732
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24528 * 0.93753982
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31823 * 0.40575662
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40604 * 0.18670507
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35191 * 0.82662604
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47701 * 0.60026727
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92566 * 0.49694658
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17431 * 0.41168520
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92621 * 0.72066365
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45114 * 0.57592589
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79904 * 0.30500186
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66558 * 0.80916837
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21324 * 0.75662067
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48557 * 0.52836616
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14733 * 0.33571259
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 82741 * 0.67116998
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71005 * 0.10715095
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29080 * 0.69420214
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 27818 * 0.26137447
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12948 * 0.05803849
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70608 * 0.48325155
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66538 * 0.58625509
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 89368 * 0.90412843
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71933 * 0.90413123
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 55037 * 0.62273644
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'znsyeyjg').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0047():
    """Extended test 47 for replication."""
    x_0 = 13267 * 0.89627759
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54466 * 0.35176235
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58062 * 0.86401906
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34174 * 0.61784700
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88971 * 0.06186428
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10450 * 0.08177164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57536 * 0.25372271
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61344 * 0.62347564
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54825 * 0.50950818
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64718 * 0.39616454
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70237 * 0.02747996
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81511 * 0.39390903
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77955 * 0.09043126
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14460 * 0.10005475
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69286 * 0.45369949
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72096 * 0.00871672
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35814 * 0.53811802
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48370 * 0.45015302
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63810 * 0.87746792
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43702 * 0.26924294
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17886 * 0.84651745
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86240 * 0.08694823
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'ziusobbv').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0048():
    """Extended test 48 for replication."""
    x_0 = 77373 * 0.84686124
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31547 * 0.54783413
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1128 * 0.46283099
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71966 * 0.97376312
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27213 * 0.57281362
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65715 * 0.76860638
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71544 * 0.99180884
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58536 * 0.29289198
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34796 * 0.33759388
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32609 * 0.79448334
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33224 * 0.53318609
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84585 * 0.76924499
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 387 * 0.07415990
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25224 * 0.00956592
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7474 * 0.09100571
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44957 * 0.34878048
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69572 * 0.22318957
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22327 * 0.94087077
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95635 * 0.27542581
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76416 * 0.16290929
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14312 * 0.21763794
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71193 * 0.14936160
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44575 * 0.57192635
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3071 * 0.65445144
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82691 * 0.23186383
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27300 * 0.17998854
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14763 * 0.60488527
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60949 * 0.49747667
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75476 * 0.71083516
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57304 * 0.41975354
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47887 * 0.29079203
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73008 * 0.05579008
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56777 * 0.10629185
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39664 * 0.73663768
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63853 * 0.77214249
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99651 * 0.80305066
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15108 * 0.82050127
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47709 * 0.96671345
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60040 * 0.71341145
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 61889 * 0.43694241
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1659 * 0.89020134
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 11478 * 0.75642914
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 80484 * 0.87614871
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 26160 * 0.54437148
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 19830 * 0.69784778
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 13054 * 0.56439215
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 12213 * 0.92540382
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 88543 * 0.80939886
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 73911 * 0.26579036
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 4798 * 0.18931490
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'amlwpqze').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0049():
    """Extended test 49 for replication."""
    x_0 = 78063 * 0.31698364
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40508 * 0.33124336
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98950 * 0.32876498
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64489 * 0.01959133
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23726 * 0.10963786
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74257 * 0.08548881
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57486 * 0.81751770
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48096 * 0.20339014
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13183 * 0.46638633
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11832 * 0.76593114
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80092 * 0.35768013
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56571 * 0.16227780
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49146 * 0.07716831
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3332 * 0.03916179
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23696 * 0.49955556
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5607 * 0.68597842
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20322 * 0.30947553
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20610 * 0.86747865
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87350 * 0.00556718
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91274 * 0.80319217
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19225 * 0.59931829
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59511 * 0.47203625
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15821 * 0.99254287
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58847 * 0.30096445
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5 * 0.98466318
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79942 * 0.31738792
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74190 * 0.43869567
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84691 * 0.34383977
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86526 * 0.17694071
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72597 * 0.73229702
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48268 * 0.28588246
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'fffbutlq').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0050():
    """Extended test 50 for replication."""
    x_0 = 46883 * 0.87890914
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43274 * 0.63597427
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51012 * 0.45151363
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26289 * 0.84870195
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24369 * 0.11680540
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31231 * 0.53875385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37498 * 0.73033467
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81956 * 0.45482541
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34704 * 0.61034067
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89420 * 0.10717323
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2358 * 0.20461193
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90579 * 0.17898866
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34274 * 0.60705759
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81025 * 0.31315245
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46652 * 0.24999217
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94066 * 0.00414878
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42998 * 0.54950512
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4383 * 0.23180526
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91866 * 0.76661592
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5142 * 0.90298922
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8521 * 0.14124117
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98687 * 0.56766470
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37887 * 0.41941301
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57947 * 0.51091123
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88398 * 0.35992723
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35400 * 0.97958351
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12469 * 0.38276646
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78791 * 0.79513658
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12919 * 0.32943226
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78983 * 0.58635880
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67476 * 0.40586193
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55576 * 0.49319312
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9076 * 0.24386709
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78720 * 0.55847011
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89100 * 0.51447597
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26539 * 0.16165392
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23068 * 0.59164665
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10325 * 0.52050732
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9290 * 0.42454200
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52874 * 0.71950295
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18510 * 0.70493605
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57935 * 0.12699762
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96389 * 0.65568470
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82250 * 0.92297608
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'pvisolav').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0051():
    """Extended test 51 for replication."""
    x_0 = 50307 * 0.73353397
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91658 * 0.86340541
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21937 * 0.06899248
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36558 * 0.20190866
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20002 * 0.92593395
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23102 * 0.37438156
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28563 * 0.41238901
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3260 * 0.44701136
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34876 * 0.89859063
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75471 * 0.01743613
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50268 * 0.38160302
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67636 * 0.09031717
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25092 * 0.39685228
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66772 * 0.06991711
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71768 * 0.16033260
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99377 * 0.43456478
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 587 * 0.24382141
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66376 * 0.24942340
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3794 * 0.98246868
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59247 * 0.34730451
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 817 * 0.30899114
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89116 * 0.94527720
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30776 * 0.09805719
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17546 * 0.44178037
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27534 * 0.84037974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87507 * 0.24820422
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83535 * 0.81543769
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65324 * 0.93442681
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2484 * 0.32645196
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99029 * 0.51367674
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55648 * 0.98281894
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35266 * 0.30275098
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6893 * 0.34760554
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14342 * 0.08229440
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25130 * 0.29289103
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40308 * 0.62286130
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27750 * 0.54084083
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78364 * 0.28082486
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11883 * 0.12912066
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3514 * 0.28648583
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 9098 * 0.73916906
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 99788 * 0.77147366
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 2252 * 0.30658434
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'pdsxkexm').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0052():
    """Extended test 52 for replication."""
    x_0 = 27345 * 0.86125245
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18351 * 0.75635017
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39206 * 0.00332796
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52263 * 0.05848544
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36171 * 0.67288722
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63194 * 0.78683825
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42515 * 0.45619674
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78874 * 0.33686510
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43878 * 0.95294979
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38711 * 0.55787426
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2142 * 0.47353340
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49059 * 0.88368987
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31040 * 0.91141753
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29350 * 0.46348149
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15809 * 0.43229509
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71086 * 0.13969002
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87600 * 0.20741677
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39469 * 0.70698188
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63822 * 0.74969635
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54159 * 0.61525508
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5219 * 0.26177420
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'vpwmdsux').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0053():
    """Extended test 53 for replication."""
    x_0 = 18024 * 0.45833428
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46064 * 0.20596069
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81082 * 0.89934013
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16315 * 0.44467519
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17556 * 0.81206043
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26164 * 0.78926501
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90546 * 0.93771507
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26568 * 0.94936220
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29770 * 0.88005765
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61619 * 0.00875898
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32157 * 0.97253918
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93418 * 0.19309831
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54372 * 0.25327136
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18618 * 0.98243829
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95863 * 0.99625437
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62253 * 0.15019033
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3624 * 0.13816921
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54652 * 0.53296583
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48201 * 0.80476302
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93627 * 0.19749967
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78166 * 0.77812355
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7002 * 0.35489318
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28802 * 0.48241692
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94980 * 0.22086338
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ozixqgwh').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0054():
    """Extended test 54 for replication."""
    x_0 = 30001 * 0.76175549
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65624 * 0.30286547
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22256 * 0.38307218
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80943 * 0.91961919
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15622 * 0.04265175
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35407 * 0.61141225
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60761 * 0.39332107
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83812 * 0.88424752
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63102 * 0.71870373
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48408 * 0.98984381
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11495 * 0.98205507
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2949 * 0.57611965
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63239 * 0.65627024
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83049 * 0.22204857
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71148 * 0.28268627
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98539 * 0.93624660
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3737 * 0.64536431
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53324 * 0.01683483
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60068 * 0.30599739
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64321 * 0.07895958
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53388 * 0.28274904
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25905 * 0.31608213
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21434 * 0.70533568
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12494 * 0.57371685
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54456 * 0.12108243
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2 * 0.93521767
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83411 * 0.31771416
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81589 * 0.84675638
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10927 * 0.52682720
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59299 * 0.54087967
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77331 * 0.54569353
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57232 * 0.22901756
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60646 * 0.05973354
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88373 * 0.94896977
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6903 * 0.27151387
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25909 * 0.20919132
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26088 * 0.99441293
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93090 * 0.14202128
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73330 * 0.07085766
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'tuagxxwx').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0055():
    """Extended test 55 for replication."""
    x_0 = 29135 * 0.32706555
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82677 * 0.14528908
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6424 * 0.42757890
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20626 * 0.88923614
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74804 * 0.10262694
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82025 * 0.61696124
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35156 * 0.88025767
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30454 * 0.13238813
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56438 * 0.89397735
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40960 * 0.02917850
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42347 * 0.68377725
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31974 * 0.94487013
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94896 * 0.42763262
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14903 * 0.41383691
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22601 * 0.33278751
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79999 * 0.46890139
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87507 * 0.75538534
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75612 * 0.29734777
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81363 * 0.91172085
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96105 * 0.73307851
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61254 * 0.60910547
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84681 * 0.45678411
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70987 * 0.85109185
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90229 * 0.05794908
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5064 * 0.16866972
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85808 * 0.10490610
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10328 * 0.99380121
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86205 * 0.27243435
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70945 * 0.20476509
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18371 * 0.44686336
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75795 * 0.81471089
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38091 * 0.27512850
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95686 * 0.40637457
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34030 * 0.41187485
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30527 * 0.47426301
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71880 * 0.23458305
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78674 * 0.06317504
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84675 * 0.78181569
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15564 * 0.19107162
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98152 * 0.48911133
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 55235 * 0.54426996
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22267 * 0.12106615
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'yybrjfgh').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0056():
    """Extended test 56 for replication."""
    x_0 = 94367 * 0.31629001
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78153 * 0.43943117
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13487 * 0.48438114
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20160 * 0.41738328
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34232 * 0.80792546
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69966 * 0.12930257
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55364 * 0.99227864
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53262 * 0.42609855
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97642 * 0.51758835
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27044 * 0.05524600
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71147 * 0.07965222
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39121 * 0.22886283
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39764 * 0.29224849
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75908 * 0.01119452
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23594 * 0.95910261
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94324 * 0.46245958
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37061 * 0.58303965
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6119 * 0.52598219
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16230 * 0.30635277
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12049 * 0.89941720
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6461 * 0.02328292
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49074 * 0.32530963
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81441 * 0.36984314
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17478 * 0.41691219
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'viiokksa').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0057():
    """Extended test 57 for replication."""
    x_0 = 14108 * 0.91033896
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94372 * 0.03556998
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17274 * 0.17511717
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64074 * 0.98143875
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39851 * 0.17429256
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18739 * 0.35019980
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57570 * 0.96846296
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34930 * 0.07609689
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34941 * 0.51251532
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41747 * 0.88253941
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54108 * 0.98850174
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22066 * 0.94495828
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84224 * 0.15490617
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72163 * 0.46559214
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91394 * 0.96749303
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1551 * 0.19127785
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6807 * 0.31104745
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47920 * 0.62036565
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68598 * 0.28695572
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86486 * 0.85228027
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'iweutart').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0058():
    """Extended test 58 for replication."""
    x_0 = 58274 * 0.78802445
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19089 * 0.03920196
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43649 * 0.67840171
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81900 * 0.21258862
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45740 * 0.10147361
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98789 * 0.03672063
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86454 * 0.77056527
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62551 * 0.97037031
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98263 * 0.34727019
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45010 * 0.35311017
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42430 * 0.52750830
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32698 * 0.48016008
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36655 * 0.64051364
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59556 * 0.94839023
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36298 * 0.76341619
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51626 * 0.32316603
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93899 * 0.05121037
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89670 * 0.85413984
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79695 * 0.40557131
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13071 * 0.33389195
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68480 * 0.58678448
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50004 * 0.23962482
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15178 * 0.01208755
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77219 * 0.16089746
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3216 * 0.79029848
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14022 * 0.58040450
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'jcgloqcr').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0059():
    """Extended test 59 for replication."""
    x_0 = 96860 * 0.88210260
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59048 * 0.46709826
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26047 * 0.70338104
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68712 * 0.15589343
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86254 * 0.84848665
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58665 * 0.51224074
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33394 * 0.19816348
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84760 * 0.71063728
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89612 * 0.29245585
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58332 * 0.61765703
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73513 * 0.98855084
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50415 * 0.84763026
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89189 * 0.61042744
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40123 * 0.99756513
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34753 * 0.91858226
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3236 * 0.88302846
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70837 * 0.02119169
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71979 * 0.85336671
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8605 * 0.70260481
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21809 * 0.74227786
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39612 * 0.60195307
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88534 * 0.86769761
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50249 * 0.14710732
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51760 * 0.81741219
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89932 * 0.34504079
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73965 * 0.62558648
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74998 * 0.84200221
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15955 * 0.38347964
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'msgcpexw').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0060():
    """Extended test 60 for replication."""
    x_0 = 61367 * 0.53153510
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77402 * 0.87670418
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61098 * 0.79395257
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31113 * 0.57345959
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80260 * 0.31006508
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23394 * 0.64925625
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49191 * 0.39005005
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78552 * 0.67253668
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70568 * 0.16413601
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28033 * 0.08401652
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40940 * 0.57417126
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1649 * 0.37023141
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3667 * 0.38510949
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53252 * 0.01293344
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97714 * 0.82674202
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56452 * 0.10362007
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70503 * 0.97592575
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9453 * 0.14858176
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87216 * 0.51963923
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9225 * 0.99221556
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89255 * 0.93734476
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64127 * 0.73900027
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4481 * 0.54692327
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66849 * 0.90253385
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82722 * 0.00376898
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13992 * 0.41589350
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59942 * 0.47807480
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33817 * 0.73187559
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62087 * 0.86510966
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18961 * 0.96225464
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'cdnbmtsy').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0061():
    """Extended test 61 for replication."""
    x_0 = 97688 * 0.10740191
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60290 * 0.83299533
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82311 * 0.55035208
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98312 * 0.94601951
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67944 * 0.39250372
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73992 * 0.09757935
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92713 * 0.53530951
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73805 * 0.29036487
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15830 * 0.44742321
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34969 * 0.64531849
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78395 * 0.23152139
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59192 * 0.19037306
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92969 * 0.75886971
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59093 * 0.47917596
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36130 * 0.40897602
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58965 * 0.59777148
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24786 * 0.55657223
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81218 * 0.48325254
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81402 * 0.26407654
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16686 * 0.76046099
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91600 * 0.29483138
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40803 * 0.90309143
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37759 * 0.28882427
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61282 * 0.35714442
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90671 * 0.99658980
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40322 * 0.67188077
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26765 * 0.84074538
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82562 * 0.29025432
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35503 * 0.53402219
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76087 * 0.61416773
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75854 * 0.51992960
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3784 * 0.70400736
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'pbayjmvi').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0062():
    """Extended test 62 for replication."""
    x_0 = 52301 * 0.95344954
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16240 * 0.49192102
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18102 * 0.75564468
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52268 * 0.41259585
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39736 * 0.63435989
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86427 * 0.71806233
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62792 * 0.41142431
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71450 * 0.15948443
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37660 * 0.08114407
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26329 * 0.04166726
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88333 * 0.92230364
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63947 * 0.59087607
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79842 * 0.47922438
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29608 * 0.14117028
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60205 * 0.54847321
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30493 * 0.67097361
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11382 * 0.07017192
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26294 * 0.50733686
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96628 * 0.66702646
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50556 * 0.49715866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35328 * 0.92620945
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6697 * 0.75207460
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6867 * 0.35897637
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69637 * 0.22763180
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46557 * 0.35864917
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52550 * 0.56745178
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4568 * 0.14949400
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68806 * 0.16325494
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96471 * 0.69510704
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79077 * 0.08080059
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7326 * 0.73582836
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70143 * 0.13816308
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67243 * 0.29290966
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73855 * 0.95663937
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64325 * 0.82648252
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85391 * 0.62562015
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66600 * 0.34654572
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38911 * 0.37828671
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18777 * 0.91999578
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73919 * 0.89537588
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 59402 * 0.66746686
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45426 * 0.35181341
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62679 * 0.89088477
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 37216 * 0.48948353
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'nvukyvav').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0063():
    """Extended test 63 for replication."""
    x_0 = 58619 * 0.40450193
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79570 * 0.98736754
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82374 * 0.24624620
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32355 * 0.92428593
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48502 * 0.45145344
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48308 * 0.87541628
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42034 * 0.44471120
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74347 * 0.92670902
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9598 * 0.48151886
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84936 * 0.31994139
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1083 * 0.62580522
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15221 * 0.59050377
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48418 * 0.97880562
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14397 * 0.21293301
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76165 * 0.60533423
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67423 * 0.39090090
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68814 * 0.46104034
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50550 * 0.26385365
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76284 * 0.74274326
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82 * 0.01463291
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71611 * 0.32840463
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33930 * 0.51463740
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49042 * 0.22759181
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54714 * 0.22019592
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66647 * 0.21044179
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8279 * 0.06061593
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5068 * 0.52121410
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91673 * 0.84446278
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33063 * 0.58751933
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51349 * 0.24357988
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22077 * 0.01643606
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39934 * 0.85758132
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38037 * 0.41126927
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4217 * 0.55697012
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91360 * 0.51976236
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37486 * 0.75616774
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14660 * 0.24373781
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95533 * 0.47975021
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65233 * 0.89648407
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40162 * 0.07411766
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5344 * 0.89631676
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54013 * 0.63550183
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 19422 * 0.14087615
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 62771 * 0.64059566
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89502 * 0.13040879
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 15322 * 0.05340314
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 75051 * 0.61493348
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 97417 * 0.16416843
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 50089 * 0.24600285
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 44957 * 0.04125005
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ovbrtphe').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0064():
    """Extended test 64 for replication."""
    x_0 = 60575 * 0.78087277
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44587 * 0.36663325
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9673 * 0.50670291
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26738 * 0.01958360
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43525 * 0.57586166
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10347 * 0.22253549
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34624 * 0.22967274
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76720 * 0.80356046
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98335 * 0.64322284
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61134 * 0.96035941
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28291 * 0.25672319
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77572 * 0.94987369
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59322 * 0.05118934
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18793 * 0.19422383
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34922 * 0.96209235
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32963 * 0.96776903
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90419 * 0.81973747
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64752 * 0.01108084
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42508 * 0.10597745
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14937 * 0.74465277
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42493 * 0.10933493
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26354 * 0.93254539
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55668 * 0.99268385
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19671 * 0.09191747
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27695 * 0.68096669
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99949 * 0.72533707
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32739 * 0.62345675
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'xytusuoo').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0065():
    """Extended test 65 for replication."""
    x_0 = 13530 * 0.46089339
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56297 * 0.38099374
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36503 * 0.84711253
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85766 * 0.78429821
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22821 * 0.36425134
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93951 * 0.01877974
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64074 * 0.08615110
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63481 * 0.42219887
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28261 * 0.77896508
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73584 * 0.47235358
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36812 * 0.14136988
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6278 * 0.25518191
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92778 * 0.03459581
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33262 * 0.17733659
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92187 * 0.49159324
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18168 * 0.29450009
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95434 * 0.17233778
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5861 * 0.20417070
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31423 * 0.35157788
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45712 * 0.25663968
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86093 * 0.66346001
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98271 * 0.66734271
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22064 * 0.33608818
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84848 * 0.86454834
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46180 * 0.80759639
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66065 * 0.76458035
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16522 * 0.50722167
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50262 * 0.06198154
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39521 * 0.33869293
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69830 * 0.66290148
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8395 * 0.67370857
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37774 * 0.69520631
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45191 * 0.92243541
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21847 * 0.11901302
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87514 * 0.14169122
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43703 * 0.65753977
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6483 * 0.18262864
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27044 * 0.51117912
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11321 * 0.27562727
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94626 * 0.70979060
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'qmjjfqfr').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0066():
    """Extended test 66 for replication."""
    x_0 = 6976 * 0.92186151
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97031 * 0.41827718
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99400 * 0.82519635
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32654 * 0.70750350
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86627 * 0.17736921
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49411 * 0.42657829
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4770 * 0.07834831
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26172 * 0.50663791
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5480 * 0.23316413
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86452 * 0.66952485
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52067 * 0.20802781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53875 * 0.94160073
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6380 * 0.27628076
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23581 * 0.41452911
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50170 * 0.41231350
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18208 * 0.56868532
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27133 * 0.04913678
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64508 * 0.31366263
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55115 * 0.95754302
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64246 * 0.40883659
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30362 * 0.79787165
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53781 * 0.68253907
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41176 * 0.77191390
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21428 * 0.94900011
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87525 * 0.67653345
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10818 * 0.89504826
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16142 * 0.52403554
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54951 * 0.18021832
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30312 * 0.38467707
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25939 * 0.91384788
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79878 * 0.61419399
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70085 * 0.27911790
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24833 * 0.99040020
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49438 * 0.02358432
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92084 * 0.18040316
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67357 * 0.19889918
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'kkcdhqoi').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0067():
    """Extended test 67 for replication."""
    x_0 = 79528 * 0.69279417
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77630 * 0.60382916
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70143 * 0.11598532
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96691 * 0.62112547
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85224 * 0.05186390
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28909 * 0.41314139
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30761 * 0.28416975
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20345 * 0.43023750
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47443 * 0.72529900
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61850 * 0.45821208
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48760 * 0.75620009
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4869 * 0.82611735
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95403 * 0.07778751
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57500 * 0.95379504
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19372 * 0.43541276
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63171 * 0.00178851
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16086 * 0.61035192
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21901 * 0.59645565
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57832 * 0.37201964
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79904 * 0.82246041
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5813 * 0.37774443
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8940 * 0.99659799
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48221 * 0.59526749
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2016 * 0.70254809
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72900 * 0.38973974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49850 * 0.48670168
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65479 * 0.11644267
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38836 * 0.54290306
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27530 * 0.73263296
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45578 * 0.77766151
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3683 * 0.15125269
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68348 * 0.19512580
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1339 * 0.02856410
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92252 * 0.89272563
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22690 * 0.73485188
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78966 * 0.93717366
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46849 * 0.19724786
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1422 * 0.76691271
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60848 * 0.83258943
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52157 * 0.23966784
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43757 * 0.29754694
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 99978 * 0.46810237
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 871 * 0.71246374
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 85267 * 0.59019974
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xvgbskgc').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0068():
    """Extended test 68 for replication."""
    x_0 = 95193 * 0.60576916
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85951 * 0.08874422
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36567 * 0.36989159
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50262 * 0.67464191
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91568 * 0.61814357
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34150 * 0.44948332
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1400 * 0.95939588
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67286 * 0.04586759
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69726 * 0.84324061
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50012 * 0.42483253
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56531 * 0.77739381
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70202 * 0.22462543
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95976 * 0.36081558
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8252 * 0.00388274
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69018 * 0.41540148
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76515 * 0.71516524
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 230 * 0.46545231
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86680 * 0.90866126
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27466 * 0.98315255
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62321 * 0.48794246
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83580 * 0.18408878
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26684 * 0.60248059
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85873 * 0.30498723
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50343 * 0.95025794
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86542 * 0.73434092
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82417 * 0.98448309
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88281 * 0.22485867
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94418 * 0.48013941
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77317 * 0.13329044
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79040 * 0.96564442
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62877 * 0.51431963
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91311 * 0.24494297
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22659 * 0.94275119
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86107 * 0.02224823
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47467 * 0.70347196
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21267 * 0.19318194
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60416 * 0.75071094
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'cgoeakev').hexdigest()
    assert len(h) == 64

def test_replication_extended_0_0069():
    """Extended test 69 for replication."""
    x_0 = 71652 * 0.55558554
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32023 * 0.62728856
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1203 * 0.88302214
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37760 * 0.37127680
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12025 * 0.75148148
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65824 * 0.29244355
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94554 * 0.25977022
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27499 * 0.10633157
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3024 * 0.59272176
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42215 * 0.77436612
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24905 * 0.14358396
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63199 * 0.14609150
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1128 * 0.64016983
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46778 * 0.19265675
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31913 * 0.80206059
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7229 * 0.19908181
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28798 * 0.49952579
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57672 * 0.13180181
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46481 * 0.53889820
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9244 * 0.20355091
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46408 * 0.29622549
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86462 * 0.56106732
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45477 * 0.10938355
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27853 * 0.10709559
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20990 * 0.97051856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65733 * 0.70860516
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3349 * 0.71835729
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7725 * 0.69340301
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31775 * 0.66602678
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90777 * 0.65867369
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49989 * 0.36576938
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61943 * 0.06612565
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96710 * 0.52509814
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14329 * 0.49644937
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23318 * 0.65622229
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30748 * 0.44912543
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29583 * 0.70749335
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40123 * 0.83730644
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65347 * 0.12347999
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17218 * 0.77932234
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36432 * 0.09420409
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4762 * 0.81148936
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 61910 * 0.25117556
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 98831 * 0.96982450
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 63166 * 0.77187960
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 44195 * 0.04343472
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 65107 * 0.50858659
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 25572 * 0.67340853
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 16942 * 0.79973718
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 27341 * 0.79526383
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'punwizsm').hexdigest()
    assert len(h) == 64
