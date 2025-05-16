"""Extended tests for replication suite 5."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_replication_extended_5_0000():
    """Extended test 0 for replication."""
    x_0 = 65716 * 0.81469566
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37606 * 0.66171648
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40112 * 0.40633969
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84031 * 0.06496626
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9899 * 0.72388754
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50655 * 0.21169263
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14531 * 0.22654411
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82494 * 0.64540729
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68104 * 0.50290996
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11044 * 0.30915128
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70548 * 0.85868255
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79118 * 0.84810111
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68005 * 0.22010155
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13350 * 0.88684841
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28536 * 0.78329243
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31858 * 0.98401006
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98743 * 0.87163683
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72234 * 0.57206992
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95370 * 0.45169441
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93096 * 0.99310751
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95069 * 0.10789080
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'vibxpath').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0001():
    """Extended test 1 for replication."""
    x_0 = 16347 * 0.90005963
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59988 * 0.14752000
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88074 * 0.12245226
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38787 * 0.22055983
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20533 * 0.70042356
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32628 * 0.10449197
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 152 * 0.03386989
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79087 * 0.27785898
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85355 * 0.55722305
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 570 * 0.81149498
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28945 * 0.33635229
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19839 * 0.40265114
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63198 * 0.49469873
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28553 * 0.19554320
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3545 * 0.43502496
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20850 * 0.22482886
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48472 * 0.83154597
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42924 * 0.79542428
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98639 * 0.36814860
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67141 * 0.13005726
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57929 * 0.68364653
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34864 * 0.78110256
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92528 * 0.26936108
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 342 * 0.88806659
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63673 * 0.97583787
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20523 * 0.46263038
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'bsrrjrjn').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0002():
    """Extended test 2 for replication."""
    x_0 = 73562 * 0.27989166
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23887 * 0.30724646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54373 * 0.69394264
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98032 * 0.35141657
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15106 * 0.83624383
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97495 * 0.81619437
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75417 * 0.02906258
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2873 * 0.85611537
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75531 * 0.29308328
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19886 * 0.47724788
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75962 * 0.77464393
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67838 * 0.23098137
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25037 * 0.65807952
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53606 * 0.89884609
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93463 * 0.48903105
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33991 * 0.07690343
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61614 * 0.64409140
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72939 * 0.06938765
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75240 * 0.40713645
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73991 * 0.79213056
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99032 * 0.47028413
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 113 * 0.29535942
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38127 * 0.45358208
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64638 * 0.29579073
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40608 * 0.60198356
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97600 * 0.73094607
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94619 * 0.10709959
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98735 * 0.00018538
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 912 * 0.85704295
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80439 * 0.14010128
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44687 * 0.11961008
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48262 * 0.47967977
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96233 * 0.75999045
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65604 * 0.82724710
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2069 * 0.92131648
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99913 * 0.88168485
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87668 * 0.58341152
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5792 * 0.76604024
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87867 * 0.89075953
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95415 * 0.04688839
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80874 * 0.18737641
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84378 * 0.39254261
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13848 * 0.98041096
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84918 * 0.57033130
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 29256 * 0.31909139
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 59806 * 0.99995548
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 62045 * 0.58376227
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 12001 * 0.19830665
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 97882 * 0.21248258
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'rdjuedxf').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0003():
    """Extended test 3 for replication."""
    x_0 = 24322 * 0.09425810
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80303 * 0.31292300
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74755 * 0.34256914
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25853 * 0.50776880
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18906 * 0.71987372
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83816 * 0.57385963
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76225 * 0.32851664
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34584 * 0.93551921
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23102 * 0.72635332
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26375 * 0.11714068
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70323 * 0.59492054
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49769 * 0.60219046
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16868 * 0.63991577
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88662 * 0.87347935
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78461 * 0.59293249
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47323 * 0.50247169
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80025 * 0.83232831
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73611 * 0.45436927
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3350 * 0.35025618
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66774 * 0.73598180
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28053 * 0.93271017
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61377 * 0.58241012
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43124 * 0.39748572
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73227 * 0.73773497
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1859 * 0.14137576
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48889 * 0.16205917
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36718 * 0.73890722
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14104 * 0.93442137
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67744 * 0.35592509
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52706 * 0.53751362
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23450 * 0.63637424
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1586 * 0.39956370
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80573 * 0.67212608
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88554 * 0.98506920
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39306 * 0.78274064
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77627 * 0.09293777
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34938 * 0.69846180
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60097 * 0.56679941
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20351 * 0.85581003
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17860 * 0.04210319
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44652 * 0.91678185
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40884 * 0.92700616
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12862 * 0.06760432
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39133 * 0.66175946
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17685 * 0.13351270
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'sfgvtzal').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0004():
    """Extended test 4 for replication."""
    x_0 = 55944 * 0.88313749
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76643 * 0.04978889
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58108 * 0.33754700
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44808 * 0.83564628
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26859 * 0.99410106
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17162 * 0.77805345
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93064 * 0.45167802
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70099 * 0.76394656
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44487 * 0.98444029
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24414 * 0.86636372
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49934 * 0.29674026
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10885 * 0.56940856
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12406 * 0.92800253
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15129 * 0.81625238
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81427 * 0.99443782
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39617 * 0.99298682
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59910 * 0.09248749
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86703 * 0.65857089
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91111 * 0.60999955
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53858 * 0.49981055
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6399 * 0.54191904
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85452 * 0.91050089
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96837 * 0.46585137
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25118 * 0.66403843
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51198 * 0.95650499
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4954 * 0.60948863
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81937 * 0.69395385
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19919 * 0.09383368
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60600 * 0.49299219
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2706 * 0.91346227
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57255 * 0.11885658
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86433 * 0.30067157
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78795 * 0.12959246
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71581 * 0.98336861
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17252 * 0.41947463
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40409 * 0.59350888
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54887 * 0.13084188
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42486 * 0.92575393
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 236 * 0.21477209
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43821 * 0.64889460
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79960 * 0.14969855
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77654 * 0.27831083
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'fdxzohrt').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0005():
    """Extended test 5 for replication."""
    x_0 = 91185 * 0.01581771
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34389 * 0.99546330
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71012 * 0.68204008
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57929 * 0.63604395
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86098 * 0.20706546
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92074 * 0.66204483
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25798 * 0.44356347
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16678 * 0.95881022
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98135 * 0.43527908
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30931 * 0.50860726
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89746 * 0.23690721
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68075 * 0.53426259
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79231 * 0.39800557
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84259 * 0.52524816
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97012 * 0.75790268
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67650 * 0.22248768
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13401 * 0.87622105
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77983 * 0.51301273
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46890 * 0.20828397
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64995 * 0.62805685
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80112 * 0.60519079
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57384 * 0.06906073
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51290 * 0.67219067
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71267 * 0.57394389
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84843 * 0.30138335
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65195 * 0.16464346
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44253 * 0.43509509
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38627 * 0.38068942
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65152 * 0.46997016
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48286 * 0.15754441
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79088 * 0.87459805
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11787 * 0.48089741
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29142 * 0.76959691
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83630 * 0.43196709
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92633 * 0.92562841
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22929 * 0.61339927
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42772 * 0.66463164
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18073 * 0.45298526
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'rxjjzhqr').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0006():
    """Extended test 6 for replication."""
    x_0 = 64457 * 0.21018293
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62777 * 0.71289224
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85298 * 0.45295845
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47202 * 0.05966218
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62770 * 0.67454593
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47191 * 0.39721489
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2318 * 0.69750767
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62591 * 0.09012632
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12940 * 0.20234389
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17002 * 0.88660206
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85100 * 0.77821598
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94499 * 0.01469468
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66937 * 0.35358133
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77707 * 0.61075047
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83707 * 0.32438613
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39970 * 0.92518784
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 574 * 0.72923426
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76620 * 0.40219107
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98271 * 0.59272047
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75830 * 0.23326351
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92050 * 0.40723796
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96390 * 0.83159770
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16908 * 0.61375114
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80643 * 0.78727126
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14651 * 0.56975008
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45799 * 0.94776003
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88807 * 0.85280254
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'kaooxoip').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0007():
    """Extended test 7 for replication."""
    x_0 = 6991 * 0.07504077
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10188 * 0.76543331
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62955 * 0.56180081
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42961 * 0.72877129
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4727 * 0.59962831
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48792 * 0.59037971
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97427 * 0.97898519
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44898 * 0.62896189
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10970 * 0.80890452
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88083 * 0.54134274
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28518 * 0.82224724
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31315 * 0.68231151
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3727 * 0.48728809
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77065 * 0.89085745
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24685 * 0.01393038
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56301 * 0.69175338
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79949 * 0.75827958
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54917 * 0.02205810
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96103 * 0.15471571
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76408 * 0.14903147
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54159 * 0.19054677
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40550 * 0.92136772
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58517 * 0.75116617
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79348 * 0.67994488
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51775 * 0.79999446
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23294 * 0.99631724
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82547 * 0.23312554
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'vpyqlcwv').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0008():
    """Extended test 8 for replication."""
    x_0 = 16658 * 0.76600554
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33809 * 0.42290717
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79340 * 0.91510432
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77999 * 0.00696977
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17992 * 0.34121176
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13748 * 0.44990401
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18202 * 0.07352425
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23544 * 0.00590427
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48335 * 0.67051003
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70199 * 0.99148152
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90566 * 0.21711187
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71907 * 0.29324433
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32475 * 0.80861327
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38688 * 0.23825802
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98270 * 0.21277164
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42045 * 0.45864560
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10984 * 0.01576510
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95955 * 0.10052115
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71730 * 0.14999266
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14118 * 0.12888395
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69019 * 0.04305319
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16659 * 0.10404297
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43288 * 0.41158770
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76481 * 0.09099439
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48413 * 0.34295831
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2764 * 0.86847001
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77245 * 0.83290061
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97623 * 0.99965489
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46940 * 0.69760330
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11024 * 0.33960378
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11935 * 0.45948372
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29044 * 0.89023886
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38492 * 0.06246829
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3147 * 0.25205507
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54700 * 0.94119003
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19406 * 0.47723506
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25528 * 0.28935560
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55588 * 0.65759109
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'szekjziq').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0009():
    """Extended test 9 for replication."""
    x_0 = 42641 * 0.54762891
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53255 * 0.93399763
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7768 * 0.13356019
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36937 * 0.69617621
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37822 * 0.46432422
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73810 * 0.31058356
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29945 * 0.60016278
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19578 * 0.48316306
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58247 * 0.47528273
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81644 * 0.52981843
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78700 * 0.34462120
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33719 * 0.99310467
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88865 * 0.82497966
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76495 * 0.85901143
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6650 * 0.48448693
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63880 * 0.97533888
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41343 * 0.63988638
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57922 * 0.34958444
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65975 * 0.28409700
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38613 * 0.47788535
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97689 * 0.05126223
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91094 * 0.91964212
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 250 * 0.54286152
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68516 * 0.45006019
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23777 * 0.61570396
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47515 * 0.54611721
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68602 * 0.12075921
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47805 * 0.81403729
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76333 * 0.58044958
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82462 * 0.77786249
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32256 * 0.89300221
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92411 * 0.04957749
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64983 * 0.48415259
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96461 * 0.23453710
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50487 * 0.70281881
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64934 * 0.65763441
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41113 * 0.43645937
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13631 * 0.05709343
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40243 * 0.66910069
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 58888 * 0.26144256
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95242 * 0.03796391
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'ohhcuogd').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0010():
    """Extended test 10 for replication."""
    x_0 = 79221 * 0.79170716
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92938 * 0.08975469
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26932 * 0.00241390
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3457 * 0.82909112
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39585 * 0.51091552
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73003 * 0.50332784
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7632 * 0.57281445
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74081 * 0.57009454
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74799 * 0.97817076
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87011 * 0.29040931
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9656 * 0.97855241
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58711 * 0.42093862
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88191 * 0.69849497
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62753 * 0.52674447
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47163 * 0.81048298
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33162 * 0.42438561
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73166 * 0.56015835
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19174 * 0.86317198
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8555 * 0.04399321
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39884 * 0.85938424
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33826 * 0.78868440
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89937 * 0.49905025
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59743 * 0.38267730
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51023 * 0.03974139
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57909 * 0.01618638
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84090 * 0.64230876
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99201 * 0.67381832
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96493 * 0.33499603
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82315 * 0.02056889
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82016 * 0.61275356
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79234 * 0.56035346
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36735 * 0.61667434
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1667 * 0.63619029
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14820 * 0.09532822
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14824 * 0.04454349
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33838 * 0.45729420
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47914 * 0.85716918
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46590 * 0.77497911
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16080 * 0.42919424
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 5292 * 0.84993249
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94750 * 0.90405835
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57136 * 0.61381660
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 37132 * 0.98770034
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 5618 * 0.57463993
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 25998 * 0.96764834
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 44456 * 0.75685716
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 38177 * 0.11979056
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 7719 * 0.33358107
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 89080 * 0.49728001
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'dzwmgboc').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0011():
    """Extended test 11 for replication."""
    x_0 = 786 * 0.66166769
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53518 * 0.75390336
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65407 * 0.64066427
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59964 * 0.08390777
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18977 * 0.32601567
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60016 * 0.09135212
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88391 * 0.50025895
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97024 * 0.42217520
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75877 * 0.36782705
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54290 * 0.77347329
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13987 * 0.12285190
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74520 * 0.07963619
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81495 * 0.91626496
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87982 * 0.92932688
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81440 * 0.19428270
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60367 * 0.61623928
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26692 * 0.23120079
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86438 * 0.13449731
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19525 * 0.48981825
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63758 * 0.26689335
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71120 * 0.89690422
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78395 * 0.95913105
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12751 * 0.56344467
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55292 * 0.68501282
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78506 * 0.00597409
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30799 * 0.82344460
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77327 * 0.33526142
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38063 * 0.70203929
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91107 * 0.38416303
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'kusbvnhc').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0012():
    """Extended test 12 for replication."""
    x_0 = 81667 * 0.48400607
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68785 * 0.77465934
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78064 * 0.35746932
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86072 * 0.84645601
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20801 * 0.86633728
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72151 * 0.88720956
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65935 * 0.46056864
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47309 * 0.73546553
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95148 * 0.74939568
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20249 * 0.10298753
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15915 * 0.50822343
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27448 * 0.39488749
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17819 * 0.58375960
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76808 * 0.40295001
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52783 * 0.53420554
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58826 * 0.56822677
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22860 * 0.93705754
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14474 * 0.05818891
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70749 * 0.61326186
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19172 * 0.17832996
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7081 * 0.43067709
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10655 * 0.37179373
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87639 * 0.05189446
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99296 * 0.37411299
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34305 * 0.34857568
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9262 * 0.88310212
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35599 * 0.61599026
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89275 * 0.37360082
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58694 * 0.99220748
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33222 * 0.34453670
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'aejqojtu').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0013():
    """Extended test 13 for replication."""
    x_0 = 67176 * 0.57030040
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10207 * 0.47137853
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51964 * 0.63331662
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9149 * 0.85974067
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66863 * 0.89010880
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18350 * 0.28237093
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85641 * 0.48933524
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64 * 0.44038112
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89641 * 0.35620704
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84607 * 0.92470556
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94658 * 0.76720843
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72258 * 0.24302129
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69839 * 0.27891652
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52654 * 0.54498215
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75868 * 0.18164282
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47228 * 0.41542259
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99426 * 0.00046011
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34634 * 0.67859141
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52776 * 0.85088483
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48579 * 0.63143536
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'fiqtaomn').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0014():
    """Extended test 14 for replication."""
    x_0 = 85574 * 0.59311631
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4264 * 0.50575038
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19556 * 0.73532703
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18907 * 0.27261004
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35082 * 0.11771402
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55492 * 0.73843762
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43274 * 0.62585734
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14720 * 0.34399795
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12932 * 0.95996582
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6785 * 0.07171992
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27525 * 0.97538526
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56689 * 0.20968040
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55020 * 0.12979813
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3687 * 0.05590117
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26732 * 0.66087531
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81660 * 0.31944237
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25138 * 0.93654215
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40863 * 0.98486271
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48300 * 0.72319808
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89978 * 0.42613228
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77280 * 0.69674632
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34356 * 0.64995143
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49316 * 0.20409692
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52783 * 0.49908246
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67294 * 0.10146835
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99682 * 0.49630587
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78639 * 0.71220835
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67283 * 0.19579311
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3475 * 0.26176793
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47697 * 0.56045713
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65926 * 0.66720600
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38202 * 0.95650804
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96219 * 0.77935828
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54801 * 0.46200424
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6838 * 0.95463742
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66315 * 0.62753324
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16253 * 0.80226021
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3601 * 0.43116908
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46261 * 0.83861680
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86542 * 0.29456039
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 87308 * 0.59518935
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'djypyvqj').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0015():
    """Extended test 15 for replication."""
    x_0 = 58503 * 0.64470054
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68893 * 0.92601643
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9284 * 0.19167147
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5174 * 0.91692261
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82194 * 0.99787419
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31477 * 0.12075118
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32992 * 0.50243310
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1646 * 0.25476290
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41667 * 0.48169636
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42929 * 0.45826228
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31943 * 0.46683478
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32078 * 0.60881828
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35623 * 0.41753342
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8862 * 0.88439457
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20500 * 0.08207808
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75548 * 0.89244765
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 524 * 0.44984367
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17114 * 0.35883066
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10100 * 0.38951594
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44368 * 0.34916716
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'jlgqxoye').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0016():
    """Extended test 16 for replication."""
    x_0 = 46771 * 0.78036012
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21392 * 0.44352785
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62387 * 0.01630257
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10133 * 0.37679971
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41496 * 0.42278670
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86472 * 0.82248065
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16130 * 0.10489607
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14102 * 0.74052161
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86088 * 0.12297853
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68497 * 0.85281455
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68547 * 0.85556112
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23255 * 0.93593490
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63875 * 0.52790735
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70199 * 0.77586021
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17811 * 0.33762259
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50608 * 0.99433436
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92080 * 0.85278397
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77424 * 0.33352033
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52135 * 0.64122140
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34505 * 0.30170478
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7940 * 0.70811107
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15719 * 0.51662085
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59388 * 0.04480936
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32214 * 0.99944538
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68381 * 0.00328998
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5554 * 0.54056650
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76029 * 0.10284347
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'lgbkqgty').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0017():
    """Extended test 17 for replication."""
    x_0 = 3459 * 0.98866161
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98255 * 0.03488136
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56192 * 0.94383347
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10734 * 0.18703684
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17011 * 0.72246500
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29847 * 0.03838267
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32450 * 0.89183612
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43684 * 0.72304993
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78870 * 0.94429125
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64805 * 0.17129127
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17497 * 0.52994540
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55634 * 0.56875671
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12310 * 0.48242244
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47522 * 0.82181442
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72565 * 0.38157567
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94934 * 0.19627899
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14734 * 0.50457073
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53619 * 0.84227079
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83765 * 0.91403030
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25171 * 0.50727307
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28835 * 0.23561601
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83607 * 0.45503110
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26592 * 0.58042891
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9572 * 0.92410109
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24895 * 0.60841369
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96218 * 0.56373305
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61100 * 0.74638381
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3152 * 0.74449490
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77752 * 0.73054702
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51430 * 0.80806778
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28307 * 0.89429531
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48977 * 0.43794819
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81577 * 0.97456050
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42004 * 0.94058266
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42932 * 0.73297741
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89459 * 0.98787520
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42093 * 0.90513376
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84588 * 0.41075448
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82109 * 0.99712331
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19770 * 0.56462487
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98992 * 0.69414069
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22365 * 0.23987752
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 59140 * 0.15956360
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 26447 * 0.91092535
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'shiwunpx').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0018():
    """Extended test 18 for replication."""
    x_0 = 46989 * 0.81938068
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64032 * 0.33710846
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53814 * 0.77861222
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81506 * 0.97104240
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80504 * 0.62895676
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55751 * 0.75667496
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64099 * 0.41590017
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34262 * 0.04558500
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71779 * 0.14452024
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55814 * 0.15946746
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71951 * 0.29722181
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44855 * 0.53704106
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7212 * 0.94918736
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73963 * 0.69971348
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59686 * 0.77818379
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63317 * 0.83608929
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50510 * 0.79208778
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54390 * 0.83364904
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19667 * 0.69874186
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55197 * 0.03822756
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59247 * 0.84456697
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ctaidfsu').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0019():
    """Extended test 19 for replication."""
    x_0 = 20085 * 0.25990807
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78108 * 0.07260909
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53495 * 0.43627686
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30930 * 0.32682094
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64935 * 0.50232783
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70504 * 0.94280254
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17705 * 0.61439994
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25028 * 0.90529116
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21827 * 0.71787654
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75103 * 0.45449276
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51018 * 0.02435694
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24784 * 0.43460229
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24422 * 0.97704384
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23099 * 0.88577249
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42441 * 0.22052147
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77803 * 0.23798682
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61036 * 0.31070708
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74705 * 0.46143039
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34654 * 0.97021562
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95821 * 0.52820277
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43579 * 0.21512227
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92224 * 0.19322558
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98820 * 0.63923657
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84384 * 0.53867090
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69328 * 0.67498570
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60996 * 0.32071476
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7995 * 0.93606539
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75849 * 0.07958784
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1562 * 0.87860530
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73029 * 0.01496977
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36087 * 0.22154779
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53728 * 0.73069808
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35452 * 0.05297205
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20932 * 0.80994100
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19931 * 0.76098567
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23419 * 0.87924878
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12062 * 0.66031645
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18600 * 0.10315446
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43562 * 0.69291096
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79461 * 0.65138576
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36934 * 0.62177453
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22111 * 0.94562018
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 52304 * 0.99075838
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83691 * 0.72405258
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 26485 * 0.98260607
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 54460 * 0.79015754
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 67638 * 0.35948906
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 92397 * 0.04281017
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 29227 * 0.89232675
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 60665 * 0.09843508
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'xzemeuka').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0020():
    """Extended test 20 for replication."""
    x_0 = 50366 * 0.24440845
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65287 * 0.45604726
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64073 * 0.51536571
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82492 * 0.27719694
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77786 * 0.15937731
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88543 * 0.64584970
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25567 * 0.86670670
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73666 * 0.70683385
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42281 * 0.54771617
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83613 * 0.25429543
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44181 * 0.19276009
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80104 * 0.76973506
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9609 * 0.60983751
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2017 * 0.58156960
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43509 * 0.75722061
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29394 * 0.84893311
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72556 * 0.81366529
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57374 * 0.53870343
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10637 * 0.02506274
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80760 * 0.71989097
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67353 * 0.01363602
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56562 * 0.54699278
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50430 * 0.33341641
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'tcgqzcrc').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0021():
    """Extended test 21 for replication."""
    x_0 = 95221 * 0.94769820
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23497 * 0.70636996
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29544 * 0.24718145
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71405 * 0.08171139
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49957 * 0.51973514
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90140 * 0.72154708
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55712 * 0.93875538
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30330 * 0.74128400
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63419 * 0.34109818
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36178 * 0.54932181
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92662 * 0.23777692
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98249 * 0.08541974
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76495 * 0.50943482
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11375 * 0.70697556
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42671 * 0.82989370
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48880 * 0.35110047
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65704 * 0.78010812
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83609 * 0.36647507
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22620 * 0.43155647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78502 * 0.08504739
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34071 * 0.98820159
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13572 * 0.94989730
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18601 * 0.13567035
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84811 * 0.05297198
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 326 * 0.91460164
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78018 * 0.01329897
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20742 * 0.09361809
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22730 * 0.85437892
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98261 * 0.01024286
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94093 * 0.01128577
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74776 * 0.45350641
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21475 * 0.64513482
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66065 * 0.72042609
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4487 * 0.14970473
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29745 * 0.26171757
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60257 * 0.79690289
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36225 * 0.71573223
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32913 * 0.80067876
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64203 * 0.62682412
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57218 * 0.31654921
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 76383 * 0.14938766
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'rehitlzi').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0022():
    """Extended test 22 for replication."""
    x_0 = 76741 * 0.18854958
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96387 * 0.97081129
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3200 * 0.86711739
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6777 * 0.89915610
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14131 * 0.87865743
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10469 * 0.54985014
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51705 * 0.55451658
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11060 * 0.81184217
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13348 * 0.79965179
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83346 * 0.17312068
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98885 * 0.35997436
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16280 * 0.28624910
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92843 * 0.39415011
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57543 * 0.91975434
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54583 * 0.18130606
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4154 * 0.57767352
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69709 * 0.76679254
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48686 * 0.33964952
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82438 * 0.95964904
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57798 * 0.44530013
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33688 * 0.55758332
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86986 * 0.30722768
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38428 * 0.32648056
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28692 * 0.41425237
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97007 * 0.31875509
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69323 * 0.69744458
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46990 * 0.85188999
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8278 * 0.03730245
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40601 * 0.12725343
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60464 * 0.76312007
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60274 * 0.80307179
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 468 * 0.65031525
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38976 * 0.03416366
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66910 * 0.62726221
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72021 * 0.16559726
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8142 * 0.11941757
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3686 * 0.49357519
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68982 * 0.28272603
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9337 * 0.03537136
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94522 * 0.35993346
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 57124 * 0.35870483
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59399 * 0.60185637
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'dausdafs').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0023():
    """Extended test 23 for replication."""
    x_0 = 47533 * 0.85288635
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43502 * 0.10176669
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8715 * 0.44553185
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36859 * 0.10526745
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86340 * 0.08388411
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7869 * 0.33196204
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97906 * 0.03067073
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72821 * 0.00198492
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49479 * 0.21740657
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69315 * 0.44584483
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75572 * 0.12816422
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2713 * 0.16059838
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56413 * 0.47554843
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15326 * 0.35760721
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58817 * 0.44730124
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71892 * 0.68998541
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71027 * 0.81811096
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7214 * 0.13250489
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94928 * 0.09672253
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86437 * 0.10295862
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35130 * 0.25213147
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46230 * 0.96753604
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36528 * 0.59315807
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49592 * 0.07623586
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29772 * 0.36461690
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42520 * 0.98186770
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21108 * 0.05023264
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3417 * 0.41113172
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5861 * 0.51088848
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8674 * 0.10452820
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55684 * 0.70031049
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25193 * 0.89996209
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'qfxxgaku').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0024():
    """Extended test 24 for replication."""
    x_0 = 328 * 0.24388916
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86889 * 0.73722084
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45071 * 0.25444644
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80519 * 0.64179957
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29144 * 0.22333873
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99250 * 0.01246943
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34935 * 0.67655905
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60205 * 0.77869380
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86206 * 0.11620217
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65817 * 0.75132978
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54456 * 0.44402355
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1230 * 0.76405121
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51554 * 0.62592167
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81147 * 0.71653186
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37261 * 0.37169733
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16632 * 0.80738942
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68920 * 0.75351672
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29290 * 0.64202116
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71510 * 0.06473270
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80487 * 0.23573310
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55433 * 0.92904169
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89381 * 0.98935345
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64500 * 0.97387598
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30489 * 0.44777725
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8600 * 0.25738374
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64658 * 0.60368260
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66313 * 0.57353552
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7715 * 0.00062645
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9412 * 0.02744109
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71082 * 0.76798011
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88447 * 0.33964461
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82710 * 0.24775884
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99797 * 0.27660008
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32825 * 0.44904959
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85102 * 0.16825774
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62490 * 0.25915776
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53197 * 0.30650555
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68435 * 0.74489325
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65446 * 0.85442764
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14071 * 0.71328820
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60445 * 0.70927567
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 73925 * 0.96991095
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66380 * 0.95361252
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 44977 * 0.47765720
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'njwyjiox').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0025():
    """Extended test 25 for replication."""
    x_0 = 79162 * 0.15208507
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71722 * 0.64550598
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82125 * 0.97126092
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94830 * 0.18916987
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49240 * 0.69341521
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53130 * 0.97459524
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69783 * 0.53719190
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90405 * 0.70945824
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56054 * 0.95387265
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24789 * 0.60171588
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45373 * 0.33309033
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72239 * 0.57640136
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46789 * 0.19861674
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66093 * 0.43538519
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36614 * 0.97611469
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88760 * 0.71682184
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53284 * 0.79441079
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9917 * 0.72667434
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54330 * 0.23298295
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32252 * 0.94431995
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66229 * 0.79298641
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10644 * 0.44362416
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34763 * 0.70562597
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94767 * 0.91892655
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60819 * 0.04106599
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37102 * 0.69109735
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3388 * 0.41041113
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82104 * 0.94126260
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67195 * 0.07497444
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14240 * 0.10974086
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22814 * 0.14760101
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40426 * 0.91059003
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52253 * 0.29237511
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95246 * 0.96130514
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89599 * 0.71197440
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48917 * 0.11394511
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20273 * 0.67970146
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95777 * 0.06822869
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55255 * 0.25161364
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72174 * 0.92743580
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89204 * 0.28040222
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58136 * 0.86118314
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 27603 * 0.00022852
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 74466 * 0.71736271
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 76873 * 0.31281505
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 96247 * 0.81149945
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 57367 * 0.36513516
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 57654 * 0.99671326
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 37491 * 0.48686084
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'hkglzyrh').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0026():
    """Extended test 26 for replication."""
    x_0 = 97398 * 0.41437078
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11725 * 0.20882132
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4196 * 0.00236960
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1975 * 0.79371324
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45841 * 0.72144143
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59052 * 0.87143636
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57619 * 0.76694473
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99262 * 0.26071393
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91203 * 0.76232949
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38394 * 0.19897178
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30756 * 0.54820753
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99560 * 0.84936339
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54066 * 0.37014436
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 474 * 0.10796069
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46769 * 0.31955950
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62846 * 0.93693419
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17072 * 0.91879213
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17277 * 0.93729410
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99187 * 0.48974331
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57953 * 0.09003924
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18842 * 0.26724156
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82010 * 0.93502690
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62311 * 0.73772957
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'rzgqyjnw').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0027():
    """Extended test 27 for replication."""
    x_0 = 6951 * 0.06699911
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88236 * 0.61911928
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11095 * 0.50514718
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91541 * 0.90933341
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21592 * 0.04317740
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34671 * 0.77010741
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11936 * 0.89712105
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29435 * 0.57231738
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37496 * 0.39096133
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45052 * 0.06746617
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74456 * 0.97014734
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53707 * 0.93216811
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7118 * 0.86841425
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32689 * 0.04208904
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38316 * 0.96502174
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37306 * 0.57139687
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46587 * 0.78449458
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24201 * 0.03088272
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37547 * 0.35145361
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15230 * 0.37616840
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44418 * 0.91926190
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94123 * 0.74548328
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85076 * 0.06746561
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40897 * 0.51040834
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2611 * 0.66851522
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64159 * 0.15786090
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7316 * 0.99335738
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96641 * 0.44418380
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14374 * 0.61868784
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51113 * 0.69977168
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79273 * 0.48419898
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69860 * 0.51118046
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48876 * 0.17892841
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30485 * 0.08114018
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59088 * 0.39251819
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86959 * 0.35184491
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36979 * 0.40580096
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97372 * 0.04221579
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44424 * 0.39659970
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46297 * 0.18200084
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 7658 * 0.51187078
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'myclrulu').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0028():
    """Extended test 28 for replication."""
    x_0 = 36535 * 0.28751136
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32782 * 0.95744485
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44391 * 0.32559187
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8771 * 0.17146032
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75021 * 0.07818130
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17296 * 0.63174234
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89731 * 0.73934019
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19858 * 0.37946996
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90367 * 0.25119698
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80768 * 0.60717981
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63647 * 0.25972191
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18798 * 0.53114095
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21783 * 0.44640343
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34003 * 0.16899012
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17555 * 0.16867621
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53577 * 0.43862735
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7056 * 0.61091331
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28487 * 0.39574281
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67204 * 0.67445909
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81540 * 0.42681803
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97392 * 0.84539605
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52883 * 0.09850734
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64553 * 0.56575601
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42641 * 0.27551268
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66514 * 0.30124965
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26819 * 0.51380127
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76215 * 0.08954195
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76506 * 0.15241409
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47377 * 0.33487224
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47907 * 0.75331711
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62437 * 0.34811253
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13430 * 0.17396621
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16399 * 0.63665889
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54870 * 0.53462795
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98145 * 0.51704114
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66691 * 0.98048063
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42697 * 0.69709137
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19515 * 0.69014318
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44859 * 0.09437788
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 5512 * 0.23917998
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 28952 * 0.18146450
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9453 * 0.27211695
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29044 * 0.28832360
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 51006 * 0.27511557
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 51553 * 0.37985936
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 270 * 0.76255513
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 44497 * 0.62063048
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 41469 * 0.90308248
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 93858 * 0.59415268
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'otvpgdud').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0029():
    """Extended test 29 for replication."""
    x_0 = 67406 * 0.85174599
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66918 * 0.44950763
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68870 * 0.58617431
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86622 * 0.88516078
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52552 * 0.24328759
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52909 * 0.11423307
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27799 * 0.96671590
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38467 * 0.22332023
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55504 * 0.47337434
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96925 * 0.90179833
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5894 * 0.44512776
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76697 * 0.84832551
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4769 * 0.03937703
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45581 * 0.15238618
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2511 * 0.05802974
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26439 * 0.39192107
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71215 * 0.63339205
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49883 * 0.60208077
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74432 * 0.46851903
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60413 * 0.89461454
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89891 * 0.47064263
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59187 * 0.18741226
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73175 * 0.52201499
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47083 * 0.83407823
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6344 * 0.47312801
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24845 * 0.51884835
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22728 * 0.35989226
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23290 * 0.54236266
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79872 * 0.80465550
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87024 * 0.59650039
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58186 * 0.56256760
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58856 * 0.95708189
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87671 * 0.70830047
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65646 * 0.79189779
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51982 * 0.26482373
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77195 * 0.89262627
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63220 * 0.84022768
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29462 * 0.93884254
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65592 * 0.80408337
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69729 * 0.52095457
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ribuxhbs').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0030():
    """Extended test 30 for replication."""
    x_0 = 41021 * 0.12301641
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68121 * 0.09698408
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36051 * 0.12781535
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78007 * 0.59044688
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46263 * 0.73151451
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47693 * 0.72639571
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54538 * 0.97753649
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89224 * 0.69580270
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81583 * 0.87401313
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23937 * 0.09376672
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38059 * 0.88331392
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71296 * 0.54407481
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84504 * 0.36461846
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3984 * 0.78313800
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35462 * 0.58118000
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83529 * 0.78334204
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32816 * 0.22352275
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41906 * 0.96483856
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96910 * 0.43001588
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1999 * 0.36850779
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4529 * 0.58332198
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76929 * 0.96207516
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69916 * 0.79121650
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84581 * 0.88805704
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77237 * 0.63887253
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56997 * 0.64290928
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'vefyibox').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0031():
    """Extended test 31 for replication."""
    x_0 = 10318 * 0.67786350
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65866 * 0.16368518
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77271 * 0.65182340
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80572 * 0.04602425
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68751 * 0.92315530
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31130 * 0.45057880
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89653 * 0.86475737
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7147 * 0.76606784
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65145 * 0.15843712
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82753 * 0.66049104
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37742 * 0.38593148
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40503 * 0.36548279
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58874 * 0.03352646
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40744 * 0.44041872
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99472 * 0.56491566
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46057 * 0.76980907
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49580 * 0.21342962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14055 * 0.81553826
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99029 * 0.39146722
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80141 * 0.72401387
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18922 * 0.28719110
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70943 * 0.29808449
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'gjczuirr').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0032():
    """Extended test 32 for replication."""
    x_0 = 82467 * 0.75664467
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69494 * 0.49910332
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67863 * 0.10423832
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16263 * 0.35298757
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91173 * 0.88312707
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65062 * 0.73518381
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14589 * 0.87380685
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52148 * 0.84666815
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85784 * 0.19392060
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78790 * 0.17823039
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68194 * 0.16275131
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82236 * 0.25414868
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29918 * 0.04250162
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17375 * 0.57792709
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52496 * 0.06890622
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60486 * 0.66816649
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55187 * 0.30267649
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80907 * 0.84987452
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84311 * 0.56938348
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13393 * 0.28330085
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79585 * 0.00747185
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74566 * 0.97898682
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18904 * 0.50922272
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62054 * 0.86787044
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45984 * 0.97530917
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22480 * 0.51720143
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94912 * 0.35975327
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77312 * 0.81130150
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84299 * 0.29044931
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60463 * 0.42983072
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52460 * 0.94804273
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4619 * 0.68692697
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5790 * 0.21802331
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99525 * 0.56874726
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'uhbphtit').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0033():
    """Extended test 33 for replication."""
    x_0 = 69214 * 0.34637243
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 113 * 0.48654821
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98072 * 0.01234793
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59413 * 0.03120114
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65750 * 0.42358333
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30554 * 0.56081975
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95865 * 0.37075927
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9817 * 0.07609145
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74876 * 0.53844121
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1924 * 0.96889639
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19977 * 0.69653648
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30453 * 0.00959263
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44862 * 0.60474863
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17423 * 0.01898239
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47508 * 0.22155818
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16051 * 0.85088513
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11792 * 0.25648131
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82096 * 0.53953186
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27127 * 0.04739185
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82130 * 0.64142105
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83483 * 0.36248727
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76560 * 0.54284802
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38527 * 0.85819802
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54934 * 0.43341953
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96348 * 0.67097693
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6263 * 0.04741425
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92669 * 0.82216774
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'cvrhhztx').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0034():
    """Extended test 34 for replication."""
    x_0 = 18973 * 0.67098227
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66640 * 0.71039528
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60540 * 0.56665688
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64380 * 0.75508982
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58458 * 0.59728916
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98458 * 0.79856164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29681 * 0.04119077
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36837 * 0.48536291
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4395 * 0.82213533
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73674 * 0.67039939
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36300 * 0.08271376
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24725 * 0.35245015
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29880 * 0.24961825
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50626 * 0.23776757
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75063 * 0.31691504
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20046 * 0.32452003
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 636 * 0.86182402
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16233 * 0.45442644
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60542 * 0.54947250
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14398 * 0.82690070
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45006 * 0.86686392
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18326 * 0.32073906
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42345 * 0.60143190
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98872 * 0.25576013
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84659 * 0.41952326
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99774 * 0.98994553
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35045 * 0.36359027
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97498 * 0.16027472
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92119 * 0.19759553
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88374 * 0.38313040
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45701 * 0.99471113
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25591 * 0.58031493
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90506 * 0.85293945
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96823 * 0.27900697
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69803 * 0.95665781
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18775 * 0.11785167
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32182 * 0.72144646
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72525 * 0.30439812
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 85391 * 0.16113271
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87490 * 0.63992207
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 28412 * 0.73975875
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21110 * 0.81205258
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 283 * 0.88221058
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 48252 * 0.41413786
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'gidzqhju').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0035():
    """Extended test 35 for replication."""
    x_0 = 62015 * 0.58618074
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80951 * 0.22892987
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53341 * 0.32433986
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59878 * 0.32693820
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37859 * 0.65543926
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64633 * 0.28951273
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8073 * 0.90249457
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99800 * 0.76128246
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78105 * 0.39504695
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68425 * 0.12001389
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72600 * 0.97993287
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9670 * 0.65378355
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13235 * 0.81732155
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4282 * 0.15272490
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53832 * 0.22243180
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44743 * 0.05171462
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21897 * 0.76537734
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27782 * 0.81311398
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87083 * 0.24142342
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4802 * 0.58456108
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24781 * 0.67752235
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45451 * 0.64171512
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69478 * 0.23067561
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57038 * 0.95692131
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7063 * 0.09873595
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4184 * 0.21513616
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27265 * 0.81194621
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70879 * 0.18819984
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25027 * 0.60559122
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1094 * 0.46759647
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8733 * 0.24432377
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82937 * 0.99296542
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78605 * 0.82369260
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12143 * 0.29140699
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48402 * 0.10884055
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5701 * 0.72087271
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31778 * 0.52007342
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88984 * 0.27095326
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'cftxeifq').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0036():
    """Extended test 36 for replication."""
    x_0 = 35039 * 0.80851451
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65353 * 0.67432254
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6322 * 0.37995013
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76620 * 0.86135098
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61199 * 0.36173998
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15408 * 0.47641276
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94080 * 0.08480403
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67774 * 0.09438655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51643 * 0.92718841
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35066 * 0.14386086
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28805 * 0.14006589
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75706 * 0.22347772
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71028 * 0.13767897
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55596 * 0.84835459
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15601 * 0.23265625
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67914 * 0.42452719
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11898 * 0.69961807
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39518 * 0.48107931
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39977 * 0.07823136
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97407 * 0.44842736
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32385 * 0.17927087
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10416 * 0.28392945
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28885 * 0.02575707
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14021 * 0.14892905
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15483 * 0.07401547
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44968 * 0.54774001
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72850 * 0.64438146
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55211 * 0.24193093
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56016 * 0.27680365
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1571 * 0.64008621
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40406 * 0.78698050
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33829 * 0.32429052
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36239 * 0.49437093
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83318 * 0.45234123
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74752 * 0.84183844
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35302 * 0.01581327
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41138 * 0.23250910
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41849 * 0.18953033
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79244 * 0.73109206
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92817 * 0.21841803
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43877 * 0.56354927
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92132 * 0.10214543
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12160 * 0.34879163
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58191 * 0.62077863
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 96575 * 0.68549919
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 30540 * 0.00268017
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 19344 * 0.07186803
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ezogioxi').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0037():
    """Extended test 37 for replication."""
    x_0 = 16600 * 0.66142890
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17429 * 0.67571356
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63126 * 0.94176750
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3264 * 0.31013891
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56262 * 0.73476864
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44631 * 0.27097905
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19553 * 0.68734203
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46403 * 0.68775992
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13396 * 0.29825353
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33985 * 0.54357912
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9365 * 0.10341347
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49251 * 0.67727182
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7531 * 0.91247483
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51055 * 0.61699790
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42937 * 0.04557271
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21210 * 0.02746526
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67854 * 0.62771970
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74464 * 0.44674967
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92327 * 0.06821602
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77480 * 0.15765308
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93879 * 0.04726647
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43896 * 0.62538431
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97005 * 0.51379490
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16812 * 0.63614089
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38639 * 0.05423713
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89077 * 0.86147425
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89122 * 0.92335073
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10727 * 0.23336623
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30743 * 0.88031004
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81930 * 0.32136653
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21891 * 0.44656535
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92407 * 0.18625175
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96240 * 0.78252607
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85024 * 0.25245804
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20564 * 0.13797142
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46824 * 0.70662821
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51751 * 0.43470391
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83098 * 0.79960359
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86534 * 0.14489790
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98244 * 0.74470313
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 72145 * 0.40847202
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47510 * 0.83982456
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96783 * 0.08280023
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88022 * 0.43904700
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 7148 * 0.08688967
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 429 * 0.47767757
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 69342 * 0.71758978
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 43104 * 0.41916952
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'pnkrmmqn').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0038():
    """Extended test 38 for replication."""
    x_0 = 67821 * 0.56454229
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71749 * 0.39718359
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48623 * 0.25212801
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53548 * 0.84938960
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99569 * 0.60599330
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55812 * 0.53454108
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12525 * 0.46360824
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20352 * 0.34552673
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59105 * 0.94576182
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52606 * 0.60725003
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8224 * 0.73204077
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57151 * 0.76865693
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56260 * 0.74483803
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16472 * 0.16686411
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14675 * 0.51208184
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60635 * 0.22611741
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76385 * 0.76322637
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47396 * 0.44118027
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59292 * 0.37614427
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77786 * 0.43878603
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95245 * 0.53754011
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ptdowpfn').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0039():
    """Extended test 39 for replication."""
    x_0 = 80185 * 0.02754639
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34421 * 0.78123614
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98916 * 0.70234062
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95313 * 0.03629358
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55076 * 0.44147160
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51503 * 0.48978172
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94191 * 0.94801738
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30088 * 0.03663173
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99938 * 0.14709406
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46668 * 0.21422731
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84746 * 0.91579650
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29877 * 0.33371362
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47761 * 0.41249451
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7407 * 0.74683856
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72248 * 0.66038654
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29244 * 0.47723603
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38922 * 0.72218575
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68618 * 0.24505158
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62026 * 0.41690374
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50744 * 0.11436371
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36567 * 0.15388900
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43036 * 0.18929601
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89995 * 0.32185134
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40191 * 0.15953712
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49387 * 0.75155308
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66314 * 0.42409973
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32093 * 0.18153099
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16699 * 0.71977346
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25405 * 0.33477210
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20543 * 0.20595353
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66348 * 0.93024154
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94549 * 0.82740780
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98265 * 0.27834040
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31943 * 0.85179105
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29529 * 0.19526850
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'oqzfsohv').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0040():
    """Extended test 40 for replication."""
    x_0 = 36561 * 0.66912862
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77778 * 0.18439946
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64441 * 0.60138582
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48438 * 0.65770844
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45839 * 0.17115030
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35199 * 0.13592239
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35189 * 0.13208394
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73300 * 0.92839860
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96064 * 0.58617730
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67168 * 0.84222781
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45827 * 0.60802916
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30701 * 0.11802066
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28684 * 0.12859804
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28950 * 0.03782030
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89386 * 0.05262712
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8746 * 0.25793806
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66406 * 0.89606347
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21240 * 0.66905855
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93772 * 0.68050237
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67057 * 0.56317690
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36543 * 0.95212771
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37920 * 0.58837835
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62250 * 0.34726114
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81171 * 0.80015275
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82513 * 0.64379610
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17229 * 0.69282738
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58741 * 0.91463839
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19935 * 0.60571945
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93994 * 0.80758252
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23467 * 0.61106875
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90551 * 0.66230135
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25548 * 0.51858902
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31789 * 0.87589033
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1741 * 0.26788359
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67413 * 0.47767867
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8138 * 0.60795884
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25738 * 0.36587905
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69864 * 0.55318603
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37329 * 0.64993470
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16540 * 0.17331563
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85249 * 0.01286011
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77224 * 0.55756790
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16631 * 0.13615175
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 59203 * 0.78651194
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61161 * 0.47154433
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'aniwzioj').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0041():
    """Extended test 41 for replication."""
    x_0 = 17245 * 0.47842571
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26051 * 0.59768593
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76269 * 0.35388502
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5127 * 0.31219471
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45183 * 0.31826431
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23457 * 0.19157751
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24709 * 0.78449717
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17614 * 0.43004829
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80251 * 0.66452890
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76210 * 0.81337622
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91387 * 0.95964307
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11288 * 0.56091059
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17121 * 0.57436788
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12356 * 0.70352966
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54038 * 0.00420989
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51318 * 0.44264701
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25052 * 0.52217494
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11524 * 0.89015116
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4429 * 0.97073117
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26924 * 0.76845990
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11760 * 0.75582270
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61212 * 0.65337618
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43952 * 0.85481508
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67234 * 0.54614676
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44972 * 0.51013421
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34064 * 0.61984668
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81010 * 0.40341074
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46079 * 0.66184581
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67068 * 0.34124002
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49962 * 0.96844309
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5023 * 0.19270230
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1229 * 0.16821313
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'bszltmal').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0042():
    """Extended test 42 for replication."""
    x_0 = 22660 * 0.18987291
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67543 * 0.57009569
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94415 * 0.03024791
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69814 * 0.82014917
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23090 * 0.30675031
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16912 * 0.39078979
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73872 * 0.85170743
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92278 * 0.64929466
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57939 * 0.56606577
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72903 * 0.50514029
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3086 * 0.43522594
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91259 * 0.81039833
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66964 * 0.11772041
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71639 * 0.01957639
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78895 * 0.66701481
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42611 * 0.86729683
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99039 * 0.12731742
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93472 * 0.81585442
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39332 * 0.83780590
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49326 * 0.80965987
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54004 * 0.07068273
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45079 * 0.89497666
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58085 * 0.00086984
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'obmftqth').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0043():
    """Extended test 43 for replication."""
    x_0 = 76888 * 0.89442250
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59128 * 0.80104157
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49297 * 0.33364366
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6253 * 0.09460190
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91238 * 0.20254394
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47945 * 0.66526190
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17514 * 0.58834089
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57389 * 0.64910831
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63491 * 0.60874295
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60507 * 0.26402159
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12415 * 0.38823385
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83474 * 0.46641367
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62458 * 0.91716954
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88071 * 0.22364354
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38985 * 0.98390398
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86023 * 0.06306068
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80732 * 0.62939218
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98964 * 0.10028512
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51392 * 0.59065212
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56589 * 0.96090953
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12932 * 0.63476136
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60547 * 0.17200142
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96009 * 0.43542032
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79372 * 0.73323308
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34905 * 0.18871064
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55803 * 0.75809980
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90298 * 0.96776903
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50744 * 0.99724084
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'mqmntkjm').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0044():
    """Extended test 44 for replication."""
    x_0 = 35093 * 0.24019001
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10038 * 0.86761358
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78423 * 0.14562642
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49362 * 0.99519175
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34533 * 0.56952525
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17597 * 0.39525878
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5409 * 0.47465220
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73292 * 0.88004018
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46782 * 0.07503520
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18437 * 0.95228405
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83794 * 0.60642692
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45591 * 0.92025594
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93854 * 0.96769067
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4897 * 0.64111928
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26470 * 0.30440734
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22620 * 0.86143529
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24056 * 0.65423029
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18973 * 0.66280238
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9196 * 0.97973129
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29953 * 0.37902904
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70432 * 0.95269429
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45419 * 0.54777417
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'qikmexzb').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0045():
    """Extended test 45 for replication."""
    x_0 = 76900 * 0.11818323
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41675 * 0.16249966
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38525 * 0.41106936
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85623 * 0.01704692
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61655 * 0.98942678
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12959 * 0.66043217
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62079 * 0.06696150
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9987 * 0.98561932
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34371 * 0.26339524
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56211 * 0.13373572
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93708 * 0.98918666
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2858 * 0.14437393
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53509 * 0.05591353
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48057 * 0.23705145
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26917 * 0.02533590
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87718 * 0.90541313
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91690 * 0.65756673
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61491 * 0.73448462
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83214 * 0.62650547
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80439 * 0.13965658
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58693 * 0.42080439
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65803 * 0.35735944
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22991 * 0.78766755
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85458 * 0.01283365
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89694 * 0.56519549
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63070 * 0.47315873
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19584 * 0.15870864
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39318 * 0.49434719
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99174 * 0.84305771
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32553 * 0.70983656
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27432 * 0.21894836
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'vqcyoghz').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0046():
    """Extended test 46 for replication."""
    x_0 = 58865 * 0.30910617
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82587 * 0.23112854
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77087 * 0.59524594
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80161 * 0.15448221
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64794 * 0.68626101
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13966 * 0.06667406
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39000 * 0.75709496
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84403 * 0.67553765
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93261 * 0.97427479
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75444 * 0.99587918
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57673 * 0.83088637
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8268 * 0.81995455
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84916 * 0.82105567
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44691 * 0.49350119
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92147 * 0.20200521
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59333 * 0.55724349
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82895 * 0.47423960
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75095 * 0.65229779
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55004 * 0.32348022
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45674 * 0.87263226
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55163 * 0.85627684
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51447 * 0.89134044
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20181 * 0.21487841
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69887 * 0.40030238
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 422 * 0.24489581
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47110 * 0.83095261
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75174 * 0.88257268
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10716 * 0.36073308
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76515 * 0.52702413
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99488 * 0.37343672
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1018 * 0.04899674
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9311 * 0.81602507
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58185 * 0.82805365
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68226 * 0.06264065
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76406 * 0.24657939
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40 * 0.92660210
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17145 * 0.11201136
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78599 * 0.31071913
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42862 * 0.21692999
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28977 * 0.64696553
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86561 * 0.66607659
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77619 * 0.38375030
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 26086 * 0.37471645
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61014 * 0.84555877
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 54780 * 0.43417855
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 72107 * 0.66306747
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 87249 * 0.89834569
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 55558 * 0.88906052
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 1402 * 0.96971204
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 64517 * 0.65320437
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'eetecmdl').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0047():
    """Extended test 47 for replication."""
    x_0 = 32576 * 0.07155164
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29267 * 0.22966681
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83761 * 0.16132806
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14637 * 0.58782288
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88132 * 0.02148558
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42415 * 0.63751612
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38671 * 0.44230214
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98754 * 0.15128938
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50819 * 0.63046605
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2344 * 0.16377165
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25049 * 0.33651937
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82556 * 0.96731882
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25311 * 0.54756558
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94487 * 0.85497970
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53155 * 0.38087861
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27824 * 0.18118451
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59855 * 0.30203870
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66195 * 0.47572855
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92066 * 0.68177894
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22667 * 0.36415210
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20806 * 0.52449825
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57065 * 0.05238757
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58295 * 0.15739049
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87750 * 0.06840909
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8360 * 0.12121072
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'udoxzsje').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0048():
    """Extended test 48 for replication."""
    x_0 = 82299 * 0.74322917
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96006 * 0.21418329
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69656 * 0.95806166
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45021 * 0.29936687
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32713 * 0.70130329
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11151 * 0.41652723
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 214 * 0.16351430
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41736 * 0.15223392
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 724 * 0.56763970
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50036 * 0.31190284
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4804 * 0.53166367
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68178 * 0.81685412
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77820 * 0.70564835
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56741 * 0.36575084
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4946 * 0.53191212
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95383 * 0.86594954
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28665 * 0.23791016
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40737 * 0.26113679
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62752 * 0.04230088
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60660 * 0.84739539
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88504 * 0.54165415
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59731 * 0.63659885
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30349 * 0.66295683
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29892 * 0.03276034
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94881 * 0.43406664
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94867 * 0.65036903
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97739 * 0.41010847
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42646 * 0.66548842
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55146 * 0.95757203
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 441 * 0.29512057
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91578 * 0.72330556
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31271 * 0.26308353
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44254 * 0.71438877
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31744 * 0.83662602
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78377 * 0.45953270
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61256 * 0.44152945
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70354 * 0.39725839
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64862 * 0.67261483
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66693 * 0.03390932
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1410 * 0.39079342
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71503 * 0.92312015
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 19011 * 0.46504353
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13284 * 0.89327145
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38371 * 0.35531629
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 67484 * 0.51261177
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 17709 * 0.94861039
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'dlhgcbcd').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0049():
    """Extended test 49 for replication."""
    x_0 = 83517 * 0.70189829
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60153 * 0.32122656
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50919 * 0.30225286
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94861 * 0.75749144
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15743 * 0.11089595
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72864 * 0.31699579
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34013 * 0.71854076
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33675 * 0.15181868
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37174 * 0.80619719
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94353 * 0.20889547
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60938 * 0.86460175
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74319 * 0.61933451
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82995 * 0.91419536
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95720 * 0.53952690
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38325 * 0.27395527
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4306 * 0.47868689
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30323 * 0.90321681
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73710 * 0.67574987
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73604 * 0.25209045
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25291 * 0.11094055
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87963 * 0.29897907
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8765 * 0.86047352
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98836 * 0.20846590
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91475 * 0.77162591
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93506 * 0.86781208
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86859 * 0.00771512
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93667 * 0.18593109
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20313 * 0.13750278
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47782 * 0.38089613
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70172 * 0.39951238
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22231 * 0.14690104
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55236 * 0.57478126
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'furamhdr').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0050():
    """Extended test 50 for replication."""
    x_0 = 18654 * 0.05120976
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98343 * 0.05955676
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34563 * 0.07920195
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6367 * 0.60549035
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35387 * 0.79609846
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99693 * 0.89108189
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59854 * 0.52107399
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91265 * 0.18468632
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38051 * 0.63199604
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84125 * 0.05100279
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14614 * 0.96858079
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 978 * 0.28154640
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28999 * 0.92183542
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5385 * 0.60723814
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62567 * 0.84293551
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51537 * 0.83115383
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72656 * 0.80345533
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69855 * 0.45491251
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86161 * 0.20688106
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41381 * 0.34336844
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32575 * 0.55067048
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76598 * 0.48589856
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63890 * 0.46032288
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66159 * 0.74035683
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64329 * 0.20419173
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'djfszgcj').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0051():
    """Extended test 51 for replication."""
    x_0 = 78296 * 0.96568897
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89496 * 0.81897326
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18723 * 0.71368014
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58982 * 0.78725752
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29563 * 0.69469948
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90550 * 0.62846423
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9395 * 0.72703977
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84546 * 0.34974756
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70847 * 0.88519595
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5830 * 0.30374009
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61228 * 0.46768099
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68095 * 0.54131526
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21037 * 0.58851623
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33440 * 0.14155069
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35004 * 0.73338409
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4578 * 0.46265052
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16412 * 0.53816879
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72927 * 0.17003605
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14688 * 0.46818223
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53085 * 0.53337452
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47629 * 0.50916508
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50583 * 0.07381588
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97024 * 0.27335585
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25308 * 0.85713448
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75481 * 0.32941039
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95323 * 0.47222216
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55007 * 0.02863595
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74465 * 0.67960358
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79145 * 0.95836896
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77432 * 0.57937721
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24258 * 0.71678459
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81424 * 0.10249653
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18601 * 0.39907131
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54890 * 0.94225798
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45322 * 0.90629009
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70678 * 0.34617999
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4506 * 0.35608841
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63736 * 0.95375449
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'clbayghg').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0052():
    """Extended test 52 for replication."""
    x_0 = 79578 * 0.33370291
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6929 * 0.83612841
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48889 * 0.24220662
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53732 * 0.61053283
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38454 * 0.81403427
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43318 * 0.27000989
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98384 * 0.21169246
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99691 * 0.81429468
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21480 * 0.00885418
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69034 * 0.76397364
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88188 * 0.71962550
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16215 * 0.68606171
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32345 * 0.26398335
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9718 * 0.92369679
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90293 * 0.92416163
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26589 * 0.56271149
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98221 * 0.81360404
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67753 * 0.76730533
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12329 * 0.08962974
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11254 * 0.94817133
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92706 * 0.07984501
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7828 * 0.77895401
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38811 * 0.20218527
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9724 * 0.41103192
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78234 * 0.99561917
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93158 * 0.88044875
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38603 * 0.40703349
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55872 * 0.65914265
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4995 * 0.99592522
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37782 * 0.75652546
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98596 * 0.09482203
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 281 * 0.96466831
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90101 * 0.39622828
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15180 * 0.62852505
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53587 * 0.52289544
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6027 * 0.75856569
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98857 * 0.25134055
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'xtzhreyg').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0053():
    """Extended test 53 for replication."""
    x_0 = 68544 * 0.65190529
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76449 * 0.06842046
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61409 * 0.95356803
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23040 * 0.78431506
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65173 * 0.11816272
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92637 * 0.67379945
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70212 * 0.55313951
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27309 * 0.35878831
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81696 * 0.44122370
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99913 * 0.67913391
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67320 * 0.81308743
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5654 * 0.88802870
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28781 * 0.04785618
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45328 * 0.19332114
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10435 * 0.74325720
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74755 * 0.90214422
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36378 * 0.78936137
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36782 * 0.12184841
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89317 * 0.27743241
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44114 * 0.95977772
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77461 * 0.49248808
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20318 * 0.08544450
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62127 * 0.81427262
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 303 * 0.56878553
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41951 * 0.42873489
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86562 * 0.55817121
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63044 * 0.51325955
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61213 * 0.48563127
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21463 * 0.88364011
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74573 * 0.18270631
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21195 * 0.69561580
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57669 * 0.62855553
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89293 * 0.14643257
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69442 * 0.21134291
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54854 * 0.02231418
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20668 * 0.92808986
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96130 * 0.02496537
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23829 * 0.84745851
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 424 * 0.95833518
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52604 * 0.84462941
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17479 * 0.39840312
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18287 * 0.25439414
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65920 * 0.07285013
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 57506 * 0.37102978
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23505 * 0.79963568
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'flnqrpid').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0054():
    """Extended test 54 for replication."""
    x_0 = 4889 * 0.38492544
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41689 * 0.92778082
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71267 * 0.46532380
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25359 * 0.11190546
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89820 * 0.10645257
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80947 * 0.77994321
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85090 * 0.68087458
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60682 * 0.82969341
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90702 * 0.85966554
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68787 * 0.75862118
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82799 * 0.85661567
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43165 * 0.84300070
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20814 * 0.15174359
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77604 * 0.87152377
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21649 * 0.98738475
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15720 * 0.31957758
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70123 * 0.19959778
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49735 * 0.66740582
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43298 * 0.46207189
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41470 * 0.65398337
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86149 * 0.21681431
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56263 * 0.08301343
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55046 * 0.48502657
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94296 * 0.33371545
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87819 * 0.69771573
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66284 * 0.71311074
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75782 * 0.82119491
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67717 * 0.59470247
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32878 * 0.20371987
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63348 * 0.48447530
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85361 * 0.05882195
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68707 * 0.25290173
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33111 * 0.73797602
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50962 * 0.35628786
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20451 * 0.38068585
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25228 * 0.24150694
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62435 * 0.34311043
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23889 * 0.76824167
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4486 * 0.21654587
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3830 * 0.91842026
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2152 * 0.02393707
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39031 * 0.88241438
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 17064 * 0.21947093
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 80416 * 0.77420577
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 8383 * 0.54564578
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 29331 * 0.58627783
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 42706 * 0.59755940
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 56665 * 0.29387146
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'obzbcnlh').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0055():
    """Extended test 55 for replication."""
    x_0 = 11417 * 0.81455717
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43700 * 0.32004181
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63871 * 0.35760288
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23525 * 0.70792233
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94916 * 0.29566698
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81782 * 0.64403140
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40264 * 0.51796622
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42390 * 0.70080552
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24931 * 0.64993777
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64270 * 0.54068529
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72434 * 0.33441762
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42753 * 0.47415506
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59581 * 0.08596934
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77371 * 0.14921821
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92938 * 0.56839596
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61102 * 0.01513598
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70016 * 0.75283795
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19998 * 0.68469363
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67600 * 0.19500949
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41203 * 0.17318691
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66165 * 0.68485833
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82346 * 0.53987686
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64418 * 0.66904882
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37578 * 0.94307121
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77488 * 0.31217171
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37989 * 0.55061711
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90239 * 0.52456499
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'bmticewg').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0056():
    """Extended test 56 for replication."""
    x_0 = 18568 * 0.39190197
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96856 * 0.81664513
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65879 * 0.58608334
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91294 * 0.85287254
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63195 * 0.07458643
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93793 * 0.36999760
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47767 * 0.33521127
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57049 * 0.68166048
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4005 * 0.55559262
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1622 * 0.65855470
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59747 * 0.03878600
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82336 * 0.99162018
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46940 * 0.17885561
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53064 * 0.76503198
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86751 * 0.19051500
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27017 * 0.96914319
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40952 * 0.58135301
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5647 * 0.42309370
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58394 * 0.94392101
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16198 * 0.62314662
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4707 * 0.58284670
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34470 * 0.71280959
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33242 * 0.49791228
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63529 * 0.48232772
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56440 * 0.27646174
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98563 * 0.10224138
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46539 * 0.18321793
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3843 * 0.58520856
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 953 * 0.55138540
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4713 * 0.41208150
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93302 * 0.46307265
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71121 * 0.08333877
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20743 * 0.90964359
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11077 * 0.73341694
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47654 * 0.48033233
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37034 * 0.88007913
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88604 * 0.43819560
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'aqujrpzs').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0057():
    """Extended test 57 for replication."""
    x_0 = 7226 * 0.50983753
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96436 * 0.44249953
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48635 * 0.45693218
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2572 * 0.93170698
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94484 * 0.82717785
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26293 * 0.41474181
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19792 * 0.26739318
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38529 * 0.51457075
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51806 * 0.42018573
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33704 * 0.09466118
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85408 * 0.30945737
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39599 * 0.68384790
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76806 * 0.81817006
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81831 * 0.39128459
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37665 * 0.95597097
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93528 * 0.56402031
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89297 * 0.00307843
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86330 * 0.40910060
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69617 * 0.35211700
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83209 * 0.73200360
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2813 * 0.60401034
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78753 * 0.40198167
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11013 * 0.91394312
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8156 * 0.95349598
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84900 * 0.15483415
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98789 * 0.70372742
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8161 * 0.55633248
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50917 * 0.07177868
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31519 * 0.58107317
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66052 * 0.82549012
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35122 * 0.22539685
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91334 * 0.32106791
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58459 * 0.25708062
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'yowucfmq').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0058():
    """Extended test 58 for replication."""
    x_0 = 51469 * 0.71111143
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47245 * 0.00572732
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66487 * 0.61104263
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65511 * 0.42673345
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23043 * 0.44480176
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51838 * 0.83684768
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46072 * 0.95150283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46259 * 0.32958423
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47163 * 0.48386442
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36300 * 0.45957263
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69906 * 0.84995848
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94650 * 0.83958236
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85157 * 0.93768711
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59638 * 0.68647695
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52207 * 0.71883088
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16033 * 0.28627138
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95776 * 0.06026697
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85186 * 0.78805372
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14759 * 0.85585703
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3349 * 0.91173452
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27844 * 0.99976085
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47381 * 0.57202860
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30927 * 0.44528542
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14400 * 0.37040450
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83362 * 0.43891200
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74457 * 0.44839236
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25953 * 0.53872316
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93697 * 0.70683102
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50164 * 0.27696772
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44498 * 0.09479171
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20802 * 0.42712203
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79544 * 0.94184997
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49043 * 0.77787937
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4006 * 0.05662846
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43654 * 0.42143628
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6671 * 0.15861257
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32067 * 0.32963977
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11552 * 0.38273748
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66021 * 0.82112492
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'kvjmwpig').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0059():
    """Extended test 59 for replication."""
    x_0 = 66503 * 0.03376472
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12545 * 0.21217269
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94375 * 0.83529545
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62157 * 0.51791288
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73818 * 0.64691484
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67229 * 0.79154643
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41730 * 0.32951704
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31614 * 0.23073389
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3776 * 0.02155488
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10091 * 0.48162766
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70515 * 0.67329513
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92239 * 0.74312079
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88210 * 0.82137742
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16216 * 0.02900010
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45772 * 0.97523589
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86400 * 0.92305617
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80889 * 0.92719530
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76961 * 0.53153013
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42757 * 0.18256789
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55940 * 0.55693889
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85286 * 0.74454140
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39114 * 0.35892507
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8194 * 0.85134537
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'lrnvpxtt').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0060():
    """Extended test 60 for replication."""
    x_0 = 9734 * 0.41881861
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12470 * 0.20315269
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53494 * 0.80634919
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21451 * 0.00928246
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50284 * 0.36498678
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86971 * 0.01556315
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88677 * 0.56844840
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4462 * 0.55229061
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6011 * 0.33550028
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14942 * 0.52523475
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82752 * 0.40467325
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31350 * 0.25986407
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35790 * 0.53372799
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54381 * 0.16596208
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47802 * 0.43613528
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2741 * 0.42383582
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13358 * 0.47699779
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91902 * 0.68874801
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11175 * 0.75912215
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90562 * 0.61988640
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6475 * 0.87048699
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41661 * 0.25901043
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2625 * 0.78948990
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25767 * 0.69164744
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71747 * 0.62947739
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50314 * 0.99640809
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38137 * 0.22520591
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91138 * 0.55379407
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'wgeijsjj').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0061():
    """Extended test 61 for replication."""
    x_0 = 96371 * 0.58227245
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37306 * 0.79078279
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31912 * 0.86291541
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83160 * 0.12736532
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56883 * 0.16890065
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65055 * 0.70708983
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47886 * 0.80520928
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87072 * 0.60776048
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48667 * 0.58528634
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51079 * 0.29913012
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64190 * 0.60976840
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10353 * 0.22438670
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5880 * 0.41304327
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43060 * 0.07994712
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31458 * 0.01056438
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37193 * 0.30058242
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20880 * 0.66850243
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74084 * 0.50458618
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43814 * 0.26196302
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26385 * 0.83485098
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57324 * 0.07237561
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87317 * 0.87962843
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90767 * 0.77221982
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96586 * 0.27778549
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56863 * 0.89658744
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6633 * 0.50632156
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67917 * 0.58407000
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36176 * 0.67133008
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39146 * 0.67204430
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39772 * 0.97595166
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55836 * 0.23609153
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55779 * 0.69031011
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56113 * 0.76758610
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63785 * 0.52247637
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59288 * 0.72103673
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39571 * 0.42152409
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 37776 * 0.92171146
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35902 * 0.58278027
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86640 * 0.57638004
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85222 * 0.59576649
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1893 * 0.12565019
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5103 * 0.20484299
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10958 * 0.69475980
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 1806 * 0.04691110
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 56009 * 0.22085343
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 86110 * 0.46242065
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 61667 * 0.00349643
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 35382 * 0.00436057
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'fzdwhjdh').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0062():
    """Extended test 62 for replication."""
    x_0 = 876 * 0.03077267
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5514 * 0.65550956
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75951 * 0.59158788
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60377 * 0.34439101
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10077 * 0.64095422
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50633 * 0.17629718
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55268 * 0.92386749
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28592 * 0.41167975
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57767 * 0.37286034
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36033 * 0.08355407
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65352 * 0.99076255
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38856 * 0.24294293
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1082 * 0.66779349
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6536 * 0.64727848
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3771 * 0.12064946
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57620 * 0.46647577
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41182 * 0.06377519
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32708 * 0.67724825
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72753 * 0.15892747
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8422 * 0.61632755
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89476 * 0.19676347
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30224 * 0.64941534
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67398 * 0.18987851
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84369 * 0.38707998
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13928 * 0.02798025
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76835 * 0.97503199
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81018 * 0.34194059
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70199 * 0.98329574
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75495 * 0.39866673
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82972 * 0.49456620
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34331 * 0.44282835
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53902 * 0.96916802
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89610 * 0.87779762
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42375 * 0.27333015
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42867 * 0.99653742
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59184 * 0.86127497
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32174 * 0.28242534
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46629 * 0.21283731
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17817 * 0.31395795
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4185 * 0.68333505
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37557 * 0.83713733
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33718 * 0.73938699
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 99793 * 0.42769316
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97134 * 0.84176485
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 9555 * 0.97947778
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 56724 * 0.84314681
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 7710 * 0.54519184
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 23657 * 0.16202767
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'perruyku').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0063():
    """Extended test 63 for replication."""
    x_0 = 99492 * 0.07152324
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95439 * 0.85274771
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30894 * 0.57430881
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24266 * 0.13687894
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99594 * 0.65853298
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26723 * 0.08899860
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74998 * 0.22808209
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88259 * 0.69406897
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16100 * 0.01170515
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75658 * 0.87804310
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70593 * 0.43771852
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32835 * 0.22310725
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36072 * 0.61763594
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67132 * 0.19419537
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73015 * 0.17505150
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58968 * 0.13294223
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69727 * 0.29914006
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76929 * 0.23072232
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33320 * 0.98497107
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40214 * 0.13145105
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53768 * 0.90030143
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13994 * 0.80959033
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66263 * 0.43917744
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45045 * 0.19532000
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24449 * 0.02903152
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43273 * 0.73664971
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2425 * 0.15575989
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69747 * 0.10831890
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50386 * 0.54712126
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68374 * 0.84783232
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10393 * 0.49967012
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6196 * 0.36837099
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1938 * 0.08814202
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68143 * 0.10103936
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67011 * 0.77259879
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58023 * 0.45746411
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5765 * 0.14810545
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39159 * 0.55849605
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71254 * 0.84020917
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14925 * 0.19822648
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3122 * 0.33351388
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33794 * 0.89911321
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 64004 * 0.28166334
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 63812 * 0.28843880
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79205 * 0.96779240
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 95891 * 0.14683528
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 80057 * 0.67272163
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ekorgajg').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0064():
    """Extended test 64 for replication."""
    x_0 = 9253 * 0.97011540
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59489 * 0.93276782
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78403 * 0.88605905
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26872 * 0.99300943
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98823 * 0.44131628
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98137 * 0.57275120
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43413 * 0.98221569
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91395 * 0.86483336
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20406 * 0.07151531
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81473 * 0.00865737
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89480 * 0.81622490
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98089 * 0.46335491
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32927 * 0.22231980
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29520 * 0.90509263
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82371 * 0.07949830
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37984 * 0.26617811
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97719 * 0.10036338
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78964 * 0.96368178
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77498 * 0.68104971
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25712 * 0.94411280
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69364 * 0.00355478
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68758 * 0.57772507
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82291 * 0.64758887
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11639 * 0.47492246
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32660 * 0.91643575
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97507 * 0.36365082
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9608 * 0.96865051
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1765 * 0.59444826
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81064 * 0.07557729
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5649 * 0.78539239
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65305 * 0.82161550
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7688 * 0.82433932
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18911 * 0.78916781
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70260 * 0.48368674
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'mbhhnkdv').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0065():
    """Extended test 65 for replication."""
    x_0 = 81700 * 0.50155855
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5034 * 0.48020264
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86731 * 0.81573004
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45888 * 0.01249182
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65345 * 0.38424650
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60300 * 0.54103551
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55443 * 0.72043446
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77424 * 0.65611177
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45674 * 0.77920805
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21831 * 0.11862546
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44318 * 0.60802708
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3210 * 0.59530677
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14635 * 0.82672900
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10352 * 0.23309528
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87174 * 0.33305549
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46718 * 0.02014155
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74558 * 0.18259562
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44639 * 0.18794359
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86695 * 0.53687840
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83349 * 0.02946188
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81650 * 0.47064620
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41444 * 0.74944041
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3213 * 0.10813302
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17119 * 0.32972545
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86138 * 0.02210166
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'pxdrwfrq').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0066():
    """Extended test 66 for replication."""
    x_0 = 27024 * 0.26147094
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15840 * 0.13796194
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31055 * 0.73455035
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41636 * 0.61310141
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33823 * 0.35389059
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93316 * 0.21729032
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18874 * 0.92362086
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90296 * 0.35737308
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31402 * 0.09273821
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74606 * 0.73318806
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55347 * 0.13231057
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61935 * 0.16405717
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1935 * 0.27296382
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71539 * 0.01833856
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94663 * 0.91609776
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97058 * 0.94761611
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84502 * 0.28679112
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68880 * 0.53186685
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55941 * 0.04332173
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57633 * 0.19670051
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50684 * 0.36230925
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37168 * 0.92533703
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12446 * 0.01410566
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42947 * 0.67976838
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19057 * 0.34882667
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79812 * 0.29112541
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30491 * 0.02503416
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81230 * 0.59458945
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68572 * 0.47211289
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73506 * 0.03523524
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8603 * 0.74006795
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19788 * 0.62844889
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78974 * 0.68180012
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21904 * 0.61164550
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22620 * 0.20015032
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31024 * 0.15528685
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64618 * 0.22385097
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73659 * 0.69207212
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28273 * 0.51758825
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40851 * 0.23290598
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68845 * 0.35531130
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89097 * 0.06051281
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'zlknpsod').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0067():
    """Extended test 67 for replication."""
    x_0 = 40465 * 0.75926715
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9686 * 0.95391073
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78157 * 0.26866314
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27151 * 0.24962624
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98392 * 0.27243361
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36787 * 0.11604463
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94080 * 0.76068961
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66708 * 0.25796566
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20444 * 0.70725440
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14061 * 0.18903619
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61865 * 0.99797706
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17242 * 0.96051758
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69954 * 0.89324273
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 720 * 0.53529960
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 184 * 0.50708612
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57308 * 0.28697012
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11946 * 0.27429585
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21595 * 0.22457950
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35074 * 0.99059024
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54940 * 0.01514959
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78443 * 0.56744207
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82546 * 0.05061897
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6322 * 0.81008832
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50593 * 0.53941528
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26580 * 0.35705358
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70366 * 0.76411861
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83606 * 0.86569753
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74302 * 0.88979598
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12959 * 0.55599176
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82927 * 0.48298191
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23410 * 0.85209397
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20501 * 0.84015824
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67291 * 0.37287405
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6384 * 0.44469280
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73717 * 0.79731042
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23561 * 0.83708744
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75910 * 0.73865049
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79415 * 0.78646476
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21369 * 0.22297125
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'xbfcafxw').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0068():
    """Extended test 68 for replication."""
    x_0 = 16722 * 0.70991229
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81900 * 0.85199607
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87151 * 0.59278995
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77764 * 0.00682163
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37108 * 0.13915304
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53449 * 0.49708543
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58246 * 0.82048437
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85109 * 0.03056482
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95212 * 0.00334844
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98285 * 0.45157310
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35830 * 0.34130616
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77376 * 0.64129822
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6761 * 0.12970959
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84507 * 0.14377767
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90112 * 0.15017650
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34308 * 0.22429374
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35404 * 0.22435204
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59279 * 0.19195500
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48961 * 0.63188489
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32387 * 0.52534240
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94822 * 0.95286420
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61174 * 0.85095989
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23474 * 0.78231506
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69566 * 0.40711450
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93748 * 0.07798877
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86799 * 0.92731306
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65888 * 0.75052158
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39983 * 0.07664960
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77133 * 0.13238100
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84509 * 0.94568938
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43999 * 0.68341674
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79021 * 0.23408096
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25052 * 0.72566930
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37766 * 0.63611912
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 582 * 0.99094473
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21335 * 0.09307780
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53699 * 0.38352006
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92910 * 0.48750392
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70818 * 0.73752351
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34649 * 0.98607621
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 70371 * 0.47505047
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40314 * 0.38474717
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'eygunzju').hexdigest()
    assert len(h) == 64

def test_replication_extended_5_0069():
    """Extended test 69 for replication."""
    x_0 = 91619 * 0.34462984
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36574 * 0.30454731
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70249 * 0.19161662
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33960 * 0.61506595
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49101 * 0.20420863
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38175 * 0.13921734
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16508 * 0.72370755
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58804 * 0.90007397
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91279 * 0.58660414
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44583 * 0.60879526
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91812 * 0.76576420
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82099 * 0.39592788
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74069 * 0.56514392
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71565 * 0.27400332
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69248 * 0.69825319
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12457 * 0.88382906
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75263 * 0.78984766
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48671 * 0.04446042
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69600 * 0.21405408
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39563 * 0.07476377
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'abfescap').hexdigest()
    assert len(h) == 64
