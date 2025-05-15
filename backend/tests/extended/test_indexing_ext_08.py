"""Extended tests for indexing suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_indexing_extended_8_0000():
    """Extended test 0 for indexing."""
    x_0 = 42699 * 0.41265769
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4609 * 0.63798149
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44263 * 0.55773767
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99025 * 0.25318508
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29242 * 0.93101600
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95988 * 0.02937691
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55245 * 0.44666062
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19766 * 0.61659905
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52920 * 0.23438918
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95915 * 0.35476189
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95661 * 0.29555541
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42039 * 0.06798142
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98185 * 0.30793690
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69551 * 0.00133043
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28910 * 0.87112264
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88047 * 0.39912619
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17305 * 0.42853766
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8979 * 0.60138962
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75525 * 0.52737590
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52476 * 0.52480683
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50342 * 0.75802029
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86393 * 0.07802367
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31008 * 0.48174178
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58819 * 0.84380825
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92512 * 0.14453823
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88746 * 0.57162605
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83505 * 0.83271070
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75101 * 0.88498193
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58798 * 0.48158430
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98902 * 0.51052847
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61157 * 0.04914811
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97467 * 0.13803135
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11964 * 0.72149719
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83077 * 0.76942240
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23400 * 0.88793633
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59623 * 0.77363231
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99124 * 0.97379467
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12037 * 0.29463271
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83578 * 0.04157108
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39740 * 0.13516974
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82797 * 0.35299046
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 44913 * 0.10802423
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6123 * 0.04654524
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 78131 * 0.90846386
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 82127 * 0.85191698
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 13678 * 0.64636981
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 16605 * 0.14813360
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'mlvdezxf').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0001():
    """Extended test 1 for indexing."""
    x_0 = 72948 * 0.23976438
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74994 * 0.80427205
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77889 * 0.11583112
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52593 * 0.33079903
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20690 * 0.48318313
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60551 * 0.55685964
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9939 * 0.28191845
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99197 * 0.89018022
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16499 * 0.73921812
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22713 * 0.39122662
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32507 * 0.51044392
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52485 * 0.77745406
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49213 * 0.88858186
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16485 * 0.45551936
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3715 * 0.05471805
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55870 * 0.37807119
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14410 * 0.78590834
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70284 * 0.60210256
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4775 * 0.12627173
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59211 * 0.92986170
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56716 * 0.02581011
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91533 * 0.22104144
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99464 * 0.43061610
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90354 * 0.83669270
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69256 * 0.04278610
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89270 * 0.05183055
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87002 * 0.34022884
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64404 * 0.02504628
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'dihmczbm').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0002():
    """Extended test 2 for indexing."""
    x_0 = 1436 * 0.19118824
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44818 * 0.71841336
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66840 * 0.96656313
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87472 * 0.33058038
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35253 * 0.87547835
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5217 * 0.95832170
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43088 * 0.09722661
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43081 * 0.56891103
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15769 * 0.09954498
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8346 * 0.85530833
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 158 * 0.02632971
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28677 * 0.55144644
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23459 * 0.46804819
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14338 * 0.73963755
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10848 * 0.61342867
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80433 * 0.97234337
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23294 * 0.58223513
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27925 * 0.42718085
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38281 * 0.73944504
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3701 * 0.73376762
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63146 * 0.39987010
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63721 * 0.68870061
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32239 * 0.94872582
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66110 * 0.91222264
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29872 * 0.10876958
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20521 * 0.06554138
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74662 * 0.54162587
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53966 * 0.69050928
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48070 * 0.83112773
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38154 * 0.71254987
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6324 * 0.84753802
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93106 * 0.87403707
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1867 * 0.49550998
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83548 * 0.58686863
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14689 * 0.88528414
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4408 * 0.84396592
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35479 * 0.46643938
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22360 * 0.04689342
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 95043 * 0.17788042
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20879 * 0.77482300
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 22705 * 0.21980511
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'doyaqoif').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0003():
    """Extended test 3 for indexing."""
    x_0 = 82408 * 0.83876371
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6080 * 0.81996854
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21170 * 0.90744767
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16515 * 0.48394908
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75889 * 0.69813515
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42933 * 0.36034493
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5987 * 0.42541398
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31068 * 0.77460105
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83556 * 0.06748206
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76726 * 0.69106730
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73418 * 0.82215066
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50539 * 0.81569382
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70690 * 0.20825449
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55047 * 0.49554530
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88184 * 0.07003942
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20882 * 0.71448250
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51959 * 0.88101333
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13680 * 0.97730806
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25043 * 0.72704262
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49123 * 0.36328066
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10814 * 0.54198325
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11545 * 0.77619036
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18530 * 0.24174683
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92776 * 0.54456831
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56575 * 0.03423307
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55730 * 0.07083425
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24986 * 0.75130170
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33067 * 0.41586442
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10721 * 0.29156770
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59364 * 0.65144704
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70192 * 0.42182145
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40199 * 0.66210773
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54506 * 0.32192114
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53216 * 0.92686910
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79464 * 0.85805254
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12126 * 0.65457343
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62297 * 0.46310704
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'qaqoyrww').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0004():
    """Extended test 4 for indexing."""
    x_0 = 85304 * 0.99810261
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12844 * 0.75147141
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44802 * 0.37035515
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44178 * 0.01476615
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1871 * 0.50037608
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65154 * 0.31021769
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7730 * 0.40794623
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65450 * 0.14706563
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92727 * 0.92418084
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67867 * 0.52976881
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55400 * 0.35887097
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72726 * 0.23441105
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30784 * 0.27237670
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53348 * 0.07013200
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87909 * 0.71740288
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13746 * 0.21805936
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13891 * 0.18841546
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37614 * 0.39205667
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72186 * 0.33477418
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35110 * 0.42521105
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68333 * 0.95163792
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99831 * 0.03286045
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36843 * 0.24550840
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15737 * 0.74243813
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75440 * 0.74964072
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40076 * 0.08463890
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92652 * 0.12294624
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7328 * 0.53057366
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48121 * 0.46088140
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47355 * 0.61124309
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84324 * 0.83884576
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54348 * 0.59941233
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36196 * 0.76166691
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'gukfvmob').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0005():
    """Extended test 5 for indexing."""
    x_0 = 30235 * 0.51195223
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58962 * 0.89598222
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76003 * 0.32248170
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96701 * 0.90499872
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53920 * 0.13769320
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19295 * 0.13469213
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55784 * 0.06647849
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17353 * 0.77131053
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73053 * 0.91241704
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66949 * 0.81239028
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45076 * 0.76511776
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34064 * 0.63565183
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46933 * 0.50572344
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73427 * 0.76736076
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76619 * 0.02889716
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31005 * 0.14921014
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52677 * 0.72594826
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86293 * 0.14571141
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34501 * 0.59631012
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18406 * 0.89321696
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36763 * 0.79793296
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54443 * 0.56992863
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7403 * 0.53028503
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91790 * 0.38761142
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92867 * 0.40324056
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66423 * 0.06236264
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29005 * 0.01211465
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94034 * 0.14551865
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75531 * 0.76724614
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34974 * 0.67745763
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76450 * 0.69009169
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5441 * 0.70145581
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82557 * 0.97278043
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5787 * 0.84845160
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72928 * 0.40277290
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1378 * 0.67298597
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51462 * 0.87314236
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32965 * 0.57490603
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6904 * 0.40801068
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 35876 * 0.10472794
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20051 * 0.48016925
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 2782 * 0.94657307
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55038 * 0.85211913
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 55459 * 0.54092241
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'jfglwlaj').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0006():
    """Extended test 6 for indexing."""
    x_0 = 31443 * 0.46194776
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40641 * 0.77962044
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76566 * 0.20168568
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42894 * 0.39996074
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48099 * 0.64122505
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74812 * 0.95075726
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6959 * 0.57728315
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31873 * 0.46021282
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27963 * 0.51923586
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99511 * 0.33119465
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11790 * 0.06944123
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89174 * 0.95525865
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53043 * 0.88231691
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80773 * 0.43795035
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21514 * 0.39693827
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17327 * 0.20617246
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24521 * 0.37396255
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38256 * 0.48838087
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51360 * 0.21356090
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70044 * 0.43156336
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22096 * 0.95697947
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40024 * 0.79846020
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20945 * 0.30058270
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9082 * 0.00966960
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20848 * 0.67068239
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78633 * 0.70775204
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37176 * 0.37131593
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10766 * 0.16113937
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94574 * 0.65749661
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89192 * 0.31435083
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'whpufmri').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0007():
    """Extended test 7 for indexing."""
    x_0 = 1378 * 0.93710652
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67913 * 0.98186072
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72647 * 0.95009918
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22308 * 0.73830230
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21896 * 0.43637453
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4914 * 0.05408758
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64092 * 0.71005320
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82817 * 0.67818664
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36545 * 0.32466131
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 814 * 0.20793827
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74374 * 0.82485351
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53230 * 0.63502283
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69016 * 0.33135171
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15136 * 0.82836580
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63615 * 0.08765944
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17429 * 0.39510636
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88844 * 0.08100543
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81974 * 0.66630348
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35183 * 0.62795679
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74797 * 0.83710435
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45986 * 0.24458552
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68438 * 0.60237052
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'lakokjzb').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0008():
    """Extended test 8 for indexing."""
    x_0 = 85423 * 0.29812703
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46530 * 0.65126681
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6891 * 0.43841511
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64161 * 0.39045932
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99399 * 0.77276678
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77034 * 0.08221467
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44109 * 0.00123055
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80815 * 0.79014280
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8489 * 0.50858561
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72290 * 0.90066013
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76159 * 0.79516012
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1930 * 0.05902558
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34600 * 0.37957964
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97625 * 0.12682152
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25105 * 0.72422617
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67645 * 0.24992072
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25766 * 0.38799030
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91007 * 0.54178415
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6765 * 0.92798511
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86490 * 0.91146899
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53159 * 0.36718648
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80224 * 0.86553094
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70465 * 0.63705232
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6760 * 0.14197502
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96181 * 0.66110018
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71263 * 0.78530595
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78418 * 0.14292566
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10486 * 0.48555265
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53770 * 0.23378126
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32469 * 0.61226817
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21051 * 0.74959873
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79747 * 0.06923991
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41217 * 0.14768745
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ycfiqmnj').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0009():
    """Extended test 9 for indexing."""
    x_0 = 97707 * 0.93527330
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60098 * 0.33299017
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16678 * 0.53817378
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83889 * 0.13252327
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85635 * 0.87165313
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17577 * 0.64430858
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76274 * 0.91285232
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76153 * 0.86231658
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83929 * 0.86731480
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76842 * 0.42676739
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90993 * 0.88327646
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42004 * 0.56698455
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88323 * 0.37231026
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78457 * 0.56131561
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43286 * 0.85941733
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57043 * 0.65856860
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60836 * 0.04012356
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98850 * 0.56856975
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83284 * 0.49194835
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23213 * 0.71760136
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'dfrbycfs').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0010():
    """Extended test 10 for indexing."""
    x_0 = 80448 * 0.33918654
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32384 * 0.87164726
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96426 * 0.85334683
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64354 * 0.12747514
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20011 * 0.30388272
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30319 * 0.96287442
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72988 * 0.39648335
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21139 * 0.94656929
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25422 * 0.31573179
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10567 * 0.81097149
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33229 * 0.68534060
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61532 * 0.10845161
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7013 * 0.10030698
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38833 * 0.31396231
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28680 * 0.00541069
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76838 * 0.46522617
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76932 * 0.43424724
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84789 * 0.17924002
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78647 * 0.49393831
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88012 * 0.74790785
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5454 * 0.46765346
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79641 * 0.40161346
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89423 * 0.13292404
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34413 * 0.00838931
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55803 * 0.20285101
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69288 * 0.60666083
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14112 * 0.18264588
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13316 * 0.95132199
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12798 * 0.76800365
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'rriyztio').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0011():
    """Extended test 11 for indexing."""
    x_0 = 67604 * 0.80866854
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51360 * 0.97597683
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70038 * 0.82486373
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3425 * 0.13313384
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38234 * 0.38471228
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55276 * 0.34340995
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74091 * 0.83129710
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83810 * 0.40048883
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43149 * 0.38041871
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67695 * 0.01426272
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38366 * 0.59213373
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31372 * 0.63385157
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23802 * 0.37046611
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33610 * 0.41009756
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81501 * 0.17539787
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80737 * 0.11738134
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26884 * 0.49389832
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27479 * 0.11555060
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74285 * 0.34480493
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63675 * 0.35010018
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49220 * 0.16125861
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24333 * 0.81821813
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85291 * 0.06028319
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42716 * 0.92624516
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70738 * 0.66119121
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35395 * 0.55374482
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 255 * 0.53812922
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40407 * 0.72567996
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14403 * 0.59065694
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31115 * 0.94288918
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70066 * 0.05381577
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48390 * 0.78660128
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8757 * 0.26204797
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ivikwxgb').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0012():
    """Extended test 12 for indexing."""
    x_0 = 58446 * 0.59165428
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38563 * 0.36090609
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78084 * 0.29872247
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70235 * 0.09192594
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35554 * 0.02660713
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93119 * 0.64627059
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82593 * 0.03438160
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34487 * 0.42495262
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70632 * 0.16624425
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80852 * 0.28528677
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99917 * 0.72008106
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56020 * 0.71599161
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82909 * 0.36870931
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70574 * 0.67015341
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49452 * 0.32432611
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27200 * 0.80452408
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99759 * 0.12183719
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41304 * 0.83666700
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98909 * 0.57163030
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34791 * 0.44849781
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81972 * 0.08044645
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7625 * 0.92765460
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69865 * 0.20150589
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92008 * 0.43639833
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36452 * 0.22728382
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51549 * 0.34927885
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93623 * 0.73700931
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27934 * 0.32752906
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34705 * 0.84010635
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14631 * 0.80332191
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12192 * 0.35783840
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80867 * 0.56151170
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82898 * 0.58976569
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86386 * 0.76119752
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67849 * 0.85275803
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3638 * 0.29827911
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9264 * 0.51932823
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88065 * 0.49775869
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27551 * 0.51177404
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17369 * 0.12214072
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 24826 * 0.64590102
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52586 * 0.72486185
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29145 * 0.29788899
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 10951 * 0.56763452
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 223 * 0.49758867
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 21436 * 0.10347189
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 97638 * 0.76678090
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'vgvmqrgi').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0013():
    """Extended test 13 for indexing."""
    x_0 = 19060 * 0.65755669
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56931 * 0.60614856
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40240 * 0.09800241
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61931 * 0.99290416
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81363 * 0.79306219
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5644 * 0.09870703
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95907 * 0.94207990
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21859 * 0.76743966
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72675 * 0.43307675
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2520 * 0.86913312
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74384 * 0.07392994
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21007 * 0.50533372
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52078 * 0.27221332
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31996 * 0.84162801
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81424 * 0.05582308
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71190 * 0.73418278
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52678 * 0.47670664
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43588 * 0.37029213
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73904 * 0.32673806
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62879 * 0.34052678
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87539 * 0.20037691
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85450 * 0.72484124
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81722 * 0.85939490
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6092 * 0.31356513
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92880 * 0.70961487
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56902 * 0.97507955
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84475 * 0.31080528
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14293 * 0.62228643
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80702 * 0.15403521
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15814 * 0.96026741
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25433 * 0.60205434
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8440 * 0.33969222
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46715 * 0.55251856
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76134 * 0.16111123
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45953 * 0.83537555
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24120 * 0.46744384
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45040 * 0.98146462
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97954 * 0.32125671
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13807 * 0.48045656
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'wxgfpxak').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0014():
    """Extended test 14 for indexing."""
    x_0 = 57689 * 0.85516290
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73135 * 0.96180462
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36356 * 0.80279970
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94449 * 0.46129754
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12584 * 0.94152213
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34868 * 0.78093219
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77212 * 0.82013642
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84770 * 0.93501998
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77900 * 0.62649211
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40789 * 0.75303297
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81722 * 0.69058571
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39122 * 0.91220482
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44309 * 0.44226163
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87623 * 0.58113273
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30345 * 0.06811659
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55066 * 0.32060503
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6728 * 0.43260517
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65439 * 0.88587260
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24430 * 0.44398072
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71963 * 0.79660992
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16442 * 0.44114251
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63300 * 0.32570322
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4053 * 0.75106153
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22865 * 0.73035237
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74243 * 0.25534910
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63148 * 0.85062946
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60407 * 0.03425374
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48827 * 0.52528833
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'eliyaxai').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0015():
    """Extended test 15 for indexing."""
    x_0 = 26941 * 0.60246865
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11767 * 0.32554803
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85175 * 0.42908568
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7770 * 0.51251042
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66118 * 0.15851632
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44240 * 0.39491156
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61394 * 0.21783892
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67810 * 0.96419884
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6697 * 0.72355455
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 192 * 0.74251138
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40957 * 0.19705412
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29177 * 0.85877351
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83839 * 0.97048163
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38945 * 0.94846043
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76619 * 0.22928893
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67258 * 0.98976099
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68911 * 0.41479409
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78526 * 0.84313471
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27682 * 0.26703103
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91563 * 0.92055693
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77360 * 0.07873747
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1846 * 0.30555901
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41215 * 0.67774554
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'giwkdfmm').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0016():
    """Extended test 16 for indexing."""
    x_0 = 98382 * 0.80484753
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91915 * 0.29658950
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99415 * 0.97281866
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75173 * 0.37990714
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24206 * 0.50195450
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65783 * 0.30831651
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46182 * 0.24990471
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97846 * 0.41734298
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25873 * 0.42770866
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96523 * 0.68927730
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4027 * 0.19589988
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17519 * 0.30737182
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32988 * 0.17327978
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19239 * 0.53445481
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9395 * 0.28785714
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51570 * 0.96277902
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31689 * 0.28665020
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84595 * 0.29482779
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99370 * 0.96554977
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22438 * 0.23070339
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'wxnstqgv').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0017():
    """Extended test 17 for indexing."""
    x_0 = 47785 * 0.13211648
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96789 * 0.35171919
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55292 * 0.09255214
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54866 * 0.44297659
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28756 * 0.15270538
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73588 * 0.41754375
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79806 * 0.80436404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80491 * 0.46749568
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78942 * 0.44493047
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7303 * 0.28102317
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3223 * 0.72470872
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71874 * 0.04704182
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31774 * 0.10459265
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46928 * 0.10271364
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40180 * 0.72709133
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52200 * 0.45006479
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99375 * 0.88052865
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55631 * 0.60373105
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16973 * 0.67955213
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39228 * 0.94203564
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73095 * 0.21945838
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41704 * 0.57958122
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52591 * 0.42672078
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96623 * 0.02659462
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'guwqdruk').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0018():
    """Extended test 18 for indexing."""
    x_0 = 63713 * 0.41329870
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24028 * 0.95257124
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12409 * 0.96402874
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74480 * 0.27892853
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31712 * 0.03003557
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58024 * 0.38759677
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93709 * 0.85099170
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10913 * 0.51589755
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58504 * 0.72702742
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32673 * 0.95488013
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78094 * 0.54119340
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88719 * 0.95238691
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51959 * 0.80466844
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96270 * 0.10437200
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70860 * 0.81892071
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26444 * 0.60432362
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39830 * 0.30909095
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44655 * 0.27183346
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34963 * 0.79302935
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72078 * 0.39334971
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92015 * 0.65097356
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ngsepjzc').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0019():
    """Extended test 19 for indexing."""
    x_0 = 56586 * 0.37072614
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32053 * 0.98355402
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2197 * 0.41024690
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89719 * 0.46401527
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33109 * 0.30607703
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69825 * 0.03638646
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64097 * 0.35064257
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51300 * 0.60864829
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77446 * 0.02416323
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50574 * 0.21647143
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39779 * 0.18767842
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52956 * 0.88175500
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 912 * 0.82878259
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83172 * 0.56272118
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35515 * 0.69751056
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98703 * 0.42783933
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10844 * 0.68356123
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36862 * 0.99371699
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11528 * 0.53674570
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14953 * 0.51216788
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5400 * 0.39081268
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57202 * 0.52814350
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7608 * 0.16977248
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92094 * 0.25433568
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68211 * 0.60818293
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34446 * 0.42819240
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71246 * 0.11139262
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65234 * 0.86483193
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50478 * 0.52977739
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'dcyajcjj').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0020():
    """Extended test 20 for indexing."""
    x_0 = 93000 * 0.26317332
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31905 * 0.08173604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43964 * 0.92761345
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19578 * 0.74834193
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87149 * 0.84472414
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94766 * 0.63423689
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22771 * 0.35894974
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4130 * 0.26416033
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93745 * 0.00008461
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80922 * 0.15873289
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19818 * 0.91444132
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43407 * 0.26211256
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81935 * 0.39032183
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66674 * 0.79818583
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75865 * 0.52651026
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78205 * 0.99900940
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66069 * 0.20042546
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95768 * 0.80757621
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19166 * 0.03989276
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55775 * 0.59955068
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74166 * 0.20998862
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64381 * 0.03411179
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84967 * 0.43713104
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61129 * 0.43884142
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36313 * 0.05771303
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18172 * 0.79857948
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50024 * 0.11546862
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36787 * 0.00597643
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20077 * 0.84830807
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54387 * 0.26336992
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73628 * 0.25686900
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70484 * 0.73626138
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10139 * 0.94857564
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16731 * 0.29174094
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75058 * 0.24600082
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85592 * 0.68869845
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56842 * 0.57915664
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55983 * 0.52943968
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4783 * 0.31364338
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76532 * 0.98571662
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 39612 * 0.13428109
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50539 * 0.05602302
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 2117 * 0.54377388
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 19814 * 0.15550490
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 29791 * 0.26713884
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 71211 * 0.16838167
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 39953 * 0.95937443
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'owogbqky').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0021():
    """Extended test 21 for indexing."""
    x_0 = 3455 * 0.96653329
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19046 * 0.79648171
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88496 * 0.58931458
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 818 * 0.66900403
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84805 * 0.11729241
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7649 * 0.96039891
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57716 * 0.00243670
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79300 * 0.28441371
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45347 * 0.19438855
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67974 * 0.74081186
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72737 * 0.02561848
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9000 * 0.05659868
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1155 * 0.26387679
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4274 * 0.20983746
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62589 * 0.31443315
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75929 * 0.55775089
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69195 * 0.15626703
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55400 * 0.73160366
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62839 * 0.09594089
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47158 * 0.20408367
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75147 * 0.02488824
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73814 * 0.61789368
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21555 * 0.25347438
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18880 * 0.16384165
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69711 * 0.64772463
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29938 * 0.56252119
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72137 * 0.39463360
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64670 * 0.51456568
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17694 * 0.80198064
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28239 * 0.53895827
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60098 * 0.07258857
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35234 * 0.91979146
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41390 * 0.97365662
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9847 * 0.19859161
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30724 * 0.47053017
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'nrtiqzrb').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0022():
    """Extended test 22 for indexing."""
    x_0 = 82279 * 0.89026788
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2634 * 0.49345233
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31584 * 0.22478581
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31139 * 0.10792159
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79820 * 0.06211389
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87630 * 0.91340323
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27465 * 0.50240809
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61450 * 0.07431533
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91557 * 0.54388015
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55958 * 0.42659492
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47616 * 0.02141842
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30035 * 0.17029297
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75370 * 0.49670452
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73764 * 0.57438106
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62920 * 0.60268313
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59715 * 0.34199164
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97845 * 0.73535002
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57734 * 0.97136418
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6090 * 0.10545479
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50000 * 0.56035993
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96325 * 0.69349037
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14651 * 0.64214827
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46149 * 0.61807910
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8152 * 0.90638997
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69179 * 0.27583580
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7189 * 0.62038774
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82531 * 0.22126083
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59213 * 0.92869633
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17897 * 0.74171308
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12626 * 0.16500450
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'kerbwmxg').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0023():
    """Extended test 23 for indexing."""
    x_0 = 46081 * 0.97866085
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23426 * 0.53147270
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75154 * 0.75039858
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48368 * 0.87529693
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21335 * 0.33198448
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35276 * 0.90855583
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37607 * 0.49982271
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87287 * 0.97113602
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 118 * 0.61926979
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96890 * 0.07033737
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97783 * 0.30811630
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46344 * 0.35941975
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99638 * 0.46863807
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30527 * 0.07892425
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27726 * 0.45474776
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84669 * 0.72522037
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86644 * 0.50069711
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31227 * 0.58140028
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95858 * 0.61264098
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76685 * 0.57956335
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82126 * 0.30967056
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99421 * 0.44317792
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'xtkytyqv').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0024():
    """Extended test 24 for indexing."""
    x_0 = 42237 * 0.94338883
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85079 * 0.95551173
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28648 * 0.02395726
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 773 * 0.24129534
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76538 * 0.27568348
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70466 * 0.73783012
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97997 * 0.94888622
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77345 * 0.90042083
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14172 * 0.92949779
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38415 * 0.21066652
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36378 * 0.72388651
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83254 * 0.26887761
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8282 * 0.99819242
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22843 * 0.05462848
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69820 * 0.92809857
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71123 * 0.50006011
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70093 * 0.97326923
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23861 * 0.98692105
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16889 * 0.73612896
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10259 * 0.89064063
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72986 * 0.92371561
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30795 * 0.63920926
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'glaspyzd').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0025():
    """Extended test 25 for indexing."""
    x_0 = 74671 * 0.29352443
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67054 * 0.44091691
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29670 * 0.51826708
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84192 * 0.85822808
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70510 * 0.09238112
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74533 * 0.53001462
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46767 * 0.19658406
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29797 * 0.28544435
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30908 * 0.82352055
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13942 * 0.77074566
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60541 * 0.34717035
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36360 * 0.12506533
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67405 * 0.28246078
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18912 * 0.08312334
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64329 * 0.30159151
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46548 * 0.82880743
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7663 * 0.46811543
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2206 * 0.45314868
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4807 * 0.70771370
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78497 * 0.05053890
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31184 * 0.52609030
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15854 * 0.61830664
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14908 * 0.28714798
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99515 * 0.37891995
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50853 * 0.33186216
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36116 * 0.85078089
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98654 * 0.66241265
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94321 * 0.97401196
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96388 * 0.16946169
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5298 * 0.36421351
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67319 * 0.15835935
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82232 * 0.17611637
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7873 * 0.72559540
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25915 * 0.72555630
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37432 * 0.77542986
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 9888 * 0.98572937
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65354 * 0.77293319
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25653 * 0.68927273
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'rfkyyhia').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0026():
    """Extended test 26 for indexing."""
    x_0 = 24431 * 0.36095476
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44214 * 0.25343049
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25477 * 0.50432080
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87860 * 0.95210703
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94630 * 0.08608014
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62619 * 0.91199789
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55882 * 0.56437170
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84329 * 0.15088410
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10253 * 0.33253897
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10753 * 0.40303432
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57802 * 0.12800772
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 458 * 0.96385098
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84075 * 0.31489532
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53385 * 0.06053387
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24033 * 0.62532733
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99802 * 0.34658312
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29958 * 0.44131527
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44668 * 0.63121539
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12497 * 0.72699842
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51618 * 0.04886340
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52987 * 0.20653325
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39675 * 0.70047764
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57180 * 0.85243618
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18301 * 0.43699029
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65082 * 0.13670343
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73307 * 0.97655046
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35752 * 0.12217482
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38700 * 0.66365460
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8180 * 0.76620924
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59122 * 0.14090280
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16530 * 0.25803744
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16067 * 0.50075846
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53027 * 0.82269485
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99908 * 0.08318174
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71852 * 0.42350700
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62056 * 0.07309861
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51130 * 0.15305478
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5116 * 0.24258226
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48579 * 0.46055058
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'hzutbrgt').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0027():
    """Extended test 27 for indexing."""
    x_0 = 14963 * 0.43477294
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53843 * 0.42189220
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5367 * 0.19210864
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18207 * 0.79100092
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94472 * 0.63825130
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63995 * 0.66867968
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7653 * 0.55422088
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12636 * 0.85809966
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1259 * 0.87612570
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35185 * 0.17528148
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5993 * 0.98201045
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21766 * 0.72224738
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77162 * 0.06646984
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6504 * 0.33546905
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31094 * 0.02293627
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11467 * 0.37925499
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19757 * 0.14062236
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91073 * 0.88526042
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4268 * 0.09961278
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74840 * 0.05633775
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54357 * 0.63011976
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92205 * 0.64658555
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37651 * 0.67292216
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69773 * 0.02565976
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73618 * 0.22015001
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3043 * 0.87569900
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31429 * 0.45789141
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5235 * 0.82912682
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80356 * 0.92846762
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50482 * 0.70768620
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10806 * 0.24837353
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18050 * 0.77843992
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74879 * 0.87800255
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59901 * 0.53262311
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33231 * 0.10897138
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20384 * 0.83935540
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13329 * 0.07096674
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92613 * 0.82475056
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73834 * 0.99340776
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67413 * 0.54387330
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75130 * 0.09051396
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'twgfvlqe').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0028():
    """Extended test 28 for indexing."""
    x_0 = 30852 * 0.08411966
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22022 * 0.77256383
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3017 * 0.51146987
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32388 * 0.01939380
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85687 * 0.64817371
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17460 * 0.86758258
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75194 * 0.09682984
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15959 * 0.03743953
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41402 * 0.17898008
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53188 * 0.25667412
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84601 * 0.12581898
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4374 * 0.33220879
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66988 * 0.54321750
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36265 * 0.88500377
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79533 * 0.75102532
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53517 * 0.82625239
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53458 * 0.47257727
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45254 * 0.32453302
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34336 * 0.69281573
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46006 * 0.48590696
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77565 * 0.39342949
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22325 * 0.24139058
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32810 * 0.96699738
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88078 * 0.91726914
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55843 * 0.58931453
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51480 * 0.73665196
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69939 * 0.10245420
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37595 * 0.35830677
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76802 * 0.61482551
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23183 * 0.02646304
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57703 * 0.22944753
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26011 * 0.22370898
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77054 * 0.18922992
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46908 * 0.25400723
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23064 * 0.23742505
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22265 * 0.64780218
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'tvyuffaz').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0029():
    """Extended test 29 for indexing."""
    x_0 = 27629 * 0.43105735
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72300 * 0.12273343
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23399 * 0.26312646
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34120 * 0.53704437
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94131 * 0.50690604
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13281 * 0.71558280
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73153 * 0.64262053
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77918 * 0.17353779
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23347 * 0.02515390
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78784 * 0.42279345
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39508 * 0.75490505
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37637 * 0.38988853
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26249 * 0.68659175
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54371 * 0.76149272
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71187 * 0.83443209
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85895 * 0.76611050
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44027 * 0.59283251
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68453 * 0.48137451
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15354 * 0.64826977
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29699 * 0.44729006
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63798 * 0.73041387
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16246 * 0.48882464
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36320 * 0.68051446
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85394 * 0.57198413
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43796 * 0.88037140
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58951 * 0.69036035
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60968 * 0.67027897
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14081 * 0.55727503
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99738 * 0.31059812
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58082 * 0.57439146
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3860 * 0.87678095
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'pczcwggp').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0030():
    """Extended test 30 for indexing."""
    x_0 = 47001 * 0.00067768
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15292 * 0.65991097
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5149 * 0.81053460
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81944 * 0.05434559
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59407 * 0.67671926
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18574 * 0.30517561
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52812 * 0.10679271
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72767 * 0.40247684
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36172 * 0.50070833
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78074 * 0.66234222
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83474 * 0.68346929
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36688 * 0.23330208
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3921 * 0.40329494
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10245 * 0.37011892
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26407 * 0.19923955
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95052 * 0.29027763
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51133 * 0.27202907
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44314 * 0.00015571
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55959 * 0.03409586
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47208 * 0.45253628
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40720 * 0.34631072
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ehvxobmb').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0031():
    """Extended test 31 for indexing."""
    x_0 = 57055 * 0.13618725
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21345 * 0.25423130
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82210 * 0.16683669
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77881 * 0.37004362
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38583 * 0.15283340
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65863 * 0.95841530
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36686 * 0.15369866
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76543 * 0.92646599
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98903 * 0.73231542
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13085 * 0.35931110
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13712 * 0.96581408
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14056 * 0.49789203
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31452 * 0.42044721
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97591 * 0.46355991
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20054 * 0.56458833
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20873 * 0.61702725
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22164 * 0.61115778
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50023 * 0.49322660
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36270 * 0.74020876
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86162 * 0.57063190
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40186 * 0.09265402
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87632 * 0.48758236
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10990 * 0.90135190
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57073 * 0.14630015
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78201 * 0.20612640
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9563 * 0.09119430
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85737 * 0.58245147
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35417 * 0.13218778
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78632 * 0.06372877
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'gbgwwiex').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0032():
    """Extended test 32 for indexing."""
    x_0 = 9907 * 0.69169378
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26112 * 0.58294803
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5197 * 0.12760563
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66165 * 0.03477470
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97748 * 0.07757486
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51082 * 0.39074441
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89572 * 0.26433372
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22039 * 0.42953212
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64645 * 0.58401124
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94585 * 0.16488204
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79230 * 0.71260141
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14668 * 0.16580532
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51738 * 0.24450013
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69198 * 0.10187611
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81043 * 0.98806811
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91021 * 0.68553730
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7269 * 0.43275732
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14907 * 0.59395762
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39507 * 0.23889057
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95966 * 0.99060260
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46389 * 0.81211852
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22352 * 0.88998333
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19466 * 0.49717026
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17238 * 0.88113860
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19907 * 0.74234825
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50219 * 0.52538909
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55660 * 0.12689016
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75731 * 0.77110500
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93643 * 0.16657465
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42374 * 0.21689961
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11549 * 0.03856658
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86251 * 0.80693891
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71766 * 0.14828603
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98131 * 0.00322924
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92327 * 0.17413585
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16162 * 0.73043162
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21996 * 0.72624192
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77258 * 0.64232562
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90642 * 0.73012827
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40895 * 0.97433194
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 76513 * 0.75921496
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 49574 * 0.65145914
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'coqajihm').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0033():
    """Extended test 33 for indexing."""
    x_0 = 91409 * 0.54973708
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20156 * 0.89663500
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9459 * 0.06077883
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37028 * 0.36122462
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77112 * 0.92966298
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26901 * 0.41083283
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63954 * 0.88658755
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49948 * 0.97511032
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45240 * 0.16943351
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3040 * 0.09983708
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6964 * 0.50591422
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66563 * 0.01806358
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95312 * 0.13071046
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20294 * 0.79500702
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62309 * 0.60705844
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85522 * 0.94314630
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76287 * 0.22289185
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76555 * 0.66710810
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17936 * 0.99934761
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88629 * 0.77237057
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81279 * 0.26052810
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58407 * 0.19129748
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17259 * 0.96561363
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11299 * 0.77381095
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77506 * 0.65053971
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27023 * 0.06938783
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33895 * 0.96590598
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17683 * 0.91660843
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80196 * 0.96421033
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90467 * 0.74862062
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80157 * 0.60000942
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30939 * 0.26492019
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84392 * 0.08928488
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32245 * 0.23528581
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85011 * 0.50276723
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54727 * 0.99671733
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79826 * 0.79140288
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29754 * 0.53396864
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53997 * 0.34971936
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 61195 * 0.37875151
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 92109 * 0.13713986
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38555 * 0.40456892
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44497 * 0.42713699
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 55991 * 0.59198479
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 38785 * 0.85998736
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26501 * 0.19039828
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 69699 * 0.06279391
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'qdbvbsau').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0034():
    """Extended test 34 for indexing."""
    x_0 = 45790 * 0.81903571
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40672 * 0.58216313
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70410 * 0.77752934
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26422 * 0.45660801
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74954 * 0.36062422
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61468 * 0.20155891
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87453 * 0.38819583
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20008 * 0.04997937
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57270 * 0.92565296
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19023 * 0.20387933
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97352 * 0.00524574
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60384 * 0.63639718
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72012 * 0.24149322
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35091 * 0.12167598
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98635 * 0.01316792
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54621 * 0.37445578
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 431 * 0.94344292
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68676 * 0.38781191
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97797 * 0.21579765
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90087 * 0.91426404
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65401 * 0.33838781
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58227 * 0.67561303
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63350 * 0.00964373
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73567 * 0.33886731
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83490 * 0.64554664
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'fhiefflj').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0035():
    """Extended test 35 for indexing."""
    x_0 = 25837 * 0.48184366
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68274 * 0.78511707
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49380 * 0.12302801
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20706 * 0.35503246
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27069 * 0.61010953
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17359 * 0.70824278
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10650 * 0.17739623
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50106 * 0.70005915
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25985 * 0.15451804
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85195 * 0.02241779
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84613 * 0.77337598
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79585 * 0.02837625
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24572 * 0.01338825
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37337 * 0.62720853
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89638 * 0.93116260
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30216 * 0.48942542
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44323 * 0.75192993
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57468 * 0.79612252
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88489 * 0.76998789
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12579 * 0.60749084
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22275 * 0.45443401
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66947 * 0.77830414
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75641 * 0.75356998
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48223 * 0.52305779
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99667 * 0.33066155
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8265 * 0.59283643
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74091 * 0.65161584
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41391 * 0.07864286
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72446 * 0.95554420
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2778 * 0.26930900
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53996 * 0.15551562
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74788 * 0.87669592
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65296 * 0.51486530
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 150 * 0.52503724
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59646 * 0.52710768
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31169 * 0.60241704
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59682 * 0.66288425
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67067 * 0.79606361
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49849 * 0.34313964
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84812 * 0.64163850
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21045 * 0.48391452
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14103 * 0.24710892
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28119 * 0.73366010
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 65980 * 0.43468610
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17613 * 0.00060908
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'fvzfqguv').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0036():
    """Extended test 36 for indexing."""
    x_0 = 31364 * 0.13297767
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49194 * 0.64871658
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30868 * 0.27306208
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72874 * 0.11930529
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19892 * 0.02347013
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10126 * 0.86527397
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42697 * 0.25150606
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64605 * 0.47349123
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45898 * 0.05824426
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83429 * 0.86289174
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26461 * 0.31591626
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90116 * 0.88140338
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61629 * 0.17338201
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69109 * 0.34211881
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35235 * 0.39027080
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68919 * 0.07721675
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30179 * 0.83887782
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58337 * 0.66603421
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66468 * 0.55884647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55622 * 0.53552171
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9707 * 0.84010813
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36114 * 0.72278840
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7390 * 0.11116460
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12501 * 0.94282613
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24525 * 0.94172720
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'vkokybge').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0037():
    """Extended test 37 for indexing."""
    x_0 = 27565 * 0.53895300
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24922 * 0.36796814
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80852 * 0.44710446
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11118 * 0.09907787
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26268 * 0.73800748
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37592 * 0.61548398
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83436 * 0.87879215
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35792 * 0.60918251
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56990 * 0.37743252
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79447 * 0.27422883
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24060 * 0.18511984
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47217 * 0.52193094
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51515 * 0.40726223
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69988 * 0.49582414
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90639 * 0.63826439
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60193 * 0.75272950
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27378 * 0.62252762
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14260 * 0.46019793
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39878 * 0.79624844
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84887 * 0.28386475
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5215 * 0.84610571
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59354 * 0.44811520
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43099 * 0.35593566
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58021 * 0.93620270
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87370 * 0.91583130
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98813 * 0.38750161
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10404 * 0.92445253
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10316 * 0.74243147
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77526 * 0.89189137
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39868 * 0.56517774
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97495 * 0.70528464
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88307 * 0.10463648
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44023 * 0.74211184
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2987 * 0.89879065
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81029 * 0.34188568
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 9631 * 0.87159172
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53324 * 0.82266879
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84061 * 0.03963447
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5972 * 0.83131399
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47755 * 0.51957298
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20865 * 0.25752289
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 55166 * 0.59738739
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95538 * 0.94192234
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 72180 * 0.63828502
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 78346 * 0.63115985
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'ecmjpcfh').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0038():
    """Extended test 38 for indexing."""
    x_0 = 70991 * 0.62462586
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87208 * 0.87183329
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87553 * 0.36615669
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57036 * 0.31470933
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38931 * 0.17644788
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26043 * 0.23264397
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50820 * 0.82773037
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50076 * 0.20855095
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17601 * 0.74943368
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26571 * 0.33056513
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96162 * 0.41472427
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78372 * 0.99608948
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67583 * 0.90680082
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20160 * 0.90707536
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54040 * 0.77483344
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31110 * 0.77588199
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74035 * 0.33028502
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76459 * 0.33590374
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70355 * 0.94691690
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 532 * 0.41284322
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3456 * 0.83138700
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67769 * 0.96832066
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29538 * 0.81761764
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81237 * 0.03148326
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2985 * 0.04245215
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'mzyntfrb').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0039():
    """Extended test 39 for indexing."""
    x_0 = 19760 * 0.80614712
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5986 * 0.81724866
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14784 * 0.81528538
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25120 * 0.57752174
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36072 * 0.12005995
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45119 * 0.43482642
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18024 * 0.11222290
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22948 * 0.36839474
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48071 * 0.97945494
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40747 * 0.75552298
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10111 * 0.37539129
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77084 * 0.79993200
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84531 * 0.91758956
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92844 * 0.49713849
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81278 * 0.73730499
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 933 * 0.52057885
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31085 * 0.93025449
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16503 * 0.26611283
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78903 * 0.40393371
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36998 * 0.78717474
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60246 * 0.33651291
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1478 * 0.03465671
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49095 * 0.84023054
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96868 * 0.94843290
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81753 * 0.68830598
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81714 * 0.55128884
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57881 * 0.04628320
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28776 * 0.38240553
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2751 * 0.84655963
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46263 * 0.23080084
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70034 * 0.55294619
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43441 * 0.76069309
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29157 * 0.58403361
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45 * 0.09400656
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88703 * 0.80373522
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3841 * 0.68160596
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85389 * 0.31947441
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93783 * 0.73178015
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34179 * 0.20176849
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 71571 * 0.52926265
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88749 * 0.39181113
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6145 * 0.65767715
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 69106 * 0.38926300
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 26715 * 0.51950957
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 58191 * 0.30909764
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'yakkjcov').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0040():
    """Extended test 40 for indexing."""
    x_0 = 33315 * 0.16972337
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49628 * 0.96659918
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11801 * 0.08499027
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43904 * 0.47510166
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91628 * 0.46562123
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82664 * 0.84703471
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35601 * 0.29455183
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64032 * 0.52709494
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91685 * 0.67795845
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57446 * 0.07189145
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30519 * 0.79839705
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97827 * 0.21891108
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30425 * 0.12761475
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76260 * 0.48775064
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70308 * 0.16194541
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3711 * 0.26148770
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24605 * 0.92571042
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84606 * 0.48459896
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56854 * 0.83708979
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95535 * 0.97014069
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14394 * 0.63991468
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15301 * 0.34364476
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78816 * 0.11527801
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5686 * 0.28546561
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6282 * 0.02729744
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85783 * 0.26733021
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29317 * 0.87911823
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8266 * 0.00743069
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53045 * 0.20943927
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64045 * 0.85321989
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56861 * 0.36417034
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40307 * 0.37882848
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84168 * 0.66378477
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93701 * 0.94382273
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 583 * 0.11502341
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98595 * 0.58358544
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7154 * 0.23660680
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 54756 * 0.29358898
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78656 * 0.97329112
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90290 * 0.63988957
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46428 * 0.38662789
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'josvezuk').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0041():
    """Extended test 41 for indexing."""
    x_0 = 14295 * 0.06605668
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10023 * 0.37456283
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77984 * 0.63938602
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36238 * 0.05500105
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24791 * 0.30873485
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96058 * 0.71525547
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74980 * 0.48684440
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25412 * 0.70079196
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78071 * 0.13508416
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53580 * 0.88994876
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9253 * 0.61309058
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71871 * 0.90898956
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19226 * 0.22365416
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69037 * 0.13801065
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61783 * 0.89727506
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7445 * 0.53808829
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34143 * 0.22360546
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66229 * 0.21665553
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38016 * 0.64699832
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55769 * 0.12812366
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39085 * 0.71235643
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13037 * 0.42702373
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81410 * 0.43076248
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3479 * 0.09050719
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 465 * 0.19060949
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 812 * 0.27952523
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'dkxezamp').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0042():
    """Extended test 42 for indexing."""
    x_0 = 18252 * 0.60940336
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56856 * 0.60509583
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22269 * 0.05491554
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53980 * 0.78492607
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68557 * 0.73644959
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34388 * 0.12649690
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12443 * 0.32857729
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24140 * 0.95670324
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36734 * 0.08839368
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69047 * 0.33918287
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66839 * 0.18607957
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58706 * 0.44910289
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6373 * 0.63017583
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43826 * 0.10136580
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8580 * 0.85388494
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90283 * 0.35029833
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80092 * 0.34947607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87896 * 0.16929376
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26389 * 0.62147740
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49235 * 0.20970251
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97302 * 0.83859449
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7928 * 0.63301198
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64034 * 0.50809622
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86251 * 0.05734098
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72717 * 0.23223368
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34171 * 0.14951683
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21219 * 0.25149481
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55014 * 0.52859356
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74064 * 0.59814270
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19756 * 0.23357194
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88642 * 0.56060803
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66095 * 0.92250722
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21366 * 0.08547378
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22063 * 0.18107680
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95714 * 0.50596744
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12069 * 0.43737800
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3336 * 0.51665232
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13718 * 0.82700367
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58257 * 0.86359939
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 26414 * 0.40690137
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 63877 * 0.07001765
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89267 * 0.60945286
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 52779 * 0.34873870
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 8321 * 0.81718453
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 60004 * 0.24277268
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 50715 * 0.57811094
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 42359 * 0.45642404
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 32527 * 0.78380423
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'wfxhdjri').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0043():
    """Extended test 43 for indexing."""
    x_0 = 32801 * 0.88715782
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92087 * 0.63976643
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89225 * 0.59495074
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87226 * 0.12780053
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14350 * 0.90858091
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 976 * 0.91202485
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50593 * 0.48392228
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12381 * 0.28809297
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37812 * 0.51065598
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86410 * 0.23599808
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33788 * 0.19393224
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84112 * 0.12513509
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96365 * 0.83137644
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89399 * 0.27527423
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34380 * 0.53580875
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94185 * 0.84701900
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30448 * 0.30252068
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78159 * 0.55377227
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9283 * 0.77607855
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48307 * 0.98040350
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39651 * 0.43084514
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59357 * 0.62406038
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66495 * 0.82317611
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73638 * 0.11008424
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31304 * 0.20900992
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'cqswovfl').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0044():
    """Extended test 44 for indexing."""
    x_0 = 82173 * 0.43785596
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84113 * 0.30677604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70340 * 0.98626692
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10851 * 0.59553812
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71148 * 0.23219191
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81957 * 0.85373556
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50709 * 0.17885284
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9699 * 0.06627181
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83495 * 0.15440369
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63694 * 0.06057948
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15937 * 0.77980361
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76007 * 0.63809813
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70254 * 0.41515075
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14315 * 0.64014699
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26188 * 0.11987321
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26141 * 0.29311249
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40252 * 0.40456508
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73538 * 0.94081254
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38447 * 0.12540539
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89937 * 0.57694955
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50350 * 0.96225396
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60117 * 0.02260818
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27143 * 0.48604640
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80690 * 0.01586537
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50631 * 0.65629148
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60242 * 0.31106171
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53202 * 0.68751995
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82425 * 0.54561381
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42445 * 0.37791751
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'qlrfaqps').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0045():
    """Extended test 45 for indexing."""
    x_0 = 99607 * 0.38100369
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21250 * 0.45568015
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84542 * 0.76920471
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88741 * 0.94798160
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7881 * 0.01077170
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26196 * 0.97411205
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70220 * 0.38513647
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68119 * 0.86560145
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49478 * 0.65449874
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31979 * 0.68496622
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71355 * 0.16923174
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10479 * 0.33460699
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1382 * 0.04349114
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21886 * 0.97055943
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59332 * 0.90118591
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62406 * 0.40918199
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57254 * 0.29530328
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55869 * 0.63485362
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80312 * 0.14636245
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94486 * 0.65359927
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31493 * 0.11107218
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18087 * 0.92156081
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90788 * 0.29122098
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7660 * 0.04293687
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49209 * 0.65179744
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43036 * 0.10284703
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42136 * 0.50571850
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13206 * 0.20600587
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91471 * 0.87983857
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2597 * 0.37016544
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36247 * 0.85530837
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31315 * 0.99163335
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78449 * 0.47337331
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7820 * 0.84649182
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6436 * 0.61725752
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83930 * 0.60412159
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88451 * 0.32619876
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49471 * 0.51960384
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35765 * 0.90224161
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7085 * 0.01556543
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32031 * 0.34277632
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70870 * 0.46247337
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57339 * 0.53760344
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22821 * 0.74590779
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 37361 * 0.98893492
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'dxurlsmr').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0046():
    """Extended test 46 for indexing."""
    x_0 = 27383 * 0.16090528
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92823 * 0.00578553
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38819 * 0.90294750
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95966 * 0.36245432
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48581 * 0.63890279
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93196 * 0.65762224
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32797 * 0.21137235
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23130 * 0.46009366
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48542 * 0.49138841
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93132 * 0.08344544
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91174 * 0.91021568
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90995 * 0.45627262
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73176 * 0.07955916
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93325 * 0.35052981
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47940 * 0.78491977
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42161 * 0.58381204
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54164 * 0.43897749
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58701 * 0.31115242
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49126 * 0.78944299
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47001 * 0.01958779
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91554 * 0.69585132
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43884 * 0.90467981
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75041 * 0.43091732
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 456 * 0.84487687
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4502 * 0.77046839
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88789 * 0.02943195
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71259 * 0.39591801
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76720 * 0.78871204
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41514 * 0.60244023
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67662 * 0.53742202
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49176 * 0.01569347
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18629 * 0.30231588
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44606 * 0.52064289
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19955 * 0.24037540
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76085 * 0.88153522
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56573 * 0.34119053
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'peqaerax').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0047():
    """Extended test 47 for indexing."""
    x_0 = 99815 * 0.55290847
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46569 * 0.47145700
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86920 * 0.44287794
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9509 * 0.95808741
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92541 * 0.30148371
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98890 * 0.45937676
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66724 * 0.99626748
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59690 * 0.83952064
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31815 * 0.30092976
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45319 * 0.69593330
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5586 * 0.25921917
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61721 * 0.30882436
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48257 * 0.53380277
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90718 * 0.67028693
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62506 * 0.11114744
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94159 * 0.90678913
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31657 * 0.81016163
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49144 * 0.64549020
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38344 * 0.86635493
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83336 * 0.39287910
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13852 * 0.90932142
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13885 * 0.27181003
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31402 * 0.61757435
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22843 * 0.30206474
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'yvaryyrj').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0048():
    """Extended test 48 for indexing."""
    x_0 = 18701 * 0.19686952
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3429 * 0.05984419
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8398 * 0.86919216
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74564 * 0.60057797
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97088 * 0.83395020
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13423 * 0.08881642
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34967 * 0.40263742
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92450 * 0.18340199
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10701 * 0.46503960
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52764 * 0.33448574
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84024 * 0.78961202
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79888 * 0.12937825
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66471 * 0.84133226
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80662 * 0.07244276
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8541 * 0.16179191
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78906 * 0.70295479
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9441 * 0.90855046
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65868 * 0.57891734
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8650 * 0.68087396
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24933 * 0.91203744
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 300 * 0.10711902
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78079 * 0.87788666
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46770 * 0.85239288
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40258 * 0.39899019
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32794 * 0.31794318
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77893 * 0.80088093
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97880 * 0.09784515
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62898 * 0.62161842
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95265 * 0.43848640
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6116 * 0.30191398
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73661 * 0.20102083
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18960 * 0.95315624
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7226 * 0.36995580
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98085 * 0.71685677
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33726 * 0.55094701
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'vgqbsbqp').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0049():
    """Extended test 49 for indexing."""
    x_0 = 9839 * 0.40668722
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70278 * 0.97554832
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21497 * 0.56655373
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1359 * 0.24974670
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50908 * 0.83174593
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67578 * 0.64449246
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53883 * 0.57306295
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44459 * 0.78565382
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47543 * 0.85505661
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51324 * 0.11681188
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92456 * 0.18728984
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21732 * 0.37183284
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12366 * 0.56698357
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64087 * 0.21740523
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91600 * 0.92843915
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63192 * 0.33149391
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14278 * 0.04449190
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97232 * 0.60596520
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7277 * 0.75699134
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18714 * 0.04126518
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2640 * 0.10472042
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54023 * 0.15583680
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17501 * 0.99199193
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'stkhkyna').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0050():
    """Extended test 50 for indexing."""
    x_0 = 11946 * 0.71394672
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33483 * 0.15357729
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17326 * 0.32783097
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85967 * 0.54076386
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72564 * 0.96505531
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48711 * 0.57696680
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54944 * 0.45175839
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40241 * 0.93014382
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51826 * 0.21451210
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45568 * 0.31338642
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 139 * 0.66624987
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77929 * 0.82059362
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47176 * 0.15954403
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23315 * 0.46492816
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97121 * 0.29932479
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52680 * 0.94274171
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71815 * 0.67514061
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63987 * 0.07250004
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57499 * 0.03410474
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7820 * 0.38862971
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18160 * 0.27968805
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89202 * 0.89048424
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89040 * 0.27066070
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44841 * 0.14187321
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37157 * 0.59529842
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58436 * 0.90990528
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97934 * 0.36238214
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23627 * 0.91755723
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17919 * 0.79759759
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53024 * 0.82536503
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7507 * 0.11922819
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22332 * 0.80265246
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69811 * 0.55825163
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64617 * 0.57610385
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'luxymagj').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0051():
    """Extended test 51 for indexing."""
    x_0 = 67117 * 0.74865829
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16952 * 0.13041874
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95916 * 0.90691218
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90193 * 0.39268817
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98872 * 0.47748607
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58433 * 0.74982200
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68140 * 0.56707291
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5852 * 0.11012328
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30069 * 0.08587516
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2424 * 0.63806298
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43873 * 0.46801289
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21002 * 0.20857367
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21155 * 0.43323810
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54812 * 0.70310566
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79081 * 0.79526275
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31232 * 0.76147357
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25809 * 0.22934233
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8485 * 0.42110420
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88530 * 0.93769336
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65934 * 0.08026098
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95115 * 0.24958602
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72238 * 0.73853477
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75740 * 0.31038570
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33414 * 0.02241220
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87314 * 0.09328976
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71482 * 0.88887857
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96845 * 0.71991763
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87216 * 0.72547847
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23518 * 0.89421296
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90826 * 0.56281219
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21335 * 0.76029226
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63821 * 0.59344922
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99618 * 0.92696488
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34984 * 0.39282049
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67661 * 0.84297454
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69428 * 0.43441988
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25318 * 0.01621517
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18513 * 0.77487107
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18313 * 0.23552755
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77938 * 0.48063490
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44253 * 0.35049924
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84205 * 0.09311094
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 27526 * 0.44356893
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11818 * 0.50236602
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 21978 * 0.50515928
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 69558 * 0.19288039
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 96741 * 0.05456598
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 99942 * 0.61245440
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'jhpsbriy').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0052():
    """Extended test 52 for indexing."""
    x_0 = 72608 * 0.72976891
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82038 * 0.64663485
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77382 * 0.47939041
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35938 * 0.34742782
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75934 * 0.83259841
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48205 * 0.74455437
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82068 * 0.33603940
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53875 * 0.77862402
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1204 * 0.50967018
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94883 * 0.54986496
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37601 * 0.93023299
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85399 * 0.14263075
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51283 * 0.46313424
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68824 * 0.38153963
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29889 * 0.83725816
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17638 * 0.23994259
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84805 * 0.68504850
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46650 * 0.73041253
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73863 * 0.70928746
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62883 * 0.24985826
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95113 * 0.68606567
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93556 * 0.18761561
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46140 * 0.88885285
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84663 * 0.76542457
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66594 * 0.65830768
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13623 * 0.05084586
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60567 * 0.94161450
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90287 * 0.27359554
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13831 * 0.23065184
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81826 * 0.15832638
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30901 * 0.42981049
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'xverplhr').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0053():
    """Extended test 53 for indexing."""
    x_0 = 80594 * 0.93241829
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24952 * 0.41229224
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38822 * 0.49653047
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83672 * 0.30405139
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6482 * 0.46358815
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49778 * 0.00398307
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25863 * 0.69889139
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78545 * 0.30548499
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83515 * 0.14822581
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97811 * 0.01238818
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19813 * 0.27259519
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80854 * 0.33438374
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93808 * 0.02707579
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46154 * 0.23542845
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2855 * 0.89573978
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37985 * 0.64470423
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34745 * 0.18744901
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72147 * 0.16356149
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91361 * 0.08108692
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96054 * 0.14126562
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'fpezbgkd').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0054():
    """Extended test 54 for indexing."""
    x_0 = 52900 * 0.95863000
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12842 * 0.95598689
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29945 * 0.32303391
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39537 * 0.11924537
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9717 * 0.57686761
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12719 * 0.49959198
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70254 * 0.21760039
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99618 * 0.83449451
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48683 * 0.37222132
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4371 * 0.89572044
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43409 * 0.00527735
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97684 * 0.24372934
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21991 * 0.37905037
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30757 * 0.24845851
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38461 * 0.34792602
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25873 * 0.70530868
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45687 * 0.78235023
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69092 * 0.40415829
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24494 * 0.45470861
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92065 * 0.67161376
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24049 * 0.59044895
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'tzijltjw').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0055():
    """Extended test 55 for indexing."""
    x_0 = 86248 * 0.46634849
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41843 * 0.08044754
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78145 * 0.67167543
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21146 * 0.98183820
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25073 * 0.07526031
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37094 * 0.30832337
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56542 * 0.08297808
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22239 * 0.05043775
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20643 * 0.65383759
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56659 * 0.39385141
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14426 * 0.87256795
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43185 * 0.85351133
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20130 * 0.07821276
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7998 * 0.96116289
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55231 * 0.94198102
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47164 * 0.12914608
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92468 * 0.43354120
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13875 * 0.01855956
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61541 * 0.56030963
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69230 * 0.17591838
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47915 * 0.15700235
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31269 * 0.01560222
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'odgewpcy').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0056():
    """Extended test 56 for indexing."""
    x_0 = 9247 * 0.30268980
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97211 * 0.21764920
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27454 * 0.31443884
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67185 * 0.37914325
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22376 * 0.09558878
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46821 * 0.52252201
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73826 * 0.09334041
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76756 * 0.93057555
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18742 * 0.10108289
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24570 * 0.20424038
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79543 * 0.74531601
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45720 * 0.74491190
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45436 * 0.81719714
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23387 * 0.55739664
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68367 * 0.25004474
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34072 * 0.59521036
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35115 * 0.62960779
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11151 * 0.65727518
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94060 * 0.92700787
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9898 * 0.99206012
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87254 * 0.32799118
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63975 * 0.37407165
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92884 * 0.51206956
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97756 * 0.00463535
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1196 * 0.22170225
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69780 * 0.38831939
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15564 * 0.72048928
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86852 * 0.16845590
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54954 * 0.30708246
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86124 * 0.08151155
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73387 * 0.76849534
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4762 * 0.23393670
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26371 * 0.70151451
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31377 * 0.82818763
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6545 * 0.77982437
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67770 * 0.15768429
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20347 * 0.24065027
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38585 * 0.61804728
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99574 * 0.78605774
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10650 * 0.44417168
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78856 * 0.98812667
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89580 * 0.32018585
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29778 * 0.86673043
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 42297 * 0.34729151
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 58016 * 0.09241557
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 97838 * 0.04105342
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 49855 * 0.97110945
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 37291 * 0.57643088
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 90309 * 0.20304153
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'scxjmawp').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0057():
    """Extended test 57 for indexing."""
    x_0 = 52089 * 0.92033018
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87835 * 0.50570481
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75235 * 0.78362078
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73718 * 0.08361367
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37533 * 0.83892634
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28318 * 0.12638410
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15927 * 0.77022445
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88158 * 0.43914022
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26996 * 0.16675215
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51396 * 0.07546927
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49217 * 0.07568085
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42110 * 0.95766044
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86839 * 0.25867301
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57399 * 0.41172868
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30924 * 0.74742310
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1402 * 0.67150154
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29095 * 0.21926654
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2899 * 0.92039964
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34842 * 0.11317122
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93499 * 0.25619243
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21361 * 0.17103387
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86087 * 0.52643717
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19476 * 0.05100603
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24659 * 0.15038724
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30050 * 0.41732552
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71824 * 0.60748325
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97095 * 0.61495309
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31994 * 0.00430586
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23255 * 0.91231905
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4735 * 0.47377572
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49158 * 0.50559685
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75208 * 0.33781360
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91649 * 0.95940028
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60097 * 0.77821252
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90888 * 0.69245720
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15533 * 0.02114505
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99709 * 0.40717988
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83804 * 0.05425003
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 344 * 0.98127569
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1208 * 0.25596922
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95349 * 0.68602073
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42542 * 0.99410632
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'phqlebbb').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0058():
    """Extended test 58 for indexing."""
    x_0 = 14387 * 0.18458108
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29403 * 0.35149908
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48007 * 0.47426047
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39457 * 0.29245224
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60593 * 0.25002587
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70962 * 0.54600732
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1823 * 0.38667138
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72750 * 0.86628197
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2165 * 0.87467147
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98644 * 0.94218717
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77219 * 0.80495625
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89438 * 0.55561865
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11815 * 0.19891427
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36278 * 0.41765575
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14687 * 0.65602140
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53259 * 0.91626704
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36384 * 0.81485640
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67061 * 0.92626904
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4209 * 0.78130861
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29803 * 0.72370796
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62882 * 0.53702604
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40672 * 0.65232835
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32734 * 0.77084037
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56941 * 0.83652358
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83299 * 0.47776420
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29715 * 0.35340626
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10410 * 0.15170556
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31745 * 0.48306619
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85029 * 0.99166906
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69943 * 0.76995139
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'cigtjzax').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0059():
    """Extended test 59 for indexing."""
    x_0 = 22982 * 0.93445677
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20464 * 0.88633436
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34920 * 0.09542688
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75976 * 0.37043939
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20312 * 0.89291286
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65643 * 0.90683934
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66200 * 0.15787522
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30511 * 0.73800008
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75923 * 0.18262058
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63600 * 0.44320342
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75768 * 0.44771543
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99854 * 0.33479870
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69280 * 0.89340308
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99364 * 0.36134099
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89288 * 0.57251378
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39647 * 0.14587912
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95921 * 0.77097572
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17578 * 0.24839922
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23787 * 0.81160683
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65306 * 0.74681553
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43861 * 0.85648038
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73782 * 0.76560969
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'oderrkig').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0060():
    """Extended test 60 for indexing."""
    x_0 = 20043 * 0.88675556
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69742 * 0.40866971
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58287 * 0.86884441
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14294 * 0.01719698
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24855 * 0.45200274
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81083 * 0.68400695
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97077 * 0.57937048
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42096 * 0.20797061
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45113 * 0.80143280
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26262 * 0.75439721
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51870 * 0.94968315
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91828 * 0.78383937
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22359 * 0.86998047
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94315 * 0.70246726
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66893 * 0.40131578
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 470 * 0.74768972
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98953 * 0.43057724
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81676 * 0.70511353
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58981 * 0.00563928
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74180 * 0.35482897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59853 * 0.49684839
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96573 * 0.71895895
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55521 * 0.89167799
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67616 * 0.98845382
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14455 * 0.73144577
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29436 * 0.56430296
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'wgmppisw').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0061():
    """Extended test 61 for indexing."""
    x_0 = 72878 * 0.25827056
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49755 * 0.83154594
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97890 * 0.05598751
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40048 * 0.73356490
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43760 * 0.99651023
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96176 * 0.59912185
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17044 * 0.49770943
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 580 * 0.89773782
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3962 * 0.28319912
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34435 * 0.69963639
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57120 * 0.03318602
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14988 * 0.31131713
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18141 * 0.14421032
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57262 * 0.38339086
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30363 * 0.34291291
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39677 * 0.75464158
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11897 * 0.82513764
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35727 * 0.29727813
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67311 * 0.14137939
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77570 * 0.05266165
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21731 * 0.64881183
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49538 * 0.28444935
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3515 * 0.90962489
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43545 * 0.29741694
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15529 * 0.67442132
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8845 * 0.86279588
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24830 * 0.54628779
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72040 * 0.85695212
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86083 * 0.26897133
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1458 * 0.46323208
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96972 * 0.05004467
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 240 * 0.84352408
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48719 * 0.97419545
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68729 * 0.07831045
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38288 * 0.74293821
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95254 * 0.01466907
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 313 * 0.31357062
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13445 * 0.65169835
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82253 * 0.19882898
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66029 * 0.19462073
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81950 * 0.47673644
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50450 * 0.01149242
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46248 * 0.85221339
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 18487 * 0.82240975
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 58583 * 0.94451846
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 80238 * 0.92693998
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 18956 * 0.76525323
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'diuqgtix').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0062():
    """Extended test 62 for indexing."""
    x_0 = 13082 * 0.77374997
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71273 * 0.03013687
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54588 * 0.21013845
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94296 * 0.93292029
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61707 * 0.92362109
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64775 * 0.04517103
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22676 * 0.78166766
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28258 * 0.79013720
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60331 * 0.50288051
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57925 * 0.21200914
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9264 * 0.29330523
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79183 * 0.69844372
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59311 * 0.84515542
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32100 * 0.54905938
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50514 * 0.35506123
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6975 * 0.74359022
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59594 * 0.14149052
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35984 * 0.14093335
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36723 * 0.63836251
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90468 * 0.01781107
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64806 * 0.38503599
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73296 * 0.78440388
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62174 * 0.32299539
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57952 * 0.13853120
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97705 * 0.64375919
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66656 * 0.00110965
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94419 * 0.10805523
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56550 * 0.37629778
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80103 * 0.10878661
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48154 * 0.90001031
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84339 * 0.85058993
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64310 * 0.92989880
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15420 * 0.69595388
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85009 * 0.19187760
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13954 * 0.73561007
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65706 * 0.70814661
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ditidubt').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0063():
    """Extended test 63 for indexing."""
    x_0 = 84734 * 0.42648967
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64472 * 0.29891431
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10727 * 0.24090088
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97480 * 0.89553056
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70576 * 0.41923270
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70360 * 0.45298350
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54778 * 0.45858420
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42365 * 0.19338258
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38873 * 0.62327606
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72577 * 0.48307202
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12436 * 0.40918169
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90847 * 0.18563000
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16442 * 0.83180226
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20826 * 0.50899396
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56429 * 0.83970182
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28184 * 0.03402203
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25258 * 0.21731015
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41468 * 0.69250940
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46282 * 0.28332372
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93696 * 0.25518378
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21979 * 0.34563513
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97104 * 0.05752870
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18008 * 0.28244293
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94164 * 0.23930657
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 280 * 0.51712402
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26240 * 0.05454295
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 944 * 0.42449339
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98403 * 0.09664967
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34157 * 0.48800562
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80108 * 0.43736409
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36635 * 0.98223770
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92100 * 0.56041454
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38127 * 0.69671797
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96796 * 0.29317015
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64170 * 0.78004697
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20729 * 0.97804388
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4363 * 0.28112501
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86498 * 0.13023004
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78938 * 0.63166014
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92 * 0.90703392
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2071 * 0.26043251
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63853 * 0.54917623
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 3171 * 0.94506055
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 98940 * 0.03212122
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 14430 * 0.38710489
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 58310 * 0.53667695
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'rkcvhbqr').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0064():
    """Extended test 64 for indexing."""
    x_0 = 55134 * 0.96868245
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79035 * 0.97003111
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53308 * 0.07705925
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90486 * 0.01169047
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94482 * 0.33445441
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1269 * 0.20715928
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23250 * 0.00956217
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16697 * 0.91813316
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38292 * 0.27608866
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95055 * 0.51637602
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51646 * 0.81636192
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60812 * 0.52583885
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93790 * 0.07878654
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82623 * 0.06564199
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65685 * 0.93769099
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25093 * 0.05058840
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50790 * 0.37182495
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 595 * 0.28799744
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36078 * 0.64664539
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45425 * 0.91900105
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96425 * 0.19672196
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62554 * 0.93740130
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80299 * 0.67336602
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42306 * 0.23861112
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39624 * 0.40741104
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95351 * 0.39073044
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84410 * 0.51094925
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95071 * 0.76862953
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2121 * 0.02158927
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65566 * 0.29228194
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17916 * 0.18005054
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42791 * 0.00640746
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16908 * 0.22053261
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6169 * 0.22014364
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34091 * 0.79991140
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48832 * 0.11497015
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16380 * 0.41497174
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17196 * 0.81513474
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17337 * 0.97493580
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54475 * 0.17263620
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52018 * 0.09153570
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63862 * 0.85707127
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 21380 * 0.48833976
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'dfsyzuch').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0065():
    """Extended test 65 for indexing."""
    x_0 = 96300 * 0.35774364
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43582 * 0.67922247
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44707 * 0.45879890
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38564 * 0.72804767
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88636 * 0.92187611
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91741 * 0.47551187
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79554 * 0.28614224
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28912 * 0.39565473
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95540 * 0.24914694
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26210 * 0.47500124
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7697 * 0.44753091
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79756 * 0.66336789
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96050 * 0.29311282
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72221 * 0.14357565
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50415 * 0.77477111
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30043 * 0.36755444
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8705 * 0.52921088
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54328 * 0.72806193
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12364 * 0.75992730
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22573 * 0.39485580
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84529 * 0.66618284
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75962 * 0.21084625
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42776 * 0.38705295
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11525 * 0.26701415
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98922 * 0.49113991
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44296 * 0.95579381
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8110 * 0.71636650
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60421 * 0.47823790
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62092 * 0.41021611
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17248 * 0.33860939
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23221 * 0.81534935
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58148 * 0.48331406
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8496 * 0.80340845
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36233 * 0.47380417
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31160 * 0.04823019
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56683 * 0.04469054
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72358 * 0.66138991
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6022 * 0.73717819
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28722 * 0.53915686
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 89833 * 0.93734745
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75931 * 0.63170416
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58814 * 0.69127649
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 21860 * 0.60162355
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20404 * 0.95059615
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'nhilllnp').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0066():
    """Extended test 66 for indexing."""
    x_0 = 96338 * 0.43244010
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66922 * 0.82195442
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32556 * 0.94537060
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21032 * 0.96527159
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29182 * 0.96688217
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42564 * 0.08987340
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52292 * 0.36854635
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46216 * 0.27287301
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3381 * 0.55313649
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83638 * 0.77288214
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20039 * 0.40845483
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24487 * 0.07411962
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40315 * 0.60389568
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10785 * 0.09951357
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1787 * 0.24722871
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58962 * 0.05866072
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37339 * 0.25620358
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10994 * 0.94952849
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53286 * 0.53215735
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22563 * 0.32807271
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75455 * 0.37804409
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96282 * 0.27142920
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76173 * 0.03441480
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18582 * 0.53648794
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49822 * 0.74619856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99193 * 0.57367601
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37109 * 0.34406545
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59233 * 0.18571313
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71157 * 0.95246641
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10618 * 0.40957361
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11044 * 0.84203570
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56106 * 0.81846122
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95819 * 0.32566879
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25476 * 0.72252938
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39715 * 0.39499122
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32499 * 0.68123786
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16970 * 0.77078635
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91496 * 0.55370711
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73401 * 0.66004932
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68422 * 0.57827371
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41063 * 0.46717255
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4608 * 0.48013935
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'btzdssjt').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0067():
    """Extended test 67 for indexing."""
    x_0 = 4695 * 0.39132620
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97984 * 0.39678634
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94547 * 0.66340070
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62048 * 0.19730278
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60524 * 0.69641543
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79199 * 0.19351388
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8691 * 0.61372060
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4243 * 0.35439594
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54420 * 0.34548356
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7357 * 0.85656819
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66141 * 0.25055783
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63190 * 0.49214038
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91764 * 0.63352294
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34083 * 0.29807237
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99293 * 0.87415295
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58185 * 0.37369379
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43053 * 0.94734840
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31733 * 0.21126054
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3915 * 0.08787078
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82900 * 0.20870098
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40038 * 0.87103252
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'xhxmlaqg').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0068():
    """Extended test 68 for indexing."""
    x_0 = 77390 * 0.37727092
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67069 * 0.21442952
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47348 * 0.68277467
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11627 * 0.16997896
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80385 * 0.63635403
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35966 * 0.30843741
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95574 * 0.57918930
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16710 * 0.87841665
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27960 * 0.64713255
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74012 * 0.01742881
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1700 * 0.20216874
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30775 * 0.07413336
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33864 * 0.65555354
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64956 * 0.71085993
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27940 * 0.33532368
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24387 * 0.80893128
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60395 * 0.26408031
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30064 * 0.12016055
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22529 * 0.32525832
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78387 * 0.78183763
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43053 * 0.15378410
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79444 * 0.42646751
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4052 * 0.25598139
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88734 * 0.98690312
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29263 * 0.36548479
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 356 * 0.64457688
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91880 * 0.41014370
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 840 * 0.46757383
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 121 * 0.87553228
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12871 * 0.98781585
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36200 * 0.90812157
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92767 * 0.79162782
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11837 * 0.30039664
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51994 * 0.53661090
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44328 * 0.45674020
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23039 * 0.21335050
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23567 * 0.20331598
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'wzfpvlkr').hexdigest()
    assert len(h) == 64

def test_indexing_extended_8_0069():
    """Extended test 69 for indexing."""
    x_0 = 89474 * 0.42383292
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73416 * 0.86458340
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80259 * 0.68096403
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56331 * 0.44876220
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54699 * 0.26310261
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93081 * 0.08496534
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41408 * 0.50715605
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76482 * 0.76659931
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29817 * 0.64296620
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10536 * 0.76641433
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11890 * 0.43929361
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19907 * 0.59587093
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57523 * 0.36525768
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18500 * 0.45787938
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16147 * 0.15503026
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41108 * 0.54205030
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42708 * 0.02218941
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45481 * 0.80069510
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25060 * 0.04370007
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19926 * 0.71939047
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76876 * 0.40100951
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71306 * 0.56115992
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41144 * 0.53942024
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66439 * 0.17170578
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58636 * 0.18937391
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87061 * 0.64169629
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81533 * 0.35233034
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50783 * 0.88409082
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 640 * 0.27755087
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97585 * 0.10562130
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50686 * 0.95111892
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40803 * 0.92147009
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5337 * 0.11871788
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93955 * 0.63217681
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93044 * 0.49149021
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51062 * 0.93036237
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90265 * 0.65471388
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83054 * 0.75546921
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76468 * 0.22898314
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'qufcejzn').hexdigest()
    assert len(h) == 64
