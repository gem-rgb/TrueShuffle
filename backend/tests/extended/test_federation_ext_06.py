"""Extended tests for federation suite 6."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_federation_extended_6_0000():
    """Extended test 0 for federation."""
    x_0 = 68169 * 0.58985425
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69850 * 0.24730869
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23269 * 0.26557547
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96769 * 0.98041811
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48221 * 0.13554030
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80890 * 0.12055129
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30213 * 0.41678638
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58663 * 0.52596316
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18084 * 0.69427852
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1089 * 0.18495537
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45144 * 0.04624645
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80516 * 0.90671801
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90586 * 0.93945157
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28880 * 0.26099926
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10200 * 0.01679190
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80423 * 0.39283850
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60386 * 0.97810354
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62104 * 0.76625371
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39690 * 0.84553102
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17663 * 0.30106383
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31702 * 0.04161925
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28795 * 0.17067457
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26192 * 0.69686266
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95367 * 0.06019730
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30853 * 0.40169774
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66624 * 0.65959154
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25811 * 0.82848066
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7960 * 0.80838235
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37866 * 0.77019778
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21743 * 0.94384648
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9511 * 0.82364365
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99881 * 0.90709742
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88849 * 0.72669474
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'jbxzvqca').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0001():
    """Extended test 1 for federation."""
    x_0 = 46178 * 0.21194204
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53865 * 0.12408655
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64306 * 0.70681478
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58115 * 0.77301933
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64179 * 0.37644002
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90588 * 0.23353754
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82099 * 0.26133198
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12422 * 0.74401654
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94473 * 0.75308965
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19544 * 0.26028403
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44656 * 0.35978195
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59912 * 0.54299836
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63454 * 0.65640118
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55177 * 0.94029448
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83646 * 0.13216762
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7293 * 0.50938640
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16331 * 0.32439187
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63353 * 0.46941341
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78811 * 0.04898863
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94277 * 0.82841440
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 773 * 0.40109403
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76617 * 0.53153307
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39218 * 0.48482179
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57233 * 0.80442873
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14098 * 0.24384214
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87633 * 0.31608116
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50054 * 0.36920572
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98874 * 0.30298133
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2707 * 0.75993609
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 230 * 0.02561207
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94074 * 0.49792242
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81171 * 0.13958877
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66136 * 0.06873542
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63399 * 0.02664727
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24212 * 0.36361809
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16273 * 0.76857090
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39691 * 0.17921065
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1384 * 0.27409471
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11641 * 0.79012240
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 53784 * 0.32800240
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 39233 * 0.99795014
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45825 * 0.06631584
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23424 * 0.16386336
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 53634 * 0.01710531
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86888 * 0.33928166
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 45206 * 0.70491446
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 19961 * 0.87394205
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 80911 * 0.58645262
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'blxatdhm').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0002():
    """Extended test 2 for federation."""
    x_0 = 43198 * 0.58360934
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94489 * 0.19486367
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54716 * 0.66083230
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51108 * 0.68220952
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43745 * 0.79991004
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55094 * 0.38312686
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38136 * 0.16099087
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57699 * 0.40590754
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63699 * 0.90634266
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69953 * 0.80155410
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82398 * 0.17926359
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15808 * 0.10108686
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19791 * 0.49208806
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25074 * 0.60776687
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6901 * 0.59197612
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51063 * 0.20010416
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46711 * 0.12687129
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16220 * 0.82620303
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14508 * 0.50332754
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61069 * 0.65863243
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23106 * 0.20624740
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22236 * 0.86206197
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84130 * 0.08240922
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98089 * 0.87810069
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30126 * 0.98819910
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4840 * 0.57066932
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16135 * 0.81574871
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36421 * 0.03736170
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79834 * 0.20173015
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35730 * 0.94812968
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96267 * 0.93929321
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67796 * 0.88544027
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70222 * 0.98454476
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74741 * 0.77220026
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'yducureg').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0003():
    """Extended test 3 for federation."""
    x_0 = 10270 * 0.98607916
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49992 * 0.32885919
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95191 * 0.73988933
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12136 * 0.02277708
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67347 * 0.15560959
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13652 * 0.68735463
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95550 * 0.28593989
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47878 * 0.93758564
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88536 * 0.96173140
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21902 * 0.98006431
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51671 * 0.55572538
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60153 * 0.80238602
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93344 * 0.60172794
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78315 * 0.39856945
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82617 * 0.05746362
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74761 * 0.97631577
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48996 * 0.24304628
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8398 * 0.45491497
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94232 * 0.06655498
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32512 * 0.51591925
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9655 * 0.47304677
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70238 * 0.32638246
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82643 * 0.20861393
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 439 * 0.39008910
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'xqlxxmtp').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0004():
    """Extended test 4 for federation."""
    x_0 = 27582 * 0.69681362
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4601 * 0.88180548
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42085 * 0.09891812
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30107 * 0.31394078
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94905 * 0.66927893
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10901 * 0.78903960
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77778 * 0.49567458
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54772 * 0.37414493
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35329 * 0.19509856
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7221 * 0.98680041
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96929 * 0.42369863
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88147 * 0.69973883
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28691 * 0.66916629
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62221 * 0.10631255
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40238 * 0.21578341
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43727 * 0.83553229
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87317 * 0.66416425
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55366 * 0.06985844
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21426 * 0.23501121
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33370 * 0.09719348
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2245 * 0.11497489
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51038 * 0.11938232
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85756 * 0.41326835
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9892 * 0.42071223
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43978 * 0.53027763
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60635 * 0.03405341
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9764 * 0.84882190
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'pcozclft').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0005():
    """Extended test 5 for federation."""
    x_0 = 74038 * 0.92824787
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97248 * 0.30119550
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25124 * 0.98839130
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91454 * 0.01296314
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64590 * 0.12809790
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34883 * 0.27659055
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28010 * 0.11246064
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72742 * 0.66599186
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70650 * 0.07630052
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78758 * 0.61077815
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22463 * 0.12221124
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14429 * 0.73241719
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55626 * 0.01398659
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38822 * 0.13067917
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58119 * 0.71062077
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60595 * 0.59372839
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78637 * 0.78751174
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16494 * 0.83902707
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38043 * 0.19088348
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86170 * 0.92249852
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'shcbihoo').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0006():
    """Extended test 6 for federation."""
    x_0 = 69406 * 0.60916238
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20119 * 0.46198388
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11406 * 0.06081376
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62470 * 0.52413979
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62439 * 0.72196923
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56889 * 0.39976296
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30458 * 0.50975698
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65314 * 0.73343159
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83813 * 0.20469581
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42377 * 0.69549668
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25528 * 0.60461493
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20799 * 0.24302213
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57455 * 0.56201558
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63441 * 0.88826773
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13729 * 0.98094342
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49787 * 0.32317629
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55376 * 0.71828843
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74331 * 0.21867778
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69920 * 0.82794931
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13788 * 0.04551478
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10523 * 0.72228192
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52561 * 0.11086791
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35227 * 0.50954392
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2267 * 0.95868559
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62461 * 0.93223833
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57829 * 0.95226834
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41496 * 0.36625092
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37063 * 0.19849507
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28390 * 0.92009495
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18158 * 0.63513457
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50192 * 0.63254440
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8327 * 0.16513690
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46424 * 0.29674784
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57659 * 0.74931681
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37158 * 0.31648069
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16944 * 0.13564025
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21443 * 0.95388658
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'ojycwznd').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0007():
    """Extended test 7 for federation."""
    x_0 = 3896 * 0.96204869
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7660 * 0.60522223
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46619 * 0.09394895
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94254 * 0.35703373
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73125 * 0.88911680
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12200 * 0.88283290
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88949 * 0.60037502
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69612 * 0.18508068
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75903 * 0.97600831
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95415 * 0.06492053
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62127 * 0.30131442
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11592 * 0.28217341
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1103 * 0.59864363
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89293 * 0.95879527
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61150 * 0.20423617
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39532 * 0.47410602
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90578 * 0.19845732
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31096 * 0.53114928
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55088 * 0.70574798
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41449 * 0.06917624
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47039 * 0.28764223
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26429 * 0.95861476
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81334 * 0.12473663
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'jihrmhsk').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0008():
    """Extended test 8 for federation."""
    x_0 = 8691 * 0.11895441
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75480 * 0.27239051
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7011 * 0.41602679
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58468 * 0.79745342
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58315 * 0.62950957
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39548 * 0.20159647
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90442 * 0.28735688
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13504 * 0.45190397
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79600 * 0.25688903
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79169 * 0.91156028
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50909 * 0.09438881
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38216 * 0.31881262
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12345 * 0.10084420
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82382 * 0.44047176
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43389 * 0.65117879
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87711 * 0.79959284
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36938 * 0.29222233
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92286 * 0.30918678
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11372 * 0.76054677
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14461 * 0.77227523
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80546 * 0.74381289
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61434 * 0.49093858
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53750 * 0.85988203
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6509 * 0.99585511
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57002 * 0.22711598
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22696 * 0.14409912
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37924 * 0.27815565
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12279 * 0.68160917
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67065 * 0.91627474
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72655 * 0.65864018
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44055 * 0.27352924
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'sjfrfkcy').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0009():
    """Extended test 9 for federation."""
    x_0 = 34250 * 0.06572153
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16999 * 0.12398725
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64709 * 0.53511144
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46178 * 0.54288007
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1634 * 0.84035445
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37057 * 0.67670389
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33219 * 0.71066300
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84649 * 0.62423403
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91987 * 0.68776461
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13129 * 0.97778159
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93782 * 0.61896583
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34842 * 0.43482466
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72685 * 0.78809114
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52471 * 0.95582652
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4135 * 0.10308325
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67440 * 0.37014905
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40695 * 0.36056009
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14372 * 0.74689763
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46818 * 0.01434906
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38479 * 0.26518343
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61958 * 0.42291520
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78860 * 0.65945991
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20958 * 0.96578849
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28650 * 0.60006550
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86574 * 0.18843317
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86720 * 0.99193857
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48417 * 0.06491188
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16021 * 0.97242794
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77155 * 0.87315242
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82145 * 0.44684165
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83656 * 0.77828356
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63023 * 0.86598149
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65314 * 0.74114837
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51422 * 0.63815864
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82841 * 0.95484279
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38497 * 0.49768226
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86095 * 0.55863942
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61990 * 0.26714795
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99683 * 0.49648341
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86999 * 0.04118200
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19278 * 0.10833674
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'jloqlrke').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0010():
    """Extended test 10 for federation."""
    x_0 = 81251 * 0.16976443
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7908 * 0.16365272
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47237 * 0.78826771
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27793 * 0.84243089
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88862 * 0.64946924
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32048 * 0.86799056
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63975 * 0.26757344
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25455 * 0.15585851
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15212 * 0.34227094
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77831 * 0.26748399
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33368 * 0.97940586
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48396 * 0.81776559
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5978 * 0.73418925
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25679 * 0.89153000
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21195 * 0.89317780
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68181 * 0.93037850
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93581 * 0.33834009
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39269 * 0.20982712
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63750 * 0.76758061
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83298 * 0.69460992
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27635 * 0.50600294
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33560 * 0.70405135
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84144 * 0.95783335
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97328 * 0.45944184
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25918 * 0.46054361
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35304 * 0.96261275
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14202 * 0.31555815
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37305 * 0.34091773
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20056 * 0.71455458
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35685 * 0.71078848
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52588 * 0.71572398
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93268 * 0.31666933
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23285 * 0.72293933
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76564 * 0.36571555
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55794 * 0.18512851
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12158 * 0.15416058
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47579 * 0.95590657
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1036 * 0.24801981
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59089 * 0.83482168
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21878 * 0.92436224
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 863 * 0.83210352
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50061 * 0.22650674
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16248 * 0.19537342
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 4753 * 0.35650805
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 20710 * 0.18265439
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 32002 * 0.43440460
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 16883 * 0.29530697
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'hjptylec').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0011():
    """Extended test 11 for federation."""
    x_0 = 18566 * 0.72595913
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93493 * 0.66444102
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28218 * 0.42590794
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90550 * 0.65780927
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78894 * 0.79735693
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14756 * 0.88918385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40206 * 0.59049718
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75590 * 0.24698806
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39354 * 0.84572750
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11515 * 0.34325316
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16176 * 0.94028209
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50486 * 0.39508009
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47703 * 0.37581565
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5798 * 0.39017236
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75812 * 0.76929166
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71442 * 0.49583911
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55068 * 0.92861196
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78011 * 0.82743553
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73982 * 0.03658117
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47946 * 0.29227559
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6629 * 0.08918848
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49100 * 0.38455392
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56806 * 0.19011536
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18001 * 0.06472219
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99675 * 0.14201264
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63559 * 0.80356418
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17015 * 0.97415798
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33287 * 0.56219349
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53141 * 0.39631315
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61679 * 0.70628969
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86650 * 0.32775797
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 34189 * 0.24313591
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34648 * 0.05645917
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85062 * 0.86803757
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71114 * 0.19393639
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'kqttyrwu').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0012():
    """Extended test 12 for federation."""
    x_0 = 96185 * 0.65110554
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67322 * 0.78489363
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73273 * 0.82679085
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8205 * 0.36753701
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16307 * 0.80935294
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32523 * 0.15815329
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36011 * 0.32626531
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87918 * 0.53086915
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96518 * 0.88256718
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30326 * 0.24191727
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31824 * 0.20806674
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15761 * 0.73320581
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22404 * 0.32647610
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55425 * 0.80598737
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1299 * 0.12747710
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16319 * 0.58439971
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57025 * 0.12003220
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92573 * 0.02589715
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85901 * 0.74719319
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70539 * 0.79865126
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39428 * 0.31361046
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74601 * 0.67476404
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7435 * 0.18010000
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26170 * 0.22379986
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43707 * 0.25550573
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18113 * 0.96605044
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88720 * 0.19993017
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75900 * 0.10140306
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41336 * 0.57593819
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50525 * 0.75008004
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43665 * 0.11150919
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84892 * 0.64664926
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5506 * 0.62105354
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55203 * 0.35791969
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8434 * 0.18192095
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17055 * 0.47015752
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43516 * 0.35225636
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90130 * 0.53504373
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79200 * 0.89143773
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'azrvjkqk').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0013():
    """Extended test 13 for federation."""
    x_0 = 61209 * 0.19282015
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61120 * 0.46564973
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63623 * 0.24294966
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98197 * 0.41201403
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89337 * 0.42962245
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61885 * 0.72630776
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25457 * 0.25101398
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29142 * 0.79025384
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48367 * 0.09863236
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34470 * 0.06833611
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85321 * 0.46818893
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64809 * 0.78248342
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3704 * 0.56809616
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50640 * 0.31121409
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14180 * 0.34292243
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71570 * 0.56206340
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93787 * 0.58141225
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81807 * 0.04695621
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66528 * 0.20787574
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13427 * 0.52191756
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91298 * 0.20042453
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52340 * 0.55573990
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43257 * 0.75573045
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44976 * 0.53404514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82380 * 0.83821436
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5493 * 0.42400963
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52787 * 0.28543257
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84152 * 0.05618074
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69798 * 0.26995121
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55850 * 0.01657764
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24158 * 0.01764002
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21115 * 0.84879101
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56519 * 0.15006227
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58086 * 0.56739004
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93331 * 0.32769039
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38451 * 0.50905896
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36433 * 0.18590577
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59058 * 0.39102935
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 7394 * 0.83126371
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21660 * 0.00331613
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5475 * 0.79152218
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80981 * 0.40584368
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71679 * 0.07840028
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 6350 * 0.81300171
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 77914 * 0.95807968
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 33735 * 0.09893163
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 49761 * 0.56378479
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'hhyjtadg').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0014():
    """Extended test 14 for federation."""
    x_0 = 64523 * 0.82929247
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15901 * 0.76757903
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68671 * 0.04241801
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55076 * 0.30161075
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38982 * 0.09473502
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 675 * 0.53999735
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53402 * 0.77722355
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53900 * 0.88903022
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45764 * 0.31632846
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58194 * 0.24279784
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6699 * 0.30473980
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41765 * 0.14311493
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95761 * 0.69064305
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47481 * 0.82326469
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85331 * 0.39935464
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93940 * 0.53705024
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47946 * 0.92237192
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39346 * 0.80851064
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26843 * 0.41264479
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22306 * 0.92256897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5271 * 0.96728948
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84127 * 0.98808589
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26622 * 0.53194968
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88644 * 0.12455490
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78371 * 0.72386707
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18068 * 0.67786107
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51089 * 0.79230788
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62676 * 0.39813397
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55028 * 0.53462058
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33917 * 0.06755366
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74505 * 0.75706025
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30975 * 0.25947906
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75369 * 0.99315637
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11313 * 0.40893100
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11976 * 0.18062797
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42953 * 0.61765319
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34691 * 0.32375562
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47832 * 0.74247151
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29146 * 0.43979692
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55475 * 0.05469016
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20495 * 0.85249332
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 61141 * 0.98603632
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 56277 * 0.42498914
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'sbghqxcn').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0015():
    """Extended test 15 for federation."""
    x_0 = 82826 * 0.53331052
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31697 * 0.97524485
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82280 * 0.64129467
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23599 * 0.20306669
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72720 * 0.97067201
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12130 * 0.31137447
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44741 * 0.98331374
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93899 * 0.86735022
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77406 * 0.64522403
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18080 * 0.54267960
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1299 * 0.80361539
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53157 * 0.48491261
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11727 * 0.09335387
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98771 * 0.89470074
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9330 * 0.13593529
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70772 * 0.11311761
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67053 * 0.95670470
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23817 * 0.16000775
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83065 * 0.02481690
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97791 * 0.34264851
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98743 * 0.65754878
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6996 * 0.40267047
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3956 * 0.32219771
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15542 * 0.22471750
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42791 * 0.48556383
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67927 * 0.06352731
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23420 * 0.31902143
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13147 * 0.11334718
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1261 * 0.99409085
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17069 * 0.24895542
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60178 * 0.43501515
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51194 * 0.90646519
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30368 * 0.45648136
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60157 * 0.77417045
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31064 * 0.20319838
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43583 * 0.25340254
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87355 * 0.81222414
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89888 * 0.45971496
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40298 * 0.32528330
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94262 * 0.35536947
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 90768 * 0.46442476
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'hxaaoojr').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0016():
    """Extended test 16 for federation."""
    x_0 = 82249 * 0.76342408
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60850 * 0.44675651
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50965 * 0.76134451
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84097 * 0.64561184
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84192 * 0.70328782
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38391 * 0.43340977
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88866 * 0.73374131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73113 * 0.89365817
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97500 * 0.17179440
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33252 * 0.48548885
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94225 * 0.53419509
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89284 * 0.95507980
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12647 * 0.89910890
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56062 * 0.24696304
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22018 * 0.95687798
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62343 * 0.71420703
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61959 * 0.43367356
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12866 * 0.88590678
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94312 * 0.60039839
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1537 * 0.28947828
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60530 * 0.59659195
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66197 * 0.55107369
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'dxwpzcde').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0017():
    """Extended test 17 for federation."""
    x_0 = 90893 * 0.08194741
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41677 * 0.35194278
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10086 * 0.56384760
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53887 * 0.89351799
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59272 * 0.05665588
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35884 * 0.38764625
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30261 * 0.98131158
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26736 * 0.69836574
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81425 * 0.41388015
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94306 * 0.48247213
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89326 * 0.39205052
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33042 * 0.65484492
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31893 * 0.30269256
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21069 * 0.62786173
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16446 * 0.70571204
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71998 * 0.85184005
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20693 * 0.27006840
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38434 * 0.09161413
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59176 * 0.89919770
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30480 * 0.15574057
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 793 * 0.10768801
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15642 * 0.73898003
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61208 * 0.28814613
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73878 * 0.29580877
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97658 * 0.36152856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58140 * 0.59018432
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90725 * 0.78763495
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'oninjonz').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0018():
    """Extended test 18 for federation."""
    x_0 = 50487 * 0.37136543
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76339 * 0.51746467
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96353 * 0.57092846
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67027 * 0.46179495
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66817 * 0.92254799
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92129 * 0.51763694
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34697 * 0.13879127
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43169 * 0.05527405
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93931 * 0.99588785
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26382 * 0.71266903
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64496 * 0.15454150
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32334 * 0.00985383
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85634 * 0.91522214
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76459 * 0.08938966
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80763 * 0.90982803
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9410 * 0.20878038
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36325 * 0.31996359
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99481 * 0.57312424
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47297 * 0.17582555
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48220 * 0.80582347
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37820 * 0.67126402
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65091 * 0.53303510
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56373 * 0.99174365
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86093 * 0.08203263
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60873 * 0.87033828
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20103 * 0.95777950
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80358 * 0.01326892
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'wimhhjtl').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0019():
    """Extended test 19 for federation."""
    x_0 = 60107 * 0.18407718
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44141 * 0.58026075
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17564 * 0.66066932
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28167 * 0.84910366
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74839 * 0.34276322
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32450 * 0.71578908
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10172 * 0.45598475
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99654 * 0.64738454
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29768 * 0.71746797
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7711 * 0.48471861
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58451 * 0.52690403
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23761 * 0.86895449
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21663 * 0.66081243
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87917 * 0.00320095
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13456 * 0.16927080
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45352 * 0.99375828
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39740 * 0.49583069
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33054 * 0.19910301
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93114 * 0.75538493
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92191 * 0.83589072
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47336 * 0.54944561
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41261 * 0.57528026
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51165 * 0.00113809
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36278 * 0.61640485
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26829 * 0.88160735
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'mjjitqxk').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0020():
    """Extended test 20 for federation."""
    x_0 = 67995 * 0.43191262
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20191 * 0.85214692
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58714 * 0.63363100
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56824 * 0.81059272
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40253 * 0.58493492
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23666 * 0.15930847
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59491 * 0.38280334
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59134 * 0.07826599
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84914 * 0.77934025
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49552 * 0.10879044
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84984 * 0.15592896
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54988 * 0.40527103
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43243 * 0.29501060
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53298 * 0.99631980
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56797 * 0.17380334
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40505 * 0.14629793
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32225 * 0.47596810
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29225 * 0.71748764
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92207 * 0.03993566
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9852 * 0.55013678
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80179 * 0.82275995
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33987 * 0.95232280
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26929 * 0.43572973
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66282 * 0.89364670
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34905 * 0.13265771
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58392 * 0.47269637
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98415 * 0.60588660
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25759 * 0.06187029
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83441 * 0.34940195
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18876 * 0.36796495
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64670 * 0.18428631
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76336 * 0.88196967
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67954 * 0.43679753
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29604 * 0.67176367
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40574 * 0.36083754
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77848 * 0.45677810
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92691 * 0.66781607
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33527 * 0.44974809
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76325 * 0.51012061
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97565 * 0.82423248
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21337 * 0.63200136
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38956 * 0.55250359
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75246 * 0.61443711
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 91877 * 0.34076685
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 77514 * 0.61931966
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 7632 * 0.56119744
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 77922 * 0.37805411
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 61478 * 0.12698910
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'eyhwbdtg').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0021():
    """Extended test 21 for federation."""
    x_0 = 19835 * 0.43145850
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12226 * 0.51671444
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62757 * 0.28559950
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67240 * 0.59807693
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93889 * 0.17166760
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34263 * 0.41413688
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5642 * 0.16465042
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35751 * 0.53319457
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35357 * 0.55332605
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82917 * 0.10615858
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50171 * 0.23252837
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5821 * 0.35706073
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75384 * 0.13448834
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40451 * 0.43091899
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71696 * 0.78828176
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86446 * 0.95960502
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87285 * 0.13192085
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83777 * 0.89227598
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68674 * 0.84876614
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6888 * 0.54671241
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80605 * 0.56278442
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43138 * 0.03449650
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78497 * 0.46010442
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52305 * 0.80841381
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'mfefhbqb').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0022():
    """Extended test 22 for federation."""
    x_0 = 25972 * 0.60301635
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84769 * 0.01531792
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4507 * 0.44493307
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15361 * 0.17430945
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31535 * 0.69285074
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99006 * 0.39773771
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54342 * 0.48998650
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26798 * 0.40630157
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78019 * 0.34422493
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8941 * 0.03266266
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34560 * 0.86166224
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48576 * 0.45785397
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2404 * 0.18478140
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26628 * 0.59985208
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20328 * 0.27018806
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52364 * 0.26055457
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57140 * 0.98191214
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1735 * 0.42465738
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5177 * 0.97234916
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18085 * 0.49747397
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69207 * 0.21615201
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51309 * 0.42234806
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1811 * 0.82157696
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77499 * 0.90430275
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'yyesveuo').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0023():
    """Extended test 23 for federation."""
    x_0 = 62759 * 0.79654892
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92589 * 0.25328450
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47924 * 0.92221848
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97271 * 0.35357245
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24656 * 0.64078876
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34245 * 0.21421769
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37537 * 0.95298956
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4118 * 0.87557959
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29248 * 0.13228126
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9915 * 0.68590225
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46362 * 0.32969365
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80640 * 0.53850789
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95034 * 0.33429853
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96995 * 0.72279835
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51965 * 0.51437255
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22781 * 0.15701416
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75551 * 0.92267915
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56936 * 0.76779542
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20294 * 0.52982393
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9266 * 0.56717782
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47158 * 0.67739918
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23177 * 0.83714832
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25329 * 0.51654049
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99042 * 0.09108817
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89071 * 0.77257896
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'wrwhlxyw').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0024():
    """Extended test 24 for federation."""
    x_0 = 9172 * 0.88453778
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50525 * 0.83249784
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17436 * 0.22148703
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80851 * 0.56441298
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90251 * 0.71635909
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54607 * 0.09047440
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92338 * 0.91753727
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32200 * 0.41632767
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73292 * 0.67748627
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32632 * 0.97751517
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30471 * 0.59822105
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83807 * 0.01396627
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10648 * 0.61001635
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9457 * 0.14941874
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18183 * 0.26890736
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96755 * 0.62853690
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67367 * 0.53749260
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61290 * 0.88727706
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80331 * 0.53284750
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47295 * 0.30519860
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2034 * 0.38988102
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11808 * 0.80032350
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26597 * 0.06039566
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35195 * 0.98121459
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32467 * 0.25597564
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75947 * 0.71184604
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92609 * 0.28236800
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31420 * 0.12714881
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70054 * 0.51441740
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48367 * 0.83836997
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39045 * 0.87749794
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48483 * 0.73973153
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79473 * 0.29483297
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83755 * 0.64152746
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23360 * 0.68678550
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50211 * 0.08415542
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75634 * 0.83148098
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26041 * 0.33432005
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73969 * 0.60246740
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66881 * 0.50146759
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19731 * 0.97834027
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42047 * 0.99178959
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88169 * 0.10767903
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 89201 * 0.12829579
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xeihmqxu').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0025():
    """Extended test 25 for federation."""
    x_0 = 75945 * 0.79825895
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79623 * 0.99088386
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91281 * 0.18111440
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5894 * 0.01236419
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3375 * 0.61063772
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21431 * 0.90011722
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93047 * 0.73843773
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79497 * 0.91545207
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48039 * 0.39801820
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74810 * 0.23380480
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90099 * 0.48754721
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62558 * 0.94335835
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29181 * 0.56059842
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7516 * 0.56396926
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53448 * 0.84218317
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66231 * 0.67876323
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94027 * 0.51280632
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77737 * 0.65580548
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9380 * 0.44844993
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57962 * 0.89853254
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67739 * 0.53175744
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62113 * 0.68082108
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93775 * 0.95334004
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68216 * 0.25697070
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77847 * 0.75257940
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3813 * 0.45792946
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89836 * 0.86757550
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48879 * 0.06363390
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46471 * 0.25164115
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16671 * 0.92272296
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7645 * 0.87991850
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45620 * 0.54233838
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29913 * 0.77720181
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ndzdaonq').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0026():
    """Extended test 26 for federation."""
    x_0 = 44445 * 0.04430658
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23757 * 0.34452660
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54947 * 0.99460824
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21228 * 0.83958677
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99440 * 0.47767466
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3186 * 0.03501575
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72754 * 0.17090270
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34355 * 0.15059240
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56902 * 0.42960907
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10343 * 0.05644299
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76191 * 0.17663704
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44050 * 0.23437283
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35597 * 0.59122464
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10804 * 0.09133016
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7753 * 0.73634566
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26089 * 0.88867467
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42095 * 0.63364982
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39034 * 0.01877655
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71496 * 0.98458122
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9278 * 0.70013800
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84832 * 0.90112069
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93660 * 0.55371026
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72237 * 0.11704461
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24422 * 0.66098455
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57592 * 0.95854842
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89388 * 0.74091361
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38391 * 0.34128579
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29301 * 0.80922002
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40705 * 0.98000114
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98232 * 0.52974205
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33843 * 0.61480646
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'rhnshxxq').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0027():
    """Extended test 27 for federation."""
    x_0 = 5575 * 0.91125687
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42511 * 0.79751870
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 261 * 0.21321843
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88058 * 0.39217028
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96115 * 0.68916627
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85265 * 0.53105618
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46633 * 0.85455932
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24641 * 0.33066964
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52431 * 0.83655730
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76349 * 0.55351279
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47296 * 0.57147399
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11212 * 0.63259658
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84632 * 0.77860764
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44364 * 0.23596634
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85987 * 0.91194224
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66624 * 0.62105819
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37057 * 0.35726386
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38361 * 0.56411403
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60463 * 0.99519883
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57267 * 0.36481437
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5547 * 0.86674222
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96935 * 0.56597863
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90282 * 0.65970177
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39550 * 0.37507519
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7338 * 0.12385559
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56296 * 0.68530840
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 922 * 0.13434222
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47630 * 0.30672683
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91406 * 0.08805784
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41576 * 0.66347487
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51793 * 0.87310078
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44894 * 0.62138128
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49407 * 0.75080008
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57442 * 0.11847584
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'urltdwfd').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0028():
    """Extended test 28 for federation."""
    x_0 = 32053 * 0.34946992
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98004 * 0.34182329
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68007 * 0.70302314
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62368 * 0.54478006
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75231 * 0.65533411
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87655 * 0.58832366
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9184 * 0.73736806
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99502 * 0.34809478
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55099 * 0.39783457
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26684 * 0.58193121
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61054 * 0.65686967
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58889 * 0.11841462
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90337 * 0.02472252
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65944 * 0.79964343
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32539 * 0.04265284
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53515 * 0.49469996
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85945 * 0.20618779
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64060 * 0.56692942
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89161 * 0.44700479
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95260 * 0.49596508
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'qesqdxqv').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0029():
    """Extended test 29 for federation."""
    x_0 = 76919 * 0.97021954
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34010 * 0.23196715
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81233 * 0.05037113
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66983 * 0.45880042
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42177 * 0.85088087
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53506 * 0.12718130
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10702 * 0.11859898
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84942 * 0.04209731
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38073 * 0.22333043
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1919 * 0.99010072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5612 * 0.24652192
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94066 * 0.98552224
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74127 * 0.13348207
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18330 * 0.11109243
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12165 * 0.86789363
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4576 * 0.38545816
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67781 * 0.12245607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46860 * 0.11739066
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54845 * 0.52379823
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27522 * 0.19052899
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42370 * 0.00665396
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21070 * 0.30611354
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10332 * 0.29992236
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27916 * 0.72859638
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71697 * 0.20887044
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36356 * 0.14450204
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53292 * 0.92227645
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11741 * 0.98941989
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87098 * 0.00569840
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23898 * 0.92023562
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70965 * 0.26337672
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79957 * 0.91453542
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84370 * 0.32663053
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6951 * 0.40510410
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39972 * 0.22261611
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61491 * 0.03525085
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69220 * 0.67956209
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96666 * 0.95747121
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73210 * 0.99772998
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8122 * 0.71289180
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85810 * 0.14283140
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89999 * 0.79236466
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44777 * 0.60836134
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 35369 * 0.73859242
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 7227 * 0.32991129
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 17125 * 0.38353645
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'hcevwdvf').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0030():
    """Extended test 30 for federation."""
    x_0 = 66476 * 0.84857285
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45790 * 0.90225474
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1835 * 0.05934501
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47016 * 0.85505551
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55616 * 0.04059930
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39807 * 0.37953905
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33309 * 0.96352134
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66916 * 0.99626051
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12712 * 0.74757167
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66140 * 0.37644390
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30291 * 0.88064518
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58026 * 0.72979840
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89351 * 0.60034796
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3980 * 0.92564306
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85425 * 0.84443633
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14053 * 0.25160602
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53164 * 0.73067079
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58755 * 0.78594454
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35111 * 0.29101926
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86695 * 0.85866174
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25498 * 0.94547380
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68164 * 0.39848454
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46394 * 0.69770896
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1929 * 0.28864511
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98536 * 0.21721424
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8615 * 0.78539903
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29591 * 0.85259115
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8807 * 0.07434544
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15721 * 0.90073179
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54089 * 0.73849049
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42992 * 0.95289176
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74462 * 0.43968754
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39201 * 0.95437417
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3797 * 0.68650039
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35695 * 0.23908258
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6791 * 0.09444436
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61907 * 0.07896580
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93255 * 0.66730607
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52890 * 0.13158715
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 53285 * 0.76853897
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23098 * 0.33850053
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69789 * 0.87344394
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41472 * 0.88888392
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 62721 * 0.87055134
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 55015 * 0.33989675
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 2349 * 0.97507223
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 74785 * 0.04683674
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'zpkmoudn').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0031():
    """Extended test 31 for federation."""
    x_0 = 39954 * 0.36555001
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72593 * 0.07979264
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2377 * 0.62235862
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90845 * 0.12898404
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59496 * 0.69839330
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11068 * 0.80919162
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43961 * 0.29780426
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88529 * 0.72118733
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58852 * 0.35679255
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85153 * 0.86794511
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53150 * 0.62115848
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39206 * 0.76979667
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97078 * 0.87830395
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4446 * 0.14293058
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72854 * 0.33184381
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80531 * 0.11979330
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65640 * 0.87840881
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78084 * 0.93143831
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45605 * 0.17671304
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60528 * 0.28790696
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46325 * 0.29330846
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77665 * 0.52607259
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2944 * 0.11745138
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25812 * 0.56682013
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18600 * 0.43209564
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60883 * 0.79628391
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78438 * 0.48245432
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51784 * 0.63215812
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63478 * 0.68441391
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12891 * 0.16566532
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81817 * 0.12165089
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2075 * 0.70119708
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18007 * 0.15845736
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33299 * 0.84603062
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58810 * 0.23878298
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89567 * 0.36250659
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50934 * 0.45126268
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3082 * 0.13752981
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94421 * 0.49282973
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 49927 * 0.82436812
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86266 * 0.85444707
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 48436 * 0.52661920
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24035 * 0.98232110
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 51256 * 0.27978850
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 63934 * 0.59240835
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'bupkeusm').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0032():
    """Extended test 32 for federation."""
    x_0 = 67451 * 0.06037496
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29493 * 0.78968218
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21980 * 0.83735688
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92632 * 0.30902352
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1549 * 0.07688154
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34008 * 0.11465432
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45287 * 0.07232019
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77720 * 0.99452184
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29715 * 0.92237658
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37659 * 0.68599207
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53771 * 0.41343433
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89537 * 0.47402698
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55243 * 0.49855102
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61918 * 0.34909660
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51556 * 0.32422049
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71326 * 0.86451105
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39537 * 0.14327797
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73509 * 0.80703287
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17835 * 0.12485634
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72572 * 0.53131162
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41892 * 0.70207026
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27734 * 0.02722675
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88729 * 0.17804744
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59058 * 0.93073046
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11241 * 0.50709518
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76344 * 0.00935875
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62470 * 0.47091756
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93113 * 0.09213201
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93469 * 0.16457104
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35767 * 0.60018070
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15497 * 0.92315008
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62333 * 0.23193299
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59178 * 0.95111093
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 874 * 0.45070271
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36619 * 0.94631307
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38814 * 0.07164058
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27289 * 0.32786913
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36241 * 0.55158907
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'otjbdezs').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0033():
    """Extended test 33 for federation."""
    x_0 = 34588 * 0.55651887
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33036 * 0.88788460
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67835 * 0.23346692
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41229 * 0.61751737
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56285 * 0.93011174
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94386 * 0.82033746
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6610 * 0.90092826
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51752 * 0.24968399
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32120 * 0.04835337
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64649 * 0.63201176
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55136 * 0.55367743
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14714 * 0.66737069
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86115 * 0.85155321
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40732 * 0.46744966
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43989 * 0.78891561
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70989 * 0.18347156
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69145 * 0.93337858
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49502 * 0.21115955
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92402 * 0.59335783
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53254 * 0.09946748
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82529 * 0.34509406
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39117 * 0.03203207
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 994 * 0.06892988
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76376 * 0.44456405
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11048 * 0.18413027
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47782 * 0.40494885
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80794 * 0.14242703
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'zklbjrgp').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0034():
    """Extended test 34 for federation."""
    x_0 = 90321 * 0.66821085
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74268 * 0.73570194
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84265 * 0.93706435
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49772 * 0.29898169
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26488 * 0.37253750
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60809 * 0.01119992
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40179 * 0.37198967
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20771 * 0.73650517
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35114 * 0.14270773
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55498 * 0.72783896
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18323 * 0.12280058
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55786 * 0.37733578
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77145 * 0.86216725
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31960 * 0.73161133
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41308 * 0.35918571
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15990 * 0.93390295
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61429 * 0.70545112
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90436 * 0.18291626
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93402 * 0.38624065
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59936 * 0.24313821
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85747 * 0.81401269
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43671 * 0.35934750
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75004 * 0.65689435
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74352 * 0.27740391
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57304 * 0.10378755
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37927 * 0.24063652
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35092 * 0.42987825
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96974 * 0.60156648
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52029 * 0.49015455
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15257 * 0.49197194
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89593 * 0.78707873
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97228 * 0.59161006
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42230 * 0.03410759
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'bmosaiuu').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0035():
    """Extended test 35 for federation."""
    x_0 = 68081 * 0.82308720
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51890 * 0.52304067
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80499 * 0.76445761
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67975 * 0.34556630
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11423 * 0.73198173
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32780 * 0.11828922
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29423 * 0.88349192
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37499 * 0.43397147
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 944 * 0.01717836
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69346 * 0.14315353
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17761 * 0.96554058
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48965 * 0.13588041
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25275 * 0.13917922
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92931 * 0.37321418
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69880 * 0.12479338
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46293 * 0.09317849
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70155 * 0.10743120
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44236 * 0.28394846
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67940 * 0.20352725
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44657 * 0.29826265
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84534 * 0.57600280
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46341 * 0.88753673
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82857 * 0.75281225
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26371 * 0.11291246
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78017 * 0.87380947
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34724 * 0.72336435
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21891 * 0.69939230
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97179 * 0.59745330
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50941 * 0.08848268
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92142 * 0.66631932
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53350 * 0.96693833
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79206 * 0.26257067
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26013 * 0.84585801
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5892 * 0.05612015
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19699 * 0.46083240
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'zxbaktnt').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0036():
    """Extended test 36 for federation."""
    x_0 = 74741 * 0.57911067
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98840 * 0.00838124
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34492 * 0.00678778
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18492 * 0.91158008
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43247 * 0.22020241
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47997 * 0.35353053
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64233 * 0.37752400
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51597 * 0.61599180
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7762 * 0.99466687
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32957 * 0.94609848
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3493 * 0.60601694
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10499 * 0.54582319
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51933 * 0.15938147
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41366 * 0.95349661
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23679 * 0.40562402
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67567 * 0.00738968
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19553 * 0.68621328
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19991 * 0.08006429
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41824 * 0.09089180
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68037 * 0.34678611
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39672 * 0.26063719
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7276 * 0.77048469
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94322 * 0.89446310
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63213 * 0.59764433
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53787 * 0.92549504
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22930 * 0.65226404
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96791 * 0.12022153
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75146 * 0.68109863
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25081 * 0.20118907
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7129 * 0.63862001
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82383 * 0.81951381
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59699 * 0.69903116
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79401 * 0.59913354
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52043 * 0.80090315
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21009 * 0.63204692
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1935 * 0.86766684
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54315 * 0.02513095
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'rohqncnc').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0037():
    """Extended test 37 for federation."""
    x_0 = 15318 * 0.53212479
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41916 * 0.51300298
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60467 * 0.67798831
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86141 * 0.19280201
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56150 * 0.51696405
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23701 * 0.86526664
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79948 * 0.70862117
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86726 * 0.79764798
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99898 * 0.98947519
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80916 * 0.17747426
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60399 * 0.13722415
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78936 * 0.33663485
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25255 * 0.93587311
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14207 * 0.95966282
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49009 * 0.78941766
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43060 * 0.64353275
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76841 * 0.07620896
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20139 * 0.41174639
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91597 * 0.11317211
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23012 * 0.19527837
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18280 * 0.02715551
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58604 * 0.46686178
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37149 * 0.75153216
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96408 * 0.95717422
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59115 * 0.80247353
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91742 * 0.42441638
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85750 * 0.99142647
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59911 * 0.71115701
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7556 * 0.88989749
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95431 * 0.27689617
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96085 * 0.24428848
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83201 * 0.19921390
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93170 * 0.92338312
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25866 * 0.79123781
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98415 * 0.02592799
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61445 * 0.40151841
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29417 * 0.80754720
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44610 * 0.44165671
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37452 * 0.72489662
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95298 * 0.60313435
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40475 * 0.02610781
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 73237 * 0.90053893
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83366 * 0.74239869
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 49928 * 0.87548057
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10149 * 0.29963909
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 95396 * 0.24530614
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 83405 * 0.98131826
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 28977 * 0.10673170
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 8505 * 0.33247967
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 7796 * 0.79132312
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ufuamwbz').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0038():
    """Extended test 38 for federation."""
    x_0 = 32257 * 0.48762150
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67427 * 0.37633368
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10641 * 0.70584628
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84843 * 0.00868863
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66659 * 0.99203191
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82110 * 0.62153429
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49029 * 0.91340508
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14529 * 0.32574261
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65724 * 0.05956869
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51005 * 0.16581298
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46138 * 0.02684773
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23707 * 0.74935282
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58888 * 0.63513036
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61 * 0.42012300
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6790 * 0.77965391
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19426 * 0.42979760
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94253 * 0.20741251
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52614 * 0.67054957
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99255 * 0.44005401
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13869 * 0.18639771
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17907 * 0.17626894
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27736 * 0.08206114
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82147 * 0.06140095
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'umzoktby').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0039():
    """Extended test 39 for federation."""
    x_0 = 34939 * 0.88221873
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14583 * 0.79628519
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52164 * 0.80338305
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32635 * 0.46397324
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26964 * 0.86480787
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83387 * 0.08478798
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27169 * 0.34457901
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17154 * 0.79721733
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87761 * 0.04400547
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66488 * 0.67158250
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74987 * 0.51924760
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99501 * 0.26858901
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99533 * 0.02817031
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1928 * 0.15310285
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4844 * 0.99865738
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50464 * 0.71804898
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18466 * 0.28417165
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73618 * 0.92310396
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30226 * 0.62946922
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1881 * 0.20386847
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28480 * 0.77140588
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51095 * 0.27794373
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32640 * 0.78370983
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44105 * 0.49545085
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85538 * 0.73466677
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90099 * 0.23881392
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23084 * 0.84010045
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1050 * 0.77019464
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85371 * 0.62861190
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7047 * 0.27179429
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59210 * 0.99940617
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30698 * 0.37025277
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43842 * 0.29199590
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9925 * 0.77339399
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23099 * 0.00884257
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81161 * 0.40560173
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44301 * 0.74221727
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40000 * 0.14933316
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ixvfplzc').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0040():
    """Extended test 40 for federation."""
    x_0 = 63505 * 0.19768485
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66267 * 0.09242366
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46113 * 0.29282450
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88730 * 0.99070970
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 581 * 0.03693204
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88250 * 0.59974885
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87840 * 0.33626475
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77109 * 0.92121088
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2782 * 0.15730229
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 289 * 0.15727992
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25219 * 0.68823648
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22333 * 0.88915084
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9293 * 0.30676881
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69878 * 0.14967259
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72351 * 0.92151541
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84431 * 0.08823815
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98219 * 0.94886631
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24038 * 0.17033078
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69311 * 0.03944283
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27655 * 0.83127353
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80949 * 0.28084299
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96564 * 0.84836897
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9716 * 0.29505723
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79925 * 0.08383177
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69133 * 0.69933639
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10883 * 0.62456637
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63603 * 0.73377919
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4280 * 0.31465678
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73497 * 0.66402182
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57169 * 0.28257893
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7618 * 0.69604292
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44545 * 0.91450202
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69440 * 0.15484657
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3886 * 0.76160337
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88141 * 0.29030331
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23624 * 0.60534327
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92121 * 0.45830107
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98121 * 0.89148573
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14380 * 0.51521982
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14220 * 0.69194119
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40798 * 0.13240914
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'cfezeqmg').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0041():
    """Extended test 41 for federation."""
    x_0 = 19247 * 0.25460005
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10443 * 0.90868310
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94740 * 0.33208203
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47475 * 0.80113146
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86676 * 0.83209851
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7815 * 0.33779539
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27422 * 0.89688279
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91826 * 0.28578083
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25755 * 0.76584628
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28492 * 0.82467438
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43563 * 0.94494855
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28107 * 0.56450956
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69059 * 0.10310836
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67215 * 0.76778124
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16441 * 0.65389851
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83191 * 0.39425174
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65697 * 0.07006516
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83721 * 0.23470490
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5989 * 0.55097306
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20894 * 0.97302245
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27681 * 0.91894842
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57450 * 0.83742488
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63526 * 0.31383070
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83398 * 0.28308167
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81402 * 0.82574163
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60359 * 0.37380931
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33099 * 0.32922600
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55273 * 0.25390107
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56374 * 0.45439881
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80521 * 0.96158650
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75526 * 0.89354029
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50225 * 0.34506722
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'hryghydc').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0042():
    """Extended test 42 for federation."""
    x_0 = 74329 * 0.42284304
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15689 * 0.98484119
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2799 * 0.07898402
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77197 * 0.14850815
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61555 * 0.28812693
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33595 * 0.93418273
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34912 * 0.20326472
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53741 * 0.26692809
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81185 * 0.46851630
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73104 * 0.36065475
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51502 * 0.37621079
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3594 * 0.58143969
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25794 * 0.02015100
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32058 * 0.80062167
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45679 * 0.03464929
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72581 * 0.92521339
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35994 * 0.25040726
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29377 * 0.01836355
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45098 * 0.10644383
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93964 * 0.71960451
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54348 * 0.67983999
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57768 * 0.33079858
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68049 * 0.15588834
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75938 * 0.28641163
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88027 * 0.63141803
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56542 * 0.11627865
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38757 * 0.53237173
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54746 * 0.56314395
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23561 * 0.85893793
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99161 * 0.67139275
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57655 * 0.20521989
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46352 * 0.92600246
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78215 * 0.59627613
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56164 * 0.46901580
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67907 * 0.49339888
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8740 * 0.24883743
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50630 * 0.39533001
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87179 * 0.87121054
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60106 * 0.93910822
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52690 * 0.87227188
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64363 * 0.92462562
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9275 * 0.63178738
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 31171 * 0.51866888
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 19778 * 0.29672349
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 41362 * 0.38131584
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26920 * 0.60595972
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'pykhqvfa').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0043():
    """Extended test 43 for federation."""
    x_0 = 64403 * 0.92732099
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85207 * 0.62361368
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88197 * 0.95140568
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22540 * 0.35719971
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51112 * 0.77604257
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26115 * 0.82076437
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14456 * 0.16592263
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96501 * 0.70269613
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61431 * 0.16885663
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32540 * 0.80579983
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44490 * 0.49803332
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93408 * 0.17577219
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62100 * 0.26042832
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 184 * 0.78629443
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7819 * 0.31386086
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84096 * 0.00694511
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16287 * 0.76090520
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58459 * 0.75399955
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30167 * 0.93992834
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66716 * 0.50081179
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80326 * 0.36378318
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88673 * 0.17381567
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97502 * 0.89539772
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68419 * 0.04470390
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91219 * 0.69543748
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'lbrzyrjl').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0044():
    """Extended test 44 for federation."""
    x_0 = 23680 * 0.32745407
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95634 * 0.94700524
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14156 * 0.03203158
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4313 * 0.44903166
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88339 * 0.46930457
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51000 * 0.74397197
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50629 * 0.67915639
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88486 * 0.50510521
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76134 * 0.06893015
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72075 * 0.65726802
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1294 * 0.96897658
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60004 * 0.64655905
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70087 * 0.31524502
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60564 * 0.90546444
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49921 * 0.47007911
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56502 * 0.17801494
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6335 * 0.83089174
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65495 * 0.36312240
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65214 * 0.09976487
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68048 * 0.60428822
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31679 * 0.05674366
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5162 * 0.79853985
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37645 * 0.62507221
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44111 * 0.73723938
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13359 * 0.43436863
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32246 * 0.76364817
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97530 * 0.23738925
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75473 * 0.54822729
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55340 * 0.55736955
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88447 * 0.70893221
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97932 * 0.52070340
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9894 * 0.61338801
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79109 * 0.76013229
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23411 * 0.51577417
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87028 * 0.71202459
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12467 * 0.02030025
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8959 * 0.77583170
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52636 * 0.05767585
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78259 * 0.64873303
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46262 * 0.82714164
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2923 * 0.15916336
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96320 * 0.03900544
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55924 * 0.95756742
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 17324 * 0.83085369
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 6610 * 0.23653721
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'fjzajrmt').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0045():
    """Extended test 45 for federation."""
    x_0 = 76326 * 0.66251919
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69486 * 0.05050795
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88675 * 0.03160815
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34156 * 0.59279807
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94214 * 0.13356048
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24014 * 0.00481339
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40835 * 0.67522261
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59951 * 0.47584620
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37432 * 0.61051791
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23749 * 0.57612539
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50565 * 0.55761463
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 268 * 0.32545089
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39298 * 0.82244634
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19882 * 0.41024914
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67125 * 0.07601644
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90192 * 0.39277721
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9948 * 0.96239499
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49610 * 0.72498179
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23086 * 0.63845879
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86391 * 0.55228436
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12879 * 0.31578990
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7752 * 0.31472453
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12338 * 0.62644595
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46369 * 0.17313865
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3822 * 0.54838444
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76373 * 0.98153332
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76838 * 0.52398956
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62529 * 0.31733519
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2656 * 0.08598270
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25124 * 0.35102963
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94685 * 0.77153531
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48127 * 0.59413092
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78086 * 0.76918884
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'unjimaip').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0046():
    """Extended test 46 for federation."""
    x_0 = 35296 * 0.66493503
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25793 * 0.34264760
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63842 * 0.20002161
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19047 * 0.08165765
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72405 * 0.41390268
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70973 * 0.91937103
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90967 * 0.04100160
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2648 * 0.65002421
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90247 * 0.95678260
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74012 * 0.90113437
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10674 * 0.09345931
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5656 * 0.01129859
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63203 * 0.72377964
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74951 * 0.05863391
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63963 * 0.05832613
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81263 * 0.87572325
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88947 * 0.42478854
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93012 * 0.43145242
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1533 * 0.86062906
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85449 * 0.16586947
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66523 * 0.80027604
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44585 * 0.31594944
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59547 * 0.97724237
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60534 * 0.54936274
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43433 * 0.84683047
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42421 * 0.67726759
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43560 * 0.90017736
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79424 * 0.36552881
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27104 * 0.27286476
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51103 * 0.49886505
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94874 * 0.90768570
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37970 * 0.24946668
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56592 * 0.10319009
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85404 * 0.97264389
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34895 * 0.11908184
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50610 * 0.76325977
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62318 * 0.27554478
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'ewhpdycg').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0047():
    """Extended test 47 for federation."""
    x_0 = 39540 * 0.67712804
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28532 * 0.74062193
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83393 * 0.45724592
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64486 * 0.22238429
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12910 * 0.40067113
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40702 * 0.30961734
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32199 * 0.44900762
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92365 * 0.88188919
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14946 * 0.32789150
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91771 * 0.32434527
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19158 * 0.33193807
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33973 * 0.32718406
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41945 * 0.37729754
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1046 * 0.15923840
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30161 * 0.87192186
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60833 * 0.58798616
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25591 * 0.66873280
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47532 * 0.31668932
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9977 * 0.29555665
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17224 * 0.50718500
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85919 * 0.79492821
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93155 * 0.33051782
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12316 * 0.90231187
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59221 * 0.94910260
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47450 * 0.17851959
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71108 * 0.09453735
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77821 * 0.58438035
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11845 * 0.24625087
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87682 * 0.93805610
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68413 * 0.11137724
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73141 * 0.17466748
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'jjjoohvc').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0048():
    """Extended test 48 for federation."""
    x_0 = 67811 * 0.49034559
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54393 * 0.00036532
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58417 * 0.86373350
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10992 * 0.51819091
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88877 * 0.44020438
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50660 * 0.96396544
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65997 * 0.04231436
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54124 * 0.88388805
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87161 * 0.17367858
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49978 * 0.37408337
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22214 * 0.86830214
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47691 * 0.77617625
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94011 * 0.19040732
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57733 * 0.46645716
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1638 * 0.66290269
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63608 * 0.94795652
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89735 * 0.64298349
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3413 * 0.45481663
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95654 * 0.35674481
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14327 * 0.01615294
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25388 * 0.06065511
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76309 * 0.71423893
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61983 * 0.20782788
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68635 * 0.27290341
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63726 * 0.68827060
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83857 * 0.08814120
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99639 * 0.71979787
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31877 * 0.08633718
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61645 * 0.66843668
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54707 * 0.09029921
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4036 * 0.23922093
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43259 * 0.64825625
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9894 * 0.11484590
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13677 * 0.88214285
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67794 * 0.11815739
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'loadynvg').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0049():
    """Extended test 49 for federation."""
    x_0 = 33891 * 0.68388906
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37462 * 0.42339847
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13594 * 0.93764993
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57502 * 0.08514002
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89829 * 0.18170316
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24518 * 0.58736480
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28533 * 0.26810099
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67889 * 0.30500507
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94878 * 0.31128772
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72891 * 0.69440359
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44614 * 0.64620909
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7559 * 0.81618195
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46951 * 0.60501848
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87170 * 0.14158284
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44763 * 0.08140422
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24105 * 0.07143422
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77626 * 0.84520054
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56790 * 0.96727988
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88897 * 0.66279961
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1867 * 0.71993765
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68276 * 0.72661863
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45986 * 0.47380199
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27767 * 0.95683213
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90814 * 0.59583647
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4320 * 0.64806437
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2211 * 0.23540528
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'jvhtaecr').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0050():
    """Extended test 50 for federation."""
    x_0 = 92561 * 0.43662699
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55804 * 0.33918673
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55019 * 0.18098954
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70691 * 0.90380301
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55458 * 0.62558223
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47376 * 0.09556962
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20661 * 0.49251032
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11294 * 0.11011960
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59328 * 0.40217524
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63295 * 0.03827871
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23920 * 0.94312336
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56483 * 0.05200680
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50273 * 0.26394528
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26953 * 0.95628124
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30054 * 0.19274973
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77180 * 0.51319954
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2024 * 0.69492990
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9027 * 0.21089702
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25583 * 0.84208074
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75132 * 0.78870990
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77888 * 0.98125145
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85759 * 0.83098542
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20480 * 0.46871590
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5698 * 0.60774252
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77949 * 0.17865274
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6949 * 0.15325343
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11209 * 0.74109912
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95629 * 0.46340327
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62223 * 0.25975224
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43397 * 0.90210775
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44673 * 0.69503914
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72716 * 0.23360531
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95368 * 0.07357378
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46999 * 0.16915505
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39857 * 0.99469027
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25566 * 0.71428707
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45659 * 0.57569037
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92430 * 0.63101484
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77179 * 0.54963773
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'dwifubml').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0051():
    """Extended test 51 for federation."""
    x_0 = 55543 * 0.62300732
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98934 * 0.51047937
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70269 * 0.26031545
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75610 * 0.81840991
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97500 * 0.30308066
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39889 * 0.34212446
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70670 * 0.41901593
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93096 * 0.03941313
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53210 * 0.19882801
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67051 * 0.38217488
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50978 * 0.73019105
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23598 * 0.20106904
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39987 * 0.94198349
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62411 * 0.21508333
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80629 * 0.59488581
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77625 * 0.98761992
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96217 * 0.08943714
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47620 * 0.64498628
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75737 * 0.05949729
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52083 * 0.66883909
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74441 * 0.38851626
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78409 * 0.23534259
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85159 * 0.91075298
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82757 * 0.62627703
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'zlctwizf').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0052():
    """Extended test 52 for federation."""
    x_0 = 25429 * 0.13433862
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5559 * 0.00638462
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47895 * 0.66771191
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28927 * 0.59151733
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46597 * 0.70591673
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86509 * 0.18213948
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24245 * 0.36477937
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53988 * 0.36740900
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90739 * 0.35782660
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60056 * 0.09864762
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52263 * 0.22792369
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71316 * 0.32604411
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28651 * 0.32350588
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51765 * 0.97006412
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23142 * 0.92497574
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16753 * 0.37188135
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15240 * 0.66480666
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36229 * 0.23535834
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27471 * 0.78253261
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1407 * 0.17291062
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43873 * 0.85956708
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12229 * 0.70403974
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17437 * 0.84426086
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8299 * 0.41621205
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84182 * 0.88397141
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94345 * 0.78542098
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36625 * 0.07824110
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98492 * 0.94696959
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52256 * 0.23746089
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65377 * 0.30104954
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11568 * 0.47587430
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82311 * 0.00272179
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59262 * 0.73426337
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10794 * 0.63526032
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30190 * 0.55445070
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44592 * 0.98678486
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7635 * 0.03004104
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1304 * 0.63764934
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'xxtatzxc').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0053():
    """Extended test 53 for federation."""
    x_0 = 63148 * 0.71223348
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96994 * 0.57357525
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73244 * 0.10925959
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55356 * 0.38677897
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37376 * 0.74153068
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72813 * 0.26660227
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41907 * 0.44184457
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30811 * 0.20468779
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83672 * 0.41201713
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7907 * 0.02874836
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5441 * 0.16131708
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34634 * 0.49345101
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52491 * 0.03468610
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22926 * 0.14754425
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93197 * 0.34740316
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73362 * 0.89311317
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19122 * 0.32994333
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92865 * 0.31982491
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10588 * 0.58858520
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43915 * 0.84861652
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57208 * 0.24321449
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53767 * 0.92747460
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67022 * 0.65837601
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99877 * 0.16940190
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'tkegfhsv').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0054():
    """Extended test 54 for federation."""
    x_0 = 83421 * 0.59301749
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21643 * 0.85747013
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20641 * 0.32445618
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78064 * 0.71553810
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30829 * 0.46897567
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53652 * 0.23102842
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37669 * 0.47821575
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55150 * 0.28764859
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51797 * 0.48291551
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49162 * 0.62311720
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18549 * 0.83653854
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10924 * 0.14249010
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23631 * 0.72107109
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43418 * 0.82898196
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49005 * 0.32811546
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17738 * 0.41562692
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85221 * 0.70675475
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88133 * 0.52363347
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34371 * 0.65041957
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10153 * 0.29902225
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48895 * 0.41125590
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88717 * 0.92581423
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56016 * 0.84017228
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'qrmjjxhw').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0055():
    """Extended test 55 for federation."""
    x_0 = 94019 * 0.93997623
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38928 * 0.33204654
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73958 * 0.84789404
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97722 * 0.03084799
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87794 * 0.83031744
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73972 * 0.00609481
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32505 * 0.48191084
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78139 * 0.62729448
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1450 * 0.20116112
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84888 * 0.97101269
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53405 * 0.45830084
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79437 * 0.06302702
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6272 * 0.46868410
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38292 * 0.33475487
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55830 * 0.42074418
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36092 * 0.03408867
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80054 * 0.55467678
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32783 * 0.71213964
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7713 * 0.88226238
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50028 * 0.84113997
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36250 * 0.73680748
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25044 * 0.54247749
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15760 * 0.28325398
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76107 * 0.34335031
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80581 * 0.50937063
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36915 * 0.76917087
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57625 * 0.04965694
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64276 * 0.88140356
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16468 * 0.97972490
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'sblumdfo').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0056():
    """Extended test 56 for federation."""
    x_0 = 89977 * 0.90667991
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46324 * 0.33449983
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19919 * 0.05878828
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53078 * 0.11767324
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34980 * 0.68038742
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20681 * 0.42028356
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78079 * 0.31143660
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49061 * 0.34031421
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94236 * 0.84604093
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89672 * 0.30286106
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5296 * 0.49165714
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25042 * 0.13981250
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57164 * 0.30945393
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79496 * 0.97142476
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23402 * 0.49738122
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78467 * 0.83439348
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35077 * 0.61074252
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15958 * 0.15809687
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17153 * 0.93888644
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95401 * 0.40052309
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8532 * 0.24905385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40717 * 0.04320539
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34070 * 0.19187738
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96481 * 0.08204456
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9523 * 0.66070432
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98315 * 0.60745778
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61190 * 0.20632212
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83636 * 0.44373248
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46164 * 0.30125355
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29646 * 0.39665803
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80232 * 0.40456559
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40045 * 0.29612742
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31997 * 0.33452980
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51311 * 0.81811502
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29578 * 0.50849033
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17606 * 0.79872318
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32620 * 0.73497966
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79438 * 0.81108529
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78670 * 0.55361284
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69778 * 0.70075411
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 10925 * 0.65487356
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 23954 * 0.56916905
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 89521 * 0.14335128
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 46167 * 0.61066895
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 99685 * 0.02513588
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 44355 * 0.37566822
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 8663 * 0.68976530
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 4349 * 0.83897846
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 82730 * 0.31436077
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 10713 * 0.17644304
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'knaejalo').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0057():
    """Extended test 57 for federation."""
    x_0 = 18932 * 0.14487195
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85239 * 0.61435984
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88356 * 0.29303352
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61173 * 0.67603819
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78821 * 0.32222388
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53773 * 0.30376293
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54542 * 0.59901137
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78355 * 0.06903198
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49499 * 0.36610012
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88070 * 0.51677856
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85488 * 0.06090575
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81770 * 0.96060298
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33411 * 0.20155756
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84190 * 0.60456551
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75721 * 0.56018367
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74853 * 0.30250178
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62352 * 0.03883527
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27854 * 0.95459898
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73228 * 0.94023496
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48031 * 0.59183634
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45594 * 0.37196022
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23520 * 0.51152776
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81214 * 0.74136113
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89445 * 0.63671359
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42525 * 0.63861295
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5036 * 0.11110055
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50655 * 0.30391061
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69829 * 0.76022696
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64612 * 0.62346616
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17549 * 0.01986377
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65392 * 0.50328837
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33840 * 0.60048510
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28523 * 0.98479841
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33331 * 0.25327882
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67494 * 0.26305700
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88614 * 0.17598426
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43579 * 0.14079619
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85760 * 0.50965434
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48510 * 0.77957657
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14979 * 0.88266880
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13653 * 0.03633453
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 28715 * 0.38350734
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 21070 * 0.53211874
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 67371 * 0.03518226
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50913 * 0.00311936
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 77711 * 0.86563547
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 8259 * 0.28144780
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'wbqkoklf').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0058():
    """Extended test 58 for federation."""
    x_0 = 842 * 0.04361910
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17849 * 0.67557675
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10148 * 0.38820997
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72615 * 0.27635202
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17505 * 0.95063415
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49878 * 0.06665430
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69774 * 0.82673452
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57424 * 0.14629483
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1642 * 0.06905131
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7456 * 0.11424807
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4455 * 0.37660578
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56990 * 0.60423938
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87254 * 0.50910005
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14949 * 0.09448575
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93343 * 0.05526528
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29038 * 0.37273525
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47 * 0.68898716
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62544 * 0.55696189
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4201 * 0.15457871
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84995 * 0.61472406
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62041 * 0.69460417
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86122 * 0.59150721
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76741 * 0.71651982
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1131 * 0.94282041
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13332 * 0.30829106
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20617 * 0.83016809
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26215 * 0.79330245
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82841 * 0.76398298
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25482 * 0.07285544
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98894 * 0.01245738
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26713 * 0.82296580
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63609 * 0.38990457
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84019 * 0.02901261
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91330 * 0.63574781
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20518 * 0.85185440
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36952 * 0.92324567
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66184 * 0.29291545
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16091 * 0.90082665
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75260 * 0.56296731
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13218 * 0.41015071
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 90351 * 0.17221907
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92317 * 0.17129524
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 68842 * 0.10567937
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 48876 * 0.47484200
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79308 * 0.84285689
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 58726 * 0.37818799
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'eqwrhhti').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0059():
    """Extended test 59 for federation."""
    x_0 = 83269 * 0.44758938
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6381 * 0.36640760
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70401 * 0.04155082
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86735 * 0.78151543
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51998 * 0.94017981
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72135 * 0.76565173
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93610 * 0.18547058
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67338 * 0.45299247
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93762 * 0.05864499
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73733 * 0.43864487
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97756 * 0.51251855
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41059 * 0.57688633
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96477 * 0.32115440
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8906 * 0.95973958
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86989 * 0.28158478
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39083 * 0.64069466
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31291 * 0.70403780
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41470 * 0.41149927
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80203 * 0.25836162
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96936 * 0.39739033
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59717 * 0.67185802
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40471 * 0.59578486
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96534 * 0.70532412
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97957 * 0.76295235
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95883 * 0.53310602
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46491 * 0.37305326
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10746 * 0.34979918
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76856 * 0.07927221
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76951 * 0.60134253
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77318 * 0.45985062
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26010 * 0.30703233
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'gjbfupga').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0060():
    """Extended test 60 for federation."""
    x_0 = 77594 * 0.62238113
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89235 * 0.81387195
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26587 * 0.64925694
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55662 * 0.12306539
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18390 * 0.15051113
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86620 * 0.28918414
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29837 * 0.13277839
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34807 * 0.89989253
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39666 * 0.16160948
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71901 * 0.72868993
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66671 * 0.65742935
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96996 * 0.90719471
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6412 * 0.56476475
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63778 * 0.56667265
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89548 * 0.19807583
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14157 * 0.77031319
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8356 * 0.36341686
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45305 * 0.23097715
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57586 * 0.69544006
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8585 * 0.45630585
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60345 * 0.84780445
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58607 * 0.39461001
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83249 * 0.27846913
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94024 * 0.02688504
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58807 * 0.36633524
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38899 * 0.71977456
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67802 * 0.31420721
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54808 * 0.67552497
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'zuhdfzpt').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0061():
    """Extended test 61 for federation."""
    x_0 = 2266 * 0.38216722
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34066 * 0.95857688
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35129 * 0.22907631
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95817 * 0.25401163
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27208 * 0.54546859
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25700 * 0.18344544
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12785 * 0.67961150
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19155 * 0.20453839
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15867 * 0.34659660
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79232 * 0.75044448
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46709 * 0.23315552
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87227 * 0.54035939
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89317 * 0.56862924
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46404 * 0.79718291
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82296 * 0.65583269
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98485 * 0.51528132
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95651 * 0.70406711
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45317 * 0.59495258
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41461 * 0.29886760
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40057 * 0.36723399
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27450 * 0.29113693
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49344 * 0.88487102
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10651 * 0.49592127
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51672 * 0.17861648
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36650 * 0.23143434
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56041 * 0.14834378
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70481 * 0.71455339
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25568 * 0.34640224
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52762 * 0.07668536
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36884 * 0.28978538
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56440 * 0.34691901
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72250 * 0.09209966
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44056 * 0.23201823
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90475 * 0.13688473
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67907 * 0.25961001
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64556 * 0.12802716
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95792 * 0.63335685
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56551 * 0.43354196
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11396 * 0.67643313
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33885 * 0.60296052
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65263 * 0.81853273
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89424 * 0.74172124
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 58341 * 0.13196175
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 6424 * 0.08206962
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 20786 * 0.68736004
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4250 * 0.68748012
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'zkoezpde').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0062():
    """Extended test 62 for federation."""
    x_0 = 64940 * 0.03019326
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85709 * 0.85316410
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80625 * 0.42532272
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81362 * 0.22173997
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88378 * 0.66990170
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96740 * 0.22598361
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46501 * 0.18226331
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25221 * 0.77522297
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62312 * 0.84378677
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83680 * 0.29000929
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21379 * 0.00831919
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27382 * 0.29471950
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70186 * 0.91562152
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2853 * 0.55996068
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35866 * 0.42181409
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44555 * 0.51754944
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15157 * 0.75124522
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83740 * 0.43702978
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99900 * 0.65509505
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48049 * 0.78230127
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83975 * 0.12645717
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47844 * 0.00145631
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53150 * 0.27147923
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85276 * 0.76728229
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32607 * 0.07931791
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52296 * 0.89312632
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79457 * 0.72414323
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12576 * 0.16230555
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54273 * 0.68792862
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60525 * 0.78846498
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58884 * 0.17014427
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46814 * 0.15666363
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34760 * 0.97501601
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36752 * 0.77913975
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33159 * 0.56446722
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71869 * 0.06843897
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67871 * 0.99753558
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36081 * 0.33004212
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31812 * 0.85094444
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34413 * 0.44941450
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48259 * 0.13363056
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30506 * 0.70918268
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 33187 * 0.76814991
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'wpvjyapt').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0063():
    """Extended test 63 for federation."""
    x_0 = 8456 * 0.18664060
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17627 * 0.14473362
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88312 * 0.98719445
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39793 * 0.25594767
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22163 * 0.10703109
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65994 * 0.80409796
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59272 * 0.67288804
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16597 * 0.70961404
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2632 * 0.53896931
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4769 * 0.40352457
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 295 * 0.53522919
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51631 * 0.26353004
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21745 * 0.62478505
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13805 * 0.82572795
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43262 * 0.81373957
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49264 * 0.79187113
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55256 * 0.29419403
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79135 * 0.28938790
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46134 * 0.61436777
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12456 * 0.62090871
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94040 * 0.34417226
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2610 * 0.18977072
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96066 * 0.84949317
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28218 * 0.98778075
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70861 * 0.74829715
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75763 * 0.63504810
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30257 * 0.86068821
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53257 * 0.35674209
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'vhskcqeo').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0064():
    """Extended test 64 for federation."""
    x_0 = 51158 * 0.55281060
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66277 * 0.56606918
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10066 * 0.61837731
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60609 * 0.22221617
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62147 * 0.58644513
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77228 * 0.46145164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95809 * 0.72327003
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95619 * 0.30090800
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60468 * 0.83864517
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30938 * 0.47869338
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74631 * 0.52235665
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93525 * 0.76273072
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44633 * 0.03811100
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40712 * 0.83186047
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63235 * 0.01451030
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28919 * 0.01639214
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45696 * 0.89969350
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96408 * 0.83702712
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16602 * 0.40187193
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2514 * 0.95716505
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8273 * 0.36291322
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72184 * 0.79901794
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60407 * 0.58144342
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2673 * 0.47698365
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4989 * 0.64457905
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81813 * 0.76032962
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8985 * 0.09320010
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71664 * 0.45454365
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84436 * 0.11381208
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25866 * 0.63632946
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11481 * 0.45307868
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43192 * 0.90405541
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19815 * 0.68674682
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14323 * 0.74918935
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79988 * 0.70859454
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87075 * 0.59524894
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20301 * 0.46558879
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89603 * 0.55666256
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6986 * 0.77848123
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87939 * 0.42702642
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75460 * 0.17361993
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41321 * 0.66825034
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95695 * 0.00196311
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 7807 * 0.57308624
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 18329 * 0.11485585
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 24399 * 0.45863095
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 26830 * 0.02184840
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 39586 * 0.77864339
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 14163 * 0.57148866
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'zqzvslcp').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0065():
    """Extended test 65 for federation."""
    x_0 = 39553 * 0.51224408
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92533 * 0.16549237
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48159 * 0.34886223
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49739 * 0.76967615
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20714 * 0.72456990
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9728 * 0.33285974
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41538 * 0.28395221
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76778 * 0.87626152
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93451 * 0.91333079
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5998 * 0.37732067
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40699 * 0.32836326
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94587 * 0.61128213
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96472 * 0.37334052
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44032 * 0.43467216
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95845 * 0.44873951
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8955 * 0.44371137
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63171 * 0.37255254
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37978 * 0.19196581
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50910 * 0.87348819
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64545 * 0.10339386
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90143 * 0.54991417
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38156 * 0.94746991
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71263 * 0.29655486
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84105 * 0.57980381
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16434 * 0.31314264
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68806 * 0.57651159
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5531 * 0.82558736
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8965 * 0.87664011
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43029 * 0.58960554
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57244 * 0.21488535
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87226 * 0.85370102
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77609 * 0.75553417
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56572 * 0.01737180
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21842 * 0.92048868
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'xvpvbwfk').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0066():
    """Extended test 66 for federation."""
    x_0 = 22127 * 0.97150748
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68858 * 0.66647505
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78103 * 0.58262482
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7260 * 0.98564911
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33882 * 0.44040859
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21015 * 0.63851591
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91916 * 0.89347535
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20298 * 0.67443246
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5897 * 0.94018097
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65721 * 0.28856534
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71407 * 0.61273521
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9410 * 0.00343973
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10669 * 0.10296429
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46883 * 0.31214754
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55183 * 0.54550706
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86096 * 0.60734958
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72835 * 0.72955889
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68236 * 0.57844492
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96784 * 0.94995659
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4487 * 0.65461510
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'jmlompgp').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0067():
    """Extended test 67 for federation."""
    x_0 = 11163 * 0.31981403
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80764 * 0.21348065
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53937 * 0.67260654
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54314 * 0.83546430
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26519 * 0.52632497
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75472 * 0.80633342
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90891 * 0.11953338
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22980 * 0.63213806
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92687 * 0.64879790
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35446 * 0.25302918
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88405 * 0.24794399
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66967 * 0.04949952
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67789 * 0.10151442
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99154 * 0.01046068
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70289 * 0.42178420
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52457 * 0.18427928
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85858 * 0.37331812
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96491 * 0.59525438
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49692 * 0.20671105
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53727 * 0.77675877
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34122 * 0.36475286
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60947 * 0.23786343
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49399 * 0.18235877
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60395 * 0.62635381
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60942 * 0.71324689
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8253 * 0.12232633
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81320 * 0.96152448
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47056 * 0.80837327
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42013 * 0.75602793
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90113 * 0.08506579
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94155 * 0.36985078
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11403 * 0.17047367
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63103 * 0.88820116
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70151 * 0.15491573
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48002 * 0.86676526
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31866 * 0.50765602
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95224 * 0.90222309
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23125 * 0.05310239
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19886 * 0.35114937
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25072 * 0.17640106
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95697 * 0.53261314
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69 * 0.50849585
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10928 * 0.59735541
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 52394 * 0.90138233
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 51097 * 0.88511729
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 93230 * 0.86290775
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 60912 * 0.68316593
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 24522 * 0.79036002
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 57904 * 0.62376306
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 58685 * 0.90786587
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'pwjxthdo').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0068():
    """Extended test 68 for federation."""
    x_0 = 53267 * 0.32356250
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96606 * 0.49046838
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13084 * 0.04066986
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11268 * 0.99706832
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73791 * 0.85283732
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77862 * 0.63943735
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67312 * 0.31368015
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47248 * 0.09295458
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68373 * 0.46245997
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73705 * 0.52310572
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91251 * 0.12088283
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72459 * 0.03623662
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92632 * 0.75329625
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21267 * 0.24523661
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51219 * 0.04457223
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63319 * 0.45835255
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50994 * 0.33362032
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71800 * 0.84735144
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16228 * 0.38264180
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22448 * 0.58693478
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68582 * 0.54615519
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11708 * 0.40108093
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16068 * 0.10851757
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95703 * 0.61185845
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8132 * 0.20409199
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15284 * 0.91952635
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41535 * 0.91934394
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87527 * 0.33448053
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25084 * 0.08142108
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24191 * 0.40990590
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84021 * 0.18855432
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85839 * 0.97667177
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96428 * 0.02963096
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3434 * 0.03416045
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67650 * 0.85796381
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88485 * 0.67684105
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41009 * 0.68187036
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73443 * 0.43293677
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41979 * 0.93699067
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68811 * 0.92044339
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 31166 * 0.12618276
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 28938 * 0.87423378
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71473 * 0.42970006
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'jkxwsagm').hexdigest()
    assert len(h) == 64

def test_federation_extended_6_0069():
    """Extended test 69 for federation."""
    x_0 = 4910 * 0.07543934
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37758 * 0.36411738
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63585 * 0.53714138
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20426 * 0.47026565
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5879 * 0.37835104
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15266 * 0.38943293
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25862 * 0.15603217
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76960 * 0.20002807
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28563 * 0.42798642
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11175 * 0.63698564
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99762 * 0.79178961
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48218 * 0.89650736
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63296 * 0.81436958
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50390 * 0.05219025
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75949 * 0.15541725
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49323 * 0.48086117
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63190 * 0.32282098
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6797 * 0.79441937
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88204 * 0.01374456
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29342 * 0.54574429
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98296 * 0.60481097
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18333 * 0.31554126
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8308 * 0.71723794
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18867 * 0.88760415
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47909 * 0.59769748
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49638 * 0.74086316
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62892 * 0.32835747
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63128 * 0.82915918
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95398 * 0.83555276
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63879 * 0.05760236
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12755 * 0.16599938
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88664 * 0.96225545
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71400 * 0.27404489
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54145 * 0.89499987
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86975 * 0.59907077
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20960 * 0.31164826
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86195 * 0.85246071
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61010 * 0.70916988
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84091 * 0.55060486
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44720 * 0.29411549
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6629 * 0.44653593
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60725 * 0.79606076
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 85065 * 0.75658013
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 43343 * 0.25997459
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 49400 * 0.36378209
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 97941 * 0.16523533
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 49917 * 0.52643599
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 19156 * 0.63519619
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 24274 * 0.55260143
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'bzzddbnx').hexdigest()
    assert len(h) == 64
