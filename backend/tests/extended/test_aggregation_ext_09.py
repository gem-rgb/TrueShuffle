"""Extended tests for aggregation suite 9."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_aggregation_extended_9_0000():
    """Extended test 0 for aggregation."""
    x_0 = 61295 * 0.71543673
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85663 * 0.66561441
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42875 * 0.27153779
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88095 * 0.73447148
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43905 * 0.81615028
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83172 * 0.82386054
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21691 * 0.20364851
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60094 * 0.20605450
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5650 * 0.10478442
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44605 * 0.38667378
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95869 * 0.98680720
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68828 * 0.45888147
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56866 * 0.29350295
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54045 * 0.59269005
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55831 * 0.49699447
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72809 * 0.44195813
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92940 * 0.75938254
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23150 * 0.96281395
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1646 * 0.67307283
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59181 * 0.12552664
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47170 * 0.93655509
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70882 * 0.28876688
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'brfsakaa').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0001():
    """Extended test 1 for aggregation."""
    x_0 = 99347 * 0.02927376
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91704 * 0.53778675
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82157 * 0.18656468
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82810 * 0.60884496
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63319 * 0.03310139
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54930 * 0.48200075
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23916 * 0.92086206
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28650 * 0.82883813
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70083 * 0.56072868
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12205 * 0.89708140
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82356 * 0.54292973
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58176 * 0.34224202
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61365 * 0.42333925
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33365 * 0.19144739
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30654 * 0.40577370
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51238 * 0.45739075
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37726 * 0.72426946
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68432 * 0.49350517
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38150 * 0.25225311
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78179 * 0.83913230
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43064 * 0.78938304
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94868 * 0.21064581
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67646 * 0.28119042
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'xbvqdyjg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0002():
    """Extended test 2 for aggregation."""
    x_0 = 62978 * 0.12112815
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34340 * 0.70253224
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65894 * 0.95646256
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5888 * 0.92952782
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18443 * 0.68546012
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97030 * 0.95794342
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20693 * 0.13511131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93676 * 0.61023338
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73896 * 0.52193734
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18196 * 0.24744559
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72733 * 0.57405735
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56228 * 0.39953779
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41101 * 0.54959179
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79497 * 0.35677224
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90834 * 0.22784755
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13256 * 0.61495296
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52884 * 0.30592643
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60798 * 0.67639551
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9300 * 0.73081746
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58473 * 0.99502281
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39714 * 0.30554546
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30216 * 0.48028291
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54120 * 0.15838806
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6498 * 0.00929016
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67978 * 0.77798733
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'tdepxkge').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0003():
    """Extended test 3 for aggregation."""
    x_0 = 66075 * 0.93830848
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14867 * 0.72955472
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95351 * 0.87609858
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38682 * 0.45439041
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89789 * 0.55613807
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34986 * 0.42834878
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95468 * 0.46296573
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21961 * 0.30841387
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64533 * 0.73905665
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9655 * 0.66869689
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10624 * 0.74400763
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83890 * 0.75845564
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43806 * 0.25899965
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14757 * 0.68581360
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55088 * 0.93547639
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59495 * 0.81885995
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40075 * 0.55517276
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16379 * 0.49419570
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14777 * 0.14772294
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95678 * 0.35172031
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79664 * 0.49015751
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61669 * 0.82130121
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36697 * 0.37166502
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82748 * 0.56215452
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28404 * 0.02799901
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59432 * 0.00970928
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26825 * 0.90739913
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6139 * 0.47039303
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54076 * 0.59134615
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48899 * 0.54118303
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65695 * 0.30444750
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13665 * 0.59086322
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57087 * 0.82908600
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2440 * 0.98908551
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62157 * 0.96571622
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59911 * 0.34760619
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'jhmtfivt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0004():
    """Extended test 4 for aggregation."""
    x_0 = 25360 * 0.94864131
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48317 * 0.44377646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2777 * 0.51362592
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27611 * 0.27259399
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28185 * 0.70243726
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77472 * 0.85037299
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82257 * 0.52734421
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21124 * 0.89183610
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85121 * 0.04344971
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27390 * 0.67075782
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84634 * 0.00745365
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26232 * 0.02103929
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50098 * 0.98187883
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13677 * 0.83850651
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28080 * 0.64042979
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71298 * 0.77116800
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17622 * 0.10106782
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78121 * 0.74676342
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47806 * 0.44524790
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70973 * 0.42035294
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97731 * 0.05605927
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58357 * 0.90539615
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 182 * 0.94359983
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86282 * 0.93014797
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32300 * 0.93168025
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6282 * 0.96257771
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65348 * 0.17326686
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85042 * 0.86192568
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74739 * 0.58664854
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94530 * 0.29855541
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71633 * 0.43098358
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63620 * 0.12905108
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80261 * 0.91362830
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72709 * 0.31617962
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50132 * 0.11384103
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76552 * 0.54717225
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94714 * 0.00587995
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30237 * 0.42650595
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98643 * 0.09087324
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'sgohphvu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0005():
    """Extended test 5 for aggregation."""
    x_0 = 80135 * 0.21201337
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60847 * 0.73744547
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88376 * 0.52375985
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14608 * 0.60814459
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96182 * 0.52773289
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32301 * 0.01184342
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78543 * 0.85773324
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11759 * 0.08761971
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77181 * 0.61252537
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23743 * 0.58969258
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3761 * 0.96100511
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39459 * 0.47781347
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20925 * 0.11402663
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48964 * 0.44112220
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34110 * 0.07878010
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82974 * 0.87432315
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63711 * 0.69164244
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54753 * 0.65712771
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88761 * 0.90940079
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30490 * 0.44279205
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23783 * 0.90278826
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29701 * 0.91164013
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97256 * 0.70546286
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82134 * 0.51804601
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34923 * 0.07328872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10298 * 0.11552043
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79267 * 0.36125966
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75164 * 0.76433556
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83643 * 0.50608666
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91533 * 0.23841461
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69288 * 0.81024455
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19661 * 0.89784697
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62328 * 0.85977012
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11369 * 0.79083060
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'ylzcplbf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0006():
    """Extended test 6 for aggregation."""
    x_0 = 30073 * 0.46953176
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32767 * 0.38533397
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77737 * 0.82044863
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92856 * 0.87488326
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37383 * 0.74305874
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61409 * 0.51718128
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56637 * 0.30621952
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2679 * 0.00289665
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59285 * 0.05078811
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61006 * 0.37794126
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22904 * 0.25352177
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35313 * 0.16418283
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85528 * 0.82568171
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28524 * 0.44804750
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67934 * 0.12038004
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63661 * 0.42974770
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53791 * 0.89024325
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19451 * 0.06613831
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 867 * 0.80453735
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22135 * 0.76895767
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18873 * 0.30794723
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45054 * 0.73140609
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33515 * 0.10916741
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92825 * 0.87675882
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94534 * 0.23405526
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61967 * 0.56000871
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44118 * 0.40874709
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81744 * 0.13499645
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23182 * 0.46326068
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51316 * 0.13789766
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64203 * 0.56392959
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ksaxdmee').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0007():
    """Extended test 7 for aggregation."""
    x_0 = 57111 * 0.20309091
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34949 * 0.83643813
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48089 * 0.32394317
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61983 * 0.82351662
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68437 * 0.84325049
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75226 * 0.72087243
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46605 * 0.60478969
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6880 * 0.81624665
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17938 * 0.15467857
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2089 * 0.30489775
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51282 * 0.75297445
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20468 * 0.71725518
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4463 * 0.85889909
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49590 * 0.86813736
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52267 * 0.19421800
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44687 * 0.73347862
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23199 * 0.76901278
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42565 * 0.62572960
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21968 * 0.55499188
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46211 * 0.25648193
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82615 * 0.94274482
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41882 * 0.50099860
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14824 * 0.02667310
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65977 * 0.89386119
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46499 * 0.68557934
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62397 * 0.12856060
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93407 * 0.23189780
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33996 * 0.21307989
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95994 * 0.90849521
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69912 * 0.84599561
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36786 * 0.95379590
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95200 * 0.41520729
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30108 * 0.62608059
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93483 * 0.54344117
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 49580 * 0.64359155
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10614 * 0.69755720
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35502 * 0.82586103
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98531 * 0.43397084
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91882 * 0.50967488
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66241 * 0.11229061
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74711 * 0.03542565
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'jfixgpby').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0008():
    """Extended test 8 for aggregation."""
    x_0 = 2264 * 0.31851545
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66615 * 0.69384667
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86298 * 0.12945790
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88255 * 0.56901397
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32335 * 0.08111703
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87602 * 0.95296302
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25772 * 0.51874450
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75234 * 0.37696873
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64614 * 0.91269989
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92983 * 0.37937050
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50918 * 0.37515321
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89018 * 0.82699853
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40213 * 0.16377367
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64243 * 0.33419171
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29300 * 0.94351061
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56426 * 0.14177785
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48651 * 0.60902349
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57454 * 0.66367560
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9874 * 0.19732236
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26568 * 0.37078569
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14675 * 0.08267979
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77042 * 0.37269482
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92518 * 0.99416086
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'zbsujhhb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0009():
    """Extended test 9 for aggregation."""
    x_0 = 58225 * 0.84637859
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69555 * 0.06342219
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16419 * 0.78708510
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74112 * 0.59097962
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32232 * 0.93062867
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13860 * 0.47379076
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73764 * 0.87759737
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35819 * 0.41529910
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99152 * 0.16646940
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33700 * 0.08742530
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26934 * 0.22893174
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9739 * 0.28391684
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97258 * 0.06643401
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76890 * 0.21646316
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87256 * 0.58545682
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23111 * 0.04041943
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65892 * 0.96714237
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73905 * 0.42254471
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73104 * 0.38387124
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54136 * 0.73161980
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54830 * 0.81628061
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 644 * 0.65167488
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67934 * 0.89678618
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7634 * 0.51708012
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93159 * 0.60991767
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1935 * 0.26556981
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48375 * 0.81546447
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48454 * 0.72163773
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22905 * 0.93515618
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75919 * 0.92949106
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48951 * 0.21246533
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33666 * 0.68172993
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10549 * 0.16671794
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94766 * 0.92533752
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'rfgeiwsq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0010():
    """Extended test 10 for aggregation."""
    x_0 = 53859 * 0.72101799
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18879 * 0.41227911
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50683 * 0.02737235
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27848 * 0.77688189
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8274 * 0.96972213
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65752 * 0.77567749
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69890 * 0.04493072
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8811 * 0.57734327
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26433 * 0.62801808
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56931 * 0.01994350
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75660 * 0.30780763
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59460 * 0.16259864
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43122 * 0.03186123
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98671 * 0.32989999
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15183 * 0.14057513
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61340 * 0.01692224
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97276 * 0.68317522
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10960 * 0.36852395
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52628 * 0.77115700
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94664 * 0.17043410
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59904 * 0.00597595
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81920 * 0.95522153
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71946 * 0.91257670
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2441 * 0.77791513
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'viqgwbrr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0011():
    """Extended test 11 for aggregation."""
    x_0 = 66160 * 0.72091333
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92832 * 0.21046127
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63156 * 0.41115685
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69639 * 0.15050790
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34994 * 0.43346203
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4222 * 0.34968215
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99470 * 0.38842447
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59325 * 0.72774618
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90320 * 0.92127971
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41940 * 0.04370066
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27206 * 0.94211540
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79115 * 0.57953236
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79137 * 0.11233134
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6258 * 0.14439401
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21258 * 0.27714165
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28871 * 0.10614805
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14657 * 0.74106799
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98655 * 0.47531924
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21687 * 0.49567728
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42797 * 0.72396720
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74755 * 0.62547426
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61607 * 0.59487274
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91869 * 0.31455755
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93293 * 0.56138837
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40000 * 0.86770921
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20999 * 0.51532931
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85318 * 0.74255752
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91091 * 0.97030941
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'qbnmxmps').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0012():
    """Extended test 12 for aggregation."""
    x_0 = 51610 * 0.42593330
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37992 * 0.54735332
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82815 * 0.89179057
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30888 * 0.75344487
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30826 * 0.76948303
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36901 * 0.08313143
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66044 * 0.34257137
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51659 * 0.78252210
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91577 * 0.75904676
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59219 * 0.73486981
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70160 * 0.15181357
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16560 * 0.30998715
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81649 * 0.94620392
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84010 * 0.35689524
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28254 * 0.98138059
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29883 * 0.63546345
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67774 * 0.97488180
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31691 * 0.22200579
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82288 * 0.41915245
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72440 * 0.49463594
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55899 * 0.12881871
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73550 * 0.95487265
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 473 * 0.26839119
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9602 * 0.23212419
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34546 * 0.44518689
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87986 * 0.23525354
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83796 * 0.37430184
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68367 * 0.05313008
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97380 * 0.65141557
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59845 * 0.52682285
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73145 * 0.82333026
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83353 * 0.29896666
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79372 * 0.08578882
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23185 * 0.77538793
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38920 * 0.49005351
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57753 * 0.73398818
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35022 * 0.88132335
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'hsscfuln').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0013():
    """Extended test 13 for aggregation."""
    x_0 = 95752 * 0.14390193
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74334 * 0.09806168
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39632 * 0.71198622
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45386 * 0.91342552
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42653 * 0.33216456
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1939 * 0.07165597
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44122 * 0.30798255
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17265 * 0.59788878
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70484 * 0.79531999
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43046 * 0.28313171
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63027 * 0.01847428
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38317 * 0.29626386
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90456 * 0.28251093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20950 * 0.20504929
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90395 * 0.24829879
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46751 * 0.31415722
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10064 * 0.28676818
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48723 * 0.01517166
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37259 * 0.72144954
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47032 * 0.43382651
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75841 * 0.40754223
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24704 * 0.56283406
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49058 * 0.97164868
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'upsecgph').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0014():
    """Extended test 14 for aggregation."""
    x_0 = 78517 * 0.66160731
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68984 * 0.46463570
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42703 * 0.12928730
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45844 * 0.11029787
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86948 * 0.95481026
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8410 * 0.21646930
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6871 * 0.45424383
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67284 * 0.68151755
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58769 * 0.19891372
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22438 * 0.89893072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1172 * 0.44809550
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90513 * 0.37000675
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31596 * 0.85494778
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32813 * 0.78360044
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49772 * 0.08543059
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3227 * 0.99210416
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24156 * 0.00804422
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18040 * 0.10387225
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30031 * 0.60081698
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89197 * 0.30533734
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92320 * 0.19499239
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38693 * 0.51622671
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9100 * 0.20558389
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24611 * 0.80235280
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61035 * 0.84812873
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37477 * 0.34862781
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56425 * 0.94108090
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82290 * 0.65475978
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4410 * 0.90605745
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31631 * 0.48537008
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1912 * 0.34816521
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86067 * 0.56741396
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'lzqpldvx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0015():
    """Extended test 15 for aggregation."""
    x_0 = 18370 * 0.21895918
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13436 * 0.08184392
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10017 * 0.03914019
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89339 * 0.24428081
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93742 * 0.57403066
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16911 * 0.99267586
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25582 * 0.10126425
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79570 * 0.16223871
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46609 * 0.82464665
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89324 * 0.21192714
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80847 * 0.26578831
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31447 * 0.59777616
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45457 * 0.98421451
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51802 * 0.26633346
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39174 * 0.55225803
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79677 * 0.46601791
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71034 * 0.47778821
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49568 * 0.14009528
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99260 * 0.29563556
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12112 * 0.72772750
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81734 * 0.76063326
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50711 * 0.58532325
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52851 * 0.86364130
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55168 * 0.98723294
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80199 * 0.35294964
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16820 * 0.35206324
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48919 * 0.15717324
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9878 * 0.84955660
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24985 * 0.19270586
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29624 * 0.06801827
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60147 * 0.99395429
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85642 * 0.05952880
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32149 * 0.44116041
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56454 * 0.08630957
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54430 * 0.58408419
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95716 * 0.07219760
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73148 * 0.35882059
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65081 * 0.34934350
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73134 * 0.06684572
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66757 * 0.55431878
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29789 * 0.71138757
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4500 * 0.24186669
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 85220 * 0.46376183
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69987 * 0.39622146
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 30376 * 0.06376843
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'ozpkxmhx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0016():
    """Extended test 16 for aggregation."""
    x_0 = 48480 * 0.21126490
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95916 * 0.34479534
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91579 * 0.54560330
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98765 * 0.39504354
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53353 * 0.90613203
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29797 * 0.33414408
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25209 * 0.57937879
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94931 * 0.56433321
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18290 * 0.63432254
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79735 * 0.04100001
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 944 * 0.95908373
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23314 * 0.08146821
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56668 * 0.74498827
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58907 * 0.83333172
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66220 * 0.61856844
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57167 * 0.78803094
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78139 * 0.70338872
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22080 * 0.16197721
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78908 * 0.49329347
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37565 * 0.88019418
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51646 * 0.56703707
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75180 * 0.48677925
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44628 * 0.99234903
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59967 * 0.04895695
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85952 * 0.82690305
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17808 * 0.60825605
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53911 * 0.74726242
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1943 * 0.38722088
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71686 * 0.13729240
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53610 * 0.10469693
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63597 * 0.73502079
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'xfwbugde').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0017():
    """Extended test 17 for aggregation."""
    x_0 = 39793 * 0.46839961
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94399 * 0.15364412
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23103 * 0.57813313
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55639 * 0.09276445
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2972 * 0.46638810
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15214 * 0.07149857
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80916 * 0.21565966
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74205 * 0.32783088
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12310 * 0.35178716
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94646 * 0.93116220
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37847 * 0.73185445
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54680 * 0.09536436
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64301 * 0.59053372
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12209 * 0.43391092
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98947 * 0.58070530
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8384 * 0.60145703
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38507 * 0.71211631
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90688 * 0.52250448
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44241 * 0.83314496
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84315 * 0.60586659
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6038 * 0.43736179
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'nywvzukv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0018():
    """Extended test 18 for aggregation."""
    x_0 = 12081 * 0.92337127
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39289 * 0.09828611
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36775 * 0.95600412
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15936 * 0.01068876
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53571 * 0.08147873
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78427 * 0.62498891
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86729 * 0.28583293
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83237 * 0.08895517
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27388 * 0.64995625
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72550 * 0.62792356
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35012 * 0.45128251
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95055 * 0.31133310
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 412 * 0.83865825
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79535 * 0.94869772
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 472 * 0.58546734
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64794 * 0.15477979
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44470 * 0.70879889
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59462 * 0.73894729
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 781 * 0.08869701
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82395 * 0.76033536
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48380 * 0.06909702
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62229 * 0.55884032
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16985 * 0.61994111
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24356 * 0.40736173
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49789 * 0.00034762
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'vtmwycmq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0019():
    """Extended test 19 for aggregation."""
    x_0 = 84625 * 0.10814668
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42052 * 0.18295425
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13185 * 0.11220250
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18704 * 0.39037449
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47765 * 0.01231246
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85430 * 0.73147696
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86643 * 0.77692512
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71873 * 0.20986055
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57175 * 0.64411209
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68685 * 0.29112848
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13311 * 0.38544851
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75061 * 0.70707257
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87239 * 0.54766160
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54812 * 0.27425853
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10202 * 0.42360716
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19758 * 0.20853565
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39264 * 0.55111709
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86121 * 0.35006322
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66513 * 0.78494274
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84299 * 0.92603229
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2751 * 0.30443929
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5515 * 0.07329925
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'zhobdkoz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0020():
    """Extended test 20 for aggregation."""
    x_0 = 11335 * 0.65952142
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98999 * 0.53853622
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15762 * 0.09902511
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54735 * 0.51420975
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22186 * 0.52883853
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40560 * 0.76866753
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9640 * 0.32371077
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42286 * 0.47904001
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1531 * 0.91421717
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79378 * 0.89704562
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44412 * 0.86899283
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17458 * 0.59581964
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57970 * 0.07640779
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55062 * 0.83420029
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19349 * 0.74976965
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83942 * 0.68712176
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98200 * 0.37687496
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90271 * 0.25516972
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92547 * 0.81595856
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46304 * 0.14026627
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'dypabhqc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0021():
    """Extended test 21 for aggregation."""
    x_0 = 22793 * 0.04671896
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13832 * 0.93333645
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68802 * 0.02431279
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70409 * 0.24602226
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24718 * 0.13161089
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40216 * 0.34432047
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69427 * 0.98499624
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37605 * 0.39130125
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71146 * 0.25959548
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80219 * 0.00977466
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81547 * 0.00065899
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86981 * 0.71666306
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50689 * 0.68426382
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28287 * 0.89171081
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57131 * 0.00100229
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96688 * 0.08742378
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57587 * 0.61985158
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91921 * 0.74885760
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60627 * 0.52076460
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53289 * 0.46542066
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43718 * 0.40280144
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24552 * 0.56967817
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70186 * 0.27025950
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 428 * 0.31092623
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74618 * 0.00162205
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5247 * 0.44801504
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60506 * 0.75545120
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80862 * 0.10938233
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78766 * 0.78388672
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89605 * 0.04716227
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97682 * 0.46552930
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39507 * 0.72452424
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'kwbhafds').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0022():
    """Extended test 22 for aggregation."""
    x_0 = 9707 * 0.01501912
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36994 * 0.20945481
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48550 * 0.46954178
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91666 * 0.50799825
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70260 * 0.25685297
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91445 * 0.99547169
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19018 * 0.26866966
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96462 * 0.68514346
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51639 * 0.31768934
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78658 * 0.10628500
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96840 * 0.86703875
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88023 * 0.19953271
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82884 * 0.26718611
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25668 * 0.82423878
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28006 * 0.81493473
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52612 * 0.06713950
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53194 * 0.04346788
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17927 * 0.36733618
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64751 * 0.23310822
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91676 * 0.33328704
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2070 * 0.95734519
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12280 * 0.27218478
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61418 * 0.15391622
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27388 * 0.92602574
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30838 * 0.63505044
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38700 * 0.73395244
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49172 * 0.74702555
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7954 * 0.58028015
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12602 * 0.57558408
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47763 * 0.81940293
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2638 * 0.88232069
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29076 * 0.06992701
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69959 * 0.70919415
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2481 * 0.08715142
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20599 * 0.84441597
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88028 * 0.74508644
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51067 * 0.64525874
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 51121 * 0.93679954
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60810 * 0.54925443
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83402 * 0.93455952
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36487 * 0.62655303
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 10136 * 0.07268112
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66783 * 0.48644342
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 70206 * 0.28687363
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 93910 * 0.99251342
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26951 * 0.89456284
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 47673 * 0.14711853
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 70831 * 0.30088235
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'jmqxartx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0023():
    """Extended test 23 for aggregation."""
    x_0 = 31579 * 0.83413507
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85827 * 0.07635839
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41848 * 0.45525925
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42579 * 0.71545013
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89699 * 0.52826969
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84868 * 0.25209663
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62812 * 0.99576671
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1161 * 0.45227902
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35591 * 0.75427086
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19458 * 0.31975920
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10483 * 0.36815374
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81596 * 0.72276213
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31386 * 0.27517921
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47862 * 0.69018852
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6751 * 0.22960095
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76501 * 0.80090305
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50294 * 0.22403192
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7529 * 0.90831696
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85623 * 0.41663441
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56892 * 0.41819773
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42593 * 0.55198378
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57862 * 0.26449053
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78434 * 0.53906501
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12563 * 0.41258177
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95166 * 0.82761031
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32389 * 0.74261941
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16745 * 0.47650147
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1983 * 0.48202777
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22306 * 0.68444652
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40120 * 0.64958887
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48547 * 0.36622390
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5253 * 0.03374088
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85505 * 0.85559591
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62057 * 0.77618883
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37731 * 0.39137230
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40138 * 0.24876826
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16810 * 0.28568155
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19362 * 0.14734968
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74227 * 0.33247153
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25621 * 0.92447412
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45104 * 0.21205895
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96472 * 0.18102184
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 3481 * 0.06097883
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 95401 * 0.17548983
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 31326 * 0.46178918
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'adzrawxy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0024():
    """Extended test 24 for aggregation."""
    x_0 = 19482 * 0.64925299
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 177 * 0.56580318
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34082 * 0.33721388
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53610 * 0.59069918
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46945 * 0.25369836
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12290 * 0.63687886
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3745 * 0.41344371
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63547 * 0.72410138
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84823 * 0.40294089
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48489 * 0.17087125
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90830 * 0.82125580
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 352 * 0.23245337
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55276 * 0.58920668
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7937 * 0.35744096
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68506 * 0.40224829
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66349 * 0.36110895
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23448 * 0.05412626
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62195 * 0.29355629
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58327 * 0.20933223
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75333 * 0.04279271
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10743 * 0.95754567
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61614 * 0.98453878
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28210 * 0.66591764
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47864 * 0.91447467
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44008 * 0.03007468
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66965 * 0.87101161
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36007 * 0.95109103
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55851 * 0.69240687
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18661 * 0.54757662
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76949 * 0.38012811
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66166 * 0.05422220
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51057 * 0.13802980
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56838 * 0.63657200
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85982 * 0.58685877
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'jlcggszn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0025():
    """Extended test 25 for aggregation."""
    x_0 = 41399 * 0.80057424
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20554 * 0.74517664
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64411 * 0.46478068
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30136 * 0.92717572
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37596 * 0.06214751
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93173 * 0.35943774
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13105 * 0.29264607
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83277 * 0.83789014
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76962 * 0.63031666
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17529 * 0.18201153
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69729 * 0.24973741
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14770 * 0.89750329
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57308 * 0.53450412
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19111 * 0.29354129
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71848 * 0.01009212
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11053 * 0.90208962
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75073 * 0.41903688
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70866 * 0.64375808
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9154 * 0.77949650
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92156 * 0.98678922
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49231 * 0.50838075
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88032 * 0.27294846
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4987 * 0.31597546
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96733 * 0.03124653
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49228 * 0.51056229
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55531 * 0.67330256
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2672 * 0.48198427
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96160 * 0.19153670
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14655 * 0.60423128
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27642 * 0.96194506
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28069 * 0.78109993
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8358 * 0.11828576
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87850 * 0.53549045
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11531 * 0.70447360
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92144 * 0.20892807
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63007 * 0.85109317
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88946 * 0.76934170
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3439 * 0.64098438
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36026 * 0.99939635
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42882 * 0.54701479
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5438 * 0.80786759
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3594 * 0.19977992
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 63997 * 0.42761701
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 312 * 0.34876588
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 7667 * 0.82106207
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 96145 * 0.85965256
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 98020 * 0.84192881
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 72667 * 0.98875707
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 37982 * 0.78127444
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'gajoekry').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0026():
    """Extended test 26 for aggregation."""
    x_0 = 9877 * 0.62034097
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96677 * 0.61596767
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91877 * 0.68546050
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38088 * 0.11454690
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10966 * 0.36577042
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73221 * 0.95011733
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46584 * 0.15866257
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99908 * 0.42264216
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23567 * 0.22527152
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96457 * 0.09163398
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54794 * 0.61052926
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3613 * 0.00035197
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32009 * 0.59035528
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24064 * 0.52321482
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61781 * 0.22195681
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26663 * 0.93290398
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73492 * 0.66801802
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60683 * 0.25986433
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25652 * 0.29195502
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71745 * 0.23088816
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 148 * 0.28908808
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18748 * 0.22127049
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55814 * 0.73569970
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2346 * 0.85803017
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98188 * 0.64193322
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46700 * 0.08194515
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32879 * 0.88436770
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74888 * 0.74163651
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14374 * 0.54434878
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'qfmagezs').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0027():
    """Extended test 27 for aggregation."""
    x_0 = 34751 * 0.35515802
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71541 * 0.86746920
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32352 * 0.24453296
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20574 * 0.33555681
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13642 * 0.42789016
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88803 * 0.29575283
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43564 * 0.10706237
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85553 * 0.91682544
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34304 * 0.67810739
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80629 * 0.16657894
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26725 * 0.21297556
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91300 * 0.94411662
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8088 * 0.82445109
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19368 * 0.13643849
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16325 * 0.11497618
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16866 * 0.63440600
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19867 * 0.66120044
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92809 * 0.73382728
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91678 * 0.06043895
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19925 * 0.00909593
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27778 * 0.61148838
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16814 * 0.71533182
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6336 * 0.10862261
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65264 * 0.82422383
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33990 * 0.15830222
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68600 * 0.72223391
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35788 * 0.87078303
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72958 * 0.08750953
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 282 * 0.26332130
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35576 * 0.11895804
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45873 * 0.00857553
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97691 * 0.31781685
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9320 * 0.86715772
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3682 * 0.80925352
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60438 * 0.36518064
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27034 * 0.86094514
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6982 * 0.13135592
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81347 * 0.83136337
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76874 * 0.73512580
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1135 * 0.80664201
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21702 * 0.73842505
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 61140 * 0.80515134
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9968 * 0.28959796
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75037 * 0.52906635
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 28223 * 0.42882687
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 86692 * 0.95114928
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 23471 * 0.66409987
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 83753 * 0.74793425
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 99745 * 0.39360349
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'cspnkpku').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0028():
    """Extended test 28 for aggregation."""
    x_0 = 22777 * 0.01537186
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41827 * 0.05222665
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40791 * 0.98339152
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88769 * 0.47100596
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50046 * 0.52043545
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3978 * 0.08429832
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92049 * 0.11385877
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96530 * 0.77287774
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47522 * 0.14078362
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50325 * 0.50119744
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5520 * 0.61808544
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54026 * 0.07399888
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55441 * 0.28040908
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38839 * 0.59699824
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85372 * 0.61512384
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22345 * 0.39038485
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66984 * 0.80289037
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69726 * 0.44003167
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83070 * 0.45523432
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30147 * 0.99637017
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21130 * 0.70538102
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19329 * 0.96476422
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33890 * 0.70007278
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74229 * 0.65196366
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80301 * 0.99735362
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10788 * 0.28933542
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54853 * 0.49954363
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46302 * 0.08227981
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44712 * 0.59969469
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22532 * 0.86392212
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18356 * 0.81655715
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81936 * 0.34251679
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76941 * 0.12589020
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16844 * 0.31023874
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2893 * 0.68566259
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96872 * 0.06405206
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9 * 0.69298986
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'wylfcvef').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0029():
    """Extended test 29 for aggregation."""
    x_0 = 75253 * 0.86036184
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75308 * 0.44656295
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13266 * 0.11823703
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38355 * 0.19385564
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95520 * 0.70483836
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64216 * 0.18073369
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1488 * 0.35809455
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27746 * 0.88586731
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62147 * 0.29608497
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66036 * 0.86679554
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14290 * 0.15230068
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17407 * 0.06009536
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97891 * 0.09327023
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16619 * 0.63676076
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31286 * 0.33771214
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34115 * 0.55350886
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21544 * 0.68325285
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78526 * 0.56123144
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23010 * 0.09452416
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68355 * 0.93244190
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40104 * 0.77926867
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48615 * 0.04777854
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87687 * 0.01895668
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40995 * 0.77138027
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'rztehdte').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0030():
    """Extended test 30 for aggregation."""
    x_0 = 8209 * 0.03002508
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27994 * 0.21034892
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5656 * 0.03855922
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24858 * 0.11253585
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58179 * 0.46911415
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59106 * 0.33394327
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68532 * 0.65277735
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89763 * 0.31506872
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35069 * 0.21220418
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37421 * 0.42616220
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84550 * 0.51116078
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50469 * 0.98981706
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52331 * 0.55674977
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44516 * 0.28669896
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42201 * 0.02455382
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95778 * 0.70244339
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50160 * 0.38973096
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34446 * 0.12804266
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61761 * 0.90195747
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32441 * 0.95865145
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76128 * 0.56122996
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50360 * 0.88666546
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50707 * 0.73189156
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25039 * 0.20651713
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96719 * 0.22301218
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11653 * 0.06008697
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19479 * 0.71490366
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32865 * 0.45651504
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79196 * 0.93608744
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52518 * 0.11449635
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49920 * 0.13235461
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73321 * 0.54319503
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58347 * 0.84388018
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39815 * 0.21634599
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'avrsqzdq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0031():
    """Extended test 31 for aggregation."""
    x_0 = 44442 * 0.63935487
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66439 * 0.48797214
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33894 * 0.59066396
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81380 * 0.40292989
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88757 * 0.85550476
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71370 * 0.67145102
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65351 * 0.14206723
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27725 * 0.17519666
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58814 * 0.30697094
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73905 * 0.23681203
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55982 * 0.50280014
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21437 * 0.55404065
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22851 * 0.86214712
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78924 * 0.69598346
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13999 * 0.56917980
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23014 * 0.54291617
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79524 * 0.59961113
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28412 * 0.80021799
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76638 * 0.91740157
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57724 * 0.64051229
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64096 * 0.66088035
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'obipzxft').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0032():
    """Extended test 32 for aggregation."""
    x_0 = 52874 * 0.36179869
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53559 * 0.67136579
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2186 * 0.82393277
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96628 * 0.04198893
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9666 * 0.95815626
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79169 * 0.60631564
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11086 * 0.14818748
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85219 * 0.45804608
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92980 * 0.30410941
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91236 * 0.15728255
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27884 * 0.54301348
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60574 * 0.21983885
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41130 * 0.78300787
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91684 * 0.77109925
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65022 * 0.95263409
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67550 * 0.17049514
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91840 * 0.49286573
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87800 * 0.27587369
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83291 * 0.75960111
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77148 * 0.79076745
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7426 * 0.11458921
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94871 * 0.92167772
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4388 * 0.18299233
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62956 * 0.10195750
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63132 * 0.95146327
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54826 * 0.79641188
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32887 * 0.90188780
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62204 * 0.05769085
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70246 * 0.16587543
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93158 * 0.92803177
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83444 * 0.19764947
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35134 * 0.38294866
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7708 * 0.50351435
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63581 * 0.72210317
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77169 * 0.62800356
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3990 * 0.03446281
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'qqjiyfik').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0033():
    """Extended test 33 for aggregation."""
    x_0 = 80833 * 0.61809681
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21854 * 0.43316481
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69277 * 0.01612232
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27245 * 0.73287186
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61460 * 0.85998990
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15464 * 0.92736806
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10934 * 0.09223201
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17840 * 0.51918473
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58563 * 0.80418084
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20753 * 0.84157029
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65524 * 0.88417552
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78932 * 0.11399379
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79539 * 0.14164386
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37128 * 0.15509388
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98975 * 0.95147510
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68148 * 0.95717372
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24804 * 0.29904607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73515 * 0.41652532
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97063 * 0.79999231
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45755 * 0.22858257
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61902 * 0.76286968
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92738 * 0.93137700
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93736 * 0.39735337
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50887 * 0.45029310
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94975 * 0.50872572
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66169 * 0.67727072
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40561 * 0.20219669
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92040 * 0.39616767
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5126 * 0.29337895
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77057 * 0.54216949
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49869 * 0.87619391
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48458 * 0.30876508
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3235 * 0.25164146
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60244 * 0.30021850
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64967 * 0.01258812
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53050 * 0.59589792
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65599 * 0.00691928
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34523 * 0.61455374
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74971 * 0.23963324
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'szeqpthx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0034():
    """Extended test 34 for aggregation."""
    x_0 = 73534 * 0.10298566
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27238 * 0.38387248
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83516 * 0.62185471
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18576 * 0.69166807
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43307 * 0.14025837
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86885 * 0.02214286
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74521 * 0.13877250
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23164 * 0.28282755
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5874 * 0.16932328
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54601 * 0.04567746
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8006 * 0.44795361
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7951 * 0.79477563
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38301 * 0.54708482
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29077 * 0.06279465
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98261 * 0.62666692
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94727 * 0.31824577
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84297 * 0.29895034
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49914 * 0.03296731
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98210 * 0.66705817
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76499 * 0.56928961
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39633 * 0.90159931
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12653 * 0.54670874
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98089 * 0.29224780
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81481 * 0.88192844
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7472 * 0.01896497
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83403 * 0.29121749
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'whqiwdep').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0035():
    """Extended test 35 for aggregation."""
    x_0 = 906 * 0.15723318
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17585 * 0.35181272
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51435 * 0.82748091
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28663 * 0.04977804
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8482 * 0.94070421
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8546 * 0.59406342
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31716 * 0.92179357
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90133 * 0.11881093
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14470 * 0.13716059
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52722 * 0.67037958
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98174 * 0.62265068
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62893 * 0.92377638
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76184 * 0.62056973
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14130 * 0.14341845
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28874 * 0.07647088
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82856 * 0.74377894
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68512 * 0.79637422
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13367 * 0.50675835
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39499 * 0.94609914
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72788 * 0.53986328
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17379 * 0.60633514
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54143 * 0.16700673
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'rewciopf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0036():
    """Extended test 36 for aggregation."""
    x_0 = 48458 * 0.03883005
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63903 * 0.60893695
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22883 * 0.78892841
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56026 * 0.23546859
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71508 * 0.25634239
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15570 * 0.00853796
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35834 * 0.05656406
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19383 * 0.20110559
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87363 * 0.75646072
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13100 * 0.50740837
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41674 * 0.17305773
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19854 * 0.90587050
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36421 * 0.54254489
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9504 * 0.51923747
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82992 * 0.25315069
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39257 * 0.94683468
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59003 * 0.30559121
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20181 * 0.86939078
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98924 * 0.16589213
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68061 * 0.93437783
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29886 * 0.04168198
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76197 * 0.89238967
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 257 * 0.90702259
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32970 * 0.34868334
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'toayleny').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0037():
    """Extended test 37 for aggregation."""
    x_0 = 15111 * 0.75580665
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62103 * 0.72435106
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72595 * 0.41169085
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92500 * 0.41309930
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64495 * 0.19939087
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33833 * 0.01780610
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70956 * 0.22390653
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87644 * 0.64278984
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31378 * 0.75912331
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78981 * 0.41785299
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85399 * 0.64045190
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28714 * 0.74159354
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73317 * 0.34614328
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32964 * 0.87659236
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25344 * 0.96139240
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57512 * 0.85013546
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68758 * 0.01913674
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19407 * 0.83608299
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58899 * 0.18487176
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93550 * 0.80562594
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54113 * 0.71234676
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93635 * 0.47633683
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99041 * 0.98818203
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88786 * 0.09548045
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73068 * 0.09782049
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24852 * 0.60051705
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50235 * 0.90363952
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57640 * 0.38709896
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17934 * 0.25969462
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32208 * 0.35861699
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80944 * 0.90194913
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88874 * 0.41165488
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30904 * 0.82321266
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92721 * 0.34074887
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38366 * 0.70602403
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45360 * 0.02787871
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41485 * 0.60497003
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25303 * 0.75197704
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75025 * 0.96822781
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54729 * 0.51605599
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53233 * 0.63383652
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27160 * 0.86150800
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41494 * 0.11237673
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 85203 * 0.72484159
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 62186 * 0.32865501
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 77082 * 0.02979179
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'zxnammzk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0038():
    """Extended test 38 for aggregation."""
    x_0 = 67568 * 0.76341715
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70902 * 0.66728103
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90704 * 0.45419040
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8565 * 0.40902582
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41686 * 0.90092891
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60548 * 0.32409707
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85102 * 0.73208983
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83361 * 0.21222378
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24867 * 0.72741661
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44611 * 0.96079143
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63465 * 0.38230639
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50232 * 0.72260020
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71117 * 0.99562080
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9488 * 0.82125341
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95323 * 0.38259036
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6718 * 0.06490143
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94803 * 0.57131800
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11319 * 0.52911001
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2784 * 0.53560537
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32852 * 0.12802270
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95014 * 0.74560934
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37804 * 0.80106922
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58881 * 0.65164016
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80576 * 0.40514884
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58332 * 0.81806031
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62598 * 0.74347432
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22752 * 0.75774582
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28291 * 0.48582538
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3884 * 0.18190828
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59730 * 0.99037572
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26261 * 0.54539247
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7756 * 0.93643218
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29791 * 0.08284264
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18804 * 0.05049832
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42155 * 0.65585591
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45276 * 0.11061218
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90512 * 0.58290962
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 223 * 0.89628986
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20172 * 0.74227739
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 48965 * 0.98246091
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'eujgyajl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0039():
    """Extended test 39 for aggregation."""
    x_0 = 81132 * 0.61087572
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14958 * 0.37002291
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96785 * 0.14219599
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46096 * 0.02801121
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47167 * 0.92928654
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40840 * 0.05217653
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40173 * 0.41936133
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74279 * 0.54279757
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39204 * 0.94048093
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98510 * 0.37383645
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46448 * 0.84460424
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40352 * 0.17834908
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94196 * 0.24924325
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57535 * 0.95324838
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26669 * 0.88646863
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73755 * 0.29887954
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67743 * 0.09937325
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23927 * 0.76083618
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72443 * 0.31053362
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53894 * 0.69171038
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90331 * 0.27768941
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88781 * 0.58235732
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21962 * 0.65586236
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73540 * 0.95127521
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71058 * 0.82063860
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34363 * 0.48869507
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85222 * 0.85393095
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54000 * 0.43110939
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53309 * 0.28466130
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20579 * 0.25458689
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52709 * 0.41679068
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62539 * 0.05110315
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16740 * 0.54164816
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43230 * 0.42669918
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6966 * 0.65370958
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14778 * 0.41114477
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30359 * 0.93014979
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34608 * 0.54268393
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30500 * 0.02421221
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54486 * 0.24503268
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 22238 * 0.12763655
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37269 * 0.86580021
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 86590 * 0.94836872
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 2883 * 0.03261414
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 93209 * 0.89437534
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'nibpezdj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0040():
    """Extended test 40 for aggregation."""
    x_0 = 68797 * 0.23205523
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70169 * 0.68033842
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36772 * 0.40154054
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35966 * 0.70459693
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41977 * 0.14479561
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76761 * 0.62001352
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35743 * 0.90162308
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2291 * 0.13282716
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23797 * 0.66229052
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12839 * 0.38872810
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2886 * 0.09371849
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10383 * 0.28842305
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81137 * 0.81385518
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19040 * 0.95085952
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72747 * 0.46678186
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71976 * 0.07287044
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53733 * 0.62960705
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75851 * 0.94824307
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10680 * 0.37219203
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12795 * 0.19193120
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59549 * 0.71237849
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43636 * 0.94200221
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92804 * 0.94838510
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9178 * 0.57541883
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'jdnspaxx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0041():
    """Extended test 41 for aggregation."""
    x_0 = 76182 * 0.87609444
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85001 * 0.38579022
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18992 * 0.75556011
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88104 * 0.43749116
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2489 * 0.85644825
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9423 * 0.18119607
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86706 * 0.09084606
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59080 * 0.92548930
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50971 * 0.28239323
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71028 * 0.87723289
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36887 * 0.63548771
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7306 * 0.86470697
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27299 * 0.63825701
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74874 * 0.43331965
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24120 * 0.78725133
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4160 * 0.36070957
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1348 * 0.19355611
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18649 * 0.09440836
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73250 * 0.21335469
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31818 * 0.37844764
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22232 * 0.24711355
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80603 * 0.88861987
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60249 * 0.67320881
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13759 * 0.99090097
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27327 * 0.40836492
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ieonccqf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0042():
    """Extended test 42 for aggregation."""
    x_0 = 7590 * 0.01820976
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24198 * 0.60175477
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98017 * 0.03421596
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6269 * 0.94112040
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37832 * 0.78745107
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15323 * 0.92055546
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14991 * 0.31796313
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29241 * 0.01958019
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52804 * 0.83588654
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12371 * 0.68130709
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24328 * 0.02728607
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7550 * 0.38113439
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33382 * 0.58146731
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83648 * 0.69005808
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66060 * 0.77224677
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47466 * 0.19913166
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 832 * 0.86506547
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38231 * 0.66991955
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46938 * 0.18610066
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41746 * 0.04148171
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79395 * 0.14254082
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60323 * 0.38049860
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51361 * 0.25509516
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39881 * 0.62350501
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30999 * 0.31357980
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51359 * 0.68932480
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83860 * 0.51007732
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'mvivxhrd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0043():
    """Extended test 43 for aggregation."""
    x_0 = 73096 * 0.76522837
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81431 * 0.38869535
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15815 * 0.18933488
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50591 * 0.38136467
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63226 * 0.89094011
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21961 * 0.25306285
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22158 * 0.98567225
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49006 * 0.02291733
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95518 * 0.26028188
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1690 * 0.65706443
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39558 * 0.24362335
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91695 * 0.76833005
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64822 * 0.85852375
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24854 * 0.93842442
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80099 * 0.00348697
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18901 * 0.87450078
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98365 * 0.96542754
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22964 * 0.87093270
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11340 * 0.11019985
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27535 * 0.13283485
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21114 * 0.72580481
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13206 * 0.10844648
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53272 * 0.40725476
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45058 * 0.06543190
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37363 * 0.73354586
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71380 * 0.26079206
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74809 * 0.17249689
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62001 * 0.59345465
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23038 * 0.35543011
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99066 * 0.69957968
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45649 * 0.39251372
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8267 * 0.71562505
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40617 * 0.76371605
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40354 * 0.41833659
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10826 * 0.56141234
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14068 * 0.55360174
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68319 * 0.22196542
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7516 * 0.97338257
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65821 * 0.28839178
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'lrtvclut').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0044():
    """Extended test 44 for aggregation."""
    x_0 = 43803 * 0.74102083
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91626 * 0.06871735
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14026 * 0.82916385
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26567 * 0.24113490
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1774 * 0.45682525
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11886 * 0.01189765
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45123 * 0.59882570
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30449 * 0.89179914
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31890 * 0.68501283
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46677 * 0.74285084
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8490 * 0.21344279
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81151 * 0.62349614
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75708 * 0.67811077
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65249 * 0.24203638
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16865 * 0.30766373
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38819 * 0.00577691
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4954 * 0.67051939
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88551 * 0.51559280
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61544 * 0.57511654
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36603 * 0.51312700
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87124 * 0.72402922
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'kqgeqyrv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0045():
    """Extended test 45 for aggregation."""
    x_0 = 97790 * 0.09584615
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33791 * 0.11741896
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33039 * 0.68036862
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78198 * 0.55693377
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73144 * 0.30445996
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40698 * 0.73373463
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7518 * 0.69637569
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24967 * 0.95966253
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8045 * 0.88388976
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38914 * 0.59029731
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11497 * 0.91034451
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69122 * 0.78612800
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89376 * 0.58298451
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46401 * 0.03671872
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73254 * 0.86662028
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70274 * 0.58643449
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40255 * 0.58673376
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 990 * 0.55885470
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34506 * 0.75080263
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57930 * 0.38312021
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24380 * 0.08100073
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78283 * 0.72470812
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58673 * 0.83771917
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11743 * 0.64584502
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98954 * 0.34982937
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98006 * 0.21400635
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43984 * 0.66578087
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65409 * 0.65846480
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36331 * 0.23804509
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12237 * 0.42819259
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32262 * 0.22229825
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76266 * 0.93595355
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32032 * 0.58715079
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78929 * 0.48817453
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74499 * 0.06930113
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26731 * 0.76847116
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40118 * 0.15189048
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92970 * 0.12708217
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34247 * 0.03575004
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7378 * 0.44005372
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 97288 * 0.84999323
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 10858 * 0.17637751
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14873 * 0.30478536
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 56422 * 0.72475012
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 38238 * 0.31708155
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 45758 * 0.66068936
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 60929 * 0.09555084
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 60023 * 0.79231423
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 73189 * 0.58676774
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 53706 * 0.53569073
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'mdkhjzls').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0046():
    """Extended test 46 for aggregation."""
    x_0 = 73197 * 0.44462000
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65339 * 0.33213815
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48865 * 0.82813088
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54196 * 0.01123647
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19634 * 0.86232847
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38215 * 0.57837279
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13287 * 0.60999674
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76982 * 0.55364209
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96824 * 0.33677640
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57817 * 0.10475622
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83469 * 0.12001331
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67919 * 0.77543293
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18548 * 0.98248091
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66988 * 0.87519830
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6870 * 0.97090877
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47035 * 0.36649243
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46888 * 0.89361702
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6347 * 0.54859416
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13782 * 0.25109716
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93447 * 0.98947853
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29410 * 0.12163862
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67540 * 0.13170796
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73904 * 0.96804485
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79333 * 0.78637524
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'oypvyhpm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0047():
    """Extended test 47 for aggregation."""
    x_0 = 46305 * 0.74297395
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 164 * 0.39618302
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14417 * 0.32434955
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61004 * 0.55674518
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97371 * 0.60718907
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48931 * 0.04811625
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27153 * 0.92574936
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73064 * 0.08045303
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63613 * 0.18237608
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72330 * 0.59321566
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76886 * 0.09542980
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89140 * 0.15602413
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42266 * 0.90127417
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94596 * 0.23759936
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56520 * 0.37407107
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31701 * 0.18685070
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89474 * 0.86363280
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77350 * 0.92670096
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77782 * 0.13280195
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12878 * 0.61614888
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18718 * 0.39072441
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22520 * 0.61166568
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84179 * 0.60753443
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27930 * 0.15783231
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32193 * 0.02744487
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71204 * 0.85891545
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74615 * 0.24874900
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5993 * 0.34608426
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2165 * 0.19117879
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60847 * 0.88694944
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83139 * 0.10892576
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80607 * 0.47084315
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10307 * 0.27648422
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23514 * 0.48803916
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11695 * 0.07352732
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65628 * 0.29097164
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19018 * 0.29127477
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17555 * 0.52393573
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 54387 * 0.18334266
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29789 * 0.78718501
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2552 * 0.55509905
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22150 * 0.17619715
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'tcrnbaql').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0048():
    """Extended test 48 for aggregation."""
    x_0 = 9580 * 0.76990838
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88134 * 0.21048114
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15849 * 0.78852834
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74152 * 0.51370490
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70354 * 0.54930815
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84417 * 0.43623579
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59411 * 0.03044754
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23639 * 0.18258870
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93788 * 0.32216044
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13435 * 0.12642488
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86416 * 0.33457145
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26855 * 0.70516149
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36883 * 0.85749945
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66306 * 0.57076379
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75370 * 0.24163288
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18589 * 0.09401706
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28554 * 0.71284336
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55485 * 0.08811435
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91992 * 0.94783411
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89054 * 0.16983675
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85399 * 0.03955384
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66645 * 0.55547074
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91433 * 0.00228847
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21471 * 0.48620339
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88813 * 0.36330906
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9431 * 0.37826334
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2973 * 0.26398672
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99097 * 0.71555105
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31934 * 0.97134822
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55531 * 0.34273429
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27308 * 0.38167541
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36245 * 0.91578328
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73401 * 0.66357506
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13792 * 0.12224599
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81901 * 0.42489066
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26564 * 0.77092235
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79299 * 0.58745869
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 57791 * 0.93577028
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74973 * 0.83420333
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24359 * 0.87385560
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6718 * 0.65335602
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67807 * 0.94359546
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 76306 * 0.99436466
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97306 * 0.66944941
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 20920 * 0.11730648
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 99849 * 0.84047011
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 1779 * 0.51300314
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 3224 * 0.15465981
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 81644 * 0.93515438
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'pjxpdpcp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0049():
    """Extended test 49 for aggregation."""
    x_0 = 31500 * 0.69319544
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45668 * 0.81846699
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17164 * 0.52782274
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77018 * 0.63637072
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60347 * 0.09525619
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45324 * 0.35191561
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44812 * 0.13368408
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50239 * 0.55113722
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5022 * 0.10150071
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83498 * 0.13781338
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35127 * 0.72390849
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68253 * 0.95717850
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83425 * 0.64459896
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19694 * 0.02122321
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5069 * 0.61912472
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9581 * 0.43012023
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41182 * 0.06595133
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24575 * 0.95741334
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77860 * 0.58201426
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39890 * 0.45646702
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'uppvkojp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0050():
    """Extended test 50 for aggregation."""
    x_0 = 51677 * 0.44462855
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68398 * 0.75520326
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 131 * 0.18006888
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64628 * 0.32488767
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81439 * 0.26118268
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62955 * 0.38174976
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3010 * 0.67307848
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36615 * 0.11262252
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83252 * 0.46954094
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78981 * 0.80003800
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97513 * 0.47333409
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82068 * 0.96304847
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77280 * 0.57607616
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38164 * 0.79230295
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50151 * 0.36771395
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39405 * 0.22787671
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97552 * 0.99763006
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72365 * 0.79604131
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88258 * 0.02447858
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37426 * 0.86464071
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36031 * 0.30927860
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53691 * 0.90251616
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77163 * 0.46265181
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96847 * 0.65514123
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4438 * 0.46379561
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80325 * 0.72243244
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50662 * 0.38924626
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90264 * 0.09197646
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59756 * 0.70822016
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84791 * 0.65054215
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85438 * 0.19444876
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21012 * 0.26574033
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30427 * 0.66163526
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36501 * 0.83334248
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1665 * 0.52284431
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17776 * 0.52268225
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31672 * 0.08709157
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12661 * 0.84705626
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24809 * 0.89544158
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19281 * 0.81844002
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69017 * 0.89791928
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18797 * 0.78839125
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81108 * 0.66203519
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20270 * 0.33962482
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 73050 * 0.04691939
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 9964 * 0.71575248
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 16995 * 0.19051633
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 6941 * 0.44069807
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 17050 * 0.70049930
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 56066 * 0.53955842
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'xtrfmwlc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0051():
    """Extended test 51 for aggregation."""
    x_0 = 95269 * 0.07077940
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3140 * 0.98818920
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61442 * 0.60830732
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16174 * 0.01175962
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65535 * 0.21621564
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42603 * 0.00507042
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55231 * 0.04347109
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26295 * 0.73285824
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66329 * 0.92294983
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6220 * 0.39758757
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40961 * 0.42349432
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25302 * 0.85989754
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56638 * 0.71623891
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77752 * 0.53369675
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51694 * 0.27841411
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79516 * 0.23862215
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31232 * 0.63944280
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54578 * 0.47788003
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50503 * 0.46386642
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82726 * 0.70390707
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62720 * 0.59952770
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70470 * 0.64031751
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97038 * 0.91770946
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52913 * 0.04909613
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31533 * 0.25932578
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77641 * 0.55322284
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25088 * 0.36689497
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93426 * 0.33986934
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55809 * 0.52731487
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95073 * 0.54642860
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96498 * 0.56025009
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22652 * 0.39650116
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11866 * 0.21596028
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98278 * 0.97981452
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39959 * 0.20524272
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11459 * 0.00437784
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14330 * 0.25390789
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12517 * 0.94013085
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8084 * 0.71307463
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97387 * 0.84996910
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79497 * 0.67735990
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53494 * 0.52565619
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47311 * 0.63190836
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 55680 * 0.64717032
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50205 * 0.67776381
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 53467 * 0.75606536
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 84816 * 0.77380768
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 81917 * 0.41781641
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 57644 * 0.04377488
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'hmpmittb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0052():
    """Extended test 52 for aggregation."""
    x_0 = 45696 * 0.46722597
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17402 * 0.38905102
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30696 * 0.64250644
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91780 * 0.20138502
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3771 * 0.40997407
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92836 * 0.32841598
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47793 * 0.05292934
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26667 * 0.25426499
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14063 * 0.73589572
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52934 * 0.32201217
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1027 * 0.39144341
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24 * 0.46817828
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48564 * 0.26112887
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77140 * 0.93460459
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13691 * 0.32682598
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85259 * 0.20026832
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94920 * 0.24110257
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26123 * 0.29992415
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29163 * 0.03968962
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84784 * 0.88104214
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93766 * 0.40931341
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62911 * 0.36928225
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78600 * 0.41234286
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7707 * 0.07497044
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'qyqiighw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0053():
    """Extended test 53 for aggregation."""
    x_0 = 68250 * 0.43117739
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21072 * 0.83446773
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19724 * 0.70452726
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98075 * 0.92443749
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98023 * 0.01669615
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34927 * 0.36695771
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86530 * 0.54954096
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77307 * 0.06965097
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43846 * 0.06248523
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59062 * 0.11763924
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80076 * 0.70760231
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33768 * 0.89520338
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46537 * 0.60393681
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98818 * 0.34041577
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85156 * 0.59666344
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44623 * 0.23898177
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30603 * 0.76506226
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62872 * 0.90157404
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13650 * 0.93481546
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23803 * 0.08509496
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35348 * 0.28632884
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68481 * 0.34480337
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24217 * 0.32709158
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6268 * 0.09039698
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72662 * 0.42124298
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5727 * 0.28272202
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11757 * 0.08058729
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12016 * 0.99780317
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75767 * 0.26119645
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14100 * 0.02541893
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'xjrtkfnj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0054():
    """Extended test 54 for aggregation."""
    x_0 = 48985 * 0.24500717
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32991 * 0.77900624
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39840 * 0.41612979
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17657 * 0.62612464
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43537 * 0.10596836
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61450 * 0.49026945
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51126 * 0.63006022
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6680 * 0.96238243
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19551 * 0.00092454
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78411 * 0.46242078
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29158 * 0.02780237
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89637 * 0.15792539
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72593 * 0.02144874
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75906 * 0.00666139
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43079 * 0.94295043
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45649 * 0.48893953
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44285 * 0.45405643
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22918 * 0.78129055
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15506 * 0.90017542
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20919 * 0.08702144
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69921 * 0.88502750
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90902 * 0.45651585
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22481 * 0.01134673
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36893 * 0.77575948
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22985 * 0.75629500
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18213 * 0.90274867
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80922 * 0.09834438
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58376 * 0.25703092
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48044 * 0.45699871
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15798 * 0.75703844
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78222 * 0.94080838
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98418 * 0.04673690
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58753 * 0.08810874
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12408 * 0.60280351
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44590 * 0.98553636
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16413 * 0.56054271
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73219 * 0.95942837
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4356 * 0.78815598
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84286 * 0.19555959
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25718 * 0.55219919
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'sudpoxwd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0055():
    """Extended test 55 for aggregation."""
    x_0 = 78876 * 0.63587149
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45192 * 0.63869830
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54995 * 0.26485627
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31181 * 0.41227752
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71853 * 0.80903071
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50843 * 0.24156790
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66144 * 0.08025922
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49 * 0.49414184
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65020 * 0.87785255
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95698 * 0.93477805
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71857 * 0.63979739
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7694 * 0.03857724
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78014 * 0.93457885
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38880 * 0.61403010
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96685 * 0.35450030
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29084 * 0.92013170
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26782 * 0.29179776
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66721 * 0.50751550
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36909 * 0.72752772
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85672 * 0.59165716
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55992 * 0.99771713
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99710 * 0.03094235
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33009 * 0.93671426
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39422 * 0.39675681
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84258 * 0.06890421
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88573 * 0.83573657
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45322 * 0.03216055
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98119 * 0.40075259
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7634 * 0.02508351
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40943 * 0.65400071
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35494 * 0.57057158
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80610 * 0.19908370
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50517 * 0.80468595
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'sncnknyo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0056():
    """Extended test 56 for aggregation."""
    x_0 = 17245 * 0.37768458
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53418 * 0.20300924
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4055 * 0.93020046
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97843 * 0.36721863
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87278 * 0.04447513
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81230 * 0.33620088
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40190 * 0.35813318
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30853 * 0.95285458
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91459 * 0.59358642
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28188 * 0.27434931
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82097 * 0.62037863
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99315 * 0.01051404
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18198 * 0.45167023
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71478 * 0.77364001
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81056 * 0.83265786
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68916 * 0.05588489
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9083 * 0.68890505
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97429 * 0.28132931
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20612 * 0.57123736
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4713 * 0.93661925
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13237 * 0.97922117
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'itdbnhmq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0057():
    """Extended test 57 for aggregation."""
    x_0 = 37471 * 0.53663285
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84727 * 0.65404307
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71089 * 0.20692519
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96012 * 0.89441945
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51790 * 0.82056257
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68058 * 0.76116204
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62315 * 0.45380452
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93983 * 0.83680431
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80627 * 0.29165144
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90670 * 0.68079923
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7874 * 0.88967098
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59553 * 0.63802470
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50359 * 0.14663463
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10030 * 0.51266354
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91624 * 0.54232204
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55080 * 0.07170657
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22147 * 0.14210733
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99338 * 0.56885780
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44832 * 0.73581785
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98778 * 0.27944036
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45934 * 0.88962380
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1554 * 0.04554868
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99272 * 0.92687056
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62748 * 0.06297642
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6933 * 0.66548877
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73059 * 0.40077506
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39092 * 0.30792578
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 272 * 0.40516604
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78151 * 0.88055815
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50702 * 0.84207961
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42776 * 0.58723781
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15215 * 0.16701526
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18465 * 0.75669653
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93537 * 0.18376850
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72227 * 0.92606516
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25497 * 0.86112304
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20848 * 0.29598492
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48002 * 0.10326053
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 89323 * 0.32985609
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70961 * 0.77399248
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 97933 * 0.04271810
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79888 * 0.42680741
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35118 * 0.88861779
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61604 * 0.45099511
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 30274 * 0.05827672
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 29104 * 0.97251103
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 59339 * 0.80798352
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 45418 * 0.55730125
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 16387 * 0.80548878
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'ljrcloqh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0058():
    """Extended test 58 for aggregation."""
    x_0 = 50131 * 0.81888126
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35732 * 0.64722139
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42658 * 0.83364035
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14941 * 0.44525252
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33577 * 0.72635092
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88125 * 0.00357544
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14354 * 0.48529629
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69323 * 0.60901934
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26869 * 0.50664670
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24191 * 0.88978001
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59562 * 0.05556520
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68882 * 0.54061585
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13549 * 0.81834643
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36756 * 0.77667803
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22200 * 0.73243443
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29766 * 0.35794598
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54511 * 0.10786986
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83765 * 0.04591325
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52603 * 0.52192980
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41924 * 0.88874331
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55524 * 0.79707527
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23936 * 0.31268441
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22333 * 0.32373598
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27770 * 0.98627143
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21815 * 0.33554486
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19550 * 0.02854118
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25853 * 0.00886824
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89068 * 0.22519919
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'fxqkiykl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0059():
    """Extended test 59 for aggregation."""
    x_0 = 89086 * 0.54625016
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86932 * 0.06835006
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2663 * 0.08252190
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18590 * 0.43941774
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9616 * 0.00102641
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51511 * 0.28594124
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42786 * 0.16193687
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84830 * 0.48994464
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79359 * 0.75347321
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89763 * 0.27091408
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17716 * 0.48437926
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15682 * 0.16550390
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95225 * 0.27060974
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15522 * 0.89036961
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18889 * 0.01462930
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85072 * 0.82447115
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96658 * 0.96180874
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14456 * 0.49739551
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47507 * 0.25807441
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91833 * 0.10055004
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70399 * 0.10895241
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29498 * 0.45173662
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55844 * 0.30777978
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55973 * 0.67223006
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ymaykvaa').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0060():
    """Extended test 60 for aggregation."""
    x_0 = 43959 * 0.78353075
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10796 * 0.39739488
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8379 * 0.87895074
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26351 * 0.77832926
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19957 * 0.70799750
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8486 * 0.00321370
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46952 * 0.57241620
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77981 * 0.45443347
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3593 * 0.50411044
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90403 * 0.05540794
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58535 * 0.00601437
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46993 * 0.07968353
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18695 * 0.12172054
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30617 * 0.23714251
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94762 * 0.20378121
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94987 * 0.50276554
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5411 * 0.87701106
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42621 * 0.60589817
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75198 * 0.17769049
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38934 * 0.23502807
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52835 * 0.09227315
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42422 * 0.10428624
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39730 * 0.70527849
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51858 * 0.66158665
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18729 * 0.93115809
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47332 * 0.95033514
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27220 * 0.79579630
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97374 * 0.58066715
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9731 * 0.34341794
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21141 * 0.73446192
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39728 * 0.40888040
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'sjoqqxoj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0061():
    """Extended test 61 for aggregation."""
    x_0 = 43625 * 0.61784396
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34720 * 0.97818169
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98145 * 0.85163411
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80157 * 0.25983768
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55595 * 0.20336013
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16092 * 0.85307656
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54730 * 0.79810509
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52474 * 0.38386744
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38300 * 0.46799072
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39950 * 0.78755148
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92978 * 0.68983891
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53222 * 0.52431189
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29343 * 0.57390127
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77111 * 0.25316017
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31108 * 0.87654436
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33218 * 0.38538476
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59425 * 0.09038940
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8432 * 0.68111359
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10846 * 0.72342375
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43704 * 0.76071679
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16433 * 0.98580950
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53111 * 0.29926924
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72750 * 0.34578902
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23713 * 0.53250627
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44263 * 0.39935774
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81411 * 0.80244400
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13751 * 0.74464553
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67228 * 0.05442637
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35693 * 0.46050972
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65980 * 0.30145352
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 246 * 0.38281689
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54037 * 0.84737650
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75148 * 0.56582241
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59251 * 0.86802609
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18025 * 0.65889544
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27822 * 0.04143295
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78111 * 0.89141977
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13813 * 0.09051852
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81124 * 0.32290089
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33823 * 0.16945005
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'lnlsnbpm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0062():
    """Extended test 62 for aggregation."""
    x_0 = 92562 * 0.45306958
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96794 * 0.73063386
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27336 * 0.93490779
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54352 * 0.78197166
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57044 * 0.67897821
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84769 * 0.55590164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53947 * 0.54440762
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22519 * 0.11512173
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9441 * 0.68419496
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1018 * 0.43644699
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91406 * 0.30819459
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12346 * 0.76068923
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58374 * 0.34964971
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65965 * 0.67703268
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43500 * 0.10611287
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92855 * 0.78551001
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32337 * 0.03420587
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34089 * 0.78549236
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52473 * 0.83231441
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43277 * 0.64252883
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99115 * 0.89725607
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91040 * 0.80107431
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26940 * 0.40374289
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'mxftcbhk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0063():
    """Extended test 63 for aggregation."""
    x_0 = 1745 * 0.94956780
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37729 * 0.56684786
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63817 * 0.53471272
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49692 * 0.71769651
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63731 * 0.33110364
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11606 * 0.23143407
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57837 * 0.99818223
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45265 * 0.52884414
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24320 * 0.99666436
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44284 * 0.94132611
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14443 * 0.78739500
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64597 * 0.48300990
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54593 * 0.32462922
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30258 * 0.82153771
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87181 * 0.29370880
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58131 * 0.16310155
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85139 * 0.92064478
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47600 * 0.46879055
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58003 * 0.05695688
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77687 * 0.30057475
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74209 * 0.34133389
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85648 * 0.66313470
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90718 * 0.30690570
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7664 * 0.31138900
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18229 * 0.14887292
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73611 * 0.61667019
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21615 * 0.22214251
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'smpptqrj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0064():
    """Extended test 64 for aggregation."""
    x_0 = 66387 * 0.19511858
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4965 * 0.16559438
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38203 * 0.27729585
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39149 * 0.78349463
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42662 * 0.62634812
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67371 * 0.88728857
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34937 * 0.81325229
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51798 * 0.79963990
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55166 * 0.53170873
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82441 * 0.59644415
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57837 * 0.32251119
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88637 * 0.59030822
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65963 * 0.11136970
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61124 * 0.93281721
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29904 * 0.21439396
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54959 * 0.49302596
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77305 * 0.31019501
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91119 * 0.56748424
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72895 * 0.14717746
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31267 * 0.20123584
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51989 * 0.46759917
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71086 * 0.55537126
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53854 * 0.49811538
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73911 * 0.05144429
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98668 * 0.39390375
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66222 * 0.51069212
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5825 * 0.81444795
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38676 * 0.45900838
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29868 * 0.98137117
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10021 * 0.60201728
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86094 * 0.29525776
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43249 * 0.08431523
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84438 * 0.69898654
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8066 * 0.61260910
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98096 * 0.18225092
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65590 * 0.56625668
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73348 * 0.81014036
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'kmknunld').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0065():
    """Extended test 65 for aggregation."""
    x_0 = 61897 * 0.81854880
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10958 * 0.99765241
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51370 * 0.29155837
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69793 * 0.06131127
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7852 * 0.60070586
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74430 * 0.80592608
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18658 * 0.40211323
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25248 * 0.42142586
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77030 * 0.66177017
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77962 * 0.13980157
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50690 * 0.01166024
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 608 * 0.67652723
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5977 * 0.96573287
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1833 * 0.04871286
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59281 * 0.44101962
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83746 * 0.06245542
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17461 * 0.48311254
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42364 * 0.92613378
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13326 * 0.66030350
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13087 * 0.33875337
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68964 * 0.10168354
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70673 * 0.24155190
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61536 * 0.77749596
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67835 * 0.84518777
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20932 * 0.93595338
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59647 * 0.07667165
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74638 * 0.05377151
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57655 * 0.39843036
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8055 * 0.65149641
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15866 * 0.02806751
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26583 * 0.93090697
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59973 * 0.23569611
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71969 * 0.76911716
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38334 * 0.10625132
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'xnqbsrab').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0066():
    """Extended test 66 for aggregation."""
    x_0 = 73209 * 0.46481228
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33442 * 0.10611537
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80087 * 0.97279443
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 703 * 0.84781672
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47601 * 0.77098098
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98668 * 0.37810262
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8147 * 0.43580384
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91685 * 0.25735110
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2760 * 0.35208971
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10904 * 0.05077571
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16613 * 0.62057228
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84283 * 0.88535765
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5262 * 0.82897612
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3566 * 0.05189799
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99942 * 0.74957666
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6195 * 0.59654586
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59261 * 0.29652991
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51362 * 0.45239076
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88845 * 0.11373176
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27767 * 0.98824093
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45517 * 0.78940635
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16564 * 0.89064124
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57161 * 0.16250556
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42143 * 0.23756372
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99248 * 0.30611629
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5482 * 0.11057808
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5788 * 0.10290655
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61966 * 0.89312372
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39805 * 0.18173811
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17518 * 0.21805212
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61703 * 0.78315712
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19911 * 0.92168403
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77390 * 0.70113719
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47057 * 0.13222997
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76559 * 0.71699987
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77520 * 0.51339906
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30103 * 0.94405340
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2783 * 0.08030606
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79832 * 0.36365689
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52304 * 0.03013016
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37637 * 0.39971564
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15308 * 0.33726485
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88834 * 0.38643303
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 74853 * 0.87414941
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 19675 * 0.06941717
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 47348 * 0.64654356
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 46523 * 0.67185184
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'umgfwrwa').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0067():
    """Extended test 67 for aggregation."""
    x_0 = 27589 * 0.11170815
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89569 * 0.96669777
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12745 * 0.16144242
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41222 * 0.52433099
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76148 * 0.40256011
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26607 * 0.56857462
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60180 * 0.34268958
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20897 * 0.11517222
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36449 * 0.76231963
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67308 * 0.36751562
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31595 * 0.51376224
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69390 * 0.68503677
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56198 * 0.60204556
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62579 * 0.65666006
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21408 * 0.21246456
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46772 * 0.94217730
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57144 * 0.32495132
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68136 * 0.13038535
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79660 * 0.62359240
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72751 * 0.52536758
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9947 * 0.78587704
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6436 * 0.10205046
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77533 * 0.13597888
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43570 * 0.45679009
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48486 * 0.59984553
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3996 * 0.17569206
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'yisledla').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0068():
    """Extended test 68 for aggregation."""
    x_0 = 15426 * 0.82822727
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25712 * 0.79445017
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 794 * 0.59778807
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37018 * 0.27726529
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98639 * 0.80929179
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83202 * 0.59020903
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97861 * 0.85796241
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57056 * 0.75374300
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1105 * 0.90506632
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24379 * 0.53295257
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12126 * 0.82810455
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99353 * 0.38186501
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69376 * 0.33379919
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27476 * 0.61711329
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46637 * 0.70011095
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51057 * 0.20103917
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57630 * 0.84521948
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41623 * 0.53840304
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35828 * 0.73791035
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43007 * 0.76252875
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68852 * 0.96239170
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64044 * 0.89490219
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49287 * 0.40294186
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98430 * 0.76887187
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61123 * 0.22250824
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24095 * 0.04236180
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82338 * 0.06522436
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69221 * 0.45236148
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38818 * 0.13611325
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74728 * 0.18463428
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84056 * 0.25035080
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76826 * 0.05431310
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25838 * 0.25818160
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34948 * 0.75752006
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71224 * 0.13493339
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68056 * 0.78873315
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1605 * 0.27185592
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'xbvwwvtd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_9_0069():
    """Extended test 69 for aggregation."""
    x_0 = 1332 * 0.79113682
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72568 * 0.83220042
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20950 * 0.46166437
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58856 * 0.18773355
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23454 * 0.27800251
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44468 * 0.18663238
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82339 * 0.53563665
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12275 * 0.72963195
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44839 * 0.47520921
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86448 * 0.46158860
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98416 * 0.36285944
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80244 * 0.95042161
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65125 * 0.27113373
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18543 * 0.14578014
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79468 * 0.84412569
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2196 * 0.30467330
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65760 * 0.58628102
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96197 * 0.79012868
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66203 * 0.88862608
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39300 * 0.73093198
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59814 * 0.73196450
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19586 * 0.29568347
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63454 * 0.03473460
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58347 * 0.27234981
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33188 * 0.32579049
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2120 * 0.94362735
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13113 * 0.03023190
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9996 * 0.18531002
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59835 * 0.07484631
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16575 * 0.72720538
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11097 * 0.41335951
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59450 * 0.14955239
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64692 * 0.45754012
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35745 * 0.99827574
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48235 * 0.77255601
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50787 * 0.74736297
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60135 * 0.81013593
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47652 * 0.09136076
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42795 * 0.54465332
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57101 * 0.23884393
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69253 * 0.78751106
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 86451 * 0.56901496
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75321 * 0.87876057
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'keuejdbl').hexdigest()
    assert len(h) == 64
